"""X2, in its neutral form (FINAL, re-scoped by R24): how many stored
sessions and names `cobalt_dev` holds for i1. Coverage only — it chooses no
fixture and no gate day. Zero → every stored-session experiment is UNPROVEN
and moves to the deploy. Prints counts only (L32)."""

from __future__ import annotations

import os

import pytest

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: needs cobalt_dev",
)


@requires_db
def test_x2_stored_i1_sessions_and_names():
    from cobalt import db

    with db.connect("cobalt_dev", side=db.Side.SYSTEM) as conn:
        sessions, names, rows = conn.execute(
            "SELECT count(DISTINCT (ts AT TIME ZONE 'America/New_York')::date), count(DISTINCT ticker), count(*) "
            "FROM system.bars WHERE interval = 'i1'"
        ).fetchone()
        per_session = conn.execute(
            "SELECT count(DISTINCT ticker) FROM system.bars WHERE interval = 'i1' "
            "GROUP BY (ts AT TIME ZONE 'America/New_York')::date ORDER BY 1"
        ).fetchall()
    counts = [r[0] for r in per_session]
    print(f"X2: stored i1 sessions={sessions} names={names} rows={rows} "
          f"names-per-session min={min(counts, default=0)} max={max(counts, default=0)}")
    assert sessions >= 0
