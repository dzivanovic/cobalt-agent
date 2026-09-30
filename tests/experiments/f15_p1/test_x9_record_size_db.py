"""X9 — card 61 RUN row, FINAL row X9 (O6: record volume), at BASE inside
the suite's rolled-back transaction on the real-shape `world` fixture.

No record table exists at BASE: after one scan creates the card and a
second refreshes it, the test builds the refresh record's `inputs`
(`[F-32]`: `{taps_moved, locked}`) and `output` (`published_numbers` of the
row's numbers with the dots as `_dots_for` reads them, plus
`proposed_key_reason`) and asks Postgres for
`pg_column_size(inputs::jsonb) + pg_column_size(output::jsonb)`. The scan
interval is the repo's tunable (`configs/cobalt/taxonomy/tunables.yaml`
`radar.scan_interval`, loaded, never assumed). Prints the byte figure and
the product. Asserts nothing (L70).
"""

from __future__ import annotations

import json
from datetime import timedelta

from test_radar_cards_db import ENABLED, SCAN0, world  # noqa: F401 — the with-DB fixture

import radar_p2_support as sup
from test_x12_transition_ids_db import requires_db

pytestmark = [requires_db]

#: One regular session, 09:30-16:00 ET, in seconds.
RTH_SECONDS = 6 * 3600 + 30 * 60


def test_x9_one_refresh_records_bytes_times_open_cards_times_scans(world):
    from cobalt.aset.models import Grade
    from cobalt.cards.scoring import proposed_key
    from cobalt.radar.evaluate import CardUpdate, published_numbers
    from cobalt.settings.card import CardSettings

    cards = world["cards"]
    card_id = world["scan"](SCAN0).created[0]
    assert world["scan"](SCAN0 + timedelta(seconds=100)).refreshed == [card_id]
    with cards._connect() as conn:
        row = conn.execute("SELECT proximity, conviction, card_score, score_suppressed, proposed_key FROM aset_sizings "
                           "WHERE id = %s", (card_id,)).fetchone()
        dots = cards._dots_for(conn, [card_id])[card_id]
        open_cards = conn.execute("SELECT count(*) FROM aset_sizings WHERE origin = 'radar' "
                                  "AND state IN ('WATCH', 'ARMED', 'TRIGGERED', 'FILLED')").fetchone()[0]
    update = CardUpdate(card_id=card_id, proximity=row[0], conviction=row[1], card_score=row[2],
                        score_suppressed=row[3], proposed_key=row[4], dots=dots, health=None, radar_score_id=None)
    _key, reason = proposed_key(row[1], CardSettings.from_rows(ENABLED).proposed_key, [Grade.A, Grade.B, Grade.C])
    inputs = {"taps_moved": False, "locked": None}
    output = {**published_numbers(update), "proposed_key_reason": reason}
    with cards._connect() as conn:
        size = conn.execute("SELECT pg_column_size(%s::jsonb) + pg_column_size(%s::jsonb)",
                            (json.dumps(inputs), json.dumps(output))).fetchone()[0]
    interval = int(sup.engine_tunables()["radar.scan_interval"].value)
    scans = RTH_SECONDS // interval
    print(f"X9: one refresh record inputs+output = {size} bytes ({len(dots)} dots)")
    print(f"X9: radar.scan_interval = {interval} s -> {scans} scans per RTH session")
    print(f"X9: {size} bytes x {open_cards} open card(s) in this world x {scans} scans = {size * open_cards * scans} "
          f"bytes per session; per open card {size * scans} bytes per session")
