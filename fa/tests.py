# coding: utf-8
from __future__ import unicode_literals

from django.template import Template, Context
from django.test import TestCase

from .conf import FONT_AWESOME


def render_template(text, **context_args):
    """
    Create a template ``text`` that first loads the font-awesome tags.
    """
    template = Template("{% load font_awesome %}" + text)
    return template.render(Context(context_args))


class SettingsTest(TestCase):
    """
    Test the settings for django-fa
    """

    def test_settings(self):
        # This has the default setting, also this means to change the URL you have to change this test
        self.assertEqual(FONT_AWESOME['url'], '//maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css')
        # This is a setting altered in testsettings.py -- the default value is `i`
        self.assertEqual(FONT_AWESOME['tag'], 'span')


class TemplateTagsTest(TestCase):
    """
    Test all template tags
    """

    def test_css_url(self):
        res = render_template('{% fa_css_url %}')
        self.assertEqual(
            res.strip(),
            FONT_AWESOME['url'],
        )

    def test_css_tag(self):
        res = render_template('{% fa_css %}')
        self.assertEqual(
            res.strip(),
            '<link rel="stylesheet" href="{url}">'.format(url=FONT_AWESOME['url']),
        )

    def test_fa_tag(self):
        res = render_template('{% fa %}')
        self.assertEqual(
            res.strip(),
            '<span class="fa"></span>',
        )
        res = render_template('{% fa "foo" %}')
        self.assertEqual(
            res.strip(),
            '<span class="fa fa-foo"></span>',
        )
        res = render_template('{% fa "fa-foo" %}')
        self.assertEqual(
            res.strip(),
            '<span class="fa fa-foo"></span>',
        )
