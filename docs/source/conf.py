# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Modeltools documentation'
copyright = '2022, Beatriz'
author = 'Beatriz'
release = "1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'  # 'furo'
html_static_path = ['_static']

extensions = [
    'sphinx.ext.autodoc',
    'autoapi.extension',
]

autoapi_type = 'python'
autoapi_dirs = ['../../modeltools']  # subo dos directorios para que encuentre el paquete.

