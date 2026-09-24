"""X16 (v2 §7, before S2; `cobalt_dev`): no bar this scan, previous
`last_price` 5.25 (this test's own construction) → the column still holds
5.25 (`COALESCE`, Q4) and proximity is NULL. "No bar this scan" is the next
trade date's first scan, before any bar of that day is stored."""

from __future__ import annotations

from datetime import timedelta
from decimal import Decimal

import stale_db_support as sds

pytestmark = sds.requires_db

PREVIOUS = Decimal("5.25")


def test_x16_coalesce_keeps_the_previous_last_price():
    world = sds.DevWorld(ticker="ZZX16", pool="stale_x16")
    card_id = sds.scored_pre_c1_card(world)
    with world.cards._connect() as conn:
        conn.execute("UPDATE aset_sizings SET last_price = %s WHERE id = %s", (PREVIOUS, card_id))
    next_day = sds.SCAN0 + timedelta(days=1)
    outcome = world.scan(next_day)
    row = world.row(card_id)
    print(f"X16: refreshed={card_id in outcome.refreshed} last_price_kept={row['last_price'] == PREVIOUS} "
          f"proximity_null={row['proximity'] is None} score_null={row['card_score'] is None} "
          f"reason={row['score_suppressed']!r}")
    assert card_id in outcome.refreshed
    assert row["last_price"] == PREVIOUS and row["proximity"] is None and row["card_score"] is None
