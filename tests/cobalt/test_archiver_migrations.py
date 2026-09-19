"""Chunk M — migrations 0010 `archive_progress` and 0011 `archive_incidents`.

Spec `ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §11. Both tables are
ADDITIVE and SYSTEM side (L32: market-data bookkeeping, nothing of one
trader's choice), and each rollback is a plain `DROP TABLE` of its own
table — no other object is touched.

WHY 0010/0011 AND NOT 0008/0009. `0008`/`0009` belonged to the then
unmerged branch `sprint-2/p4`, which shipped on 2026-09-19 (deploy 2);
this branch rebased onto it, so both sets now live in the registry in
numeric order — exactly what the gap note said the second lander would
do. The registry is an EXPLICIT ordered tuple
(`db_migrations/__init__.py`) and the tests below assert the
registration and the rollback SELECTION by numeric prefix, never by
position.

The `requires_db` half is written here and owed its first run on
`cobalt_dev` once `p4-verify-0919` releases the lane (L41 interim).
Everything above it is offline.
"""

from __future__ import annotations

import os
import re

import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import _apply, _rollback_paths
from cobalt.db_migrations.placement import CREATED_TABLES, PLACEMENT, side_of

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

PROGRESS_SQL = MIGRATIONS_DIR / "0010_archive_progress.sql"
PROGRESS_ROLLBACK = MIGRATIONS_DIR / "0010_archive_progress.rollback.sql"
INCIDENTS_SQL = MIGRATIONS_DIR / "0011_archive_incidents.sql"
INCIDENTS_ROLLBACK = MIGRATIONS_DIR / "0011_archive_incidents.rollback.sql"

NEW_TABLES = ("archive_progress", "archive_incidents")

#: `sprint-2/p4`'s own tables, created by 0008/0009, which now sit BELOW
#: this branch's pair in the united registry. Named here so the rollback
#: pins can say which bound owns what instead of asserting "mine only".
P4_TABLES = ("movers_daily", "picks", "missed")

#: §11: the five kinds. `regression` is v3's addition to v2's four.
INCIDENT_KINDS = ("gap", "restated", "stored_only", "empty_export", "regression")


def _code(path) -> str:
    """The SQL with `--` comment lines removed, so an assertion cannot
    pass on a sentence in a comment."""
    return "\n".join(
        line for line in path.read_text().splitlines() if not line.strip().startswith("--")
    )


def _regclass(conn, name: str):
    """`to_regclass` for a table in the schema `CREATED_TABLES` declares
    for it — the one place that mapping is turned into a qualified name."""
    schema = '"user"' if CREATED_TABLES[name] is Side.USER else "system"
    return conn.execute("SELECT to_regclass(%s)", (f"{schema}.{name}",)).fetchone()[0]


# ---------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------


def test_forward_ends_0008_0009_0010_0011():
    """The tail after the P4 rebase: P4's pair, then this branch's pair,
    in numeric order. The invariant is unchanged — 0010 and 0011 are the
    LAST two registered, and nothing of this branch's was displaced."""
    assert [p.name for p in FORWARD[-4:]] == [
        "0008_radar_value_movers.sql",
        "0009_picks_missed.sql",
        "0010_archive_progress.sql",
        "0011_archive_incidents.sql",
    ]


def test_reverse_begins_0011_0010_0009_0008():
    """The exact mirror of the tail above: this branch's pair reverses
    FIRST, then P4's."""
    assert [p.name for p in REVERSE[:4]] == [
        "0011_archive_incidents.rollback.sql",
        "0010_archive_progress.rollback.sql",
        "0009_picks_missed.rollback.sql",
        "0008_radar_value_movers.rollback.sql",
    ]


def test_each_new_migration_has_its_rollback_and_both_are_registered():
    for path in (PROGRESS_SQL, PROGRESS_ROLLBACK, INCIDENTS_SQL, INCIDENTS_ROLLBACK):
        assert path.exists(), path
    assert PROGRESS_SQL in FORWARD and INCIDENTS_SQL in FORWARD
    assert PROGRESS_ROLLBACK in REVERSE and INCIDENTS_ROLLBACK in REVERSE


