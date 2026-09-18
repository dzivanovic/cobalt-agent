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

Eight groups:

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
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

import psycopg
import pytest
from psycopg import sql

from cobalt import db, env
from cobalt.db_migrations import cli
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


def _concurrency_rel(conn) -> sql.Identifier:
    """`<schema>.cobalt_redactions`, wherever the migrations put it.

    Read from the catalog rather than hard-coded `system.`: these tests
    must not quietly pass on a database where the table has not moved.
    """
    schema = cli._schema_of(conn, CONCURRENCY_TABLE)
    assert schema is not None, (
        f"{CONCURRENCY_TABLE} is on none of {cli.SEARCHED_SCHEMAS} — run "
        "`cobalt db migrate` against this database first"
    )
    return sql.Identifier(schema, CONCURRENCY_TABLE)


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
    """
    other = db.connect_migration(env.DEV_DB_NAME)
    row_id = _insert_redaction(other, "snapshot-fix-e")
    reached: list[str] = []

    def _conflicting_apply(conn, paths):
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
        assert reached == ["other session committed"], (
            "the migration's UPDATE of a row another session had already "
            f"changed was allowed through: {reached}"
        )
        assert _hits(other, row_id) == 2, (
            "the migration's write survived a transaction that failed — the "
            "rollback path did not run"
        )
    finally:
        _delete_redaction(other, row_id)
        other.close()
