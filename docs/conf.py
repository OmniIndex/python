# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# -- Path setup ----------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'OmniIndex Connector Python Library'
copyright = '2023, OmniIndex Inc'
author = 'James Stanbridge'
release = '0.2.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo'
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_domain_indices = True # https://stackoverflow.com/questions/56336234/build-fail-sphinx-error-contents-rst-not-found
html_domain_indices = [('*','genindex', 'genindex.html', 4)]
# Display todos by setting to True
todo_include_todos = False
