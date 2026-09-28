"""Float handicap H1 STEP-5 — migration `0014` and the store (v3 §6;
`29` §8; L76).

OFFLINE: the SQL, the registry, the digest exclusion, the store's SQL.
WITH-DB: `0014` is applied ONLY inside each test's own rolled-back
transaction on the migration connection (`test_p4_migrations.py:403`'s
shape for the migration; `radar_migrated_support.migrated_radar` for the
store). Nothing here commits a migration to `cobalt_dev`.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from decimal import Decimal

from radar_migrated_support import migrated_radar, requires_db  # noqa: F401  (fixture)
from test_radar_store import RecordingConn

from cobalt import db, env
from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import (
    TABLE_DIGEST_EXCLUDED_COLUMNS,
    _apply,
    _migration_version,
    _probe,
    _rollback_paths,
)
from cobalt.db_migrations.placement import PLACEMENT, side_of
from cobalt.radar.handicap import HandicapRecord
from cobalt.radar.pool import Action, Transition
from cobalt.radar.store import RadarStore

SQL = MIGRATIONS_DIR / "0014_radar_handicap.sql"
ROLLBACK = MIGRATIONS_DIR / "0014_radar_handicap.rollback.sql"
COLUMNS = ("raw_rank", "handicap_factor", "handicap")
RTH = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def _code(path) -> str:
    return "\n".join(line.split("--", 1)[0] for line in path.read_text().splitlines())


def _record(**overrides) -> HandicapRecord:
    values = dict(
        float_m=Decimal("5.0"), market_cap_m=None, verdict="yes", reason="float", missing_rule="apply",
        mode="shadow", position=3, effective_position=5, source="screen:x@000000000000",
        block_sha256="0" * 64,
    )
    values.update(overrides)
    return HandicapRecord(**values)


# ---------------------------------------------------------------------
# OFFLINE
# ---------------------------------------------------------------------


def test_the_pair_is_registered_after_0013_and_reversed_before_it():
    names = [p.name for p in FORWARD]
    assert names.index("0014_radar_handicap.sql") == names.index("0013_tunables_slug_nullable.sql") + 1
    reverse = [p.name for p in REVERSE]
    assert reverse.index("0014_radar_handicap.rollback.sql") + 1 == reverse.index(
        "0013_tunables_slug_nullable.rollback.sql")


def test_forward_adds_exactly_the_three_nullable_columns_idempotently_with_no_check():
    code = _code(SQL)
    added = re.findall(r"ADD COLUMN IF NOT EXISTS (\w+)\s+([A-Z]+(?:\(\d+,\d+\))?)", code)
    assert added == [("raw_rank", "INTEGER"), ("handicap_factor", "NUMERIC(6,4)"), ("handicap", "JSONB")]
    assert "ALTER TABLE system.radar_membership" in code
    assert "CHECK" not in code and "NOT NULL" not in code and "CREATE" not in code


def test_rollback_drops_exactly_the_three_and_nothing_else():
    code = _code(ROLLBACK)
    assert set(re.findall(r"DROP COLUMN IF EXISTS (\w+)", code)) == set(COLUMNS)
    assert code.count("DROP") == 3 and "system.radar_membership" in code


def test_down_to_0013_selects_only_this_rollback():
    # every rollback newer than 0013, newest first — 0014 is the oldest (the stack seam)
    assert [p.name for p in _rollback_paths("0013")] == [
        "0021_legs.rollback.sql",  # S3 exits C1 (M1)
        "0017_voice_turns.rollback.sql", "0015_shadow_agreement_stale.rollback.sql",
        "0014_radar_handicap.rollback.sql"]


def test_no_new_table_and_membership_stays_system_side():
    assert side_of("radar_membership") is Side.SYSTEM
    assert "handicap" not in PLACEMENT


def test_the_migrate_proof_digest_excludes_the_three_on_membership_only():
    assert set(COLUMNS) <= set(TABLE_DIGEST_EXCLUDED_COLUMNS["radar_membership"])


def _writes(statements, ticker):
    return [(sql, params) for sql, params in statements if params and ticker in params]


def test_the_store_writes_the_three_on_insert_retain_and_exclude_and_never_on_hold_or_leave():
    conn = RecordingConn()
    RadarStore(connect=lambda: conn).apply_membership(pool_key="primary", scan_id=7, now=RTH, session="rth", transitions=[
        Transition(ticker="RET", action=Action.RETAIN, sources=["s"], rank=1, raw_rank=1,
                   handicap_factor=Decimal("0.8"), handicap=_record()),
        Transition(ticker="EXC", action=Action.EXCLUDE, sources=["s"], rank=3, raw_rank=3,
                   excluded_by="config_cap"),
        Transition(ticker="ADM", action=Action.ADMIT, sources=["s"], rank=2, raw_rank=2),
        Transition(ticker="HLD", action=Action.HOLD, sources=["s"], rank=4),
        Transition(ticker="LVE", action=Action.LEAVE, sources=["s"]),
    ])
    statements = conn.statements
    (retain_sql, retain_params), = _writes(statements, "RET")
    assert "raw_rank=%s, handicap_factor=%s, handicap=%s::jsonb" in retain_sql
    assert 1 in retain_params and Decimal("0.8") in retain_params
    assert _record().model_dump_json() in retain_params
    exclude = _writes(statements, "EXC")
    assert len(exclude) == 2 and all("raw_rank" in sql for sql, _ in exclude)
    (insert_sql, _), = [w for w in _writes(statements, "ADM") if w[0].startswith("INSERT")]
    assert "raw_rank,handicap_factor,handicap" in insert_sql
    for ticker in ("HLD", "LVE"):
        assert all("raw_rank" not in sql and "handicap" not in sql for sql, _ in _writes(statements, ticker))


def test_members_for_day_selects_the_three_and_open_members_does_not():
    conn = RecordingConn()
    store = RadarStore(connect=lambda: conn)
    store.open_members("primary")
    store.members_for_day("primary", RTH.date())
    open_sql, day_sql = (sql for sql, _ in conn.statements)
    assert all(column in day_sql for column in COLUMNS)
    assert not any(column in open_sql for column in ("raw_rank", "handicap_factor"))


# ---------------------------------------------------------------------
# WITH-DB — the migration inside its own rolled-back transaction
# ---------------------------------------------------------------------


def _conn():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    return conn


def _columns(conn) -> set[str]:
    return {row[0] for row in conn.execute(
        "SELECT a.attname FROM pg_attribute a JOIN pg_class c ON c.oid = a.attrelid "
        "JOIN pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname = 'system' "
        "AND c.relname = 'radar_membership' AND a.attnum > 0 AND NOT a.attisdropped"
    ).fetchall()}


def _seed(conn, ticker: str, scan_id: int) -> int:
    conn.execute(
        "INSERT INTO system.radar_pool (pool_key,state,session,members) "
        "VALUES ('h1_proof','scanning','rth',1) ON CONFLICT (pool_key) DO NOTHING"
    )
    return conn.execute(
        "INSERT INTO system.radar_membership (pool_key,ticker,trade_date,first_seen_at,entered_at,source,"
        "sources,rank_at_entry,last_rank,session,opened_scan_id,last_scan_id) VALUES ('h1_proof',%s,"
        "'2040-01-03','2040-01-03 15:00+00','2040-01-03 15:00+00','test','[\"test\"]'::jsonb,1,1,'rth',%s,%s) "
        "RETURNING id",
        (ticker, scan_id, scan_id),
    ).fetchone()[0]


@requires_db
def test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply():
    conn = _conn()
    try:
        _apply(conn, [p for p in FORWARD if _migration_version(p) < 14])
        before_cols = _columns(conn)
        assert not (before_cols & set(COLUMNS))                   # cobalt_dev holds no 0014
        row = _seed(conn, "H1PRE", 9700001)                       # seeded BEFORE 0014
        before = _probe(conn, "radar_membership")
        _apply(conn, [SQL])
        assert _columns(conn) == before_cols | set(COLUMNS)
        assert conn.execute(
            "SELECT raw_rank, handicap_factor, handicap FROM system.radar_membership WHERE id = %s", (row,)
        ).fetchone() == (None, None, None)                        # the old row stays valid
        _apply(conn, [SQL])                                       # twice: idempotent
        after = _probe(conn, "radar_membership")
        assert (after["rows"], after["digest"]) == (before["rows"], before["digest"])
        _apply(conn, _rollback_paths("0013"))
        assert _columns(conn) == before_cols                      # exactly the three removed
        assert _probe(conn, "radar_membership")["digest"] == before["digest"]
        _apply(conn, _rollback_paths("0013"))                     # repeated reverse is a no-op
        _apply(conn, [SQL])
        assert _columns(conn) == before_cols | set(COLUMNS)
    finally:
        conn.rollback()
        conn.close()


# ---------------------------------------------------------------------
# WITH-DB — the store, under `migrated_radar`
# ---------------------------------------------------------------------


@requires_db
def test_the_store_round_trips_the_record_and_hold_leaves_the_three(migrated_radar):
    store = RadarStore("cobalt_dev")
    key = "h1_store_test"

    def apply(scan_id, transition):
        store.apply_membership(pool_key=key, transitions=[transition], scan_id=scan_id, now=RTH, session="rth")

    apply(9910001, Transition(ticker="H1A", action=Action.ADMIT, sources=["t"], source="t", rank=3,
                              raw_rank=3, handicap_factor=Decimal("0.8"), handicap=_record()))
    (row,) = store.members_for_day(key, RTH.date())
    assert (row["raw_rank"], row["handicap_factor"]) == (3, Decimal("0.8000"))
    assert HandicapRecord.model_validate(row["handicap"]) == _record()          # round trip
    apply(9910002, Transition(ticker="H1A", action=Action.RETAIN, sources=["t"], source="t", rank=2,
                              raw_rank=2, handicap_factor=Decimal(1),
                              handicap=_record(verdict="no", reason="neither", position=2, effective_position=2)))
    (row,) = store.members_for_day(key, RTH.date())
    assert (row["raw_rank"], row["handicap_factor"], row["handicap"]["verdict"]) == (2, Decimal("1.0000"), "no")
    apply(9910003, Transition(ticker="H1A", action=Action.HOLD, sources=["t"], rank=2))
    (row,) = store.members_for_day(key, RTH.date())
    assert (row["raw_rank"], row["handicap_factor"], row["handicap"]["verdict"]) == (2, Decimal("1.0000"), "no")


@requires_db
def test_an_exclude_writes_the_three_and_an_absent_block_writes_nulls(migrated_radar):
    store = RadarStore("cobalt_dev")
    key = "h1_store_test_2"
    store.apply_membership(pool_key=key, now=RTH, session="rth", scan_id=9920001, transitions=[
        Transition(ticker="H1X", action=Action.EXCLUDE, sources=["t"], source="t", rank=9, raw_rank=9,
                   excluded_by="config_cap", handicap_factor=Decimal("0.8"),
                   handicap=_record(position=9, effective_position=11)),
        Transition(ticker="H1N", action=Action.ADMIT, sources=["t"], source="t", rank=1, raw_rank=1),
    ])
    rows = {row["ticker"]: row for row in store.members_for_day(key, RTH.date())}
    assert (rows["H1X"]["raw_rank"], rows["H1X"]["handicap"]["effective_position"]) == (9, 11)
    assert (rows["H1N"]["raw_rank"], rows["H1N"]["handicap_factor"], rows["H1N"]["handicap"]) == (1, None, None)
