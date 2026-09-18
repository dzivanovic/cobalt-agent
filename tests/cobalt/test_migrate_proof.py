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

Five groups:

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
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

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
    assert cli._digest_rows(iter(rows)) == expected, (
        f"{case}: the streamed fold does not produce the bytes "
        "string_agg(..., '|') would have produced"
    )


def test_no_rows_digests_the_empty_string():
    """The `coalesce(string_agg(...), '')` arm, which every empty table hits."""
    assert cli._digest_rows(iter([])) == hashlib.md5(b"").hexdigest()
    assert cli._digest_rows(iter([])) == "d41d8cd98f00b204e9800998ecf8427e"


def test_the_separator_goes_between_rows_and_never_after_the_last():
    """One row must digest the row alone — no trailing `|`."""
    assert cli._digest_rows(iter(["solo"])) == hashlib.md5(b"solo").hexdigest()
    assert cli._digest_rows(iter(["a", "b"])) == hashlib.md5(b"a|b").hexdigest()
    assert cli._digest_rows(iter(["a", "b"])) != hashlib.md5(b"a|b|").hexdigest()


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
