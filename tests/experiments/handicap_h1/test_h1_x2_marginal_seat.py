"""X2 (v3; grok X2 / Fable X2; `29` §4 — FIRST): replay `decide()` scan
by scan over the 2026-09-18 retained RTH scans with HIS pool block (read
through the existing reader, never printed) and record, for every RTH scan
after the `first_from` time:

- `first_from equity < seats` — the equity names on the `first_from`
  screen against `seats` (= cap − held);
- `all screens < seats` — every equity name on a live screen against seats;
- the marginal seat's TIER, tallied.

Counts and relations only: no cap, no seat count, no time, no ticker (L32).

TIER of the marginal seat, one rule per scan, first match wins:
`held`       — held members took seats (`held > 0`);
`stickiness` — a sticky member displaced a newcomer (a RETAIN whose
               `below_cap_streak > 0` this scan);
`none`       — nothing was cut (every ranked name admitted);
`priority`   — the last admitted and the first cut differ in group
               (screens / lists);
`first_from` — both are screen names and exactly one sits on the
               `first_from` screen after its time;
`position`   — otherwise (same group and same `first` flag).
"""

from __future__ import annotations

from collections import Counter
from datetime import date

import pytest
from h1_support import CACHE, config, et_hhmm, his_sources, replay, retained_days

from cobalt.radar.pool import Action, _source_key
from cobalt.session import session_clock
from cobalt.session.models import Session

WANTED = date(2026, 9, 18)


def _first_from(pool):
    hits = [
        (key, override.first_from)
        for key, override in pool.overrides.items()
        if override.first_from is not None
    ]
    return hits[0] if hits else (None, None)


def _tier(replayed, pool, ff_key, ff_time) -> str:
    transitions = replayed.decision.transitions
    held = sum(t.action is Action.HOLD for t in transitions)
    if held:
        return "held"
    if any(t.action is Action.RETAIN and t.below_cap_streak > 0 for t in transitions):
        return "stickiness"
    ranked = sorted((t for t in transitions if t.rank is not None and t.action is not Action.HOLD),
                    key=lambda t: t.rank)
    admitted = [t for t in ranked if t.action in {Action.ADMIT, Action.RETAIN}]
    cut = [t for t in ranked if t.action in {Action.EXCLUDE, Action.LEAVE}]
    if not cut or not admitted:
        return "none"
    last, first_cut = max(admitted, key=lambda t: t.rank), min(cut, key=lambda t: t.rank)

    def group(t):
        return "screens" if (t.source or "").startswith("screen:") else "lists"

    if group(last) != group(first_cut):
        return "priority"
    after = et_hhmm(replayed.scan.instant) >= ff_time if ff_time else False

    def on_ff(t):
        return after and group(t) == "screens" and ff_key is not None and (
            (t.source or "").split(":", 1)[-1].split("@", 1)[0] == ff_key
        )

    if on_ff(last) != on_ff(first_cut):
        return "first_from"
    return "position"


def test_x2_marginal_seat_tier_on_the_retained_rth_scans():
    days = retained_days()
    wanted = CACHE / WANTED.isoformat()
    day_dir = wanted if wanted in days else days[0]
    if day_dir != wanted:
        print(f"X2: {WANTED} not retained — ran on the oldest retained day {day_dir.name}")
    cfg = config()
    parsed = his_sources(cfg)
    assert parsed.pool is not None, "his screens note has no pool block"
    ff_key, ff_time = _first_from(parsed.pool)
    clock = session_clock()
    scans = rth = after = 0
    ff_lt = all_lt = 0
    tiers: Counter[str] = Counter()
    for replayed in replay(day_dir, parsed, cfg):
        scans += 1
        if clock.session(replayed.scan.instant) is not Session.RTH:
            continue
        rth += 1
        if not ff_time or et_hhmm(replayed.scan.instant) < ff_time:
            continue
        after += 1
        held = sum(t.action is Action.HOLD for t in replayed.decision.transitions)
        seats = max(0, parsed.pool.cap - held)
        screens = replayed.live_screens()
        ff = [s for s in screens if _source_key(s) == ff_key]
        ff_equity = {t for s in ff for t in replayed.equity(s)}
        all_equity = {t for s in screens for t in replayed.equity(s)}
        ff_lt += len(ff_equity) < seats
        all_lt += len(all_equity) < seats
        tiers[_tier(replayed, parsed.pool, ff_key, ff_time)] += 1
    print(f"X2: day {day_dir.name} · scans {scans} · RTH scans {rth} · RTH scans after first_from {after}")
    print(f"X2: first_from equity < seats: {ff_lt} of {after} scans")
    print(f"X2: all screens < seats: {all_lt} of {after} scans")
    print("X2: marginal-seat tier tally: " + ", ".join(f"{k} {v}" for k, v in sorted(tiers.items())))
    print(f"X2: every marginal seat decided on position: {set(tiers) <= {'position', 'none'}}")
    assert after > 0, "no RTH scan after first_from was replayed"
