#! /usr/bin/python
from distutils.core import setup
from glob import glob

# to install type:
# python setup.py install --root=/

setup (name='arramooz-pysqlite', version='0.1',
      description='Arramooz: Arabic Dictionary for Morphological analysis - python + sqlite',
      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://arramooz-pysqlite.sourceforge.net/',
      license='GPL',
      Description="Arramooz; Arabic Dictionary for Morphological analysis - python + sqlite",
      package_dir={'arramooz': 'arramooz'},
      packages=['arramooz'],
      # include_package_data=True,
      package_data = {
        'arramooz': ['doc/*.*','doc/html/*', 'data/*.sqlite', 'data/*.sql'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );

