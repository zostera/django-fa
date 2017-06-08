=========
django-fa
=========


Font Awesome for Django.

.. image:: https://coveralls.io/repos/github/zostera/django-fa/badge.svg?branch=master
    :target: https://coveralls.io/github/zostera/django-fa?branch=master

.. image:: https://travis-ci.org/zostera/django-fa.svg?branch=master
    :target: https://travis-ci.org/zostera/django-fa


Installation
------------

1. Install using pip:

   ``pip install django-fa``

   Alternatively, you can install download or clone this repo and call ``pip install -e .``.

2. Add to INSTALLED_APPS in your ``settings.py``:

   ``'fa',``

3. Use the `font-awesome` tag library in your templates


Example template
----------------

   .. code:: Django

    {% load font_awesome %}

    {# Load CSS #}

    {% fa_css %}

    {# Display an icon #}

    {% fa 'fa-shield' %}


Documentation
-------------

See https://django-fa.readthedocs.io for complete documentation.


Compatible Django and Python versions
-------------------------------------

Currently `django-fa` requires Django >= 1.8 and a matching Python version.

Python and Django support will match the Django project. When a Django or Python versions is no longer
supported by the Django Project, this package will also stop supporting those versions. You are strongly
encouraged to upgrade to the newest (LTS) combination of Python/Django.


Requirements
------------

Django >= 1.8 and a matching Python version


Bugs and requests
-----------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/zostera/django-fa/issues


License
-------

You can use this under the MIT License. See `LICENSE <LICENSE>`_ file for details.


Author
------

Developed and maintained by `Zostera <https://zostera.nl/>`_.

Original author & Development lead: `Dylan Verheul <https://github.com/dyve>`_.

Thanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.

Please see `AUTHORS.rst <AUTHORS.rst>`_ for a list of contributors.
