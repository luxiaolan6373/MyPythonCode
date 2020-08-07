====================
downloadduxiu readme
====================
----------------------------------------
author: luoboiqingcai<sf.cumt@gmail.com>
----------------------------------------

About this package
===================

This downloadduxiu package is used to download books either from duxiu or from chaoxing if the book is accessable in your browsers.

It runs on Python 3 platform and rely on requests package, so download and install *python 3* and *requests* before running following commands.

Files
======
*downloadlib.py*

* --prex=prex :download directory, should be created before command runs.

* --logifle=logfile :logfile

* --procnum=1 :means how many threads will work to download pages

* --yourlink :the link you get from returned email.
 
::

    # prex direction must be created in order to execute this command.
    # on linux
    ./downloadlib.py --logfile=logfile --prex=prex --procnum=n duxiu_url "yourlink"
    # on windows
    downloadlib.py --logfile=logfile --prex=prex --procnum=n duxiu_url "yourlink"

*prefaces.py*

::

    # this script must be run first to prepare the prefaces before any images copyed to current direction.

    # on linux
    ./prefaces.py *.jpg *.png
    # on windows
    prefaces.py *.jpg *.png

*gui.py*

Deprecated. Don't run this script.
