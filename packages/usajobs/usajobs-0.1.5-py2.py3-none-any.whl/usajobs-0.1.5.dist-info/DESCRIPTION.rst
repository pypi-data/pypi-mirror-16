
.. image:: https://travis-ci.org/brennv/usajobs.svg?branch=master
    :target: https://travis-ci.org/brennv/usajobs
.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5-blue.svg
.. image:: https://img.shields.io/codecov/c/github/brennv/usajobs.svg
    :target: https://codecov.io/gh/brennv/usajobs

`https://github.com/brennv/usajobs`_

Installation
============

.. code:: bash

    pip install usajobs

Getting started
===============

.. code:: python

    import usajobs

    results = usajobs.search('manager')

    len(results)              # 1392

    result = results[0]       # first result
    result.id                 # 'usajobs:445507500'
    result.organization_name  # 'National Park Service'
    result.position_title     # 'Project Manager (Interdisciplinary)'
    result.start_date         # '2016-08-23'
    result.end_date           # '2016-09-13'
    result.url                # 'https://www.usajobs.gov/GetJob/ViewDetails/445507500'
    result.locations          # ['Vancouver, WA']
    result.minimum            # 71012
    result.maximum            # 92316
    result.rate_interval_code # 'PA'

.. _https://github.com/brennv/usajobs: https://github.com/brennv/usajobs


