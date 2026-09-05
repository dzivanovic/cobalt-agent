"""F19 exfiltration guard — one function, on every outbound channel.

    from cobalt.redact import redact
    safe, hits = redact(text, channel="mattermost")

Two halves, because one is not enough (see `configs/cobalt/redact.yaml`):
PATTERNS catch anything token-shaped, in text nobody has seen before; the
LITERAL guard catches the human usernames and passwords no shape can
describe, matched against the values VaultManager holds.

A hit is redacted AND counted. The count reaches the F18 heartbeat; the
value reaches nothing — not a log line, not an exception message, not a
counter row. `redactions` has no column that could hold one.
"""

from .config import RedactConfig, RedactConfigError, load_redact_config
from .guard import LITERAL_PREFIX, RedactResult, install_log_guard, redact
from .secrets import load_literals
from .store import RedactionStore

__all__ = [
    "LITERAL_PREFIX",
    "RedactConfig",
    "RedactConfigError",
    "RedactResult",
    "RedactionStore",
    "install_log_guard",
    "load_literals",
    "load_redact_config",
    "redact",
]
