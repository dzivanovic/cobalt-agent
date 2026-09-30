"""The DRC settings family — ONE reader of the daily stop and the dollars
per grade (DRC D4; v2 §5 T9 [F-18] / [F-16], his R95 / R96 / R102).

    load_drc_settings(conn)      every DRC key; absent -> None
    daily_risk_values(conn)      the daily stop + the grade dollars
    propose_daily_change(form)   the ASET change line's reviewed payload

WHY ONE READER. The daily stop used to be a number typed into the
committed daily-note template, and the dollars per grade lived in the
`aset.sheet_modes` row: two places, and the template's copy was his value
sitting in git. R95 ruled ONE place; R96 / R102 ruled that place is the
central settings (`"user".trader_settings`), changed by his change line
in ASET and SHOWN in the daily note. So every DRC or daily-note path that
needs either number calls `daily_risk_values` — the daily stop from the
`account.*` rows, the grade dollars from `load_sheet_modes_config()` (the
existing `aset.sheet_modes` row; a second copy would be an L3 defect).

`conn` is the settings source: a `TraderSettingsStore`, or any object
with `.values() -> {key: value}`; `None` opens the default store. It is
what D3's `drc-risk/facts` unit passes (L72 seam).

ABSENT IS `not given` (L1). A DRC key with no row is `None`, and every
caller renders `not given`; nothing here supplies a default. A row that IS
present but invalid is a stored value known false — that is loud
(`TraderSettingsError` naming the key), never skipped.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Any, Mapping, Optional, Protocol

from pydantic import BaseModel, ConfigDict, ValidationError

from cobalt.aset.config import SheetModeGrades, SheetModesConfig, load_sheet_modes_config
from cobalt.aset.models import Grade

from .cli import payload_sha256
from .models import (
    DAILY_STOP_KEYS,
    DRC_FAMILIES,
    DrcAccountSettings,
    DrcGoalSettings,
    DrcKey,
    DrcLimitsSettings,
    DrcWindowsSettings,
    TraderSettingsError,
    _jsonable,
)
from .store import TraderSettingsStore

#: The existing row that carries the dollars per grade (ADR-0008 D3.4).
SHEET_MODES_KEY = "aset.sheet_modes"

#: How every caller renders an absent value (L1).
NOT_GIVEN = "not given"

#: `SheetModeGrades`' fields, low to high, and how the page labels them.
GRADE_FIELDS = tuple(SheetModeGrades.model_fields)
_GRADE_LABEL = {"A_plus": Grade.A_PLUS.value, "A": "A", "B": "B", "C": "C", "D": "D"}


class SettingsSource(Protocol):
    def values(self) -> dict[str, Any]: ...


def _values(conn: Optional[SettingsSource]) -> dict[str, Any]:
    return (conn if conn is not None else TraderSettingsStore()).values()


class DrcSettings(BaseModel):
    """Every DRC key family this slice reads. Every leaf is Optional."""

    model_config = ConfigDict(frozen=True)

    account: DrcAccountSettings
    limits: DrcLimitsSettings
    windows: DrcWindowsSettings
    goal: DrcGoalSettings


def load_drc_settings(conn: Optional[SettingsSource] = None) -> DrcSettings:
    """THE reader of the DRC keys. A key with no row is `None`; a present
    row that does not validate raises naming the key."""
    rows = _values(conn)
    families: dict[str, BaseModel] = {}
    for family, model in DRC_FAMILIES.items():
        present = {
            field: DrcKey(f"{family}.{field}").validate(rows[f"{family}.{field}"])
            for field in model.model_fields
            if f"{family}.{field}" in rows
        }
        families[family] = model(**present)
    return DrcSettings(**families)


class DailyRisk(BaseModel):
    """The daily stop (per sheet; `None` = not given) and the grade
    dollars (the sheets, low to high)."""

    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)

    daily_stop: dict[str, Optional[Decimal]]
    sheet_modes: SheetModesConfig

    @property
    def grade_dollars(self) -> dict[str, dict[str, Decimal]]:
        return {
            sheet: {g.value: self.sheet_modes.dollars_for(sheet, g) for g in Grade}
            for sheet in self.sheet_modes.order
        }


def daily_risk_values(conn: Optional[SettingsSource] = None) -> DailyRisk:
    """THE ONLY function on any DRC or daily-note path that returns the
    daily stop or the dollars per grade (L3). A missing `aset.sheet_modes`
    row is the sheet's own loud `ConfigError` — it is a required key."""
    account = load_drc_settings(conn).account
    stops = {sheet: getattr(account, key.partition(".")[2]) for sheet, key in DAILY_STOP_KEYS.items()}
    return DailyRisk(daily_stop=stops, sheet_modes=load_sheet_modes_config())


def shown(value: Optional[Decimal]) -> str:
    """A value as the page and the note print it: `not given` when absent."""
    return NOT_GIVEN if value is None else str(value)


# ---------------------------------------------------------------------
# The change line (D4-4): what the ASET page shows and proposes
# ---------------------------------------------------------------------


