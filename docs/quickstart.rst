Quickstart
==========


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
