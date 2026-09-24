"""X21 (v2 §7, before S2; `cobalt_dev`): one tap on `htf_level_proximity`
while `intraday_stale` inserts `engine_grade_at_tap` NULL and adds no row to
`shadow_agreement_v`; a tap from before the change (a fresh-graded tap,
engine grade present) is still in the view."""

from __future__ import annotations

from datetime import date, timedelta

import stale_db_support as sds

pytestmark = sds.requires_db


def _pairs(world) -> int:
    rows = [r for r in world.cards.shadow_agreement(None)
            if r["factor"] == sds.HTF and r["trade_date"] == date(2026, 1, 6)]
    return sum(r["pairs"] for r in rows)


def test_x21_stale_htf_tap_is_not_a_pair():
    world = sds.DevWorld(ticker="ZZX21", pool="stale_x21")
    card_id = sds.scored_pre_c1_card(world)  # every dot tapped while fresh: the htf tap is a pair
    fresh_pairs = _pairs(world)
    with world.cards._connect() as conn:
        fresh_tap = conn.execute(
            "SELECT engine_grade_at_tap FROM card_dot_taps WHERE card_id = %s AND factor = %s ORDER BY id LIMIT 1",
            (card_id, sds.HTF),
        ).fetchone()[0]
    stale_at = sds.stale_as_of(sds.bars_before(sds.SCAN0))
    world.scan(stale_at)
    engine_after_stale_scan = world.engine_grade(card_id, sds.HTF)
    world.tap(card_id, sds.HTF, 6, stale_at + timedelta(seconds=5))
    with world.cards._connect() as conn:
        stale_tap = conn.execute(
            "SELECT engine_grade_at_tap FROM card_dot_taps WHERE card_id = %s AND factor = %s ORDER BY id DESC LIMIT 1",
            (card_id, sds.HTF),
        ).fetchone()[0]
    stale_pairs = _pairs(world)
    print(f"X21: pre_change_tap_engine_grade_present={fresh_tap is not None} pairs_before={fresh_pairs} "
          f"dot_engine_grade_after_stale_scan={engine_after_stale_scan} stale_tap_engine_grade_at_tap={stale_tap} "
          f"pairs_after={stale_pairs} pre_change_tap_still_in_view={stale_pairs >= 1}")
    assert fresh_tap is not None and fresh_pairs >= 1
    assert engine_after_stale_scan is None and stale_tap is None
    assert stale_pairs == fresh_pairs
