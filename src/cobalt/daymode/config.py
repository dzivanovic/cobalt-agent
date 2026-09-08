"""F6 config: the mode ladder, the reduced pointer, the attested files,
and the step-down table.

`configs/cobalt/daymode.yaml`, Pydantic-validated on load — a bad or
missing file CRASHES with the file name (config-as-code law, no silent
defaults).

THE ONE IDEA IN THIS MODULE. The mode ladder is not written down
anywhere as a list of names. It is DERIVED:

    modes (low -> high) = ["reduced"] + aset.yaml's sheet_modes.order

so today it is `reduced, half, full`, and the day a quarter sheet is
added to aset.yaml it becomes `reduced, quarter, half, full` with no
edit here and no edit in src/. `reduced` sits at the bottom because it
is the ROLE of the bottom rung, and `reduced_sheet` says which sheet
currently plays it (today `half`).

Everything that could have been a hardcoded name — the floor, the
refusal messages, the grade restriction, the .htk names, the step-down
rules — resolves through this object instead. Cobalt is a product for
many traders: a trader's rung, grades, sheets and thresholds are config
today and profile-scoped later, never code.

THE .HTK NAMES ARE DERIVED TOO (CTO review of S1-P2, 2026-09-04). They
used to be a hand-written `file -> mode` list, which carried an invented
`reduced_day.htk` naming no declared sheet, and mapped files to RUNGS
when a `.htk` is a KEY TABLE and a key table is a SHEET. Now:

    hotkey file for sheet S = hotkey_file_template.format(sheet=S)

one entry per declared sheet, in `order`, and nothing else. The
attestation is therefore about the SHEET he loaded, and it is compared
against `sheet_for(mode)` — the sheet the rung in force sizes from.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from cobalt.aset.config import ConfigError
from cobalt.aset.models import Grade

REPO_ROOT = Path(__file__).resolve().parents[3]
#: SEEDING ONLY (ADR-0008 D3.4) — see `aset/config.py`'s note. The
#: runtime reads `"user".trader_settings`.
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "daymode.yaml"

#: The role name for the bottom rung. It is a ROLE, not a sheet: which
#: sheet plays it is `reduced_sheet`. This is the one mode id that is not
#: a sheet id, which is why it is a named constant rather than a literal
#: sprinkled through the module.
REDUCED = "reduced"

#: The placeholder `hotkey_file_template` must contain — the ONE thing a
#: derived file name is allowed to vary by.
SHEET_PLACEHOLDER = "{sheet}"

#: Every fact id the proposer can compute, with the words the reason uses
#: when the table has no `because` of its own. `stepdowns` must carry a
#: row for each: an id the code can compute but the table does not rule
#: is a silent policy hole, so the loader refuses it (turn a rule OFF
#: with `effect: none`, visibly).
#: What a fired signal costs. `floor` pins the proposal to the lowest
#: enabled rung; `down` walks `rungs` down the ladder; `none` is how a
#: rule is turned OFF visibly, rather than by deleting its row.
EFFECT_FLOOR = "floor"
EFFECT_DOWN = "down"
EFFECT_NONE = "none"
EFFECTS = (EFFECT_FLOOR, EFFECT_DOWN, EFFECT_NONE)

SIGNAL_IDS = (
    "daily_stop_hit",
    "no_prior_drc",
    "drc_not_informative",
    "early_close_today",
    "first_session_after_close",
    "trade_count_band_placeholder",
)


class StepDown(BaseModel):
    """One row of the step-down table: a fact id, and what it costs."""

    model_config = ConfigDict(extra="forbid")

    signal: str = Field(min_length=1)
    effect: str = Field(min_length=1)
    rungs: int = Field(default=1, ge=1)
    because: str = Field(min_length=1)

    @field_validator("signal")
    @classmethod
    def _known_signal(cls, v: str) -> str:
        if v not in SIGNAL_IDS:
            raise ValueError(
                f"unknown step-down signal {v!r}. The proposer can compute: "
                f"{', '.join(SIGNAL_IDS)}. A signal Cobalt cannot compute would "
                "sit in the table looking like a rule and never fire."
            )
        return v

    @field_validator("effect")
    @classmethod
    def _known_effect(cls, v: str) -> str:
        if v not in EFFECTS:
            raise ValueError(
                f"unknown step-down effect {v!r} — must be one of "
                f"{' | '.join(EFFECTS)}."
            )
        return v

    def describe(self, target: str) -> str:
        """The clause that lands in the 09:00 reason, e.g.
        `no prior DRC -> one rung down`."""
        if self.effect == EFFECT_FLOOR:
            return f"{self.because} -> floor"
        if self.effect == EFFECT_NONE:
            return f"{self.because} -> no step-down (ruled off in config)"
        rungs = "one rung down" if self.rungs == 1 else f"{self.rungs} rungs down"
        return f"{self.because} -> {rungs} ({target})"


class DayModeConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    reduced_sheet: str = Field(min_length=1)
    reduced_enabled_grades: list[Grade] = Field(min_length=1)
    enabled_modes: list[str] = Field(min_length=1)
    hotkey_file_template: str = Field(min_length=1)
    stepdowns: list[StepDown] = Field(min_length=1)

    # Populated at load from aset.yaml, not written in daymode.yaml —
    # one path to the sheet order.
    sheet_order: list[str] = Field(default_factory=list)
    account_enabled_grades: list[Grade] = Field(default_factory=list)

    # -- the ladder ---------------------------------------------------

    @property
    def modes(self) -> list[str]:
        """Every mode, LOW to HIGH. Derived, never listed."""
        return [REDUCED, *self.sheet_order]

    def rank(self, mode: str) -> int:
        try:
            return self.modes.index(mode)
        except ValueError as e:
            raise ConfigError(
                f"unknown day mode {mode!r}. The ladder is {' < '.join(self.modes)} "
                f"(derived: '{REDUCED}' plus configs/cobalt/aset.yaml's "
                "sheet_modes.order)."
            ) from e

    @property
    def lowest_enabled(self) -> str:
        """Stage 1's answer: the lowest PERMITTED rung.

        Charter §3 F6 — "before 09:00 the lowest enabled sheet applies by
        system rule". No stop can rest premarket, so this is market
        mechanics, not a personal gate, and it asks him nothing.
        """
        return min(self.enabled_modes, key=self.rank)

    @property
    def highest_enabled(self) -> str:
        return max(self.enabled_modes, key=self.rank)

    def is_enabled(self, mode: str) -> bool:
        return mode in self.enabled_modes

    # -- the reduced role ---------------------------------------------

    def sheet_for(self, mode: str) -> str:
        """Which SHEET (key table) a mode sizes from.

        `reduced` resolves through the pointer; every other mode IS a
        sheet. This is the whole "code says reduced, config says which
        sheet that is" mechanism, in four lines.
        """
        return self.reduced_sheet if mode == REDUCED else mode

    def enabled_grades_for(self, mode: str) -> list[Grade]:
        """The keys permitted on this rung.

        The reduced rung narrows the account ladder to
        `reduced_enabled_grades`; every other mode takes the account
        ladder as-is. Narrowing only — see the validator below.
        """
        return list(self.reduced_enabled_grades if mode == REDUCED else self.account_enabled_grades)

    # -- the attested files (DERIVED from the sheets) ------------------

    def hotkey_file_for_sheet(self, sheet: str) -> str:
        """The `.htk` name for a declared sheet. One template, no list."""
        if sheet not in self.sheet_order:
            raise ConfigError(
                f"no sheet {sheet!r} in configs/cobalt/aset.yaml. Declared sheets "
                f"(low to high): {', '.join(self.sheet_order)}."
            )
        return self.hotkey_file_template.format(sheet=sheet)

    def hotkey_file_for_mode(self, mode: str) -> str:
        """The `.htk` the rung in force expects — via its SHEET."""
        return self.hotkey_file_for_sheet(self.sheet_for(mode))

    @property
    def hotkey_file_names(self) -> list[str]:
        """Exactly one name per declared sheet, in ladder order. THIS is
        the attested-sheet selector on the ASET sheet — a sheet added to
        configs/cobalt/aset.yaml appears in it with no code change."""
        return [self.hotkey_file_for_sheet(s) for s in self.sheet_order]

    def sheet_for_hotkey_file(self, filename: str) -> str:
        """Which SHEET he says he loaded. Refuses a name off the list."""
        for sheet in self.sheet_order:
            if self.hotkey_file_for_sheet(sheet) == filename:
                return sheet
        raise ConfigError(
            f"unknown hotkey file {filename!r}. Declared files (derived from "
            f"configs/cobalt/aset.yaml's sheets via "
            f"daymode.hotkey_file_template={self.hotkey_file_template!r}): "
            f"{', '.join(self.hotkey_file_names)}."
        )

    # -- the step-down table ------------------------------------------

    def stepdown_for(self, signal: str) -> StepDown:
        for row in self.stepdowns:
            if row.signal == signal:
                return row
        raise ConfigError(  # pragma: no cover - the validator forbids this
            f"no step-down row for signal {signal!r} in configs/cobalt/daymode.yaml."
        )

    # -- validation ---------------------------------------------------

    @model_validator(mode="after")
    def _pointers_resolve(self) -> "DayModeConfig":
        if SHEET_PLACEHOLDER not in self.hotkey_file_template:
            raise ValueError(
                f"daymode.hotkey_file_template must contain {SHEET_PLACEHOLDER!r} — "
                f"got {self.hotkey_file_template!r}. Without it every sheet would "
                "derive the same file name and the attestation would mean nothing."
            )
        ruled = [row.signal for row in self.stepdowns]
        dupes = sorted({s for s in ruled if ruled.count(s) > 1})
        if dupes:
            raise ValueError(f"duplicate step-down signal(s): {dupes}")
        unruled = [s for s in SIGNAL_IDS if s not in ruled]
        if unruled:
            raise ValueError(
                f"daymode.stepdowns has no row for {unruled}. Every signal the "
                "proposer can compute must be ruled here — an unruled one would be "
                "a policy hole made by silence. Turn a rule off with `effect: none`."
            )

        if not self.sheet_order:            # pre-population pass
            return self
        if self.reduced_sheet not in self.sheet_order:
            raise ValueError(
                f"daymode.reduced_sheet points at {self.reduced_sheet!r}, which is "
                f"not a declared sheet. Sheets (low to high): "
                f"{', '.join(self.sheet_order)}. A dangling pointer is refused rather "
                "than defaulted to the lowest sheet — the premarket floor and the "
                "live rung both resolve through it, and guessing either is a risk "
                "decision no config error should be allowed to make."
            )
        unknown = [m for m in self.enabled_modes if m not in self.modes]
        if unknown:
            raise ValueError(
                f"daymode.enabled_modes names unknown mode(s) {unknown}. "
                f"The ladder is {' < '.join(self.modes)}."
            )
        widened = [g for g in self.reduced_enabled_grades if g not in self.account_enabled_grades]
        if widened:
            raise ValueError(
                f"daymode.reduced_enabled_grades would WIDEN the account ladder with "
                f"{[g.value for g in widened]}. The reduced rung narrows what "
                f"`aset.enabled_grades` permits "
                f"({[g.value for g in self.account_enabled_grades]}); it can never "
                "permit a key the account itself does not."
            )
        names = self.hotkey_file_names
        dupe_files = sorted({f for f in names if names.count(f) > 1})
        if dupe_files:
            raise ValueError(
                f"daymode.hotkey_file_template {self.hotkey_file_template!r} derives "
                f"duplicate file name(s) {dupe_files} from sheets {self.sheet_order}."
            )
        return self


def load_daymode_config(sheet_modes=None) -> DayModeConfig:
    """The F6 ladder — FROM THE DATABASE (ADR-0008 D3.4).

    Which rung a trader is on, which grades it permits, what makes today
    a smaller day: one person's rulings, so rows in
    `"user".trader_settings` rather than a committed file. Same name,
    same call sites, same object — a different source.

    `sheet_modes` is still accepted so a caller that already resolved the
    sheets does not pay for a second read; it is ignored otherwise,
    because both halves come from the same seven rows.
    """
    from cobalt.settings import TraderSettings, TraderSettingsError

    try:
        return TraderSettings.from_db().daymode
    except TraderSettingsError as e:
        raise ConfigError(str(e)) from e


__all__ = [
    "CONFIG_PATH",
    "EFFECTS",
    "EFFECT_DOWN",
    "EFFECT_FLOOR",
    "EFFECT_NONE",
    "REDUCED",
    "SIGNAL_IDS",
    "DayModeConfig",
    "StepDown",
    "load_daymode_config",
]
