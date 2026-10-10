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
from typing import TYPE_CHECKING, Literal

import yaml
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)

from .models import Grade

if TYPE_CHECKING:  # quoted annotation only — dollars_for takes an id or an enum
    from .models import SheetMode

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "aset.yaml"
LOCAL_CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "aset.local.yaml"
#: SEEDING ONLY (ADR-0008 D3.4). The runtime reads
#: `"user".trader_settings`; this path is where `cobalt settings load
#: --from configs/cobalt` looks, and after the file leaves the tree the
#: seed comes from `--from-git <commit>` instead.
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
    # LAW L28 containment lever (2026-09-03). The 09-03 containment
    # session had to stop the whole ASET LaunchAgent to stop its
    # daily-note writes, because no flag existed to separate "serve the
    # sheet" from "write the journal". With this false, sizing, the
    # Postgres persist and the whole sheet keep working and the note
    # write becomes a LOUD, logged no-op (aset/daily_note.py) with a
    # visible banner on the page. Default true — off is a deliberate,
    # visible act, never the silent state.
    write_enabled: bool = True


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
    # RULING 7 (2026-09-04): `db_name` is DELETED, not defaulted.
    # configs/dev/aset.local.yaml pinned it to cobalt_dev for every
    # caller, so the PRODUCTION sheet and both prefill jobs wrote live
    # cards and their L28 audit trail into the dev database alongside
    # pytest rows. The database is not a per-component setting any
    # more: it comes from COBALT_ENV via cobalt.env.resolve_db_name().
    # extra="forbid" above means a leftover `db_name:` key in a config
    # file is now a LOUD crash, not a silently honoured override.
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
    """The sheets, as an ORDERED CONFIG LIST — never a hardcoded pair.

    RULED 2026-09-04 (S1-P2, F6): "Sheets are an ordered config list from
    aset.yaml — today [half, full]; a quarter sheet will be added later
    as a config row + its .htk, so never hardcode the count or names."

    Before this the model carried `full:` and `half:` as two literal
    fields and `dollars_for` branched `self.full if mode is FULL else
    self.half` — so a third rung could not be added without editing this
    class, which is exactly the anti-rigidity rule CLAUDE.md opens with.
    Now `sheets` is a mapping keyed by whatever ids the config declares
    and `order` lists them low -> high; adding a quarter sheet is a
    config row and nothing else here changes.

    `order` is explicit rather than relying on YAML mapping order: dict
    insertion order happens to survive pyyaml today, but "which rung is
    lower" is a trading fact and it is not going to rest on an
    implementation detail of the parser.
    """

    model_config = ConfigDict(extra="forbid")

    #: Sheet id -> its fixed-dollar key table. Ids are the config's, not
    #: this module's: `half`, `full`, and `quarter` when it exists.
    sheets: dict[str, SheetModeGrades] = Field(min_length=1)
    #: The rungs, LOW to HIGH. F6's "lowest enabled sheet" reads this.
    order: list[str] = Field(min_length=1)
    # UI/compute availability, separate from the dollar truth above.
    # Enabling a grade later is a config edit here — never a code
    # change (see engine.compute_sizing, which takes this as an
    # explicit argument rather than reading a hardcoded constant).
    enabled_grades: list[Grade] = Field(min_length=1)

    @model_validator(mode="after")
    def _order_covers_every_sheet(self) -> "SheetModesConfig":
        missing = [s for s in self.sheets if s not in self.order]
        unknown = [s for s in self.order if s not in self.sheets]
        if missing or unknown:
            raise ValueError(
                f"sheet_modes.order must name every sheet exactly once — "
                f"declared but unordered: {missing or 'none'}; "
                f"ordered but undeclared: {unknown or 'none'}. "
                "F6 resolves 'the lowest enabled sheet' from this list, so a "
                "rung missing from it would silently never be reachable."
            )
        if len(set(self.order)) != len(self.order):
            raise ValueError(f"duplicate sheet id(s) in sheet_modes.order: {self.order}")
        return self

    def dollars_for(self, mode: "SheetMode | str", grade: "Grade | str") -> Decimal:
        """Fixed dollars for (sheet, grade). Takes an enum or a raw id.

        The signature is unchanged from the two-field version — callers
        (web.py, prefill/daily.py, the tests) pass `"full"` / `"half"` and
        keep working.
        """
        sheet_id = getattr(mode, "value", mode)
        grades = self.sheets.get(str(sheet_id))
        if grades is None:
            raise ConfigError(
                f"no sheet {str(sheet_id)!r} in `aset.sheet_modes` "
                f'("user".trader_settings). Declared sheets (low to high): '
                f"{', '.join(self.order)}."
            )
        return getattr(grades, _FIELD_BY_GRADE[Grade(grade)])

    def is_enabled(self, grade: "Grade | str") -> bool:
        return Grade(grade) in self.enabled_grades

    @property
    def lowest_sheet(self) -> str:
        """The bottom rung as declared. F6's stage-1 floor resolves
        through `daymode.reduced_sheet`, not through this — but a config
        whose order disagrees with the pointer is worth being able to
        see."""
        return self.order[0]


def load_sheet_modes_config() -> SheetModesConfig:
    """The sheets and the account grade ladder — FROM THE DATABASE.

    ADR-0008 D3.4: these are the trader's own numbers, so they are rows in
    `"user".trader_settings`, not a committed file. The function keeps its
    name and its twenty-odd call sites; what changed is where it reads.
    `configs/cobalt/aset.yaml` is gone from the runtime — it survives only
    as a seed that `cobalt settings load` can be pointed at, in a
    directory or at a git revision.

    The local import is the import cycle's price: `cobalt.settings` builds
    `SheetModesConfig`, which lives here.
    """
    from cobalt.settings import TraderSettings, TraderSettingsError

    try:
        return TraderSettings.from_db().sheet_modes
    except TraderSettingsError as e:
        raise ConfigError(str(e)) from e
