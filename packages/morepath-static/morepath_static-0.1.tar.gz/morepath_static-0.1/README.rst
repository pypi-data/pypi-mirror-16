Morepath_static
===============

Introduction
------------

This is a demo app for Morepath_ that illustrates how to serve static
resources. It uses the `More.static extension`_ to integrate BowerStatic_.

Getting started
---------------

To get started with this demo right away, you can install it and run it in
a newly created `virtual environment`_::

  $ virtualenv env
  $ ./env/bin/pip install morepath_static
  $ ./env/bin/morepath_static

You can now access the app at http://localhost:5000.


Installation from sources
-------------------------

You can grab the sources from GitHub_ and set them up in a fresh `virtual environment`_::

  $ git clone https://github.com/morepath/morepath_static.git
  $ cd morepath_static
  $ virtualenv env
  $ ./env/bin/pip install -e '.[test]'

You'll then be able to start the app::

  $ ./env/bin/morepath_static

And to run the test suite::

  $ ./env/bin/py.test -v


.. _Morepath: http://morepath.readthedocs.io/

.. _more.static extension: http://morepath.readthedocs.io/en/latest/more.static.html

.. _BowerStatic: http://bowerstatic.readthedocs.io

.. _GitHub: https://github.com/morepath/morepath_static

.. _virtual environment: http://www.virtualenv.org/