def test_rollback_down_to_0009_undoes_this_branch_alone_and_0007_also_reaches_p4():
    """The bound the operator actually runs to undo THIS branch is
    `--down-to 0009`: after the P4 rebase that is the boundary which
    selects exactly this branch's two files and stops. `--down-to 0007`
    is no longer that bound — it correctly reaches P4's pair as well,
    because selection is by numeric prefix and P4 now sits between.
    Both are pinned so neither can drift."""
    assert [p.name for p in _rollback_paths("0009")] == [
        "0011_archive_incidents.rollback.sql",
        "0010_archive_progress.rollback.sql",
    ]
    assert [p.name for p in _rollback_paths("0007")] == [
        "0011_archive_incidents.rollback.sql",
        "0010_archive_progress.rollback.sql",
        "0009_picks_missed.rollback.sql",
        "0008_radar_value_movers.rollback.sql",
    ]


def test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it():
    """The gap of 0008/0009 is CLOSED — P4 shipped and this branch
    rebased onto it. The invariant underneath the old gap test survives
    and is what is pinned here: the registry is an EXPLICIT ordered list,
    its numbers run 1…11 contiguously with no duplicate, and REVERSE is
    FORWARD reversed — minus 0001, which is deliberately never reversed
    (`db_migrations/__init__.py`). Selection stays by numeric prefix,
    never by position."""
    numbers = [int(p.name.split("_", 1)[0]) for p in FORWARD]
    assert numbers == sorted(numbers), "FORWARD must be in numeric order"
    assert len(numbers) == len(set(numbers)), f"duplicate migration number in {numbers}"
    assert numbers == list(range(1, 12)), f"1…11 contiguous, got {numbers}"
    assert numbers[-2:] == [10, 11], "this branch's pair is still the tail"
    reverse_numbers = [int(p.name.split("_", 1)[0]) for p in REVERSE]
    assert reverse_numbers == sorted(reverse_numbers, reverse=True)
    assert reverse_numbers == [n for n in reversed(numbers) if n != 1], (
        "REVERSE must be FORWARD reversed, 0001 excepted"
    )


# ---------------------------------------------------------------------
# Placement — both SYSTEM (L32)
# ---------------------------------------------------------------------


@pytest.mark.parametrize("table", NEW_TABLES)
def test_both_tables_are_declared_system_side(table):
    assert side_of(table) is Side.SYSTEM
    assert PLACEMENT[table] is Side.SYSTEM
    # Created by a database-wide migration on its final side, so the
    # migrate proof carries it and a rollback's DROP reads as DROPPED.
    assert CREATED_TABLES[table] is Side.SYSTEM


# ---------------------------------------------------------------------
# 0010 — archive_progress
# ---------------------------------------------------------------------


def test_progress_carries_its_primary_key_and_the_check():
    code = _code(PROGRESS_SQL)
    assert "CREATE TABLE IF NOT EXISTS system.archive_progress" in code
    assert "PRIMARY KEY (ticker, interval)" in code
    assert re.search(r"CHECK\s*\(\s*archived_through\s*<=\s*export_newest\s*\)", code), (
        "§11: archived_through can never be newer than the export it came from"
    )


@pytest.mark.parametrize(
    "column",
    [
        "ticker",
        "interval",
        "archived_through",
        "export_oldest",
        "export_newest",
        "raw_export_newest",
        "fetch_started_at",
        "bootstrap_at",
        "run_id",
        "updated_at",
    ],
)
def test_progress_carries_every_column_the_design_names(column):
    assert re.search(rf"^\s+{column}\s", _code(PROGRESS_SQL), re.M), column


