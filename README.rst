=========
django-fa
=========

Font Awesome for Django.


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

This is pretty much what it does.


Requirements
------------

- Python 2.6, 2.7, 3.2 or 3.3
- Django >= 1.4

Contributions and pull requests for other Django and Python versions are welcome.


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
