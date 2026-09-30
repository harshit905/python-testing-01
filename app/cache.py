"""In-process cache (Werkzeug)."""
from werkzeug.contrib.cache import SimpleCache  # werkzeug.contrib was REMOVED in 1.0

_cache = SimpleCache(default_timeout=60)


def remember(key, value):
    _cache.set(key, value)
    return _cache.get(key)