def test_progress_nullability_matches_the_design():
    code = _code(PROGRESS_SQL)
    for column in (
        "archived_through",
        "export_oldest",
        "export_newest",
        "fetch_started_at",
        "bootstrap_at",
        "run_id",
        "updated_at",
    ):
        assert re.search(rf"^\s+{column}\s+\w+(\(.*\))?\s+NOT NULL", code, re.M), column
    # The ONE diagnostic column is deliberately nullable: a vendor export
    # with no parseable raw bound must still write progress.
    assert not re.search(r"^\s+raw_export_newest\s+\S+\s+NOT NULL", code, re.M)


def test_progress_rollback_drops_only_its_own_table():
    code = _code(PROGRESS_ROLLBACK)
    assert "DROP TABLE IF EXISTS system.archive_progress" in code
    assert code.count("DROP") == 1, "additive migration, additive rollback"
    assert "archive_incidents" not in code
    assert "bars" not in code and "radar_pool" not in code


# ---------------------------------------------------------------------
# 0011 — archive_incidents
# ---------------------------------------------------------------------


def test_incidents_carries_the_five_kinds_and_nothing_else():
    code = _code(INCIDENTS_SQL)
    assert "CREATE TABLE IF NOT EXISTS system.archive_incidents" in code
    match = re.search(r"kind\s+TEXT\s+NOT NULL\s+CHECK\s*\(\s*kind\s+IN\s*\(([^)]*)\)", code)
    assert match, "the kind CHECK is the domain; it must be in the DDL"
    kinds = {part.strip().strip("'") for part in match.group(1).split(",")}
    assert kinds == set(INCIDENT_KINDS)


def test_incidents_has_the_partial_unique_index_on_unresolved_rows():
    """§11: ONE unresolved row per (kind, ticker, interval, range_start) —
    a recurring night refreshes `last_seen_at`, it never duplicates."""
    code = _code(INCIDENTS_SQL)
    index = re.search(
        r"CREATE UNIQUE INDEX[^;]*archive_incidents[^;]*;", code, re.S
    )
    assert index, "no unique index on archive_incidents"
    body = " ".join(index.group(0).split())
    assert "(kind, ticker, interval, range_start)" in body
    assert "WHERE resolved_at IS NULL" in body
    # Tribunal round 1, F7. `NULLS NOT DISTINCT` (pg15+; this install is
    # pg16) is LOAD-BEARING, not tidiness: an `empty_export` incident has
    # no span, so its `range_start` is NULL, and under the DEFAULT rule
    # every NULL is distinct from every other — a target failing empty
    # for a month would open thirty rows for one condition and the
    # heartbeat's "oldest kind" detail would be meaningless. The clause
    # is in the SQL; until this round nothing said it had to stay.
    assert "NULLS NOT DISTINCT" in body, (
        "the partial unique index lost NULLS NOT DISTINCT — an "
        "`empty_export` incident (range_start IS NULL) would duplicate on "
        f"every run instead of refreshing: {body}"
    )


@pytest.mark.parametrize(
    "column",
    [
        "id",
        "kind",
        "ticker",
        "interval",
        "range_start",
        "range_end",
        "first_seen_at",
        "last_seen_at",
        "detail",
        "resolved_at",
        "resolved_by",
        "run_id",
    ],
)
def test_incidents_carries_every_column_the_design_names(column):
    assert re.search(rf"^\s+{column}\s", _code(INCIDENTS_SQL), re.M), column


def test_incidents_id_is_a_bigserial_primary_key():
    code = _code(INCIDENTS_SQL)
    assert re.search(r"^\s+id\s+BIGSERIAL\s+PRIMARY KEY", code, re.M)


def test_incidents_detail_is_a_json_object():
    assert "jsonb_typeof(detail) = 'object'" in _code(INCIDENTS_SQL)


def test_incidents_rollback_drops_only_its_own_table():
    code = _code(INCIDENTS_ROLLBACK)
    assert "DROP TABLE IF EXISTS system.archive_incidents" in code
    assert code.count("DROP") == 1
    assert "archive_progress" not in code


