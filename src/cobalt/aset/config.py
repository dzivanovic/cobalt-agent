"""ASET config loader — config-as-code (TRIAGE cross-cutting law).

Pydantic-validated on load; a bad or missing file CRASHES with the file
name — no silent defaults. `configs/dev/aset.local.yaml` (gitignored)
REPLACES `configs/dev/aset.yaml` entirely when present — it must be a
complete config — so real account numbers never have to be committed.

Iteration 4 (ruled by Dejan, 2026-08-28): sheet-mode dollar risk
(`configs/cobalt/aset.yaml`) replaces the old daily_stop_default /
broker_hard_stop fields entirely — see models.py / engine.py. It lives
under configs/cobalt/ (shared new-core data, same boundary class as the
Bar Archiver's watchlists.yaml) rather than configs/dev/ because it's
not per-developer settings, it's Dejan's actual trading rule.
"""

from decimal import Decimal
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "aset.yaml"
LOCAL_CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "aset.local.yaml"
SHEET_MODES_CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "aset.yaml"


class ConfigError(RuntimeError):
    """Config missing or invalid — crash loudly."""


class DailyNoteConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # Relative to the resolved vault root (cobalt.vault.resolve_vault_path()
    # — NOT configured here; vault location is the one resolver's job, not
    # ASET's). Exact folder name verified on disk, matches the vault's own
    # .obsidian/daily-notes.json.
    daily_notes_dir: str = Field(min_length=1)
    filename_pattern: str = Field(default="%Y-%m-%d.md", min_length=1)


class ServerConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # "loopback" (127.0.0.1, default) or "lan" (0.0.0.0 — reachable from
    # other devices on the home network). LAN bind serves this page with
    # NO authentication to anyone on the local network — acceptable for
    # now; an access token is a backlog item (see docs/00 - Project/BACKLOG.md).
    bind: Literal["loopback", "lan"] = "loopback"
    port: int = Field(default=5010, gt=0, lt=65536)

    @property
    def host(self) -> str:
        return "127.0.0.1" if self.bind == "loopback" else "0.0.0.0"


class AsetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # Kept for the future computed sizing mode (the real ceiling is 1%
    # of account, dynamic — see configs/cobalt/aset.yaml's header
    # comment). Not read anywhere in the current fixed-dollar sheet-mode
    # math.
    account_size: Decimal = Field(gt=0)
    db_name: str = Field(default="cobalt_dev", min_length=1)
    daily_note: DailyNoteConfig
    server: ServerConfig = Field(default_factory=ServerConfig)


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


class SheetModeGrades(BaseModel):
    model_config = ConfigDict(extra="forbid")

    A: Decimal = Field(gt=0)
    B: Decimal = Field(gt=0)


class SheetModesConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    full: SheetModeGrades
    half: SheetModeGrades

    def dollars_for(self, mode: "SheetMode | str", grade: "Grade | str") -> Decimal:
        # Local imports: keep models.py -> config.py free of a reverse
        # dependency; config.py importing models.py at module scope
        # would still be a one-directional (config depends on models)
        # relationship, but the string-typed signature lets callers
        # pass either enums or raw values without config.py forcing the
        # import on every caller of load_config().
        from cobalt.aset.models import Grade, SheetMode

        mode = SheetMode(mode)
        grade = Grade(grade)
        grades = self.full if mode is SheetMode.FULL else self.half
        if grade is Grade.A:
            return grades.A
        if grade is Grade.B:
            return grades.B
        raise ConfigError(f"no fixed-dollar risk defined for grade {grade!r}")


def load_sheet_modes_config() -> SheetModesConfig:
    path = SHEET_MODES_CONFIG_PATH
    if not path.exists():
        raise ConfigError(
            f"sheet-modes config not found: {path}. "
            "Create it (see configs/cobalt/aset.yaml)."
        )
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict) or "sheet_modes" not in raw:
        raise ConfigError(f"{path}: expected a 'sheet_modes' mapping")
    try:
        return SheetModesConfig(**raw["sheet_modes"])
    except ValidationError as e:
        raise ConfigError(f"{path}: invalid sheet-modes config:\n{e}") from e
