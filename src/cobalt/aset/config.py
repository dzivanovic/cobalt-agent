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

Config-completion follow-up (Dejan, 2026-08-28): the grade ladder now
carries the FULL truth (A+/A/B/C/D dollar figures, D always $0) with
UI/compute availability tracked separately via `enabled_grades` — see
`SheetModesConfig`.
"""

from decimal import Decimal
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from .models import Grade

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


class ValidationConfig(BaseModel):
    """Typo guards for the ASET card (slice 2.1a, 2026-08-31 defects
    D2/D3) — thresholds only, resolved by callers (web.py) and passed
    explicitly into engine.compute_sizing / compute_fill_recompute so
    the engine itself stays config-agnostic. Optional section: a config
    file that omits it gets these defaults, same pattern as ServerConfig."""

    model_config = ConfigDict(extra="forbid")

    # D3: a 32% PCG stop typo (13.72 fat-fingered as 17.72) went
    # unflagged. Not a trading rule — just a sanity ceiling on how far a
    # stop can be from entry before it's more likely a typo than a plan.
    max_stop_distance_pct: Decimal = Field(default=Decimal("10"), gt=0)
    # D2: a 2518.91 fill against a 218.595 entry computed to 0 shares
    # and was persisted twice before the real 218.91 fill came in.
    max_fill_distance_pct: Decimal = Field(default=Decimal("5"), gt=0)


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
    validation: ValidationConfig = Field(default_factory=ValidationConfig)


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


# Config completion (Dejan, 2026-08-28): the full grade ladder — every
# grade carries a real dollar figure now, D always $0 (SAW principle,
# enforced below, not left to convention).
_FIELD_BY_GRADE = {
    Grade.A_PLUS: "A_plus",
    Grade.A: "A",
    Grade.B: "B",
    Grade.C: "C",
    Grade.D_SAW: "D",
}


class SheetModeGrades(BaseModel):
    model_config = ConfigDict(extra="forbid")

    A_plus: Decimal = Field(gt=0)
    A: Decimal = Field(gt=0)
    B: Decimal = Field(gt=0)
    C: Decimal = Field(gt=0)
    D: Decimal = Field(ge=0)

    @field_validator("D")
    @classmethod
    def _d_is_always_zero(cls, v: Decimal) -> Decimal:
        if v != 0:
            raise ValueError("D (SAW) risk must always be 0 — the SAW principle is non-negotiable")
        return v


class SheetModesConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    full: SheetModeGrades
    half: SheetModeGrades
    # UI/compute availability, separate from the dollar truth above.
    # Enabling a grade later is a config edit here — never a code
    # change (see engine.compute_sizing, which takes this as an
    # explicit argument rather than reading a hardcoded constant).
    enabled_grades: list[Grade] = Field(min_length=1)

    def dollars_for(self, mode: "SheetMode | str", grade: "Grade | str") -> Decimal:
        # Local import of SheetMode only (Grade is already a module-level
        # import, needed for the enabled_grades field's type itself) —
        # the string-typed signature lets callers pass either enums or
        # raw values without forcing every load_config() caller through
        # models.py's SheetMode too.
        from cobalt.aset.models import SheetMode

        mode = SheetMode(mode)
        grade = Grade(grade)
        grades = self.full if mode is SheetMode.FULL else self.half
        return getattr(grades, _FIELD_BY_GRADE[grade])

    def is_enabled(self, grade: "Grade | str") -> bool:
        return Grade(grade) in self.enabled_grades


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
