.PHONY: lint install

lint:
	pylint ./wke_cloudlab

install:
	pip install .
