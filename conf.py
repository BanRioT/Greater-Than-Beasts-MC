# Configuration file for the Sphinx documentation builder.

project = 'Greater Than Beasts'
copyright = '2026, BanRioT'
author = 'BanrioT'

# Add 'myst_parser' to handle Markdown (.md) files
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
]

# Use the classic Read the Docs theme
html_theme = "sphinx_rtd_theme"

# Define where your files are
source_suffix = {
    '.md': 'markdown',
}