class ChangeField(BaseModel):
    """One input of the change line: its form name (the settings key, or
    `aset.sheet_modes.<sheet>.<grade>`), a label, and the current value
    as text ('' when not given)."""

    name: str
    label: str
    current: str


def change_line_fields(risk: DailyRisk) -> list[ChangeField]:
    fields = [
        ChangeField(
            name=key, label=f"daily stop · {sheet}",
            current="" if risk.daily_stop.get(sheet) is None else str(risk.daily_stop[sheet]),
        )
        for sheet, key in DAILY_STOP_KEYS.items()
    ]
    for sheet in risk.sheet_modes.order:
        grades = risk.sheet_modes.sheets[sheet]
        fields.extend(
            ChangeField(
                name=f"{SHEET_MODES_KEY}.{sheet}.{g}",
                label=f"{sheet} {_GRADE_LABEL[g]}",
                current=str(getattr(grades, g)),
            )
            for g in GRADE_FIELDS
        )
    return fields


class DailyChangeInvalid(TraderSettingsError):
    """The change line's input failed validation. Every message names its
    field; nothing is written."""

    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("refused — nothing written:\n" + "\n".join(errors))


class DailyChange(BaseModel):
    """The reviewed proposal: the rows that would change, a per-field diff
    (field, old, new) and the sha256 of the payload."""

    payload: dict[str, Any]
    diff: list[tuple[str, str, str]]
    sha256: str


def _number(name: str, raw: str, errors: list[str]) -> Optional[Decimal]:
    try:
        value = Decimal(raw)
    except InvalidOperation:
        errors.append(f"{name}: not a number ({raw!r})")
        return None
    if not value.is_finite():
        errors.append(f"{name}: not a number ({raw!r})")
        return None
    return value


def propose_daily_change(
    form: Mapping[str, str], conn: Optional[SettingsSource] = None
) -> DailyChange:
    """Validate the change line's form against what is stored now and
    return the payload that would be written.

    A BLANK daily-stop field leaves that key as it is. A blank grade field
    is refused ("a grade with no dollar"): every grade carries a dollar
    figure, D always 0. Every failure names its field and ALL of them are
    reported together; any failure means nothing is proposed, so a
    partial write cannot be built.
    """
    risk = daily_risk_values(conn)
    errors: list[str] = []
    payload: dict[str, Any] = {}
    diff: list[tuple[str, str, str]] = []

    for sheet, key in DAILY_STOP_KEYS.items():
        raw = (form.get(key) or "").strip()
        if not raw or _number(key, raw, errors) is None:
            continue
        try:
            typed = DrcKey(key).validate(raw)
        except TraderSettingsError as e:
            errors.append(str(e))
            continue
        old = risk.daily_stop.get(sheet)
        if old != typed:
            payload[key] = DrcKey(key).from_rows({key: raw}).row()
            diff.append((key, shown(old), str(typed)))

    sheets: dict[str, SheetModeGrades] = {}
    grade_diff: list[tuple[str, str, str]] = []
    for sheet in risk.sheet_modes.order:
        typed_grades: dict[str, Decimal] = {}
        for g in GRADE_FIELDS:
            name = f"{SHEET_MODES_KEY}.{sheet}.{g}"
            raw = (form.get(name) or "").strip()
            if not raw:
                errors.append(
                    f"{name}: a grade with no dollar — every grade carries a dollar "
                    "figure (D is always 0)"
                )
                continue
            value = _number(name, raw, errors)
            if value is not None:
                typed_grades[g] = value
        if len(typed_grades) != len(GRADE_FIELDS):
            continue
        try:
            new = SheetModeGrades(**typed_grades)
        except ValidationError as e:
            for err in e.errors():
                field = err["loc"][0] if err["loc"] else "(grades)"
                errors.append(f"{SHEET_MODES_KEY}.{sheet}.{field}: {err['msg']}")
            continue
        current = risk.sheet_modes.sheets[sheet]
        for g in GRADE_FIELDS:
            if getattr(current, g) != getattr(new, g):
                grade_diff.append(
                    (f"{SHEET_MODES_KEY}.{sheet}.{g}", str(getattr(current, g)), str(getattr(new, g)))
                )
        sheets[sheet] = new

    if errors:
        raise DailyChangeInvalid(errors)
    if grade_diff:
        cfg = SheetModesConfig(
            sheets=sheets,
            order=list(risk.sheet_modes.order),
            enabled_grades=list(risk.sheet_modes.enabled_grades),
        )
        row = cfg.model_dump(mode="json")
        row.pop("enabled_grades")
        payload[SHEET_MODES_KEY] = _jsonable(row)
        diff.extend(grade_diff)
    return DailyChange(payload=payload, diff=diff, sha256=payload_sha256(payload))


__all__ = [
    "ChangeField",
    "DailyChange",
    "DailyChangeInvalid",
    "DailyRisk",
    "DrcSettings",
    "NOT_GIVEN",
    "SHEET_MODES_KEY",
    "change_line_fields",
    "daily_risk_values",
    "load_drc_settings",
    "propose_daily_change",
    "shown",
]
