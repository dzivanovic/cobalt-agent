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

K2 (v3 §6 K2, R51, R52)
- `record_day` re-pairs every LATER recorded day forward from the day it
  records, in one transaction, or writes nothing (`[F-03]`); a first
  record of an earlier day is a trigger too (R51). A day with no trading
  log needs its `no_trade` statement (`[F-05]`).
- `rebuild` — THE one re-pair of a day from its stored inputs (A1, a desk
  reading of R51), then forward. `_repair` is the one path (L3).
- `seed_for` — a statement beside a recorded close: the close wins, the
  statement stays history with `stated_differs` (R51); the `[F-06]`
  reader applies, supersedes or FAILS every current resolve.
- `stated_difference` — the R51 line, read from the stored `seed` row.
- The rebuild never writes his statements (L7).
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Iterable, Optional

from psycopg.types.json import Jsonb
from pydantic import TypeAdapter, ValidationError

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import assert_writable
from cobalt.session import clock as clock_mod

from . import trading_log
from .models import (
    DayPairing,
    ExecSide,
    Execution,
    ImportResult,
    Kind,
    OpenPosition,
    Outcome,
    PairingError,
    ParsedStatsLog,
    ParsedTradingLog,
    ResolveInput,
    ResolveOutcome,
    SeedBook,
    StatedBook,
    StatedPosition,
    StatedResolve,
    StatsRow,
    TradeStatus,
    missing_of,
)
from .pairing import (
    FN_VERSION,
    book_sha256,
    build_day,
    canonical_sha256,
    check_contiguity,
    stated_differs,
    stated_open_positions,
)

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


def _stopped(day: date) -> str:
    """Why the forward re-pair stops at a not-computed day (C4)."""
    return f"{day} has pairing not computed — its open positions are unknown"


def _outcomes(pairing: DayPairing, seed: Optional[SeedBook]) -> list[ResolveOutcome]:
    """Every resolve outcome of a computed day: the ones its book already
    decided (`seed_for`), then the ones `build_day` decided. A
    not-computed day applies none (C2)."""
    if "pairing" in pairing.not_computed:
        return []
    return [*(seed.resolve_outcomes if seed is not None else []), *pairing.resolves]


