"""`DrcStore` — the ONE writer of every `drc_*` row (L40).

The tables are created by the database-wide migration
`db_migrations/0016_drc.sql` (run with `cobalt db migrate`); this store
never creates or alters a table. `ensure_schema()` only proves they are
there and names the command when they are not.

The database is not named here: `COBALT_ENV` chooses it through
`env.resolve_db_name()` (RULING 7), and the connection comes from the
one factory, pinned to the USER side (ADR-0008 D1, L32).

WHAT IS WRITTEN
- `record_import` — one `drc_imports` row per file (sha256 of the exact
  bytes; `parsed` / `partial` / `failed` with its reason and line;
  `supersedes` the day's previous file of that kind) and, unless the file
  failed, one `drc_fills` row per execution. One transaction: a failed
  file stores its reason and ZERO fills (L1).
- `record_day` — the day's derived rows in `drc_rows`: one per trade, per
  open position (the next day's seed, R67), per stats row (matched or
  `unmatched`, shown) and one for the day. Each carries its inputs and
  `pairing.FN_VERSION` (L57). Recording a day again replaces that day's
  rows in one transaction; the inputs they derive from stay in
  `drc_imports` / `drc_fills`.
- `seed_for` — the prior trading day's open positions, after the
  contiguity check (`pairing.check_contiguity`).
"""

from __future__ import annotations

import hashlib
from datetime import date
from typing import Iterable, Optional

from psycopg.types.json import Jsonb

from cobalt import db, env
from cobalt.db import Side

from .models import DayPairing, Execution, ImportResult, Kind, OpenPosition, Outcome
from .pairing import FN_VERSION, check_contiguity

TABLES = ("drc_imports", "drc_fills", "drc_rows")

_TENANT = "current_setting('cobalt.trader_id')::int"


