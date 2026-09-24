"""X23 (v2 §7, before S2; Fable X10; `cobalt_dev`): a def whose
`preferred_windows_ref` ends after the day's last scan, a card formed on it,
a scan on the NEXT trade date before any bar. Does the card survive to that
scan (is it refreshed), what does it publish, and what state does the scan
leave it in? On `main` the `card.entry` fallback published proximity 1 here
(X5a, `46`); this run is on STEP-2's commit, where S1 has removed it."""

from __future__ import annotations

from datetime import timedelta

import stale_db_support as sds

pytestmark = sds.requires_db


def test_x23_a_card_carried_to_the_next_trade_date():
    world = sds.DevWorld(ticker="ZZX23", pool="stale_x23")
    card_id = sds.scored_pre_c1_card(world)  # SCAN0 is 11:30 ET; the def's window ends 15:30 ET; no later scan
    next_day = sds.SCAN0 + timedelta(days=1) - timedelta(hours=2)  # 09:30 ET the next day, no bar stored
    outcome = world.scan(next_day)
    row = world.row(card_id)
    with world.cards._connect() as conn:
        state = conn.execute("SELECT state FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()[0]
    print(f"X23: survives_to_next_day_scan={card_id in outcome.refreshed} expired_by_that_scan={card_id in outcome.expired} "
          f"state_after={state} published_proximity={row['proximity']} published_score={row['card_score']} "
          f"reason={row['score_suppressed']!r}")
    assert card_id in outcome.refreshed
    assert row["proximity"] is None and row["card_score"] is None
