"""S2-P2 STEP-1 — migrations 0006 (system seam) and 0007 (user cards).

Two halves. The pure half reads the SQL files and the placement map and
needs no database: registration order, bounded rollback selection, every
new relation declared on exactly one side, idempotency guards (Astra
R1-3), `user_id NOT NULL` + FK + GUC default on every user table (L32,
ADR-0008), executable view bodies, and the proof harness's digest
exclusions covering every column 0007 adds.

The `requires_db` half is written here and run by the hub on `cobalt_dev`
(L41 interim): migrate twice, side-role ownership/grants/sequence use and
wrong-side refusal per new table (Astra R1-2), the card CHECKs and the one
open radar card index (R1-14), receipt immutability (R1-10), and a bounded
reverse + reapply on populated rows. Every DB test runs inside a
transaction that is rolled back.
"""

from __future__ import annotations

import os
import re

import psycopg
import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import (
    TABLE_DIGEST_EXCLUDED_COLUMNS,
    _apply,
    _rollback_paths,
)
from cobalt.db_migrations.placement import CREATED_TABLES, CREATED_VIEWS, PLACEMENT

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

SYSTEM_SQL = MIGRATIONS_DIR / "0006_radar_score.sql"
SYSTEM_ROLLBACK = MIGRATIONS_DIR / "0006_radar_score.rollback.sql"
USER_SQL = MIGRATIONS_DIR / "0007_radar_cards.sql"
USER_ROLLBACK = MIGRATIONS_DIR / "0007_radar_cards.rollback.sql"

SYSTEM_TABLES = {"radar_score_run", "radar_score", "desk_regime", "desk_packet", "desk_grade"}
USER_TABLES = {"card_dots", "card_dot_taps", "radar_score_receipt"}
SYSTEM_VIEWS = {"radar_board_v"}
USER_VIEWS = {"radar_cards_v", "shadow_agreement_v"}


def _code(path) -> str:
    """The SQL with `--` comment lines removed."""
    return "\n".join(
        line for line in path.read_text().splitlines() if not line.strip().startswith("--")
    )


def _created(text: str, schema: str) -> set[str]:
    pattern = rf"CREATE TABLE IF NOT EXISTS {re.escape(schema)}\.([a-z_]+)"
    return set(re.findall(pattern, text))


def _table_body(text: str, qualified: str) -> str:
    start = text.index(f"CREATE TABLE IF NOT EXISTS {qualified} (")
    depth, i = 0, text.index("(", start)
    for j in range(i, len(text)):
        if text[j] == "(":
            depth += 1
        elif text[j] == ")":
            depth -= 1
            if depth == 0:
                return " ".join(text[i:j + 1].split())
    raise AssertionError(f"unbalanced CREATE TABLE for {qualified}")


# ---------------------------------------------------------------------
# Registration and rollback selection
# ---------------------------------------------------------------------


def test_0006_and_0007_are_registered_forward_in_order():
    """ADJACENCY, not position (2026-09-19): P4's 0008/0009 and the
    archiver's 0010/0011 are appended after 0007, so `FORWARD` no longer
    ends here. What 0006/0007 need is to run in that order, with 0006's
    system seam before 0007's user cards that reference it."""
    # A position in FORWARD is not an identity — later sprints append. Assert
    # by name: 0006 is followed immediately by 0007.
    names = [p.name for p in FORWARD]
    assert "0006_radar_score.sql" in names, names
    start = names.index("0006_radar_score.sql")
    assert names[start:][:2] == ["0006_radar_score.sql", "0007_radar_cards.sql"]
    assert names.index("0007_radar_cards.sql") == names.index("0006_radar_score.sql") + 1
    for path in (SYSTEM_SQL, SYSTEM_ROLLBACK, USER_SQL, USER_ROLLBACK):
        assert path.exists(), path


