"""X9 (v2 §7, measurement only; `cobalt_dev` half, READ-ONLY): radar cards
whose `radar_score_id` seam row is `input_stale` while `card_score IS NOT
NULL`. Zero on `cobalt_dev` says nothing about production (the production
half is the desk's, before `44`, L41)."""

from __future__ import annotations

import stale_db_support as sds

pytestmark = sds.requires_db

X9 = (
    'SELECT count(*) FROM "user".aset_sizings AS c JOIN system.radar_score AS s ON s.id = c.radar_score_id '
    "WHERE c.origin = 'radar' AND s.evaluation = 'input_stale' AND c.card_score IS NOT NULL"
)


def test_x9_count_on_cobalt_dev():
    from cobalt.cards.store import CardStore

    with CardStore("cobalt_dev")._connect() as conn:
        n = conn.execute(X9).fetchone()[0]
        cards = conn.execute("SELECT count(*) FROM \"user\".aset_sizings WHERE origin = 'radar'").fetchone()[0]
    print(f"X9: cobalt_dev radar_cards={cards} stale_seam_with_live_score={n}")
    assert n >= 0
