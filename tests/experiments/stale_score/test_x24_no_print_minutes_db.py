"""X24 (v2 §7, before S2; Fable X11; `cobalt_dev`, READ-ONLY): are minutes
with no prints stored as i1 bars? Per archived (ticker, ET date), the RTH
minutes stored vs the 390 of a full session. COUNTS only (L32) — no ticker
and no price is printed. Zero archived rows on `cobalt_dev` makes this
UNPROVEN, never a finding."""

from __future__ import annotations

import stale_db_support as sds

pytestmark = sds.requires_db

FULL_SESSION = 390  # 09:30–16:00 ET, one i1 bar per minute


def test_x24_minutes_without_prints():
    from cobalt.radar.store import RadarStore

    with RadarStore("cobalt_dev")._connect() as conn:
        rows = conn.execute(
            "SELECT ticker, (ts AT TIME ZONE 'America/New_York')::date AS d, count(*) FROM system.bars "
            "WHERE interval = 'i1' AND ticker NOT LIKE 'ZZ%%' "
            "AND (ts AT TIME ZONE 'America/New_York')::time >= '09:30' "
            "AND (ts AT TIME ZONE 'America/New_York')::time < '16:00' "
            "GROUP BY 1, 2"
        ).fetchall()
        # The thinnest archived ticker-days (lowest RTH volume): minutes stored,
        # and how many of those minutes carry zero volume (a no-print minute
        # stored as a bar).
        thin = conn.execute(
            "SELECT count(*), sum(volume), count(*) FILTER (WHERE volume = 0) FROM system.bars "
            "WHERE interval = 'i1' AND ticker NOT LIKE 'ZZ%%' "
            "AND (ts AT TIME ZONE 'America/New_York')::time >= '09:30' "
            "AND (ts AT TIME ZONE 'America/New_York')::time < '16:00' "
            "GROUP BY ticker, (ts AT TIME ZONE 'America/New_York')::date ORDER BY sum(volume) ASC LIMIT 5"
        ).fetchall()
        zero = conn.execute(
            "SELECT count(*) FROM system.bars WHERE interval = 'i1' AND volume = 0 AND ticker NOT LIKE 'ZZ%%'"
        ).fetchone()[0]
        # Premarket (04:00–09:30 ET, 330 minutes): where a thin name goes minutes without a print (Q2 / R38).
        pre = [r[0] for r in conn.execute(
            "SELECT count(*) FROM system.bars WHERE interval = 'i1' AND ticker NOT LIKE 'ZZ%%' "
            "AND (ts AT TIME ZONE 'America/New_York')::time >= '04:00' "
            "AND (ts AT TIME ZONE 'America/New_York')::time < '09:30' "
            "GROUP BY ticker, (ts AT TIME ZONE 'America/New_York')::date"
        ).fetchall()]
    counts = [r[2] for r in rows]
    gapped = [c for c in counts if c < FULL_SESSION]
    share = (len(gapped) / len(counts)) if counts else None
    print(f"X24: ticker_days={len(counts)} with_missing_minutes={len(gapped)} share={share} "
          f"min_minutes={min(counts) if counts else None} max_minutes={max(counts) if counts else None} "
          f"full_session={FULL_SESSION} zero_volume_i1_bars={zero} "
          f"thinnest5_minutes={[t[0] for t in thin]} thinnest5_zero_volume_minutes={[t[2] for t in thin]} "
          f"premarket_ticker_days={len(pre)} premarket_with_missing_minutes={sum(1 for c in pre if c < 330)} "
          f"premarket_min_minutes={min(pre) if pre else None} premarket_full=330")
    assert all(c <= FULL_SESSION for c in counts)