def test_rollback_selects_every_newer_migration_then_0007_then_0006_newest_first():
    """The USER cards reverse before the SYSTEM seam they reference — an
    adjacency in REVERSE, and a suffix of each bounded selection. The
    newest four are named explicitly: P4's 0008/0009 and the archiver's
    0010/0011 both reverse before 0007."""
    newest_four = [
        "0013_tunables_slug_nullable.rollback.sql",  # the setups one build (R2-3 = B)
        "0011_archive_incidents.rollback.sql",
        "0010_archive_progress.rollback.sql",
        "0009_picks_missed.rollback.sql",
        "0008_radar_value_movers.rollback.sql",
    ]
    reverse_names = [p.name for p in REVERSE]
    assert reverse_names[:5] == newest_four
    assert (
        reverse_names.index("0006_radar_score.rollback.sql")
        == reverse_names.index("0007_radar_cards.rollback.sql") + 1
    )
    assert [p.name for p in _rollback_paths("0005")][:5] == newest_four
    assert [p.name for p in _rollback_paths("0005")][-2:] == [
        "0007_radar_cards.rollback.sql",
        "0006_radar_score.rollback.sql",
    ]
    assert [p.name for p in _rollback_paths("0006")][:5] == newest_four
    assert [p.name for p in _rollback_paths("0006")][-1:] == [
        "0007_radar_cards.rollback.sql"
    ]
    assert not any(
        p.name.startswith(("0005", "0004", "0003", "0002"))
        for p in _rollback_paths("0006")
    )


# ---------------------------------------------------------------------
# Placement: every new relation on exactly one side
# ---------------------------------------------------------------------


def test_placement_declares_the_new_tables_and_views_on_their_sides():
    for name in SYSTEM_TABLES | SYSTEM_VIEWS:
        assert PLACEMENT[name] is Side.SYSTEM, name
    for name in USER_TABLES | USER_VIEWS:
        assert PLACEMENT[name] is Side.USER, name
    assert SYSTEM_TABLES | USER_TABLES <= set(CREATED_TABLES)
    assert SYSTEM_VIEWS | USER_VIEWS == set(CREATED_VIEWS)
    assert not set(CREATED_VIEWS) & set(CREATED_TABLES)


def test_0006_creates_only_system_relations_and_0007_only_user_relations():
    system_text, user_text = _code(SYSTEM_SQL), _code(USER_SQL)
    assert _created(system_text, "system") == SYSTEM_TABLES
    assert _created(system_text, '"user"') == set()
    assert _created(user_text, '"user"') == USER_TABLES
    assert _created(user_text, "system") == set()
    assert set(re.findall(r"CREATE OR REPLACE VIEW system\.([a-z_]+)", system_text)) == SYSTEM_VIEWS
    assert set(re.findall(r'CREATE OR REPLACE VIEW "user"\.([a-z_]+)', user_text)) == USER_VIEWS


def test_every_new_relation_is_owned_by_its_side_role():
    system_text, user_text = _code(SYSTEM_SQL), _code(USER_SQL)
    for name in SYSTEM_TABLES:
        assert f"ALTER TABLE system.{name} OWNER TO cobalt_system" in system_text, name
        assert f"system.{name}_id_seq TO cobalt_system" in system_text, name
    for name in SYSTEM_VIEWS:
        assert f"ALTER VIEW system.{name} OWNER TO cobalt_system" in system_text, name
    for name in USER_TABLES:
        assert f'ALTER TABLE "user".{name} OWNER TO cobalt_user' in user_text, name
        assert f'"user".{name}_id_seq TO cobalt_user' in user_text, name
    for name in USER_VIEWS:
        assert f'ALTER VIEW "user".{name} OWNER TO cobalt_user' in user_text, name


def test_cross_side_references_are_granted_in_0006():
    text = _code(SYSTEM_SQL)
    assert "GRANT SELECT, REFERENCES ON system.radar_score TO cobalt_user" in text
    assert "GRANT SELECT, REFERENCES ON system.radar_score_run TO cobalt_user" in text
    assert "GRANT SELECT ON system.radar_board_v TO cobalt_user" in text


