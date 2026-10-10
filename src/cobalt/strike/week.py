"""`cobalt strike week [--from <date>] [--to <date>]` — the F9 week report
(S4-P2 S6, DECISION E8). READ-ONLY: writes nothing, anywhere.

Per ET day: TRIGGERED and MISSED counts (S4-P1's seam rows, `seam_kind`),
the DETECT lag `seen_at − bar_close_at` and the PANEL lag
`shown_at − bar_close_at` (n, p50, p95, max; P1's nearest-rank
`measure.percentile`), the DMs sent and their results, the triggers never
shown. DECISION E5: an `intrabar` trigger fires inside its bar, so its
clock is `seen_at` (the first poll that saw the cross) — its panel lag is
`shown_at − seen_at`, reported apart; no number mixes the two clocks.

Unwatchable and capped cards are logged by P1 (`detector.py`), never
written to the database, so this report says so instead of a count.

THE LAST LINE, the verdict against `strike.alert_criterion_s` (P1's
tunable): `F9 CRITERION MET <n>/<n> ≤ <s> s` or `NOT MET — <k> of <n> over
<s> s`, `n` = every TRIGGERED in range; a trigger never shown counts as
over (the alert did not reach the panel), never as met.
"""

from __future__ import annotations

import sys
from collections import Counter
from datetime import date, datetime, timedelta
from typing import Any, Optional

from .measure import _stats

INTRABAR = "intrabar"


def default_range(today: date) -> tuple[date, date]:
    """Monday of `today`'s week through `today` (ET dates, inclusive)."""
    return today - timedelta(days=today.weekday()), today


def _ts(value) -> Optional[datetime]:
    if value is None:
        return None
    return value if isinstance(value, datetime) else datetime.fromisoformat(str(value))


def _lags(trigger, record: Optional[dict[str, Any]]) -> tuple[bool, Optional[float], Optional[float]]:
    """(intrabar, detect lag s, panel lag s) — None where it does not exist."""
    evidence = trigger.evidence or {}
    seen, close = _ts(evidence.get("seen_at")), _ts(evidence.get("bar_close_at"))
    shown = _ts((record or {}).get("shown_at"))
    if evidence.get("policy") == INTRABAR:
        return True, None, None if shown is None or seen is None else (shown - seen).total_seconds()
    detect = None if seen is None or close is None else (seen - close).total_seconds()
    panel = None if shown is None or close is None else (shown - close).total_seconds()
    return False, detect, panel


def _day_lines(label: str, triggers: list, missed: int, records: dict[int, dict[str, Any]]) -> list[str]:
    detect, panel, intrabar_panel, never_shown = [], [], [], 0
    dms: Counter = Counter()
    for row in triggers:
        record = records.get(row.transition_id)
        intrabar, d, p = _lags(row, record)
        if d is not None:
            detect.append(d)
        if p is None:
            never_shown += 1
        elif intrabar:
            intrabar_panel.append(p)
        else:
            panel.append(p)
        if record and record.get("dm_at") is not None:
            dms[record.get("dm_result") or "no result recorded"] += 1
    results = ", ".join(f"{text} ×{n}" for text, n in sorted(dms.items()))
    return [
        f"{label} · TRIGGERED {len(triggers)} · MISSED {missed}",
        f"  DETECT lag s (close-based, seen_at − bar_close_at): {_stats(detect)}",
        f"  PANEL lag s (close-based, shown_at − bar_close_at): {_stats(panel)}",
        f"  intrabar PANEL lag s (shown_at − seen_at): {_stats(intrabar_panel)} · intrabar DETECT: n/a (seen_at is its clock)",
        f"  DMs {sum(dms.values())}" + (f" ({results})" if results else "") + f" · never shown {never_shown}",
    ]


def verdict(triggers: list, records: dict[int, dict[str, Any]], criterion_s: int) -> str:
    if not triggers:
        return "NOT MET — no TRIGGERED in range"
    over = 0
    for row in triggers:
        _intrabar, _detect, panel = _lags(row, records.get(row.transition_id))
        if panel is None or panel > criterion_s:
            over += 1
    n = len(triggers)
    if over == 0:
        return f"F9 CRITERION MET {n}/{n} ≤ {criterion_s} s"
    return f"NOT MET — {over} of {n} over {criterion_s} s"


def week_report(rows: list, records: dict[int, dict[str, Any]], *, criterion_s: int, start: date,
                end: date) -> list[str]:
    from cobalt.aset.strike import seam_kind
    from cobalt.session.clock import ET

    lines = [
        f"strike week {start.isoformat()} → {end.isoformat()} (ET) · strike.alert_criterion_s = {criterion_s} s",
        "unwatchable / capped: not recorded in the database — S4-P1 logs them in the radar's log only",
    ]
    by_day: dict[date, dict[str, list]] = {}
    for row in rows:
        kind = seam_kind(row)
        if kind is None:
            continue
        day = row.at.astimezone(ET).date()
        by_day.setdefault(day, {"trigger": [], "missed": []})[kind].append(row)
    triggers_all, missed_all = [], 0
    for day in sorted(by_day):
        triggers, missed = by_day[day]["trigger"], len(by_day[day]["missed"])
        lines += _day_lines(day.isoformat(), triggers, missed, records)
        triggers_all += triggers
        missed_all += missed
    lines += _day_lines("TOTAL", triggers_all, missed_all, records)
    lines.append(verdict(triggers_all, records, criterion_s))
    return lines


def _source():
    from cobalt.aset.strike import StrikeAlertStore

    return StrikeAlertStore()


def _criterion_s() -> int:
    from .config import check

    return check().alert_criterion_s


def command(args) -> None:
    from cobalt.session import clock as clock_mod
    from cobalt.session.clock import ET

    today = clock_mod.now_utc().astimezone(ET).date()
    first, last = default_range(today)
    start = args.start or first
    end = args.end or last
    if start > end:
        print(f"REFUSED: --from {start.isoformat()} is after --to {end.isoformat()}")
        sys.exit(2)
    source = _source()
    rows = source.seam_rows_between(start, end)
    records = source.records_for([row.transition_id for row in rows])
    for line in week_report(rows, records, criterion_s=_criterion_s(), start=start, end=end):
        print(line)


__all__ = ["command", "default_range", "verdict", "week_report"]
