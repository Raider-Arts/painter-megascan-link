# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from recommonmark.transform import AutoStructify
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'Megascan Link Painter'
copyright = '2020, Luca Faggion'
author = 'Luca Faggion'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx_js', 'sphinx.ext.autodoc', 'sphinx_rtd_theme', 'recommonmark', 'sphinx_markdown_tables', 'breathe','sphinx.ext.autosectionlabel'
]

# Source files suffixes
source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'megascan_link_python/websocket']

# Mock modules
# List imports to mock
autodoc_mock_imports = ["substance_painter","websocket"]

# Base path of js files
js_source_path = '../megascan_link_js/'

# # default breathe project
breathe_default_project = "megascanlink"

breathe_projects_source = {
	"megascanlink" : (  os.path.abspath('..') + "/megascan_link_js/", ["AlgNewProject.qml", "main.qml", "AlgSelectDialog.qml"] )
}

breathe_default_members = ('members', 'undoc-members')

breathe_doxygen_config_options = {"GENERATE_XML": "YES",
								"EXTENSION_MAPPING": "qml=C++",
								"FILTER_PATTERNS": "*.qml=doxyqml",
								"FILE_PATTERNS": "*.qml",
								"PREDEFINED": "Q_PROPERTY(x)=x;",
								"MACRO_EXPANSION": "YES",
								"ENABLE_PREPROCESSING": "YES",
								"MACRO_EXPANSION ": "YES",
								"EXPAND_ONLY_PREDEF": "YES",
								"EXPAND_ONLY_PREDEF": "YES"}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#css style
html_css_files = ['style.css']

#logo
#Logo
html_logo = '_static/logo_big.gif'

# -- Autostructify -------------------------------------------------

def setup(app):
    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True
            }, True)
    app.add_transform(AutoStructify)