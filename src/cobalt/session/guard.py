"""The market_reset hard block. SPRINT-LADDER §S1 F1, Charter §3 F1.

    from cobalt.session import assert_writable

    assert_writable("aset.card", target=ticker)   # raises in market_reset

WHAT IT PROTECTS. 20:00-21:00 ET is the window in which the day's record
is being closed out and `com.cobalt.archiver` pulls the day's bars at
20:30. A card or a note written into that window lands in a day whose
books are being closed, and the L28 incident is exactly what a write
landing at the wrong moment costs. So the answer is a refusal, not a
warning.

THREE THINGS HAPPEN ON A REFUSAL, in this order:

1. `SessionBlocked` is raised, carrying ONE loud message that names the
   window, the current ET clock, and when the block lifts. The caller
   surfaces it; nothing downstream runs.
2. A line goes to the log at ERROR.
3. A row goes to `session_blocks` — the heartbeat-visible counter (F18,
   S1-P3, reads `count_last_24h()`).

Step 3 can fail without changing step 1. The refusal is decided before
anything is written anywhere; a database that is down loses the counter
row and says so at ERROR, and the write still does not happen.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from loguru import logger

from . import clock as clock_mod
from .clock import ET, SessionClock, session_clock
from .models import BLOCKED_SESSION, Session
from .store import SessionBlockStore


class SessionBlocked(RuntimeError):
    """A write was refused because of the session it was attempted in."""

    def __init__(self, message: str, *, session: Session, actor: str):
        super().__init__(message)
        self.session = session
        self.actor = actor


def block_message(clock: SessionClock, ts: datetime, actor: str) -> str:
    """The one loud line. Names the window, the clock, and the lift."""
    et = clock.to_et(ts)
    lifts_at, next_session = clock.next_boundary(ts)
    return (
        f"REFUSED ({actor}): it is {et:%H:%M:%S} ET on {et:%Y-%m-%d} — inside "
        f"MARKET RESET, the {_window_text(clock)} ET hard block. Cobalt writes "
        f"nothing in this window: the day's record is closing and the bar "
        f"archiver runs inside it. The block lifts at "
        f"{lifts_at.astimezone(ET):%H:%M} ET ({next_session})."
    )


def _window_text(clock: SessionClock) -> str:
    windows = {w.session: w for w in clock.windows_for(clock_mod.now_utc().astimezone(ET).date())}
    window = windows.get(BLOCKED_SESSION)
    if window is None:  # today is closed; read the boundaries directly
        return "20:00-21:00"
    return f"{window.start:%H:%M}-{window.end:%H:%M}"


def assert_writable(
    actor: str,
    *,
    target: Optional[str] = None,
    now: Optional[datetime] = None,
    clock: Optional[SessionClock] = None,
    store: Optional[SessionBlockStore] = None,
) -> Session:
    """Refuse the caller if the session forbids writing; else return it.

    `actor` names the write site ("vaultwrite", "aset.card", ...) and is
    what the refusal message, the log line and the counter row all carry.
    `now` is the seam the F1 tests freeze — production passes nothing and
    the clock is read once, here.
    """
    clock = clock or session_clock()
    ts = now or clock_mod.now_utc()
    session = clock.session(ts)

    if session is not BLOCKED_SESSION:
        return session

    message = block_message(clock, ts, actor)
    logger.error(message)
    (store or SessionBlockStore()).record(
        session=session.value, actor=actor, target=target, reason=message
    )
    raise SessionBlocked(message, session=session, actor=actor)
