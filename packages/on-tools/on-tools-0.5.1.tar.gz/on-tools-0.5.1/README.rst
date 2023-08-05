********
on-tools
********

Opportunity Network Python Helpers

.. image:: https://travis-ci.org/opportunitynetwork/on-tools.svg?branch=master
    :target: https://travis-ci.org/opportunitynetwork/on-tools

------------
Installation
------------



    pip install on-tools

---------------
Available tools
---------------

    $ check_migrations.py -h
    usage: check_migrations.py [-h] [--strict] dir
    
    Find duplicated Django South migrations.
    
    positional arguments:
    dir         directory
    
    optional arguments:
    -h, --help  show this help message and exit
    --strict    exit with error code when first duplicated migration found
    