def test_every_user_table_carries_user_id_not_null_fk_and_guc_default():
    text = _code(USER_SQL)
    expected = re.compile(
        r"user_id\s+INTEGER\s+NOT\s+NULL\s+DEFAULT\s+\(current_setting\('cobalt\.trader_id'\)::int\)"
        r"\s+REFERENCES\s+\"user\"\.traders\(id\)"
    )
    for name in USER_TABLES:
        body = _table_body(text, f'"user".{name}')
        assert expected.search(body), f"{name}: user_id NOT NULL + FK + GUC default missing"
        assert not re.search(r"DEFAULT\s+\d", body.split("user_id", 1)[1].split(",", 1)[0])


# ---------------------------------------------------------------------
# Idempotency (Astra R1-3) and executable views
# ---------------------------------------------------------------------


@pytest.mark.parametrize("path", [SYSTEM_SQL, USER_SQL])
def test_forward_ddl_is_guarded_for_a_second_run(path):
    text = _code(path)
    assert not re.search(r"CREATE TABLE (?!IF NOT EXISTS)", text), "unguarded CREATE TABLE"
    assert not re.search(r"CREATE VIEW", text), "views must be CREATE OR REPLACE"
    assert not re.search(r"CREATE (UNIQUE )?INDEX (?!IF NOT EXISTS)", text)
    assert not re.search(r"ADD COLUMN (?!IF NOT EXISTS)", text)
    # Every ADD CONSTRAINT sits inside a DO block that checks pg_constraint.
    for match in re.finditer(r"ADD CONSTRAINT ([a-z_]+)", text):
        before = text[: match.start()]
        do_open = before.rfind("DO $")
        assert do_open != -1 and "pg_constraint" in text[do_open: match.start()], match.group(1)


@pytest.mark.parametrize("path", [SYSTEM_SQL, USER_SQL])
def test_views_have_executable_definitions(path):
    text = _code(path)
    assert "AS ..." not in text
    for body in re.findall(r"CREATE OR REPLACE VIEW [^\s]+ AS(.*?);", text, re.DOTALL):
        assert "SELECT" in body and "FROM" in body


def test_0006_widens_failed_stage_by_reading_the_constraint_from_the_catalog():
    text = _code(SYSTEM_SQL)
    assert "pg_constraint" in text and "failed_stage" in text
    assert "radar_pool_failed_stage_check" in text
    for stage in ("membership", "pool_row", "mirror", "bars", "evaluate"):
        assert f"'{stage}'" in text
    rollback = _code(SYSTEM_ROLLBACK)
    assert "failed_stage = 'evaluate'" in rollback
    assert "'evaluate'" not in rollback.split("ADD CONSTRAINT", 1)[1].split(";", 1)[0]


def test_radar_score_is_system_payload_only_no_trade_def_content_columns():
    """L32 / Astra R1-1: the system seam carries md5 only — no slug, no
    def text, no WHY, no settings content. Payload shape is closed in
    `cobalt.radar.seam`; this is the DDL half."""
    text = _code(SYSTEM_SQL)
    for table in ("radar_score", "radar_score_run"):
        body = _table_body(text, f"system.{table}")
        for forbidden in ("slug", "trade_def TEXT", " why ", "settings_snapshot", "definitions"):
            assert forbidden not in body, (table, forbidden)
    assert "trade_def_md5 TEXT NOT NULL" in _table_body(text, "system.radar_score")


def test_0007_card_checks_and_one_open_radar_card_index():
    text = _code(USER_SQL)
    assert "aset_sizings_manual_sized" in text
    assert "aset_sizings_radar_provenance" in text
    assert "aset_sizings_one_open_radar_card" in text
    index = text.split("aset_sizings_one_open_radar_card", 1)[1].split(";", 1)[0]
    assert "(pool_member_id, trade_def_slug, direction)" in index
    assert "origin = 'radar'" in index
    for state in ("WATCH", "ARMED", "TRIGGERED", "FILLED"):
        assert f"'{state}'" in index
    for terminal in ("CLOSED", "PASSED", "EXPIRED", "MISSED"):
        assert f"'{terminal}'" not in index


