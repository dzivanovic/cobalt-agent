"""F1 session clock — the one place that knows what time it is for Cobalt.

Charter §3 F1: "every card, alert and note carries the session
(premarket 04-09:30 / RTH / aftermarket 16-20 / market_reset 20-21
hard-blocked / overnight); no feature keys off wall-clock."

Three pieces, one law each:

* `clock.py` — sessions are defined in **ET**, storage is **UTC**, and a
  naive datetime is refused rather than guessed at (ADR-0007).
* `calendar.py` — holidays and early closes are **config**, and a year
  with no calendar file is a loud failure, never "probably a weekday".
* `guard.py` — `market_reset` is a **hard block**, not a warning, with a
  log line and a durable counter behind it.

The boundaries themselves are tunables rows (`session.*` in
`configs/cobalt/taxonomy/tunables.yaml`) with named consumers — F16's
"no inline literal in a predicate" applied to the module that is nothing
but boundary predicates.
"""

from .calendar import CalendarError, TradingCalendar, load_calendar
from .clock import ET, SessionClock, SessionError, current_session, session_clock
from .guard import SessionBlocked, assert_writable, block_message, note_ungated
from .models import BLOCKED_SESSION, Session
from .store import SessionBlockStore

__all__ = [
    "BLOCKED_SESSION",
    "ET",
    "CalendarError",
    "Session",
    "SessionBlockStore",
    "SessionBlocked",
    "SessionClock",
    "SessionError",
    "TradingCalendar",
    "assert_writable",
    "block_message",
    "note_ungated",
    "current_session",
    "load_calendar",
    "session_clock",
]
