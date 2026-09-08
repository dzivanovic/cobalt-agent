"""Outbound-channel config (F18/F19). `configs/cobalt/notify.yaml`.

No credential lives here. The Mattermost URL and token come from
VaultManager (`MATTERMOST_CREDS`) exactly as the old tree's did, and the
Gmail OAuth triple from `GOOGLE_OAUTH_*` — this file carries only WHO to
talk to and WHETHER the channel is on.

NO THRESHOLD LIVES HERE EITHER, and that is F16 rather than taste. The
email channel needs two numbers — the loopback port the consent flow
binds and the HTTP timeout on a send — and both are thresholds with
consumers, so both are `tunables.yaml` rows (`notify.email.auth_port`,
`notify.email.timeout_s`) reached through `cobalt.taxonomy.loader`. The
Mattermost block's own `timeout_s` predates that sweep and is left where
it is: moving a live production field is a change with no proof attached
to it, and F16's rule binds every NEW threshold.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "notify.yaml"


class NotifyConfigError(RuntimeError):
    """Missing/invalid notify config — crash, never fall back."""


class MattermostConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    #: Off by default is NOT the posture here: a heartbeat that silently
    #: stops DM-ing is a heartbeat that has stopped. `enabled: false` is a
    #: deliberate, visible act, and the sender says so out loud.
    enabled: bool = True
    #: The username Cobalt opens a direct channel with.
    dm_username: str = Field(min_length=1)
    #: Vault key holding {"url": ..., "token": ...} — the name only.
    vault_key: str = Field(default="MATTERMOST_CREDS", min_length=1)
    timeout_s: float = Field(default=10.0, gt=0)


#: Vault key names for the Layer-B Google OAuth credential (Charter §3
#: F18's out-of-band channel). NAMES, in code, never values — and not in
#: the YAML either: a config file that named its own secret keys would
#: invite someone to paste the values next to them one day.
#:
#: Three separate top-level entries rather than one JSON blob, because
#: the F19 literal guard reports a hit by its VAULT KEY NAME: a leaked
#: refresh token shows up in the heartbeat as
#: `literal:GOOGLE_OAUTH_REFRESH_TOKEN`, which says exactly which
#: credential to rotate. A blob would have reported the parent key and
#: left an operator guessing.
CLIENT_ID_KEY = "GOOGLE_OAUTH_CLIENT_ID"
CLIENT_SECRET_KEY = "GOOGLE_OAUTH_CLIENT_SECRET"
REFRESH_TOKEN_KEY = "GOOGLE_OAUTH_REFRESH_TOKEN"


class EmailConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    #: Charter §3 F18's SECOND channel. `false` is a loud, logged no-op
    #: exactly as it is for Mattermost — the heartbeat says the channel
    #: is off in its own block rather than appearing to have sent.
    enabled: bool = True
    #: The recipient. One address: L14's one-throat law again, and a
    #: distribution list is a place an alert goes to be ignored.
    to: str = Field(min_length=3)
    #: Prepended to every subject, so a mail rule can catch the channel
    #: without parsing the body.
    subject_prefix: str = Field(default="[COBALT]", min_length=1)

    @field_validator("to")
    @classmethod
    def _looks_like_an_address(cls, v: str) -> str:
        # Not RFC 5322 — deliberately. The one failure worth catching at
        # config time is a placeholder someone forgot to replace, and
        # that is what an @ with something either side of it catches.
        local, _, domain = v.partition("@")
        if not local or "." not in domain:
            raise ValueError(
                f"notify.email.to={v!r} is not an email address. The out-of-band "
                "alert channel has no default recipient (F18)."
            )
        return v


class NotifyConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mattermost: MattermostConfig
    email: EmailConfig


def load_notify_config() -> NotifyConfig:
    if not CONFIG_PATH.exists():
        raise NotifyConfigError(
            f"notify config not found: {CONFIG_PATH}. There is no built-in default: "
            "an alert channel nobody declared is an alert channel nobody checks."
        )
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    if not isinstance(raw, dict) or "notify" not in raw:
        raise NotifyConfigError(f"{CONFIG_PATH}: expected a 'notify' mapping")
    try:
        return NotifyConfig(**raw["notify"])
    except ValidationError as e:
        raise NotifyConfigError(f"{CONFIG_PATH}: invalid notify config:\n{e}") from e


__all__ = [
    "CLIENT_ID_KEY",
    "CLIENT_SECRET_KEY",
    "CONFIG_PATH",
    "EmailConfig",
    "MattermostConfig",
    "NotifyConfig",
    "NotifyConfigError",
    "REFRESH_TOKEN_KEY",
    "load_notify_config",
]
