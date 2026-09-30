import pytest

pytest.importorskip("requests")


def test_session_has_user_agent():
    from app.client import session

    assert session().headers["User-Agent"].startswith("sca-test")
