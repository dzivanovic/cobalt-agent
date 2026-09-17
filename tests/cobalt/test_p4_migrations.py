"""S2-P4 STEP-1 — migrations 0008 (system) and 0009 (user).

Offline tests read the registry, the placement map and the SQL text.
`requires_db` tests run on `cobalt_dev` through the migration connection,
inside one transaction that is always rolled back (DDL is transactional),
and switch roles with the ONE `db.apply_side` so the grants that bite are
the side roles', not the superuser's.

Both merge orders (plan STEP-1, Astra R1-1/R1-3): P2's 0006/0007 are not
in this tree (P2 not merged — hub report STEP-0). The P2-before-P4 order is
exercised by adding P2's `aset_sizings.card_score`/`conviction` columns
before 0008/0009; the P4-before-P2 order by adding them after. The lint
test proves 0008/0009 name nothing of P2's, which is the property that
makes either order safe. The hub reruns these on the rebased tree.
"""

from __future__ import annotations

import os
import re

import psycopg
import pytest

from cobalt import db, env, tenant
from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import (
    DIGEST_EXCLUDED_COLUMNS,
    _apply,
    _migration_version,
    _probe,
    _rollback_paths,
)
from cobalt.db_migrations.placement import (
    CREATED_TABLES,
    DECLARED_TABLES,
    PLACEMENT,
    side_of,
)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)

FWD_0008 = MIGRATIONS_DIR / "0008_radar_value_movers.sql"
FWD_0009 = MIGRATIONS_DIR / "0009_picks_missed.sql"
REV_0008 = MIGRATIONS_DIR / "0008_radar_value_movers.rollback.sql"
REV_0009 = MIGRATIONS_DIR / "0009_picks_missed.rollback.sql"

#: Names that belong to S2-P2's 0006/0007 seam. P4's SQL must name none.
P2_SEAM_NAMES = (
    "radar_score", "radar_score_run", "radar_board_v", "desk_regime",
    "desk_packet", "desk_grade", "card_dots", "card_dot_taps",
    "radar_cards_v", "shadow_agreement_v", "radar_score_receipt",
)


def _sql(path) -> str:
    """The statements only — comments stripped, so prose cannot satisfy a test."""
    return "\n".join(
        line.split("--", 1)[0] for line in path.read_text().splitlines()
    )


# ---------------------------------------------------------------------
# Registry and placement
# ---------------------------------------------------------------------


def test_0008_0009_registered_forward_in_version_order_with_named_rollbacks():
    assert FWD_0008 in FORWARD and FWD_0009 in FORWARD
    assert REV_0008 in REVERSE and REV_0009 in REVERSE
    for path in (FWD_0008, FWD_0009, REV_0008, REV_0009):
        assert path.exists(), path
    versions = [_migration_version(p) for p in FORWARD]
    assert versions == sorted(versions), "FORWARD must stay version-ordered"
    reverse_versions = [_migration_version(p) for p in REVERSE]
    assert reverse_versions == sorted(reverse_versions, reverse=True)


def test_rollback_down_to_0007_reverses_0009_then_0008_only():
    """R1-23: the explicit boundary is `--down-to 0007`, numerically right
    whether or not P2's 0007 exists yet — it never reaches 0006/0007."""
    assert [p.name for p in _rollback_paths("0007")] == [
        "0009_picks_missed.rollback.sql",
        "0008_radar_value_movers.rollback.sql",
    ]
    assert [p.name for p in _rollback_paths("0008")] == [
        "0009_picks_missed.rollback.sql"
    ]


def test_placement_movers_daily_system_picks_and_missed_user():
    assert CREATED_TABLES["movers_daily"] is Side.SYSTEM
    assert CREATED_TABLES["picks"] is Side.USER
    assert CREATED_TABLES["missed"] is Side.USER
    assert "missed" not in DECLARED_TABLES, "missed is built now; it leaves DECLARED"
    assert side_of("picks") is Side.USER
    # Every table on exactly one side: the map is a dict, so a name twice
    # across its parts would silently collapse. Count the parts instead.
    from cobalt.db_migrations import placement as p

    parts = [
        p.MOVED_TABLES,
        p.SEEDED_TABLES,
        p.MODULE_TABLES,
        p.CREATED_TABLES,
        p.CREATED_VIEWS,
        p.DECLARED_TABLES,
    ]
    names = [name for part in parts for name in part]
    assert len(names) == len(set(names)) == len(PLACEMENT)


