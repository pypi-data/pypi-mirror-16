package main

/*
#cgo pkg-config: python2
#define Py_LIMITED_API
#include <Python.h>
#include <stdlib.h>
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

PyObject *get_go_vncdriver_VNCSession_type();
void PyErr_SetGoVNCDriverError(char* msg);

static PyObject *GoPyArray_SimpleNew(int nd, npy_intp* dims, int typenum) {
    return PyArray_SimpleNew(nd, dims, typenum);
}

static PyObject *GoPyArray_SimpleNewFromData(int nd, npy_intp* dims, int typenum, void *data) {
  return PyArray_SimpleNewFromData(nd, dims, typenum, data);
}

// Workaround missing variadic function support
// https://github.com/golang/go/issues/975
static int PyArg_ParseTuple_LL(PyObject *args, long long *a, long long *b) {
    return PyArg_ParseTuple(args, "LL", a, b);
}

static int PyArg_ParseTuple_OO(PyObject *args, PyObject **a, PyObject **b) {
    return PyArg_ParseTuple(args, "O!O", &PyList_Type, a, b);
}

static PyObject *PyTuple_Pack_2(PyObject *a, PyObject *b) {
    return PyTuple_Pack(2, a, b);
}

static PyObject *PyObject_CallFunctionObjArgs_1(PyObject *callable, PyObject *a) {
    return PyObject_CallFunctionObjArgs(callable, a, NULL);
}

typedef struct {
      PyObject_HEAD
      PyObject *remotes;
} go_vncdriver_VNCSession_object;

// Can't access macros through cgo
static void go_vncdriver_decref(PyObject *obj) {
    Py_DECREF(obj);
}

static void go_vncdriver_incref(PyObject *obj) {
    Py_INCREF(obj);
}
*/
import "C"
import (
	"sync"
	"unsafe"

	"github.com/juju/errors"
	"github.com/op/go-logging"
	"github.com/openai/gym-vnc/go-vncdriver/gymvnc"
)

var (
	log     = logging.MustGetLogger("go_vncdriver")
	data    = [1024 * 768 * 3]uint8{}
	Py_None = &C._Py_NoneStruct
)

var vncUpdatesN = C.PyString_FromString(C.CString("vnc.updates.n"))

type batchInfo struct {
	done  chan bool
	batch *gymvnc.VNCBatch

	screenPylist      *C.PyObject
	infoPylist        *C.PyObject
	infoPydicts       []*C.PyObject
	screenInfoPytuple *C.PyObject
	screenNumpy       map[*gymvnc.Screen]*C.PyObject
}

// Sets the Python error for you
func (b *batchInfo) populateScreenPylist(screens []*gymvnc.Screen) bool {
	for i, screen := range screens {
		ary, ok := b.screenNumpy[screen]
		if !ok {
			err := errors.Errorf("missing Numpy object for screen: %d", i)
			setError(errors.ErrorStack(err))
			return false
		}

		C.go_vncdriver_incref(ary)
		if C.PyList_SetItem(b.screenPylist, C.Py_ssize_t(i), ary) == C.int(-1) {
			return false
		}
	}
	return true
}

// Preallocate all needed Python objects, so we don't need to
// generate a lot of garbage.
func (b *batchInfo) preallocatePythonObjects() bool {
	// Create holder for info dictionaries. Populate those now.
	n := b.batch.N()
	b.infoPylist = C.PyList_New(C.Py_ssize_t(n))

	for i := 0; i < n; i++ {
		infoPydict := C.PyDict_New()
		b.infoPydicts = append(b.infoPydicts, infoPydict)

		if C.PyList_SetItem(b.infoPylist, C.Py_ssize_t(i), infoPydict) == C.int(-1) {
			return false
		}
	}

	// Create holder for numpy screens. Populate it at flip/peek
	// time using the front screens.
	b.screenPylist = C.PyList_New(C.Py_ssize_t(b.batch.N()))
	// Create numpy screens
	screens := append(b.batch.Peek(), b.batch.PeekBack()...)
	b.screenNumpy = make(map[*gymvnc.Screen]*C.PyObject)
	for _, screen := range screens {
		dims := []C.npy_intp{C.npy_intp(screen.Height), C.npy_intp(screen.Width), 3}
		ary := C.GoPyArray_SimpleNewFromData(3, &dims[0], C.NPY_UINT8, unsafe.Pointer(&screen.Data[0]))
		b.screenNumpy[screen] = ary
	}

	b.screenInfoPytuple = C.PyTuple_Pack_2(b.screenPylist, b.infoPylist)
	return true
}

