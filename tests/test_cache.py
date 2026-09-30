import pytest

pytest.importorskip("werkzeug")


def test_remember():
    from app.cache import remember

    assert remember("k", 1) == 1