def test_0008_creates_only_system_objects_and_0009_only_user_tables():
    s8, s9 = _sql(FWD_0008), _sql(FWD_0009)
    assert "CREATE TABLE IF NOT EXISTS system.movers_daily" in s8
    assert "ALTER TABLE system.radar_membership" in s8
    assert '"user".' not in s8, "0008 is system-side only"
    assert 'CREATE TABLE IF NOT EXISTS "user".picks' in s9
    assert 'CREATE TABLE IF NOT EXISTS "user".missed' in s9
    assert "CREATE TABLE IF NOT EXISTS system." not in s9


def test_0008_0009_name_nothing_of_the_p2_seam_so_either_merge_order_applies():
    for path in (FWD_0008, FWD_0009, REV_0008, REV_0009):
        text = _sql(path)
        found = [n for n in P2_SEAM_NAMES if re.search(rf"\b{n}\b", text)]
        assert not found, f"{path.name} depends on P2 names {found}"


def test_0009_user_tables_carry_user_id_not_null_fk_and_guc_default():
    s9 = _sql(FWD_0009)
    for table in ("picks", "missed"):
        body = re.search(
            rf'CREATE TABLE IF NOT EXISTS "user"\.{table} \((.*?)\n\);', s9, re.S
        ).group(1)
        assert re.search(
            r"user_id\s+INTEGER NOT NULL\s+DEFAULT \(current_setting\('cobalt\.trader_id'\)::int\)"
            r'\s+REFERENCES "user"\.traders\(id\)',
            body,
        ), table
        assert not re.search(r"user_id[^,]*DEFAULT\s+\d", body), (
            f"{table}: a literal default invents an owner"
        )
        assert f'ALTER TABLE "user".{table} OWNER TO cobalt_user' in s9


def test_0008_owner_and_grants_for_movers_daily():
    """R1-2: SYSTEM owns it; USER reads it and may REFERENCE it (the FK
    from `"user".missed.mover_id`), plus the identity sequence grants."""
    s8 = _sql(FWD_0008)
    assert "ALTER TABLE system.movers_daily OWNER TO cobalt_system" in s8
    assert "GRANT SELECT, REFERENCES ON system.movers_daily TO cobalt_user" in s8
    assert "GRANT USAGE, SELECT ON SEQUENCE system.movers_daily_id_seq TO cobalt_system" in s8
    assert "GRANT SELECT ON SEQUENCE system.movers_daily_id_seq TO cobalt_user" in s8


def test_0008_rank_columns_are_constrained_and_digest_excluded():
    s8 = _sql(FWD_0008)
    assert "ADD COLUMN IF NOT EXISTS rank_metric TEXT CHECK (rank_metric IN ('volume','rvol'))" in s8
    assert "ADD COLUMN IF NOT EXISTS rank_value  NUMERIC(20,6)" in s8
    assert {"rank_metric", "rank_value"} <= set(DIGEST_EXCLUDED_COLUMNS)


def test_missed_carries_an_immutable_receipt_and_current_versioning():
    """R1-8 (receipt, never hash-only; no cobalt_jobs id) and R2-1/R3-1
    (run_seq, is_current, superseded_by; partial unique on is_current)."""
    s9 = _sql(FWD_0009)
    missed = re.search(r'CREATE TABLE IF NOT EXISTS "user"\.missed \((.*?)\n\);', s9, re.S).group(1)
    for column in (
        "receipt              JSONB NOT NULL",
        "inputs_sha256        TEXT NOT NULL",
        "replay_run_id        TEXT NOT NULL",
        "run_seq              INTEGER NOT NULL DEFAULT 1",
        "is_current           BOOLEAN NOT NULL DEFAULT true",
        'superseded_by        BIGINT REFERENCES "user".missed(id)',
        "retired_by_run_id    TEXT",
    ):
        assert column in missed, column
    assert "replay_job_id" not in missed
    index = re.search(
        r'CREATE UNIQUE INDEX IF NOT EXISTS missed_one_current_per_subject\s+ON "user"\.missed(.*?);',
        s9,
        re.S,
    ).group(1)
    assert "WHERE is_current" in index
    # R1-21: formations key on their trigger time and member.
    assert "formation_at" in index and "pool_member_id" in index
    assert "missed_one_per_subject " not in s9


def test_picks_record_the_replay_inputs_for_pool_and_score_rank():
    """R1-6 / L57: the rank cohort is stored, not only the rank."""
    s9 = _sql(FWD_0009)
    picks = re.search(r'CREATE TABLE IF NOT EXISTS "user"\.picks \((.*?)\n\);', s9, re.S).group(1)
    for column in (
        "card_id              BIGINT NOT NULL UNIQUE REFERENCES \"user\".aset_sizings(id)",
        "pool_member_id       BIGINT REFERENCES system.radar_membership(id)",
        "not_in_pool          BOOLEAN NOT NULL",
        "pool_basis           TEXT NOT NULL",
        "score_basis          TEXT NOT NULL",
        "score_inputs         JSONB NOT NULL",
    ):
        assert column in picks, column
    assert "CHECK (not_in_pool = (pool_member_id IS NULL))" in picks


