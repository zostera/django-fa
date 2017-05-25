# coding: utf-8
from __future__ import unicode_literals

from django.template import Template, Context
from django.test import TestCase

from fa.conf import get_fa_setting


def render_template(content, **context_args):
    """
    Create a template with content ``content`` that first loads the font-awesome tags.
    """
    template = Template("{% load font_awesome %}" + content)
    return template.render(Context(context_args))


class SettingsTest(TestCase):
    """
    Test the settings for django-fa
    """

    def test_settings(self):
        # This has the default setting, also this means to change the URL you have to change this test
        self.assertEqual(
            get_fa_setting('url'),
            'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'
        )
        with self.settings(FONT_AWESOME={'tag': 'span'}):
            self.assertEqual(get_fa_setting('tag'), 'span')


class TemplateTagsTest(TestCase):
    """
    Test all template tags
    """

    def test_css_url(self):
        res = render_template('{% fa_css_url %}')
        self.assertHTMLEqual(
            res,
            get_fa_setting('url'),
        )

    def test_css_tag(self):
        res = render_template('{% fa_css %}')
        self.assertHTMLEqual(
            res,
            '<link rel="stylesheet" href="{url}">'.format(url=get_fa_setting('url')),
        )

    def test_fa_tag(self):
        res = render_template('{% fa %}')
        self.assertHTMLEqual(
            res,
            '<i class="fa"></i>',
        )
        res = render_template('{% fa "foo" %}')
        self.assertHTMLEqual(
            res,
            '<i class="fa fa-foo"></i>',
        )
        res = render_template('{% fa "fa-foo" %}')
        self.assertHTMLEqual(
            res,
            '<i class="fa fa-foo"></i>',
        )
