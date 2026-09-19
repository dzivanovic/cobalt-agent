"""Persistence for archived bars. Idempotent upserts.

The database is NOT named here: `COBALT_ENV` chooses it via
`cobalt.env.resolve_db_name()` (RULING 7/9) — production writes
`cobalt_brain`, dev and the test suite write `cobalt_dev`.

Until RULING 9 (2026-09-04) this module defaulted to `"cobalt_dev"` as
a literal, which is how 4.5M rows of PRODUCTION bars came to live in
the dev database while every other store had already moved onto the
resolver. `bars` was migrated to `cobalt_brain` in the same ruling.

DDL lives in exactly one place (migrations/0001_bars.sql) — this module
executes that file, it does not carry a second copy (one-path rule).
"""

from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Optional

from cobalt import db, env
from cobalt.db import Side

from .models import Bar, Interval
from .reconcile import values_from_row

MIGRATION_SQL = Path(__file__).parent / "migrations" / "0001_bars.sql"

#: §9: ONE constant key for the run-level advisory lock, SESSION level.
#: Held for the whole of `run_full`, `run_backfill`, `restate --apply`
#: and `backfill-missing`, in BOTH write modes. The POLLER does not take
#: it (R8: the live radar's write path is not touched by this build), so
#: this lock serialises the archiver against ITSELF and against repairs —
#: it is not, and is not claimed to be, protection against the poller.
#: The number is arbitrary but FIXED: two holders must collide.
ARCHIVE_RUN_LOCK_KEY = 20260919


class ArchiveLockError(RuntimeError):
    """Another archive or repair run holds the run-level lock."""


def try_acquire_run_lock(conn, *, what: str | None = None) -> bool:
    """Take the run-level lock on `conn`, or return False.

    SESSION level, not transaction level: a repair re-checks the quiet
    window immediately before COMMIT and rolls back when it has closed
    (§8), and `pg_try_advisory_xact_lock` would hand the lock away at
    that rollback while the command is still running.

    `what` turns the refusal into an exception instead of a False, for
    the callers that cannot continue without it.
    """
    held = conn.execute(
        "SELECT pg_try_advisory_lock(%s)", (ARCHIVE_RUN_LOCK_KEY,)
    ).fetchone()[0]
    if held:
        return True
    if what is not None:
        raise ArchiveLockError(
            f"another archive/repair run holds the lock — refusing to start "
            f"{what}. One archiver writes to system.bars at a time (spec §9); "
            "wait for the other run to finish, or find it in `cobalt jobs list`."
        )
    return False


def release_run_lock(conn) -> None:
    """Give the run-level lock back. Safe to call when it is not held."""
    conn.execute("SELECT pg_advisory_unlock(%s)", (ARCHIVE_RUN_LOCK_KEY,))


