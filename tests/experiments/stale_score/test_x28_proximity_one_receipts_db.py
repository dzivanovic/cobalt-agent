"""X28 (v2 §7, measurement only; Fable X15; `cobalt_dev`, READ-ONLY):
receipts whose published proximity is 1 on a card whose seam row for that
receipt's run is `input_stale` — how often the `card.entry` fallback
published in the past. Counts only; the production half is the desk's."""

from __future__ import annotations

import stale_db_support as sds

pytestmark = sds.requires_db

X28 = (
    'SELECT count(*) FROM "user".radar_score_receipt AS r '
    "CROSS JOIN LATERAL jsonb_array_elements(r.tap_versions -> 'cards') AS card "
    'JOIN system.radar_score AS s ON s.run_id = r.run_id '
    "AND s.membership_id = (card ->> 'pool_member_id')::bigint "
    "AND s.trade_def_md5 = coalesce(card ->> 'definition_md5', card ->> 'trade_def_md5') "
    "WHERE (card -> 'published' ->> 'proximity') ~ '^[0-9.]+$' "
    "AND (card -> 'published' ->> 'proximity')::numeric = 1 AND s.evaluation = 'input_stale'"
)


def test_x28_count_on_cobalt_dev():
    from cobalt.cards.store import CardStore

    with CardStore("cobalt_dev")._connect() as conn:
        receipts = conn.execute('SELECT count(*) FROM "user".radar_score_receipt').fetchone()[0]
        n = conn.execute(X28).fetchone()[0]
    print(f"X28: cobalt_dev receipts={receipts} proximity_one_on_stale_seam={n}")
    assert n >= 0
