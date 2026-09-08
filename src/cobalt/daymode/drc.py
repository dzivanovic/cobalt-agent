"""F6's four inputs, gathered from what actually exists at S1.

Charter §3 F6: the 09:00 reason comes from "prior DRC + running goal +
context". This module fetches the parts that are real today and is
LOUD about the parts that are not — an absent DRC is reported as
`no prior DRC`, never as a blank or an assumed-good day.

WHAT "PRIOR DRC" MEANS AT S1. The DRC prefill (slice 2,
`cobalt.prefill.drc`) writes a note per trading day. There is no DRC
schema in Postgres yet — the numbers live in the note's markdown — so
this reads the FILE: if the prior trading day's DRC note exists, its
stub fields are reported as far as they parse; if it does not exist, or
cannot be read, the literal string `no prior DRC` goes into the reason
and into the sheet banner. Parsing more of the note than its headline
fields is deliberately NOT attempted: a half-understood DRC would let a
wrong number into a risk decision, and CLAUDE.md requires a verbatim
source for any extracted figure.

The FILLED count and the daily-stop marker come from Postgres, where
they are countable — `aset_sizings` rows in state FILLED on that ET
trading date (F7's state, not the retired `status` column).
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from typing import Optional

from loguru import logger

from cobalt import db, env
from cobalt.aset.models import Grade
from cobalt.prefill.config import load_prefill_paths
from cobalt.prefill.vault_writer import resolve_dir

from .propose import NO_PRIOR_DRC, prior_trading_day

#: A daily-stop marker on a prior-day card. Matched case-insensitively
#: against the card's own warnings text — the ONLY place a stop-out is
#: recorded at S1. When F17/F18's jobs table lands (S1-P3) this moves to
#: a real marker row and this regex retires.
_DAILY_STOP = re.compile(r"daily[\s_-]*stop", re.IGNORECASE)


@dataclass(frozen=True)
class PriorDayInputs:
    prior_day: date
    filled_count: int
    daily_stop_hit: bool
    drc_note: Optional[str]     # None means "no prior DRC" — loud, by design
    drc_path: Optional[str]
    #: The note EXISTS and at least one headline field is filled. A DRC
    #: that exists but says nothing is informationally the same as no DRC
    #: for the proposal's purposes — but it is a DIFFERENT sentence in
    #: the reason, because "you did not write one" and "you wrote one and
    #: left it blank" are different facts about his day.
    drc_informative: bool


def _filled_and_stop(prior_day: date) -> tuple[int, bool]:
    """FILLED cards on `prior_day`, and whether any carries a stop marker."""
    try:
        # ADR-0008: this reads `aset_sizings`, so it is a USER-side
        # connection — the same side DayModeStore and AsetStore use.
        with db.connect(env.resolve_db_name(), side=db.Side.USER) as conn:
            row = conn.execute(
                "SELECT count(*) FILTER (WHERE state = 'FILLED'), "
                "       coalesce(string_agg(array_to_string(warnings, ' '), ' '), '') "
                "FROM aset_sizings "
                "WHERE (created_at AT TIME ZONE 'America/New_York')::date = %s",
                (prior_day,),
            ).fetchone()
    except Exception as e:
        # Degraded, not silent: the proposal still happens, and the
        # reason will say the count could not be read.
        logger.error("daymode: could not count prior-day fills ({}: {})", type(e).__name__, e)
        return (0, False)
    if row is None:
        return (0, False)
    return (int(row[0] or 0), bool(_DAILY_STOP.search(row[1] or "")))


def _drc_note(prior_day: date) -> tuple[Optional[str], Optional[str], bool]:
    """(summary, path, informative) for the prior day's DRC note.

    A None summary is the honest answer for a note that does not exist,
    and it becomes the literal `no prior DRC` in the reason string — it
    is never softened into "assume it was fine". `informative` is False
    when the note exists but no headline field is filled: same effect on
    the proposal, different sentence in the reason.
    """
    try:
        paths = load_prefill_paths()
        review_dir = resolve_dir(paths.review_dir)
        note = review_dir / prior_day.strftime(paths.drc_filename_pattern)
    except Exception as e:  # noqa: BLE001 - config OR vault resolution, both degrade the same
        # PrefillConfigError is the expected one; vault resolution can
        # raise its own. Either way the answer is the same and it is
        # LOUD: the reason will carry "no prior DRC" rather than a blank,
        # and the proposal steps down a rung for it.
        logger.error("daymode: DRC path unresolved ({}: {})", type(e).__name__, e)
        return (None, None, False)
    if not note.exists():
        logger.info("daymode: {} — {}", NO_PRIOR_DRC, note)
        return (None, None, False)
    try:
        text = note.read_text(encoding="utf-8")
    except OSError as e:
        logger.error("daymode: DRC note unreadable ({}: {})", type(e).__name__, e)
        return (None, str(note), False)

    # Headline stub fields only. Anything not found is reported as
    # absent rather than inferred.
    grade = _field(text, r"^\s*[-*]?\s*(?:\*\*)?Grade(?:\*\*)?\s*[:|]\s*(.+)$")
    goal = _field(text, r"^\s*[-*]?\s*(?:\*\*)?Goal(?:\*\*)?\s*[:|]\s*(.+)$")

    # A FIELD THAT STILL HOLDS THE TEMPLATE'S PLACEHOLDER IS NOT FILLED.
    # The real 2026-09-03 DRC parsed as `grade (A+, A, B, C, etc..)` —
    # the prompt text out of drc.md.j2, not a grade he wrote. Reported as
    # a value it would have suppressed the "no prior DRC" step-down on a
    # DRC that carries no information at all.
    #
    # The test is exact, not a heuristic on punctuation: a filled grade is
    # one of the ladder's own values, and a filled goal contains a digit.
    # Anything else is a placeholder or prose, and reads as unfilled —
    # which steps the proposal DOWN, the safe direction to be wrong in.
    if grade and grade.strip() not in {g.value for g in Grade}:
        grade = None
    if goal and not any(c.isdigit() for c in goal):
        goal = None

    bits = [f"grade {grade}" if grade else "grade not filled",
            f"goal {goal}" if goal else "goal not filled"]
    informative = bool(grade or goal)
    if not informative:
        logger.info("daymode: {} exists but no headline field is filled", note.name)
    return (f"{note.name} ({', '.join(bits)})", str(note), informative)


def _field(text: str, pattern: str) -> Optional[str]:
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return None
    value = m.group(1).strip().strip("|").strip()
    return value or None


def prior_day_inputs(day: date) -> PriorDayInputs:
    """Everything the 09:00 reason needs about the day before `day`."""
    prior = prior_trading_day(day)
    filled, stop_hit = _filled_and_stop(prior)
    note, path, informative = _drc_note(prior)
    return PriorDayInputs(
        prior_day=prior,
        filled_count=filled,
        daily_stop_hit=stop_hit,
        drc_note=note,
        drc_path=path,
        drc_informative=informative,
    )


__all__ = ["PriorDayInputs", "prior_day_inputs"]
