"""The Mattermost DM channel — new core, and EVERY line goes through F19.

Charter §3 F18: red/green to the daily note + a DM. L14's one-throat law
makes that a direct message, not a room.

WHY THIS IS NOT `cobalt_agent.interfaces.mattermost`. The strangler rule
(CLAUDE.md): the old tree stays runnable and untouched, and no new-core
module imports it. That file is 800 lines of websocket listener, proposal
parsing and brain callbacks; what the heartbeat needs is "open a DM
channel, post a string". This is that, over plain HTTP — no
`mattermostdriver`, no websocket, no shared state with the running agent.

THE ONE RULE THIS MODULE EXISTS TO ENFORCE: nothing leaves without
passing `cobalt.redact.redact()` first. Not a heartbeat block, not an
exception message, not a debug line. The redaction happens HERE, at the
last point before the socket, rather than at each caller — a guard every
caller must remember to call is a guard that eventually nobody calls.

The credential comes from VaultManager and is held for the life of one
send. It is never logged; the sender's own error messages are redacted
before they are raised, because a 401 body can echo the token back.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Optional
from urllib import error as urlerror
from urllib import request as urlrequest

from loguru import logger

from cobalt.redact import redact

from .config import MattermostConfig, load_notify_config

CHANNEL = "mattermost"


class MattermostError(RuntimeError):
    """A DM could not be sent. Message is ALREADY redacted."""


@dataclass
class SendResult:
    sent: bool
    detail: str
    redactions: dict[str, int]

    def report(self) -> str:
        head = "DM sent" if self.sent else "DM NOT sent"
        if self.redactions:
            kinds = ", ".join(f"{k} x{v}" for k, v in sorted(self.redactions.items()))
            return f"{head} — {self.detail} · F19 redacted: {kinds}"
        return f"{head} — {self.detail}"


def _creds(cfg: MattermostConfig) -> tuple[str, str]:
    """(url, token) from the vault. Never logged, never returned upward."""
    from cobalt.redact.secrets import MASTER_KEY_ENV, VAULT_FILE
    import os

    key = os.getenv(MASTER_KEY_ENV)
    if not key:
        raise MattermostError(
            f"{MASTER_KEY_ENV} is not set on this process — the Mattermost "
            "credential cannot be unlocked. Set it on the job that needs to send "
            "(ops/*.plist), or turn the channel off in configs/cobalt/notify.yaml "
            "so the silence is deliberate."
        )
    if not VAULT_FILE.exists():
        raise MattermostError(f"vault file {VAULT_FILE} does not exist.")
    try:
        from cryptography.fernet import Fernet

        data = json.loads(Fernet(key.encode()).decrypt(VAULT_FILE.read_bytes()).decode())
    except Exception as e:  # noqa: BLE001 - type only; a decrypt error can echo material
        raise MattermostError(
            f"vault could not be opened ({type(e).__name__}). The exception text is "
            "deliberately omitted."
        ) from None
    raw = data.get(cfg.vault_key)
    if not raw:
        raise MattermostError(
            f"vault has no entry named {cfg.vault_key!r} (configs/cobalt/notify.yaml)."
        )
    creds = json.loads(raw) if isinstance(raw, str) else raw
    url, token = creds.get("url"), creds.get("token")
    if not url or not token:
        raise MattermostError(
            f"vault entry {cfg.vault_key!r} is missing 'url' or 'token'."
        )
    return url.rstrip("/"), token


def _api(url: str, token: str, path: str, payload: Optional[dict], timeout: float) -> dict:
    req = urlrequest.Request(
        f"{url}/api/v4{path}",
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST" if payload is not None else "GET",
    )
    try:
        with urlrequest.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode() or "{}")
    except urlerror.HTTPError as e:
        body = ""
        try:
            body = e.read().decode()[:400]
        except Exception:  # noqa: BLE001
            pass
        # A 4xx body can contain the request it rejected — token included.
        safe, _ = redact(f"HTTP {e.code} on {path}: {body}", channel=CHANNEL)
        raise MattermostError(safe) from None
    except Exception as e:  # noqa: BLE001
        safe, _ = redact(f"{type(e).__name__} on {path}: {e}", channel=CHANNEL)
        raise MattermostError(safe) from None


def send_dm(message: str, *, cfg: Optional[MattermostConfig] = None) -> SendResult:
    """Redact, then DM. The redaction is not optional and not skippable.

    Returns a `SendResult` rather than raising on a disabled channel: a
    caller (the heartbeat) needs to say IN ITS OWN OUTPUT that the DM did
    not go, which is different from crashing.
    """
    cfg = cfg or load_notify_config().mattermost

    # F19, before anything else touches the wire.
    safe = redact(message, channel=CHANNEL)
    if not safe.clean:
        logger.warning(
            "F19: {} secret(s) redacted from an outbound Mattermost DM ({})",
            safe.total, safe.describe(),
        )

    if not cfg.enabled:
        logger.warning(
            "Mattermost DM channel is DISABLED in configs/cobalt/notify.yaml — "
            "message NOT sent. This is a deliberate setting, not an outage."
        )
        return SendResult(False, "channel disabled in configs/cobalt/notify.yaml", safe.hits)

    url, token = _creds(cfg)
    me = _api(url, token, "/users/me", None, cfg.timeout_s)
    them = _api(url, token, f"/users/username/{cfg.dm_username}", None, cfg.timeout_s)
    channel = _api(
        url, token, "/channels/direct", [me["id"], them["id"]], cfg.timeout_s
    )
    post = _api(
        url, token, "/posts",
        {"channel_id": channel["id"], "message": safe.text},
        cfg.timeout_s,
    )
    return SendResult(True, f"post {post.get('id', '?')} to @{cfg.dm_username}", safe.hits)


__all__ = ["CHANNEL", "MattermostError", "SendResult", "send_dm"]
