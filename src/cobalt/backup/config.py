"""Backup config (`configs/cobalt/backup.yaml`).

Pydantic-validated on load; a bad row CRASHES with its field. No
credential lives here — the restic repository password and the B2 keys
are named by VAULT KEY only, the same shape
`configs/cobalt/notify.yaml` uses for `MATTERMOST_CREDS`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "backup.yaml"


class BackupConfigError(RuntimeError):
    """Missing/invalid backup config — crash, never fall back."""


class Destination(BaseModel):
    """One restic repository.

    `enabled` is deliberately separate from `repo` being set: a
    destination that is configured but switched off is a visible,
    reviewable state, whereas an empty string that silently means "off"
    is the kind of thing a backup discovers on the day it is needed.
    """

    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    kind: Literal["local", "b2"]
    repo: str = ""
    enabled: bool = False

    @model_validator(mode="after")
    def _enabled_needs_a_repo(self) -> "Destination":
        if self.enabled and not self.repo.strip():
            raise ValueError(
                f"destination {self.name!r} is enabled but has no `repo`. An armed "
                "destination with nowhere to write is the failure this config exists "
                "to make impossible."
            )
        return self

    def restic_repo(self) -> str:
        """The value restic's `-r` wants."""
        return self.repo if self.kind == "local" else f"b2:{self.repo}"


class ForgetPolicy(BaseModel):
    """Retention. Ruled: daily 14 / weekly 8 / monthly 12."""

    model_config = ConfigDict(extra="forbid")

    daily: int = Field(gt=0)
    weekly: int = Field(gt=0)
    monthly: int = Field(gt=0)

    def restic_args(self) -> list[str]:
        return [
            "--keep-daily", str(self.daily),
            "--keep-weekly", str(self.weekly),
            "--keep-monthly", str(self.monthly),
        ]

    def describe(self) -> str:
        return f"daily {self.daily} / weekly {self.weekly} / monthly {self.monthly}"


class DatabaseSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = True
    name: str = Field(min_length=1)


class BackupConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sources: list[Path] = Field(min_length=1)
    database: DatabaseSpec
    excludes: list[str] = Field(default_factory=list)
    destinations: list[Destination] = Field(min_length=1)
    password_vault_key: str = Field(min_length=1)
    b2_key_id_vault_key: str = Field(min_length=1)
    b2_app_key_vault_key: str = Field(min_length=1)
    forget: ForgetPolicy

    @model_validator(mode="after")
    def _unique_names(self) -> "BackupConfig":
        names = [d.name for d in self.destinations]
        dupes = sorted({n for n in names if names.count(n) > 1})
        if dupes:
            raise ValueError(f"duplicate destination name(s): {dupes}")
        return self

    @property
    def armed(self) -> list[Destination]:
        return [d for d in self.destinations if d.enabled]


def load_backup_config(path: Path = CONFIG_PATH) -> BackupConfig:
    if not path.exists():
        raise BackupConfigError(
            f"backup config not found: {path}. There is no built-in default: a "
            "backup nobody declared is a backup nobody has."
        )
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict) or "backup" not in raw:
        raise BackupConfigError(f"{path}: expected a 'backup' mapping")
    try:
        return BackupConfig(**raw["backup"])
    except ValidationError as e:
        raise BackupConfigError(f"{path}: invalid backup config:\n{e}") from e


__all__ = [
    "CONFIG_PATH",
    "BackupConfig",
    "BackupConfigError",
    "DatabaseSpec",
    "Destination",
    "ForgetPolicy",
    "load_backup_config",
]