@dataclass(frozen=True)
class _Close:
    """A day re-paired in memory during ONE forward re-pair: what the next
    day's seed rule reads instead of the store (`[F-03]`)."""

    is_computed: bool
    positions: tuple[OpenPosition, ...]
    closed: frozenset[str]
    resolves: tuple[dict, ...]

    @staticmethod
    def computed(pairing: DayPairing) -> bool:
        return "pairing" not in pairing.not_computed

    @classmethod
    def of(cls, pairing: DayPairing, seed: Optional[SeedBook]) -> "_Close":
        return cls(
            is_computed=cls.computed(pairing),
            positions=tuple(pairing.open_positions),
            closed=frozenset(t.trade_id for t in pairing.trades if t.status is TradeStatus.CLOSED),
            resolves=tuple(o.model_dump(mode="json") for o in _outcomes(pairing, seed)),
        )

    def seed(self, day: date, prior: date) -> SeedBook:
        """`_carried`'s book, from memory (the hash is the one `record_day`
        will store for `prior`)."""
        if not self.is_computed:
            raise PairingError(
                f"{day}: the prior trading day {prior} has pairing not computed — its open "
                "positions are unknown; never assumed flat"
            )
        positions = sorted(self.positions, key=lambda p: p.trade_id)
        return SeedBook(
            source="carried", positions=positions, from_day=prior, from_book_sha256=book_sha256(positions)
        )


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
        number of rows written for `pairing.day`.

        `seed` is the book the pairing ran from (`seed_for`), REQUIRED of
        every caller: a COMPUTED pairing with `seed=None` is refused — no
        assumed book (L1). A not-computed day (no book stated, or a
        partial file) writes no `book_close`: it left no known book.

        K2: a day with no trading-log import is refused unless his
        `no_trade` statement for it is current (`[F-05]`). When a LATER
        day is recorded, every later recorded day is re-paired from this
        day's close in memory, in date order (`_repair`), and all of them
        are written in ONE transaction with this day — or, when any later
        day fails, nothing in `drc_rows` is (`[F-03]`, R51)."""
        computed = "pairing" not in pairing.not_computed
        if computed and seed is None:
            raise ValueError(
                f"{pairing.day}: a computed pairing with no book — record_day needs the "
                "SeedBook it ran from (seed_for); nothing written (L1)"
            )
        conn = self._connect()
        conn.autocommit = False
        try:
            no_trade_id = None
            if Kind.TRADING_LOG not in import_ids:
                no_trade_id = self._no_trade_id(conn, pairing.day)
                if no_trade_id is None:
                    raise ValueError(
                        f"{pairing.day}: no trading-log import and no no-trade DRC statement — "
                        "record_day refused; nothing written ([F-05])"
                    )
                # K2 fix r1 F-3: the one no-trade seed rule `_repair` uses (L3).
                seed = self._no_trade_seed(seed, no_trade_id)
            written, _ = self._commit(conn, pairing, import_ids, seed, no_trade_id)
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return written

    def rebuild(self, day: date) -> list[date]:
        """THE one re-pair of a recorded (or no-trade) day from its STORED
        inputs (A1 — R51 sub-item (iii), a DESK READING), then the forward
        re-pair of every later recorded day (C4), one transaction. Returns
        the dates written, `day` first. The same `_repair` is
        `record_day`'s forward step (L3). A remedy for a statement made
        after the day was recorded (a no-trade DRC, a resolve, an opening
        for an unpaired day) and for a pre-lane day (`rebuild <P>`, v3 §4
        row 4). It never writes his statements (R51, L7)."""
        conn = self._connect()
        conn.autocommit = False
        try:
            pairing, ids, seed, no_trade_id = self._repair(conn, day, {})
            _, dates = self._commit(conn, pairing, ids, seed, no_trade_id)
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return dates

    def stated_difference(self, day: date) -> Optional[str]:
        """R51's line for `/drc`, read from `day`'s stored `seed` row: his
        statement kept as history beside a close that differs from it —
        else `None`. Nothing is computed here."""
        with self._connect() as conn:
            row = conn.execute(
                f"SELECT inputs, derived FROM drc_rows WHERE user_id = {_TENANT} "
                "AND kind = 'seed' AND day = %s AND ref = 'book'",
                (day,),
            ).fetchone()
        if row is None:
            return None
        inputs, derived = row
        if inputs.get("stated_book_id") is None or not derived.get("stated_differs"):
            return None
        return (
            f"stated book for {day} differed from {inputs['from_day']}'s close: "
            f"{', '.join(derived['stated_differs'])}"
        )

    def stated_day(self, stated_id: int) -> date:
        """The `day` of the `drc_stated_books` row `stated_id` — any row,
        current or superseded. THE one read of a stated row's day (L3),
        used by `effect_day` and by the CLI's rebuild trigger (K2 fix r2
        F-1r2). An unknown id raises `ValueError`; nothing is assumed."""
        with self._connect() as conn:
            row = conn.execute(
                f"SELECT day FROM drc_stated_books WHERE user_id = {_TENANT} AND id = %s",
                (stated_id,),
            ).fetchone()
        if row is None:
            raise ValueError(f"supersedes #{stated_id} names no stated row — nothing assumed")
        return row[0]

    def effect_day(self, day: date, supersedes: Optional[int]) -> date:
        """The day a statement's rebuild starts from (K2 fix r1 F-1): `day`,
        or — for a restatement — the earlier of `day` and the superseded
        row's day, so the superseded resolve's effect leaves every stored
        row (L1; v3 `[F-06]` `:190`). An unknown id raises `ValueError`;
        nothing is assumed. K2 fix r2: the superseded row's day is read by
        `stated_day`, the one read (L3)."""
        return day if supersedes is None else min(day, self.stated_day(supersedes))

    def has_current_import(self, day: date, kind: Kind) -> bool:
        """Whether `day` has a current (not superseded) import of `kind`."""
        with self._connect() as conn:
            return self._current_import(conn, day, kind) is not None

    def has_chain_through(self, day: date) -> bool:
        """Whether a `day` row exists on or before `day` — a recorded chain
        a rebuild of `day` would join."""
        with self._connect() as conn:
            return conn.execute(
                f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' AND day <= %s LIMIT 1",
                (day,),
            ).fetchone() is not None

    # -----------------------------------------------------------------
    # K2 — the one re-pair (`_repair`) and the one write (`_commit`)
    # -----------------------------------------------------------------

    @staticmethod
    def _current_import(conn, day: date, kind: Kind):
        """The day's current import of `kind`: the row no other row
        supersedes (`record_import`'s predicate)."""
        return conn.execute(
            f"""
            SELECT id, name, parse_status, reason FROM drc_imports
             WHERE user_id = {_TENANT} AND import_date = %s AND kind = %s
               AND id NOT IN (SELECT supersedes FROM drc_imports
                               WHERE supersedes IS NOT NULL AND user_id = {_TENANT})
             ORDER BY id DESC LIMIT 1
            """,
            (day, kind.value),
        ).fetchone()

    @staticmethod
    def _no_trade_id(conn, day: date) -> Optional[int]:
        row = conn.execute(
            f"SELECT id FROM drc_stated_books WHERE {_CURRENT} AND day = %s AND kind = 'no_trade' "
            "ORDER BY id DESC LIMIT 1",
            (day,),
        ).fetchone()
        return None if row is None else int(row[0])

    def _repair(
        self, conn, day: date, overlay: dict[date, "_Close"]
    ) -> tuple[DayPairing, dict[Kind, int], Optional[SeedBook], Optional[int]]:
        """`day` paired again from its STORED inputs (A1): the fills of its
        CURRENT trading-log import (never the ids on its old `day` row), or
        its current `no_trade` statement; its stored `stats_row` rows,
        read before any delete; and its seed by `seed_for`'s one rule, with
        a prior day re-paired in this call read from `overlay`."""
        imp = self._current_import(conn, day, Kind.TRADING_LOG)
        no_trade_id = self._no_trade_id(conn, day)
        ids: dict[Kind, int] = {}
        if imp is not None:
            import_id, name, status, reason = imp
            if status == Outcome.FAILED.value:
                raise PairingError(
                    f"{day}: its current trading log {name} failed ({reason}) — nothing to re-pair; "
                    "never assumed empty (L1)"
                )
            executions = [
                Execution(
                    line=line,
                    time=None if at is None else at.astimezone(trading_log.ET),
                    symbol=symbol,
                    side=None if side is None else ExecSide(side),
                    price=price,
                    qty=qty,
                    route=route,
                    broker=broker,
                    account=account,
                    order_type=order_type,
                    order_id=order_id,
                )
                for line, at, symbol, side, price, qty, route, broker, account, order_type, order_id
                in conn.execute(
                    f"""SELECT line, executed_at, symbol, side, price, qty, route, broker, account,
                               order_type, order_id
                          FROM drc_fills WHERE user_id = {_TENANT} AND import_id = %s ORDER BY line""",
                    (import_id,),
                ).fetchall()
            ]
            outcome = Outcome(status)
            try:
                missing = missing_of(outcome, reason)
            except ValueError as e:
                raise PairingError(
                    f"{day}: its current trading log {name} is partial with an unreadable reason — "
                    "nothing assumed"
                ) from e
            result = ImportResult(
                name=name,
                kind=Kind.TRADING_LOG,
                outcome=outcome,
                reason=reason,
                missing=missing,
                # K2 fix r1 F-5 (v3 `:181` "exactly as its first record
                # did", `FR14`; L3): the parser's ONE partial-import rule,
                # on the file's own stored missing columns.
                not_computed=trading_log.pairing_not_computed(missing),
            )
            ids[Kind.TRADING_LOG] = int(import_id)
        elif no_trade_id is not None:
            executions = []
            result = ImportResult(name="no-trade DRC", kind=Kind.TRADING_LOG, outcome=Outcome.PARSED)
        else:
            raise PairingError(
                f"{day}: no trading-log import and no no-trade DRC — nothing to re-pair ([F-05])"
            )
        parsed = ParsedTradingLog(result=result, import_date=day, executions=executions)

        day_row = conn.execute(
            f"SELECT inputs, derived FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' AND day = %s",
            (day,),
        ).fetchone()
        stored_rows = [
            r[0]
            for r in conn.execute(
                f"SELECT derived FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'stats_row' "
                "AND day = %s ORDER BY ref",
                (day,),
            ).fetchall()
        ]
        stats: Optional[ParsedStatsLog] = None
        if stored_rows:
            # K2 fix r1 F-4 (A1 `:179`, a DESK READING of R51: "Re-run
            # `match_stats` … from those stored rows against the new
            # pairing"): the stats input is rebuilt with its OWN file's
            # missing columns and always re-matched — a day still not
            # computed stores "pairing did not run" (true), a paired day
            # matches exactly as its first record (a `Side`-less file to the
            # same `not computed — missing: Side`: no match invented).
            stats_id = ((day_row[0] if day_row else {}).get("import_ids") or {}).get(Kind.STATS_LOG.value)
            if stats_id is None:
                raise PairingError(f"{day}: stats rows are stored with no stats import named — nothing assumed")
            ids[Kind.STATS_LOG] = int(stats_id)
            stats_name, stats_status, stats_reason = conn.execute(
                f"SELECT name, parse_status, reason FROM drc_imports WHERE user_id = {_TENANT} AND id = %s",
                (int(stats_id),),
            ).fetchone()
            stats_outcome = Outcome(stats_status)
            try:
                stats_missing = missing_of(stats_outcome, stats_reason)
            except ValueError as e:
                raise PairingError(
                    f"{day}: its stats log {stats_name} is partial with an unreadable reason — nothing assumed"
                ) from e
            stats = ParsedStatsLog(
                result=ImportResult(
                    name=stats_name, kind=Kind.STATS_LOG, outcome=stats_outcome, missing=stats_missing
                ),
                rows=[StatsRow.model_validate(d["row"]) for d in stored_rows],
            )

        seed = self._no_trade_seed(self._seed(conn, day, overlay), no_trade_id if imp is None else None)
        pairing = build_day(
            parsed,
            stats,
            seed=None if seed is None else seed.positions,
            resolves=() if seed is None else seed.resolves,
        )
        return pairing, ids, seed, (no_trade_id if imp is None else None)

    @staticmethod
    def _no_trade_seed(seed: Optional[SeedBook], no_trade_id: Optional[int]) -> Optional[SeedBook]:
        """THE no-trade seed rule (K2 fix r1 F-3; v3 §2b `:97`, `[F-05]`;
        L3), called by `_repair` and by `record_day`: a `carried` book with
        no statement, on a day whose input is his `no_trade` DRC, is
        `no_trade_carry` naming it. A carried book naming his statement
        stays `carried` with its link and difference (R51, L7); anything
        else is returned unchanged."""
        if (
            seed is None
            or no_trade_id is None
            or seed.source != "carried"
            or seed.stated_book_id is not None
        ):
            return seed
        return SeedBook(
            source="no_trade_carry",
            positions=seed.positions,
            from_day=seed.from_day,
            from_book_sha256=seed.from_book_sha256,
            no_trade_id=no_trade_id,
            resolves=seed.resolves,
            resolve_outcomes=seed.resolve_outcomes,
        )

    def _commit(
        self,
        conn,
        pairing: DayPairing,
        import_ids: dict[Kind, int],
        seed: Optional[SeedBook],
        no_trade_id: Optional[int],
    ) -> tuple[int, list[date]]:
        """Write `pairing.day` and re-pair every later recorded day forward
        (`[F-03]`, R51 side A: a first record of an earlier day is a
        trigger too). All in memory first; any later day that raises →
        `PairingError` naming it and nothing written. A day that comes out
        `not computed` STOPS the chain: every later day keeps its rows and
        is named in `not_repaired` (the ESCALATE default, C4).

        K2 fix r1 F-2 (L1; v3 §4 `:214`, `:232`; L72): each day named in
        `not_repaired` also carries `derived.book_stale = {root, reason}`
        on its OWN `day` row, in this transaction — one `UPDATE` of that
        row's `derived` (`drc_rows` has no append-only trigger; only
        `drc_stated_books` does, `0018_drc_stated_books.sql:51`). Nothing
        else of that day is touched. `_carried` refuses a marked prior. A
        re-pair that reaches a marked day rewrites its rows whole through
        `_rows`, so the mark leaves with the stale book; nothing else
        clears it."""
        later = [
            r[0]
            for r in conn.execute(
                f"SELECT DISTINCT day FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' "
                "AND day > %s ORDER BY day",
                (pairing.day,),
            ).fetchall()
        ]
        extra: dict[str, Any] = {}
        writes: list[tuple[date, list]] = []
        dates = [pairing.day]
        stale: list[date] = []
        stale_mark: dict[str, str] = {}
        if later:
            overlay = {pairing.day: _Close.of(pairing, seed)}
            root = None if _Close.computed(pairing) else pairing.day
            stop = None if root is None else _stopped(root)
            repaired: list[str] = []
            not_repaired: list[dict] = []
            for n in later:
                if stop is not None:
                    not_repaired.append({"day": n.isoformat(), "reason": stop})
                    stale.append(n)
                    stale_mark = {"root": root.isoformat(), "reason": stop}
                    continue
                try:
                    p, ids, s, nt = self._repair(conn, n, overlay)
                except PairingError as e:
                    raise PairingError(
                        f"{pairing.day}: not recorded — the forward re-pair of {n} failed: {e}"
                    ) from e
                writes.append((n, self._rows(p, ids, s, nt, {})))
                overlay[n] = _Close.of(p, s)
                repaired.append(n.isoformat())
                dates.append(n)
                if not _Close.computed(p):
                    root, stop = n, _stopped(n)
            extra["repaired"] = repaired
            if not_repaired:
                extra["not_repaired"] = not_repaired
        rows = self._rows(pairing, import_ids, seed, no_trade_id, extra)
        for d, out in [(pairing.day, rows), *writes]:
            conn.execute(f"DELETE FROM drc_rows WHERE user_id = {_TENANT} AND day = %s", (d,))
            with conn.cursor() as cur:
                cur.executemany(
                    """
                    INSERT INTO drc_rows (day, kind, ref, inputs, derived, fn_version)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    [(d, kind, ref, Jsonb(i), Jsonb(dv), FN_VERSION) for kind, ref, i, dv in out],
                )
        for d in stale:
            conn.execute(
                f"UPDATE drc_rows SET derived = derived || %s WHERE user_id = {_TENANT} "
                "AND day = %s AND kind = 'day'",
                (Jsonb({"book_stale": stale_mark}), d),
            )
        return len(rows), dates

    @staticmethod
    def _rows(
        pairing: DayPairing,
        import_ids: dict[Kind, int],
        seed: Optional[SeedBook],
        no_trade_id: Optional[int],
        extra: dict[str, Any],
    ) -> list[tuple[str, str, dict, dict]]:
        """The day's `drc_rows`, each with its inputs (L57)."""
        computed = "pairing" not in pairing.not_computed
        trading_id = import_ids.get(Kind.TRADING_LOG)
        stats_id = import_ids.get(Kind.STATS_LOG)
        applied = {o.trade_id: o.resolve_id for o in pairing.resolves if o.status == "applied"}
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
                    if seed.from_day is not None
                    else {"stated_book_id": seed.stated_book_id}
                )
            if t.trade_id in applied:
                trade_inputs[t.trade_id]["resolve_id"] = applied[t.trade_id]
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
        if no_trade_id is not None:
            day_inputs["no_trade_id"] = no_trade_id  # `[F-05]`: the empty day's input
        day_derived: dict[str, Any] = {
            "trades": len(pairing.trades),
            "open_positions": len(pairing.open_positions),
            "unmatched": len(pairing.unmatched),
            "not_computed": dict(pairing.not_computed),
        }
        outcomes = _outcomes(pairing, seed)
        if outcomes:
            day_derived["resolves"] = [o.model_dump(mode="json") for o in outcomes]
        day_derived.update(extra)
        out.append(("day", "day", day_inputs, day_derived))
        if seed is not None:
            # What the day started from (v3 §2b step 3).
            seed_inputs: dict[str, Any] = {
                "source": seed.source,
                "from_day": seed.from_day.isoformat() if seed.from_day else None,
                "from_book_sha256": seed.from_book_sha256,
                "stated_book_id": seed.stated_book_id,
            }
            if seed.no_trade_id is not None:
                seed_inputs["no_trade_id"] = seed.no_trade_id
            seed_derived: dict[str, Any] = {
                "count": len(seed.positions),
                "trade_ids": sorted(p.trade_id for p in seed.positions),
            }
            if seed.source == "carried" and seed.stated_book_id is not None:
                # R51 / L7: his statement kept by id, the difference stored.
                seed_derived["stated_differs"] = list(seed.stated_differs)
            out.append(("seed", "book", seed_inputs, seed_derived))
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
        return out

    def seed_for(self, day: date) -> Optional[SeedBook]:
        """The book `day` starts from, or `None` when no book is stated.

        P = the prior trading day. P recorded → P's `book_close`, checked
        against a hash recomputed over P's `open_position` rows (carried);
        when his `opening` statement for `day` also exists, the close wins
        and the statement is kept as history with the difference (R51,
        K2). P not recorded → his current `opening` statement for `day`
        (stated: the first import, or a chain he mended). Nothing recorded
        before `day` and nothing stated → `None`. The day's stored resolves
        are read (`[F-06]`). Every other case FAILS loud, naming why —
        never an assumed flat book (L1, v3 §2b, §4)."""
        with self._connect() as conn:
            return self._seed(conn, day, {})

    def _seed(self, conn, day: date, overlay: dict[date, "_Close"]) -> Optional[SeedBook]:
        """`seed_for`'s ONE rule (L3), also `_repair`'s: a day re-paired
        earlier in the same call is read from `overlay`, never the store."""
        from cobalt.daymode.propose import prior_trading_day

        prior = prior_trading_day(day)
        recorded = {
            r[0]
            for r in conn.execute(
                f"SELECT DISTINCT day FROM drc_rows WHERE user_id = {_TENANT} "
                "AND kind = 'day' AND day < %s",
                (day,),
            ).fetchall()
        } | {d for d in overlay if d < day}
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
            book = overlay[prior].seed(day, prior) if prior in overlay else self._carried(conn, day, prior)
            if stated is not None:
                # R51 (side A of R2-1): the close wins; his statement is kept
                # as history, with the difference stored and shown.
                said = stated_open_positions(day, _OPENING.validate_python(stated.positions))
                book = SeedBook(
                    source="carried",
                    positions=book.positions,
                    from_day=book.from_day,
                    from_book_sha256=book.from_book_sha256,
                    stated_book_id=stated.id,
                    stated_differs=stated_differs(said, book.positions),
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
        return self._with_resolves(conn, day, book, overlay)

    def _with_resolves(self, conn, day: date, book: SeedBook, overlay: dict[date, "_Close"]) -> SeedBook:
        """The `[F-06]` reader: every CURRENT `resolve` row, all days.
        Two for one trade id FAIL naming both (`[F-01]`, v3 §4 row 15). One
        dated `day` naming a held trade is applied by `build_day`; naming a
        trade an earlier export closed, it is superseded; naming anything
        else, it FAILS. One dated before `day` whose trade is still held
        and was not superseded on its own day FAILS naming `rebuild <R>` —
        a later day never silently carries a resolved trade."""
        rows = conn.execute(
            f"SELECT id, day, positions->0 FROM drc_stated_books WHERE {_CURRENT} "
            "AND kind = 'resolve' ORDER BY id"
        ).fetchall()
        by_trade: dict[str, list[int]] = {}
        for resolve_id, _, position in rows:
            by_trade.setdefault(position["trade_id"], []).append(resolve_id)
        for trade_id, ids in by_trade.items():
            if len(ids) > 1:
                raise PairingError(
                    f"{day}: {len(ids)} current resolves name {trade_id} — "
                    f"{' and '.join(f'#{i}' for i in ids)}; one restatement must supersede the "
                    "other (v3 [F-01]); nothing assumed"
                )
        held = {p.trade_id for p in book.positions}
        inputs: list[ResolveInput] = []
        outcomes: list[ResolveOutcome] = []
        for resolve_id, resolve_day, position in rows:
            resolve = _RESOLVE.validate_python([position])[0]
            trade_id = resolve.trade_id
            if resolve_day == day:
                if trade_id in held:
                    inputs.append(ResolveInput(id=resolve_id, resolve=resolve))
                    continue
                closed_on = self._closed_on(conn, trade_id, day, overlay)
                if closed_on is None:
                    raise PairingError(
                        f"{day}: resolve #{resolve_id} names {trade_id}, which {day}'s opening book "
                        "does not hold"
                    )
                outcomes.append(ResolveOutcome(
                    resolve_id=resolve_id, trade_id=trade_id, status="superseded",
                    reason=f"superseded — closed by the export of {closed_on}",
                ))
            elif resolve_day < day and trade_id in held and not self._superseded_on(
                conn, resolve_day, resolve_id, overlay
            ):
                raise PairingError(
                    f"{day}: resolve #{resolve_id} for {trade_id} dated {resolve_day} is not applied "
                    f"— rebuild {resolve_day}"
                )
        return book.model_copy(update={"resolves": inputs, "resolve_outcomes": outcomes})

    @staticmethod
    def _closed_on(conn, trade_id: str, day: date, overlay: dict[date, "_Close"]) -> Optional[date]:
        """The latest recorded day before `day` whose trades closed `trade_id`."""
        days = {d for d, c in overlay.items() if d < day and trade_id in c.closed}
        days |= {
            r[0]
            for r in conn.execute(
                f"SELECT day FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'trade' AND ref = %s "
                "AND derived->>'status' = 'closed' AND day < %s",
                (trade_id, day),
            ).fetchall()
            if r[0] not in overlay
        }
        return max(days) if days else None

    @staticmethod
    def _superseded_on(conn, day: date, resolve_id: int, overlay: dict[date, "_Close"]) -> bool:
        """Whether `day`'s pairing recorded this resolve as superseded."""
        if day in overlay:
            outcomes = overlay[day].resolves
        else:
            row = conn.execute(
                f"SELECT derived->'resolves' FROM drc_rows WHERE user_id = {_TENANT} "
                "AND kind = 'day' AND day = %s",
                (day,),
            ).fetchone()
            outcomes = (row[0] if row else None) or []
        return any(o["resolve_id"] == resolve_id and o["status"] == "superseded" for o in outcomes)

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
        stale = conn.execute(
            f"SELECT derived->'book_stale' FROM drc_rows WHERE user_id = {_TENANT} "
            "AND kind = 'day' AND day = %s AND derived ? 'book_stale'",
            (prior,),
        ).fetchone()
        if stale:
            # K2 fix r1 F-2: a day left behind a not-computed root holds a
            # book that root's new file may contradict (L1).
            root = stale[0]["root"]
            raise PairingError(
                f"{day}: the prior trading day {prior} is stale — {root} was re-recorded with pairing "
                f"not computed, so {prior}'s book is unknown; state {root}'s book and rebuild {root}; "
                "never carried"
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
        """Derived by the store, never passed in (v3 `:139`). An `opening`
        for a day whose prior trading day is recorded is REFUSED: that day
        starts from the recorded close (R51), and neither reason v3 names
        would be true of it (L1)."""
        if kind == "resolve":
            return "closed outside export"
        if kind == "no_trade":
            return "no-trade DRC"
        from cobalt.daymode.propose import prior_trading_day

        earlier = conn.execute(
            f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' AND day < %s LIMIT 1",
            (day,),
        ).fetchone()
        if not earlier:
            return "first import"
        # Only a day with history asks the calendar (a recorded P implies it).
        prior = prior_trading_day(day)
        if conn.execute(
            f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' AND day = %s LIMIT 1",
            (prior,),
        ).fetchone():
            raise ValueError(
                f"{day} opening: {prior} is recorded — {day} starts from {prior}'s close "
                "(v3 §2b; R51: the close wins); a stated opening is taken only on a first "
                "import or a broken chain (v3 §2c); nothing written"
            )
        return f"chain broken at {prior}"

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
            if kind == "resolve":
                # K2 fix r1 F-1 (v3 `[F-01]` `:126`, `:134`): a resolve's
                # key is its trade id, ON ANY DAY — a second current one is
                # refused, and a restatement on another day supersedes it.
                found = conn.execute(
                    f"SELECT id, day FROM drc_stated_books WHERE {_CURRENT} AND kind = 'resolve' "
                    "AND positions->0->>'trade_id' = %s ORDER BY id",
                    (trade,),
                ).fetchall()
            else:
                found = conn.execute(
                    f"SELECT id, day FROM drc_stated_books WHERE {_CURRENT} AND day = %s AND kind = %s "
                    "ORDER BY id",
                    (day, kind),
                ).fetchall()
            current = [r[0] for r in found]
            named = ", ".join(f"#{i} ({d})" for i, d in found) or "none"
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
