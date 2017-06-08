# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.html import format_html

from ..conf import get_fa_setting

TRUE_ICON = 'fa-check-circle-o'
FALSE_ICON = 'fa-circle-o'
NONE_ICON = 'fa-question-circle-o'
UNKNOWN_ICON = 'fa-question-circle'

register = template.Library()


def _sanitize_icon_name(name, default=None):
    """
    Helper function to sanitize icon string
    :param name: The name of the icon
    :param default: A fallback if the name is invalid or empty
    :return: Lowercase icon name that starts with `fa-`
    """
    if name:
        name = '{}'.format(name).lower()
        if name == 'default':
            name = ''
    else:
        name = ''
    if not name:
        name = default if default else UNKNOWN_ICON
    if not name.startswith('fa-'):
        name = 'fa-{}'.format(name)
    return name


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
    Return the HTML to insert the Font Awesome CSS library

    Default value: ``None``

    This value is configurable, see Settings section

    **Tag name**::

        fa_css

    **usage**::

        {% fa_css %}

    **example**::

        {% fa_css %}
    """
    return format_html('<link rel="stylesheet" href="{url}">', url=fa_css_url())


@register.simple_tag
def icon(name, *args, **kwargs):
    """
    Return a Font Awesome icon tag based on the arguments to this template tag
    """
    # Get tag from settings
    tag = get_fa_setting('tag')
    # Prepare format string with proper placeholder for css_classes
    format_string = '<' + tag + ' class="{css_classes}"></' + tag + '>'
    # Sanitize icon
    name = _sanitize_icon_name(name, kwargs.get('default', None))
    # Prepare HTML attributes
    fa_args = ['fa', name] + ['{}'.format(a) for a in args]
    # Return safely formatted HTML
    return format_html(
        format_string,
        css_classes=u' '.join(fa_args),
    )


@register.simple_tag
def fa(*args, **kwargs):
    """
    Backwards compatible alias
    :param args:
    :param kwargs:
    :return:
    """
    # TODO: Warning for deprecation
    return icon(*args, **kwargs)


def _yesno_icon(value, arg, force_none):
    """
    Helper function for yesno filters
    """
    # Lazy trick to make sure we get at least 3 results
    args = '{},,'.format(arg if arg else '').split(',')
    parts = [x.strip() for x in args]
    yes = parts[0]
    no = parts[1]
    none = parts[2]
    if value:
        return icon(yes, default=TRUE_ICON)
    if (force_none or none) and value is None:
        return icon(none, default=NONE_ICON)
    return icon(no, default=FALSE_ICON)


@register.filter()
def yesno_icon(value, arg=''):
    """
    Like the yesno filter in Django, only resulting in an icon
    """
    return _yesno_icon(value, arg, force_none=False)


@register.filter()
def yesnonone_icon(value, arg=''):
    """
    Like the yesno filter in Django, only resulting in an icon, and always use an icon for None
    """
    return _yesno_icon(value, arg, force_none=True)