# ---------------------------------------------------------------------
# Ownership and grants — 0006's pattern for the system role, and an
# explicit REVOKE of everything from cobalt_user (cto-2026-09-19 R25)
# ---------------------------------------------------------------------


@pytest.mark.parametrize("path,table", [(PROGRESS_SQL, "archive_progress"), (INCIDENTS_SQL, "archive_incidents")])
def test_each_table_is_owned_by_the_system_role(path, table):
    assert f"ALTER TABLE system.{table} OWNER TO cobalt_system;" in _code(path)


@pytest.mark.parametrize("path", [PROGRESS_SQL, INCIDENTS_SQL, PROGRESS_ROLLBACK, INCIDENTS_ROLLBACK])
def test_nothing_is_granted_to_cobalt_user(path):
    """§11: `cobalt_user` is granted nothing on either table. The user
    side has no business reading the archiver's bookkeeping, and a
    wrong-side query must fail loud (L32 tenancy).

    The role's NAME now appears in the two forward files: `cto-2026-09-19`
    R25 ruled an explicit `REVOKE` (pinned below), and a REVOKE has to
    name the role it takes the privilege from. What must stay absent is a
    grant in its direction, so this test pins the DIRECTION rather than
    the bare string. The rollbacks name the role not at all.
    """
    code = _code(path)
    assert "TO cobalt_user" not in code
    if path in (PROGRESS_ROLLBACK, INCIDENTS_ROLLBACK):
        assert "cobalt_user" not in code


@pytest.mark.parametrize(
    "path,table", [(PROGRESS_SQL, "archive_progress"), (INCIDENTS_SQL, "archive_incidents")]
)
def test_each_table_revokes_everything_from_cobalt_user(path, table):
    """`cto-2026-09-19` R25 ("B"), from the DB run's DB-1: 0001's blanket
    `GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user`
    (`0001_schemas.sql:124`) and its default-privilege twin (`:149-151`)
    reach every table schema `system` gains later, these two included — so
    §11's "granted nothing" is only true if the migration says so out loud.

    `REVOKE ALL`, not `REVOKE SELECT`: §11's word is "nothing", and no
    other privilege is granted today for the wider form to cost anything.
    """
    assert f"REVOKE ALL ON system.{table} FROM cobalt_user;" in _code(path)


@pytest.mark.parametrize(
    "path,table", [(PROGRESS_SQL, "archive_progress"), (INCIDENTS_SQL, "archive_incidents")]
)
def test_the_revoke_comes_after_the_table_exists(path, table):
    """Postgres errors on a REVOKE naming a relation the script has not
    created yet, so the ORDER is the invariant, not only the presence."""
    code = _code(path)
    assert code.index(f"CREATE TABLE IF NOT EXISTS system.{table}") < code.index(
        f"REVOKE ALL ON system.{table} FROM cobalt_user;"
    )


def test_the_incident_sequence_is_also_revoked_from_cobalt_user():
    """`id BIGSERIAL PRIMARY KEY` (`0011_archive_incidents.sql:49`) creates
    `archive_incidents_id_seq` as part of the `CREATE TABLE`, and
    `0001_schemas.sql:152-154` default-grants SELECT on a new sequence to
    `cobalt_user` exactly as `:149-151` does for a new table. 0011's own
    comment says "NOTHING is granted to `cobalt_user`", so the sequence is
    revoked too rather than the comment narrowed to the table alone.
    """
    code = _code(INCIDENTS_SQL)
    assert "REVOKE ALL ON SEQUENCE system.archive_incidents_id_seq FROM cobalt_user;" in code
    assert code.index("CREATE TABLE IF NOT EXISTS system.archive_incidents") < code.index(
        "REVOKE ALL ON SEQUENCE system.archive_incidents_id_seq"
    )


def test_the_incident_sequence_is_granted_to_the_system_role():
    """0006's pattern, line for line (Astra R1-2): a BIGSERIAL's sequence
    is granted explicitly, never assumed from default privileges."""
    assert (
        "GRANT USAGE, SELECT ON SEQUENCE system.archive_incidents_id_seq TO cobalt_system;"
        in _code(INCIDENTS_SQL)
    )


