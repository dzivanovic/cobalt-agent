"""R692 — migration `0023_radar_price_floor` and the `price_floor` reads
(card 137, rows M and F5).

OFFLINE half: the SQL and the registry.

WITH-DB half (skipped offline): every registered migration, `0023`
included, is applied ONLY inside the test's own never-committed
transaction on `cobalt_dev` (`migrated_radar`, L76); `RadarStore` reads
through a savepoint proxy over that same connection. Nothing commits.
The file needs level 0023, so the gate runs it in PASS 2 only
(`ops/desk/gate-lists.md`). Tickers and dates are constructed (L32).
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

import psycopg
import pytest
from radar_migrated_support import migrated_radar, requires_db  # noqa: F401  (fixture: FORWARD inside the test's transaction, L76)

from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import _apply
from cobalt.radar.store import RadarStore

SQL = MIGRATIONS_DIR / "0023_radar_price_floor.sql"
ROLLBACK = MIGRATIONS_DIR / "0023_radar_price_floor.rollback.sql"
POOL = "price_floor_test"
DAY = date(2001, 1, 2)
T0 = datetime(2001, 1, 2, 15, 0, tzinfo=timezone.utc)
FOUR = ("config_cap", "not_equity", "screen_inactive", "manual")


def _code(path) -> str:
    return "\n".join(l for l in path.read_text().splitlines() if not l.strip().startswith("--"))


# ---------------------------------------------------------------------
# OFFLINE — the registry and the SQL
# ---------------------------------------------------------------------


def test_0023_is_registered_last_and_its_rollback_first():
    assert SQL.exists() and ROLLBACK.exists()
    assert FORWARD[-1] == SQL and REVERSE[0] == ROLLBACK


def test_0023_creates_no_table_and_matches_the_excluded_by_in_check_only():
    code = _code(SQL)
    assert "CREATE TABLE" not in code
    assert "'%''config_cap''%'" in code, "the one CHECK is found by its 'config_cap' value"
    assert "found_count <> 1" in code
    assert ("CHECK (excluded_by IN ('config_cap', 'not_equity', 'screen_inactive', 'manual', 'price_floor'))"
            in code)


def test_the_rollback_states_its_cost_and_is_guarded():
    back = ROLLBACK.read_text()
    assert "-- COST:" in back
    assert "to_regclass('system.radar_membership')" in back
    code = _code(ROLLBACK)
    assert ("SET excluded_by = NULL WHERE excluded_by = 'price_floor' AND entered_at IS NOT NULL"
            in " ".join(code.split()))
    assert "CHECK (excluded_by IN ('config_cap', 'not_equity', 'screen_inactive', 'manual'))" in code


# ---------------------------------------------------------------------
# WITH-DB — at 0023, inside the suite transaction
# ---------------------------------------------------------------------


def _pool(conn) -> None:
    conn.execute(
        "INSERT INTO system.radar_pool (pool_key, state, session, members) "
        "VALUES (%s, 'scanning', 'rth', 0) ON CONFLICT (pool_key) DO NOTHING",
        (POOL,),
    )


def _insert(conn, ticker: str, excluded_by: str | None, *, scan: int, admitted: bool = True) -> int:
    """One CLOSED episode (left_at set), admitted or never-admitted."""
    return conn.execute(
        "INSERT INTO system.radar_membership (pool_key, ticker, trade_date, first_seen_at, entered_at, "
        "left_at, source, sources, excluded_by, session, opened_scan_id, last_scan_id, closed_scan_id) "
        "VALUES (%s, %s, %s, %s, %s, %s, 'test', '[\"test\"]'::jsonb, %s, 'rth', %s, %s, %s) RETURNING id",
        (POOL, ticker, DAY, T0, T0 if admitted else None, T0 + timedelta(hours=1), excluded_by,
         scan, scan, scan),
    ).fetchone()[0]


def _refused(conn, ticker: str, excluded_by: str, *, scan: int) -> None:
    with pytest.raises(psycopg.errors.CheckViolation):
        with conn.transaction():
            _insert(conn, ticker, excluded_by, scan=scan)


def _excluded_by_checks(conn) -> list[tuple[str, str]]:
    return conn.execute(
        "SELECT c.conname, pg_get_constraintdef(c.oid) FROM pg_constraint AS c "
        "JOIN pg_class AS t ON t.oid = c.conrelid JOIN pg_namespace AS n ON n.oid = t.relnamespace "
        "WHERE n.nspname = 'system' AND t.relname = 'radar_membership' AND c.contype = 'c' "
        "AND pg_get_constraintdef(c.oid) LIKE '%%excluded_by%%' ORDER BY c.conname"
    ).fetchall()


@requires_db
def test_0023_admits_price_floor_and_keeps_the_four(migrated_radar):
    conn = migrated_radar
    _pool(conn)
    row_id = _insert(conn, "PFLA", "price_floor", scan=9_100_001)
    assert conn.execute(
        "SELECT excluded_by FROM system.radar_membership WHERE id = %s", (row_id,)
    ).fetchone()[0] == "price_floor"
    for offset, value in enumerate(FOUR):
        _insert(conn, f"PFL{offset}", value, scan=9_100_010 + offset)
    _refused(conn, "PFLB", "bogus", scan=9_100_020)
    checks = _excluded_by_checks(conn)
    assert len(checks) == 2, checks
    named = dict(checks)
    assert "'price_floor'" in named["radar_membership_excluded_by_check"]
    assert any("entered_at IS NOT NULL" in definition for definition in named.values())
    _apply(conn, [SQL])  # a second run is a no-op
    assert _excluded_by_checks(conn) == checks


@requires_db
def test_0023_rollback_clears_price_floor_and_restores_the_check(migrated_radar):
    conn = migrated_radar
    _pool(conn)
    row_id = _insert(conn, "PFLR", "price_floor", scan=9_200_001)
    _apply(conn, [ROLLBACK])
    excluded_by, left_at = conn.execute(
        "SELECT excluded_by, left_at FROM system.radar_membership WHERE id = %s", (row_id,)
    ).fetchone()
    assert excluded_by is None and left_at == T0 + timedelta(hours=1)
    _refused(conn, "PFLS", "price_floor", scan=9_200_002)
    _insert(conn, "PFLT", "config_cap", scan=9_200_003)
    _apply(conn, [ROLLBACK])  # repeated: the four-value CHECK stays
    assert "'price_floor'" not in dict(_excluded_by_checks(conn))["radar_membership_excluded_by_check"]
    _apply(conn, [SQL])
    _insert(conn, "PFLU", "price_floor", scan=9_200_004)


@requires_db
def test_members_for_day_hides_price_floor_rows_and_the_drc_reads_them(migrated_radar):
    conn = migrated_radar
    _pool(conn)
    _insert(conn, "PFDA", "price_floor", scan=9_300_001)
    _insert(conn, "PFDB", "config_cap", scan=9_300_002)
    _insert(conn, "PFDC", "config_cap", scan=9_300_003, admitted=False)
    store = RadarStore("cobalt_dev")
    assert {row["ticker"] for row in store.members_for_day(POOL, DAY)} == {"PFDB", "PFDC"}
    assert {row["ticker"] for row in store.members_for_day(POOL, DAY, price_floor_rows=True)} == {
        "PFDA", "PFDB", "PFDC"}
    assert {row["ticker"] for row in store.members_for_replay(POOL, DAY)} == {"PFDA", "PFDB"}
