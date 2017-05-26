# -*- coding: utf-8 -*-
import os
import re
import sys

import sphinx_rtd_theme

os.environ['DJANGO_SETTINGS_MODULE'] = 'testsettings'

sys.path.insert(0, os.path.abspath('..'))

# Import project
project = 'django-fa'
with open('../fa/__init__.py', 'rb') as f:
    release = re.search('__version__ = \'(.+?)\'', f.read()).group(1)
version = release.rpartition('.')[0]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
]

source_suffix = '.rst'

master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
