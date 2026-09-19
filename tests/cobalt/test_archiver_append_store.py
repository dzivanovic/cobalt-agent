"""Chunk P — the append path's writers, all on the TARGET'S ONE CONNECTION.

Spec `ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §3 (V2-1 as amended by
V3-2), §4, §9, §11.

§4 is the rule this file exists to enforce: **one transaction on one
connection per target** holds the stored-range read, the inserts, the
progress write, the incident writes and the accepted outcome. A crash
between any two of them commits none of them. So none of these methods
may open or commit a connection of its own — they TAKE one — and the
offline half proves that with a recording fake (the shape
`test_migrate_proof.py` uses) rather than by reading the code.

The `requires_db` half is written here and owed its first run on
`cobalt_dev` once `p4-verify-0919` releases the lane (L41 interim).
"""

from __future__ import annotations

import inspect
import os
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.archiver import incidents as incidents_mod
from cobalt.archiver import progress as progress_mod
from cobalt.db import Side
from cobalt.archiver.models import Bar, Interval
from cobalt.archiver.reconcile import (
    BarValues,
    IncidentDraft,
    IncidentKind,
    compare,
    plan_candidates,
    reconcile,
)
from cobalt.archiver.store import (
    ARCHIVE_RUN_LOCK_KEY,
    ArchiveLockError,
    BarStore,
    release_run_lock,
    try_acquire_run_lock,
)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

UTC = timezone.utc


def ts(minute: int) -> datetime:
    return datetime(2026, 9, 18, 19, minute, tzinfo=UTC)


def bar(when: datetime, close="100.00", ticker="TESTARCH", interval=Interval.I5) -> Bar:
    return Bar(
        ticker=ticker, interval=interval, ts=when,
        open=Decimal("99.00"), high=Decimal("101.00"), low=Decimal("98.50"),
        close=Decimal(close), volume=1234,
    )


# ---------------------------------------------------------------------
# A recording fake connection — the shape test_migrate_proof.py uses
# ---------------------------------------------------------------------


class _FakeCursor:
    def __init__(self, conn, rows=(), rowcount=0):
        self._conn = conn
        self._rows = list(rows)
        self.rowcount = rowcount

    def execute(self, query, params=None):
        self._conn.queries.append((str(query), params))
        return self

    def executemany(self, query, rows, **kwargs):
        self._conn.queries.append((str(query), list(rows)))
        self._conn.executemany_calls += 1
        self.rowcount = self._conn.executemany_rowcount
        return self

    def fetchone(self):
        return self._rows[0] if self._rows else None

    def fetchall(self):
        return list(self._rows)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class _FakeConn:
    """Records every statement; refuses to be a connection MANAGER.

    `commit`, `rollback` and `close` are recorded rather than forbidden,
    so a test can assert they were never called — which is stronger than
    an exception, because it also catches a call inside a `finally`.
    """

    def __init__(self, rows=(), executemany_rowcount=0):
        self.queries: list[tuple[str, object]] = []
        self.rows = list(rows)
        self.executemany_rowcount = executemany_rowcount
        self.executemany_calls = 0
        self.commits = 0
        self.rollbacks = 0
        self.closes = 0

    def execute(self, query, params=None):
        self.queries.append((str(query), params))
        return _FakeCursor(self, self.rows)

    def cursor(self, *args, **kwargs):
        return _FakeCursor(self, self.rows)

    def commit(self):
        self.commits += 1

    def rollback(self):
        self.rollbacks += 1

    def close(self):
        self.closes += 1

    @property
    def sql(self) -> str:
        return "\n".join(q for q, _ in self.queries)


@pytest.fixture
def no_connections(monkeypatch):
    """Any attempt to OPEN a connection inside these methods is a failure."""
    def _boom(*_a, **_k):
        raise AssertionError(
            "a method of the append path opened its own connection — §4 says "
            "every one of them takes the target's connection"
        )

    monkeypatch.setattr(BarStore, "_connect", _boom)
    return _boom


def store() -> BarStore:
    return BarStore(db_name="unused-offline")


