"""X12 (i) / (ii) — card 61 RUN row, FINAL row X12 (R2-1 (c) B).

At BASE no record table exists, so a "record" here is a grade write the
test makes (a scan's create / refresh, or a tap) followed by the card's
`max(card_transitions.id)` read under the card's row lock — exactly the
`transition_id` rule R2-1 (c) B stores. The test keeps `(seq,
transition_id)` itself and applies the ruled rule: the DECISION GRADE is
the last record, by `seq`, whose `transition_id` is less than the id of the
card's first `card_transitions` row with `from_state = 'WATCH'`. Prints the
records and the pick. Asserts nothing (L70).

Inside the suite's rolled-back transaction on the real-shape `world`
fixture (`tests/cobalt/test_radar_cards_db.py:44-93`); constructed values
only (ticker `ZZPB`).
"""

from __future__ import annotations

from datetime import timedelta
from decimal import Decimal

from test_radar_cards_db import SCAN0, world  # noqa: F401 — the with-DB fixture

import pytest

from test_x12_transition_ids_db import requires_db

pytestmark = [requires_db]


def _record(world, card_id, records, label):
    with world["cards"]._connect() as conn:
        conn.execute("SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,))
        tid = conn.execute("SELECT max(id) FROM card_transitions WHERE card_id = %s", (card_id,)).fetchone()[0]
    records.append((len(records) + 1, int(tid), label))


def _decision(world, card_id, records):
    with world["cards"]._connect() as conn:
        first_leave = conn.execute(
            "SELECT min(id) FROM card_transitions WHERE card_id = %s AND from_state = 'WATCH'", (card_id,)
        ).fetchone()[0]
        ledger = conn.execute("SELECT id, from_state, to_state FROM card_transitions WHERE card_id = %s ORDER BY id",
                              (card_id,)).fetchall()
    if first_leave is None:
        return None, ledger, None
    below = [r for r in records if r[1] < first_leave]
    return (below[-1] if below else None), ledger, first_leave


def _size(world, card_id, at):
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.settings.models import TraderSettings

    cards = world["cards"]
    trader = TraderSettings.from_db(world["settings"])
    record = cards.radar_card(card_id)
    sizing = size_at_key(
        Grade.A_PLUS, ticker=record["ticker"], entry=record["entry"], stop=record["stop"],
        direction=Direction(record["direction"]), sheet_modes=trader.sheet_modes, sheet="half",
        enabled=trader.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("10"),
    )
    cards.tap_key(card_id, sizing, now=at)


def _tap(world, card_id, grade, at):
    import inspect

    from cobalt.aset.models import Grade
    from cobalt.settings.card import CardSettings
    from test_radar_cards_db import ENABLED

    cards = world["cards"]
    settings = CardSettings.from_rows(ENABLED)
    if "settings" in inspect.signature(cards.tap_dot).parameters:  # the checker's rerun on <tip>
        return cards.tap_dot(card_id, "trail_fit", grade, settings=settings, enabled=[Grade.A, Grade.B, Grade.C],
                             now=at)
    return cards.tap_dot(card_id, "trail_fit", grade, bands=settings.proposed_key,
                         enabled=[Grade.A, Grade.B, Grade.C], now=at)


def test_x12_i_arm_then_disarm_the_decision_grade_is_the_last_record_before_the_first_leave(world):
    from cobalt.cards import Actor, CardState

    cards = world["cards"]
    records: list = []
    first = world["scan"](SCAN0)
    card_id = first.created[0]
    _record(world, card_id, records, "create (scan SCAN0)")
    _tap(world, card_id, 8, SCAN0 + timedelta(seconds=30))
    _record(world, card_id, records, "tap trail_fit 8")
    second = world["scan"](SCAN0 + timedelta(seconds=100))
    _record(world, card_id, records, f"refresh (scan +100 s, refreshed={second.refreshed})")
    _size(world, card_id, SCAN0 + timedelta(seconds=110))
    arm = cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, now=SCAN0 + timedelta(seconds=120))
    disarm = cards.transition(card_id, CardState.WATCH, actor=Actor.YOU, reason="x12 disarm",
                              now=SCAN0 + timedelta(seconds=140))
    third = world["scan"](SCAN0 + timedelta(seconds=200))
    _record(world, card_id, records, f"refresh (scan +200 s, refreshed={third.refreshed})")
    expired = cards.transition(card_id, CardState.EXPIRED, actor=Actor.COBALT, reason="x12 expiry",
                               now=SCAN0 + timedelta(seconds=300))
    picked, ledger, first_leave = _decision(world, card_id, records)
    print(f"X12 (i): ARM id {arm}, disarm id {disarm}, EXPIRED id {expired}; first from_state='WATCH' id {first_leave}")
    print(f"X12 (i): ledger {ledger}")
    print(f"X12 (i): records (seq, transition_id, what) {records}")
    print(f"X12 (i): the ruled rule picks {picked}")


def test_x12_ii_a_scan_refresh_at_t_committed_after_an_arm_at_t_plus_20s(world):
    from cobalt.cards import Actor, CardState

    cards = world["cards"]
    records: list = []
    card_id = world["scan"](SCAN0).created[0]
    _record(world, card_id, records, "create (scan SCAN0)")
    t = SCAN0 + timedelta(seconds=100)
    _size(world, card_id, t)
    arm = cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, now=t + timedelta(seconds=20))
    later = world["scan"](t)  # the stage's refresh carries now=T and commits after the ARM
    _record(world, card_id, records, f"refresh (scan at T, now=T, refreshed={later.refreshed})")
    picked, ledger, first_leave = _decision(world, card_id, records)
    print(f"X12 (ii): ARM at T+20 s id {arm}; first from_state='WATCH' id {first_leave}; ledger {ledger}")
    print(f"X12 (ii): records (seq, transition_id, what) {records}")
    print(f"X12 (ii): the ruled rule picks {picked}; the refresh at T is picked: "
          f"{picked is not None and picked[0] == 2}")
