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

**Hipchat message**

Sends a hipchat message to selected channel.

    $ hipon.py room_id "This is a message @all"

    $ hipon.py -h
    usage: hipon.py [-h] roomid message
    
    positional arguments:
      roomid
      message

    optional arguments:
      -h, --help  show this help message and exit


Where *room_id* is your integer room id.


**Check migrations**

Validates Django project against duplicated migrations number (useful for
med - big size projects with CI).

    $ check_migrations.py -h
    usage: check_migrations.py [-h] [--strict] [-x exclude] dir
    
    Find duplicated Django South migrations.
    
    positional arguments:
      dir                   directory
    
    optional arguments:
      -h, --help            show this help message and exit
      --strict              exit with error code when first duplicated migration
                            found
      -x exclude, --exclude exclude
                            exclude pattern

**Devault Client**

Get a latest deployed version on a provided environment.

    $ devault.py -h

    usage: devault.py [-h] command [options]
    
    positional arguments:
      command
      options
    
    optional arguments:
      -h, --help  show this help message and exit
    
    $ devault.py gv production

    4.14


