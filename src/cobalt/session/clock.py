"""The session resolver. Charter §3 F1: "no feature keys off wall-clock."

    from cobalt.session import session_clock
    session_clock().session(ts)   -> Session
    session_clock().next_boundary(ts) -> (when_utc, Session)

WHAT THIS MODULE IS FOR. Two facts have to be held apart and were not:

* **Sessions are defined in ET.** 09:30 means 09:30 America/New_York on
  that date's DST regime, not 09:30 anywhere else and not 13:30 in
  winter.
* **Storage is UTC `timestamptz`.** ADR-0007 (2026-09-04) had to
  reinterpret 4.75M `bars` rows because a naive ET wall clock was
  written into a UTC column and everything downstream read it as UTC.

So `session()` takes a **tz-aware** instant, converts it to ET itself,
and compares against boundaries that are ET wall-clock tunables. A naive
datetime is refused, loudly — that refusal is ADR-0007's lesson encoded
as a precondition rather than trusted to a convention.

BOUNDARY SEMANTICS. Inclusive of its own minute, exclusive of the next:
09:29:59 is `premarket`, 09:30:00.000000 is `rth`. Charter F1's test
pair.

THE DAY IS A WALK, NOT A CASE ANALYSIS. `_windows_for()` builds the
day's ordered [start, end) windows from the tunables and the calendar,
and `session()` walks them. That is why an early close needs no special
case downstream: its aftermarket window simply ends at 17:00, and the
17:00-20:00 gap before `market_reset` falls through to `overnight` the
same way 02:00 does. The archiver still runs at 20:30 on a half day, so
`market_reset` is NOT moved.
"""

from __future__ import annotations

import functools
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo

from cobalt.taxonomy.loader import TaxonomyConfigError, load_tunables
from cobalt.taxonomy.tunables import TunableUnit

from .calendar import CalendarError, TradingCalendar, load_calendar
from .models import Session

#: Sessions are defined in ET and nowhere else (RULING, 2026-09-04).
ET = ZoneInfo("America/New_York")

#: Safety bound on `next_boundary`'s forward walk. NOT a threshold and
#: deliberately NOT a tunables row (F16 is about predicates that encode
#: trading judgement): it is an assertion that the exchange does not
#: close for more than a year, and if it ever trips the answer is a
#: broken calendar, not a number someone should tune.
MAX_CLOSED_RUN_DAYS = 400

#: The tunables rows this module reads. Every boundary is a row with a
#: named consumer (F16) — there is no clock literal anywhere below.
BOUNDARY_KEYS = (
    "session.premarket_open",
    "session.rth_open",
    "session.rth_close",
    "session.aftermarket_close",
    "session.market_reset_open",
    "session.market_reset_close",
    "session.early_close.rth_close",
    "session.early_close.aftermarket_close",
)


class SessionError(RuntimeError):
    """A session could not be resolved — refuse, never guess."""


def now_utc() -> datetime:
    """The ONE system-clock read in the new core.

    Everything that needs "now" — the guard, the vault writer, the ASET
    store, the CLI — calls THIS, as `clock.now_utc()`, through the module
    rather than by importing the name. That indirection is the whole
    point: one `monkeypatch.setattr(clock, "now_utc", ...)` freezes time
    for every caller at once, so the F1 tests can assert 20:30 behaviour
    without sleeping and the rest of the suite cannot go red merely
    because it was run at 20:30 (which it would have, silently, one
    evening).
    """
    return datetime.now(timezone.utc)


@dataclass(frozen=True)
class Window:
    """One [start, end) ET wall-clock window within a single day."""

    session: Session
    start: time
    end: time


def _parse_hhmm(key: str, raw: object) -> time:
    if not isinstance(raw, str):
        raise SessionError(
            f"tunable {key} must be an 'HH:MM' string (unit: time), got "
            f"{type(raw).__name__} {raw!r}"
        )
    try:
        hour, _, minute = raw.partition(":")
        parsed = time(int(hour), int(minute))
    except ValueError as e:
        raise SessionError(f"tunable {key} is not an 'HH:MM' ET time: {raw!r} ({e})") from e
    return parsed