def test_receipt_and_taps_are_immutable_at_the_database():
    text = _code(USER_SQL)
    assert "radar_score_receipt_immutable" in text
    assert "card_dot_taps_append_only" in text
    for column in ("pool_unit JSONB NOT NULL", "pool_unit_sha256 TEXT NOT NULL",
                   "tunables_snapshot JSONB NOT NULL", "settings_snapshot JSONB NOT NULL",
                   "definitions_snapshot JSONB NOT NULL", "tap_versions JSONB NOT NULL",
                   "observations JSONB NOT NULL", "ordered_cohort JSONB NOT NULL",
                   "tie_policy TEXT NOT NULL"):
        assert column in _table_body(text, '"user".radar_score_receipt'), column
    assert "REFERENCES system.radar_score_run(id)" in _table_body(text, '"user".radar_score_receipt')


def test_0007_rollback_drops_dependents_before_columns_and_restores_not_null_last():
    text = _code(USER_ROLLBACK)
    order = [
        text.index('DROP VIEW IF EXISTS "user".shadow_agreement_v'),
        text.index('DROP VIEW IF EXISTS "user".radar_cards_v'),
        text.index("origin = 'radar'"),
        text.index('DROP TABLE IF EXISTS "user".card_dots'),
        text.index("DROP COLUMN IF EXISTS radar_score_id"),
        text.index("ALTER COLUMN grade SET NOT NULL"),
    ]
    assert order == sorted(order)


def test_digest_excludes_every_column_0007_adds_to_aset_sizings():
    text = _code(USER_SQL)
    added = set(re.findall(r"ADD COLUMN IF NOT EXISTS ([a-z_0-9]+)", text))
    assert added, "0007 adds columns to aset_sizings"
    assert added <= set(TABLE_DIGEST_EXCLUDED_COLUMNS["aset_sizings"])


# ---------------------------------------------------------------------
# requires_db — run by the hub on cobalt_dev
# ---------------------------------------------------------------------


def _migration_conn():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    return conn


@requires_db
def test_migrate_twice_is_idempotent_on_cobalt_dev():
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        _apply(conn, FORWARD)
        for name, side in CREATED_TABLES.items():
            schema = '"user"' if side is Side.USER else "system"
            assert conn.execute(
                "SELECT to_regclass(%s)", (f"{schema}.{name}",)
            ).fetchone()[0], name
    finally:
        conn.rollback()
        conn.close()


@requires_db
@pytest.mark.parametrize("name", sorted(SYSTEM_TABLES | USER_TABLES | SYSTEM_VIEWS | USER_VIEWS))
def test_owner_is_the_side_role(name, real_connect):
    conn = real_connect(side=Side.SYSTEM)
    side = PLACEMENT[name]
    row = conn.execute(
        """
        SELECT pg_get_userbyid(c.relowner) FROM pg_class c
          JOIN pg_namespace n ON n.oid = c.relnamespace
         WHERE n.nspname = %s AND c.relname = %s
        """,
        (side.schema, name),
    ).fetchone()
    assert row is not None, f"{name} missing — run `cobalt db migrate`"
    assert row[0] == side.role


