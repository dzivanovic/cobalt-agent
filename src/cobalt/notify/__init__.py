"""Outbound channels for the new core. Every one goes through F19.

Two channels, and they are deliberately independent:

    send_dm(text)                      Mattermost — the primary
    send_email(to, subject, body)      Gmail/OAuth — the out-of-band one

Charter §3 F18 requires the second BECAUSE of the first: the DM travels
over Mattermost, which is one of the services the heartbeat watches, so
it cannot carry the news that Mattermost is down. `email.py`'s docstring
states that channel's exact dependency chain — what a send needs, and
the longer list of what it deliberately does not.

The redaction happens inside each sender, at the last point before the
socket — a guard each caller has to remember to call is a guard that
eventually nobody calls.
"""

from .config import (
    CLIENT_ID_KEY,
    CLIENT_SECRET_KEY,
    REFRESH_TOKEN_KEY,
    EmailConfig,
    MattermostConfig,
    NotifyConfig,
    NotifyConfigError,
    load_notify_config,
)
from .email import EmailError, channel_status, send_email
from .mattermost import MattermostError, send_dm
from .result import SendResult
from .store import EmailSendStore, record_attempt

__all__ = [
    "CLIENT_ID_KEY",
    "CLIENT_SECRET_KEY",
    "REFRESH_TOKEN_KEY",
    "EmailConfig",
    "EmailError",
    "EmailSendStore",
    "MattermostConfig",
    "MattermostError",
    "NotifyConfig",
    "NotifyConfigError",
    "SendResult",
    "channel_status",
    "load_notify_config",
    "record_attempt",
    "send_dm",
    "send_email",
]
