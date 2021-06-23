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

# bootstrap theme
import sphinx_bootstrap_theme

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
    "numpydoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "myst_nb",
    # "myst_parser",
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
    "http://docs.openmm.org/latest/api-python/": None,
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

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = [".rst", ".md", ".ipynb"]

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
# The full version, including alpha/beta/rc tags.
release = openff.toolkit.__version__

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
pygments_style = "sphinx"
# pygments_style = 'paraiso-dark'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = "_static/openforcefield.png"

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {
    # Disable the sidebar, since it takes up too much space
    "nosidebar": True,
    # Navigation bar title. (Default: ``project`` value)
    "navbar_title": "OpenFF Toolkit",
    # Tab name for entire site. (Default: "Site")
    "navbar_site_name": "OpenFF Toolkit",
    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    "navbar_links": [
        # ("Examples", "https://github.com/openforcefield/openff-toolkit/tree/master/examples", True),
        ("Open Force Field Initiative", "http://openforcefield.org", True),
    ],
    # Render the next and previous page links in navbar. (Default: true)
    "navbar_sidebarrel": True,
    # Render the current pages TOC in the navbar. (Default: true)
    "navbar_pagenav": True,
    # Tab name for the current pages TOC. (Default: "Page")
    "navbar_pagenav_name": "Page",
    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    "globaltoc_depth": 2,
    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    "globaltoc_includehidden": "true",
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    "navbar_class": "navbar navbar-inverse",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    "navbar_fixed_top": "false",
    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    "source_link_position": "nav",
    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "cosmo" or "sandstone".
    "bootswatch_theme": "yeti",
    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    "bootstrap_version": "3",
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

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
