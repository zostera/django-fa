# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.html import format_html

from ..conf import get_fa_setting

register = template.Library()


@register.simple_tag
def fa_css_url():
    """
    Return the full url to the Font Awesome CSS library

    Default value: ``None``

    This value is configurable, see Settings section

    **Tag name**::

        fa_css_url

    **usage**::

        {% fa_css_url %}

    **example**::

        {% fa_css_url %}
    """
    return get_fa_setting('url')


@register.simple_tag
def fa_css():
    """
    Return the full url to the Font Awesome CSS library

    Default value: ``None``

    This value is configurable, see Settings section

    **Tag name**::

        fa_css_url

    **usage**::

        {% fa_css_url %}

    **example**::

        {% fa_css_url %}
    """
    return format_html(
        '<link rel="stylesheet" href="{url}">',
        url=fa_css_url(),
    )


@register.simple_tag
def fa(*args):
    """
    Return a Font Awesome tag with all these arguments (fa- is automatically prepended)
    """
    # Get tag from settings
    tag = get_fa_setting('tag')
    # Prepare format string with proper placeholder for css_classes
    format_string = '<' + tag + ' class="{css_classes}"></' + tag + '>'
    # Prepend arguments with fa- if needed
    fa_args = []
    for arg in args:
        if arg.startswith('fa-'):
            fa_args.append(arg)
        else:
            fa_args.append('fa-{arg}'.format(arg=arg))
    # Return safely formatted HTML
    return format_html(
        format_string,
        css_classes=' '.join(['fa'] + fa_args),
    )
