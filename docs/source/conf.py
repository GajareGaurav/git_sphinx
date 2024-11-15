import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Onetru AI'
copyright = 'tu-dev'
author = 'tu-dev'
# The full version, including alpha/beta/rc tags
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_multiversion'  # Add this line
]

# Sphinx-multiversion specific settings
smv_tag_whitelist = r'^.*$'  # Include all tags
smv_branch_whitelist = r'^.*$'  # Include all branches
smv_remote_whitelist = None  # Include all remotes
smv_outputdir_format = '{ref.name}'  # Output format for versioned builds

# Templates config
templates_path = ['_templates']
html_sidebars = {
    '**': [
        'versions.html',
    ],
}

# List of patterns to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Multiversion custom template -------------------------------------------
html_context = {
    'home_page': 'index',  # Name of the main page without .html
}
