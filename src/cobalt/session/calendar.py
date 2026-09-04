"""The NYSE calendar as config, loaded through the Pydantic path.

`configs/cobalt/calendar/nyse-<year>.yaml` — one file per year, globbed.
Holidays and early closes only; weekends are derived, never listed.

FAIL-LOUD COVERAGE. A `TradingCalendar` answers only for the years it
actually loaded. Ask it about 2027 with no `nyse-2027.yaml` on disk and
it raises `CalendarError` naming the year and the directory. It does not
fall back to "weekday => trading day", because that fallback is silently
wrong exactly on the days that matter most (a holiday would resolve to
`rth`, and every count keyed off the session would inherit the error).
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
CALENDAR_DIR = REPO_ROOT / "configs" / "cobalt" / "calendar"
CALENDAR_GLOB = "nyse-*.yaml"

SATURDAY = 5


class CalendarError(RuntimeError):
    """Calendar config missing, invalid, or asked about an uncovered year."""


class CalendarDay(BaseModel):
    model_config = ConfigDict(extra="forbid")

    date: date
    name: str = Field(min_length=1)


class CalendarYear(BaseModel):
    """One `nyse-<year>.yaml` file."""

    model_config = ConfigDict(extra="forbid")

    year: int = Field(ge=1900, le=2999)
    holidays: list[CalendarDay] = Field(default_factory=list)
    early_closes: list[CalendarDay] = Field(default_factory=list)

    @model_validator(mode="after")
    def _dates_belong_to_this_year(self) -> "CalendarYear":
        for label, days in (("holidays", self.holidays), ("early_closes", self.early_closes)):
            for day in days:
                if day.date.year != self.year:
                    raise ValueError(
                        f"{label} entry {day.date} ({day.name}) is not in year "
                        f"{self.year} — one file covers exactly one year"
                    )
        overlap = {d.date for d in self.holidays} & {d.date for d in self.early_closes}
        if overlap:
            raise ValueError(
                f"date(s) listed as BOTH a holiday and an early close: "
                f"{sorted(overlap)} — a closed day cannot also close early"
            )
        for label, days in (("holidays", self.holidays), ("early_closes", self.early_closes)):
            seen = [d.date for d in days]
            dupes = sorted({d for d in seen if seen.count(d) > 1})
            if dupes:
                raise ValueError(f"duplicate {label} date(s): {dupes}")
        return self


class TradingCalendar:
    """Every loaded year, answering three questions about a date."""

    def __init__(self, years: dict[int, CalendarYear], source: Path):
        self._years = years
        self._source = source
        self._holidays = {d.date: d.name for y in years.values() for d in y.holidays}
        self._early = {d.date: d.name for y in years.values() for d in y.early_closes}

    @property
    def covered_years(self) -> list[int]:
        return sorted(self._years)

    @property
    def holiday_count(self) -> int:
        return len(self._holidays)

    @property
    def early_close_count(self) -> int:
        return len(self._early)

    def _assert_covered(self, day: date) -> None:
        if day.year not in self._years:
            raise CalendarError(
                f"no NYSE calendar for {day.year} (asked about {day}). Loaded "
                f"years: {self.covered_years or 'none'}. Add "
                f"{self._source}/nyse-{day.year}.yaml — this never guesses a "
                "trading day from the weekday alone."
            )

    def is_weekend(self, day: date) -> bool:
        return day.weekday() >= SATURDAY

    def holiday_name(self, day: date) -> str | None:
        self._assert_covered(day)
        return self._holidays.get(day)

    def early_close_name(self, day: date) -> str | None:
        self._assert_covered(day)
        return self._early.get(day)

    def is_early_close(self, day: date) -> bool:
        return self.early_close_name(day) is not None

    def is_trading_day(self, day: date) -> bool:
        """A weekday that is not an exchange holiday. An early close IS a
        trading day — it just ends sooner."""
        if self.is_weekend(day):
            return False
        return self.holiday_name(day) is None

    def describe(self, day: date) -> str:
        """One human line for the CLI and for refusal messages."""
        if self.is_weekend(day):
            return f"{day} is a weekend ({day:%A}) — not a trading day"
        holiday = self.holiday_name(day)
        if holiday:
            return f"{day} is an NYSE holiday ({holiday}) — not a trading day"
        early = self.early_close_name(day)
        if early:
            return f"{day} is an early close ({early})"
        return f"{day} is a full trading day"


def load_calendar(directory: Path = CALENDAR_DIR) -> TradingCalendar:
    """Load every `nyse-*.yaml` in `directory`. No files = crash."""
    if not directory.exists() or not directory.is_dir():
        raise CalendarError(f"calendar directory not found: {directory}")

    files = sorted(directory.glob(CALENDAR_GLOB))
    if not files:
        raise CalendarError(
            f"no {CALENDAR_GLOB} files in {directory} — the session clock has "
            "no calendar and will not invent one"
        )

    years: dict[int, CalendarYear] = {}
    for file in files:
        raw = yaml.safe_load(file.read_text())
        if not isinstance(raw, dict):
            raise CalendarError(
                f"{file}: expected a YAML mapping, got {type(raw).__name__}"
            )
        try:
            parsed = CalendarYear(**raw)
        except ValidationError as e:
            raise CalendarError(f"{file}: invalid NYSE calendar:\n{e}") from e
        if parsed.year in years:
            raise CalendarError(
                f"{file}: year {parsed.year} is already covered by another "
                "calendar file — one file per year (one-path rule)"
            )
        years[parsed.year] = parsed

    return TradingCalendar(years, directory)
