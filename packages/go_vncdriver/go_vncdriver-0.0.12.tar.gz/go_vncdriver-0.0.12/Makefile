.PHONY: build clean upload install test

install:
	pip install -r requirements.txt

upload: clean
	rm -rf dist go_vncdriver.egg-info
	python setup.py sdist
	twine upload dist/*

clean:
	rm -rf *.so *.h *~

build:
	./build.sh

test:
	python -c 'import go_vncdriver; print(go_vncdriver.VNCSession)'
