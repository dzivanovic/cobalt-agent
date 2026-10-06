"""X7, X10, X11 — card 2026-10-04/02 RUN row X (FINAL `## First-gate
experiments` `:435`, `:438`, `:439`).

Each prints what it measured and asserts nothing about the design (L70).
Inside the suite's rolled-back transaction on the real-shape `world`
fixture (`tests/cobalt/test_radar_cards_db.py:44-96`), `0022` applied there
only (L76); constructed values only (ticker `ZZPB`).
"""

from __future__ import annotations

import os
from datetime import datetime, time, timedelta
from decimal import Decimal

import pytest

from predictions_db_support import records_of
from test_radar_cards_db import ENABLED, SCAN0, world  # noqa: F401 — the with-DB fixture

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db]


def _tap(world, card_id, factor, grade, at):
    from cobalt.aset.models import Grade
    from cobalt.settings.card import CardSettings

    return world["cards"].tap_dot(card_id, factor, grade, settings=CardSettings.from_rows(ENABLED),
                                  enabled=[Grade.A, Grade.B, Grade.C], now=at)


def test_x7_numeric_8_6_conviction_read_back_after_scoring_conviction(world):
    from cobalt.cards.scoring import conviction

    cards = world["cards"]
    card_id = world["scan"](SCAN0).created[0]
    for i, (factor, grade) in enumerate((("trail_fit", 7), ("setup_relation", 8))):
        _tap(world, card_id, factor, grade, SCAN0 + timedelta(seconds=30 + i))
    with cards._connect() as conn:
        stored = conn.execute("SELECT conviction FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()[0]
        dots = cards._dots_for(conn, [card_id])[card_id]
    written = conviction(dots)
    rec = records_of(cards, card_id)[-1]
    print(f"X7: scoring.conviction() -> {written!r} (str {str(written)!r})")
    print(f"X7: psycopg read of NUMERIC(8,6) aset_sizings.conviction -> {stored!r} (str {str(stored)!r})")
    print(f"X7: the tap record's output.conviction -> {rec['output']['conviction']!r}")
    print(f"X7: reprs equal: {repr(written) == repr(stored)}; strings equal: {str(written) == str(stored)}; "
          f"Decimal values equal: {written == stored}")


def test_x10_a_records_output_after_the_jsonb_round_trip_vs_published_numbers(world):
    from cobalt.cards.predictions import write_record
    from cobalt.cards.scoring import Dot
    from cobalt.radar.evaluate import CardUpdate, published_numbers

    cards = world["cards"]
    first = world["scan"](SCAN0)
    card_id = first.created[0]
    chain = cards.receipts_chain(cards.receipt_for_run(first.run_id))
    published = next(c["published"] for c in chain[-1]["tap_versions"]["cards"] if c["card_id"] == card_id)
    create = records_of(cards, card_id)[0]
    stored = {k: v for k, v in create["output"].items() if k != "proposed_key_reason"}
    print(f"X10 (a) the create record's output (JSONB, read back) == the receipt's published_numbers: "
          f"{stored == published}")
    for key in published:
        if stored.get(key) != published[key]:
            print(f"X10 (a) differs at {key}: record {stored.get(key)!r} vs receipt {published[key]!r}")

    dot = Dot(factor="rvol", position=0, source="cobalt", tier="deterministic", role="shadow",
              engine_value=Decimal("4.200000"), engine_grade=7)
    update = CardUpdate(card_id=card_id, proximity=Decimal("0.512300"), conviction=Decimal("0.7"), card_score=36,
                        score_suppressed=None, proposed_key="B", dots=[dot], health=None, radar_score_id=None)
    numbers = published_numbers(update)
    with cards._connect() as conn:
        conn.execute("SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,))
        rid = write_record(conn, card_id=card_id, kind="refresh", at=SCAN0, run_id=first.run_id,
                           scorer_version=create["scorer_version"], formula_sha256=create["formula_sha256"],
                           settings_sha256=create["settings_sha256"], inputs={"taps_moved": False, "locked": None},
                           output={**numbers, "proposed_key_reason": None})
        back = conn.execute("SELECT output FROM prediction_records WHERE id = %s", (rid,)).fetchone()[0]
    back = {k: v for k, v in back.items() if k != "proposed_key_reason"}
    print(f"X10 (b) published_numbers(...) written: {numbers}")
    print(f"X10 (b) read back after JSONB: {back}")
    print(f"X10 (b) equal as stored (no canonical compare): {back == numbers}")


@pytest.mark.parametrize("entry", ["as formed", "never reached"])
def test_x11_a_card_that_expires_untriggered_then_the_nightly_card_replay(world, entry):
    from cobalt.archiver.models import Interval
    from cobalt.archiver.store import BarStore
    from cobalt.cards import Actor, CardState
    from cobalt.replay.cards import MissedStore, replay_card, resolve_window, session_close_for
    from cobalt.session.clock import ET
    from radar_p2_support import TRADE_DATE

    cards = world["cards"]
    card_id = world["scan"](SCAN0).created[0]
    print(f"X11 [{entry}]")
    with cards._connect() as conn:
        # A real card's created_at is its scan's instant; inside this suite
        # transaction now() is the wall clock, so the constructed card is put
        # back on its scan (the rolled-back transaction only).
        conn.execute("UPDATE aset_sizings SET created_at = %s WHERE id = %s", (SCAN0, card_id))
        if entry == "never reached":
            # The same card with an entry the day's bars never print through
            # (short: a sell-stop far below every low) — the no_trigger walk.
            conn.execute("UPDATE aset_sizings SET entry = 0.0100 WHERE id = %s", (card_id,))
    cards.transition(card_id, CardState.EXPIRED, actor=Actor.COBALT, reason="x11 deadline",
                     evidence={"cause": "deadline"}, now=SCAN0 + timedelta(minutes=30))
    print(f"X11: card {card_id} ledger {cards.history(card_id) and [(r['from_state'], r['to_state']) for r in cards.history(card_id)]}")

    # The nightly replay's cards step (`replay/runner.py:415-444`), on this
    # one trade date, through its own functions and the real stores.
    missed = MissedStore("cobalt_dev")
    candidates = missed.candidates(TRADE_DATE)
    positions = missed.positions(TRADE_DATE)
    close = session_close_for(TRADE_DATE)
    day_start = datetime.combine(TRADE_DATE, time(0), tzinfo=ET)
    rows, statuses = [], {}
    for card in candidates:
        bars = BarStore("cobalt_dev").bars_in_range(None, card.ticker, Interval.I1, day_start,
                                                    day_start + timedelta(days=1), end_inclusive=False, as_bars=True)
        replayed = replay_card(card, bars, trade_date=TRADE_DATE, window=resolve_window(card.window_ref, TRADE_DATE),
                               session_close=close, positions=positions)
        statuses[card.id] = (replayed.status, replayed.reason)
        if replayed.miss is not None:
            rows.append(replayed.miss)
    print(f"X11: candidates on {TRADE_DATE}: {[c.id for c in candidates]}; this card a candidate: "
          f"{card_id in [c.id for c in candidates]}")
    print(f"X11: replay_card status for this card: {statuses.get(card_id)}")
    counts = missed.reconcile(run_id="x11-f15-p2", trade_date=TRADE_DATE, kind="card", rows=rows)
    current = [r for r in missed.current(TRADE_DATE, "card") if r["card_id"] == card_id]
    print(f"X11: reconcile counts {counts}")
    print(f"X11: current missed rows for card {card_id}: {current}")
    print(f"X11: a missed row was written: {bool(current)}")
