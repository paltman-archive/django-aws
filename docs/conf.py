# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.abspath(os.curdir))
sys.path.append(os.path.abspath(os.pardir))
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.txt'
master_doc = 'index'

project = u'django-aws'
copyright = u'2010, Patrick Altman'
version = '0.1'
release = '0.1'

exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
htmlhelp_basename = 'django-aws-doc'

latex_documents = [
  ('index', 'django-aws.tex', u'django-aws Documentation',
   u'Patrick Altman', 'manual'),
]

man_pages = [
    ('index', 'django-aws', u'django-aws Documentation',
     [u'Patrick Altman'], 1)
]
