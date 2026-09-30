import pytest

pytest.importorskip("urllib3")


def test_retry_policy_allows_get():
    from app.http import retry_policy

    policy = retry_policy()
    assert policy.total == 3
