"""Outbound channels for the new core. Every one goes through F19.

Today: a Mattermost DM. The redaction happens inside the sender, at the
last point before the socket — a guard each caller has to remember to
call is a guard that eventually nobody calls.
"""

from .config import NotifyConfig, NotifyConfigError, load_notify_config
from .mattermost import MattermostError, SendResult, send_dm

__all__ = [
    "MattermostError",
    "NotifyConfig",
    "NotifyConfigError",
    "SendResult",
    "load_notify_config",
    "send_dm",
]
