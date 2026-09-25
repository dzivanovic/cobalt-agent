"""X25 (v2 §7, measurement only; Fable X12; `cobalt_dev` half, READ-ONLY):
the `htf_level_proximity` taps graded on a stale price (the predicate in
`stale_predicates`). Zero on `cobalt_dev` says nothing about production —
that half is the desk's, before `44` (L41)."""

from __future__ import annotations

import stale_db_support as sds
from stale_predicates import X25_TAPS, X30_TAPS

pytestmark = sds.requires_db


def test_x25_count_on_cobalt_dev():
    from cobalt.cards.store import CardStore

    with CardStore("cobalt_dev")._connect() as conn:
        taps = conn.execute(
            "SELECT count(*) FROM \"user\".card_dot_taps WHERE factor = 'htf_level_proximity' "
            "AND engine_grade_at_tap IS NOT NULL"
        ).fetchone()[0]
        x25 = len(conn.execute(X25_TAPS).fetchall())
        bounded = len(conn.execute(X30_TAPS).fetchall())
    print(f"X25: cobalt_dev htf_taps_with_engine_grade={taps} stale_graded={x25} stale_graded_pre_fix={bounded}")
    assert bounded <= x25 <= taps
