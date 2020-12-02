import sys, os
import {{ cookiecutter.project_slug }}

## General

project = '{{ cookiecutter.project_name }}'
copyright = '{{ cookiecutter.year }}, {{ cookiecutter.full_name }}'
version = {{ cookiecutter.project_slug }}.__version__
release = {{ cookiecutter.project_slug }}.__version__

master_doc = 'index'
source_suffix = '.rst'
templates_path = ['_templates']
exclude_patterns = ['_build']
default_role = 'any'

## Extensions

extensions = [
        'autoclasstoc',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.viewcode',
        'sphinx.ext.intersphinx',
        'sphinx_rtd_theme',
]
intersphinx_mapping = {
        'python': ('https://docs.python.org/3', None),
}
autosummary_generate = True
autodoc_default_options = {
        'exclude-members': '__dict__,__weakref__,__module__',
}
html_theme = 'sphinx_rtd_theme'
html_static_path = ['static']
pygments_style = 'sphinx'

