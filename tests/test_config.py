import pytest

pytest.importorskip("yaml")


def test_load_settings_without_loader():
    from app.config import load_safe, load_settings

    assert load_settings("a: 1") == {"a": 1}
    assert load_safe("b: 2") == {"b": 2}
