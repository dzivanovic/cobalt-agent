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

from datetime import date
from pathlib import Path
from typing import Any

from cobalt import db
from .models import FillRecompute, SizingResult

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

    def mark_filled(self, row_id: int, fill: "FillRecompute") -> None:
        """Fill-recompute persists as an UPDATE to the card row it
        belongs to (2026-09-03, LAW L28 step 3).

        Before this, the recompute wrote a note block and NOTHING to
        Postgres — the 09-03 forensics found the 10:02:36 TSLA FILL
        UPDATE had no DB row at all, which is why the DB could not be
        used to rebuild a note and could not answer "how many cards
        became trades". Fail-loud: a row id that matches nothing raises
        rather than silently updating zero rows."""
        with self._connect() as conn:
            cur = conn.execute(
                """
                UPDATE aset_sizings SET
                    status = 'FILLED',
                    filled_at = now(),
                    actual_fill = %s,
                    recomputed_shares = %s,
                    recomputed_used_risk = %s,
                    share_delta = %s,
                    distance_change_pct = %s
                WHERE id = %s
                """,
                (
                    fill.actual_fill,
                    fill.recomputed_shares,
                    fill.recomputed_used_risk,
                    fill.share_delta,
                    fill.distance_change_pct,
                    row_id,
                ),
            )
            if cur.rowcount != 1:
                raise RuntimeError(
                    f"FILL UPDATE matched {cur.rowcount} rows for aset_sizings id "
                    f"{row_id} (expected exactly 1) — refusing to report a fill "
                    "that was not persisted."
                )

    def counts_for_date(self, day: date) -> tuple[int, int]:
        """(cards written, trades taken) for `day`. Trades taken counts
        status='FILLED' ONLY — a card is a written plan, not a trade
        (DRC ruling, 2026-08-31; L28 step 3 makes it countable)."""
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT count(*), count(*) FILTER (WHERE status = 'FILLED')
                FROM aset_sizings
                WHERE (created_at AT TIME ZONE 'America/New_York')::date = %s
                """,
                (day,),
            ).fetchone()
        return (int(row[0]), int(row[1])) if row else (0, 0)

    def for_date(self, day: date) -> list[dict[str, Any]]:
        """Every card whose created_at falls on `day` in America/New_York
        (Dejan's trading-day boundary, not the DB session's UTC default),
        oldest first — the DRC prefill's re-entry numbering depends on
        chronological order within a ticker."""
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, created_at, ticker, grade, direction, sheet_mode,
                       risk_budget, entry, stop, per_share_risk, shares, used_risk,
                       status, filled_at, actual_fill, recomputed_shares,
                       recomputed_used_risk, share_delta, distance_change_pct
                FROM aset_sizings
                WHERE (created_at AT TIME ZONE 'America/New_York')::date = %s
                ORDER BY created_at ASC
                """,
                (day,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    def recent(self, limit: int = 10) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, created_at, ticker, grade, direction, sheet_mode,
                       risk_budget, entry, stop, shares, used_risk, status
                FROM aset_sizings ORDER BY id DESC LIMIT %s
                """,
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]
