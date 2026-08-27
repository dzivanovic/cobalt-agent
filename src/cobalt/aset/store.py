"""Persistence for ASET sizings (cobalt_dev).

DDL lives under migrations/ (one path — the store executes those files,
it does not carry a second copy of the schema). ensure_schema() runs
every *.sql file in filename order, strips full-line '--' comments
(a semicolon inside a comment must not be mistaken for a statement
terminator), splits what's left on ';', and executes non-empty
statements individually — psycopg's execute() runs one statement at a
time, so a multi-ALTER migration (0002) can't be handed over as a
single execute() call the way 0001's single CREATE TABLE could. Only
full-line comments are stripped — a migration must not put a trailing
comment after SQL on the same line. The table may be reshaped again by
the data-model ADR; see the note in 0001.
"""

from pathlib import Path
from typing import Any

from cobalt import db
from .models import SizingResult

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class AsetStore:
    def __init__(self, db_name: str = "cobalt_dev"):
        self.db_name = db_name

    def _connect(self):
        return db.connect(self.db_name)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
                lines = migration.read_text().splitlines()
                sql = "\n".join(line for line in lines if not line.strip().startswith("--"))
                for statement in sql.split(";"):
                    statement = statement.strip()
                    if statement:
                        conn.execute(statement)

    def save(self, result: SizingResult) -> int:
        inp = result.input
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO aset_sizings (
                    ticker, grade, direction, sheet_mode,
                    risk_budget, entry, stop, per_share_risk, shares,
                    used_risk, last_price, price_source, warnings
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    inp.ticker,
                    inp.grade.value,
                    inp.direction.value,
                    inp.sheet_mode.value,
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
                SELECT id, created_at, ticker, grade, direction, sheet_mode,
                       risk_budget, entry, stop, shares, used_risk
                FROM aset_sizings ORDER BY id DESC LIMIT %s
                """,
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]
