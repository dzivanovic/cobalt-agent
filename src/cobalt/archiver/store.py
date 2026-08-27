"""Persistence for archived bars (cobalt_dev). Idempotent upserts.

DDL lives in exactly one place (migrations/0001_bars.sql) — this module
executes that file, it does not carry a second copy (one-path rule).
"""

from pathlib import Path

from cobalt import db

from .models import Bar

MIGRATION_SQL = Path(__file__).parent / "migrations" / "0001_bars.sql"


class BarStore:
    def __init__(self, db_name: str = "cobalt_dev"):
        self.db_name = db_name

    def _connect(self):
        return db.connect(self.db_name)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            conn.execute(MIGRATION_SQL.read_text())

    def upsert_bars(self, bars: list[Bar]) -> int:
        """Insert or refresh `bars`. Returns the number of rows written.

        ON CONFLICT DO UPDATE (not DO NOTHING): a re-run refreshes a bar
        that Finviz may have finalized/revised since the last pull,
        rather than freezing it at its first-seen (possibly provisional)
        values. PK (ticker, interval, ts) makes this a true idempotent
        upsert either way — no duplicates, ever.
        """
        if not bars:
            return 0
        rows = [
            (
                b.ticker,
                b.interval.value,
                b.ts,
                b.open,
                b.high,
                b.low,
                b.close,
                b.volume,
            )
            for b in bars
        ]
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.executemany(
                    """
                    INSERT INTO bars (ticker, interval, ts, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (ticker, interval, ts) DO UPDATE SET
                        open = EXCLUDED.open,
                        high = EXCLUDED.high,
                        low = EXCLUDED.low,
                        close = EXCLUDED.close,
                        volume = EXCLUDED.volume
                    """,
                    rows,
                )
        return len(rows)

    def count_rows(self) -> int:
        with self._connect() as conn:
            row = conn.execute("SELECT count(*) FROM bars").fetchone()
        return int(row[0]) if row else 0
