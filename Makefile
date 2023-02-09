#/usr/bin/sh
# Build Arramooz: Arabic Dictionary for Morphological analysis - python + sqlite

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: install wheel doc

install:
	sudo python3 setup.py install
# Publish to github
publish:
	git push origin master 

md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst
md2html:
	pandoc -s -r markdown -w html README.md -o README.html
	
wheel:
	sudo python3 setup.py bdist_wheel
sdist:
	sudo python3 setup.py sdist
upload:
	echo "use twine upload dist/arramooz-pysqlite-0.1.tar.gz"
	
test:
	python3 -m unittest discover tests
doc:
	epydoc --config epydoc.conf
profile:
	cd tests;python3 -m cProfile -o output/profile test_dict2.py
 
