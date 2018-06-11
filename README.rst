=======
pyLinux
=======

A python wrapper for the Linux C library (glibc) and other Linux functionalities (e.g. cgroups).

The package mainly includes the Linux functionalities that are not available through the python os package. The package was created to facilitate the creation of Linux Containers in python, so as of now consists of those functionalities needed for this particular function only.

If you come across other Linux system calls/functionalities that cannot be invoked using the python os package, please open an issue_

Functionalities Included
========================

- clone
- mount
- umount
- unshare
- setns
- sethostname
- cgroups

TODO
====

- capabilities?
- Documentation

Full documentation and API
==========================

Full Documentation yet to be created. (Sorry about that!)

Developer notes
===============

Please use a virtualenv to maintain this package, but I should not need to say that.

Grab the source from the SCM repository:

.. code:: console

  $ python setup.py develop
  $ pip install pyLinux[dev]

Run the tests:

.. code:: console

  $ nosetests

Build the Sphinx documentation:

.. code:: console

  $ python setup.py build_sphinx
  $ firefox build/sphinx/html/index.html

Links
=====

FIXME: Provide real links

Project home page

  http://www.mystuff.com/project

Source code

  http://www.mystuff.com/source

Issues tracker

  https://github.com/meshde/pyLinux/issues

.. _issue: https://github.com/meshde/pyLinux/issues