@requires_db
def test_system_side_inserts_seam_rows_and_user_side_cannot(real_connect):
    sys_conn = real_connect(side=Side.SYSTEM)
    sys_conn.autocommit = False
    try:
        pool = sys_conn.execute("SELECT pool_key FROM radar_pool LIMIT 1").fetchone()
        if pool is None:
            sys_conn.execute(
                "INSERT INTO radar_pool (pool_key, state, session, members) "
                "VALUES ('p2_tenancy_probe', 'idle', 'rth', 0)"
            )
            pool = ("p2_tenancy_probe",)
        run_id = sys_conn.execute(
            "INSERT INTO radar_score_run (pool_key, scan_id, session, started_at, status, "
            "cards_enabled, evaluator_version, formula_sha256, tunables_sha256, settings_sha256, "
            "cohort_sha256) VALUES (%s, -1, 'rth', now(), 'running', false, 'probe', 'f', 't', 's', 'c') "
            "RETURNING id",
            pool,
        ).fetchone()[0]
        assert run_id > 0
        for table in ("desk_regime",):
            sys_conn.execute(
                f"INSERT INTO {table} (as_of, snapshot, snapshot_sha256, sources) "
                "VALUES (now(), '{}', 'x', '[]')"
            )
    finally:
        sys_conn.rollback()
    user_conn = real_connect(side=Side.USER)
    user_conn.autocommit = False
    try:
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            user_conn.execute(
                "INSERT INTO system.radar_score_run (pool_key, scan_id, session, started_at, "
                "status, cards_enabled, evaluator_version, formula_sha256, tunables_sha256, "
                "settings_sha256, cohort_sha256) VALUES ('x', -1, 'rth', now(), 'running', false, "
                "'p', 'f', 't', 's', 'c')"
            )
    finally:
        user_conn.rollback()


@requires_db
@pytest.mark.parametrize("name", sorted(USER_TABLES | USER_VIEWS))
def test_system_side_cannot_read_the_new_user_relations(name, real_connect):
    conn = real_connect(side=Side.SYSTEM)
    with pytest.raises(psycopg.errors.InsufficientPrivilege):
        conn.execute(f'SELECT count(*) FROM "user".{name}').fetchone()


@requires_db
@pytest.mark.parametrize("name", sorted(SYSTEM_TABLES | SYSTEM_VIEWS))
def test_user_side_reads_the_new_system_relations_qualified(name, real_connect):
    conn = real_connect(side=Side.USER)
    assert conn.execute(f"SELECT count(*) FROM system.{name}").fetchone()[0] >= 0


@requires_db
def test_new_user_tables_carry_user_id_not_null_with_guc_default(real_connect):
    conn = real_connect(side=Side.USER)
    rows = conn.execute(
        """
        SELECT table_name, is_nullable, column_default FROM information_schema.columns
         WHERE table_schema = 'user' AND column_name = 'user_id'
        """
    ).fetchall()
    found = {r[0]: (r[1], r[2]) for r in rows}
    for name in USER_TABLES:
        assert name in found, name
        nullable, default = found[name]
        assert nullable == "NO"
        assert "current_setting" in default and "cobalt.trader_id" in default


