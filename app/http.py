"""HTTP pool with a retry policy (urllib3)."""
import urllib3
from urllib3.util.retry import Retry as _Retry


def retry_policy():
    # `method_whitelist` was renamed to `allowed_methods` in urllib3 1.26 and REMOVED in 2.0.
    return _Retry(total=3, backoff_factor=0.2, method_whitelist=["GET", "HEAD"])


def pool():
    return urllib3.PoolManager(retries=retry_policy(), timeout=urllib3.Timeout(connect=2.0, read=5.0))
