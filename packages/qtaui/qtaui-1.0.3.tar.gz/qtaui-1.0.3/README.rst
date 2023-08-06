
qtaui
=====

qtaui - (c) Jérôme Laheurte 2015

.. contents:: **Table of contents**

What is qtaui ?
---------------

qtaui is a minimalist clone of wxPython's `wxaui <https://wiki.wxwidgets.org/WxAUI>`_. It allows a PySide-based program to arrange "frames", i.e. child widgets, in an arbitrary tree of splitters and tabs. The user can "undock" a frame and let it float as a top-level window, or drop it back onto the UI in a position that will create a new splitter or tabbed interface, or add it to an existing one.

This code is licensed under the `GNU LGPL version 3 or, at your
option, any later version
<https://www.gnu.org/copyleft/lesser.html>`_.

Supported platforms
-------------------

Python 2.7 with PySide 1.2.

Installation
------------

Using pip::

  $ pip install -U qtaui

From source::

  $ wget https://pypi.python.org/packages/source/q/qtaui/qtaui-1.0.3.tar.gz
  $ tar xjf qtaui-1.0.3.tar.bz2; cd qtaui-1.0.3
  $ sudo python ./setup.py install

API documentation
-----------------

The full documentation is hosted `here <http://qtaui.readthedocs.io/en/release-1.0.3/>`_.

Changelog
---------

Version 1.0.3:

- Fix addChild() signatures

Version 1.0.2:

- Another Pypi-related fix...

Version 1.0.1:

- Pypi-related fixes.

Version 1.0.0:

- First release.
