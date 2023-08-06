.PHONY: build clean upload install test

build:
	./build.sh

install:
	pip install -r requirements.txt

upload: clean
	rm -rf dist go_vncdriver.egg-info
	python setup.py sdist
	twine upload dist/*

clean:
	rm -rf *.so *.h *~

test:
	python -c 'import go_vncdriver; print(go_vncdriver.VNCSession)'
