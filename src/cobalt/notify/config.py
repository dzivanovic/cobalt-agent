"""Outbound-channel config (F18/F19). `configs/cobalt/notify.yaml`.

No credential lives here. The Mattermost URL and token come from
VaultManager (`MATTERMOST_CREDS`) exactly as the old tree's did — this
file carries only WHO to talk to and WHETHER the channel is on.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

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


class NotifyConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mattermost: MattermostConfig


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


__all__ = ["CONFIG_PATH", "MattermostConfig", "NotifyConfig", "NotifyConfigError", "load_notify_config"]