@pytest.mark.parametrize("path", [PROGRESS_SQL, INCIDENTS_SQL])
def test_both_migrations_are_idempotent(path):
    """A second `cobalt db migrate` is a no-op (Astra R1-3)."""
    code = _code(path)
    for statement in re.findall(r"CREATE (TABLE|UNIQUE INDEX|INDEX)([^;]*);", code):
        assert "IF NOT EXISTS" in statement[1], statement


@pytest.mark.parametrize("path", [PROGRESS_SQL, INCIDENTS_SQL])
def test_neither_migration_touches_bars_or_any_existing_object(path):
    """ADDITIVE means additive: `system.bars` (columns, PK, indexes) is
    explicitly out of scope (§1 non-goals) and so is every other table."""
    code = _code(path)
    for forbidden in ("ALTER TABLE system.bars", "DROP ", "UPDATE ", "DELETE ", "radar_pool"):
        assert forbidden not in code, f"{path.name} contains {forbidden!r}"


# ---------------------------------------------------------------------
# requires_db — WRITTEN HERE, first run owed on cobalt_dev
# ---------------------------------------------------------------------


def _migration_conn():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    return conn


@requires_db
def test_forward_creates_both_tables_on_the_system_side():
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        for table in NEW_TABLES:
            assert conn.execute(
                "SELECT to_regclass(%s)", (f"system.{table}",)
            ).fetchone()[0], table
            assert conn.execute(
                "SELECT to_regclass(%s)", (f'"user".{table}',)
            ).fetchone()[0] is None, f"{table} must not exist user-side"
    finally:
        conn.rollback()
        conn.close()


@requires_db
def test_migrate_twice_is_idempotent_for_the_two_new_tables():
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        _apply(conn, FORWARD)
        for table in NEW_TABLES:
            assert conn.execute(
                "SELECT to_regclass(%s)", (f"system.{table}",)
            ).fetchone()[0], table
    finally:
        conn.rollback()
        conn.close()


@requires_db
def test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4():
    """The `requires_db` sibling of the registry pin above, applied to a
    real database instead of to `FORWARD`/`REVERSE`.

    It was written while this branch was the only unmerged one and it
    asserted that `--down-to 0007` was THIS branch's operator-undo bound.
    After the P4 rebase that is false in exactly the way its five offline
    siblings were: `0008`/`0009` now sit BELOW `0010`/`0011`, so a
    rollback to `0007` correctly also reverses P4's pair. `48` §4.1 could
    not see it because that table was built from an OFFLINE run, and an
    offline run SKIPS every `requires_db` test.

    Rewritten, never weakened: it asserts what is now true — `--down-to
    0007` drops all of P4's tables as well as this branch's two — and it
    keeps the invariant the pin existed to protect by asserting the
    archiver's own bound beside it: `--down-to 0009` drops EXACTLY
    `archive_progress` and `archive_incidents` and leaves P4's tables
    standing.
    """
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        survivors = {
            name
            for name in CREATED_TABLES
            if name not in NEW_TABLES and name not in P4_TABLES and _regclass(conn, name)
        }

        # (1) THE ARCHIVER'S OWN BOUND: `--down-to 0009` is this branch alone.
        _apply(conn, _rollback_paths("0009"))
        for table in NEW_TABLES:
            assert _regclass(conn, table) is None, f"{table} survived its own rollback"
        for name in P4_TABLES:
            assert _regclass(conn, name), (
                f"{name} was dropped by --down-to 0009, which does not own it"
            )
        for name in survivors:
            assert _regclass(conn, name), (
                f"{name} was dropped by a rollback that does not own it"
            )
        _apply(conn, FORWARD)

        # (2) `--down-to 0007` REACHES P4 TOO, and stops there.
        _apply(conn, _rollback_paths("0007"))
        for table in (*NEW_TABLES, *P4_TABLES):
            assert _regclass(conn, table) is None, (
                f"{table} survived --down-to 0007, which reverses everything above 0007"
            )
        for name in survivors:
            assert _regclass(conn, name), (
                f"{name} was dropped by a rollback that does not own it"
            )

        # ...and forward again lands back where it started.
        _apply(conn, FORWARD)
        for table in (*NEW_TABLES, *P4_TABLES):
            assert _regclass(conn, table), table
    finally:
        conn.rollback()
        conn.close()