def code_of(obj) -> str:
    """Source with docstrings and comments removed.

    Several assertions below are about what the CODE does — which
    statement is sent, which clause is in it. The prose around that code
    deliberately names the thing it is not doing (`upsert_bars`'s
    docstring explains why it is `DO UPDATE` rather than `DO NOTHING`),
    so a substring search over raw source would read the explanation and
    fail. `ast.unparse` drops both.
    """
    import ast
    import textwrap

    tree = ast.parse(textwrap.dedent(inspect.getsource(obj)))
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if not isinstance(body, list) or not body:
            continue
        first = body[0]
        if (
            isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)
        ):
            node.body = body[1:] or [ast.Pass()]
    return ast.unparse(tree)


# ---------------------------------------------------------------------
# upsert_bars is UNTOUCHED (§5, mode isolation)
# ---------------------------------------------------------------------


def test_upsert_bars_still_does_update_and_never_do_nothing():
    """§5's mode isolation, followed to where the statement now lives.

    Tribunal round 1, F1 moved the `DO UPDATE` into the
    connection-taking sibling `upsert_bars_on`, because `restate
    --apply` must write on the repair's own transaction. There is still
    exactly ONE copy of the statement (L3) and `upsert_bars` still
    reaches it on its OWN connection with the same result — which is
    what the nightly `upsert` night depends on. Asserted across the
    pair, so the property survives the indirection rather than being
    dropped with it.
    """
    source = code_of(BarStore.upsert_bars_on)
    assert "ON CONFLICT (ticker, interval, ts) DO UPDATE SET" in source
    assert "DO NOTHING" not in source
    assert "return len(rows)" in source

    caller = code_of(BarStore.upsert_bars)
    assert "self._connect()" in caller, "the nightly write still owns its connection"
    assert "self.upsert_bars_on(conn, bars)" in caller
    assert "before_commit()" in caller
    assert "ON CONFLICT" not in caller, "a second copy of the statement (L3)"


def test_only_one_copy_of_the_upsert_statement_exists():
    """L3, as an assertion: F1's fix must not leave two `DO UPDATE`s."""
    source = inspect.getsource(BarStore)
    assert source.count("ON CONFLICT (ticker, interval, ts) DO UPDATE SET") == 1


def test_upsert_bars_on_takes_the_callers_connection_and_never_opens_one(no_connections):
    """The append path's rule (`store.py`'s own comment): every method
    below the line TAKES a connection. `upsert_bars_on` joins them —
    it must not connect, commit or close."""
    conn = _FakeConn()
    written = store().upsert_bars_on(conn, [bar(ts(50))])
    assert written == 1
    assert "ON CONFLICT (ticker, interval, ts) DO UPDATE SET" in conn.sql
    assert conn.executemany_calls == 1
    assert (conn.commits, conn.rollbacks, conn.closes) == (0, 0, 0)


def test_upsert_bars_on_is_a_noop_on_an_empty_list(no_connections):
    conn = _FakeConn()
    assert store().upsert_bars_on(conn, []) == 0
    assert conn.queries == []


def test_upsert_bars_signature_is_unchanged():
    sig = inspect.signature(BarStore.upsert_bars)
    assert list(sig.parameters) == ["self", "bars", "before_commit"]
    assert sig.parameters["before_commit"].kind is inspect.Parameter.KEYWORD_ONLY


# ---------------------------------------------------------------------
# insert_new_bars — DO NOTHING, ACTUAL inserts, someone else's connection
# ---------------------------------------------------------------------


def test_insert_new_bars_uses_do_nothing_on_the_primary_key(no_connections):
    conn = _FakeConn(executemany_rowcount=3)
    store().insert_new_bars(conn, [bar(ts(m)) for m in (50, 55, 58)])
    assert "ON CONFLICT (ticker, interval, ts) DO NOTHING" in conn.sql
    assert "DO UPDATE" not in conn.sql


def test_insert_new_bars_counts_actual_inserts_not_rows_sent(no_connections):
    """§3 V2-1: 'counting ACTUAL inserts … never `len(rows)`'. Three bars
    are sent and the server reports one row affected — two lost the race
    to the poller. The method must return 1."""
    conn = _FakeConn(executemany_rowcount=1)
    assert store().insert_new_bars(conn, [bar(ts(m)) for m in (50, 55, 58)]) == 1


