"""New-core test fixtures: every test runs in `cobalt_dev`, in a
transaction, and is rolled back (RULING 7.1d).

TWO JOBS.

1. Override the repo-root autouse psycopg mock. The root conftest
   patches `psycopg.connect` globally, so without this override the
   store "integration" tests would run against a MagicMock and
   pass/fail meaninglessly.

2. Pin `COBALT_ENV=dev` and give the DB-touching tests a transaction
   that never commits.

WHY (2). Before RULING 7 the test suite wrote REAL rows into the same
`cobalt_dev` tables the PRODUCTION ASET sheet and both prefill jobs
wrote to, because `configs/dev/aset.local.yaml` pinned `db_name:
cobalt_dev` for every caller. Two measured consequences:

* 15 stray `TEST`/`FORDATE` rows from test runs sat in `aset_sizings`
  and made `DRC-2026-09-03.md` report "17 cards" when 2 were real;
* one full suite run on 2026-09-04 grew `vault_writes` from 383 to
  529 — +146 rows of pytest temp-vault paths interleaved with the
  production audit trail that the 09-03 forensics depended on.

Per-test cleanup was the previous answer and it is not sufficient: it
only removes what a test remembers to name, it cannot help a test that
fails before its teardown, and `test_vaultwrite.py` cleaned up at SETUP
(by note prefix) rather than at teardown, so its rows survived every
run. A transaction that is never committed is not a discipline anyone
has to remember.

MECHANISM. `db.connect` is monkeypatched to hand every caller a
savepoint-scoped proxy over ONE real connection whose outer transaction
the fixture rolls back at the end of the test. The stores open a new
connection per operation (`with self._connect() as conn:`), so the
proxy must survive `with` blocks: its `__exit__` neither commits nor
closes. `commit()` / `rollback()` inside a store — `pending_write()`
does both — map to `RELEASE` / `ROLLBACK TO` a savepoint, so nested
transaction semantics are preserved exactly and a test that asserts
"the audit row was rolled back" still means what it says.
"""

import itertools
import os

import pytest

from cobalt import db, env


@pytest.fixture(autouse=True)
def mock_postgres_memory():
    """Neutralise the repo-root psycopg mock for new-core tests."""
    yield


@pytest.fixture(autouse=True)
def dev_env(monkeypatch):
    """RULING 7: nothing resolves without `COBALT_ENV`, and the test
    suite is `dev` by law — never `production`, never unset. Autouse so
    no test can accidentally resolve production's database or vault.

    `COBALT_VAULT_PATH` is cleared for the same reason: an exported
    override in the developer's shell must not leak into a test run.
    """
    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.delenv("COBALT_VAULT_PATH", raising=False)
    monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
    yield


class _SavepointConnection:
    """A `db.connect()` result that shares one real connection.

    Never commits and never closes the underlying connection: the
    fixture owns its lifetime and always rolls it back.
    """

    def __init__(self, conn, name: str):
        self._conn = conn
        self._name = name
        self._released = False
        self._conn.execute(f"SAVEPOINT {self._name}")

    # -- everything the stores use that we do not intercept -----------
    def __getattr__(self, item):
        return getattr(self._conn, item)

    # -- `with self._connect() as conn:` must not end the transaction --
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            self.rollback()
        return False

    # -- autocommit is a property on the real connection --------------
    @property
    def autocommit(self):
        return self._conn.autocommit

    @autocommit.setter
    def autocommit(self, value):
        # The outer transaction owns commit semantics. `pending_write()`
        # sets autocommit=False; honouring that literally would be a
        # no-op anyway (we are already in a transaction), and honouring
        # autocommit=True would end it. Swallow both.
        return

    def commit(self):
        if not self._released:
            self._conn.execute(f"RELEASE SAVEPOINT {self._name}")
            self._released = True

    def rollback(self):
        if not self._released:
            self._conn.execute(f"ROLLBACK TO SAVEPOINT {self._name}")

    def close(self):
        return


@pytest.fixture(autouse=True)
def dev_db_tx(monkeypatch):
    """Run every new-core test inside one `cobalt_dev` transaction and
    roll it back.

    AUTOUSE, deliberately. The ruling names the ASET-store and vaultwrite
    tests, and those two were the modules with the biggest leak — but
    measuring the actual delta over a full run found four more:
    `test_prefill_daily` (+29 vault_writes), `test_prefill_drc` (+23),
    `test_aset_daily_note` (+18) and `test_prefill_trade_note` (+3).
    Opt-in would have left +73 rows per run behind and the proof the
    ruling asks for — identical counts before and after — would have
    failed. Anything that reaches Postgres through `db.connect` is now
    covered whether or not its module remembered to ask.

    Also asserts the database being opened: a test that somehow asks for
    `cobalt_brain` fails here rather than reaching the live database.

    When Postgres is unavailable this is a no-op rather than a skip, so
    the pure-unit tests still run on a machine with no database.
    """
    if not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")):
        yield None
        return

    real = db.connect(env.DEV_DB_NAME)
    real.autocommit = False
    counter = itertools.count()

    def fake_connect(dbname: str, *, allow_prod: bool = False):
        if dbname != env.DEV_DB_NAME:
            raise AssertionError(
                f"RULING 7.1d: a test asked for database {dbname!r}. The suite "
                f"runs against {env.DEV_DB_NAME} only."
            )
        return _SavepointConnection(real, f"pytest_sp_{next(counter)}")

    monkeypatch.setattr(db, "connect", fake_connect)
    try:
        yield real
    finally:
        real.rollback()
        real.close()
