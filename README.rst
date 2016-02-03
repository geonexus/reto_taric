.. _Top:
==========
Reto Taric
==========


| |Build Status| |Coverage Status|

.. contents:: :local:

Introduction
============

This is the code repository for **Reto Taric**, a web application written in Python under Django.
This application was developed by Guillermo Jimenez.

Any feedback on this documentation is highly welcome, including bugs, typos or
things you think should be included but aren't. You can use `github issues`__
to provide feedback.

__ `reto_taric - GitHub issues`_

Top_.


Components
----------

taric_books
    Taric_Books is a django application to provide a search engine of books.
    Book information is collected from ``isbndb.com`` so you must have an account and an API key to perform requests.
    You can create your account in (http://isbndb.com/account/logincreate).

Top_.


Build and Install
=================

Requirements
------------

- Operating systems: CentOS (RedHat) and Ubuntu (Debian), OS X and Windows.

To install this module you have to install some components:

- Python 2.7
- pip installed (http://docs.python-guide.org/en/latest/starting/install/linux/)
- Git

To access the web application you have to use a web browser.

It's recommended to use Google Chrome (http://google.com/chrome)

Top_.


Installation
------------

Once you have all prerequisites installed, clone this repo using a shell or terminal:

::

    $ git clone https://github.com/geonexus/reto_taric.git

After finishing you should install all requirements using pip. Execute  the following command inside the root
 directory of the project:

.. code::

    $ pip install -r requirements.txt

Top_.

Configuration
-------------
Finally you must configure the application by adding some values in ``reto_taric/settings.py``:

- Add your isbndb API key in `ISBNDB_API_KEY``.
- add a unique random key for ``SECRET`` parameter.
- You should also add your host addresses to ``ALLOWED_HOSTS`` parameter.

If you disable Debug parameter, the static content (css, images and JS) will be managed by the application server
so you will need execute the application using Apache, Gunicorn, uwsgi, etc.
If you prefer still executing the application without DEBUG mode, you must run Django development server
 with ``--insecure`` parameter to load static content.

.. code::

    $ python manage.py runserver --insecure


Top_.

Running
=======

To run reto_taric, just execute in the root directory of the project:

.. code::

    $ python manage.py runserver

To stop reto_taric, you can stop django development server using CTRL + C.


NOTE: django provides a development webserver to deploy the application. If you want to deploy this project in
a production system, I recommend to deploy it using gunicorn + supervisord + nginx.

Using the application
=====================

To access to the application you should insert the following address.

.. code::

    http://{{ IP_address }}:8000/taric_books

Where {{ IP_address }} is the IP where the project was deployed.

Top_.


Testing
=======

Unit tests
----------

Download source code from github

::

    $ git clone https://github.com/geonexus/reto_taric.git

To execute the unit tests, you must set the environment variable pointing to the settings file.
Then you can use coverage to execute the tests and obtain the percentage of lines coveved by the tests.
You must execute the tests from project folder ``taric_books``.
Once you were inside the right location, execute the required commands:

::

    $ export DJANGO_SETTINGS_MODULE=reto_taric.settings
    $ python manage.py test

or coverage to get statics about the code   coverage
::

    $ coverage run --source='.' manage.py test taric_books
    $ coverage report


Top_.

Testbed
=======

There is a public execution of this project, you can find the application accessing the following link:

.. code::

    http://retotaric.geonexus.es

I hope you enjoy.

Top_.

.. IMAGES

.. |Build Status| image:: https://travis-ci.org/geonexus/reto_taric.svg?branch=develop
   :target: https://travis-ci.org/geonexus/reto_taric
   :alt: Build Status
.. |Coverage Status| image:: https://img.shields.io/coveralls/geonexus/reto_taric/develop.svg
   :target: https://coveralls.io/r/geonexus/reto_taric
   :alt: Coverage Status

.. REFERENCES

.. _Reto_taric - GitHub issues: https://github.com/geonexus/taric_books/issues/new