def test_insert_new_bars_never_opens_or_commits_a_connection(no_connections):
    conn = _FakeConn(executemany_rowcount=2)
    store().insert_new_bars(conn, [bar(ts(50)), bar(ts(55))])
    assert (conn.commits, conn.rollbacks, conn.closes) == (0, 0, 0)


def test_insert_new_bars_of_nothing_touches_the_connection_at_all(no_connections):
    conn = _FakeConn()
    assert store().insert_new_bars(conn, []) == 0
    assert conn.queries == []


def test_insert_new_bars_refuses_a_row_count_the_driver_did_not_give(no_connections):
    """L1: if the driver cannot say how many rows it inserted, the run
    FAILS rather than reporting the number it hoped for."""
    conn = _FakeConn(executemany_rowcount=-1)
    with pytest.raises(RuntimeError) as e:
        store().insert_new_bars(conn, [bar(ts(50))])
    assert "row count" in str(e.value).lower()


def test_insert_new_bars_sends_one_statement_for_the_whole_batch(no_connections):
    conn = _FakeConn(executemany_rowcount=50)
    store().insert_new_bars(conn, [bar(ts(0) + timedelta(minutes=i)) for i in range(50)])
    assert conn.executemany_calls == 1


# ---------------------------------------------------------------------
# The ONE range read (spec O-5, folded with P4's `bars_between` 2026-09-19)
# ---------------------------------------------------------------------


#: One row as the folded SELECT returns it: ticker, interval, ts, OHLCV.
_RANGE_ROW = (
    "TESTARCH", "i5", ts(50), Decimal("99.0000"), Decimal("101.0000"),
    Decimal("98.5000"), Decimal("100.0000"), 1234,
)
_RANGE_VALUES = BarValues(
    Decimal("99.0000"), Decimal("101.0000"), Decimal("98.5000"), Decimal("100.0000"), 1234
)


def test_the_range_read_uses_the_connection_it_is_given(no_connections):
    """The archiver's half of the fold: the caller's transaction, never
    one of the store's own, and never committed or closed here."""
    conn = _FakeConn(rows=[_RANGE_ROW])
    held = store().bars_in_range(conn, "TESTARCH", Interval.I5, ts(40), ts(59))
    assert held == {ts(50): _RANGE_VALUES}
    assert (conn.commits, conn.closes) == (0, 0)
    assert "SELECT" in conn.sql and "FROM bars" in conn.sql
    assert "ts >=" in conn.sql and "ts <=" in conn.sql


def test_the_range_read_renders_bars_on_a_half_open_window_for_replay(no_connections):
    """P4's half of the fold, on the SAME method: `[start, end)` and
    `list[Bar]`, exactly what `bars_between` returned to replay."""
    conn = _FakeConn(rows=[_RANGE_ROW])
    bars = store().bars_in_range(
        conn, "TESTARCH", Interval.I5, ts(40), ts(59),
        end_inclusive=False, as_bars=True,
    )
    assert [(b.ticker, b.interval, b.ts, b.close, b.volume) for b in bars] == [
        ("TESTARCH", Interval.I5, ts(50), Decimal("100.0000"), 1234)
    ]
    assert "ts <" in conn.sql and "ts <=" not in conn.sql
    assert (conn.commits, conn.closes) == (0, 0)


def test_the_range_read_is_parameterised_never_interpolated(no_connections):
    conn = _FakeConn()
    store().bars_in_range(conn, "TESTARCH", Interval.I5, ts(40), ts(59))
    (query, params) = conn.queries[0]
    assert "TESTARCH" not in query
    assert params == ("TESTARCH", "i5", ts(40), ts(59))


def test_there_is_exactly_one_range_read_on_the_store():
    """L3 / spec O-5. `sprint-2/p4` shipped `bars_between()` with its own
    connection on 2026-09-19; this branch's `_bars_in_range` took the
    caller's. The fold owed at integration is DONE — `bars_in_range` is
    the one survivor, it still takes the connection first, and `None`
    there is what now opens one of its own."""
    reads = [
        name for name in dir(BarStore)
        if ("range" in name or "between" in name) and callable(getattr(BarStore, name))
    ]
    assert reads == ["bars_in_range"]
    assert list(inspect.signature(BarStore.bars_in_range).parameters)[:2] == ["self", "conn"]