@requires_db
@pytest.mark.parametrize("table", NEW_TABLES)
def test_owner_is_the_system_role(table, real_connect):
    conn = real_connect(side=Side.SYSTEM)
    row = conn.execute(
        """
        SELECT pg_get_userbyid(c.relowner) FROM pg_class c
          JOIN pg_namespace n ON n.oid = c.relnamespace
         WHERE n.nspname = %s AND c.relname = %s
        """,
        (Side.SYSTEM.schema, table),
    ).fetchone()
    assert row is not None, f"{table} missing — run `cobalt db migrate`"
    assert row[0] == Side.SYSTEM.role


@requires_db
@pytest.mark.parametrize("table", NEW_TABLES)
def test_the_user_role_has_no_grant_on_either_table(table, real_connect):
    conn = real_connect(side=Side.SYSTEM)
    row = conn.execute(
        "SELECT has_table_privilege('cobalt_user', %s, 'SELECT')",
        (f"system.{table}",),
    ).fetchone()
    assert row[0] is False, f"cobalt_user can read system.{table}"


@requires_db
def test_the_check_refuses_progress_past_its_own_export(real_connect):
    conn = real_connect(side=Side.SYSTEM)
    conn.autocommit = False
    try:
        with pytest.raises(Exception) as e:
            conn.execute(
                "INSERT INTO archive_progress (ticker, interval, archived_through, "
                "export_oldest, export_newest, fetch_started_at, bootstrap_at, run_id, "
                "updated_at) VALUES ('TESTARCH', 'i5', now(), now() - interval '1 day', "
                "now() - interval '1 hour', now(), now(), 'probe', now())"
            )
        assert "archived_through" in str(e.value) or "check" in str(e.value).lower()
    finally:
        conn.rollback()


@requires_db
def test_one_unresolved_incident_per_key_then_a_second_after_resolution(real_connect):
    conn = real_connect(side=Side.SYSTEM)
    conn.autocommit = False
    try:
        insert = (
            "INSERT INTO archive_incidents (kind, ticker, interval, range_start, "
            "range_end, first_seen_at, last_seen_at, detail, run_id) VALUES "
            "('gap', 'TESTARCH', 'i5', '2026-09-01T00:00:00Z', '2026-09-02T00:00:00Z', "
            "now(), now(), '{}', 'probe') RETURNING id"
        )
        first = conn.execute(insert).fetchone()[0]
        with pytest.raises(Exception):
            conn.execute(insert)
        conn.rollback()
        first = conn.execute(insert).fetchone()[0]
        conn.execute(
            "UPDATE archive_incidents SET resolved_at = now(), resolved_by = 'probe' "
            "WHERE id = %s",
            (first,),
        )
        # Resolved, so the partial index no longer covers it: the same key
        # may open again.
        assert conn.execute(insert).fetchone()[0] != first
    finally:
        conn.rollback()


@requires_db
def test_the_kind_domain_is_enforced_by_the_database(real_connect):
    conn = real_connect(side=Side.SYSTEM)
    conn.autocommit = False
    try:
        with pytest.raises(Exception):
            conn.execute(
                "INSERT INTO archive_incidents (kind, ticker, interval, first_seen_at, "
                "last_seen_at, detail, run_id) VALUES ('made_up', 'TESTARCH', 'i5', "
                "now(), now(), '{}', 'probe')"
            )
    finally:
        conn.rollback()
