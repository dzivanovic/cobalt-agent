"""X2 (v2 §7, before S2; `cobalt_dev`): the proposal's sequence — form a
card and tap all its dots; stop feeding bars and run the stage (NULL score,
NULL proximity); tap another dot (score stays NULL, the helper's sentence
kept — Q6); add a fresh bar and run the stage (the score returns with no
tap). Rows live inside the suite's rollback; nothing is committed."""

from __future__ import annotations

from datetime import timedelta

import stale_db_support as sds

pytestmark = sds.requires_db


def test_x2_stale_sequence_on_cobalt_dev():
    world = sds.DevWorld(ticker="ZZX2", pool="stale_x2")
    card_id = sds.scored_pre_c1_card(world)
    fresh = world.row(card_id)
    kept = sds.bars_before(sds.SCAN0)
    stale_at = sds.stale_as_of(kept)
    world.scan(stale_at)
    stale = world.row(card_id)
    world.tap(card_id, "trail_fit", 9, stale_at + timedelta(seconds=5))
    tapped = world.row(card_id)
    back_at = stale_at + timedelta(seconds=sds.SCAN)
    world.feed(back_at)
    world.scan(back_at)
    back = world.row(card_id)
    sentence = (stale["score_suppressed"] or "").startswith("bars stale — last close ")
    kept_reason = tapped["score_suppressed"] == stale["score_suppressed"]
    print(f"X2: s2_built={sds.s2_built()} fresh_score_present={fresh['card_score'] is not None} "
          f"stale_proximity_null={stale['proximity'] is None} stale_score_null={stale['card_score'] is None} "
          f"stale_reason_is_sentence={sentence} tap_score_null={tapped['card_score'] is None} "
          f"tap_reason_kept={kept_reason} tap_reason_after={tapped['score_suppressed']!r} "
          f"back_proximity_present={back['proximity'] is not None} back_score_present={back['card_score'] is not None}")
    assert fresh["card_score"] is not None
    assert stale["proximity"] is None and stale["card_score"] is None and sentence
    assert tapped["card_score"] is None
    assert back["proximity"] is not None and back["card_score"] is not None  # no tap in between
    if sds.s2_built():
        assert kept_reason
