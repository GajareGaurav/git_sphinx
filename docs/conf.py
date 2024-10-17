import os
import sys
from pathlib import Path

# Get the absolute path to the docs directory
docs_dir = Path(__file__).resolve().parent

# Get the path to the project root (one level up from docs)
project_root = docs_dir.parent

# Add the project root and the onetru directory to the Python path
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / 'onetru'))

# Debugging information
print(f"Project root: {project_root}")
print(f"Python path: {sys.path}")

# Project information
project = 'Onetru AI'
copyright = 'tu-dev'
author = 'tu-dev'
release = '00.00.01'

# Extensions
extensions = [
    'sphinx.ext.autodoc',  # Standard extension for autodocumenting code
    'sphinx.ext.viewcode',  # Extension for including source code in the documentation
    'sphinx.ext.napoleon',  # Extension for Google-style docstrings
    'sphinx_multiversion',  # Extension for multi-version documentation
]

# Autodoc settings (mocking imports for external dependencies)
autodoc_mock_imports = [
    'numpy', 'pandas', 'torch', 'tensorflow',  # Mock external dependencies
]

# Template and static paths
templates_path = ['_templates']
html_static_path = ['_static']

# Exclusion patterns
exclude_patterns = [
    '_build',            # Exclude build directory
    'Thumbs.db',         # Exclude Windows thumbnail cache
    '.DS_Store',
]

# HTML theme
html_theme = 'sphinx_rtd_theme'  # Theme for the documentation

# sphinx-multiversion settings for building multi-version documentation
smv_tag_whitelist = r'^v\d+\.\d+'  # Include tags following version format vX.Y
smv_branch_whitelist = r'^.*$'     # Include all branches
smv_remote_whitelist = r'^.*$'     # Include all remotes
smv_released_pattern = r'^.*$'     # Match all versions to release pattern
smv_outputdir_format = '{ref.name}' # Versioned output directories

# Additional setting to include a version selector
# Ensure that the versions dropdown appears in the documentation UI
html_context = {
    "current_version": "v1.0",  # Default version to display initially
    "versions": [
        {"name": "v1.0", "url": "/v1.0"},
        {"name": "v2.0", "url": "/v2.0"},
    ]
}

# You can also adjust the version selector placement in the HTML layout if needed (by modifying theme's templates)