# ---------------------------------------------------------------------
# Progress — GREATEST, and only on an accepted outcome (§4)
# ---------------------------------------------------------------------


def _accepted_plan():
    fetch = datetime(2026, 9, 18, 20, 30, tzinfo=UTC)
    plan = plan_candidates(
        ticker="TESTARCH", interval=Interval.I5,
        bars=[bar(ts(50)), bar(ts(55))], fetch_started_at=fetch,
        archived_through=ts(50),
    )
    return reconcile(plan, {ts(50): BarValues(
        Decimal("99.0000"), Decimal("101.0000"), Decimal("98.5000"), Decimal("100.0000"), 1234
    )})


def test_progress_is_written_with_greatest_and_takes_the_connection(no_connections):
    conn = _FakeConn()
    progress_mod.upsert_progress(
        conn, plan=_accepted_plan(), run_id="probe@2026-09-18T20:30:00Z",
        now=datetime(2026, 9, 18, 20, 31, tzinfo=UTC),
    )
    assert "GREATEST" in conn.sql
    assert "archive_progress" in conn.sql
    assert "ON CONFLICT (ticker, interval) DO UPDATE" in conn.sql
    assert (conn.commits, conn.rollbacks, conn.closes) == (0, 0, 0)


def test_progress_refuses_to_write_for_a_target_that_was_not_accepted(no_connections):
    """§4: progress never moves on a failed, withheld, empty or regressed
    target. The writer REFUSES rather than trusting its caller."""
    fetch = datetime(2026, 9, 18, 20, 30, tzinfo=UTC)
    refused = reconcile(
        plan_candidates(ticker="TESTARCH", interval=Interval.I5, bars=[],
                        fetch_started_at=fetch, archived_through=ts(50)),
        {},
    )
    conn = _FakeConn()
    with pytest.raises(RuntimeError) as e:
        progress_mod.upsert_progress(conn, plan=refused, run_id="probe", now=fetch)
    assert "not accepted" in str(e.value)
    assert conn.queries == []


def test_progress_sends_the_bar_timestamp_never_a_clock_time(no_connections):
    conn = _FakeConn()
    plan = _accepted_plan()
    now = datetime(2026, 9, 18, 20, 31, tzinfo=UTC)
    progress_mod.upsert_progress(conn, plan=plan, run_id="probe", now=now)
    (_, params) = conn.queries[0]
    assert params["archived_through"] == plan.archived_through_after == ts(55)
    assert params["archived_through"] != now
    assert params["updated_at"] == now


def test_reading_progress_takes_the_connection_and_returns_the_bar_timestamp(no_connections):
    conn = _FakeConn(rows=[(ts(50),)])
    assert progress_mod.read_archived_through(conn, "TESTARCH", Interval.I5) == ts(50)
    assert (conn.commits, conn.closes) == (0, 0)


def test_a_missing_progress_row_reads_as_none_which_is_a_bootstrap(no_connections):
    assert progress_mod.read_archived_through(_FakeConn(rows=[]), "TESTARCH", Interval.I5) is None


def test_progress_rows_are_never_deleted_by_this_module():
    """§4: a progress row is NEVER deleted, not even when a ticker leaves
    the trader's Lists note — that is what makes the dropped-and-re-added
    sequence open a `gap` rather than skipping the missing days."""
    assert "DELETE" not in code_of(progress_mod).upper()


# ---------------------------------------------------------------------
# Incidents — open or refresh, on the connection (§11)
# ---------------------------------------------------------------------


def _draft(kind=IncidentKind.GAP):
    return IncidentDraft(
        kind=kind, ticker="TESTARCH", interval="i5",
        range_start=ts(40), range_end=ts(50), detail={"wording": "probe"},
    )


def test_an_incident_is_opened_or_refreshed_never_duplicated(no_connections):
    conn = _FakeConn(rows=[(7,)])
    now = datetime(2026, 9, 18, 20, 31, tzinfo=UTC)
    assert incidents_mod.open_or_refresh(conn, _draft(), run_id="probe", now=now) == 7
    assert "archive_incidents" in conn.sql
    assert "ON CONFLICT (kind, ticker, interval, range_start) WHERE resolved_at IS NULL" in conn.sql
    assert "DO UPDATE SET" in conn.sql and "last_seen_at" in conn.sql
    assert (conn.commits, conn.rollbacks, conn.closes) == (0, 0, 0)


