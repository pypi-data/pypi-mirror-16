==================================
Postcodes.io Python Client - alpha
==================================


.. image:: https://img.shields.io/pypi/v/postcodes_io.svg
        :target: https://pypi.python.org/pypi/postcodes_io

.. image:: https://img.shields.io/travis/jimmyho/postcodes_io.svg
        :target: https://travis-ci.org/jimmyho/postcodes_io

.. image:: https://readthedocs.org/projects/postcodes-io/badge/?version=latest
        :target: https://postcodes-io.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/jimmyho/postcodes_io/shield.svg
     :target: https://pyup.io/repos/github/jimmyho/postcodes_io/
     :alt: Updates


Python client to connect to Postcodes.io API


* Free software: MIT license
* Documentation: https://postcodes-io.readthedocs.io.


Features
--------
* Supports python 3.x (not yet python 2.x, sorry!)
* Response in Python native list and dict types
* Supports free http://postcodes.io/postcodes REST service and self-hosted service (See documentation for installation details)

Quick Start
-----------
Install python package:

.. code-block:: console

    $ pip install postcodes_io
    $ python


.. code-block:: python

    from postcodes_io import Postcodes
    pio = Postcodes()
    postcode = pio.get('SW1A 1AA')

Self-hosted Service using Docker
--------------------------------
1. Pull docker image::

    docker pull randomvariable/docker-postcodes.io

2. Run docker container as a daemon::

    docker run -p 8000:8000 -d randomvariable/docker-postcodes.io

3. Execute API using hosts

.. code-block:: python

    from postcodes_io import Postcodes
    postcode = Postcodes('http://localhost:8000').get('SW1A 1AA')

TODOs
--------

* Add more endpoints
* Documentation
* Proper isolated unit tests
