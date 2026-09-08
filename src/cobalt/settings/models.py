"""`TraderSettings` — the shapes, unchanged; the home, moved.

The two Pydantic objects the runtime already used (`SheetModesConfig`,
`DayModeConfig`) are untouched: every validator, every derived property,
every error message still lives where it did. What changes is where their
FIELDS come from — seven rows in `"user".trader_settings` instead of two
committed YAML files.

`from_yaml` exists for exactly one purpose: seeding a database from the
files (or from the same files at a git revision, once they have left the
tree). Nothing in the runtime calls it, and a test asserts that
`from_db() == from_yaml()` field-by-field so the move can be proven
rather than believed.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

from cobalt.aset.config import SheetModesConfig
from cobalt.daymode.config import DayModeConfig

#: The `aset.yaml` half, one row each.
SHEET_KEYS = ("aset.sheet_modes", "aset.enabled_grades")

#: The `daymode.yaml` half, one row per top-level setting.
DAYMODE_KEYS = (
    "daymode.reduced_sheet",
    "daymode.reduced_enabled_grades",
    "daymode.enabled_modes",
    "daymode.hotkey_file_template",
    "daymode.stepdowns",
)

#: Every row a complete install carries. A missing one is a loud failure,
#: never a default: a sheet dollar Cobalt invented is a position size
#: nobody chose.
SETTING_KEYS = (*SHEET_KEYS, *DAYMODE_KEYS)

ASET_FILENAME = "aset.yaml"
DAYMODE_FILENAME = "daymode.yaml"


class TraderSettingsError(RuntimeError):
    """Settings missing or invalid — crash, never fall back."""


def _jsonable(value: Any) -> Any:
    """Round-trip through the JSON the column stores, so an in-memory
    Decimal and a Decimal read back from JSONB compare equal."""
    return json.loads(json.dumps(value, default=str))


class TraderSettings(BaseModel):
    """One trader's settings, as the runtime consumes them."""

    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    sheet_modes: SheetModesConfig
    daymode: DayModeConfig

    # -- construction --------------------------------------------------

    @classmethod
    def _build(cls, rows: dict[str, Any], *, where: str) -> TraderSettings:
        missing = [k for k in SETTING_KEYS if k not in rows]
        if missing:
            raise TraderSettingsError(
                f"{where}: missing setting(s) {missing}. Every one of "
                f"{list(SETTING_KEYS)} must be present — there is no default for a "
                "sheet dollar or a step-down rule, because a value Cobalt invented "
                "is a position size nobody chose."
            )
        # A Pydantic failure here is a SETTINGS failure, and it is
        # re-raised as one: the message must name the rows the reader
        # actually read, not leave a caller guessing at a file that is no
        # longer the source. Both halves are built together on purpose —
        # `reduced_enabled_grades` may only narrow `aset.enabled_grades`,
        # and that cross-check has to keep firing now that the two live in
        # separate rows.
        try:
            sheets = SheetModesConfig(
                **rows["aset.sheet_modes"],
                enabled_grades=rows["aset.enabled_grades"],
            )
            daymode = DayModeConfig(
                reduced_sheet=rows["daymode.reduced_sheet"],
                reduced_enabled_grades=rows["daymode.reduced_enabled_grades"],
                enabled_modes=rows["daymode.enabled_modes"],
                hotkey_file_template=rows["daymode.hotkey_file_template"],
                stepdowns=rows["daymode.stepdowns"],
                sheet_order=list(sheets.order),
                account_enabled_grades=list(sheets.enabled_grades),
            )
        except ValidationError as e:
            raise TraderSettingsError(f"{where}: invalid trader settings:\n{e}") from e
        return cls(sheet_modes=sheets, daymode=daymode)

    @classmethod
    def from_db(cls, store=None) -> TraderSettings:
        """The runtime's ONLY reader."""
        from .store import TraderSettingsStore

        s = store or TraderSettingsStore()
        rows = s.values()
        if not rows:
            raise TraderSettingsError(
                'no rows in "user".trader_settings — this install has no trader '
                "settings yet. Seed them with `cobalt settings load --from "
                "configs/cobalt --apply` (or `--from-git <commit>` once the YAMLs "
                "have left the tree). Refusing to size anything without them."
            )
        return cls._build(rows, where='"user".trader_settings')

    @classmethod
    def from_yaml(
        cls,
        directory: Optional[Path] = None,
        *,
        texts: Optional[dict[str, str]] = None,
    ) -> TraderSettings:
        """SEEDING ONLY. `texts` lets a caller supply the two files'
        contents directly — which is how `--from-git` reads them out of
        history without putting them back in the working tree."""
        return cls._build(cls.rows_from_yaml(directory, texts=texts), where="YAML")

    # -- the row layout ------------------------------------------------

    @staticmethod
    def rows_from_yaml(
        directory: Optional[Path] = None,
        *,
        texts: Optional[dict[str, str]] = None,
    ) -> dict[str, Any]:
        """`{key: value}` as the two YAML files define them."""
        if texts is None:
            if directory is None:
                raise TraderSettingsError("from_yaml needs a directory or texts")
            texts = {
                name: (Path(directory) / name).read_text(encoding="utf-8")
                for name in (ASET_FILENAME, DAYMODE_FILENAME)
            }
        for name in (ASET_FILENAME, DAYMODE_FILENAME):
            if name not in texts:
                raise TraderSettingsError(f"no {name} to seed from")

        aset = yaml.safe_load(texts[ASET_FILENAME]) or {}
        daymode = yaml.safe_load(texts[DAYMODE_FILENAME]) or {}
        if "sheet_modes" not in aset:
            raise TraderSettingsError(f"{ASET_FILENAME}: expected a 'sheet_modes' mapping")
        if "daymode" not in daymode:
            raise TraderSettingsError(f"{DAYMODE_FILENAME}: expected a 'daymode' mapping")

        sheet_modes = dict(aset["sheet_modes"])
        enabled_grades = sheet_modes.pop("enabled_grades")
        dm = daymode["daymode"]
        return _jsonable(
            {
                "aset.sheet_modes": sheet_modes,
                "aset.enabled_grades": enabled_grades,
                "daymode.reduced_sheet": dm["reduced_sheet"],
                "daymode.reduced_enabled_grades": dm["reduced_enabled_grades"],
                "daymode.enabled_modes": dm["enabled_modes"],
                "daymode.hotkey_file_template": dm["hotkey_file_template"],
                "daymode.stepdowns": dm["stepdowns"],
            }
        )

    def rows(self) -> dict[str, Any]:
        """This object, back as the seven rows. The inverse of `_build`,
        and what `settings load` compares against."""
        sheets = self.sheet_modes.model_dump(mode="json")
        enabled_grades = sheets.pop("enabled_grades")
        return _jsonable(
            {
                "aset.sheet_modes": sheets,
                "aset.enabled_grades": enabled_grades,
                "daymode.reduced_sheet": self.daymode.reduced_sheet,
                "daymode.reduced_enabled_grades": [
                    g.value for g in self.daymode.reduced_enabled_grades
                ],
                "daymode.enabled_modes": list(self.daymode.enabled_modes),
                "daymode.hotkey_file_template": self.daymode.hotkey_file_template,
                "daymode.stepdowns": [
                    row.model_dump(mode="json") for row in self.daymode.stepdowns
                ],
            }
        )

    def diff(self, other: TraderSettings) -> dict[str, tuple[Any, Any]]:
        """`{key: (mine, theirs)}` for every setting that differs."""
        mine, theirs = self.rows(), other.rows()
        return {
            key: (mine.get(key), theirs.get(key))
            for key in SETTING_KEYS
            if mine.get(key) != theirs.get(key)
        }


__all__ = [
    "ASET_FILENAME",
    "DAYMODE_FILENAME",
    "DAYMODE_KEYS",
    "SETTING_KEYS",
    "SHEET_KEYS",
    "TraderSettings",
    "TraderSettingsError",
]