class SessionClock:
    """Boundaries + calendar, resolved once and reused."""

    def __init__(self, boundaries: dict[str, time], calendar: TradingCalendar):
        self._b = boundaries
        self.calendar = calendar

    # -- construction ------------------------------------------------

    @classmethod
    def from_config(cls, calendar: TradingCalendar | None = None) -> "SessionClock":
        try:
            registry = load_tunables().by_key
        except TaxonomyConfigError as e:
            raise SessionError(f"session boundaries unavailable: {e}") from e

        boundaries: dict[str, time] = {}
        for key in BOUNDARY_KEYS:
            row = registry.get(key)
            if row is None:
                raise SessionError(
                    f"tunable {key!r} is missing from tunables.yaml — the session "
                    "clock reads every boundary from config and has no built-in "
                    "default (F16)"
                )
            if row.unit is not TunableUnit.TIME:
                raise SessionError(
                    f"tunable {key!r} has unit {row.unit.value!r}, expected "
                    f"{TunableUnit.TIME.value!r} (an ET wall-clock time-of-day)"
                )
            boundaries[key] = _parse_hhmm(key, row.value)

        clock = cls(boundaries, calendar or load_calendar())
        clock._assert_ordered()
        return clock

    def _assert_ordered(self) -> None:
        """A config edit that crosses two boundaries must crash here, not
        produce a day with a negative-length window."""
        for label, keys in (
            (
                "full day",
                (
                    "session.premarket_open",
                    "session.rth_open",
                    "session.rth_close",
                    "session.aftermarket_close",
                    "session.market_reset_close",
                ),
            ),
            (
                "early-close day",
                (
                    "session.premarket_open",
                    "session.rth_open",
                    "session.early_close.rth_close",
                    "session.early_close.aftermarket_close",
                    "session.market_reset_open",
                    "session.market_reset_close",
                ),
            ),
        ):
            times = [self._b[k] for k in keys]
            if any(a >= b for a, b in zip(times, times[1:])):
                raise SessionError(
                    f"session boundaries are out of order for a {label}: "
                    + ", ".join(f"{k}={self._b[k]:%H:%M}" for k in keys)
                )
        if self._b["session.market_reset_open"] != self._b["session.aftermarket_close"]:
            # Not fatal — an early close already opens such a gap on
            # purpose — but on a FULL day these two are the same instant
            # by design, and a silent divergence would put an unnamed
            # overnight sliver in the middle of the trading evening.
            raise SessionError(
                "session.market_reset_open "
                f"({self._b['session.market_reset_open']:%H:%M}) must equal "
                "session.aftermarket_close "
                f"({self._b['session.aftermarket_close']:%H:%M}) — on a full "
                "day market_reset begins the moment aftermarket ends"
            )

    # -- the day's shape ---------------------------------------------

    def windows_for(self, day: date) -> list[Window]:
        """The ordered [start, end) ET windows of `day`. Empty list = the
        whole day is overnight (weekend or holiday)."""
        if not self.calendar.is_trading_day(day):
            return []

        early = self.calendar.is_early_close(day)
        rth_close = self._b[
            "session.early_close.rth_close" if early else "session.rth_close"
        ]
        am_close = self._b[
            "session.early_close.aftermarket_close" if early else "session.aftermarket_close"
        ]
        return [
            Window(Session.PREMARKET, self._b["session.premarket_open"], self._b["session.rth_open"]),
            Window(Session.RTH, self._b["session.rth_open"], rth_close),
            Window(Session.AFTERMARKET, rth_close, am_close),
            Window(
                Session.MARKET_RESET,
                self._b["session.market_reset_open"],
                self._b["session.market_reset_close"],
            ),
        ]

    # -- the two questions -------------------------------------------

    def session(self, ts: datetime) -> Session:
        """The session `ts` falls in. `ts` MUST be tz-aware."""
        et = self.to_et(ts)
        for window in self.windows_for(et.date()):
            if window.start <= et.time() < window.end:
                return window.session
        return Session.OVERNIGHT

    def next_boundary(self, ts: datetime) -> tuple[datetime, Session]:
        """(when the current session ends, what starts then) — both in
        UTC and as a `Session`. Walks forward day by day, so a Friday
        evening correctly lands on Monday premarket across a weekend, a
        holiday, or both."""
        et = self.to_et(ts)
        current = self.session(ts)

        day = et.date()
        for _ in range(MAX_CLOSED_RUN_DAYS):
            for window in self.windows_for(day):
                boundary_et = datetime.combine(day, window.start, tzinfo=ET)
                if boundary_et > et and window.session != current:
                    return boundary_et.astimezone(ts.tzinfo or ET), window.session
                end_et = datetime.combine(day, window.end, tzinfo=ET)
                if end_et > et and window.session == current:
                    # the current session ends here; what follows is
                    # whatever the walk finds at that instant
                    return (
                        end_et.astimezone(ts.tzinfo or ET),
                        self.session(end_et),
                    )
            day += timedelta(days=1)
        raise SessionError(
            f"no session boundary found within {MAX_CLOSED_RUN_DAYS} days of "
            f"{ts.isoformat()} — "
            "the calendar is almost certainly wrong"
        )

    # -- helpers ------------------------------------------------------

    @staticmethod
    def to_et(ts: datetime) -> datetime:
        """Convert a tz-aware instant to ET. Refuses a naive datetime.

        ADR-0007 in one precondition: a naive datetime has no instant, so
        every answer derived from one is a guess about which zone the
        caller meant. `bars` learned this the expensive way.
        """
        if not isinstance(ts, datetime):
            raise SessionError(f"session() needs a datetime, got {type(ts).__name__}")
        if ts.tzinfo is None or ts.utcoffset() is None:
            raise SessionError(
                f"REFUSED: naive datetime {ts.isoformat()} has no instant — pass a "
                "tz-aware value. Sessions are defined in ET and storage is UTC; "
                "guessing the zone is exactly the defect ADR-0007 had to undo "
                "across 4.75M bars."
            )
        return ts.astimezone(ET)

    def describe(self, ts: datetime) -> str:
        """One line: session, the ET clock, and what the day is."""
        et = self.to_et(ts)
        return (
            f"{self.session(ts)} · {et:%Y-%m-%d %H:%M:%S %Z} · "
            f"{self.calendar.describe(et.date())}"
        )


@functools.lru_cache(maxsize=1)
def session_clock() -> SessionClock:
    """The process-wide clock. Config is read once; a config change needs
    a restart, which is L28's restart-on-deploy rule anyway."""
    return SessionClock.from_config()


def current_session(now: datetime | None = None) -> Session:
    """The session right now (or at `now`, which must be tz-aware).

    `now=None` goes through `now_utc()`, the single system-clock read.
    """
    return session_clock().session(now or now_utc())


__all__ = [
    "BOUNDARY_KEYS",
    "now_utc",
    "ET",
    "CalendarError",
    "SessionClock",
    "SessionError",
    "Window",
    "current_session",
    "session_clock",
]