class DrcStore:
    #: ADR-0008 D2 — his imported files, his executions, his DRC (L32).
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        """`db_name` is a TEST/TOOLING seam only (RULING 7)."""
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            db.assert_schemas_exist(conn)
            absent = [
                t for t in TABLES if conn.execute("SELECT to_regclass(%s)", (t,)).fetchone()[0] is None
            ]
        if absent:
            raise db.SchemaMissingError(
                f"table(s) {', '.join(absent)} do not exist — migration 0016_drc has not "
                "run here. Run `cobalt db migrate`."
            )

    def record_import(
        self,
        import_date: date,
        result: ImportResult,
        data: bytes,
        executions: Iterable[Execution] = (),
    ) -> int:
        """Store one file's verdict (and its executions unless it failed)."""
        if result.kind is None or result.outcome is Outcome.IGNORED:
            raise ValueError(
                f"{result.name}: an {result.outcome.value} file of no kind is listed, never stored"
            )
        rows = list(executions)
        if result.outcome is Outcome.FAILED and rows:
            raise ValueError(f"{result.name}: a failed file stores zero executions (L1)")
        conn = self._connect()
        conn.autocommit = False
        try:
            prior = conn.execute(
                f"""
                SELECT id FROM drc_imports
                 WHERE user_id = {_TENANT} AND import_date = %s AND kind = %s
                   AND id NOT IN (SELECT supersedes FROM drc_imports
                                   WHERE supersedes IS NOT NULL AND user_id = {_TENANT})
                 ORDER BY id DESC LIMIT 1
                """,
                (import_date, result.kind.value),
            ).fetchone()
            import_id = conn.execute(
                """
                INSERT INTO drc_imports (import_date, kind, name, sha256, parse_status,
                                         reason, failed_line, degraded, supersedes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    import_date,
                    result.kind.value,
                    result.name,
                    hashlib.sha256(data).hexdigest(),
                    result.outcome.value,
                    result.reason,
                    result.line,
                    result.degraded,
                    prior[0] if prior else None,
                ),
            ).fetchone()[0]
            if rows:
                with conn.cursor() as cur:
                    cur.executemany(
                        """
                        INSERT INTO drc_fills (import_id, line, executed_at, symbol, side, price,
                                               qty, route, broker, account, order_type, order_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        [
                            (
                                import_id,
                                e.line,
                                e.time,
                                e.symbol,
                                e.side.value if e.side else None,
                                e.price,
                                e.qty,
                                e.route,
                                e.broker,
                                e.account,
                                e.order_type,
                                e.order_id,
                            )
                            for e in rows
                        ],
                    )
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return int(import_id)

    def record_day(self, pairing: DayPairing, import_ids: dict[Kind, int]) -> int:
        """Replace the day's derived rows with `pairing`'s. Returns the
        number of rows written."""
        trading_id = import_ids.get(Kind.TRADING_LOG)
        stats_id = import_ids.get(Kind.STATS_LOG)
        out: list[tuple[str, str, dict, dict]] = []
        for t in pairing.trades:
            lines = sorted(leg.line for leg in [*t.entries, *t.legs] if leg.line is not None)
            out.append((
                "trade",
                t.trade_id,
                {
                    "trading_log_import_id": trading_id,
                    "fill_lines": lines,
                    "carried_lots": [leg.model_dump(mode="json") for leg in t.entries if leg.carried],
                    "stats_log_import_id": stats_id if t.stats else None,
                    "stats_line": t.stats.line if t.stats else None,
                },
                t.model_dump(mode="json"),
            ))
            if t.stats is not None:
                out.append((
                    "stats_row",
                    f"line {t.stats.line}",
                    {"stats_log_import_id": stats_id, "line": t.stats.line},
                    {"match": "matched", "trade_id": t.trade_id, "row": t.stats.model_dump(mode="json")},
                ))
        for p in pairing.open_positions:
            out.append((
                "open_position",
                p.trade_id,
                {"trading_log_import_id": trading_id},
                p.model_dump(mode="json"),
            ))
        for u in pairing.unmatched:
            out.append((
                "stats_row",
                f"line {u.row.line}",
                {"stats_log_import_id": stats_id, "line": u.row.line},
                {"match": u.reason, "trade_id": None, "row": u.row.model_dump(mode="json")},
            ))
        out.append((
            "day",
            "day",
            {"import_ids": {k.value: v for k, v in import_ids.items()}},
            {
                "trades": len(pairing.trades),
                "open_positions": len(pairing.open_positions),
                "unmatched": len(pairing.unmatched),
                "not_computed": dict(pairing.not_computed),
            },
        ))
        conn = self._connect()
        conn.autocommit = False
        try:
            conn.execute(
                f"DELETE FROM drc_rows WHERE user_id = {_TENANT} AND day = %s", (pairing.day,)
            )
            with conn.cursor() as cur:
                cur.executemany(
                    """
                    INSERT INTO drc_rows (day, kind, ref, inputs, derived, fn_version)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    [(pairing.day, kind, ref, Jsonb(i), Jsonb(d), FN_VERSION) for kind, ref, i, d in out],
                )
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return len(out)

    def seed_for(self, day: date) -> list[OpenPosition]:
        """The positions the prior trading day left open — after proving
        the chain of recorded days is unbroken (fails loud, never flat)."""
        from cobalt.daymode.propose import prior_trading_day

        prior = prior_trading_day(day)
        with self._connect() as conn:
            recorded = [
                r[0]
                for r in conn.execute(
                    f"SELECT DISTINCT day FROM drc_rows WHERE user_id = {_TENANT} "
                    "AND kind = 'day' AND day < %s",
                    (day,),
                ).fetchall()
            ]
            check_contiguity(day, prior, recorded)
            rows = conn.execute(
                f"SELECT derived FROM drc_rows WHERE user_id = {_TENANT} "
                "AND kind = 'open_position' AND day = %s ORDER BY ref",
                (prior,),
            ).fetchall()
        return [OpenPosition.model_validate(r[0]) for r in rows]


__all__ = ["TABLES", "DrcStore"]
