#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# openff-toolkit documentation build configuration file, created by
# sphinx-quickstart on Sun Dec  3 23:12:54 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("."))

import sphinx

import openff.toolkit

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    #'sphinx.ext.napoleon',
    "numpydoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "myst_parser",
]

# Autodoc settings
autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "member-order": "bysource",
}

# Disable NumPy style attributes/methods expecting every method to have its own docs page
numpydoc_class_members_toctree = False
# Disable numpydoc rendering methods twice
# https://stackoverflow.com/questions/34216659/sphinx-autosummary-produces-two-summaries-for-each-class
numpydoc_show_class_members = False

_python_doc_base = "https://docs.python.org/3.6"
intersphinx_mapping = {
    _python_doc_base: None,
    "https://numpy.org/doc/stable": None,
    "https://docs.scipy.org/doc/scipy/reference": None,
    "https://scikit-learn.org/stable": None,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Extensions for the myst parser
myst_enable_extensions = [
    "dollarmath",
    "colon_fence",
    "smartquotes",
    "replacements",
    "deflist",
]
# Stop myst from disabling MathJax's $...$ and $$...$$ environments
myst_update_mathjax = False

# Source parsers
# source_parsers = {
#   '.md': 'recommonmark.parser.CommonMarkParser',
# }

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "OpenFF Toolkit"
copyright = "2016-2021 Open Force Field Initiative"
author = "Open Force Field Initiative"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = openff.toolkit.__version__
# version = '0.2.0'
# The full version, including alpha/beta/rc tags.
release = openff.toolkit.__version__
# release = '0.2.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "sphinx"
# pygments_style = 'paraiso-dark'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "alabaster"
# html_theme = "bootstrap"
html_theme = "sphinx_material"
# html_theme = "cloud"
# html_theme = "press"

html_title = "OpenFF Toolkit Documentation"
html_short_title = "OpenFF Toolkit Docs"
html_favicon = "_static/favicon.svg"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = "_static/openff_toolkit_v1_white on darkblue.svg"

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {
    # Repository integration
    # Set the repo url for the link to appear
    "repo_url": "https://github.com/openforcefield/openff-toolkit",
    # The name of the repo. If must be set if repo_url is set
    "repo_name": "openff-toolkit",
    # Must be one of github, gitlab or bitbucket
    "repo_type": "github",
    # TOC Tree generation
    # The maximum depth of the global TOC; set it to -1 to allow unlimited depth
    "globaltoc_depth": 2,
    # If true, TOC entries that are not ancestors of the current page are collapsed
    "globaltoc_collapse": True,
    # If true, the global TOC tree will also contain hidden entries
    "globaltoc_includehidden": False,
    # Colour for the top nav bar and links, among other things
    # "openff-blue" is defined in _static/css/palette.css
    "color_primary": "openff-blue",
    # Colour for sidebar captions and other accents
    # "openff-toolkit-blue", "openff-dataset-yellow", and "openff-evaluator-orange"
    # are all defined in _static/css/palette.css
    "color_accent": "openff-toolkit-blue",
    # Text to appear at the top of the home page in a "hero" div. Must be a
    # dict[str, str] of the form pagename: hero text, e.g., {'index': 'text on index'}
    "heroes": {},
    # Content Minification for deployment, prettification for debugging
    "html_minify": False,
    "html_prettify": False,
    "css_minify": False,
    # Include the master document at the top of the page in the breadcrumb bar.
    # You must also set this to true if you want to override the rootrellink block, in which
    # case the content of the overridden block will appear
    "master_doc": True,
}

# # Sidebars
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "searchbox.html"],
    "developing": [
        "logo-text.html",
        "globaltoc.html",
        "searchbox.html",
        "localtoc.html",
    ],
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# CSS:
html_css_files = ["css/theme.css", "css/palette.css", "css/apiref.css"]
templates_path = ["_templates"]
html_show_sourcelink = False


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#    '**': [
#        'about.html',
#        'navigation.html',
#        'relations.html',  # needs 'show_related': True theme option to display
#        'searchbox.html',
#        'donate.html',
#    ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "openforcefielddoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "letterpaper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    "preamble": r"""
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
    """,
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "openforcefield.tex",
        "OpenFF Toolkit Documentation",
        "Open Force Field Consortium",
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "openff-toolkit", "OpenFF Toolkit Documentation", [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "openff-toolkit",
        "OpenFF Toolkit Documentation",
        author,
        "openff-toolkit",
        "A modern, extensible library for molecular mechanics force field science from the Open Force Field Consortium.",
        "Miscellaneous",
    ),
]
