.. downloadduxiu documentation master file, created by
   sphinx-quickstart on Wed Oct 10 14:23:37 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to downloadduxiu's documentation!
=========================================


Introduce to downloadduxiu
---------------------------
.. module:: downloadduxiu
   :platform: Unix, Windows
   :synopsis: to download papers from duxiu.
.. moduleauthor:: luoboiqingcai <sf.cumt@gmail.com>

This **downloadduxiu** package is used to download books either from duxiu or from chaoxing if the book is accessable in your browsers.

Install this package
---------------------

This package is quite simple and is not necessary to be installed.

Although some preparations are need:

 #. python 3 installed
 #. requests package installed
 #. reportlab installed if you want to use gendocument.py script


modules included in the package
================================

downloadlib
--------------

This is the main module of the package.

::

    # prex direction must be created in order to execute this command.
    ./downloadlib.py --prex=prex  --logfile=logfile duxiu_url "yourlink"

    # utilize multiprocess function
    ./downloadlib.py --prex=prex --logfile=logfile --procnum=2 duxiu_url "yourlink"


prefaces
---------

This script is used to preprocess the preface of the ducument in order to make it ordered to be inserted in the pdf document to be generated.

::

    # this script must be run first to prepare the prefaces before any images copyed to current direction.
    ./prefaces.py *.jpg *.png


gendocument
------------

This script is used to generate pdf document from images download by downloadduxiu ang prefaces download manually.

.. note::

    This script runs on python 2.7 because it requires reportlab to generate pdf files.

::

    # copy preface images prepared in last step to where content page images sit and use command below to generate the whole document.
    ./gendocument.py --tofile=somename.pdf *.png *.jpg


gui
----

.. WARNING:: This script is deprecated. Run downloadlib.py directly.

This script provides gui for downloadduxiu script.

::

    # you have to create a direcotry named "xiazai" where all the python source sit.
    ./gui.py

Enter the url you get from your email and click ok to start download.

When it is finished, "finished" will show in the input area. Clear the input area and fill in your next url to begin a new download.

This script is the easiest way to utilize this package.

API Documentation
==================
.. toctree::
   :maxdepth: 2

   downloadlib_api
   prefaces_api
   gendocument_api
   gui_api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

