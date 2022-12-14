# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

# The documented project’s name.
project = 'VPLT - The Virtual Programming Lab Tokenizer'

# The author name(s) of the document. The default value is 'unknown'.
author = 'David Parreño Barbuzano'

# A copyright statement in the style '2008, Author Name'.
copyright = '2022 - 2023, ' + author

# An alias of copyright.
project_copyright = copyright

# The major project version, used as the replacement for |version|.
# Please note that release version may differ from version value.
version = '3.5.0++ - 4.0.1'

# The full project version, used as the replacement for |release|.
# If you don’t need the separation provided between version and release,
# just set them both to the same value.
release = '3.5.0++ - 4.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# A list of strings that are module names of extensions.
# These can be extensions coming with Sphinx (named sphinx.ext.*) or custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

# The file extensions of source files. Sphinx considers the files with this suffix as sources.
# The value can be a dictionary mapping file extensions to file types.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

# The encoding of all reST source files. The recommended encoding,
# and the default value, is 'utf-8-sig'.
source_encoding = 'utf-8-sig'

# The document name of the “root” document, that is, the document
# that contains the root toctree directive. Default is 'index'.
root_doc = 'index'

# Same as root_doc.
master_doc = 'index'

# A list of glob-style patterns [1] that should be excluded when looking for source files.
# They are matched against the source file names relative to the source directory, using
# slashes as directory separators on all platforms.
#exclude_patterns = []

# A list of glob-style patterns [1] that are used to find source files.
# They are matched against the source file names relative to the source directory,
# using slashes as directory separators on all platforms. The default is **, meaning
# that all files are recursively included from the source directory.
#include_patterns = []

# A list of paths that contain extra templates (or templates that overwrite
# builtin/theme-specific templates). Relative paths are taken as relative to
# the configuration directory.
templates_path = ['templates']

# A string of reStructuredText that will be included at the end of every source file that is read.

rst_epilog = """
For more details about VPL, visit the `VPL home page <https://vpl.dis.ulpgc.es/>`_ or the
`VPL plugin page at Moodle. <https://moodle.org/plugins/mod_vpl>`_
"""

# A string of reStructuredText that will be included at the beginning of every source file that is read.
#rst_prolog = ''

# If true, keep warnings as “system message” paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run.
keep_warnings = True

# A list of warning types to suppress arbitrary warning messages.
supress_warnings = []

# -- Options for internationalization ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

# The code for the language the docs are written in. Any text automatically generated by Sphinx will be in
# that language. Also, Sphinx will try to substitute individual paragraphs from your documents with the translation
# sets obtained from locale_dirs. Sphinx will search language-specific figures named by figure_language_filename
# (e.g. the German version of myfigure.png will be myfigure.de.png by default setting) and substitute them for
# original figures. In the LaTeX builder, a suitable language will be selected as an option for the Babel
# package. Default is 'en'.
language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# If given, this must be the name of an image file (path relative to the configuration directory) that is
# the logo of the docs, or URL that points an image file for the logo. It is placed at the top of the sidebar;
# its width should therefore not exceed 200 pixels. Default: None.
html_logo = 'images/logo.png'

# If given, this must be the name of an image file (path relative to the configuration directory) that is the favicon
# of the docs, or URL that points an image file for the favicon. Modern browsers use this as the icon for tabs, windows
# and bookmarks. It should be a Windows-style icon file (.ico), which is 16x16 or 32x32 pixels large. Default: None.
html_favicon = 'images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['images']

# If true (and html_copy_source is true as well), links to the reST sources will be added to the sidebar. The default is True.
html_show_sourcelink = False

# If true, the index is generated twice: once as a single page with all the entries,
# and once as one page per starting letter. Default is False.
html_split_index = False

# If true, “(C) Copyright …” is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Output is processed with HTML4 writer. Default is False.
html4_writer = True

# Set style to have colorful code examples
pygments_style = 'sphinx'
