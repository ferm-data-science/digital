# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('..'))


project = 'Digital'
copyright = '2024, Ferm'
author = 'Sitala'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_design',
    "myst_parser",
    "sphinxcontrib.jquery",
    "sphinx_datatables",
    "sphinx.ext.githubpages",
]

myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ua'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
# html_theme = 'pydata_sphinx_theme'
# html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# set the version to use for DataTables plugin
datatables_version = "1.13.4"
# name of the class to use for tables to enable DataTables
datatables_class = "sphinx-datatable"
# any custom options to pass to the DataTables constructor. Note that any
# options you set are used for all DataTables.
datatables_options = {}


from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions
from sphinxawesome_theme.postprocess import Icons

html_permalinks_icon = Icons.permalinks_icon

theme_options = ThemeOptions(
    # Add your theme options. For example:
    show_breadcrumbs=True,
    show_scrolltop=True,
    main_nav_links={"About": "/about"},
)

html_theme_options = asdict(theme_options)

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]