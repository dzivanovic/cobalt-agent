"""X3 (v2 §7, before S2; `cobalt_dev`): taps-moved while the update's
proximity is NULL → the row's `card_score` is NULL. At STEP-2's commit the
taps-moved branch writes proximity only, so the tap route's score (computed
on the OLD, fresh proximity) is left beside a NULL proximity — W9."""

from __future__ import annotations

from datetime import timedelta

import stale_db_support as sds

pytestmark = sds.requires_db


def test_x3_taps_moved_with_a_null_update_proximity():
    world = sds.DevWorld(ticker="ZZX3", pool="stale_x3")
    card_id = sds.scored_pre_c1_card(world)
    kept = sds.bars_before(sds.SCAN0)
    stale_at = sds.stale_as_of(kept)
    update = sds.update_for(world, card_id, stale_at, kept)
    world.tap(card_id, "trail_fit", 9, stale_at + timedelta(seconds=1))
    wrote_all = world.cards.refresh_radar_card(update, now=stale_at + timedelta(seconds=2))
    row = world.row(card_id)
    print(f"X3: s2_built={sds.s2_built()} taps_moved={not wrote_all} update_proximity_null={update.proximity is None} "
          f"row_proximity_null={row['proximity'] is None} row_score_null={row['card_score'] is None} "
          f"row_reason_is_update_reason={row['score_suppressed'] == update.score_suppressed}")
    assert not wrote_all and update.proximity is None and row["proximity"] is None
    if sds.s2_built():
        assert row["card_score"] is None and row["score_suppressed"] == update.score_suppressed
    else:  # W9 on this branch before S2: a live score beside a NULL proximity
        assert row["card_score"] is not None
