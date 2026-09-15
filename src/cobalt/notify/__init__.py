"""Outbound channels for the new core. Every one goes through F19.

One channel:

    send_dm(text)                      Mattermost

The second, out-of-band channel Charter §3 F18 asked for — Gmail over
Layer-B Google OAuth, built at S1-P4 — was RETIRED 2026-09-14 (executed
2026-09-15): Google's Publish step for the `gmail.send` scope is gated on
restricted-scope verification, so the OAuth client never left Testing
and its refresh token expired every seven days. `heartbeat/runner.py`'s
docstring carries the consequence. The channel's send-log table stays in
the database as history.

The redaction happens inside the sender, at the last point before the
socket — a guard each caller has to remember to call is a guard that
eventually nobody calls.
"""

from .config import (
    MattermostConfig,
    NotifyConfig,
    NotifyConfigError,
    load_notify_config,
)
from .mattermost import MattermostError, send_dm
from .result import SendResult

__all__ = [
    "MattermostConfig",
    "MattermostError",
    "NotifyConfig",
    "NotifyConfigError",
    "SendResult",
    "load_notify_config",
    "send_dm",
]
