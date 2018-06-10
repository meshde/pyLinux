# -*- coding: utf-8 -*-
"""\
=======
pyLinux
=======

A python wrapper over the Linux C library
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

from setuptools import setup, find_packages
import os, sys

version = '1.0.0.dev0'

this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',),
                               ('doc', 'contributors.rst'),
                               ('doc', 'changes.rst'))]
    )
dev_require = ['Sphinx']
dev_require += ['nose', 'coverage']
if sys.version_info < (2, 7):
    dev_require += ['unittest2']


setup(name='pyLinux',
      version=version,
      description="A python wrapper over the Linux C library",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
          ],
      keywords='',  # FIXME: Add whatefer fits
      author='Mehmood Deshmukh',
      author_email='meshde.md@gmail.com',
      url='http://pypi.python.org/pypi/pyLinux',
      license='GPLv3',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools'
          # Others
          ],
      entry_points={
          },
      tests_require=dev_require,
      test_suite='nose.collector',
      extras_require={
          'dev': dev_require
      })
