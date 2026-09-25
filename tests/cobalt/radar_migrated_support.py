"""`migrated_radar` — the with-DB fixture under which a test sees the
registry's migrations (`0014` included) WITHOUT `cobalt_dev` ever holding
them (L76; XL76's decision (A), `reports/handicap-h1-build-2026-09-24.md`).

ONE transaction on the migration connection: `_apply(conn, FORWARD)`, then
every `db.connect` of the test is a savepoint proxy over that same
connection (the shape of `drc/d1-trading-log`'s `migrated` fixture), and
`conn.rollback()` at teardown. Nothing commits. `tests/cobalt/conftest.py`
is not edited (every branch shares it, L68): a test file opts in by
importing the fixture from here.
"""

from __future__ import annotations

import itertools
import os

import pytest

from cobalt import db, env
from cobalt.db_migrations import FORWARD
from cobalt.db_migrations.cli import _apply

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)


class SavepointProxy:
    """A `db.connect()` result over the fixture's ONE migration connection.
    Never commits, never closes; commit/rollback map to a savepoint."""

    def __init__(self, conn, name: str):
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


@pytest.fixture
def migrated_radar(monkeypatch):
    """Every registered migration applied inside this test's own
    transaction; rolled back at teardown. Skips without `cobalt_dev`."""
    if not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")):
        pytest.skip("requires_db: Postgres env settings not available")
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    counter = itertools.count()
    try:
        _apply(conn, FORWARD)

        def _connect(dbname, *, side, allow_prod=False):
            if dbname != env.DEV_DB_NAME:
                raise AssertionError(f"RULING 7.1d: a test asked for database {dbname!r}")
            proxy = SavepointProxy(conn, f"migrated_radar_sp_{next(counter)}")
            db.apply_side(proxy, side)
            return proxy

        monkeypatch.setattr(db, "connect", _connect)
        yield conn
    finally:
        conn.rollback()
        conn.close()
