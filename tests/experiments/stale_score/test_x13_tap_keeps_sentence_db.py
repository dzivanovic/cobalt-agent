"""X13 (v2 §7, before S2; `cobalt_dev`): a tap while proximity is NULL
leaves `score_suppressed` byte-identical and `card_score` NULL. At STEP-2's
commit `tap_dot` writes `suppression(dots)` alone, which erases the
helper's sentence ([F-06], the hub's Checked row)."""

from __future__ import annotations

from datetime import timedelta

import stale_db_support as sds

pytestmark = sds.requires_db


def test_x13_tap_while_proximity_is_null():
    world = sds.DevWorld(ticker="ZZX13", pool="stale_x13")
    card_id = sds.scored_pre_c1_card(world)
    stale_at = sds.stale_as_of(sds.bars_before(sds.SCAN0))
    world.scan(stale_at)
    before = world.row(card_id)
    world.tap(card_id, "setup_relation", 4, stale_at + timedelta(seconds=5))
    after = world.row(card_id)
    same = (before["score_suppressed"] or "").encode() == (after["score_suppressed"] or "").encode()
    print(f"X13: s2_built={sds.s2_built()} proximity_null={before['proximity'] is None} "
          f"score_null_after_tap={after['card_score'] is None} reason_byte_identical={same} "
          f"reason_after={after['score_suppressed']!r}")
    assert before["proximity"] is None and after["card_score"] is None
    if sds.s2_built():
        assert same
