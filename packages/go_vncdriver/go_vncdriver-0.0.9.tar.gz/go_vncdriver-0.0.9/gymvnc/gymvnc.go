package gymvnc

import (
	"io"
	"net"
	"os/exec"
	"sync"
	"time"

	"github.com/juju/errors"
	"github.com/op/go-logging"
	"github.com/openai/gym-vnc/go-vncdriver/vncclient"
	"github.com/openai/gym-vnc/go-vncdriver/vncgl"
)

var log = logging.MustGetLogger("gymvnc")

type sessionMgr struct {
	Ready      sync.WaitGroup
	Done       chan bool
	Error      chan error
	Terminated sync.WaitGroup
}

func NewSessionMgr() *sessionMgr {
	return &sessionMgr{
		Done:  make(chan bool),
		Error: make(chan error, 1),
	}
}

func (s *sessionMgr) Close() {
	close(s.Done)
}

type VNCSession struct {
	address string
	mgr     *sessionMgr
	conn    *vnc.ClientConn

	render      *exec.Cmd
	renderStdin io.Writer

	frontScreen     *Screen
	backScreen      *Screen
	backUpdated     bool
	deferredUpdates []*vnc.FramebufferUpdateMessage
	lock            sync.Mutex

	vncgl *vncgl.VNCGL
}

func NewVNCSession(address string, mgr *sessionMgr) *VNCSession {
	c := &VNCSession{
		address:     address,
		mgr:         mgr,
		backUpdated: true,
	}
	c.start()
	return c
}

func (c *VNCSession) start() {
	updates := make(chan *vnc.FramebufferUpdateMessage, 4096)

	// Called from main thread. Will call Done once this session
	// is fully setup.
	c.mgr.Ready.Add(1)

	// Maintains the connection to the remote
	go func() {
		err := c.connect(updates)
		if err != nil {
			// Try reporting the error
			select {
			case c.mgr.Error <- err:
			default:
			}
		}
	}()
}

// Must call from main thread
func (c *VNCSession) Render() error {
	var err error
	if c.vncgl == nil {
		c.vncgl, err = vncgl.NewVNCGL(c.conn.FramebufferWidth, c.conn.FramebufferHeight, c.conn.DesktopName)
		if err != nil {
			return errors.Annotate(err, "could not render")
		}

		image := vncgl.ColorsToImage(0, 0, c.conn.FramebufferWidth, c.conn.FramebufferHeight, c.frontScreen.Data)
		c.vncgl.ApplyImage(image)
	}

	c.vncgl.Render()
	return nil
}

// If rendering, must call from main thread
func (c *VNCSession) Flip() (*Screen, []*vnc.FramebufferUpdateMessage) {
	c.lock.Lock()
	defer c.lock.Unlock()

	var updates []*vnc.FramebufferUpdateMessage

	if c.backUpdated {
		c.frontScreen, c.backScreen = c.backScreen, c.frontScreen
		c.backUpdated = false
		updates = c.deferredUpdates
		go func() {
			c.lock.Lock()
			defer c.lock.Unlock()

			c.applyDeferred()
		}()

		if c.vncgl != nil {
			// Keep the GL screen fed
			c.vncgl.Apply(updates)
		}
	}

	return c.frontScreen, updates
}

// Apply any deferred updates *while holding the lock*
func (c *VNCSession) applyDeferred() error {
	if c.backUpdated {
		return nil
	}
	c.backUpdated = true

	for _, update := range c.deferredUpdates {
		c.applyUpdate(update)
	}
	c.deferredUpdates = nil
	return nil
}

// Apply an update *while holding the lock*
func (c *VNCSession) applyUpdate(update *vnc.FramebufferUpdateMessage) error {
	var bytes uint32
	start := time.Now().UnixNano()
	for _, rect := range update.Rectangles {
		switch enc := rect.Enc.(type) {
		case *vnc.RawEncoding:
			bytes += c.applyRect(c.conn, rect, enc.Colors)
		case *vnc.ZRLEEncoding:
			bytes += c.applyRect(c.conn, rect, enc.Colors)
		default:
			return errors.Errorf("unsupported encoding: %T", enc)
		}
	}
	delta := time.Now().UnixNano() - start
	log.Debugf("[%s] Update complete: time=%dus type=%T rectangles=%+v bytes=%d", c.address, delta/1000, update, len(update.Rectangles), bytes)
	return nil
}

func (c *VNCSession) applyRect(conn *vnc.ClientConn, rect vnc.Rectangle, colors []vnc.Color) uint32 {
	var bytes uint32
	// var wg sync.WaitGroup
	// wg.Add(int(rect.Height))
	for y := uint32(0); y < uint32(rect.Height); y++ {
		// go func(y uint32) {
		encStart := uint32(rect.Width) * y
		encEnd := encStart + uint32(rect.Width)

		screenStart := uint32(conn.FramebufferWidth)*(uint32(rect.Y)+y) + uint32(rect.X)
		screenEnd := screenStart + uint32(rect.Width)

		bytes += encEnd - encStart
		copy(c.backScreen.Data[screenStart:screenEnd], colors[encStart:encEnd])
		// wg.Done()
		// }(y)
	}
	// wg.Wait()
	return bytes
}

