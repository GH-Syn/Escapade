"""Sphinx configuration file."""
import sys
from pathlib import Path

# Add path to local extension
this_dir = Path(__file__).parent
ext_dir = (this_dir / ".." / "src").resolve()
sys.path.append(str(ext_dir.absolute()))

project = "Escapade"
copyright = "2023, Joshua Rose"
author = "Joshua Rose"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ["_templates"]


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinxawesome_theme",
    "sphinx_sitemap",
    "sphinx_design",
]

exclude_patterns = ["public", "includes", "**/includes"]

nitpicky = True
nitpick_ignore = [
    ("py:class", "sphinx.application.Sphinx"),
    ("py:class", "docutils.nodes.Element"),
]

default_role = "literal"

# Global substitutions for reStructuredText files
rst_prolog = """
.. |rst| replace:: reStructuredText
.. |product| replace:: Awesome Theme
"""

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# -- Options for HTML output -------------------------------------------------
html_permalinks_icon = "<span>#</span>"
html_static_path = ["_static"]
html_title = project
html_theme = "sphinxawesome_theme"
html_baseurl = "https://github.com/GH-Syn/Escapade"
html_theme_path = ["../src"]
html_last_updated_fmt = ""
html_use_index = False  # Don't create index
html_domain_indices = False  # Don't need module indices
html_copy_source = False  # Don't need sources