def test_a_refresh_moves_last_seen_at_and_never_first_seen_at(no_connections):
    conn = _FakeConn(rows=[(7,)])
    incidents_mod.open_or_refresh(
        conn, _draft(), run_id="probe", now=datetime(2026, 9, 18, 20, 31, tzinfo=UTC)
    )
    update = conn.sql.split("DO UPDATE SET", 1)[1]
    assert "last_seen_at" in update
    assert "first_seen_at" not in update


@pytest.mark.parametrize("kind", list(IncidentKind))
def test_every_kind_the_pure_core_can_raise_is_writable(kind, no_connections):
    conn = _FakeConn(rows=[(1,)])
    assert incidents_mod.open_or_refresh(
        conn, _draft(kind), run_id="probe",
        now=datetime(2026, 9, 18, 20, 31, tzinfo=UTC),
    ) == 1


def test_listing_unresolved_incidents_writes_nothing(no_connections):
    conn = _FakeConn(rows=[])
    incidents_mod.unresolved(conn)
    assert "resolved_at IS NULL" in conn.sql
    for word in ("INSERT", "UPDATE", "DELETE"):
        assert word not in conn.sql.upper()


def test_resolving_an_incident_is_explicit_and_audited(no_connections):
    conn = _FakeConn(rows=[(7,)])
    incidents_mod.resolve(
        conn, 7, by="operator", note="repaired by restate --apply",
        now=datetime(2026, 9, 18, 20, 31, tzinfo=UTC),
    )
    assert "resolved_at" in conn.sql and "resolved_by" in conn.sql
    (_, params) = conn.queries[0]
    assert params["resolved_by"] == "operator"
    assert params["note"].obj["resolution_note"] == "repaired by restate --apply"


def test_resolve_refuses_an_empty_who(no_connections):
    with pytest.raises(ValueError):
        incidents_mod.resolve(
            _FakeConn(), 7, by="", note="x",
            now=datetime(2026, 9, 18, 20, 31, tzinfo=UTC),
        )


# ---------------------------------------------------------------------
# The run-level advisory lock (§9)
# ---------------------------------------------------------------------


def test_the_lock_key_is_one_constant():
    assert isinstance(ARCHIVE_RUN_LOCK_KEY, int)
    source = code_of(try_acquire_run_lock)
    assert "ARCHIVE_RUN_LOCK_KEY" in source
    assert "pg_try_advisory_lock" in source


def test_the_lock_is_session_level_not_transaction_level():
    """§9 says session-level: a repair's pre-commit re-check rolls its
    transaction back, and a transaction-level lock would be released by
    that rollback while the command is still running."""
    assert "pg_try_advisory_xact_lock" not in code_of(try_acquire_run_lock)


def test_acquiring_the_lock_asks_the_server_once(no_connections):
    conn = _FakeConn(rows=[(True,)])
    assert try_acquire_run_lock(conn) is True
    assert len(conn.queries) == 1
    (_, params) = conn.queries[0]
    assert params == (ARCHIVE_RUN_LOCK_KEY,)


def test_a_second_holder_is_refused_loudly(no_connections):
    conn = _FakeConn(rows=[(False,)])
    assert try_acquire_run_lock(conn) is False
    with pytest.raises(ArchiveLockError) as e:
        try_acquire_run_lock(conn, what="the nightly run")
    assert "another archive/repair run holds the lock" in str(e.value)
    assert "the nightly run" in str(e.value)


def test_releasing_the_lock_takes_the_connection(no_connections):
    conn = _FakeConn(rows=[(True,)])
    release_run_lock(conn)
    assert "pg_advisory_unlock" in conn.sql
    assert (conn.commits, conn.closes) == (0, 0)


# ---------------------------------------------------------------------
# requires_db — WRITTEN HERE, first run owed on cobalt_dev
# ---------------------------------------------------------------------