func (c *VNCSession) maintainFrameBuffer(updates chan *vnc.FramebufferUpdateMessage) error {
	done := false

	// While the VNC protocol supports more exotic formats, we
	// only want straight RGB with 1 byte per color.
	c.frontScreen = NewScreen(c.conn.FramebufferWidth, c.conn.FramebufferHeight)
	c.backScreen = NewScreen(c.conn.FramebufferWidth, c.conn.FramebufferHeight)

	for {
		select {
		case update := <-updates:
			c.lock.Lock()
			if err := c.applyDeferred(); err != nil {
				c.lock.Unlock()
				return errors.Annotate(err, "when applying deferred updates")
			}

			if err := c.applyUpdate(update); err != nil {
				c.lock.Unlock()
				return errors.Annotate(err, "when applying new update")
			}
			c.deferredUpdates = append(c.deferredUpdates, update)
			c.lock.Unlock()
		case <-c.mgr.Done:
			log.Debugf("[%s] shutting down frame buffer thread", c.address)
			return nil
		}

		if !done {
			c.mgr.Ready.Done()
			done = true
		}
	}
}

func (c *VNCSession) connect(updates chan *vnc.FramebufferUpdateMessage) error {
	log.Infof("[%s] connecting", c.address)

	target, err := net.Dial("tcp", c.address)
	if err != nil {
		return errors.Annotate(err, "could not connect to server")
	}

	errorCh := make(chan error)
	serverMessageCh := make(chan vnc.ServerMessage)
	conn, err := vnc.Client(target, &vnc.ClientConfig{
		Auth: []vnc.ClientAuth{
			&vnc.PasswordAuth{
				Password: "openai",
			},
		},
		ServerMessageCh: serverMessageCh,
		ErrorCh:         errorCh,
	})
	if err != nil {
		return errors.Annotate(err, "could not establish VNC connection to server")
	}

	go func() {
		select {
		case err := <-errorCh:
			c.mgr.Error <- errors.Annotatef(err, "[%s] vnc error", c.address)
		case <-c.mgr.Done:
		}
	}()

	c.conn = conn
	log.Infof("[%s] connection established", c.address)

	// Spin up a screenbuffer thread
	go func() {
		err := c.maintainFrameBuffer(updates)
		if err != nil {
			// Report the error, if any
			select {
			case c.mgr.Error <- err:
			default:
			}
		}
	}()

	conn.SetPixelFormat(&vnc.PixelFormat{
		BPP:        32,
		Depth:      24,
		BigEndian:  false,
		TrueColor:  true,
		RedMax:     255,
		GreenMax:   255,
		BlueMax:    255,
		RedShift:   0,
		GreenShift: 8,
		BlueShift:  16,
	})

	conn.SetEncodings([]vnc.Encoding{
		&vnc.ZRLEEncoding{},
		&vnc.RawEncoding{},
	})

	conn.FramebufferUpdateRequest(true, 0, 0, conn.FramebufferWidth, conn.FramebufferHeight)

	for {
		select {
		case msg := <-serverMessageCh:
			log.Debugf("[%s] Just received: %T %+v", c.address, msg, msg)
			switch msg := msg.(type) {
			case *vnc.FramebufferUpdateMessage:
				updates <- msg
				// Keep re-requesting!
				conn.FramebufferUpdateRequest(true, 0, 0, conn.FramebufferWidth, conn.FramebufferHeight)
			}
		case <-c.mgr.Done:
			log.Debugf("[%s] terminating VNC connection", c.address)
			if err := conn.Close(); err != nil {
				return err
			}
			return nil
		}
	}
}

type VNCBatch struct {
	sessions []*VNCSession
}

func (v *VNCBatch) N() int {
	return len(v.sessions)
}

func (v *VNCBatch) Render() {
	v.sessions[0].Render()
}

func (v *VNCBatch) Flip() (screens []*Screen, updates [][]*vnc.FramebufferUpdateMessage) {
	for _, session := range v.sessions {
		screen, update := session.Flip()
		screens = append(screens, screen)
		updates = append(updates, update)
	}
	return
}

func (v *VNCBatch) Peek() (screens []*Screen) {
	for _, session := range v.sessions {
		screens = append(screens, session.frontScreen)
	}
	return
}

func (v *VNCBatch) PeekBack() (screens []*Screen) {
	for _, session := range v.sessions {
		screens = append(screens, session.backScreen)
	}
	return
}

func NewVNCBatch(remotes []string, done chan bool, errCh chan error) (*VNCBatch, error) {
	batch := VNCBatch{}
	mgr := NewSessionMgr()

	for _, address := range remotes {
		batch.sessions = append(batch.sessions, NewVNCSession(address, mgr))
	}

	allReady := make(chan bool)
	go func() {
		mgr.Ready.Wait()
		allReady <- true
	}()

	select {
	case <-allReady:
		go func() {
			select {
			case <-done:
				// Translate 'done' closing into closing down
				// this pipeline.
				close(mgr.Done)
			case err := <-mgr.Error:
				// Capture the relevant error, and let
				// the use know.
				errCh <- err
				close(mgr.Done)
			}
		}()

		return &batch, nil
	case err := <-mgr.Error:
		return nil, err
	case <-done:
		// upstream requested a cancelation
		mgr.Close()
		return nil, nil
	}
}