class BarStore:
    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    #: `bars` is engine data: market history any trader's strategies read.
    #: Nothing here is one trader's choice, so nothing here is user data.
    SIDE = Side.SYSTEM

    def __init__(self, db_name: Optional[str] = None):
        """`db_name` is a TEST/TOOLING seam only. Production and dev both
        leave it None and take the database from `COBALT_ENV` via
        `env.resolve_db_name()` — RULING 9 removed the hard-coded
        `"cobalt_dev"` default that kept the archiver writing production
        bars into the dev database."""
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            db.assert_schemas_exist(conn)
            conn.execute(MIGRATION_SQL.read_text())

    def upsert_bars(
        self,
        bars: list[Bar],
        *,
        before_commit: Callable[[], None] | None = None,
    ) -> int:
        """Insert or refresh `bars`. Returns the number of rows written.

        ON CONFLICT DO UPDATE (not DO NOTHING): a re-run refreshes a bar
        that Finviz may have finalized/revised since the last pull,
        rather than freezing it at its first-seen (possibly provisional)
        values. PK (ticker, interval, ts) makes this a true idempotent
        upsert either way — no duplicates, ever.
        """
        if not bars:
            return 0
        with self._connect() as conn:
            written = self.upsert_bars_on(conn, bars)
            if before_commit is not None:
                before_commit()
        return written

    def upsert_bars_on(self, conn, bars: list[Bar]) -> int:
        """`upsert_bars`, on a connection the CALLER owns.

        Same statement, one copy of it (L3) — the difference is whose
        transaction the rows belong to. `restate --apply` needs that:
        §8's pre-commit re-check raises INSIDE the repair's
        `target_transaction`, and a rollback there can only undo rows
        written on that same connection. Until the tribunal's F1 the
        repair called `upsert_bars`, which opens and commits its own
        connection, so a refused repair left the rewritten bars behind —
        exactly the plausible partial write L1 forbids.

        The nightly `upsert` call site (`runner.py:130`) passes no
        connection and is unchanged: it still goes through
        `upsert_bars`.
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

    def bars_between(self, ticker: str, interval: Interval, start, end) -> list[Bar]:
        """Stored bars for one ticker/interval with `start <= ts < end`,
        oldest first — the read the nightly replay's coverage check and
        counterfactual R consume (S2-P4)."""
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT ticker, interval, ts, open, high, low, close, volume FROM bars "
                "WHERE ticker = %s AND interval = %s AND ts >= %s AND ts < %s ORDER BY ts",
                (ticker, Interval(interval).value, start, end),
            ).fetchall()
        return [
            Bar(ticker=r[0], interval=r[1], ts=r[2], open=r[3], high=r[4], low=r[5], close=r[6], volume=r[7])
            for r in rows
        ]

    def watermark(self, ticker: str, interval: str = "i1"):
        """Newest stored timestamp for one ticker/interval, or None."""
        with self._connect() as conn:
            row = conn.execute(
                "SELECT max(ts) FROM bars WHERE ticker = %s AND interval = %s",
                (ticker, interval),
            ).fetchone()
        return row[0] if row else None

    def count_rows(self) -> int:
        with self._connect() as conn:
            row = conn.execute("SELECT count(*) FROM bars").fetchone()
        return int(row[0]) if row else 0

    # -- the append path (FINAL design 2026-09-19, §3 V2-1, §4, §9) ----
    #
    # EVERY METHOD BELOW TAKES A CONNECTION. §4: one transaction on one
    # connection per target holds the stored-range read, the inserts, the
    # progress write, the incident writes and the accepted outcome, so a
    # crash between any two of them commits none of them. A method that
    # opened its own connection would break that guarantee silently —
    # which is why the offline tests assert it with a recording fake
    # rather than by reading the code.

    @contextmanager
    def run_lock(self, what: str):
        """Hold §9's run-level lock for the whole of a run or a repair.

        Its own SESSION, separate from any target's transaction: the
        lock outlives every per-target commit and rollback, which is
        exactly what "one archiver writes at a time" means. Released and
        closed on the way out, whatever happened in between.
        """
        conn = self._connect()
        try:
            try_acquire_run_lock(conn, what=what)
            yield conn
        finally:
            try:
                release_run_lock(conn)
            finally:
                conn.close()

    @contextmanager
    def target_transaction(self):
        """ONE connection, ONE transaction, for one target's whole night.

        Commits on a clean exit, rolls back on any exception, and always
        closes. A failed or withheld target's transaction is rolled back
        here; its failure EVIDENCE (the incident) is then persisted in a
        SECOND small transaction by the runner — Astra's V3-2 point,
        because evidence written inside the doomed transaction dies with
        it.
        """
        conn = self._connect()
        conn.autocommit = False
        try:
            yield conn
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def insert_new_bars(self, conn, bars: list[Bar]) -> int:
        """Offer `bars`; return how many rows were ACTUALLY inserted.

        `ON CONFLICT … DO NOTHING`, not `DO UPDATE`: this is the whole
        of the owner's ruling (R14/R15) in one clause — "only add the
        new [bars] in the database that don't exist". A key already
        stored is left exactly as it is, whatever the vendor now says
        about it; a difference is a `restated` incident for a person to
        look at, never a silent overwrite.

        THE COUNT IS THE SERVER'S, NEVER `len(rows)` (§3 V2-1). A bar
        the radar poller committed between this transaction's range read
        and this statement is a CONFLICT — not an error, and not an
        insert. Reporting `len(rows)` would count it as written and
        break §7's identity `incoming_only = inserted +
        concurrent_conflicts`. psycopg sets `rowcount` to the total rows
        affected across an `executemany`; if the driver cannot say, this
        FAILS rather than guessing (L1).
        """
        if not bars:
            return 0
        rows = [
            (b.ticker, b.interval.value, b.ts, b.open, b.high, b.low, b.close, b.volume)
            for b in bars
        ]
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO bars (ticker, interval, ts, open, high, low, close, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (ticker, interval, ts) DO NOTHING
                """,
                rows,
            )
            inserted = cur.rowcount
        if not isinstance(inserted, int) or inserted < 0:
            raise RuntimeError(
                f"the driver reported row count {inserted!r} for an insert of "
                f"{len(rows)} bar(s). The append night's counters reconcile "
                "against the number of rows ACTUALLY inserted, so a run that "
                "cannot learn it fails rather than reporting the number it "
                "hoped for (L1, L57)."
            )
        return inserted

    def _bars_in_range(
        self, conn, ticker: str, interval: Interval, start, end
    ) -> dict:
        """The stored rows of one target over `[start, end]`, normalised.

        PRIVATE and CONNECTION-TAKING on purpose (spec O-5). The
        unmerged `sprint-2/p4` adds `BarStore.bars_between()`, which
        opens its own connection; after both land there must be ONE
        range read, and the second lander folds them into one method
        with an optional connection (L3). Until then this branch adds
        exactly one, and the ESCALATE names the overlap.

        Returns `{ts: BarValues}` — already normalised to the column's
        own `NUMERIC(14,4)` / integer shape, so the comparison in
        `reconcile` is deciding on values rather than on renderings.
        """
        cursor = conn.execute(
            "SELECT ts, open, high, low, close, volume FROM bars "
            "WHERE ticker = %s AND interval = %s AND ts >= %s AND ts <= %s "
            "ORDER BY ts",
            (ticker, interval.value if isinstance(interval, Interval) else interval,
             start, end),
        )
        return {row[0]: values_from_row(row[1:]) for row in cursor.fetchall()}
