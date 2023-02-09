#!/usr/bin/python
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.md', encoding="utf8") as f:
        return f.read()
setup (name='arramooz_pysqlite', version='0.4',
      description='Arramooz: Arabic Dictionary for Morphological analysis - python + sqlite',
      long_description = readme(),  
      long_description_content_type='text/markdown',     

      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://arramooz-pysqlite.sourceforge.net/',
      license='GPL',
      Description="Arramooz; Arabic Dictionary for Morphological analysis - python + sqlite",
      package_dir={'arramooz': 'arramooz'},
      packages=['arramooz'],
      install_requires=[ 'pyarabic>=0.6.2',
      ],         
      include_package_data=True,
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

