"""FINAL §9 point (1)/(4), [F-16] (1), [F-21] — the fixture cut's PIN
(prompt `12-setups-fixture-cut.md`). Closes rubberband's `AWAITING_A_DAY`
pin on a stored pool day the DEFINITION forms on: the real stored day (see
the fixture-cut report of prompt `12`, `## FIND — rubberband`), re-dated 2026-01-07, selected by the engine's own `--expect-formed` exit
code (STEP-2, R24 — never a day because he traded or tagged it; the
fixture-cut report has the replay command and its exit code).

R24 BINDS EVERY TEST: every `DEF_WRITTEN_*` constant below is the value the
ENGINE computes from the definition's FULL shape (`setups_shapes.SHAPES`)
on the committed real-shape cut bars — a blind house re-derives each one
(prompt `13-setups-blind-values.md`, FINAL [F-16] (1)).

hitchhiker is NOT pinned here: none of the six most-recent stored pool days
forms it on the production-synced definition (its pin stays in
`test_setups_lego.py`'s `AWAITING_A_DAY`; see the fixture-cut report).
"""

from __future__ import annotations

import json
from datetime import date, datetime
from zoneinfo import ZoneInfo

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.radar.evaluate import MemberInput, evaluate_member
from cobalt.radar.evaluate_cli import admitted_at, scan_instants
from cobalt.session import session_clock

SLUG = "rubberband"
SYNTHETIC_DAY = date(2026, 1, 7)


def _cut_membership() -> list[dict]:
    rows = json.loads((sup.FIXTURES / f"membership-setups-{SLUG}.real-shape.json").read_text())
    out = []
    for r in rows:
        out.append({
            "id": r["id"], "ticker": r["ticker"],
            "trade_date": date.fromisoformat(r["trade_date"]),
            "entered_at": datetime.fromisoformat(r["entered_at"]),
            "left_at": datetime.fromisoformat(r["left_at"]) if r["left_at"] else None,
        })
    return out


def _cut_bars(ticker: str) -> list:
    return sup.fixture_bars(ticker, filename=f"bars-setups-{SLUG}.real-shape.json")


def _cut_daily(ticker: str):
    return sup.fixture_daily(ticker, filename=f"daily-bars-setups-{SLUG}.real-shape.csv")


def _formations(ld) -> list:
    """The replay's own grid (`evaluate_cli.scan_instants` + `admitted_at`)
    over the cut membership window, `radar.scan_interval` from the engine
    tunables — mirrors `replay_formations` read-only, no writes."""
    members = _cut_membership()
    rows = shapes.tunables_for(ld)
    scan_interval = int(rows["radar.scan_interval"].value)
    clock = session_clock()
    admitted_ever = [m for m in members if m.get("entered_at") is not None]
    first = min((m["entered_at"] for m in admitted_ever), default=None)
    bars_cache: dict[str, list] = {}
    out = []
    for instant in scan_instants(SYNTHETIC_DAY, clock, scan_interval, first) if admitted_ever else []:
        for member in admitted_at(members, instant):
            ticker = member["ticker"]
            if ticker not in bars_cache:
                bars_cache[ticker] = _cut_bars(ticker)
            inp = MemberInput(
                membership_id=member["id"], ticker=ticker, trade_date=SYNTHETIC_DAY, as_of=instant,
                bars=tuple(b for b in bars_cache[ticker] if b.ts < instant),
                daily=_cut_daily(ticker), daily_status="cache-hit",
            )
            ev = evaluate_member(ld, inp, tunables=rows, defaults=sup.defaults(),
                                 scan_interval=scan_interval, clock=clock)
            if ev.evaluation == "formed":
                out.append((instant, ev))
    return out


def test_rubberband_cut_day_engine_output():
    """Printing test — the blind seat's comparison source (`13`)."""
    ld = shapes.load_shape_fresh("rubberband")
    formed = _formations(ld)
    assert formed, "expected at least one formation on the cut day"
    at, ev = formed[0]
    f = ev.formation
    print(
        f"CUT ENGINE OUTPUT side={f.trade_direction} formed_bar_ts={f.formed_bar_ts.isoformat()} "
        f"trigger.price={f.trigger.price} stop.price={f.stop.price} anchor={f.anchor!r} "
        f"scan_instant={at.isoformat()} "
        f"formed_bar_ny={f.formed_bar_ts.astimezone(ZoneInfo('America/New_York')).isoformat()}"
    )


# --- FINAL §9 point (1): the five values, from the DEFINITION on the cut bars ---
# engine on the corrected cut day at R4-F4 on 8da261a; a blind house re-derives it (13, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_CUT_SIDE = "short"
# engine on the corrected cut day at R4-F4 on 8da261a; a blind house re-derives it (13, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_CUT_FORMED_BAR = datetime.fromisoformat("2026-01-07T15:24:00+00:00")
# engine on the corrected cut day at R4-F4 on 8da261a; a blind house re-derives it (13, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_CUT_TRIGGER = "0.6690"
# engine on the corrected cut day at R4-F4 on 8da261a; a blind house re-derives it (13, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_CUT_STOP = "0.87"
# engine on the corrected cut day at R4-F4 on 8da261a; a blind house re-derives it (13, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_CUT_ANCHOR = (
    "Anchor(object='Extension', direction='up', "
    "bar_ts=datetime.datetime(2026, 1, 7, 15, 24, tzinfo=datetime.timezone.utc))"
)


def test_rubberband_forms_on_the_cut_day():
    ld = shapes.load_shape_fresh("rubberband")
    formed = _formations(ld)
    assert formed
    at, ev = formed[0]
    f = ev.formation
    assert f.trade_direction == DEF_WRITTEN_RUBBERBAND_CUT_SIDE
    assert f.formed_bar_ts == DEF_WRITTEN_RUBBERBAND_CUT_FORMED_BAR
    assert str(f.trigger.price) == DEF_WRITTEN_RUBBERBAND_CUT_TRIGGER
    assert str(f.stop.price) == DEF_WRITTEN_RUBBERBAND_CUT_STOP
    assert repr(f.anchor) == DEF_WRITTEN_RUBBERBAND_CUT_ANCHOR
    # geometry guard ([F-16] (5)): stop on the correct side of trigger for the direction
    if f.trade_direction == "short":
        assert f.stop.price > f.trigger.price
    else:
        assert f.stop.price < f.trigger.price
