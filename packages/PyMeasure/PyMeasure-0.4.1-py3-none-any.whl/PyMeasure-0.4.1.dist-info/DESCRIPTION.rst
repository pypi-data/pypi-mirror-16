.. image:: https://raw.githubusercontent.com/ralph-group/pymeasure/master/docs/images/PyMeasure.png
    :alt: PyMeasure Scientific package

PyMeasure scientific package
############################

PyMeasure makes scientific measurements easy to set up and run. The package contains a repository of instrument classes and a system for running experiment procedures, which provides graphical interfaces for graphing live data and managing queues of experiments. Both parts of the package are independent, and when combined provide all the necessary requirements for advanced measurements with only limited coding.

PyMeasure is currently under active development, so please report any issues you experience to our `Issues page`_.

.. image:: https://ci.appveyor.com/api/projects/status/hcj2n2a7l97wfbb8/branch/master?svg=true
    :target: https://ci.appveyor.com/project/cjermain/pymeasure

.. image:: https://travis-ci.org/ralph-group/pymeasure.svg?branch=master
    :target: https://travis-ci.org/ralph-group/pymeasure

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
    :target: http://pymeasure.readthedocs.org/en/latest/

Quick start
***********

Check out `the documentation`_ for the `quick start guide`_, that covers the installation of Python and PyMeasure.

There are a number of examples in the `examples`_ directory that can help you get up and running.


.. _the documentation: http://pymeasure.readthedocs.org/en/latest/
.. _quick start guide: http://pymeasure.readthedocs.io/en/latest/quick_start.html
.. _Issues page: https://github.com/ralph-group/pymeasure/issues
.. _examples: https://github.com/ralph-group/pymeasure/tree/master/examples

Version 0.4.1 -- released 7/31/16
=================================
- Critical fix in setup.py for importing instruments (also added to documentation)

Version 0.4 -- released 7/29/16
===============================
- Replaced Instrument add_measurement and add_control with measurement and control functions
- Added validators to allow Instrument.control to match restricted ranges
- Added mapping to Instrument.control to allow more flexible inputs
- Conda is now used to set up the Python environment
- macOS testing in continuous integration
- Major updates to the documentation

Version 0.3 -- released 4/8/16
==============================
- Added IPython (Jupyter) notebook support with significant features
- Updated set of example scripts and notebooks
- New PyMeasure logo released
- Removed support for Python <3.4
- Changed multiprocessing to use spawn for compatibility
- Significant work on the documentation
- Added initial tests for non-instrument code
- Continuous integration setup for Linux and Windows

Version 0.2 -- released 12/16/15
================================
- Python 3 compatibility, removed support for Python 2
- Considerable renaming for better PEP8 compliance
- Added MIT License
- Major restructuring of the package to break it into smaller modules
- Major rewrite of display functionality, introducing new Qt objects for easy extensions
- Major rewrite of procedure execution, now using a Worker process which takes advantage of multi-core CPUs
- Addition of a number of examples
- New methods for listening to Procedures, introducing ZMQ for TCP connectivity
- Updates to Keithley2400 and VISAAdapter

Version 0.1.6 -- released 4/19/15
=================================
- Renamed the package to PyMeasure from Automate to be more descriptive about its purpose
- Addition of VectorParameter to allow vectors to be input for Procedures
- Minor fixes for the Results and Danfysik8500

Version 0.1.5 -- release 10/22/14
=================================
- New Manager class for handling Procedures in a queue fashion
- New Browser that works in tandem with the Manager to display the queue
- Bug fixes for Results loading

Version 0.1.4 -- released 8/2/14
================================
- Integrated Results class into display and file writing
- Bug fixes for Listener classes
- Bug fixes for SR830

Version 0.1.3 -- released 7/20/14
=================================
- Replaced logging system with Python logging package
- Added data management (Results) and bug fixes for Procedures and Parameters
- Added pandas v0.14 to requirements for data management
- Added data listeners, Qt4 and PyQtGraph helpers

Version 0.1.2 -- released 7/18/14
=================================
- Bug fixes to LakeShore 425
- Added new Procedure and Parameter classes for generic experiments
- Added version number in package

Version 0.1.1 -- released 7/16/14
=================================
- Bug fixes to PrologixAdapter, VISAAdapter, Agilent 8722ES, Agilent 8257D, Stanford SR830, Danfysik8500
- Added Tektronix TDS 2000 with basic functionality
- Fixed Danfysik communication to handle errors properly

Version 0.1.0 -- released 7/15/14
=================================
- Initial release

