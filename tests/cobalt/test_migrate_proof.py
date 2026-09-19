"""The migration harness's CONTENT PROOF, and the read-only `--proof-only` mode.

Why this file exists: on 2026-09-18 the stacked production deploy died in
`cobalt db migrate`'s BEFORE probe with

    ProgramLimitExceeded: out of memory
    DETAIL:  Cannot enlarge string buffer containing 1073741677 bytes by 155 more bytes.

The proof digest was `md5(string_agg(<row>::text, '|' ORDER BY <pk>))`,
built SERVER-SIDE as one value. Production's `system.bars` holds
8,410,174 rows, so that single value passes Postgres's 1 GB varlena
ceiling before the first `-- applying` line. `cobalt_dev` was green on
the same command, so no gate could see it — which is why the property
being asserted here is not "the digest is right" but "the digest is
computed WITHOUT ever materialising the concatenation", and separately
that its VALUE is byte-for-byte the one the old SQL produced, so proof
tables printed before today stay comparable.

Twelve groups (1-9 written 2026-09-18; 10-11 by the ops round-1 build and
12 by the ops DB run, both 2026-09-19):

1. THE FOLD (no database) — the client-side md5 over an iterator of row
   texts equals `md5('|'.join(rows))` exactly: zero rows, one row, many
   rows, rows containing the separator itself, non-ASCII, very long.
2. BYTE COMPATIBILITY (database) — for every table in the proof, the
   streamed digest equals what the OLD SQL expression returns for that
   table in the same transaction. The old expression survives HERE and
   nowhere else: it is the oracle, not a code path.
3. NO CONCATENATION (database) — nothing the probe sends to the server
   contains `string_agg`, asserted on the queries as constructed rather
   than by grepping the source, and the rows arrive through a NAMED
   (server-side) cursor in batches.
4. `--proof-only` — prints the proof with timings, applies nothing, exits
   0, refuses `--rollback`/`--down-to`, and runs in a transaction the
   server itself will not let anything write to.
5. MEMORY SHAPE (no database) — the cursor's construction, since a 1 GB
   table cannot be built in a test.
6. ONE STATEMENT, ONE PASS (no database) — review finding F1: the row
   count comes out of the fold, so a table being written to cannot yield
   a `rows` that belongs to one snapshot and a `digest` that belongs to
   another. Asserted against a fake table that grows under the probe.
7. THE CHEAP UNTESTED CASES the review listed — `--proof-only` combined
   with `--rollback` is refused before a connection is ever opened, and a
   probe that raises leaves the connection rolled back and closed.
8. SNAPSHOT CONSISTENCY (database, with a SECOND connection playing the
   other session) — group 6 fixed the two snapshots INSIDE one probe;
   this group fixes the two snapshots BETWEEN the BEFORE and the AFTER
   probe, which on production are ≈100 s apart. The harness transaction
   is REPEATABLE READ, so a commit by any other session inside that
   window is invisible to both probes and cannot make a good migration
   read `CHANGED` and roll back; the transaction's OWN writes are still
   seen, because "did THIS migration change existing content?" is the
   question the proof exists to answer.
9. THE TRIBUNAL'S ROUND 1 (2026-09-19) — an ambiguous table name is
   refused instead of resolved to whichever row came first (R1), and the
   case no house could settle from reads: DDL under REPEATABLE READ after
   ANOTHER session committed to the same table (U1).
10. `lock_timeout` ON THE MIGRATE TRANSACTION — the ceiling is set before
   the migrations run, forward and rollback alike, and `--proof-only`
   never gets one.
11. THE OUTPUT NAMES THE CODE IT RAN FROM — the `code:` line.
12. THE TRIBUNAL'S CARRIED ITEMS (R1/R11) — the one question rounds 1
   and 2 could not answer offline, settled against `cobalt_dev`: WHICH
   statement takes the REPEATABLE READ snapshot, and therefore whether
   the lock ceiling can cover the BEFORE probe. It can, and now does.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Optional

import psycopg
import pytest
from psycopg import sql

from cobalt import db, env
from cobalt.db_migrations import FORWARD, cli
from cobalt.db_migrations.placement import (
    CREATED_TABLES,
    MOVED_TABLES,
    SEEDED_TABLES,
)

REPO_ROOT = Path(__file__).resolve().parents[2]

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

#: Every table the proof covers, in the order the harness probes them.
PROOF_TABLES = sorted({**MOVED_TABLES, **SEEDED_TABLES, **CREATED_TABLES})


# ---------------------------------------------------------------------
# 1. THE FOLD
# ---------------------------------------------------------------------

#: Each case is a list of row texts. `string_agg(x, '|')` is exactly
#: `'|'.join(x)`, so that is the oracle — including the awkward ones.
FOLD_CASES = {
    "zero_rows": [],
    "one_row": ['{"id": 1, "ticker": "AAPL"}'],
    "many_rows": [f'{{"id": {i}}}' for i in range(25_000)],
    "rows_containing_the_separator": ["a|b", "|", "||", "c|", "|d"],
    "empty_strings": ["", "", "x", ""],
    "non_ascii": ["naïve", "ünïcødé — ✓", "日本語のテキスト", "Ω≈ç√∫"],
    "very_long": ["x" * 500_000, "y" * 250_000, "z"],
}


@pytest.mark.parametrize("case", sorted(FOLD_CASES))
def test_the_streamed_fold_reproduces_string_agg_byte_for_byte(case):
    rows = FOLD_CASES[case]
    expected = hashlib.md5("|".join(rows).encode("utf-8")).hexdigest()
    # An ITERATOR, not a list: the fold must never need the rows twice
    # and must never hold them all.
    assert cli._digest_rows(iter(rows))[1] == expected, (
        f"{case}: the streamed fold does not produce the bytes "
        "string_agg(..., '|') would have produced"
    )


@pytest.mark.parametrize("case", sorted(FOLD_CASES))
def test_the_fold_reports_how_many_rows_it_folded(case):
    """The COUNT comes out of the fold, not out of a second statement.

    That is the whole of review finding F1: a `SELECT count(*)` and the
    digest are two READ COMMITTED statements, so on a table being written
    to they can describe different snapshots and the printed line is
    self-contradictory. One statement, one pass, one pair.
    """
    rows = FOLD_CASES[case]
    counted, digest = cli._digest_rows(iter(rows))
    assert counted == len(rows), (
        f"{case}: the fold folded {len(rows)} row(s) and reported {counted}"
    )
    assert digest == hashlib.md5("|".join(rows).encode("utf-8")).hexdigest()


def test_no_rows_digests_the_empty_string():
    """The `coalesce(string_agg(...), '')` arm, which every empty table hits."""
    assert cli._digest_rows(iter([])) == (0, hashlib.md5(b"").hexdigest())
    assert cli._digest_rows(iter([])) == (0, "d41d8cd98f00b204e9800998ecf8427e")


def test_the_separator_goes_between_rows_and_never_after_the_last():
    """One row must digest the row alone — no trailing `|`."""
    assert cli._digest_rows(iter(["solo"])) == (1, hashlib.md5(b"solo").hexdigest())
    assert cli._digest_rows(iter(["a", "b"])) == (2, hashlib.md5(b"a|b").hexdigest())
    assert cli._digest_rows(iter(["a", "b"]))[1] != hashlib.md5(b"a|b|").hexdigest()


# ---------------------------------------------------------------------
# 2. BYTE COMPATIBILITY — the OLD SQL as the oracle
# ---------------------------------------------------------------------


def _old_sql_digest(conn, schema: str, table: str) -> str:
    """The digest EXACTLY as `cli._probe` computed it before 2026-09-18.

    This is the only place that expression still exists (L3: it is
    deleted from the module, not kept behind a switch). It runs here as
    an ORACLE — `cobalt_dev` is small enough for the 1 GB ceiling to be
    out of reach, which is precisely why the defect could only ever be
    caught by comparing values, never by running this.
    """
    pk = cli._pk_columns(conn, schema, table)
    query = sql.SQL(
        "SELECT md5(coalesce(string_agg(({row_json})::text, '|' ORDER BY {order}), '')) "
        "FROM {rel} AS t"
    ).format(
        row_json=cli._row_json(table),
        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
        rel=sql.Identifier(schema, table),
    )
    return conn.execute(query).fetchone()[0]


@requires_db
def test_every_proof_table_digests_to_the_value_the_old_sql_returns():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    checked, empty = [], []
    try:
        for table in PROOF_TABLES:
            schema = cli._schema_of(conn, table)
            if schema is None:
                continue
            probe = cli._probe(conn, table)
            assert probe["digest"] == _old_sql_digest(conn, schema, table), (
                f"{schema}.{table}: the streamed digest is NOT the value the old "
                "SQL produced — proof tables printed before today are no longer "
                "comparable, which is the one thing this rewrite promised"
            )
            assert isinstance(probe["seconds"], float) and probe["seconds"] >= 0.0, (
                f"{table}: the probe must report its own wall time — the proof "
                "runs twice inside a resident outage"
            )
            (empty if probe["rows"] == 0 else checked).append(table)
    finally:
        conn.rollback()
        conn.close()

    assert len(checked) >= 8, (
        "too few POPULATED tables were compared for this to prove anything: "
        f"{checked} (empty: {empty})"
    )
    assert "bars" in checked, (
        "`bars` is the table that broke production and `cobalt_dev` holds a "
        "million rows of it — if it is not in the comparison, the streamed "
        "fold has only ever been proven on toy data"
    )


# ---------------------------------------------------------------------
# 3. NO CONCATENATION — asserted on the queries as constructed
# ---------------------------------------------------------------------


def _rendered(query, context) -> str:
    return query.as_string(context) if hasattr(query, "as_string") else str(query)


class _RecordingCursor:
    """Delegates to a real cursor, recording what it is asked to run."""

    def __init__(self, cursor, recorder):
        self.__dict__["_cursor"] = cursor
        self.__dict__["_recorder"] = recorder

    def __getattr__(self, name):
        return getattr(self.__dict__["_cursor"], name)

    def __setattr__(self, name, value):
        setattr(self.__dict__["_cursor"], name, value)

    def execute(self, query, *args, **kwargs):
        rec = self.__dict__["_recorder"]
        rec.queries.append(_rendered(query, rec.conn))
        rec.itersizes.append(getattr(self.__dict__["_cursor"], "itersize", None))
        return self.__dict__["_cursor"].execute(query, *args, **kwargs)

    def __iter__(self):
        return iter(self.__dict__["_cursor"])

    def __enter__(self):
        self.__dict__["_cursor"].__enter__()
        return self

    def __exit__(self, *exc):
        return self.__dict__["_cursor"].__exit__(*exc)


class _RecordingConn:
    """A real connection that also remembers every statement it carried."""

    def __init__(self, conn):
        self.conn = conn
        self.queries: list[str] = []
        self.cursor_names: list[str] = []
        self.itersizes: list[int | None] = []

    def execute(self, query, *args, **kwargs):
        self.queries.append(_rendered(query, self.conn))
        return self.conn.execute(query, *args, **kwargs)

    def cursor(self, *args, **kwargs):
        name = kwargs.get("name") or (args[0] if args else None)
        if name:
            self.cursor_names.append(name)
        return _RecordingCursor(self.conn.cursor(*args, **kwargs), self)

    def __getattr__(self, name):
        return getattr(self.conn, name)


@requires_db
def test_no_statement_the_probe_sends_contains_string_agg():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    recorder = _RecordingConn(conn)
    try:
        probe = cli._probe_all(recorder)
    finally:
        conn.rollback()
        conn.close()

    assert probe and recorder.queries
    offenders = [q for q in recorder.queries if "string_agg" in q.lower()]
    assert not offenders, (
        "the proof still concatenates rows server-side — that value is what "
        f"passed the 1 GB ceiling on 8.4M rows: {offenders[:2]}"
    )


@requires_db
def test_rows_reach_the_probe_through_a_named_cursor_in_batches():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    recorder = _RecordingConn(conn)
    try:
        cli._probe_all(recorder)
    finally:
        conn.rollback()
        conn.close()

    assert len(recorder.cursor_names) == len(PROOF_TABLES), (
        "every table's rows must stream through its own NAMED (server-side) "
        f"cursor; named cursors declared: {recorder.cursor_names}"
    )
    assert set(recorder.itersizes) == {cli.PROBE_BATCH_SIZE}, (
        "an unbatched cursor fetches the whole table into the client — "
        f"itersizes seen: {sorted(set(recorder.itersizes), key=str)}"
    )


# ---------------------------------------------------------------------
# 4. `--proof-only`
# ---------------------------------------------------------------------


def _migrate(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "cobalt.cli", "db", "migrate", *args],
        cwd=REPO_ROOT,
        env={**os.environ, env.ENV_VAR: env.DEV},
        capture_output=True,
        text=True,
        timeout=600,
        check=False,
    )


def _relations() -> set[tuple[str, str]]:
    """Every table and view on the three schemas, read outside the harness."""
    conn = db.connect_migration(env.DEV_DB_NAME)
    try:
        rows = conn.execute(
            """
            SELECT schemaname, tablename FROM pg_tables
             WHERE schemaname IN ('public', 'user', 'system')
            UNION ALL
            SELECT schemaname, viewname FROM pg_views
             WHERE schemaname IN ('public', 'user', 'system')
            """
        ).fetchall()
    finally:
        conn.close()
    return {(s, t) for s, t in rows}


@requires_db
class TestProofOnly:
    """The mode that would have caught 2026-09-18 with the residents still up."""

    def test_it_prints_every_table_with_timings_and_applies_nothing(self):
        before = _relations()
        proc = _migrate("--proof-only")
        after = _relations()

        assert proc.returncode == 0, proc.stdout + proc.stderr
        assert "-- applying" not in proc.stdout, (
            "--proof-only ran a migration file:\n" + proc.stdout
        )
        for table in PROOF_TABLES:
            assert table in proc.stdout, f"{table} is missing from the proof"
        assert "secs" in proc.stdout, "no per-table wall-time column"
        assert "total" in proc.stdout.lower(), "no total wall time"
        assert after == before, (
            "--proof-only changed the schema: "
            f"added {sorted(after - before)}, removed {sorted(before - after)}"
        )

    def test_it_refuses_rollback_and_down_to(self):
        for args in (
            ("--proof-only", "--rollback", "--down-to", "0005"),
            ("--proof-only", "--rollback"),
            ("--proof-only", "--down-to", "0005"),
        ):
            proc = _migrate(*args)
            assert proc.returncode != 0, f"{args} was accepted:\n{proc.stdout}"
            message = proc.stdout + proc.stderr
            assert "unrecognized" not in message, (
                f"{args} was refused by argparse as an UNKNOWN flag, which is not "
                f"the same thing as refusing the combination:\n{message}"
            )
            assert "--proof-only" in message and "--rollback" in message, (
                f"{args} failed without naming the conflict:\n{message}"
            )
            assert "-- applying" not in proc.stdout, (
                f"{args} applied a migration before refusing:\n{proc.stdout}"
            )

    def test_its_transaction_is_read_only_at_the_server(self):
        """Not 'the code does not write' — the SERVER refuses the write."""
        conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=True)
        try:
            with pytest.raises(psycopg.errors.ReadOnlySqlTransaction):
                conn.execute(
                    "CREATE TABLE system.proof_only_must_never_create_this (id int)"
                )
        finally:
            conn.rollback()
            conn.close()

        assert ("system", "proof_only_must_never_create_this") not in _relations()


# ---------------------------------------------------------------------
# 5. MEMORY SHAPE — the cursor's construction
# ---------------------------------------------------------------------


class _FakeCursor:
    def __init__(self, name, rows):
        self.name = name
        self.itersize = 1  # psycopg's default; the code under test must set it
        self.executed = None
        self.closed = False
        self._rows = rows

    def execute(self, query, *args, **kwargs):
        self.executed = query

    def __iter__(self):
        return iter(self._rows)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.closed = True
        return False


class _FakeConn:
    def __init__(self, rows):
        self._rows = rows
        self.cursors: list[_FakeCursor] = []

    def cursor(self, *args, **kwargs):
        cursor = _FakeCursor(kwargs.get("name") or (args[0] if args else None), self._rows)
        self.cursors.append(cursor)
        return cursor


def test_row_texts_stream_through_one_named_batched_server_side_cursor():
    """A 1 GB table cannot be built here, so the SHAPE is what is asserted."""
    conn = _FakeConn([("first",), ("second",)])
    query = sql.SQL("SELECT 1")

    assert list(cli._stream_row_texts(conn, "bars", query)) == ["first", "second"]

    assert len(conn.cursors) == 1
    cursor = conn.cursors[0]
    assert cursor.name, (
        "an UNNAMED psycopg cursor buffers the entire result set in the client "
        "— the same ceiling, moved from the server to this process"
    )
    assert "bars" in cursor.name, "the cursor names the table it is reading"
    assert cursor.executed is query
    assert cursor.itersize == cli.PROBE_BATCH_SIZE
    assert cursor.closed, "the cursor is closed even though the caller iterates lazily"


def test_the_batch_size_is_bounded_and_not_one_row_at_a_time():
    assert cli.PROBE_BATCH_SIZE == 10_000


# ---------------------------------------------------------------------
# 6. ONE STATEMENT, ONE PASS — review finding F1
# ---------------------------------------------------------------------


class _FakeResult:
    def __init__(self, rows):
        self._rows = rows

    def fetchone(self):
        return self._rows[0] if self._rows else None

    def fetchall(self):
        return list(self._rows)


class _GrowingProbeConn:
    """A table under continuous insert: every statement sees one more row.

    Nothing exotic — that IS READ COMMITTED, which is what the harness's
    connection uses: each statement takes its own snapshot, so two
    statements inside one probe describe two different tables. Review
    finding F1 (Grok MAJOR, Gemini Q5) is exactly this, and the only way
    a probe can be immune to it is to send ONE statement.
    """

    def __init__(self, start_rows: int = 3):
        self._rows = [f'{{"id": {i}}}' for i in range(start_rows)]
        self.statements: list[str] = []
        self.cursors: list[_FakeCursor] = []
        self.streamed: list[list[str]] = []

    def _snapshot(self) -> list[str]:
        """A writer commits one more row before every statement runs."""
        self._rows.append(f'{{"id": {len(self._rows)}}}')
        return list(self._rows)

    def execute(self, query, *args, **kwargs):
        text = _rendered(query, None)
        self.statements.append(text)
        if "pg_tables" in text:
            return _FakeResult([("system",)])
        if "indisprimary" in text:
            return _FakeResult([("id",)])
        if "count(" in text.lower():
            return _FakeResult([(len(self._snapshot()),)])
        raise AssertionError(f"the probe sent an unexpected statement: {text}")

    def cursor(self, *args, **kwargs):
        snapshot = self._snapshot()
        self.streamed.append(snapshot)
        cursor = _FakeCursor(
            kwargs.get("name") or (args[0] if args else None),
            [(row_text,) for row_text in snapshot],
        )
        self.cursors.append(cursor)
        return cursor

    def every_statement(self) -> list[str]:
        return self.statements + [
            _rendered(c.executed, None) for c in self.cursors if c.executed is not None
        ]


def test_a_table_that_grows_under_the_probe_yields_a_self_consistent_pair():
    """`rows` and `digest` must describe the SAME snapshot, always."""
    conn = _GrowingProbeConn()
    first = cli._probe(conn, "bars")
    second = cli._probe(conn, "bars")

    for probe, streamed in zip((first, second), conn.streamed):
        assert probe["rows"] == len(streamed), (
            "the probe printed a row count that belongs to a different "
            f"snapshot than its digest: rows={probe['rows']}, digest folded "
            f"over {len(streamed)} row(s)"
        )
        assert probe["digest"] == hashlib.md5(
            "|".join(streamed).encode("utf-8")
        ).hexdigest(), (
            "the digest is not the digest of the rows the probe counted"
        )

    assert (first["rows"], first["digest"]) != (second["rows"], second["digest"]), (
        "the fake table did not grow between the two probes, so this test "
        "proved nothing"
    )


def test_the_probe_sends_no_separate_count_statement():
    """One pass over the table, not two — `bars` is read once."""
    conn = _GrowingProbeConn()
    cli._probe(conn, "bars")

    offenders = [s for s in conn.every_statement() if "count(" in s.lower()]
    assert not offenders, (
        "the content proof still counts the rows in a second statement: "
        f"{offenders}. The count comes out of the fold (review F1), which is "
        "also what stops `bars` being read twice."
    )


def test_the_documented_fold_counts_rows_and_buffers_a_batch():
    """The prose must not promise a row-at-a-time fold it does not do."""
    assert "one row at a time" not in (cli._digest_rows.__doc__ or ""), (
        "`_digest_rows`'s docstring still claims it holds exactly one row at "
        "a time; the server-side cursor buffers PROBE_BATCH_SIZE rows per fetch"
    )

    devdoc = (
        REPO_ROOT / "docs" / "40 - DevDocs" / "cobalt" / "db_migrations" / "cli.md"
    ).read_text()
    assert "one row text at a time" not in devdoc, (
        "the DevDoc still says the cursor yields one row text at a time"
    )
    assert "keeps `count(*)` in SQL" not in devdoc, (
        "the DevDoc still describes the split count/digest probe that review "
        "finding F1 removed"
    )
    assert "PROBE_BATCH_SIZE" in devdoc and "buffer" in devdoc.lower(), (
        "the DevDoc must say what is actually held: a batch of "
        "PROBE_BATCH_SIZE rows, buffered per fetch"
    )


# ---------------------------------------------------------------------
# 7. THE CHEAP UNTESTED CASES the review listed
# ---------------------------------------------------------------------


class _RecordingConnection:
    """Enough of a connection to see what the failure path does with it."""

    def __init__(self):
        self.rolled_back = 0
        self.closed = 0

    def rollback(self):
        self.rolled_back += 1

    def close(self):
        self.closed += 1


@pytest.mark.parametrize("allow_prod", [False, True])
def test_proof_only_with_rollback_is_refused_before_any_connection(
    monkeypatch, allow_prod
):
    """Including under `--allow-prod`: the refusal never reaches a database."""

    def _never(*args, **kwargs):
        raise AssertionError(
            "a connection was opened for a combination the harness refuses"
        )

    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_connect", _never)
    monkeypatch.setattr(db, "connect_migration", _never)

    for rollback, down_to in ((True, "0005"), (True, None), (False, "0005")):
        args = argparse.Namespace(
            proof_only=True,
            rollback=rollback,
            down_to=down_to,
            allow_prod=allow_prod,
        )
        with pytest.raises(cli.MigrationError) as excinfo:
            cli.cmd_migrate(args)
        message = str(excinfo.value)
        assert "--proof-only" in message and "--rollback" in message, (
            f"the refusal does not name the conflict: {message}"
        )


def test_an_exception_inside_the_probe_leaves_the_connection_rolled_back(monkeypatch):
    """A probe that dies must not leave a transaction open on the server."""
    conn = _RecordingConnection()
    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_connect", lambda *a, **k: conn)

    def _boom(_conn):
        raise MemoryError("Cannot enlarge string buffer")

    monkeypatch.setattr(cli, "_probe_all", _boom)

    args = argparse.Namespace(
        proof_only=True, rollback=False, down_to=None, allow_prod=False
    )
    with pytest.raises(MemoryError):
        cli.cmd_migrate(args)

    assert conn.rolled_back == 1, "the probe's transaction was not rolled back"
    assert conn.closed == 1, "the connection was left open"


# ---------------------------------------------------------------------
# 8. SNAPSHOT CONSISTENCY — the proof must not see other sessions' commits
# ---------------------------------------------------------------------
#
# THE DEFECT (2026-09-18, desk finding): `cmd_migrate` runs
# `before = _probe_all(conn)` → `_apply(...)` → `after = _probe_all(conn)`
# and rolls back on any `CHANGED` verdict. At READ COMMITTED every probe
# STATEMENT takes its own snapshot, so the AFTER probe sees whatever any
# other session committed in between. Until 2026-09-18 the two probes were
# seconds apart and nobody noticed; production's `system.bars` makes each
# probe ≈46 s, so the window is ≈100 s — and a deploy only takes the two
# RESIDENTS down. `com.cobalt.heartbeat` (every 15 min) and
# `com.cobalt.seat-usage` (hourly) keep updating `system.cobalt_jobs`,
# `cobalt_redactions` is append-only telemetry that drifted 118 → 121 rows
# during one afternoon on dev, and `vault_writes` grows with any vault
# write. ONE such commit inside the window = a false `CHANGED` = the whole
# migration rolled back with the residents down: an outage for nothing.
#
# THE FIX: the harness transaction runs at REPEATABLE READ. The snapshot
# is taken at the transaction's first statement, both probes read THAT
# snapshot plus this transaction's own changes, and the proof answers
# exactly the question it was written for.


#: The table the concurrency tests write to. `_probe_all`'s discovery is a
#: FIXED dict (`placement.MOVED_TABLES/SEEDED_TABLES/CREATED_TABLES`), so a
#: scratch table cannot be registered for the probe from a test; this is
#: the fallback the desk named — append-only telemetry, cheap to probe, and
#: every row inserted here is deleted BY ITS OWN ID in teardown, so the
#: database is left byte-identical.
CONCURRENCY_TABLE = "cobalt_redactions"


def _rel(conn, table: str) -> sql.Identifier:
    """`<schema>.<table>`, wherever the migrations put it.

    Read from the catalog rather than hard-coded `system.`: these tests
    must not quietly pass on a database where the table has not moved.
    """
    schema = cli._schema_of(conn, table)
    assert schema is not None, (
        f"{table} is on none of {cli.SEARCHED_SCHEMAS} — run "
        "`cobalt db migrate` against this database first"
    )
    return sql.Identifier(schema, table)


def _concurrency_rel(conn) -> sql.Identifier:
    return _rel(conn, CONCURRENCY_TABLE)


def _insert_redaction(conn, pattern: str) -> int:
    return conn.execute(
        sql.SQL(
            "INSERT INTO {rel} (channel, pattern, hits) VALUES ('test', %s, 1) "
            "RETURNING id"
        ).format(rel=_concurrency_rel(conn)),
        (pattern,),
    ).fetchone()[0]


def _delete_redaction(conn, row_id: int) -> None:
    conn.execute(
        sql.SQL("DELETE FROM {rel} WHERE id = %s").format(rel=_concurrency_rel(conn)),
        (row_id,),
    )


def _hits(conn, row_id: int) -> Optional[int]:
    row = conn.execute(
        sql.SQL("SELECT hits FROM {rel} WHERE id = %s").format(
            rel=_concurrency_rel(conn)
        ),
        (row_id,),
    ).fetchone()
    return None if row is None else row[0]


def _ids_with_pattern(conn, pattern: str) -> list[int]:
    """Every row this file's tests wrote under one pattern, by id.

    Teardown deletes by id and the assertions read by id; this is how a
    row written inside a transaction that was supposed to be rolled back
    is looked for from ANOTHER session, which is the only place it could
    show up.
    """
    return [
        row[0]
        for row in conn.execute(
            sql.SQL("SELECT id FROM {rel} WHERE pattern = %s ORDER BY id").format(
                rel=_concurrency_rel(conn)
            ),
            (pattern,),
        ).fetchall()
    ]


@requires_db
def test_a_commit_by_another_session_between_the_probes_is_invisible():
    """(a) THE DEFECT, reproduced with a second connection.

    `db.connect_migration` opens autocommit, so the second connection IS
    another session: its INSERT is committed and visible to everyone the
    instant it runs. At READ COMMITTED the AFTER probe picks it up and
    the verdict is `CHANGED` — a good migration rolled back because the
    heartbeat ticked. At REPEATABLE READ both probes read one snapshot
    and the verdict is `OK`.
    """
    other = db.connect_migration(env.DEV_DB_NAME)
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    row_id = None
    try:
        before = cli._probe(conn, CONCURRENCY_TABLE)
        row_id = _insert_redaction(other, "snapshot-fix-a")
        after = cli._probe(conn, CONCURRENCY_TABLE)
    finally:
        conn.rollback()
        conn.close()
        if row_id is not None:
            _delete_redaction(other, row_id)
        other.close()

    assert cli._verdict(CONCURRENCY_TABLE, before, after) == "OK", (
        "another session committed one row between the BEFORE and the AFTER "
        f"probe and the proof called it CHANGED: rows {before['rows']} -> "
        f"{after['rows']}, digest {before['digest']} -> {after['digest']}. "
        "That verdict rolls the migration back with the residents down — an "
        "outage caused by a scheduled job, not by the migration."
    )
    assert (after["rows"], after["digest"]) == (before["rows"], before["digest"]), (
        "the two probes did not read the same snapshot"
    )


@requires_db
def test_the_migrate_transactions_own_write_is_still_seen_between_the_probes():
    """(b) The other half of the property, and the one that must NOT break.

    A snapshot that hid the transaction's own changes would make the
    proof useless: it exists to answer "did THIS migration change
    existing content?". REPEATABLE READ shows a transaction its own
    writes, so the verdict here is `CHANGED` before and after the fix.
    The row is inserted through the MIGRATE connection and never
    committed — the rollback in `finally` is the whole teardown.
    """
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    try:
        row_id = _insert_redaction(conn, "snapshot-fix-b")
        before = cli._probe(conn, CONCURRENCY_TABLE)
        conn.execute(
            sql.SQL("UPDATE {rel} SET hits = hits + 1 WHERE id = %s").format(
                rel=_concurrency_rel(conn)
            ),
            (row_id,),
        )
        after = cli._probe(conn, CONCURRENCY_TABLE)
    finally:
        conn.rollback()
        conn.close()

    assert cli._verdict(CONCURRENCY_TABLE, before, after) == "CHANGED", (
        "the migrate transaction's OWN update between the probes was invisible "
        "to the AFTER probe. A proof that cannot see the migration's own "
        "changes proves nothing at all."
    )


@requires_db
def test_the_proof_only_transaction_is_repeatable_read_and_read_only():
    """(c) Asserted at the SERVER, not on the Python attributes."""
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=True)
    try:
        isolation = conn.execute("SHOW transaction_isolation").fetchone()[0]
        read_only = conn.execute("SHOW transaction_read_only").fetchone()[0]
    finally:
        conn.rollback()
        conn.close()

    assert isolation == "repeatable read", (
        f"--proof-only's transaction runs at {isolation!r}. Its whole job is to "
        "carry ONE consistent picture of the database out of a deploy window"
    )
    assert read_only == "on", f"--proof-only's transaction is not READ ONLY: {read_only!r}"


@requires_db
def test_the_migrate_transaction_is_repeatable_read_and_read_write():
    """(d) The same isolation, without losing the ability to apply."""
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    try:
        isolation = conn.execute("SHOW transaction_isolation").fetchone()[0]
        read_only = conn.execute("SHOW transaction_read_only").fetchone()[0]
    finally:
        conn.rollback()
        conn.close()

    assert isolation == "repeatable read", (
        f"the migrate transaction runs at {isolation!r}, so its BEFORE and "
        "AFTER probes read two different databases"
    )
    assert read_only == "off", (
        "the migrate transaction must still be able to APPLY the migrations: "
        f"transaction_read_only is {read_only!r}"
    )


@requires_db
def test_a_concurrent_update_to_a_row_the_migration_updates_fails_loud(monkeypatch):
    """(e) The KNOWN CONSEQUENCE, made deterministic and made loud.

    REPEATABLE READ buys the snapshot at a price, and this is the price:
    if another session commits a change to a row this transaction then
    modifies, Postgres refuses to serialize the two and raises. That is
    the RIGHT outcome — nothing is applied, the existing
    `except: conn.rollback(); raise` path runs, and the operator is told
    what happened rather than being handed a bare driver error.

    Deterministic by construction: the row is committed BEFORE the
    migration opens (so it is in the snapshot), the other session commits
    over it while the migration holds that snapshot, and the migration
    then updates the same row.

    STRENGTHENED 2026-09-19 (tribunal round 1, R3 — Astra finding 2). As
    first written, the fake migration's ONLY write was the one Postgres
    rejects, so the rollback had nothing to undo and this test passed
    with or without it. The migration now makes a write of its own FIRST,
    on a row this test owns, and the test asserts that write is GONE
    afterwards — which is a claim about the rollback rather than about
    the statement Postgres refused.
    """
    other = db.connect_migration(env.DEV_DB_NAME)
    row_id = _insert_redaction(other, "snapshot-fix-e")
    reached: list[str] = []
    owned: list[int] = []

    def _conflicting_apply(conn, paths):
        owned.append(_insert_redaction(conn, "snapshot-fix-e-owned"))
        reached.append("the migration's own write landed")
        other.execute(
            sql.SQL("UPDATE {rel} SET hits = 2 WHERE id = %s").format(
                rel=_concurrency_rel(other)
            ),
            (row_id,),
        )
        reached.append("other session committed")
        conn.execute(
            sql.SQL("UPDATE {rel} SET hits = 3 WHERE id = %s").format(
                rel=_concurrency_rel(conn)
            ),
            (row_id,),
        )
        reached.append("the migration's own update returned")

    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_apply", _conflicting_apply)
    args = argparse.Namespace(
        proof_only=False, rollback=False, down_to=None, allow_prod=False
    )
    try:
        with pytest.raises(cli.MigrationError) as excinfo:
            cli.cmd_migrate(args)
        message = str(excinfo.value)
        assert "serialize" in message.lower(), (
            "the harness did not name the serialization failure; an operator "
            f"reading this at 20:40 on a deploy gets: {message}"
        )
        assert "nothing was applied" in message.lower(), (
            f"the message does not say that nothing was applied: {message}"
        )
        assert reached == [
            "the migration's own write landed",
            "other session committed",
        ], (
            "the migration's UPDATE of a row another session had already "
            f"changed was allowed through: {reached}"
        )
        assert _hits(other, row_id) == 2, (
            "the migration's write survived a transaction that failed — the "
            "rollback path did not run"
        )
        assert owned, "the fake migration never made its own write"
        assert _hits(other, owned[0]) is None, (
            f"the migrate transaction's OWN write ({CONCURRENCY_TABLE} row "
            f"{owned[0]}, made BEFORE the conflict) is still in the database "
            "after the command failed. Nothing rolled that transaction back."
        )
        assert _ids_with_pattern(other, "snapshot-fix-e-owned") == [], (
            "a row the failed migration wrote is visible to another session"
        )
    finally:
        _delete_redaction(other, row_id)
        for leaked in _ids_with_pattern(other, "snapshot-fix-e-owned"):
            _delete_redaction(other, leaked)
        other.close()


# ---------------------------------------------------------------------
# 9. THE TRIBUNAL'S ROUND 1 (2026-09-19)
# ---------------------------------------------------------------------
#
# Three houses read the snapshot build (`scratch/review-harness-0919/`:
# Grok SAFE TO DEPLOY, Gemini FIX FIRST Q5, Astra FIX FIRST 1). What
# survived the hub's verification and lands here:
#
#   R1 (Astra finding 1, REAL, latent) — `_schema_of` looked a table up
#      across `SEARCHED_SCHEMAS` with `LIMIT 1` and no `ORDER BY`. If one
#      name existed in two of those schemas the proof could digest the
#      UNTOUCHED copy, before and after, and print `OK` for a table the
#      migration had changed. Production has no such duplicate today, so
#      this was never the 09-18 failure; it is a VERIFIER THAT CAN LIE,
#      on the production write path, and L1 says such a thing fails loud
#      rather than guesses.
#   R3 (Astra finding 2, REAL) — test (e) above could not detect a
#      missing rollback, and nothing tested the CLI boundary. Both fixed:
#      (e) is strengthened in place, and the exit status is asserted here
#      through a real process.
#   U1 (Astra Q2 + the hub; UNVERIFIABLE FROM READS) — the runner
#      re-applies `0003` on EVERY run, and its `ALTER TABLE
#      system.cobalt_jobs ADD COLUMN IF NOT EXISTS …` runs AFTER the
#      BEFORE probe has read that table under REPEATABLE READ, while
#      `com.cobalt.heartbeat` (every 15 min) and `com.cobalt.seat-usage`
#      (hourly) keep committing to it. Yesterday's dev round trip had no
#      concurrent writer, so nobody had ever run that interleaving. (f)
#      and (g) run it.
#
# (f) and (g) have NO CODE CHANGE behind them: they pin Postgres's
# behaviour against the code as it already stands, so they pass at once,
# exactly as test (b) does. That is the point — the claim was unproven,
# not wrong, and a future Postgres or a future `0003` that breaks it now
# fails HERE instead of at 20:40 on a deploy.

#: The table `0003` alters, and the one the two residents write to.
JOBS_TABLE = "cobalt_jobs"

#: Hard ceiling, in seconds, on the lock wait in test (g). A hang must
#: FAIL the test, never hang the suite, so the ceiling lives here.
LOCK_CEILING_S = 20.0

#: A1 (2026-09-19, Astra): the SERVER-SIDE ceiling on test (g)'s worker
#: connection, a little above `LOCK_CEILING_S`. `LOCK_CEILING_S` only
#: bounds how long the MAIN thread waits; it cannot end a statement
#: already running on the worker's connection. Without this, a lock wait
#: that outlived the join left a backend queued for ACCESS EXCLUSIVE on
#: `cobalt_dev` until the interpreter exited — in front of every other
#: session wanting that table. With it, a hung ALTER ends ITSELF.
WORKER_STATEMENT_TIMEOUT_S = 25


def _migration_0003_sql() -> str:
    """`0003_heartbeat_vault_outcome.sql`, WHOLE, from the file itself.

    L45: the real artifact. Retyping the `ALTER TABLE` here would prove
    something about a string in a test file, not about the statement the
    runner actually sends on every migrate — which is the statement U1 is
    a question about. The assertions below are what notice if `0003` ever
    stops being that statement.
    """
    path = next(p for p in FORWARD if p.name.startswith("0003_"))
    text = path.read_text()
    assert "ALTER TABLE system.cobalt_jobs" in text, (
        f"{path.name} no longer alters system.cobalt_jobs, so tests (f) and "
        f"(g) are no longer exercising the U1 case:\n{text}"
    )
    assert "ADD COLUMN IF NOT EXISTS" in text, (
        f"{path.name} is no longer the idempotent ADD COLUMN the runner "
        f"re-applies every run:\n{text}"
    )
    return text


def _touch_a_job_row(conn) -> None:
    """A no-CHANGE update of one existing `cobalt_jobs` row.

    `SET last_result = last_result` writes a new row version — which is
    what makes it a concurrent commit as far as MVCC and lock conflicts
    are concerned — while leaving every value, and therefore the table's
    digest, exactly as it was. So there is nothing to clean up: this is
    the one write in the file that leaves no trace to delete.
    """
    rel = _rel(conn, JOBS_TABLE)
    updated = conn.execute(
        sql.SQL(
            "UPDATE {rel} SET last_result = last_result "
            "WHERE label = (SELECT min(label) FROM {rel})"
        ).format(rel=rel)
    ).rowcount
    assert updated == 1, (
        f"the other session updated {updated} row(s) of {JOBS_TABLE}, not 1 — "
        "the interleaving these tests describe did not happen"
    )


def _wait_for_a_blocked_lock(watcher, table: str, ceiling: float, pid: int) -> bool:
    """True once THE WORKER'S OWN backend is waiting for ACCESS EXCLUSIVE
    on `table`.

    Polling the catalog rather than sleeping a guessed interval: the test
    must know the ALTER is actually BLOCKED before it releases the other
    session, or it proves nothing about waiting.

    A2 (2026-09-19, Astra; `cto-2026-09-19.md` §8). This used to count
    ANY ungranted lock on the table, in ANY mode, held by ANY session —
    so a concurrent suite run, a stray `psql`, or the test's OWN other
    session queueing behind something satisfied it, and the caller
    proceeded believing it had reproduced the interleaving when it had
    not. All three filters are now required: the backend this test
    started (`pid`, read from the worker connection BEFORE its thread
    starts), the mode an `ALTER TABLE` actually asks for
    (`AccessExclusiveLock`), and not yet granted.
    """
    schema = cli._schema_of(watcher, table)
    deadline = time.perf_counter() + ceiling
    while time.perf_counter() < deadline:
        blocked = watcher.execute(
            """
            SELECT count(*)
            FROM pg_locks l
            JOIN pg_class c ON c.oid = l.relation
            JOIN pg_namespace n ON n.oid = c.relnamespace
            WHERE c.relname = %s AND n.nspname = %s
              AND l.pid = %s
              AND l.mode = 'AccessExclusiveLock'
              AND NOT l.granted
            """,
            (table, schema, pid),
        ).fetchone()[0]
        if blocked:
            return True
        time.sleep(0.05)
    return False


@requires_db
def test_a_table_name_in_two_searched_schemas_is_refused():
    """(h) R1 — the proof must never pick one of two candidates.

    The duplicate is created through the SAME connection the probe reads
    with, and the transaction is rolled back in `finally`, so nothing is
    ever committed to `cobalt_dev`: the ambiguity exists only inside this
    transaction's own catalog view, which is exactly where `_schema_of`
    looks.
    """
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    try:
        home = cli._schema_of(conn, CONCURRENCY_TABLE)
        assert home is not None, "the fixture table is not on any searched schema"
        intruder = next(s for s in cli.SEARCHED_SCHEMAS if s != home)
        conn.execute(
            sql.SQL("CREATE TABLE {rel} (id INTEGER PRIMARY KEY)").format(
                rel=sql.Identifier(intruder, CONCURRENCY_TABLE)
            )
        )
        with pytest.raises(cli.MigrationError) as excinfo:
            cli._schema_of(conn, CONCURRENCY_TABLE)
        message = str(excinfo.value)
        # And the production path, not just the helper: `_probe` is what
        # the proof calls, and it must not digest either candidate.
        with pytest.raises(cli.MigrationError):
            cli._probe(conn, CONCURRENCY_TABLE)
    finally:
        conn.rollback()
        conn.close()

    assert CONCURRENCY_TABLE in message, (
        f"the refusal does not name the table: {message}"
    )
    assert home in message and intruder in message, (
        "the refusal must name BOTH schemas — an operator cannot act on "
        f"'a duplicate exists somewhere': {message}"
    )


@requires_db
def test_one_match_still_returns_that_schema():
    """(h2) R1's unchanged case: exactly one match behaves as it always did."""
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    try:
        found = cli._schema_of(conn, CONCURRENCY_TABLE)
        rows = conn.execute(
            "SELECT schemaname FROM pg_tables "
            "WHERE tablename = %s AND schemaname = ANY(%s)",
            (CONCURRENCY_TABLE, list(cli.SEARCHED_SCHEMAS)),
        ).fetchall()
    finally:
        conn.rollback()
        conn.close()

    assert len(rows) == 1, f"the fixture table is not unique on this database: {rows}"
    assert found == rows[0][0]


