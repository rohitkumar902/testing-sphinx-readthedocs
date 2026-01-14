import sys
from pathlib import Path
from importlib.metadata import version 

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "YOUVA"
copyright = "2026, Rohit Kumar"
author = "Rohit Kumar"
release = version("youva")
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",  # Google / NumPy style docstrings
    "sphinx.ext.viewcode",  # Add links to source code
    "autoapi.extension",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_theme_options = {
    "top_of_page_buttons": [
        "edit",
    ],
    "source_repository": "https://github.com/rohitkumar902/testing-sphinx-readthedocs",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

autoapi_type = "python"

# Point to your source directories
autoapi_dirs = [
    "../../youva",
]

# Keep generated files (useful while learning)
autoapi_keep_files = True

autoapi_generate_package_index = False

autoapi_template_dir = "_templates/autoapi"

# What AutoAPI should include
autoapi_options = [
    "members",
    "undoc-members",
    "show-module-summary",
    "show-inheritance",
]
