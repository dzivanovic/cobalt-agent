"""flake-fix-2 F1 — `migration_retry.open_migrated`, no database.

`db.connect_migration` and the caller's `apply` are faked: every attempt
must open a fresh connection with autocommit off, a failed attempt's
connection is closed (even when its rollback raises), a
`DeadlockDetected` is retried at most twice with one printed line per
retry, and any other error propagates at once.
"""

from __future__ import annotations

import psycopg
import pytest

from cobalt import db, env
from migration_retry import open_migrated

PATHS = ["constructed_forward.sql"]


class FakeConn:
    def __init__(self, *, rollback_raises: bool = False):
        self.autocommit = True
        self.closed = False
        self.rolled_back = False
        self._rollback_raises = rollback_raises

    def rollback(self):
        self.rolled_back = True
        if self._rollback_raises:
            raise RuntimeError("constructed rollback failure")

    def close(self):
        self.closed = True


def _opener(monkeypatch, **conn_kwargs):
    """Fakes `db.connect_migration`; returns the list of connections it opened."""
    opened = []

    def _open(dbname):
        assert dbname == env.DEV_DB_NAME
        conn = FakeConn(**conn_kwargs)
        opened.append(conn)
        return conn

    monkeypatch.setattr(db, "connect_migration", _open)
    return opened


def _failing_apply(error, times):
    """An `apply` whose first `times` calls raise `error`; records each call."""
    seen = []

    def _apply(conn, paths):
        seen.append((conn, conn.autocommit, paths))
        if len(seen) <= times:
            raise error("constructed by flake-fix-2 F1")

    return _apply, seen


def test_first_deadlock_retries_once_on_a_fresh_connection(monkeypatch, capsys):
    opened = _opener(monkeypatch)
    apply, seen = _failing_apply(psycopg.errors.DeadlockDetected, 1)

    conn = open_migrated(apply, PATHS)

    out = capsys.readouterr().out
    assert "migration retry 1: DeadlockDetected" in out
    assert "migration retry 2" not in out
    assert len(opened) == 2 and opened[0] is not opened[1]
    assert conn is opened[1] and not conn.closed
    assert opened[0].rolled_back and opened[0].closed
    assert seen == [(opened[0], False, PATHS), (opened[1], False, PATHS)]


def test_third_deadlock_raises_after_two_retries(monkeypatch, capsys):
    opened = _opener(monkeypatch)
    apply, seen = _failing_apply(psycopg.errors.DeadlockDetected, 10)

    with pytest.raises(psycopg.errors.DeadlockDetected):
        open_migrated(apply, PATHS)

    out = capsys.readouterr().out
    assert "migration retry 1: DeadlockDetected" in out
    assert "migration retry 2: DeadlockDetected" in out
    assert "migration retry 3" not in out
    assert len(opened) == 3 and len({id(c) for c in opened}) == 3
    assert all(c.closed for c in opened)
    assert len(seen) == 3


def test_another_error_is_not_retried(monkeypatch, capsys):
    opened = _opener(monkeypatch)
    apply, seen = _failing_apply(psycopg.errors.UndefinedTable, 1)

    with pytest.raises(psycopg.errors.UndefinedTable):
        open_migrated(apply, PATHS)

    assert "migration retry" not in capsys.readouterr().out
    assert len(opened) == 1 and opened[0].closed
    assert len(seen) == 1


def test_failed_attempt_is_closed_when_its_rollback_raises(monkeypatch, capsys):
    opened = _opener(monkeypatch, rollback_raises=True)
    apply, seen = _failing_apply(psycopg.errors.DeadlockDetected, 1)

    with pytest.raises(RuntimeError, match="constructed rollback failure"):
        open_migrated(apply, PATHS)

    assert len(opened) == 1 and opened[0].closed is True
    assert len(seen) == 1


def test_xl76_reports_false_when_the_migration_step_fails(monkeypatch, capsys):
    import importlib.util
    from pathlib import Path

    import migration_retry

    path = (
        Path(__file__).resolve().parents[1]
        / "experiments"
        / "handicap_h1"
        / "test_xl76_membership_harness.py"
    )
    spec = importlib.util.spec_from_file_location("xl76_failure_probe", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def fail(_apply, _paths):
        raise psycopg.errors.UndefinedTable("constructed XL76 migration failure")

    monkeypatch.setattr(migration_retry, "open_migrated", fail)
    with pytest.raises(
        psycopg.errors.UndefinedTable,
        match="constructed XL76 migration failure",
    ):
        module.test_xl76_2_3_harness_shape_at_step_1(monkeypatch)

    out = capsys.readouterr().out
    assert "XL76: harness_applies=False" in out
