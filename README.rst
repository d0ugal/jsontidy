JSON Tidy
==============================

The simplest JSON command line utility possible.

Install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    pip install jsontidy

Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make a JSON string more readable::

    echo '[1,2,3]' | jsontidy
    [
        1,
        2,
        3
    ]


Or, another example with Django. Make your fixtures readable.

    django-admin.py dumdata auth | jsontidy

