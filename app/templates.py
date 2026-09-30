"""Templating helpers (Jinja2)."""
from jinja2 import Environment, Markup, Template, escape

_env = Environment(autoescape=True)


def render(source, **context):
    return Template(source).render(**context)


def highlight(text):
    # Markup and escape were REMOVED from jinja2 in 3.1 (they live in markupsafe now).
    return Markup("<mark>%s</mark>") % escape(text)


def env():
    return _env
