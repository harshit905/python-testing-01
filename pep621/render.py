"""Uses the removed jinja2 Markup helper, like app/templates.py, but declared through pyproject.toml."""
from jinja2 import Markup


def bold(text):
    return Markup("<b>%s</b>") % text
