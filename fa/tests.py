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
    def test_settings(self):
        self.assertGreater(FONT_AWESOME['url'], '')


class TemplateTagsTest(TestCase):
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
            '<i class="fa"></i>',
        )
        res = render_template('{% fa "foo" %}')
        self.assertEqual(
            res.strip(),
            '<i class="fa fa-foo"></i>',
        )
        res = render_template('{% fa "fa-foo" %}')
        self.assertEqual(
            res.strip(),
            '<i class="fa fa-foo"></i>',
        )
