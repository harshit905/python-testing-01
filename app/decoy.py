"""Same-named local symbols that are NOT the third-party APIs. An assessment must not count these as call sites."""


class Retry:
    """A local retry helper unrelated to urllib3."""

    def __init__(self, attempts=3):
        self.attempts = attempts


def method_whitelist():
    """Local function; a grep for the urllib3 parameter name lands here too."""
    return ["GET", "POST"]


def markup_note():
    # historical: this used to call jinja2.Markup before the escaping moved server-side
    return "plain text"
