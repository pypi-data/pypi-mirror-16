========
Overview
========



Simple Throw-Away Publish/Subscribe. Create channels simply by connecting one or mote websocket clients to a random URL path on a webserver with staps. Not
meant to be used with webbrowsers but as a cheap way to let multiple websocket clients written outside the browser communicate with each other.

* Free software: BSD license

Installation
============

::

    pip install staps

Documentation
=============

https://staps.readthedocs.io/en/latest/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


Changelog
=========

0.1.6 (2016-07-20)
-----------------------------------------

* Do not build universal wheel as Python2 is not supported.

0.1.5 (2016-07-19)
-----------------------------------------

* Improved packaging to include missing templates.

0.1.4 (2016-07-19)
-----------------------------------------

* Add HTTP handler to show usage information and autogenerate UUID4 URLs.
* Add CLI option to listen directly on TCP ports.

0.1.3 (2016-07-18)
-----------------------------------------

* Improved documentation.

0.1.2 (2016-05-25)
-----------------------------------------

* Include requirements.txt in source distribution.
* Reorganize imports using isort.

0.1.1 (2016-05-25)
-----------------------------------------

* Include staps.conf in MANIFEST.in.
* Use prefered socket path in usage documentation.

0.1.0 (2016-03-03)
-----------------------------------------

* First release on PyPI.