@requires_db
def test_no_match_still_returns_none():
    """(h3) R1's other unchanged case: `None` is how `_probe` says ABSENT."""
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    try:
        assert cli._schema_of(conn, "no_migration_has_ever_created_this") is None
    finally:
        conn.rollback()
        conn.close()


def test_the_cli_turns_a_migration_error_into_failed_and_exit_1():
    """(i) R3 — the CLI boundary the review read but nothing tested.

    `cobalt.cli.main` catches every exception, prints
    `FAILED: <type>: <message>` on STDERR and exits 1. A deploy reads
    that exit status, so it is asserted through a REAL process rather
    than by reading `main`. The cheapest `MigrationError` there is:
    `--proof-only` with `--rollback`, refused before any connection is
    opened, which is why this test needs no database.
    """
    proc = _migrate("--proof-only", "--rollback", "--down-to", "0005")

    assert proc.returncode == 1, (
        "a MigrationError must leave the process with exit status 1; got "
        f"{proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    )
    assert "FAILED: MigrationError: " in proc.stderr, (
        "the CLI did not render the MigrationError as `FAILED: …` on stderr:\n"
        f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    )
    assert "FAILED:" not in proc.stdout, (
        "the failure was printed on STDOUT, where a deploy log mixes it with "
        f"the proof table:\n{proc.stdout}"
    )


@requires_db
def test_ddl_runs_after_another_session_committed_to_the_same_table():
    """(f) U1 — `0003`'s ALTER after a concurrent commit, under REPEATABLE READ.

    The interleaving a production deploy actually runs: BEFORE probe
    reads `cobalt_jobs` under the snapshot, the heartbeat commits to that
    same table, and then `0003` — re-applied on every run — takes ACCESS
    EXCLUSIVE on it. Nobody had run it: yesterday's round trip had no
    concurrent writer, and no house could settle it from reads.

    EXPECTED: no serialization error, and the table reads unchanged
    (the other session's commit is outside this transaction's snapshot,
    which is the whole property the snapshot fix bought).
    """
    other = db.connect_migration(env.DEV_DB_NAME)
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    try:
        before = cli._probe(conn, JOBS_TABLE)
        _touch_a_job_row(other)  # autocommit: committed the instant it runs
        conn.execute(_migration_0003_sql())
        after = cli._probe(conn, JOBS_TABLE)
    finally:
        conn.rollback()
        conn.close()
        other.close()

    assert cli._verdict(JOBS_TABLE, before, after) == "OK", (
        "a concurrent commit to cobalt_jobs, followed by 0003's ALTER TABLE, "
        f"changed what the proof reads: rows {before['rows']} -> "
        f"{after['rows']}, digest {before['digest']} -> {after['digest']}"
    )


@requires_db
def test_the_alter_waits_for_an_open_transaction_and_then_completes():
    """(g) U1's harder half: the other session is still IN its transaction.

    `ALTER TABLE` needs ACCESS EXCLUSIVE and the open transaction holds
    ROW EXCLUSIVE on the same rows, so the ALTER must WAIT — and must
    complete, without error, once that transaction commits. Driven from a
    thread with a hard ceiling inside the test, because the failure mode
    being guarded against is a hang, and a hang that stops the suite
    tells a deploy nothing.

    EXPECTED: the ALTER blocks, then completes; no error either way.

    HOW THIS TEST'S CEILINGS RELATE TO THE HARNESS'S OWN `lock_timeout`
    (A1, 2026-09-19). They do not overlap, and that is worth stating
    rather than assuming. This test calls `cli._connect` and executes the
    ALTER ITSELF; it never goes through `cmd_migrate`, which is the only
    place `SET LOCAL lock_timeout = '<DEFAULT_LOCK_TIMEOUT_S>s'` is
    issued. So the harness's 30 s ceiling is NOT in force here at all.
    What bounds this test, in the order the clocks run out:

      1. `LOCK_CEILING_S` (20 s) — the MAIN thread's `join` gives up and
         the test has its verdict.
      2. `WORKER_STATEMENT_TIMEOUT_S` (25 s), set on the worker
         connection below — the server ends a still-running ALTER by
         itself, so no backend is left queued on `cobalt_dev`. It is
         deliberately ABOVE (1): a legitimate wait must be reported by
         this test, not pre-empted by the server.

    WHAT (1)-BEFORE-(2) ACTUALLY GUARANTEES (R3, tribunal round 1; this
    used to be stated unconditionally and was not true in general). The
    two clocks do not start together: (2) starts at the server when the
    ALTER begins executing, right after `thread.start()`, while (1) is
    only armed once `_wait_for_a_blocked_lock` has returned AND
    `other.commit()` has run. So (1) fires first exactly while those two
    steps take less than the 5 s of headroom between them — which is the
    case this test drives: the probe polls the catalog every 50 ms and
    returns as soon as the worker's own ungranted `AccessExclusiveLock`
    request is visible, i.e. within milliseconds of the ALTER blocking,
    and the commit is a local round trip.

    It is NOT a general guarantee, and no bound beyond the 5 s of
    headroom is claimed here. If the probe itself ran long — its own
    ceiling is `LOCK_CEILING_S`, and it returns False rather than early
    when the worker's request never appears, e.g. because a THIRD
    session already holds ACCESS EXCLUSIVE — the server's 25 s can fire
    first. Then the worker's ALTER raises, `hung` is False, and the
    `_probe` on the next line meets an aborted transaction: the message
    a reader sees is a driver error, not this test's own "did not
    finish" assertion.

    CLEANUP RUNS ON EVERY PATH (R2, tribunal round 1; NESTED by F1,
    tribunal round 2). Whatever the `try` did or raised, the `finally`
    below cancels a still-running worker statement from the main thread,
    rejoins, then rolls back and closes the worker's connection. It is
    not conditional on the hung verdict: an exception from the lock probe
    or from `other.commit()` would otherwise leave a backend queued for
    ACCESS EXCLUSIVE past the end of the test. On the hung path the test
    still fails with the same message.

    F1 is the second half of that, and it is why the worker cleanup sits
    in a nested `finally` rather than simply below the other three
    statements: `other.commit()`, `other.close()` and `watcher.close()`
    run FIRST, and if any of THEM raises, an unnested worker cleanup is
    skipped just as surely as R2's `if hung:` used to skip it. Nesting
    makes the cleanup independent of how closing the other two
    connections goes.
    """
    other = db.connect_migration(env.DEV_DB_NAME)
    watcher = db.connect_migration(env.DEV_DB_NAME)
    conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
    outcome: list[tuple[str, Optional[BaseException]]] = []
    alter = _migration_0003_sql()

    def _run_the_alter() -> None:
        try:
            conn.execute(alter)
            outcome.append(("completed", None))
        except BaseException as e:  # a FINDING, not a test to bend
            outcome.append(("raised", e))

    thread = threading.Thread(target=_run_the_alter, daemon=True)
    committed = False
    after = None
    try:
        before = cli._probe(conn, JOBS_TABLE)
        # A1: the worker's own server-side ceiling, set on the open
        # transaction before anything can block on it. `SET LOCAL` so it
        # dies with this transaction and cannot leak into a later one.
        conn.execute(f"SET LOCAL statement_timeout = '{WORKER_STATEMENT_TIMEOUT_S}s'")
        # A2: the backend the ALTER will run on, read from the main
        # thread BEFORE the worker thread starts — so the lock probe
        # below can ask about THIS session and no other.
        worker_pid = conn.execute("SELECT pg_backend_pid()").fetchone()[0]
        other.autocommit = False  # the other session's transaction stays OPEN
        _touch_a_job_row(other)
        thread.start()
        blocked = _wait_for_a_blocked_lock(
            watcher, JOBS_TABLE, LOCK_CEILING_S, worker_pid
        )
        other.commit()
        committed = True
        thread.join(timeout=LOCK_CEILING_S)
        hung = thread.is_alive()
        if not hung:
            after = cli._probe(conn, JOBS_TABLE)
    finally:
        try:
            if not committed:
                other.commit()
            other.close()
            watcher.close()
        finally:
            # R2 (tribunal round 1, 2026-09-19): the cancel + rejoin used
            # to sit in the `try` under `if hung:`, so any exception
            # raised between `thread.start()` and that check — from
            # `_wait_for_a_blocked_lock`, from `other.commit()` — skipped
            # it and left the worker's backend queued for ACCESS
            # EXCLUSIVE on `cobalt_dev` in front of every other session.
            # It is here now, unconditional, and there is only one copy
            # of it (L3).
            #
            # F1 (tribunal round 2, folded by the DB run 2026-09-19): and
            # it is NESTED, because R2 alone was not enough — the three
            # statements above still ran first and unguarded, so a raise
            # from `other.commit()`, `other.close()` or `watcher.close()`
            # skipped this block for exactly the same reason and left
            # exactly the same backend queued.
            #
            # The commit above has already released what the ALTER was
            # waiting for, so a still-live thread at this point is one
            # that did not get its lock anyway. `cancel()` is psycopg's
            # documented cross-thread call, the one thing the main thread
            # may do to a connection another thread is using. The rejoin
            # is given the SERVER ceiling's worth of time, because that
            # is the backstop if the cancel does not land.
            if thread.is_alive():
                conn.cancel()
                thread.join(timeout=WORKER_STATEMENT_TIMEOUT_S)
            # Only from THIS thread once the ALTER is done with the
            # connection. After the cancel + rejoin above, the hung path
            # reaches here with a finished thread too, so the worker's
            # transaction is rolled back and its connection closed on
            # every path the cancel could reach (A1).
            if not thread.is_alive():
                conn.rollback()
                conn.close()

    assert not hung, (
        f"0003's ALTER TABLE did not finish within {LOCK_CEILING_S:.0f} s of "
        "the other session committing. A migration that can hang behind a "
        "resident's transaction is a deploy that never ends."
    )
    assert blocked, (
        "the ALTER never appeared in pg_locks as waiting, so this test did "
        "not exercise the lock wait it claims to (Postgres took ACCESS "
        "EXCLUSIVE without contention — check that the other session's "
        "transaction really was open)"
    )
    assert outcome and outcome[0][0] == "completed", (
        "0003's ALTER TABLE raised after waiting for a concurrent "
        f"transaction to commit: {outcome[0][1]!r}"
    )
    assert cli._verdict(JOBS_TABLE, before, after) == "OK", (
        "the table did not read unchanged after the lock wait: rows "
        f"{before['rows']} -> {after['rows']}, digest {before['digest']} -> "
        f"{after['digest']}"
    )


# ---------------------------------------------------------------------
# 10. `lock_timeout` ON THE MIGRATE TRANSACTION (ops 2026-09-19, item c)
# ---------------------------------------------------------------------
#
# ORIGIN: `prod-proof-only-3-2026-09-19.md` ESCALATE 3 — "Nothing in
# `cli.py` sets a `lock_timeout` or a statement timeout … so a deploy
# whose `0003` ALTER meets a heartbeat write waits indefinitely rather
# than failing fast". The only ceiling was the Bash tool's 600 s, which
# is a property of whoever launched the deploy, not of the code.
#
# THE SHAPE: the READ-WRITE migrate transaction issues
# `SET LOCAL lock_timeout` before `_apply`'s first statement, forward and
# rollback alike; `psycopg.errors.LockNotAvailable` is wrapped exactly as
# `SerializationFailure` already is — rollback, then a `MigrationError`
# that says NOTHING WAS APPLIED and names the timeout. `--proof-only`
# takes ACCESS SHARE only and is deliberately NOT changed: it must not
# start failing on a busy evening.
#
# WHERE THE STATEMENT SITS: BEFORE the BEFORE probe, since 2026-09-19.
# It was written the other way round — the conservative placement, so
# that the `SET` provably could not sit between the transaction's start
# and its snapshot — and the price of that, stated rather than
# discovered, was that THE BEFORE PROBE ITSELF WAS NOT UNDER THE TIMEOUT:
# it takes ACCESS SHARE, which only an ACCESS EXCLUSIVE holder (another
# DDL) can block, and against such a holder it waited unbounded. §12
# settles the snapshot question by experiment on `cobalt_dev` (R1/R11)
# and the statement moved; §12 (n) is the probe's own coverage test.
# The two tests below are unchanged by the move: they assert the `SET`
# precedes the first MIGRATION FILE, which it did before and does now.


class _StatementRecorder:
    """An offline stand-in for the migrate connection.

    It records every statement `cmd_migrate` sends and executes none of
    them, so the ORDER of the statements — which is the whole claim here
    — is checkable with no database. `_apply` is left REAL: it reads the
    registered `.sql` files off disk and hands each one to `execute`, so
    "before the first migration file's text" means the actual text of the
    actual file, not a stand-in for it (L45).
    """

    def __init__(self, raise_on_apply: Optional[BaseException] = None):
        self.statements: list[str] = []
        self.rolled_back = 0
        self.committed = 0
        self.closed = 0
        self._raise_on_apply = raise_on_apply

    def execute(self, query, *args, **kwargs):
        text = query if isinstance(query, str) else str(query)
        self.statements.append(text)
        if self._raise_on_apply is not None and "SET LOCAL" not in text:
            raise self._raise_on_apply
        return None

    def rollback(self):
        self.rolled_back += 1

    def commit(self):
        self.committed += 1

    def close(self):
        self.closed += 1


def _offline_migrate(monkeypatch, recorder, print_proof=None, **namespace):
    """Run `cmd_migrate` with no database: the connection is the recorder
    and both probe passes are stubbed (an empty probe dict makes every
    verdict vacuously OK, which is what lets the commit path run).

    `print_proof` overrides the proof-table stub for a test that needs to
    see where the table lands in the output.
    """
    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_connect", lambda *a, **k: recorder)
    monkeypatch.setattr(cli, "_probe_all", lambda conn: {})
    monkeypatch.setattr(cli, "_print_proof", print_proof or (lambda *a, **k: 0))
    fields = {
        "proof_only": False,
        "rollback": False,
        "down_to": None,
        "allow_prod": False,
        "lock_timeout_s": cli.DEFAULT_LOCK_TIMEOUT_S,
    }
    fields.update(namespace)
    return cli.cmd_migrate(argparse.Namespace(**fields))


def _index_of(statements: list[str], needle: str) -> int:
    for i, text in enumerate(statements):
        if needle in text:
            return i
    raise AssertionError(f"no statement contains {needle!r}; sent: {statements}")


def test_the_default_lock_timeout_is_thirty_seconds():
    """A module constant, not a literal buried in the call — the DevDoc
    and the deploy prompt both quote this number."""
    assert cli.DEFAULT_LOCK_TIMEOUT_S == 30


def test_a_forward_run_sets_lock_timeout_before_the_first_migration_file(monkeypatch):
    recorder = _StatementRecorder()
    _offline_migrate(monkeypatch, recorder)

    first_file_text = FORWARD[0].read_text()
    set_at = _index_of(recorder.statements, "SET LOCAL lock_timeout")
    applied_at = recorder.statements.index(first_file_text)
    assert set_at < applied_at, (
        "the lock ceiling was set AFTER the first migration file had already "
        f"been sent: statement order {recorder.statements[:3]}"
    )
    assert f"'{cli.DEFAULT_LOCK_TIMEOUT_S}s'" in recorder.statements[set_at]
    assert recorder.committed == 1 and recorder.rolled_back == 0


def test_a_rollback_run_sets_lock_timeout_too(monkeypatch):
    """A rollback's reverse migrations are DDL as well — a deploy that
    cannot roll back because it is waiting on a lock is the worse half of
    the same defect."""
    recorder = _StatementRecorder()
    _offline_migrate(monkeypatch, recorder, rollback=True, down_to="0005")

    reverse_text = cli._rollback_paths("0005")[0].read_text()
    set_at = _index_of(recorder.statements, "SET LOCAL lock_timeout")
    assert set_at < recorder.statements.index(reverse_text)


def test_proof_only_sends_no_lock_timeout(monkeypatch):
    """`--proof-only` takes ACCESS SHARE and applies nothing. Giving it a
    lock ceiling would make the one command a deploy runs while
    everything is still up start failing on a busy evening."""
    recorder = _StatementRecorder()
    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_connect", lambda *a, **k: recorder)
    monkeypatch.setattr(cli, "_probe_all", lambda conn: {})
    monkeypatch.setattr(cli, "_print_probe", lambda *a, **k: None)
    args = argparse.Namespace(
        proof_only=True, rollback=False, down_to=None, allow_prod=False,
        lock_timeout_s=cli.DEFAULT_LOCK_TIMEOUT_S,
    )
    cli.cmd_migrate(args)

    offenders = [s for s in recorder.statements if "lock_timeout" in s]
    assert not offenders, f"--proof-only sent a lock ceiling: {offenders}"


def test_a_lock_it_cannot_get_rolls_back_and_says_nothing_was_applied(monkeypatch):
    """The `SerializationFailure` shape, for the other named price of a
    deploy-time DDL."""
    recorder = _StatementRecorder(
        raise_on_apply=psycopg.errors.LockNotAvailable(
            "canceling statement due to lock timeout"
        )
    )
    with pytest.raises(cli.MigrationError) as excinfo:
        _offline_migrate(monkeypatch, recorder)

    message = str(excinfo.value)
    assert recorder.rolled_back == 1, "the transaction was not rolled back"
    assert recorder.committed == 0
    assert "nothing was applied" in message.lower(), message
    assert f"{cli.DEFAULT_LOCK_TIMEOUT_S}" in message, (
        f"the message does not name the timeout that fired: {message}"
    )
    assert "pg_locks" in message, (
        "the operator is not told how to find the session holding the lock: "
        f"{message}"
    )
    # R5 (tribunal round 1, 2026-09-19). The hint used to read `pg_locks
    # WHERE NOT granted`, which selects WAITING requests, not the holder
    # — and by the time an operator runs it this transaction has already
    # rolled back, so its own waiting row is gone too and the query can
    # come back empty while a holder is sitting there. The hint must
    # point at a GRANTED lock and name who holds it.
    assert "NOT granted" not in message, (
        "the hint still filters on ungranted locks, which lists waiters "
        f"(and after this rollback, not even this one): {message}"
    )
    assert "pg_stat_activity" in message, (
        "the hint names no way to see WHICH session holds the lock: "
        f"{message}"
    )
    assert "l.granted" in message, (
        f"the hint does not select granted locks: {message}"
    )


@pytest.mark.parametrize("bad", [0, -1, -30])
def test_a_zero_or_negative_lock_timeout_is_refused_before_any_connection(
    monkeypatch, bad
):
    """0 means "wait forever" — the very defect the flag closes — so it is
    refused where every other malformed-argument refusal lives: before a
    connection exists."""

    def _never(*args, **kwargs):
        raise AssertionError("a connection was opened for a refused lock ceiling")

    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_connect", _never)
    monkeypatch.setattr(db, "connect_migration", _never)

    args = argparse.Namespace(
        proof_only=False, rollback=False, down_to=None, allow_prod=False,
        lock_timeout_s=bad,
    )
    with pytest.raises(cli.MigrationError) as excinfo:
        cli.cmd_migrate(args)
    assert "--lock-timeout-s" in str(excinfo.value)


def test_the_cli_turns_a_refused_lock_timeout_into_failed_and_exit_1():
    """The CLI boundary for this flag, through a REAL process, in the
    shape of `test_the_cli_turns_a_migration_error_into_failed_and_exit_1`
    — and like that one it needs no database, because the refusal happens
    before any connection is opened."""
    proc = _migrate("--lock-timeout-s", "0")

    assert proc.returncode == 1, (
        f"got {proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    )
    assert "FAILED: MigrationError: " in proc.stderr, (
        f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    )
    assert "--lock-timeout-s" in proc.stderr


@requires_db
def test_a_migration_that_cannot_get_its_lock_fails_in_about_a_second(monkeypatch):
    """(j) NEVER RUN AS OF 2026-09-19 — written offline, owed a first run
    on `cobalt_dev` once `p4-verify-0919` releases it.

    Another session holds ACCESS EXCLUSIVE on the table `0003` alters, so
    `_apply`'s ALTER cannot get its lock; with `--lock-timeout-s 1` the
    run must FAIL in about a second instead of waiting, and the table's
    proof must be unchanged afterwards.

    `_probe_all` is stubbed deliberately, and what that means CHANGED on
    2026-09-19 (R1/R11, the ops DB run). It used to be a necessity: the
    `SET LOCAL` was issued AFTER the BEFORE probe, so a real probe would
    have blocked on the ACCESS EXCLUSIVE holder with no ceiling at all.
    The `SET LOCAL` now runs BEFORE the probe, so the stub is a
    NARROWING, not a workaround — it keeps this test on the one property
    it was written for, the ceiling reaching `_apply`, which is where the
    deploy's DDL is. The probe's own coverage is a separate test, §12
    (n), `test_a_blocked_before_probe_is_under_the_lock_ceiling_too`,
    which runs the real `_probe_all` against the same held lock.
    """
    reader = db.connect_migration(env.DEV_DB_NAME)
    holder = db.connect_migration(env.DEV_DB_NAME)
    try:
        before = cli._probe(reader, JOBS_TABLE)

        holder.autocommit = False
        holder.execute(
            sql.SQL("LOCK TABLE {rel} IN ACCESS EXCLUSIVE MODE").format(
                rel=_rel(holder, JOBS_TABLE)
            )
        )

        conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
        monkeypatch.setenv(env.ENV_VAR, env.DEV)
        monkeypatch.setattr(cli, "_connect", lambda *a, **k: conn)
        monkeypatch.setattr(cli, "_probe_all", lambda c: {})
        monkeypatch.setattr(cli, "_print_proof", lambda *a, **k: 0)
        args = argparse.Namespace(
            proof_only=False, rollback=False, down_to=None, allow_prod=False,
            lock_timeout_s=1,
        )

        started = time.perf_counter()
        with pytest.raises(cli.MigrationError) as excinfo:
            cli.cmd_migrate(args)
        elapsed = time.perf_counter() - started

        assert "nothing was applied" in str(excinfo.value).lower()
        assert elapsed < LOCK_CEILING_S, (
            f"--lock-timeout-s 1 took {elapsed:.1f} s to give up — the ceiling "
            "is not reaching the statement that waits"
        )
    finally:
        holder.rollback()
        holder.close()
        reader.close()

    after_conn = db.connect_migration(env.DEV_DB_NAME)
    try:
        after = cli._probe(after_conn, JOBS_TABLE)
    finally:
        after_conn.close()
    assert cli._verdict(JOBS_TABLE, before, after) == "OK", (
        "a migration that failed on its lock left the table changed: rows "
        f"{before['rows']} -> {after['rows']}, digest {before['digest']} -> "
        f"{after['digest']}"
    )


# ---------------------------------------------------------------------
# 11. THE OUTPUT NAMES THE CODE IT RAN FROM (ops 2026-09-19, item e)
# ---------------------------------------------------------------------
#
# ORIGIN: `cto-2026-09-19.md` §14 — the deploy's git-history binding
# proves the proof report was COMMITTED after a given sha on the branch,
# not which code EXECUTED; the desk had to verify by hand that the
# report's commits sat on that code. The fix is one printed line.
#
# A git failure NEVER fails a migration or a proof: the line reads
# `code: UNKNOWN — <reason>`, which is explicit and is not a plausible
# value (L1). Refusing an UNKNOWN or a DIRTY tip is the DEPLOY GATE's
# job, in the desk's prompt, not this command's.


def _fake_git_factory(sha="abc1234", porcelain="", raises=None):
    def _fake_git(repo_root, *args, **kwargs):
        if raises is not None:
            raise raises
        if args[:1] == ("rev-parse",):
            return sha + "\n"
        if args[:1] == ("status",):
            return porcelain
        raise AssertionError(f"unexpected git call: {args}")

    return _fake_git


def _patch_git(monkeypatch, **kwargs):
    from cobalt.generated import committer

    monkeypatch.setattr(committer, "_git", _fake_git_factory(**kwargs))


def _proof_only_output(monkeypatch, capsys) -> list[str]:
    recorder = _StatementRecorder()
    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_connect", lambda *a, **k: recorder)
    monkeypatch.setattr(cli, "_probe_all", lambda conn: {})
    monkeypatch.setattr(cli, "_print_probe", lambda *a, **k: print("<proof table>"))
    args = argparse.Namespace(
        proof_only=True, rollback=False, down_to=None, allow_prod=False,
        lock_timeout_s=cli.DEFAULT_LOCK_TIMEOUT_S,
    )
    cli.cmd_migrate(args)
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def test_proof_only_ends_with_the_code_it_ran_from(monkeypatch, capsys):
    _patch_git(monkeypatch, sha="abc1234", porcelain="")
    lines = _proof_only_output(monkeypatch, capsys)

    assert lines[-1] == f"code: abc1234 (clean) · {cli.CODE_ROOT}", (
        f"the LAST line is not the code line: {lines[-3:]}"
    )


def test_a_dirty_tree_says_how_many_paths(monkeypatch, capsys):
    _patch_git(
        monkeypatch, sha="abc1234",
        porcelain=" M src/cobalt/db_migrations/cli.py\n?? scratch/notes.md\n",
    )
    lines = _proof_only_output(monkeypatch, capsys)

    assert lines[-1] == f"code: abc1234 (DIRTY: 2 path(s)) · {cli.CODE_ROOT}", lines[-1]


def test_a_git_failure_is_unknown_and_never_fails_the_proof(monkeypatch, capsys):
    """L1: `UNKNOWN` is explicit. It is NOT a plausible value, and it is
    not this command's job to refuse it — the deploy gate does that."""
    _patch_git(monkeypatch, raises=RuntimeError("not a git repository"))
    lines = _proof_only_output(monkeypatch, capsys)  # returns => did not raise

    assert lines[-1].startswith("code: UNKNOWN — "), lines[-1]
    assert "not a git repository" in lines[-1]


def test_the_forward_path_prints_the_same_line_after_its_proof_table(
    monkeypatch, capsys
):
    _patch_git(monkeypatch, sha="deadbee", porcelain="")
    recorder = _StatementRecorder()

    def _table(*a, **k):
        print("<proof table>")
        return 0

    _offline_migrate(monkeypatch, recorder, print_proof=_table)

    lines = [line for line in capsys.readouterr().out.splitlines() if line.strip()]
    assert lines.index("<proof table>") < lines.index(
        f"code: deadbee (clean) · {cli.CODE_ROOT}"
    ), f"the code line does not follow the proof table: {lines}"
    assert lines[-1] == f"code: deadbee (clean) · {cli.CODE_ROOT}"


def test_the_code_root_is_the_package_not_the_current_directory():
    """A deploy hub `cd`s; the answer must not follow it. `CODE_ROOT` is
    derived from this module's own file, so it names the checkout the
    RUNNING `cobalt` package was imported from."""
    assert cli.CODE_ROOT == Path(cli.__file__).resolve().parents[3]
    assert (cli.CODE_ROOT / "src" / "cobalt" / "db_migrations" / "cli.py").exists()


def test_the_real_helper_imports_and_produces_a_line():
    """L3: there is no third git helper — `_code_line` imports an EXISTING
    one. This runs it for real against this checkout (no database, no
    network), which is what proves the import carries no cycle and no
    side effect."""
    line = cli._code_line()

    assert line.startswith("code: "), line
    assert str(cli.CODE_ROOT) in line
    assert ("(clean)" in line) or ("(DIRTY: " in line), line


# ---------------------------------------------------------------------
# 12. THE TRIBUNAL'S CARRIED ITEMS (R1/R11, 2026-09-19 DB run)
# ---------------------------------------------------------------------
#
# NUMBERED 12, NOT 10. `25-packet/db-run-spec.md` §A says "place it in a
# new section after §9, e.g. '10. …'" — but §10 (`lock_timeout` on the
# migrate transaction) and §11 (the code line) already exist in this
# file, written by round 1 of the same day. The CODE wins over the
# packet; this section is appended after §11 with the next free number,
# and the difference is an ESCALATE line in the DB-run report.
#
# WHAT R1/R11 ASKED. `cmd_migrate` issues `SET LOCAL lock_timeout` AFTER
# the BEFORE probe, deliberately, because the build that wrote it was
# offline and could not settle whether a bare `SET` is "the statement
# that takes the REPEATABLE READ snapshot" (`cli.py`, `cmd_migrate`'s
# docstring). The price of that placement is that the BEFORE PROBE ITSELF
# RUNS WITH NO LOCK CEILING. `cobalt_dev` is reachable now, so the
# question is settled here by experiment rather than by citation.
#
# ONE PLACE THE SPEC'S EXPERIMENT DIFFERS FROM THE CODE, and it matters
# enough to split the question in two. The spec's step 1 says the
# connection comes back from `cli._connect` with "no statement has run on
# it yet". It has: `_connect` calls `_assert_utf8`, which runs `SHOW
# server_encoding` (`cli.py:489`) — `cmd_migrate`'s own docstring says so
# ("Today the first statement of the transaction is `SHOW
# server_encoding`"). So a single test through `cli._connect` cannot tell
# a snapshot taken by `SHOW` from one taken by `SET LOCAL`. Both are
# asked, separately:
#
#   (k) `cli._connect` ALONE — does the `SHOW` fix the snapshot?
#   (l) `cli._connect` + a bare `SET LOCAL lock_timeout` — does the `SET`
#       fix it?
#
# THE MECHANISM, both times: session B reads the target row's `xmin`,
# commits a row-version-only UPDATE (`_touch_a_job_row`'s cleanup-free
# `SET last_result = last_result`, which changes `xmin` and no VALUE, so
# the table's digest and `cobalt_dev`'s content are untouched), and reads
# `xmin` again. Session A then runs its FIRST real query against that
# row. The `xmin` A sees names the snapshot A got: B's NEW one means the
# snapshot had not been taken yet, the OLD one means it had.


def _jobs_rel(conn) -> sql.Identifier:
    """`<schema>.cobalt_jobs`, resolved on a connection OTHER than the one
    under test.

    `_rel` runs a catalog query, and a catalog query is a statement: run
    on session A it would be A's first statement and could take the very
    snapshot these two tests are trying to time. Resolved once on session
    B and reused as a literal identifier, session A's first statement is
    the `SELECT` and nothing else.
    """
    return _rel(conn, JOBS_TABLE)


def _xmin_of_the_touched_row(conn, rel: sql.Identifier) -> str:
    """The `xmin` of the one `cobalt_jobs` row `_touch_a_job_row` updates.

    `xmin` rather than a value: the no-op UPDATE is the whole point —
    it writes a new row version while leaving every column as it was, so
    nothing needs cleaning up afterwards, and `xmin` is the only thing
    that moves. Read as text because an `xid` has no useful Python type.
    """
    row = conn.execute(
        sql.SQL(
            "SELECT xmin::text FROM {rel} "
            "WHERE label = (SELECT min(label) FROM {rel})"
        ).format(rel=rel)
    ).fetchone()
    assert row is not None, (
        f"{JOBS_TABLE} has no rows, so there is no row version to watch — "
        "run `cobalt db migrate` against this database first"
    )
    return row[0]


def _snapshot_experiment(*, send_set_local: bool) -> tuple[str, str, str]:
    """Run the (k)/(l) experiment once. Returns (before, after, seen).

    `before`/`after` are B's readings of the row's `xmin` either side of
    its own commit; `seen` is what A's FIRST real query reads. A never
    commits — it applied nothing and has nothing to keep.
    """
    other = db.connect_migration(env.DEV_DB_NAME)
    try:
        rel = _jobs_rel(other)
        xmin_before = _xmin_of_the_touched_row(other, rel)

        conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
        try:
            if send_set_local:
                # The statement under test, and NOTHING else: no table is
                # touched, which is exactly why it was unclear whether it
                # counts as the snapshot-taking statement.
                conn.execute("SET LOCAL lock_timeout = '5s'")
            _touch_a_job_row(other)
            xmin_after = _xmin_of_the_touched_row(other, rel)
            assert xmin_after != xmin_before, (
                "the other session's UPDATE did not write a new row version "
                f"({xmin_before} -> {xmin_after}), so this experiment has "
                "nothing to observe"
            )
            xmin_seen = _xmin_of_the_touched_row(conn, rel)
        finally:
            conn.rollback()
            conn.close()
    finally:
        other.close()
    return xmin_before, xmin_after, xmin_seen


@requires_db
def test_connects_show_server_encoding_does_not_take_the_snapshot():
    """(k) R1/R11, first half — proved on `cobalt_dev` 2026-09-19.

    `cli._connect` runs `SHOW server_encoding` before it hands the
    connection back. `SHOW` reads a GUC, not a table, and the result
    below says it does NOT acquire the transaction snapshot: a commit by
    another session AFTER `_connect` returned is still visible to this
    transaction's first real query.

    That is what makes (l) a separate question rather than the same one,
    and it is also the reason `cmd_migrate`'s old docstring could say the
    `SET LOCAL`'s position "cannot matter" while leaving the real
    question open.
    """
    xmin_before, xmin_after, xmin_seen = _snapshot_experiment(send_set_local=False)

    assert xmin_seen == xmin_after, (
        "`cli._connect`'s own `SHOW server_encoding` DID take the "
        f"transaction's REPEATABLE READ snapshot: the first real query read "
        f"xmin {xmin_seen}, the row version that existed before the other "
        f"session's commit ({xmin_before}), not the one after it "
        f"({xmin_after})."
    )


@requires_db
def test_a_bare_set_local_does_not_take_the_snapshot_either():
    """(l) R1/R11, the question itself — proved on `cobalt_dev` 2026-09-19.

    A bare `SET LOCAL lock_timeout`, issued on the real harness
    connection and followed by nothing, does NOT take the transaction's
    REPEATABLE READ snapshot: the first real query still sees a commit
    that landed after the `SET`.

    WHAT THIS SETTLES. Moving `SET LOCAL lock_timeout` ahead of the
    BEFORE probe in `cmd_migrate` cannot move the snapshot, because the
    `SET` does not take one — the BEFORE probe remains the statement that
    does, exactly as it is today. So the probe can be brought under the
    lock ceiling at no cost to the property the whole proof rests on
    (`test_a_commit_by_another_session_between_the_probes_is_invisible`,
    (a) above, is what would go red if that were wrong).
    """
    xmin_before, xmin_after, xmin_seen = _snapshot_experiment(send_set_local=True)

    assert xmin_seen == xmin_after, (
        "a bare `SET LOCAL lock_timeout` DID take the transaction's "
        f"REPEATABLE READ snapshot: the first real query read xmin "
        f"{xmin_seen}, the row version that existed before the other "
        f"session's commit ({xmin_before}), not the one after it "
        f"({xmin_after}). `SET LOCAL` must then stay where it is, AFTER "
        "the BEFORE probe — moving it would fix the snapshot one statement "
        "earlier than the probe that must define it."
    )


@requires_db
def test_the_instrument_can_see_a_snapshot_that_is_already_fixed():
    """(m) THE NEGATIVE CONTROL for (k) and (l).

    (k) and (l) both assert that session A sees the NEW row version. An
    assertion like that is only evidence if the OTHER outcome is
    reachable by the same instrument — otherwise "the snapshot was not
    taken" and "this test cannot see a snapshot" are the same passing
    test, and R1 would be closed on nothing (L35, L70).

    So: give session A a REAL query FIRST, which is the one thing that
    certainly does take the snapshot, and then run the identical
    sequence. A must now be pinned to the row version that existed
    before the other session's commit.
    """
    other = db.connect_migration(env.DEV_DB_NAME)
    try:
        rel = _jobs_rel(other)
        xmin_before = _xmin_of_the_touched_row(other, rel)

        conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
        try:
            # THE DIFFERENCE from (k)/(l), and the whole control: a real
            # query, before the other session commits anything.
            xmin_a_first = _xmin_of_the_touched_row(conn, rel)
            _touch_a_job_row(other)
            xmin_after = _xmin_of_the_touched_row(other, rel)
            xmin_a_second = _xmin_of_the_touched_row(conn, rel)
        finally:
            conn.rollback()
            conn.close()
    finally:
        other.close()

    assert xmin_a_first == xmin_before, (
        "session A's first real query did not read the row version that was "
        f"current when it ran: {xmin_a_first} vs {xmin_before}"
    )
    assert xmin_after != xmin_before, (
        "the other session's UPDATE did not write a new row version "
        f"({xmin_before} -> {xmin_after}), so this control observes nothing"
    )
    assert xmin_a_second == xmin_before, (
        "THE INSTRUMENT IS BLIND: another session committed a new row "
        f"version ({xmin_before} -> {xmin_after}) and session A, which had "
        f"already taken its REPEATABLE READ snapshot, read {xmin_a_second} "
        "instead of staying on the old one. Until this passes, (k) and (l) "
        "prove nothing about when the snapshot is taken."
    )


#: The server-side backstop for (n), and the reason (n) cannot hang the
#: suite. If `SET LOCAL lock_timeout` ever moves back BELOW the BEFORE
#: probe, the probe waits on the ACCESS EXCLUSIVE holder with no ceiling
#: of its own — so the server is given one, well above both the 2 s the
#: test asks for and the ~5.5 s a whole `_probe_all` pass costs on
#: `cobalt_dev` (measured 2026-09-19: `bars`, 1,043,443 rows, is 5.4 s of
#: it, and `bars` sorts BEFORE `cobalt_jobs`, so the covered probe pays
#: that before it ever reaches the blocked table). A regression then
#: FAILS this test in ~30 s instead of hanging the suite behind the lock.
PROBE_COVERAGE_BACKSTOP_S = 30

#: What (n) asks `cmd_migrate` for. Well under `LOCK_CEILING_S`, and far
#: enough under the backstop above that the two cannot be confused.
PROBE_COVERAGE_LOCK_TIMEOUT_S = 2


@requires_db
def test_a_blocked_before_probe_is_under_the_lock_ceiling_too(monkeypatch):
    """(n) R1/R11, what the move BUYS — the BEFORE probe now fails fast.

    Another session holds ACCESS EXCLUSIVE on `cobalt_jobs`, so the
    BEFORE probe's own ACCESS SHARE request cannot be granted. With the
    `SET LOCAL lock_timeout` issued ahead of the probe, the run must give
    up with the harness's `MigrationError` — through the
    `LockNotAvailable` path — instead of waiting on the holder.

    `_probe_all` IS NOT STUBBED, which is the entire point and the one
    thing that separates this test from (j)
    (`test_a_migration_that_cannot_get_its_lock_fails_in_about_a_second`,
    which stubs it and therefore pins the ceiling on `_apply` only). The
    real probe runs, reaches the locked table on its own, and waits there
    — under the ceiling.
    """
    # Held before `cli._connect` is monkeypatched below, because the AFTER
    # probe needs a REAL connection and the patch is still in force when it
    # runs (monkeypatch undoes at teardown, not mid-test).
    real_connect = cli._connect

    holder = db.connect_migration(env.DEV_DB_NAME)
    # NOT `db.connect_migration` for the probe: that connection is
    # AUTOCOMMIT, and `_probe` streams through a NAMED cursor, which
    # Postgres refuses outside a transaction block (`NoActiveSqlTransaction:
    # DECLARE CURSOR can only be used in transaction blocks`). `cli._connect`
    # is the harness's own read-only probe connection — the one
    # `--proof-only` uses.
    reader = real_connect(env.DEV_DB_NAME, allow_prod=False, read_only=True)
    try:
        rel = _rel(holder, JOBS_TABLE)
        before = cli._probe(reader, JOBS_TABLE)
        reader.rollback()
        reader.close()

        assert PROOF_TABLES.index("bars") < PROOF_TABLES.index(JOBS_TABLE), (
            "the probe order changed; the elapsed-time budget below was "
            f"measured with bars probed first: {PROOF_TABLES}"
        )

        holder.autocommit = False
        holder.execute(
            sql.SQL("LOCK TABLE {rel} IN ACCESS EXCLUSIVE MODE").format(rel=rel)
        )

        conn = real_connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)
        # Set BEFORE `cmd_migrate` touches the connection, so it is in
        # force for the probe either way. Not `LOCAL`: `cmd_migrate`'s own
        # `SET LOCAL lock_timeout` must remain the only LOCAL one, and
        # this transaction is rolled back, which discards this too.
        conn.execute(f"SET statement_timeout = '{PROBE_COVERAGE_BACKSTOP_S}s'")
        monkeypatch.setenv(env.ENV_VAR, env.DEV)
        monkeypatch.setattr(cli, "_connect", lambda *a, **k: conn)
        monkeypatch.setattr(cli, "_print_proof", lambda *a, **k: 0)
        args = argparse.Namespace(
            proof_only=False, rollback=False, down_to=None, allow_prod=False,
            lock_timeout_s=PROBE_COVERAGE_LOCK_TIMEOUT_S,
        )

        started = time.perf_counter()
        with pytest.raises(cli.MigrationError) as excinfo:
            cli.cmd_migrate(args)
        elapsed = time.perf_counter() - started
    finally:
        holder.rollback()
        holder.close()
        if not reader.closed:
            reader.rollback()
            reader.close()

    message = str(excinfo.value).lower()
    assert "could not get a lock" in message, (
        "the run failed, but not through the LockNotAvailable path — so this "
        f"says nothing about the probe being under the ceiling: {excinfo.value}"
    )
    assert "nothing was applied" in message, excinfo.value
    assert elapsed < LOCK_CEILING_S, (
        f"the BEFORE probe took {elapsed:.1f} s to give up against an ACCESS "
        f"EXCLUSIVE holder with --lock-timeout-s "
        f"{PROBE_COVERAGE_LOCK_TIMEOUT_S} — the ceiling is not reaching the "
        "probe. Budget: ~5.5 s for the probe passes that are NOT blocked "
        f"(bars is 5.4 s of it), then {PROBE_COVERAGE_LOCK_TIMEOUT_S} s on "
        f"{JOBS_TABLE}."
    )

    after_conn = real_connect(env.DEV_DB_NAME, allow_prod=False, read_only=True)
    try:
        after = cli._probe(after_conn, JOBS_TABLE)
    finally:
        after_conn.rollback()
        after_conn.close()
    assert cli._verdict(JOBS_TABLE, before, after) == "OK", (
        "a migration that failed on its BEFORE probe left the table changed: "
        f"rows {before['rows']} -> {after['rows']}, digest {before['digest']} "
        f"-> {after['digest']}"
    )
