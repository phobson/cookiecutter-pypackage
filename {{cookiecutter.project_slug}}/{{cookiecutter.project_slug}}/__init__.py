__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


from {{ cookiecutter.project_slug }} import *
from . import viz
from .tests import test
