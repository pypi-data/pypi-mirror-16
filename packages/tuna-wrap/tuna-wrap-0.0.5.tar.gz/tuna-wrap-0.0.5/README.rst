===========
Description
===========

Run Nautilus scripts with the Thunar file manager. Tuna-wrap wraps
Nautilus filemanager scripts to run these from Thunars custom actions.

**License**

    MIT License

**Notes**

    * Only tested on ubuntu with nautilus scripts written in python

========
Features
========

    * share you scripts between Thunar, Nautilus and Nemo
    * very easy use

============
Installation
============

**Installation / Deinstallation**

    *with pip*
        
        ::
        
            pip install tuna-wrap
    
            pip uninstall tuna-wrap


    *or setup.py*

        1. Unpack your package.
        2. Open a terminal and change to the folder which contains the setup.py and type

        ::

            python setup.py install
   
=====
Setup
=====
    
    * Edit your Thunar custom actions in following scheme:
      'tuna-wrap' "YOUR NAUTILUS SCRIPT NAME" "%d" "%N"

=====
Usage
=====

    * Use it as your other custom actions
    * get this readme with: tuna-wrap --help
    
=====
Hints
=====

    * The logfile is stored in you home directory: ~/.tuna-wrap.log
