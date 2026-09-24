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
  `unmatched`, shown), one for the day, and (K1) the day's `seed` (the
  book it started from, with its source and hash) and `book_close` (the
  book it left, `count = 0` included). Each carries its inputs and
  `pairing.FN_VERSION` (L57). Recording a day again replaces that day's
  rows in one transaction; the inputs they derive from stay in
  `drc_imports` / `drc_fills` / `drc_stated_books`.
- `record_stated_book` (K1) — his statement (an `opening` book, a
  `resolve`, a `no_trade` DRC) as one append-only `drc_stated_books` row:
  THE one writer behind every caller — the `/drc` page, the voice
  widget, the `cobalt drc state-book` CLI (L3, R52). Refused inside
  `market_reset` for every caller (v3 `[F-01]`).
- `seed_for` — the book day D starts from (`SeedBook`), or `None` when
  none is stated: the prior trading day's hash-checked close (carried),
  or his current `opening` statement for D (stated). Every other case
  FAILS loud, never flat (L1; v3 §2b, §4).
"""

from __future__ import annotations

import hashlib
from datetime import date, datetime
from typing import Any, Iterable, Optional

from psycopg.types.json import Jsonb
from pydantic import TypeAdapter, ValidationError

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import assert_writable
from cobalt.session import clock as clock_mod

from .models import (
    DayPairing,
    Execution,
    ImportResult,
    Kind,
    OpenPosition,
    Outcome,
    PairingError,
    SeedBook,
    StatedBook,
    StatedPosition,
    StatedResolve,
)
from .pairing import FN_VERSION, book_sha256, canonical_sha256, check_contiguity, stated_open_positions

TABLES = ("drc_imports", "drc_fills", "drc_rows", "drc_stated_books")

_TENANT = "current_setting('cobalt.trader_id')::int"

_STATED_KINDS = ("opening", "resolve", "no_trade")
_VIAS = ("drc_page", "voice_widget", "cli")
_OPENING = TypeAdapter(list[StatedPosition])
_RESOLVE = TypeAdapter(list[StatedResolve])

#: A current row is one no other row supersedes (the `drc_imports`
#: predicate of `record_import`, v3 `[F-01]`).
_CURRENT = (
    f"user_id = {_TENANT} AND id NOT IN (SELECT supersedes FROM drc_stated_books "
    f"WHERE supersedes IS NOT NULL AND user_id = {_TENANT})"
)
_STATED_COLUMNS = (
    "id, day, kind, positions, book_sha256, via, turn_id, readback_sha256, reason, supersedes, created_at"
)


def _stated(row) -> StatedBook:
    return StatedBook(**dict(zip([c.strip() for c in _STATED_COLUMNS.split(",")], row)))


class DrcStore:
    #: ADR-0008 D2 — his imported files, his executions, his DRC (L32).
    SIDE = Side.USER
    #: The statement table's name, for a caller's printout (the CLI names
    #: the row it wrote without naming the table itself, L40).
    STATED_TABLE = "drc_stated_books"

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
                f"table(s) {', '.join(absent)} do not exist — migration 0016_drc / "
                "0018_drc_stated_books has not run here. Run `cobalt db migrate`."
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
                    f"{result.degraded}: {', '.join(result.extras)}"
                    if result.degraded and result.extras
                    else result.degraded,
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

    def record_day(
        self,
        pairing: DayPairing,
        import_ids: dict[Kind, int],
        seed: Optional[SeedBook],
    ) -> int:
        """Replace the day's derived rows with `pairing`'s. Returns the
        number of rows written.

        `seed` is the book the pairing ran from (`seed_for`), REQUIRED of
        every caller: a COMPUTED pairing with `seed=None` is refused — no
        assumed book (L1). A not-computed day (no book stated, or a
        partial file) writes no `book_close`: it left no known book."""
        computed = "pairing" not in pairing.not_computed
        if computed and seed is None:
            raise ValueError(
                f"{pairing.day}: a computed pairing with no book — record_day needs the "
                "SeedBook it ran from (seed_for); nothing written (L1)"
            )
        trading_id = import_ids.get(Kind.TRADING_LOG)
        stats_id = import_ids.get(Kind.STATS_LOG)
        out: list[tuple[str, str, dict, dict]] = []
        trade_inputs: dict[str, dict] = {}
        for t in pairing.trades:
            lines = sorted(leg.line for leg in [*t.entries, *t.legs] if leg.line is not None)
            trade_inputs[t.trade_id] = {
                "trading_log_import_id": trading_id,
                "fill_lines": lines,
                "carried_lots": [leg.model_dump(mode="json") for leg in t.entries if leg.carried],
                "stats_log_import_id": stats_id if t.stats else None,
                "stats_line": t.stats.line if t.stats else None,
            }
            if seed is not None and any(leg.carried for leg in t.entries):
                # The replay key (L57, v3 `:165`): by (day, kind, ref) +
                # hash, never by a row id that re-recording changes.
                trade_inputs[t.trade_id]["carried_from"] = (
                    {"day": seed.from_day.isoformat(), "trade_id": t.trade_id,
                     "from_book_sha256": seed.from_book_sha256}
                    if seed.source == "carried"
                    else {"stated_book_id": seed.stated_book_id}
                )
            out.append(("trade", t.trade_id, trade_inputs[t.trade_id], t.model_dump(mode="json")))
            if t.stats is not None:
                out.append((
                    "stats_row",
                    f"line {t.stats.line}",
                    {"stats_log_import_id": stats_id, "line": t.stats.line},
                    {"match": "matched", "trade_id": t.trade_id, "row": t.stats.model_dump(mode="json")},
                ))
        for p in pairing.open_positions:
            # L57: the position is its trade's remainder — the same inputs.
            out.append(("open_position", p.trade_id, trade_inputs[p.trade_id], p.model_dump(mode="json")))
        for u in pairing.unmatched:
            out.append((
                "stats_row",
                f"line {u.row.line}",
                {"stats_log_import_id": stats_id, "line": u.row.line},
                {"match": u.reason, "trade_id": None, "row": u.row.model_dump(mode="json")},
            ))
        day_inputs: dict[str, Any] = {"import_ids": {k.value: v for k, v in import_ids.items()}}
        if seed is not None and seed.source == "stated":
            day_inputs["stated_book_id"] = seed.stated_book_id
        out.append((
            "day",
            "day",
            day_inputs,
            {
                "trades": len(pairing.trades),
                "open_positions": len(pairing.open_positions),
                "unmatched": len(pairing.unmatched),
                "not_computed": dict(pairing.not_computed),
            },
        ))
        if seed is not None:
            # What the day started from (v3 §2b step 3).
            out.append((
                "seed",
                "book",
                {
                    "source": seed.source,
                    "from_day": seed.from_day.isoformat() if seed.from_day else None,
                    "from_book_sha256": seed.from_book_sha256,
                    "stated_book_id": seed.stated_book_id,
                },
                {"count": len(seed.positions), "trade_ids": sorted(p.trade_id for p in seed.positions)},
            ))
        if computed:
            # What the day left (v3 §2a): stored on every computed day,
            # `count = 0` included — "flat" is a fact, never an absence.
            out.append((
                "book_close",
                "book",
                {
                    "trading_log_import_id": trading_id,
                    "seed_ref": {"day": pairing.day.isoformat(), "kind": "seed", "ref": "book"},
                },
                {
                    "count": len(pairing.open_positions),
                    "trade_ids": sorted(p.trade_id for p in pairing.open_positions),
                    "book_sha256": book_sha256(pairing.open_positions),
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

    def seed_for(self, day: date) -> Optional[SeedBook]:
        """The book `day` starts from, or `None` when no book is stated.

        P = the prior trading day. P recorded → P's `book_close`, checked
        against a hash recomputed over P's `open_position` rows (carried).
        P not recorded → his current `opening` statement for `day`
        (stated: the first import, or a chain he mended). Nothing recorded
        before `day` and nothing stated → `None`. Every other case FAILS
        loud, naming why — never an assumed flat book (L1, v3 §2b, §4)."""
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
            openings = [
                _stated(r)
                for r in conn.execute(
                    f"SELECT {_STATED_COLUMNS} FROM drc_stated_books WHERE {_CURRENT} "
                    "AND day = %s AND kind = 'opening' ORDER BY id",
                    (day,),
                ).fetchall()
            ]
            if len(openings) > 1:
                raise PairingError(
                    f"{day}: {len(openings)} current opening books are stated — "
                    f"{' and '.join(f'#{b.id}' for b in openings)}; one restatement must "
                    "supersede the other (v3 [F-01]); nothing assumed"
                )
            stated = openings[0] if openings else None

            if prior in recorded:
                book = self._carried(conn, day, prior)
                if stated is not None:
                    raise PairingError(
                        f"{day}: stated opening book #{stated.id} and {prior}'s recorded close "
                        "both exist — R51's rebuild (the close wins, the statement kept as "
                        "history) is K2's; nothing assumed"
                    )
            elif stated is not None:
                book = SeedBook(
                    source="stated",
                    positions=stated_open_positions(day, _OPENING.validate_python(stated.positions)),
                    stated_book_id=stated.id,
                    from_book_sha256=stated.book_sha256,
                )
            else:
                check_contiguity(day, prior, recorded)  # names P when an earlier day exists
                return None

            held = {p.trade_id for p in book.positions}
            for resolve_id, resolved in conn.execute(
                f"SELECT id, positions->0->>'trade_id' FROM drc_stated_books WHERE {_CURRENT} "
                "AND kind = 'resolve' AND day <= %s ORDER BY id",
                (day,),
            ).fetchall():
                if resolved in held:
                    raise PairingError(
                        f"{day}: resolve #{resolve_id} for {resolved} is stored and not applied — "
                        "RESOLVE is K2's; nothing assumed"
                    )
        return book

    @staticmethod
    def _carried(conn, day: date, prior: date) -> SeedBook:
        """P's close as `day`'s seed, hash-checked against its own rows."""
        if conn.execute(
            f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} "
            "AND kind = 'day' AND day = %s AND derived->'not_computed' ? 'pairing'",
            (prior,),
        ).fetchone():
            raise PairingError(
                f"{day}: the prior trading day {prior} has pairing not computed — its open "
                "positions are unknown; never assumed flat"
            )
        close = conn.execute(
            f"SELECT derived FROM drc_rows WHERE user_id = {_TENANT} "
            "AND kind = 'book_close' AND day = %s AND ref = 'book'",
            (prior,),
        ).fetchone()
        if close is None:
            raise PairingError(
                f"{day}: {prior} was recorded before the overnight-position lane (no book_close) "
                f"— rebuild {prior}"
            )
        rows = [
            r[0]
            for r in conn.execute(
                f"SELECT derived FROM drc_rows WHERE user_id = {_TENANT} "
                "AND kind = 'open_position' AND day = %s",
                (prior,),
            ).fetchall()
        ]
        stored = close[0]["book_sha256"]
        if canonical_sha256(sorted(rows, key=lambda r: r["trade_id"])) != stored:
            raise PairingError(f"seed for {day}: {prior}'s stored book does not match its own close row")
        positions = sorted((OpenPosition.model_validate(r) for r in rows), key=lambda p: p.trade_id)
        return SeedBook(source="carried", positions=positions, from_day=prior, from_book_sha256=stored)

    # -----------------------------------------------------------------
    # K1 — his statements (v3 §3 `drc_stated_books`; R52)
    # -----------------------------------------------------------------

    @staticmethod
    def _validated(
        kind: str,
        positions: Iterable[Any],
        via: str,
        turn_id: Optional[str],
        readback_sha256: Optional[str],
    ) -> tuple[list[dict], str]:
        """(2)–(4) of the one writer: the positions validated by kind, the
        caller's fields, and the canonical rows + their hash."""
        if kind not in _STATED_KINDS:
            raise ValueError(f"kind {kind!r} is not one of {', '.join(_STATED_KINDS)}")
        items = list(positions)
        try:
            if kind == "opening":
                book = _OPENING.validate_python(items)
                symbols = [p.symbol for p in book]
                repeated = sorted({s for s in symbols if symbols.count(s) > 1})
                if repeated:
                    raise ValueError(f"an opening book names {', '.join(repeated)} more than once")
                rows = [p.model_dump(mode="json") for p in sorted(book, key=lambda p: p.symbol)]
            elif kind == "resolve":
                book = _RESOLVE.validate_python(items)
                if len(book) != 1:
                    raise ValueError(f"a resolve names exactly one trade_id, not {len(book)}")
                rows = [book[0].model_dump(mode="json")]
            else:
                if items:
                    raise ValueError("a no_trade statement carries no positions")
                rows = []
        except ValidationError as e:
            raise ValueError(f"{kind} positions refused: {e}") from e
        if via not in _VIAS:
            raise ValueError(f"via {via!r} is not one of {', '.join(_VIAS)}")
        if via == "voice_widget":
            if turn_id is None or readback_sha256 is None:
                raise ValueError("a voice_widget statement carries both its turn_id and its readback_sha256")
        else:
            if turn_id is not None:
                raise ValueError(f"turn_id belongs to the voice_widget caller only, not {via}")
            if readback_sha256 is not None:
                raise ValueError(f"readback_sha256 belongs to the voice_widget caller only, not {via}")
        return rows, canonical_sha256(rows)

    @staticmethod
    def _reason(conn, day: date, kind: str) -> str:
        """Derived by the store, never passed in (v3 `:139`)."""
        if kind == "resolve":
            return "closed outside export"
        if kind == "no_trade":
            return "no-trade DRC"
        from cobalt.daymode.propose import prior_trading_day

        earlier = conn.execute(
            f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' AND day < %s LIMIT 1",
            (day,),
        ).fetchone()
        return f"chain broken at {prior_trading_day(day)}" if earlier else "first import"

    def preview_stated_book(
        self,
        day: date,
        kind: str,
        positions: Iterable[Any],
        *,
        via: str,
        turn_id: Optional[str] = None,
        readback_sha256: Optional[str] = None,
        supersedes: Optional[int] = None,
    ) -> StatedBook:
        """The exact row `record_stated_book` would insert, without its id.
        No gate and no write: a dry run is not gated (`writer.py`'s
        `_session_gate` docstring)."""
        rows, sha = self._validated(kind, positions, via, turn_id, readback_sha256)
        with self._connect() as conn:
            reason = self._reason(conn, day, kind)
        return StatedBook(
            day=day, kind=kind, positions=rows, book_sha256=sha, via=via, turn_id=turn_id,
            readback_sha256=readback_sha256, reason=reason, supersedes=supersedes,
        )

    def record_stated_book(
        self,
        day: date,
        kind: str,
        positions: Iterable[Any],
        *,
        via: str,
        turn_id: Optional[str] = None,
        readback_sha256: Optional[str] = None,
        supersedes: Optional[int] = None,
        expected_sha256: Optional[str] = None,
        now: Optional[datetime] = None,
    ) -> StatedBook:
        """THE one writer of `drc_stated_books` (L3, L40): every caller —
        the page, the widget, the CLI — calls this and inserts nothing
        itself. Refused inside `market_reset` for every caller, before any
        read or write (v3 `[F-01]`, X6). `expected_sha256` is L7's
        mechanical half: what is written is what was reviewed."""
        assert_writable("drc.record_stated_book", target=day.isoformat(), now=now or clock_mod.now_utc())
        rows, sha = self._validated(kind, positions, via, turn_id, readback_sha256)
        if expected_sha256 is not None and expected_sha256 != sha:
            raise ValueError(
                f"book_sha256 {sha} is not the reviewed {expected_sha256} — nothing written"
            )
        trade = rows[0]["trade_id"] if kind == "resolve" else None
        what = f"{day} {kind}" + (f" for {trade}" if trade else "")
        conn = self._connect()
        conn.autocommit = False
        try:
            conn.execute('LOCK TABLE "user".drc_stated_books IN SHARE ROW EXCLUSIVE MODE')
            reason = self._reason(conn, day, kind)
            current = [
                r[0]
                for r in conn.execute(
                    f"SELECT id FROM drc_stated_books WHERE {_CURRENT} AND day = %s AND kind = %s "
                    "AND (%s::text IS NULL OR positions->0->>'trade_id' = %s) ORDER BY id",
                    (day, kind, trade, trade),
                ).fetchall()
            ]
            named = ", ".join(f"#{i}" for i in current) or "none"
            if supersedes is None and current:
                raise ValueError(
                    f"{what}: {self.STATED_TABLE} {named} is current — a restatement names it "
                    "with supersedes; nothing written"
                )
            if supersedes is not None and (supersedes not in current or len(current) > 1):
                raise ValueError(
                    f"{what}: supersedes #{supersedes} names no single current row — current: "
                    f"{named}; nothing written"
                )
            row = conn.execute(
                f"""
                INSERT INTO drc_stated_books (day, kind, positions, book_sha256, via, turn_id,
                                              readback_sha256, reason, supersedes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING {_STATED_COLUMNS}
                """,
                (day, kind, Jsonb(rows), sha, via, turn_id, readback_sha256, reason, supersedes),
            ).fetchone()
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return _stated(row)


__all__ = ["TABLES", "DrcStore"]
