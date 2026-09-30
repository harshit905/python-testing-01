import pytest

pytest.importorskip("jinja2")


def test_render_and_highlight():
    from app.templates import highlight, render

    assert render("hi {{ name }}", name="x") == "hi x"
    assert "<mark>" in str(highlight("a<b"))
