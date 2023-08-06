Unix: |Unix Build Status| Windows: |Windows Build Status|\ Metrics:
|Coverage Status| |Scrutinizer Code Quality|\ Usage: |PyPI Version|
|PyPI Downloads|

Overview
========

Recommend songs to your friends and download their shared files to your
computer.

Features
--------

-  Recommend songs to your friends
-  Get a list of songs shared by your friends
-  Download the songs to your computer

|screenshot|

Setup
=====

Requirements
------------

-  Python 3.3+

Installation
------------

Install DropTheBeat with pip:

::

    $ pip install DropTheBeat

or directly from the source code:

::

    $ git clone https://github.com/jacebrowning/dropthebeat.git
    $ cd dropthebeat
    $ python setup.py install

Configuration
-------------

#. Create a folder named 'DropTheBeat' in your Dropbox
#. Share this folder with your friends

Usage
=====

Graphical Interface
-------------------

Start the application:

::

    $ DropTheBeat

Command-line Interface
----------------------

Create your user folder:

::

    $ dtb --new <"First Last">

Recommend a song to friends:

::

    $ dtb --share <path/to/a/song>
    $ dtb --share <path/to/a/song> --users "John Doe" "Jane Doe"

Display recommended songs:

::

    $ dtb --incoming
    $ dtb --outoing

Download recommended songs:

::

    $ dtb
    $ dtb --daemon

Launch the GUI:

::

    $ dtb --gui

.. |Unix Build Status| image:: http://img.shields.io/travis/jacebrowning/dropthebeat/develop.svg
   :target: https://travis-ci.org/jacebrowning/dropthebeat
.. |Windows Build Status| image:: https://img.shields.io/appveyor/ci/jacebrowning/dropthebeat/develop.svg
   :target: https://ci.appveyor.com/project/jacebrowning/dropthebeat
.. |Coverage Status| image:: http://img.shields.io/coveralls/jacebrowning/dropthebeat/develop.svg
   :target: https://coveralls.io/r/jacebrowning/dropthebeat
.. |Scrutinizer Code Quality| image:: http://img.shields.io/scrutinizer/g/jacebrowning/dropthebeat.svg
   :target: https://scrutinizer-ci.com/g/jacebrowning/dropthebeat/?branch=develop
.. |PyPI Version| image:: http://img.shields.io/pypi/v/DropTheBeat.svg
   :target: https://pypi.python.org/pypi/DropTheBeat
.. |PyPI Downloads| image:: http://img.shields.io/pypi/dm/DropTheBeat.svg
   :target: https://pypi.python.org/pypi/DropTheBeat
.. |screenshot| image:: https://github.com/jacebrowning/dropthebeat/blob/master/docs/assets/screenshot.png
