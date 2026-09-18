"""F7's expiry job: a card whose window has passed is EXPIRED, not left open.

    cobalt cards expire [--at ISO8601] [--dry-run]

WHY EXPIRY IS A JOB AND NOT A PREDICATE. "Is this card still live?"
could be computed on read, but then no transition row would ever be
written for it — and F7's law is that no state changes without one.
A card that quietly stopped counting is exactly the card that makes the
DRC's "unfilled cards reconciled" column wrong. So expiry is an act,
with an actor (`cobalt`), a clock, and evidence naming the window that
elapsed.

THE WINDOW, and the one judgement call in this module. Charter mock
open-question #9: "EXPIRED exists; window per trade_def via
preferred_windows_ref." That field is FREE PROSE written for humans —
the thirteen trade_defs currently carry things like:

    "sheet: 10:00-13:30"
    "First 15 minutes of the trading day"
    "Late morning 10:30-11:59 · Mid-day 12-2 PM · Power hour 3 PM-close"
    "sheet: 9:59-4:00"

It is not a machine contract yet. So the resolver is deliberately
CONSERVATIVE, and the asymmetry driving it is this: falling back to the
session close expires a card LATE (harmless — the job runs again), while
mis-resolving expires it EARLY (it kills a live card that was still in
its window). Under-resolution is safe; over-confidence is not.

`_resolve_window_end` therefore returns a time ONLY when the string is
unambiguous, and returns None — meaning "use the session close" — for
every one of these:

* no clock time in the string at all ("First 15 minutes of the trading day")
* an open-ended tail ("Power hour 3 PM-close"): the latest time found is
  3 PM but the window really runs to the bell, so trusting the max would
  expire the card an hour early
* a bare hour that could be morning or afternoon ("9:59-4:00" — "4:00"
  means 16:00 to a trader and 04:00 to a parser). A bare `H:MM` is
  accepted only when the hour is >= 9, which on the ET trading clock
  cannot be read two ways.

Every fallback is logged at INFO with the string that defeated it, so
the list of refs worth making machine-readable is observable rather than
guessed at. Making them machine-readable is a taxonomy change (a
`preferred_windows` schema with real times), not a parser change — that
belongs to the Rules Engine session, and this module is written to be
deleted from the day it lands.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Any, Optional

from loguru import logger

from cobalt.session import Session, session_clock
from cobalt.session import clock as clock_mod
from cobalt.session.clock import ET

from .models import Actor, CardState
from .store import CardStore

#: The states a card can be sitting in when its window runs out. Every
#: one of them has EXPIRED as a legal edge (models.ALLOWED) — asserted in
#: the tests, so this tuple cannot drift from the edge table.
EXPIRABLE: tuple[CardState, ...] = (CardState.WATCH, CardState.ARMED, CardState.TRIGGERED)

#: A bare `H:MM` with an hour below this is ambiguous on a trading clock
#: ("4:00" = 16:00 to Dejan, 04:00 to a parser) and defeats resolution.
#: NOT a tunable: it is not a threshold anyone would tune, it is the
#: arithmetic fact that 1-8 o'clock happens twice a day and 9-23 does not.
UNAMBIGUOUS_HOUR_FLOOR = 9

#: Words that mean "and onward to the bell" — an open tail the max-time
#: reading would silently truncate.
_OPEN_TAIL = re.compile(r"\b(close|bell|eod|end of day)\b", re.IGNORECASE)
_TIME = re.compile(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\b", re.IGNORECASE)


@dataclass(frozen=True)
class WindowEnd:
    """When a card stops being live, and where that answer came from."""

    at: time
    source: str          # "trade_def" | "session_close"
    detail: str          # the ref that resolved, or why it did not


def _resolve_window_end(ref: Optional[str]) -> Optional[tuple[time, str]]:
    """The trade_def's window end, or None to mean "use the session close"."""
    if not ref or not ref.strip():
        return None
    if _OPEN_TAIL.search(ref):
        return None

    latest: Optional[time] = None
    for raw_hour, raw_minute, meridiem in _TIME.findall(ref):
        hour = int(raw_hour)
        minute = int(raw_minute) if raw_minute else 0
        if meridiem:
            meridiem = meridiem.lower()
            if hour > 12 or hour == 0:
                return None                      # "13 PM" — malformed, do not guess
            if meridiem == "pm" and hour != 12:
                hour += 12
            elif meridiem == "am" and hour == 12:
                hour = 0
        else:
            if not raw_minute:
                continue                          # a bare number is not a clock time
            if hour < UNAMBIGUOUS_HOUR_FLOOR:
                return None                       # "4:00" — could be either half
            if hour > 23:
                return None
        if minute > 59:
            return None
        candidate = time(hour, minute)
        if latest is None or candidate > latest:
            latest = candidate
    if latest is None:
        return None
    return latest, ref.strip()