def test_rollbacks_drop_only_their_own_objects():
    r8, r9 = _sql(REV_0008), _sql(REV_0009)
    assert set(re.findall(r"DROP TABLE IF EXISTS ([\w\".]+)", r9)) == {'"user".missed', '"user".picks'}
    assert set(re.findall(r"DROP TABLE IF EXISTS ([\w\".]+)", r8)) == {"system.movers_daily"}
    assert set(re.findall(r"DROP COLUMN IF EXISTS (\w+)", r8)) == {"rank_metric", "rank_value"}
    assert "DELETE" not in r8 + r9


# ---------------------------------------------------------------------
# Database proofs (hub-run on cobalt_dev)
# ---------------------------------------------------------------------


def _migration_conn():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    return conn


def _named(paths, prefix: str):
    return [p for p in paths if p.name.startswith(prefix)]


def _simulate_p2_card_columns(conn) -> None:
    """The two P2 columns P4 reads (`record_pick`), nothing else of P2."""
    conn.execute(
        'ALTER TABLE "user".aset_sizings ADD COLUMN IF NOT EXISTS card_score INTEGER, '
        "ADD COLUMN IF NOT EXISTS conviction NUMERIC(8,6)"
    )


def _seed_membership(conn, *, ticker: str, scan_id: int, value) -> int:
    conn.execute(
        "INSERT INTO system.radar_pool (pool_key,state,session,members) "
        "VALUES ('p4_proof','scanning','rth',1) ON CONFLICT (pool_key) DO NOTHING"
    )
    return conn.execute(
        "INSERT INTO system.radar_membership (pool_key,ticker,trade_date,first_seen_at,"
        "entered_at,source,sources,rank_at_entry,last_rank,session,opened_scan_id,last_scan_id,"
        "rank_metric,rank_value) VALUES ('p4_proof',%s,'2040-01-03','2040-01-03 15:00+00',"
        "'2040-01-03 15:00+00','test','[\"test\"]'::jsonb,1,1,'rth',%s,%s,'volume',%s) RETURNING id",
        (ticker, scan_id, scan_id, value),
    ).fetchone()[0]


@requires_db
@pytest.mark.parametrize("order", ["p2_before_p4", "p4_before_p2"])
def test_0008_0009_apply_twice_reverse_and_reapply_on_populated_membership(order):
    """R1-1: first-apply, second-apply, reverse/reapply on a populated
    `radar_membership` carrying non-null post-deploy values; the digest
    (which excludes the two new columns) never changes."""
    conn = _migration_conn()
    try:
        base = [p for p in FORWARD if _migration_version(p) < 8]
        _apply(conn, base)
        if order == "p2_before_p4":
            _simulate_p2_card_columns(conn)
        _apply(conn, [FWD_0008, FWD_0009])
        _seed_membership(conn, ticker="P4A", scan_id=9800001, value="1234567.5")
        before = _probe(conn, "radar_membership")
        assert before["rows"] and before["rows"] > 0

        _apply(conn, [FWD_0008, FWD_0009])               # second apply: idempotent
        assert _probe(conn, "radar_membership") == before
        if order == "p4_before_p2":
            _simulate_p2_card_columns(conn)
            _apply(conn, [FWD_0008, FWD_0009])
            assert _probe(conn, "radar_membership") == before

        _apply(conn, [REV_0009, REV_0008])
        assert _probe(conn, "radar_membership")["digest"] == before["digest"]
        assert conn.execute("SELECT to_regclass('system.movers_daily')").fetchone()[0] is None
        assert conn.execute("SELECT to_regclass('\"user\".picks')").fetchone()[0] is None
        _apply(conn, [REV_0009, REV_0008])               # repeated reverse is a no-op
        _apply(conn, [FWD_0008, FWD_0009])
        assert _probe(conn, "radar_membership")["digest"] == before["digest"]
    finally:
        conn.rollback()
        conn.close()