var (
	batchMgr  = map[uintptr]batchInfo{}
	batchLock sync.Mutex
)

//export GoVNCDriver_VNCSession_c_init
func GoVNCDriver_VNCSession_c_init(self *C.go_vncdriver_VNCSession_object, args *C.PyObject) C.int {
	listObj := new(*C.PyObject)
	errorCallable := new(*C.PyObject)

	if C.PyArg_ParseTuple_OO(args, listObj, errorCallable) == 0 {
		return C.int(-1)
	}

	// Going to keep a pointer around
	C.go_vncdriver_incref(*errorCallable)

	remotes := []string{}
	size := C.PyList_Size(*listObj)
	for i := 0; i < int(size); i++ {
		// Look at the i'th item and convert to a Go string
		listItem := C.PyList_GetItem(*listObj, C.Py_ssize_t(i))
		strObj := C.PyString_AsString(listItem)
		str := C.GoString(strObj)
		remotes = append(remotes, str)
	}

	// Closer
	errCh := make(chan error, 10)
	done := make(chan bool)
	batch, err := gymvnc.NewVNCBatch(remotes, done, errCh)
	if err != nil {
		close(done)
		setError(errors.ErrorStack(err))
		return C.int(-1)
	}

	info := batchInfo{
		done:  done,
		batch: batch,
	}
	if err := info.initBatch(); err != nil {
		close(done)
		setError(errors.ErrorStack(err))
		return C.int(-1)
	}

	info.preallocatePythonObjects()
	go func() {
		select {
		case err := <-errCh:
			errString := C.CString(err.Error())

			var gstate C.PyGILState_STATE
			gstate = C.PyGILState_Ensure()
			pystring := C.PyString_FromString(errString)
			res := C.PyObject_CallFunctionObjArgs_1(*errorCallable, pystring)
			if res == nil {
				log.Infof("wasn't able to make python call with error: %s", err)
				C.PyErr_Print()
			}
			C.go_vncdriver_decref(pystring)
			C.PyGILState_Release(gstate)
			C.free(unsafe.Pointer(errString))

			GoVNCDriver_VNCSession_c_close(self)
		case <-done:
		}

		// And now its watch is done
		C.go_vncdriver_decref(*errorCallable)
	}()

	batchLock.Lock()
	defer batchLock.Unlock()

	ptr := uintptr(unsafe.Pointer(self))
	batchMgr[ptr] = info

	return C.int(0)
}

//export GoVNCDriver_VNCSession_render
func GoVNCDriver_VNCSession_render(self, args *C.PyObject) *C.PyObject {
	batchLock.Lock()
	defer batchLock.Unlock()

	ptr := uintptr(unsafe.Pointer(self))
	info, ok := batchMgr[ptr]
	if !ok {
		setError("No screens (perhaps you've already closed that VNCSession?)")
		return nil
	}

	err := info.batch.Render()
	if err != nil {
		setError(err.Error())
		return nil
	}

	C.go_vncdriver_incref(Py_None)
	return Py_None
}

