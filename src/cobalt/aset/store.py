"""Persistence for ASET sizings (cobalt_dev).

DDL lives in migrations/0001_aset_sizings.sql (one path — the store
executes that file, it does not carry a second copy). The table may be
reshaped by the data-model ADR; see the note in the migration file.
"""

from pathlib import Path
from typing import Any

from cobalt import db
from .models import SizingResult

MIGRATION_SQL = Path(__file__).parent / "migrations" / "0001_aset_sizings.sql"


class AsetStore:
    def __init__(self, db_name: str = "cobalt_dev"):
        self.db_name = db_name

    def _connect(self):
        return db.connect(self.db_name)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            conn.execute(MIGRATION_SQL.read_text())

    def save(self, result: SizingResult) -> int:
        inp = result.input
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO aset_sizings (
                    ticker, grade, direction, daily_stop, risk_pct,
                    risk_budget, entry, stop, per_share_risk, shares,
                    used_risk, last_price, price_source, warnings
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    inp.ticker,
                    inp.grade.value,
                    inp.direction.value,
                    inp.daily_stop,
                    result.risk_pct,
                    result.risk_budget,
                    inp.entry,
                    inp.stop,
                    result.per_share_risk,
                    result.shares,
                    result.used_risk,
                    inp.last_price,
                    inp.price_source,
                    result.warnings,
                ),
            ).fetchone()
        if row is None:
            raise RuntimeError("INSERT returned no id — persistence failed loudly.")
        return int(row[0])

    def recent(self, limit: int = 10) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, created_at, ticker, grade, direction, daily_stop,
                       risk_budget, entry, stop, shares, used_risk
                FROM aset_sizings ORDER BY id DESC LIMIT %s
                """,
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]