@requires_db
def test_side_roles_ownership_identity_guc_and_wrong_side_through_real_roles():
    """R1-2 through the side roles themselves (`db.apply_side`)."""
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        owners = dict(conn.execute(
            "SELECT n.nspname || '.' || c.relname, pg_get_userbyid(c.relowner) FROM pg_class c "
            "JOIN pg_namespace n ON n.oid = c.relnamespace "
            "WHERE (n.nspname, c.relname) IN (('system','movers_daily'),('user','picks'),('user','missed'))"
        ).fetchall())
        assert owners == {
            "system.movers_daily": "cobalt_system",
            "user.picks": "cobalt_user",
            "user.missed": "cobalt_user",
        }

        db.apply_side(conn, Side.SYSTEM)
        mover_id = conn.execute(
            "INSERT INTO system.movers_daily (trade_date,side,rank,ticker,change_pct,"
            "export_sha256,fetched_at,replay_run_id) VALUES ('2040-01-03','gainers',1,'P4M',"
            "12.5,'sha','2040-01-03 21:05+00','run-1') RETURNING id"
        ).fetchone()[0]
        conn.execute("SAVEPOINT wrong_side")
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            conn.execute('SELECT count(*) FROM "user".missed')
        conn.execute("ROLLBACK TO SAVEPOINT wrong_side")

        db.apply_side(conn, Side.USER)
        assert conn.execute("SELECT count(*) FROM system.movers_daily").fetchone()[0] >= 1
        missed_id = conn.execute(
            "INSERT INTO missed (trade_date,kind,ticker,mover_id,excluded_by,gate_detail,"
            "inputs_sha256,receipt,replay_run_id) VALUES ('2040-01-03','mover','P4M',%s,"
            "'not_in_any_source','{}'::jsonb,'sha','{}'::jsonb,'run-1') RETURNING id, user_id",
            (mover_id,),
        ).fetchone()
        assert missed_id[1] == tenant.trader_id()

        conn.execute("SAVEPOINT user_writes_system")
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            conn.execute(
                "INSERT INTO system.movers_daily (trade_date,side,rank,ticker,change_pct,"
                "export_sha256,fetched_at,replay_run_id) VALUES ('2040-01-03','losers',1,'P4X',"
                "-9,'sha','2040-01-03 21:05+00','run-1')"
            )
        conn.execute("ROLLBACK TO SAVEPOINT user_writes_system")

        conn.execute("SAVEPOINT no_guc")
        conn.execute("SELECT set_config(%s, '', false)", (tenant.TRADER_GUC,))
        with pytest.raises(psycopg.errors.InvalidTextRepresentation):
            conn.execute(
                "INSERT INTO missed (trade_date,kind,ticker,mover_id,excluded_by,gate_detail,"
                "inputs_sha256,receipt,replay_run_id) VALUES ('2040-01-03','mover','P4N',%s,"
                "'not_in_any_source','{}'::jsonb,'sha','{}'::jsonb,'run-1')",
                (mover_id,),
            )
        conn.execute("ROLLBACK TO SAVEPOINT no_guc")
    finally:
        conn.rollback()
        conn.close()


@requires_db
def test_missed_rerun_reconciles_in_the_ruled_order_against_the_live_unique_index():
    """R2-1/R3-1: (1) retire, (2) insert, (3) link — and the naive
    insert-first order collides with the partial unique index."""
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        db.apply_side(conn, Side.SYSTEM)
        mover_id = conn.execute(
            "INSERT INTO system.movers_daily (trade_date,side,rank,ticker,change_pct,"
            "export_sha256,fetched_at,replay_run_id) VALUES ('2040-01-03','gainers',1,'P4R',"
            "12.5,'sha','2040-01-03 21:05+00','run-1') RETURNING id"
        ).fetchone()[0]
        db.apply_side(conn, Side.USER)
        insert = (
            "INSERT INTO missed (trade_date,kind,ticker,mover_id,excluded_by,gate_detail,"
            "inputs_sha256,receipt,replay_run_id,run_seq) VALUES ('2040-01-03','mover','P4R',%s,"
            "'not_in_any_source','{}'::jsonb,%s,%s::jsonb,%s,%s) RETURNING id"
        )
        first = conn.execute(insert, (mover_id, "sha-1", '{"v": 1}', "run-1", 1)).fetchone()[0]

        conn.execute("SAVEPOINT naive")
        with pytest.raises(psycopg.errors.UniqueViolation):
            conn.execute(insert, (mover_id, "sha-2", '{"v": 2}', "run-2", 2))
        conn.execute("ROLLBACK TO SAVEPOINT naive")

        conn.execute(
            "UPDATE missed SET is_current = false, retired_by_run_id = 'run-2' WHERE id = %s",
            (first,),
        )
        second = conn.execute(insert, (mover_id, "sha-2", '{"v": 2}', "run-2", 2)).fetchone()[0]
        conn.execute("UPDATE missed SET superseded_by = %s WHERE id = %s", (second, first))

        rows = conn.execute(
            "SELECT id, is_current, superseded_by, receipt FROM missed WHERE ticker='P4R' ORDER BY id"
        ).fetchall()
        assert rows == [(first, False, second, {"v": 1}), (second, True, None, {"v": 2})]
    finally:
        conn.rollback()
        conn.close()
