"""XL76 (the drafter's, L70 + L76): how the with-DB leg sees `0014`
without `cobalt_dev` ever holding it.

Once `apply_membership` writes and `members_for_day` reads the three new
columns, every with-DB test that reaches `system.radar_membership` through
them would fail on a `cobalt_dev` at `0013`. This module prints:

(1) `callers=<n>` — the with-DB test ids that reach the table through
    `RadarStore.apply_membership`, `members_for_day` or `open_members`: a
    static read (AST) of every `tests/cobalt` module naming one of the
    three, narrowed to tests that run on `cobalt_dev` (a `requires_db` /
    Postgres `skipif` mark, a module `pytestmark`, or a DB fixture) and
    whose body — or a module helper it calls — names one of the three on
    a store not built with an injected `connect=`;
(2) `harness_applies=<bool>` — ONE transaction on the migration
    connection: `_apply(conn, FORWARD)`, then `db.connect` routed through
    savepoint proxies on that same connection (the `migrated` fixture
    shape of `drc/d1-trading-log`'s `test_drc_store.py:217-235`), ONE
    `RadarStore().open_members(...)` through it, `conn.rollback()` in
    `finally`;
(3) `apply_ms=<n>` — the wall time of one `_apply(conn, FORWARD)`.

Nothing here commits. Run with `COBALT_ENV=dev` inside THE LOCK; without
`.env` the DB tests skip and only (1) prints.
"""

from __future__ import annotations

import ast
import os
import time
from pathlib import Path

import pytest

TESTS = Path(__file__).resolve().parents[2] / "cobalt"
NAMES = ("apply_membership", "members_for_day", "open_members")
DB_FIXTURES = {"dev_db_tx", "real_connect", "migrated", "migrated_radar"}

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="XL76 (2)/(3): needs cobalt_dev (run inside THE LOCK)",
)


def _marks_db(decorators) -> bool:
    text = " ".join(ast.unparse(d) for d in decorators)
    return "requires_db" in text or "POSTGRES" in text or any(f in text for f in DB_FIXTURES)


def _reaches(source: str) -> bool:
    return any(name in source for name in NAMES) and "connect=lambda" not in source.replace(" ", "")


def with_db_callers() -> list[str]:
    ids: list[str] = []
    for path in sorted(TESTS.glob("test_*.py")):
        text = path.read_text()
        if not any(name in text for name in NAMES):
            continue
        tree = ast.parse(text)
        module_db = any(
            isinstance(node, ast.Assign)
            and any(getattr(t, "id", None) == "pytestmark" for t in node.targets)
            and _marks_db([node.value])
            for node in tree.body
        )
        helpers = {
            node.name: ast.get_source_segment(text, node) or ""
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("test_")
        }

        def reaches(node) -> bool:
            body = ast.get_source_segment(text, node) or ""
            if _reaches(body):
                return True
            called = {n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
            return any(_reaches(helpers[name]) for name in called if name in helpers)

        def collect(nodes, prefix, class_db=False):
            for node in nodes:
                if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
                    collect(node.body, f"{prefix}{node.name}::", class_db or _marks_db(node.decorator_list))
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test_"):
                    params = {a.arg for a in node.args.args}
                    is_db = module_db or class_db or _marks_db(node.decorator_list) or bool(params & DB_FIXTURES)
                    if is_db and reaches(node):
                        ids.append(f"{path.name}::{prefix}{node.name}")

        collect(tree.body, "")
    return ids


def test_xl76_1_the_with_db_callers():
    files = sorted(p.name for p in TESTS.glob("test_*.py") if any(n in p.read_text() for n in NAMES))
    print(f"XL76: files naming the three calls ({len(files)}): {' '.join(files)}")
    ids = with_db_callers()
    print(f"XL76: callers={len(ids)}")
    for test_id in ids:
        print(f"XL76 caller: {test_id}")


@requires_db
def test_xl76_2_3_harness_shape_at_step_1(monkeypatch):
    """(2) and (3) with the proxy written HERE (STEP-1: the support module
    does not exist yet; STEP-5 moves this shape into it)."""
    from cobalt import db, env
    from cobalt.db_migrations import FORWARD
    from cobalt.db_migrations.cli import _apply
    from cobalt.radar.store import RadarStore

    class Proxy:
        def __init__(self, conn, name):
            self._conn, self._name, self._done = conn, name, False
            conn.execute(f"SAVEPOINT {name}")

        def __getattr__(self, item):
            return getattr(self._conn, item)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, *_):
            if exc_type is not None:
                self.rollback()
            return False

        @property
        def autocommit(self):
            return False

        @autocommit.setter
        def autocommit(self, _value):
            return

        def commit(self):
            if not self._done:
                self._conn.execute(f"RELEASE SAVEPOINT {self._name}")
                self._done = True

        def rollback(self):
            if not self._done:
                self._conn.execute(f"ROLLBACK TO SAVEPOINT {self._name}")
                self._done = True

        def close(self):
            return

    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    applies = False
    try:
        started = time.monotonic()
        _apply(conn, FORWARD)
        apply_ms = int((time.monotonic() - started) * 1000)
        counter = iter(range(10_000))

        def _connect(dbname, *, side, allow_prod=False):
            assert dbname == env.DEV_DB_NAME
            proxy = Proxy(conn, f"xl76_sp_{next(counter)}")
            db.apply_side(proxy, side)
            return proxy

        monkeypatch.setattr(db, "connect", _connect)
        rows = RadarStore().open_members("xl76_probe")
        applies = rows == []
        print(f"XL76: apply_ms={apply_ms}")
    finally:
        conn.rollback()
        conn.close()
        print(f"XL76: harness_applies={applies}")
    assert applies


@requires_db
def test_xl76_close_0014_absent_on_cobalt_dev():
    """CLOSE (L76): READ-ONLY — `pg_catalog`, one SELECT, rolled back. The
    three `0014` columns must be ABSENT from `cobalt_dev` (expected 0)."""
    from cobalt import db, env

    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    try:
        count = conn.execute(
            "SELECT count(*) FROM pg_attribute a JOIN pg_class c ON c.oid = a.attrelid "
            "JOIN pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname = 'system' "
            "AND c.relname = 'radar_membership' "
            "AND a.attname IN ('raw_rank','handicap_factor','handicap') AND NOT a.attisdropped"
        ).fetchone()[0]
    finally:
        conn.rollback()
        conn.close()
    print(f"XL76: 0014_columns_on_cobalt_dev={count}")
    assert count == 0