@requires_db
def test_the_append_path_never_modifies_an_existing_row():
    st = BarStore()
    st.ensure_schema()
    key = datetime(2026, 8, 29, 9, 30, tzinfo=UTC)
    assert st.upsert_bars([bar(key, close="100.00")]) == 1
    with st.target_transaction() as conn:
        inserted = st.insert_new_bars(conn, [bar(key, close="999.00")])
    assert inserted == 0, "DO NOTHING must not count a conflict as an insert"
    with st._connect() as conn:
        row = conn.execute(
            "SELECT close FROM bars WHERE ticker=%s AND interval=%s AND ts=%s",
            ("TESTARCH", "i5", key),
        ).fetchone()
    assert str(row[0]) == "100.0000", "the append path rewrote a stored bar"


@requires_db
def test_a_poller_style_insert_between_the_read_and_the_insert_is_a_counted_conflict():
    """§9 / the concurrency test: the poller landing a bar in the window
    between the range read and this insert is a COUNTED CONFLICT, never
    an error, and the counting identity still closes."""
    st = BarStore()
    st.ensure_schema()
    keys = [datetime(2026, 8, 29, 10, m, tzinfo=UTC) for m in (0, 5)]
    with st.target_transaction() as conn:
        held = st.bars_in_range(conn, "TESTARCH", Interval.I5, keys[0], keys[-1])
        assert keys[0] not in held
        # ...the poller commits on its own connection, in between.
        st.upsert_bars([bar(keys[0])])
        inserted = st.insert_new_bars(conn, [bar(k) for k in keys])
    assert inserted == 1
    conflicts = 2 - inserted
    assert conflicts == 1


@requires_db
def test_a_crash_after_the_inserts_leaves_neither_bars_nor_progress():
    st = BarStore()
    st.ensure_schema()
    key = datetime(2026, 8, 29, 11, 0, tzinfo=UTC)
    boom = RuntimeError("crash after the inserts, before progress")
    with pytest.raises(RuntimeError):
        with st.target_transaction() as conn:
            st.insert_new_bars(conn, [bar(key)])
            raise boom
    with st._connect() as conn:
        assert conn.execute(
            "SELECT count(*) FROM bars WHERE ticker=%s AND interval=%s AND ts=%s",
            ("TESTARCH", "i5", key),
        ).fetchone()[0] == 0
        assert conn.execute(
            "SELECT count(*) FROM archive_progress WHERE ticker=%s AND interval=%s",
            ("TESTARCH", "i5"),
        ).fetchone()[0] == 0


@requires_db
def test_the_retry_after_a_crash_is_idempotent():
    st = BarStore()
    st.ensure_schema()
    key = datetime(2026, 8, 29, 11, 30, tzinfo=UTC)
    for expected in (1, 0):
        with st.target_transaction() as conn:
            assert st.insert_new_bars(conn, [bar(key)]) == expected


@requires_db
def test_a_second_holder_of_the_advisory_lock_refuses(real_connect):
    """§9's lock is SESSION level, so this test needs TWO SESSIONS.

    FIRST RUN ON `cobalt_dev`, 2026-09-19 (archiver DB run): written with
    `BarStore._connect()` twice, which goes through `db.connect` — and
    `conftest.dev_db_tx` (autouse) hands every caller a
    `_SavepointConnection` over ONE shared session. `pg_try_advisory_lock`
    is re-entrant within a session, so the second acquire returned True
    and the test read `assert True is False`. The property was never
    wrong; the test could not observe it. `real_connect` is the fixture
    conftest documents for exactly this ("a savepoint proxy over one
    shared connection cannot show …, because both proxies are the same
    session"). It writes no rows, so RULING 7 is untouched.
    """
    first = real_connect(side=Side.SYSTEM)
    second = real_connect(side=Side.SYSTEM)
    assert try_acquire_run_lock(first) is True
    assert try_acquire_run_lock(second) is False
    with pytest.raises(ArchiveLockError):
        try_acquire_run_lock(second, what="a second nightly run")
    release_run_lock(first)
    assert try_acquire_run_lock(second) is True
    release_run_lock(second)