//export GoVNCDriver_VNCSession_step
func GoVNCDriver_VNCSession_step(self, args *C.PyObject) *C.PyObject {
	batchLock.Lock()
	defer batchLock.Unlock()

	ptr := uintptr(unsafe.Pointer(self))
	info, ok := batchMgr[ptr]
	if !ok {
		setError("No screens (perhaps you've already closed that VNCSession?)")
		return nil
	}

	return flipHelper(info)
}

//export GoVNCDriver_VNCSession_flip
func GoVNCDriver_VNCSession_flip(self, args *C.PyObject) *C.PyObject {
	batchLock.Lock()
	defer batchLock.Unlock()

	ptr := uintptr(unsafe.Pointer(self))
	info, ok := batchMgr[ptr]
	if !ok {
		setError("No screens (perhaps you've already closed that VNCSession?)")
		return nil
	}

	return flipHelper(info)
}

//export GoVNCDriver_VNCSession_peek
func GoVNCDriver_VNCSession_peek(self, args *C.PyObject) *C.PyObject {
	batchLock.Lock()
	defer batchLock.Unlock()

	ptr := uintptr(unsafe.Pointer(self))
	info, ok := batchMgr[ptr]
	if !ok {
		setError("No screens (perhaps you've already closed that VNCSession?)")
		return nil
	}

	screens := info.batch.Peek()
	info.populateScreenPylist(screens)

	// Ownership will transfer away when we return
	C.go_vncdriver_incref(info.screenPylist)
	return info.screenPylist
}

//export GoVNCDriver_VNCSession_close
func GoVNCDriver_VNCSession_close(self, args *C.PyObject) *C.PyObject {
	// t := C.get_go_vncdriver_VNCSession_type()
	// check := C.PyObject_IsInstance(self, t)
	// if check == C.int(-1) {
	// 	return nil
	// } else if check == C.int(0) {
	// 	setError("Must pass an VNCSession instance")
	// 	return nil
	// }

	cast := (*C.go_vncdriver_VNCSession_object)(unsafe.Pointer(self))
	GoVNCDriver_VNCSession_c_close(cast)

	C.go_vncdriver_incref(Py_None)
	return Py_None
}

//export GoVNCDriver_VNCSession_c_close
func GoVNCDriver_VNCSession_c_close(self *C.go_vncdriver_VNCSession_object) {
	batchLock.Lock()
	defer batchLock.Unlock()

	ptr := uintptr(unsafe.Pointer(self))
	info, ok := batchMgr[ptr]
	if !ok {
		return
	}

	close(info.done)
	if info.screenInfoPytuple != nil {
		C.go_vncdriver_decref(info.screenInfoPytuple)
	}
	if info.infoPylist != nil {
		C.go_vncdriver_decref(info.infoPylist)
	}
	if info.screenPylist != nil {
		C.go_vncdriver_decref(info.screenPylist)
	}

	// Lists have taken ownership of our Numpy references and info
	// dictionaries
	// (https://docs.python.org/2.7/extending/extending.html#ownership-rules)
	delete(batchMgr, ptr)
}

//export GoVNCDriver_setup
func GoVNCDriver_setup(self, args *C.PyObject) *C.PyObject {
	gymvnc.ConfigureLogging()
	// Expansion of Py_None
	C.go_vncdriver_incref(Py_None)
	return Py_None
}

func flipHelper(info batchInfo) *C.PyObject {
	screens, updates := info.batch.Flip()
	if ok := info.populateScreenPylist(screens); !ok {
		return nil
	}

	for i, update := range updates {
		dict := info.infoPydicts[i]

		// Retain our reference!
		C.go_vncdriver_incref(vncUpdatesN)
		ok := C.PyDict_SetItem(dict, vncUpdatesN, C.PyInt_FromLong(C.long(len(update))))
		if ok != C.int(0) {
			return nil
		}
	}

	// Ownership will transfer away when we return
	C.go_vncdriver_incref(info.screenInfoPytuple)
	return info.screenInfoPytuple
}

func setError(str string) {
	C.PyErr_SetGoVNCDriverError(C.CString(str))
}

func main() {
}
