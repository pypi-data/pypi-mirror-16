
all: prepare

prepare: res_src/resources.qrc
	pyside-rcc -o qtaui/resources.py res_src/resources.qrc
	python ./prepare.py

documentation: prepare
	cd doc; $(MAKE) html
	rm -rf html
	mv doc/_build/html .

lint:
	-python -mpylint qtaui > lint.html
	open lint.html

nuke:
	hg purge --all

tarball: documentation
	python setup.py sdist --formats=bztar

release: documentation
	python ./setup.py sdist upload -r pypi