@requires_db
def test_progress_and_an_incident_commit_with_the_bars_or_not_at_all():
    st = BarStore()
    st.ensure_schema()
    plan = _accepted_plan()
    now = datetime(2026, 8, 29, 12, 0, tzinfo=UTC)
    with pytest.raises(RuntimeError):
        with st.target_transaction() as conn:
            st.insert_new_bars(conn, list(plan.to_insert))
            progress_mod.upsert_progress(conn, plan=plan, run_id="probe", now=now)
            incidents_mod.open_or_refresh(conn, _draft(), run_id="probe", now=now)
            raise RuntimeError("crash before commit")
    with st._connect() as conn:
        assert conn.execute(
            "SELECT count(*) FROM archive_progress WHERE ticker=%s", ("TESTARCH",)
        ).fetchone()[0] == 0
        assert conn.execute(
            "SELECT count(*) FROM archive_incidents WHERE ticker=%s", ("TESTARCH",)
        ).fetchone()[0] == 0


@requires_db
def test_progress_is_monotonic_across_accepted_runs():
    st = BarStore()
    st.ensure_schema()
    plan = _accepted_plan()
    now = datetime(2026, 8, 29, 12, 30, tzinfo=UTC)
    with st.target_transaction() as conn:
        progress_mod.upsert_progress(conn, plan=plan, run_id="probe-1", now=now)
    older = plan.model_copy(update={"archived_through_after": ts(50)})
    with st.target_transaction() as conn:
        progress_mod.upsert_progress(conn, plan=older, run_id="probe-2", now=now)
    with st._connect() as conn:
        row = conn.execute(
            "SELECT archived_through FROM archive_progress WHERE ticker=%s AND interval=%s",
            ("TESTARCH", "i5"),
        ).fetchone()
    assert row[0] == ts(55), "GREATEST must refuse to move the watermark backwards"


@requires_db
def test_a_recurring_incident_refreshes_rather_than_duplicating():
    st = BarStore()
    st.ensure_schema()
    now = datetime(2026, 8, 29, 13, 0, tzinfo=UTC)
    with st.target_transaction() as conn:
        first = incidents_mod.open_or_refresh(conn, _draft(), run_id="probe-1", now=now)
        again = incidents_mod.open_or_refresh(
            conn, _draft(), run_id="probe-2", now=now + timedelta(days=1)
        )
        assert first == again
        row = conn.execute(
            "SELECT first_seen_at, last_seen_at FROM archive_incidents WHERE id = %s",
            (first,),
        ).fetchone()
        assert row[0] == now and row[1] == now + timedelta(days=1)


# ---------------------------------------------------------------------
# Tribunal round 1, F1 — the repair's bar write on the repair's own
# transaction. Offline twins live in `test_archiver_quiet.py`; these two
# are the real-transaction proof and their FIRST RUN IS OWED on
# `cobalt_dev`, like every other `requires_db` test on this branch.
# ---------------------------------------------------------------------


@requires_db
def test_a_rollback_unwrites_an_upsert_made_on_the_targets_connection():
    """`upsert_bars_on` is the shape `restate --apply` now uses: the
    `DO UPDATE` lands on the caller's connection, so the caller's
    rollback — the one §8's pre-commit re-check raises — undoes it.

    The offline test can only assert which METHOD was called; that a
    real Postgres rollback actually removes the rewritten value is what
    this one proves.
    """
    st = BarStore()
    st.ensure_schema()
    key = datetime(2026, 8, 29, 14, 0, tzinfo=UTC)
    assert st.upsert_bars([bar(key, close="100.00")]) == 1

    boom = RuntimeError("the pre-commit re-check refused")
    with pytest.raises(RuntimeError):
        with st.target_transaction() as conn:
            assert st.upsert_bars_on(conn, [bar(key, close="999.00")]) == 1
            raise boom

    with st._connect() as conn:
        row = conn.execute(
            "SELECT close FROM bars WHERE ticker=%s AND interval=%s AND ts=%s",
            ("TESTARCH", "i5", key),
        ).fetchone()
    assert str(row[0]) == "100.0000", (
        "a rolled-back repair left the rewritten value in place — F1 again"
    )


