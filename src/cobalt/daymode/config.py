"""F6 config: the mode ladder, the reduced pointer, the attested files.

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
refusal messages, the grade restriction, the .htk mapping — resolves
through this object instead.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from cobalt.aset.config import ConfigError, load_sheet_modes_config
from cobalt.aset.models import Grade

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "daymode.yaml"

#: The role name for the bottom rung. It is a ROLE, not a sheet: which
#: sheet plays it is `reduced_sheet`. This is the one mode id that is not
#: a sheet id, which is why it is a named constant rather than a literal
#: sprinkled through the module.
REDUCED = "reduced"


class HotkeyFile(BaseModel):
    """One real `.htk` on the trading PC, and the mode it means."""

    model_config = ConfigDict(extra="forbid")

    file: str = Field(min_length=1)
    mode: str = Field(min_length=1)


class DayModeConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    reduced_sheet: str = Field(min_length=1)
    reduced_enabled_grades: list[Grade] = Field(min_length=1)
    enabled_modes: list[str] = Field(min_length=1)
    hotkey_files: list[HotkeyFile] = Field(min_length=1)

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

    # -- the attested files -------------------------------------------

    @property
    def hotkey_file_names(self) -> list[str]:
        return [h.file for h in self.hotkey_files]

    def mode_for_hotkey_file(self, filename: str) -> str:
        for entry in self.hotkey_files:
            if entry.file == filename:
                return entry.mode
        raise ConfigError(
            f"unknown hotkey file {filename!r}. Declared files: "
            f"{', '.join(self.hotkey_file_names)} (configs/cobalt/daymode.yaml)."
        )

    # -- validation ---------------------------------------------------

    @model_validator(mode="after")
    def _pointers_resolve(self) -> "DayModeConfig":
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
                f"configs/cobalt/aset.yaml permits ({[g.value for g in self.account_enabled_grades]}); "
                "it can never permit a key the account itself does not."
            )
        for entry in self.hotkey_files:
            if entry.mode not in self.modes:
                raise ValueError(
                    f"hotkey file {entry.file!r} maps to unknown mode {entry.mode!r}. "
                    f"The ladder is {' < '.join(self.modes)}."
                )
        files = self.hotkey_file_names
        dupes = sorted({f for f in files if files.count(f) > 1})
        if dupes:
            raise ValueError(f"duplicate hotkey file name(s): {dupes}")
        return self


def load_daymode_config(sheet_modes=None) -> DayModeConfig:
    """Load F6 config, resolving the sheet ladder from aset.yaml."""
    if not CONFIG_PATH.exists():
        raise ConfigError(
            f"day-mode config not found: {CONFIG_PATH}. "
            "Create it (see configs/cobalt/daymode.yaml)."
        )
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    if not isinstance(raw, dict) or "daymode" not in raw:
        raise ConfigError(f"{CONFIG_PATH}: expected a 'daymode' mapping")
    sheets = sheet_modes or load_sheet_modes_config()
    try:
        return DayModeConfig(
            **raw["daymode"],
            sheet_order=list(sheets.order),
            account_enabled_grades=list(sheets.enabled_grades),
        )
    except ValidationError as e:
        raise ConfigError(f"{CONFIG_PATH}: invalid day-mode config:\n{e}") from e


__all__ = ["CONFIG_PATH", "REDUCED", "DayModeConfig", "HotkeyFile", "load_daymode_config"]