@requires_db
def test_card_checks_index_and_receipt_immutability_on_cobalt_dev():
    """Populated proof inside one rolled-back migration transaction: a
    manual card must be sized, a radar card must carry provenance, a
    second open radar card for the same (member, def, direction) is
    refused, a receipt cannot be updated, and the bounded reverse +
    reapply leaves manual rows intact."""
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        conn.execute("SELECT set_config('cobalt.trader_id', '1', true)")
        conn.execute(
            "INSERT INTO system.radar_pool (pool_key, state, session, members) "
            "VALUES ('p2_probe', 'idle', 'rth', 0) ON CONFLICT DO NOTHING"
        )
        member = conn.execute(
            "INSERT INTO system.radar_membership (pool_key, ticker, trade_date, first_seen_at, "
            "entered_at, source, sources, session, opened_scan_id, last_scan_id) VALUES "
            "('p2_probe', 'PRB', current_date, now(), now(), 'screen', '[]', 'rth', -9, -9) RETURNING id"
        ).fetchone()[0]
        run = conn.execute(
            "INSERT INTO system.radar_score_run (pool_key, scan_id, session, started_at, status, "
            "cards_enabled, evaluator_version, formula_sha256, tunables_sha256, settings_sha256, "
            "cohort_sha256) VALUES ('p2_probe', -9, 'rth', now(), 'running', true, 'probe', 'f', "
            "'t', 's', 'c') RETURNING id"
        ).fetchone()[0]
        score = conn.execute(
            "INSERT INTO system.radar_score (run_id, membership_id, ticker, trade_def_md5, "
            "evaluation, detail, desk_shadow, inputs_sha256) VALUES (%s, %s, 'PRB', 'md5', "
            "'formed', '{}', '{}', 'i') RETURNING id",
            (run, member),
        ).fetchone()[0]

        base = (
            "INSERT INTO \"user\".aset_sizings (ticker, direction, entry, stop, per_share_risk, "
            "session, state, origin, trade_def_slug, trade_def_md5, trigger_price, structural_stop, "
            "radar_score_id, scan_id, formula_sha256, tunables_sha256, settings_sha256, pool_member_id) "
            "VALUES ('PRB', 'long', 10, 9, 1, 'rth', 'WATCH', %s, 'probe-def', 'md5', 10, 9, %s, -9, "
            "'f', 't', 's', %s) RETURNING id"
        )
        conn.execute("SAVEPOINT manual_unsized")
        with pytest.raises(psycopg.errors.CheckViolation):
            conn.execute(base, ("manual", score, member))
        conn.execute("ROLLBACK TO SAVEPOINT manual_unsized")

        card = conn.execute(base, ("radar", score, member)).fetchone()[0]
        conn.execute("SAVEPOINT duplicate_open")
        with pytest.raises(psycopg.errors.UniqueViolation):
            conn.execute(base, ("radar", score, member))
        conn.execute("ROLLBACK TO SAVEPOINT duplicate_open")

        conn.execute("SAVEPOINT no_provenance")
        with pytest.raises(psycopg.errors.CheckViolation):
            conn.execute(
                "INSERT INTO \"user\".aset_sizings (ticker, direction, entry, stop, per_share_risk, "
                "session, state, origin) VALUES ('PRB', 'short', 10, 11, 1, 'rth', 'WATCH', 'radar')"
            )
        conn.execute("ROLLBACK TO SAVEPOINT no_provenance")

        receipt = conn.execute(
            "INSERT INTO \"user\".radar_score_receipt (run_id, pool_key, scan_id, evaluated_at, "
            "ordered_cohort, tie_policy, pool_unit, pool_unit_sha256, tunables_snapshot, "
            "settings_snapshot, definitions_snapshot, tap_versions, observations) VALUES "
            "(%s, 'p2_probe', -9, now(), '[]', 'rank_then_ticker', '{}', 'h', '[]', '{}', '{}', "
            "'{}', '[]') RETURNING id",
            (run,),
        ).fetchone()[0]
        conn.execute("SAVEPOINT receipt_update")
        with pytest.raises(psycopg.errors.RaiseException, match="immutable"):
            conn.execute(
                "UPDATE \"user\".radar_score_receipt SET tie_policy = 'x' WHERE id = %s", (receipt,)
            )
        conn.execute("ROLLBACK TO SAVEPOINT receipt_update")

        conn.execute(
            "INSERT INTO \"user\".card_dots (card_id, factor, position, source, tier, role) "
            "VALUES (%s, 'rvol', 1, 'cobalt', 'deterministic', 'shadow')",
            (card,),
        )
        assert conn.execute(
            "SELECT count(*) FROM \"user\".radar_cards_v WHERE card_id = %s", (card,)
        ).fetchone()[0] == 1

        manual_before = conn.execute(
            "SELECT count(*) FROM \"user\".aset_sizings WHERE origin = 'manual'"
        ).fetchone()[0]
        _apply(conn, _rollback_paths("0005"))
        assert conn.execute("SELECT to_regclass('system.radar_score')").fetchone()[0] is None
        assert conn.execute("SELECT to_regclass('\"user\".card_dots')").fetchone()[0] is None
        assert conn.execute(
            "SELECT count(*) FROM \"user\".aset_sizings WHERE origin = 'radar'"
        ).fetchone()[0] == 0
        assert conn.execute(
            "SELECT count(*) FROM \"user\".aset_sizings WHERE origin = 'manual'"
        ).fetchone()[0] == manual_before
        _apply(conn, [SYSTEM_SQL, USER_SQL])
        assert conn.execute("SELECT to_regclass('\"user\".radar_score_receipt')").fetchone()[0]
    finally:
        conn.rollback()
        conn.close()
