# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import sphinx_rtd_theme

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'gptoolkit'
copyright = '2023, Roshan Nanu'
author = 'Roshan Nanu'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Extensions
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

templates_path = ['_templates']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Theme
html_theme = "sphinx_rtd_theme"

# Output directory for HTML documentation
html_baseurl = "https://your-username.github.io/gptoolkit/"
html_extra_path = ["docs"]

# -- Options for autodoc extension ----------------------------------------

# Generate API documentation from docstrings
autodoc_member_order = "bysource"
autosummary_generate = True
add_module_names = False

# Exclude special methods from documentation
exclude_patterns = ["**/tests/*", "**/test_*", "**/__init__*", "**/setup*", "**/conftest*"]

# -- Options for HTML output ----------------------------------------------

# HTML title
html_title = "gptoolkit Documentation"

# HTML logo
# html_logo = "_static/logo.png"

# HTML favicon
# html_favicon = "_static/favicon.ico"

# HTML theme options
html_theme_options = {"display_version": False, "style_external_links": True}

# -- Options for LaTeX output ---------------------------------------------

# LaTeX paper size
latex_paper_size = "letter"

# LaTeX font size
latex_font_size = "10pt"

# -- Options for manual page output ---------------------------------------

# Man page sections
man_pages = [("index", project, project, [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Texinfo document class
texinfo_documents = [(master_doc, project, project, author, project, "One line description of project.", "Miscellaneous")]

