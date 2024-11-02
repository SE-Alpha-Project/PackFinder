import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'PackFinder'
copyright = '2024, Your Team Name'
author = 'Your Team Name'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static'] 