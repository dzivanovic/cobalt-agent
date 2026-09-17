"""Direction-aware 0004 migration proof tests; no database required."""

import argparse
from pathlib import Path

import pytest

from cobalt.db_migrations import REVERSE
from cobalt.db_migrations import cli
from cobalt.db_migrations.cli import MigrationError, _rollback_paths, _verdict
from cobalt.db_migrations.placement import CREATED_TABLES


def _state(schema, rows=0, digest="d"):
    return {"schema": schema, "rows": rows if schema else None, "digest": digest if schema else None}


def test_0004_created_tables_match_placement():
    text = Path("src/cobalt/db_migrations/0004_radar_pool.sql").read_text()
    created = {
        name for name in CREATED_TABLES
        if f"CREATE TABLE IF NOT EXISTS system.{name}" in text
    }
    assert created == set(CREATED_TABLES) == {"radar_pool", "radar_membership"}
    assert 'ALTER TABLE "user".aset_sizings' in text
    assert 'ALTER TABLE "user".day_modes' in text


def test_rollback_selects_only_newer_files_newest_first():
    selected = _rollback_paths("0003")
    assert [p.name for p in selected] == [
        "0005_heartbeat_note_absent.rollback.sql",
        "0004_radar_pool.rollback.sql",
    ]
    assert selected == tuple(
        p for p in REVERSE if p.name.startswith(("0005", "0004"))
    )


def test_rollback_without_bound_refuses():
    with pytest.raises(MigrationError, match="requires --down-to"):
        _rollback_paths(None)


def test_cmd_refuses_missing_bound_before_connection(monkeypatch):
    monkeypatch.setattr(cli.db, "connect_migration", lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("connected")))
    with pytest.raises(MigrationError, match="before any connection"):
        cli.cmd_migrate(argparse.Namespace(rollback=True, down_to=None, allow_prod=False))


def test_direction_aware_verdict_table():
    absent, present = _state(None), _state("system")
    assert _verdict("radar_pool", absent, present) == "CREATED"
    assert _verdict("radar_pool", present, absent, direction="ROLLBACK") == "DROPPED"
    assert _verdict("radar_pool", present, _state("system", 1, "x")) == "CHANGED"
    assert _verdict("bars", _state("system"), _state("system")) == "OK"


def test_changed_verdict_rolls_back_before_close_and_report(monkeypatch):
    events = []

    class Conn:
        autocommit = True
        def rollback(self): events.append("rollback")
        def commit(self): events.append("commit")
        def close(self): events.append("close")

    before = {"radar_pool": _state("system")}
    after = {"radar_pool": _state("system", 1, "changed")}
    probes = iter([before, after])
    monkeypatch.setattr(cli.db, "connect_migration", lambda *_a, **_k: Conn())
    monkeypatch.setattr(cli, "_probe_all", lambda _conn: next(probes))
    monkeypatch.setattr(cli, "_apply", lambda _conn, _paths: events.append("apply"))
    monkeypatch.setattr(cli, "_print_proof", lambda *_a, **_k: events.append("report") or 1)
    with pytest.raises(MigrationError, match="rolled back before commit"):
        cli.cmd_migrate(argparse.Namespace(rollback=False, down_to=None, allow_prod=False))
    assert events == ["apply", "rollback", "close", "report"]