# Dropped 2026-09-19 (cto-2026-09-19.md R26): unobservable under
# conftest.py:133's autouse single-transaction fixture. Offline pins stay: tests/cobalt/test_archiver_append_store.py::test_upsert_bars_still_does_update_and_never_do_nothing, tests/cobalt/test_archiver_append_store.py::test_only_one_copy_of_the_upsert_statement_exists, tests/cobalt/test_archiver_append_store.py::test_upsert_bars_on_takes_the_callers_connection_and_never_opens_one.


@requires_db
def test_backfill_missings_insert_rolls_back_with_its_transaction():
    """F1's sibling, on the real database: `insert_new_bars` already
    writes on the caller's connection, so `backfill-missing` never had
    the defect. Asserted rather than assumed."""
    st = BarStore()
    st.ensure_schema()
    key = datetime(2026, 8, 29, 15, 0, tzinfo=UTC)

    with pytest.raises(RuntimeError):
        with st.target_transaction() as conn:
            assert st.insert_new_bars(conn, [bar(key)]) == 1
            raise RuntimeError("the pre-commit re-check refused")

    with st._connect() as conn:
        assert conn.execute(
            "SELECT count(*) FROM bars WHERE ticker=%s AND interval=%s AND ts=%s",
            ("TESTARCH", "i5", key),
        ).fetchone()[0] == 0


# ---------------------------------------------------------------------
# Spec §15's named races (tribunal round 1, F3 = the desk's Q10)
#
# The SEQUENCED forms are offline in `test_archiver_quiet.py`. These
# two need two REAL connections: which value survives when a poller
# commit and a repair commit contend for one row is decided by
# Postgres, not by a fake (L45). First run OWED on cobalt_dev.
# ---------------------------------------------------------------------


@requires_db
def test_a_committed_poller_write_is_overwritten_by_a_later_repair():
    """DIFFERING-VALUE RACE, same key: the poller commits X on its own
    connection inside the repair's transaction window, and the repair's
    `DO UPDATE` commits after it. Y survives.

    The offline twin asserts which method ran; this one asserts what the
    database actually holds after two real commits.
    """
    st = BarStore()
    st.ensure_schema()
    key = datetime(2026, 8, 29, 16, 0, tzinfo=UTC)
    assert st.upsert_bars([bar(key, close="100.00")]) == 1

    with st.target_transaction() as conn:
        held = st.bars_in_range(conn, "TESTARCH", Interval.I5, key, key)
        assert str(held[key].close) == "100.0000"
        # ...the poller, on its OWN connection, between the read and the
        # write. It commits the instant it returns.
        st.upsert_bars([bar(key, close="103.00")])
        assert st.upsert_bars_on(conn, [bar(key, close="105.00")]) == 1

    with st._connect() as conn:
        row = conn.execute(
            "SELECT close FROM bars WHERE ticker=%s AND interval=%s AND ts=%s",
            ("TESTARCH", "i5", key),
        ).fetchone()
    assert str(row[0]) == "105.0000", (
        "the repair committed last; its restated value must be the stored one"
    )


@requires_db
def test_an_equal_value_race_writes_the_same_value_and_changes_nothing():
    """EQUAL-VALUE RACE, same key: the poller writes X and the repair
    independently computes X.

    Two things are asserted, because only one of them is obvious: the
    stored value is unchanged, AND the repair offers nothing at all —
    `compare` finds no differing key, so `_apply_restate`'s row list is
    empty and `upsert_bars_on` returns 0 without sending a statement.
    """
    st = BarStore()
    st.ensure_schema()
    key = datetime(2026, 8, 29, 16, 30, tzinfo=UTC)
    assert st.upsert_bars([bar(key, close="105.00")]) == 1

    with st.target_transaction() as conn:
        held = st.bars_in_range(conn, "TESTARCH", Interval.I5, key, key)
        comparison = compare([bar(key, close="105.00")], held)
        assert comparison.differing == ()
        assert comparison.equal == (key,)
        rows = [b for b in [bar(key, close="105.00")] if b.ts in {
            d.ts for d in comparison.differing
        }]
        assert st.upsert_bars_on(conn, rows) == 0

    with st._connect() as conn:
        row = conn.execute(
            "SELECT close FROM bars WHERE ticker=%s AND interval=%s AND ts=%s",
            ("TESTARCH", "i5", key),
        ).fetchone()
    assert str(row[0]) == "105.0000"
