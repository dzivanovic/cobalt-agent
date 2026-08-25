"""ASET config loader — config-as-code (TRIAGE cross-cutting law).

Pydantic-validated on load; a bad or missing file CRASHES with the file
name — no silent defaults. `configs/dev/aset.local.yaml` (gitignored)
REPLACES `configs/dev/aset.yaml` entirely when present — it must be a
complete config — so real account numbers never have to be committed.
"""

from decimal import Decimal
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "aset.yaml"
LOCAL_CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "aset.local.yaml"


class ConfigError(RuntimeError):
    """Config missing or invalid — crash loudly."""


class DailyNoteConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # Absolute path, or relative to the repo root. Currently the docs/
    # playground vault; live-vault migration is a scheduled design decision.
    vault_path: str = Field(min_length=1)
    inbox_dir: str = Field(min_length=1)
    filename_pattern: str = Field(default="%Y-%m-%d.md", min_length=1)


class AsetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    account_size: Decimal = Field(gt=0)
    # Broker-enforced max daily loss. The sheet clamps at this value and
    # REFUSES anything above it, server-side included.
    broker_hard_stop: Decimal = Field(gt=0)
    # Morning-set daily stop; absent → account_size / 50. Always capped
    # by broker_hard_stop.
    daily_stop_default: Optional[Decimal] = Field(default=None, gt=0)
    db_name: str = Field(default="cobalt_dev", min_length=1)
    daily_note: DailyNoteConfig


def load_config() -> AsetConfig:
    path = LOCAL_CONFIG_PATH if LOCAL_CONFIG_PATH.exists() else CONFIG_PATH
    if not path.exists():
        raise ConfigError(
            f"ASET config not found: {path}. Create it (see configs/dev/aset.yaml)."
        )
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise ConfigError(f"{path}: expected a YAML mapping, got {type(raw).__name__}")
    try:
        return AsetConfig(**raw)
    except ValidationError as e:
        raise ConfigError(f"{path}: invalid ASET config:\n{e}") from e
