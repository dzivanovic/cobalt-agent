"""M1 `0021_legs` — the migration text and its registration (offline).

The DDL's behaviour is `test_legs_db.py` (with-DB, X4); this file pins
the seams other lanes cite (S-MIG, S-LEGS): the file pair, its place in
FORWARD / REVERSE, the side, and that the rollback removes exactly what
the forward adds.
"""

from __future__ import annotations

import re

from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.placement import CREATED_TABLES, CREATED_VIEWS, DECLARED_TABLES, side_of

SQL = MIGRATIONS_DIR / "0021_legs.sql"
ROLLBACK = MIGRATIONS_DIR / "0021_legs.rollback.sql"


def _code(path) -> str:
    return "\n".join(
        line for line in path.read_text().splitlines() if not line.strip().startswith("--")
    )


def test_the_pair_is_registered_last_and_reversed_first():
    assert SQL.exists() and ROLLBACK.exists()
    # F15 P1's 0022 now follows it (second-last forward, second reversed).
    assert FORWARD[-2] == SQL and REVERSE[1] == ROLLBACK


def test_legs_and_its_view_are_user_side_and_fills_stays_declared():
    assert side_of("legs") is Side.USER and CREATED_TABLES["legs"] is Side.USER
    assert CREATED_VIEWS["legs_current_v"] is Side.USER
    assert "legs" not in DECLARED_TABLES, "legs is built now; it leaves DECLARED"
    assert DECLARED_TABLES["fills"] is Side.USER, "O16 default: fills stays declared, unbuilt"


def test_the_forward_carries_s_legs_whole():
    code = _code(SQL)
    assert 'CREATE TABLE IF NOT EXISTS "user".legs' in code
    assert re.search(r"user_id\s+INTEGER NOT NULL\s+DEFAULT \(current_setting\('cobalt\.trader_id'\)::int\)\s+"
                     r'REFERENCES "user"\.traders\(id\)', code)
    assert 'REFERENCES "user".aset_sizings(id)' in code
    assert 'REFERENCES "user".legs(id)' in code
    assert 'REFERENCES "user".day_modes(trade_date)' in code
    for check in (
        "kind IN ('entry', 'exit')",
        "shares > 0",
        "price > 0",
        "flag IN ('estimated', 'confirmed')",
        "price_source IN ('last_poll', 'typed', 'dm', 'trading_log')",
        "preset IS NULL OR preset IN ('half', 'third', 'flat', 'typed')",
        "running_before >= 0",
        "source IN ('panel', 'sheet', 'dm', 'trading_log')",
        "(source = 'trading_log') = (source_import_id IS NOT NULL)",
        "held_stated IS NULL OR held_stated >= 0",
        "held_stated IS NULL OR (kind = 'entry' AND corrects IS NOT NULL)",
        "(kind = 'entry' AND corrects IS NULL) = (sheet_mismatch IS NOT NULL)",
    ):
        assert check in code, check
    for absent in ("running_after", "cobalt_stop", " direction "):
        assert absent not in code, absent
    assert "source_import_id BIGINT," in code, "no FK: the import table is the DRC lane's"
    assert "WHERE corrects IS NULL" in code and "WHERE kind = 'entry' AND corrects IS NULL" in code
    assert 'EXECUTE FUNCTION "user".refuse_row_update()' in code
    assert 'CREATE OR REPLACE VIEW "user".legs_current_v' in code


def test_the_forward_adds_the_three_column_sets():
    code = _code(SQL)
    assert re.search(r'ALTER TABLE "user"\.card_stop_edits\s+ADD COLUMN IF NOT EXISTS kind TEXT NOT NULL '
                     r"DEFAULT 'edit'", code)
    assert "kind IN ('edit', 'reset')" in code
    for column in ("trade_note_path TEXT", "drift_warning_pct NUMERIC(6, 2)", "drift_warned BOOLEAN"):
        assert f"ADD COLUMN IF NOT EXISTS {column}" in code, column


def test_the_migrate_proof_does_not_read_the_added_columns_as_content():
    from cobalt.db_migrations.cli import TABLE_DIGEST_EXCLUDED_COLUMNS

    assert {"trade_note_path", "drift_warning_pct", "drift_warned"} <= set(
        TABLE_DIGEST_EXCLUDED_COLUMNS["aset_sizings"])
    assert TABLE_DIGEST_EXCLUDED_COLUMNS["card_stop_edits"] == ("kind",)


def test_the_rollback_removes_exactly_what_the_forward_adds():
    code = _code(ROLLBACK)
    assert 'DROP VIEW IF EXISTS "user".legs_current_v' in code
    assert 'DROP TABLE IF EXISTS "user".legs' in code
    dropped = set(re.findall(r"DROP COLUMN IF EXISTS (\w+)", code))
    assert dropped == {"kind", "trade_note_path", "drift_warning_pct", "drift_warned"}
    assert "refuse_row_update" not in code, "0007's function is not this migration's to drop"