def window_end_for(trade_def_ref: Optional[str], day: date) -> WindowEnd:
    """When a card on `day` stops being live.

    Falls back to the day's RTH CLOSE, which is 16:00 on a full day and
    13:00 on an early close — read from the session clock's own windows,
    not from a literal, so a half day needs no special case here either
    (the same design F1's `_windows_for` uses).
    """
    resolved = _resolve_window_end(trade_def_ref)
    if resolved is not None:
        at, detail = resolved
        return WindowEnd(at=at, source="trade_def", detail=f"preferred_windows_ref: {detail!r}")

    clock = session_clock()
    windows = {w.session: w for w in clock.windows_for(day)}
    rth = windows.get(Session.RTH)
    if rth is None:
        raise RuntimeError(
            f"{day} is not a trading day, so it has no RTH close to expire cards at "
            f"({clock.calendar.describe(day)}). A card should not exist on it."
        )
    why = (
        "no preferred_windows_ref"
        if not (trade_def_ref or "").strip()
        else f"preferred_windows_ref {trade_def_ref.strip()!r} is not unambiguously resolvable"
    )
    logger.info("cards.expire: falling back to the session close ({}) — {}", rth.end, why)
    return WindowEnd(at=rth.end, source="session_close", detail=why)


def expire_due(
    store: CardStore,
    *,
    now: Optional[datetime] = None,
    dry_run: bool = False,
    trade_def_ref_for: Optional[Any] = None,
) -> list[dict[str, Any]]:
    """EXPIRE every open card whose window has passed. Returns what moved.

    `trade_def_ref_for` is a callable `(card) -> ref | None`. At S1 no
    card carries a `trade_def` yet — the sheet's cards are manual and the
    detector that attaches one lands in S2/S4 — so the default resolves
    to None for every card and every window is the session close. The
    seam exists now so that S2 attaches the trade_def and nothing in this
    module changes.
    """
    ts = now or clock_mod.now_utc()
    et = session_clock().to_et(ts)
    moved: list[dict[str, Any]] = []

    for card in store.open_cards():
        state = CardState(card["state"])
        if state not in EXPIRABLE:
            continue
        created_et = session_clock().to_et(card["created_at"])
        # A card is expired against ITS OWN trading day, not against
        # today: a WATCH card left over from Tuesday is past its window
        # on Wednesday no matter what Wednesday's window is.
        card_day = created_et.date()
        ref = trade_def_ref_for(card) if trade_def_ref_for else None
        window = window_end_for(ref, card_day)
        deadline = datetime.combine(card_day, window.at, tzinfo=ET)
        if et <= deadline:
            continue

        row = {
            "card_id": card["id"],
            "ticker": card["ticker"],
            "from_state": state.value,
            "window_end": f"{card_day} {window.at:%H:%M} ET",
            "window_source": window.source,
        }
        if not dry_run:
            row["transition_id"] = store.transition(
                card["id"],
                CardState.EXPIRED,
                actor=Actor.COBALT,
                evidence={
                    "job": "cobalt cards expire",
                    "window_end": deadline.isoformat(),
                    "window_source": window.source,
                    "window_detail": window.detail,
                    "checked_at": et.isoformat(),
                },
                reason=(
                    f"window closed at {window.at:%H:%M} ET on {card_day} "
                    f"({window.source})"
                ),
                now=ts,
            )
        moved.append(row)
    return moved


__all__ = ["EXPIRABLE", "WindowEnd", "expire_due", "window_end_for"]
