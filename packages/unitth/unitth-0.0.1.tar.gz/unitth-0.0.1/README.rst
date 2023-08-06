|PyPI package| |Documentation| |Test results| |Test coverage|

unitth
======

This package provides a Python method and command line interface for
generating HTML reports of unit test histories. The package is a Python
interface for the `UnitTH <http://junitth.sourceforge.net>`__.

Installation
------------

::

    pip install unitth

Example usage
-------------

Python
~~~~~~

::

    from unith.core import UnitTH
    UnitTH.run('junit-reports/*', html_report_dir='html-history-report')

Command line
~~~~~~~~~~~~

::

    unitth --help
    unitth --html_report_dir html-history-report junit-reports/*

Documentation
-------------

Please see the `API documentation <http://unitth.readthedocs.io>`__.

License
-------

The build utilities are released under the `MIT
license <LICENSE.txt>`__.

Development team
----------------

This package was developed by `Jonathan Karr <http://www.karrlab.org>`__
at the Icahn School of Medicine at Mount Sinai in New York, USA.

Questions and comments
----------------------

Please contact the `Jonathan Karr <http://www.karrlab.org>`__ with any
questions or comments.

.. |PyPI package| image:: https://badge.fury.io/py/unitth.svg
   :target: https://pypi.python.org/pypi/unitth
.. |Documentation| image:: https://readthedocs.org/projects/unitth/badge/?version=latest
   :target: http://unitth.readthedocs.org
.. |Test results| image:: https://circleci.com/gh/KarrLab/unitth.svg?style=shield
   :target: https://circleci.com/gh/KarrLab/unitth
.. |Test coverage| image:: https://coveralls.io/repos/github/KarrLab/unitth/badge.svg
   :target: https://coveralls.io/github/KarrLab/unitth
