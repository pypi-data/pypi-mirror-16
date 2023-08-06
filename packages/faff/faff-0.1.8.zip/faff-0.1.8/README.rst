Faff
====

.. image:: https://img.shields.io/pypi/v/faff.svg?style=flat-square
    :target: https://pypi.python.org/pypi/faff

.. image:: https://img.shields.io/pypi/status/faff.svg?style=flat-square
    :target: https://pypi.python.org/pypi/faff

.. image:: https://img.shields.io/pypi/l/faff.svg?style=flat-square
    :target: https://pypi.python.org/pypi/faff

.. image:: https://img.shields.io/travis/mojzu/faff/master.svg?style=flat-square
    :target: http://travis-ci.org/mojzu/faff

.. image:: https://img.shields.io/coveralls/mojzu/faff.svg?style=flat-square
    :target: https://coveralls.io/github/mojzu/faff

Faff is a Make build tool substitute written in Python. Input files similar
to ``Makefile``'s define rules which are used to build arbitrary targets that
may have dependencies.

Installation
------------

Install using pip.

.. code:: shell

  $ pip install faff

Quickstart
----------

Create a file in a new directory called ``faffin.py``.

.. code:: shell

  $ mkdir -p DIR && cd DIR
  $ touch faffin.py

Content of ``faffin.py`` file.

.. code:: python

  #!/usr/bin/env python
  # -*- coding: utf-8 -*-
  import os
  from faff import (Variable, FileTarget, Rule, Run)

  # Absolute path to directory.
  root = os.path.abspath(os.path.dirname(__file__))

  # Root variable definition.
  Variable("ROOT", root)

  # File targets with path variable expansion.
  SOURCE = FileTarget("{ROOT}", "main.c")
  BINARY = FileTarget("{ROOT}", "main")

  # Compile and run binary rule.
  @Rule([BINARY, SOURCE])
  def all(target, depends, args):
      Run("gcc {_D} -o {_T}", root)
      Run("main", root)

TODO

Documentation
-------------

TODO
