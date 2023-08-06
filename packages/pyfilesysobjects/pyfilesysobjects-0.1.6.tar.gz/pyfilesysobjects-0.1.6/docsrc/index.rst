
.. filesysobjects documentation master file, created by
   sphinx-quickstart on `date`.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Abstract
========

The 'filesysobjects' package provides utilities for the simplified navigation in filesystem 
hierarchies. 
This comprises basic functions for the application of object oriented patterns 
onto files, directories, and branches.

* **Manage Multiple Search Lists and support 're' and 'glob' for path search**

  Provides the creation and usage of multiple search paths including the
  full scale pattern matching on search paths by 're' and 'glob' `[details] <path_syntax.html#variants-of-pathname-parameters-literals-regexpr-and-glob>`_.

* **Gears for Filesystem Objects - Files, Directories, and Branches**

  The package provides a set of basic functions for implementing file system items 
  conceptually as classes and objects. Just a few interfaces are required in order to represent 
  some basic OO features on filesystems. This in particular comprises superposition 
  and encapsulation, polymorphism, class and object hierachies.

  * Filesystem elements as classes and objects with multiple search and iteration sets `[details] <path_syntax.html#filesystem-elements-as-objects>`_

  * Standards compliant multiplatform native path support: `[details] <path_syntax.html#syntax-elements>`_ 
    `[examples] <path_syntax_examples.html>`_.

    
  * Programming Interface: 
    `[API] <shortcuts.html#filesysobjects-filesysobjects>`_,
    `[UseCases] <UseCases.html>`_.
      .

* **Yet another attempt for file address processing on network storage**

  Evaluation for an extension modul of the interface 'os.path.normpath'.
  Thus the function is named for now 'filesysobjects.NetFiles.normpathX'.

  * `Extended Filesystems - Network Features <path_netfiles.html>`_
      .

* **RTTI for native Python source files** see
  `PySourceInfo @ https://pypi.python.org/pypi/pysourceinfo <https://pypi.python.org/pypi/pysourceinfo>`_
 

`Shortcuts <shortcuts.html>`_
============================

* `Programming Interface <shortcuts.html>`_

* `Selected Common UsesCases <usecases.html>`_

Table of Contents
=================
   
 
.. toctree::
   :maxdepth: 3

   shortcuts
   usecases
   filesysobjects
   netfiles
   UseCases
   tests
   testdata

* setup.py

  For help on extensions to standard options call onlinehelp:: 

    python setup.py --help-filesysobjects



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Resources
=========

For available downloads refer to:

* Python Package Index: https://pypi.python.org/pypi/filesysobjects

* Sourceforge.net: https://sourceforge.net/projects/filesysobjects/

* github.com: https://github.com/ArnoCan/filesysobjects/

For Licenses refer to enclosed documents:

* Artistic-License-2.0(base license): `ArtisticLicense20.html <_static/ArtisticLicense20.html>`_

* Forced-Fairplay-Constraints(amendments): `licenses-amendments.txt <_static/licenses-amendments.txt>`_ / `Protect OpenSource Authors <http://xkcd.com/1303/>`_

