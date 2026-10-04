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
from datetime import datetime, timezone

import pytest

from cobalt import db, env
from cobalt.session import clock as session_clock_module

#: The UNPATCHED factory, bound at import time. `dev_db_tx` replaces
#: `db.connect` for the whole suite, so the fixture itself — and any test
#: that is ABOUT the factory, the grants or the schemas (ADR-0008) —
#: needs the real one. Held here rather than re-imported in each test, so
#: there is one name for "a connection that is really a connection".
REAL_CONNECT = db.connect


# ---------------------------------------------------------------------
# lock-relief G1 / P1: "skipped offline" means "needs the database"
# ---------------------------------------------------------------------

#: G1: a test reached `cobalt_dev` and carries no offline skip.
UNMARKED_REACH = "with-DB test without an offline skip mark: {nodeid}"


def offline_skip_marks(item) -> list:
    """Every `skipif` mark on `item`: its own, its class's and its module's
    `pytestmark` (pytest's node chain). The ONE reading of "this test skips
    offline": the G1 guard and the `--db-only` selection both stand on it."""
    return list(item.iter_markers(name="skipif"))


def require_offline_skip(item) -> None:
    """G1: a database reach from a test with no `skipif` mark is refused."""
    if not offline_skip_marks(item):
        raise AssertionError(UNMARKED_REACH.format(nodeid=item.nodeid))


def db_only_split(items) -> tuple[list, list]:
    """P1's keep rule: (kept, dropped); kept carries at least one `skipif`
    mark. Wider than the database (a vault-path skip is kept), never narrower:
    a test that reaches the database unmarked fails G1's guard."""
    kept, dropped = [], []
    for item in items:
        (kept if offline_skip_marks(item) else dropped).append(item)
    return kept, dropped


def pytest_addoption(parser):
    """P1. Registered here, beside the guard it stands on: the pass-1 command
    names `tests/cobalt`, so this conftest is loaded before the arguments are
    parsed; a run that names no `tests/cobalt` path refuses `--db-only` as an
    unknown argument rather than ignoring it (L1)."""
    parser.addoption(
        "--db-only", action="store_true", default=False,
        help="lock-relief P1: keep only the tests that carry a skipif mark (the with-DB pass 1); "
             "deselect every other test",
    )


def pytest_collection_modifyitems(config, items):
    """P1: with `--db-only`, deselect every item that carries no `skipif`
    mark — under `tests/cobalt` and `tests/taxonomy` alike (this hook sees
    the whole session's items). Without it nothing changes."""
    if not config.getoption("--db-only"):
        return
    kept, dropped = db_only_split(items)
    if dropped:
        config.hook.pytest_deselected(items=dropped)
        items[:] = kept


@pytest.fixture(autouse=True)
def offline_skip_guard():
    """G1: the record of database reaches by unmarked tests. A store may
    swallow the guard's AssertionError, so the teardown fails the test on any
    recorded reach. Yields the record (a test that trips the guard on
    purpose clears it)."""
    tripped: list = []
    yield tripped
    if tripped:
        pytest.fail("\n".join(tripped))


#: True only while `dev_db_tx` opens its own connection: the one open
#: that is not a reach (check X1, the guarded `psycopg.connect`).
_opening_the_suite_connection = False


def _guarded_reach(item, tripped: list) -> None:
    try:
        require_offline_skip(item)
    except AssertionError as refused:
        tripped.append(str(refused))
        raise


# ---------------------------------------------------------------------
# slot-guard S2: the with-DB suite checks column-slot headroom first
# ---------------------------------------------------------------------

#: The `SLOTS WARN` lines a with-DB run prints in its terminal summary.
_SLOTS_WARN = pytest.StashKey[list]()


def pytest_sessionstart(session):
    """Before any test, when the Postgres settings are present: read
    `cobalt_dev`'s column slots. A table with fewer than
    `SLOT_FAIL_HEADROOM` free slots stops the run (exit 3) before a with-DB
    gate can fail half-way on `TooManyColumns`; a table at or above
    `SLOT_WARN_AT` is named in the terminal summary. Offline runs are
    untouched."""
    if not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")):
        return
    from cobalt.db_migrations.cli import SLOT_WARN_AT
    from cobalt.db_migrations.dev_rebuild import (
        SLOT_FAIL_HEADROOM, SLOT_LIMIT, slot_lines, slot_report, slot_verdict,
    )

    conn = REAL_CONNECT(env.DEV_DB_NAME, side=db.Side.SYSTEM)
    try:
        rows = slot_report(conn)
    finally:
        conn.rollback()
        conn.close()
    verdict = slot_verdict(rows, SLOT_WARN_AT, SLOT_FAIL_HEADROOM)
    if verdict == "fail":
        schema, table, max_attnum = max(rows, key=lambda r: r[2])[:3]
        pytest.exit(
            f"cobalt_dev column slots: {schema}.{table} {max_attnum} of {SLOT_LIMIT} — run a "
            f"devfix (cobalt db dev-rebuild {schema}.{table}) before any with-DB gate",
            returncode=3,
        )
    if verdict == "warn":
        session.config.stash[_SLOTS_WARN] = slot_lines(rows, SLOT_WARN_AT)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    for line in config.stash.get(_SLOTS_WARN, []):
        terminalreporter.write_line(line)


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
def dev_db_tx(monkeypatch, request, offline_skip_guard):
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

    lock-relief G1: every call of `fake_connect` is a reach, refused for a
    test with no `skipif` mark; this fixture's own autouse open is not.
    So is every `psycopg.connect` after that open (check X1): the
    connections that bypass `db.connect` — `db.connect_migration`, the
    migration CLI, `db._open` — all end there.
    """
    if not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")):
        yield None
        return

    # An inner pytester run's `dev_db_tx` opens under the OUTER test's
    # guarded `psycopg.connect`; that open is still not a reach.
    global _opening_the_suite_connection
    _opening_the_suite_connection = True
    try:
        real = REAL_CONNECT(env.DEV_DB_NAME, side=db.Side.SYSTEM)
    finally:
        _opening_the_suite_connection = False
    real.autocommit = False
    counter = itertools.count()

    def fake_connect(dbname: str, *, side: db.Side, allow_prod: bool = False):
        _guarded_reach(request.node, offline_skip_guard)
        if dbname != env.DEV_DB_NAME:
            raise AssertionError(
                f"RULING 7.1d: a test asked for database {dbname!r}. The suite "
                f"runs against {env.DEV_DB_NAME} only."
            )
        if not isinstance(side, db.Side):
            raise AssertionError(
                f"ADR-0008: a test's store opened a connection with side={side!r}. "
                "Every store declares SIDE and the factory requires it."
            )
        proxy = _SavepointConnection(real, f"pytest_sp_{next(counter)}")
        # ADR-0008: the suite is pinned exactly the way production is —
        # same SET ROLE, same single-schema search_path, same tenant GUC,
        # through the SAME `db.apply_side` (one path). A store that
        # declares the wrong SIDE therefore fails in the ordinary tests,
        # not only in the dedicated tenancy test.
        #
        # This is safe on a SHARED connection because all three settings
        # are session-scoped and transactional: the savepoint is taken
        # first, so a rollback puts the previous side's settings back, and
        # SET ROLE is checked against the SESSION user (still the login
        # role) rather than the current one, so re-pinning always works.
        db.apply_side(proxy, side)
        return proxy

    real_psycopg_connect = db.psycopg.connect

    def guarded_psycopg_connect(*args, **kwargs):
        if not _opening_the_suite_connection:
            _guarded_reach(request.node, offline_skip_guard)  # lock-relief G1, check X1
        return real_psycopg_connect(*args, **kwargs)

    monkeypatch.setattr(db, "connect", fake_connect)
    monkeypatch.setattr(db.psycopg, "connect", guarded_psycopg_connect)
    try:
        yield real
    finally:
        real.rollback()
        real.close()


@pytest.fixture
def real_connect(request, offline_skip_guard):
    """A REAL `db.connect` — outside the suite's rollback transaction.

    ADR-0008's tenancy tests need connections the fixture has not
    intercepted: a savepoint proxy over one shared connection cannot show
    that a SYSTEM role is refused a `"user"` table, because both proxies
    are the same session. Tests using this fixture must therefore not
    leave rows behind — every one of them either reads or asserts that a
    write is REFUSED.
    """
    opened = []

    def _open(dbname: str = env.DEV_DB_NAME, *, side: db.Side):
        _guarded_reach(request.node, offline_skip_guard)  # lock-relief G1
        if dbname != env.DEV_DB_NAME:
            raise AssertionError(
                f"RULING 7.1d: a test asked for database {dbname!r}. The suite "
                f"runs against {env.DEV_DB_NAME} only."
            )
        conn = REAL_CONNECT(dbname, side=side)
        opened.append(conn)
        return conn

    try:
        yield _open
    finally:
        for conn in opened:
            conn.close()


# ---------------------------------------------------------------------
# F1: the suite runs at a fixed, non-blocked instant
# ---------------------------------------------------------------------

#: 2026-09-03 10:00 ET — a Thursday, mid-RTH, EDT. Chosen because it is
#: a full trading day in the shipped calendar and sits far from every
#: boundary, so a test that does not care about sessions never trips one.
FROZEN_NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


@pytest.fixture(autouse=True)
def frozen_session_clock(monkeypatch):
    """Freeze `cobalt.session.clock.now_utc` for the whole suite.

    The vault writer and the ASET store now REFUSE to write inside
    `market_reset` (20:00-21:00 ET). Without this fixture the suite would
    pass all day and go red for one hour every evening — a test that is
    a function of when it is run is not a test. Freezing the one
    system-clock read fixes it for every caller at once: the guard, the
    writer, and `AsetStore.save`.

    AUTOUSE and unconditional. A test that wants a different instant
    passes `now=` explicitly (the guard, the writer and the store all
    take it) or re-patches this same attribute — both of which are
    visible in the test, which is the point.
    """
    monkeypatch.setattr(session_clock_module, "now_utc", lambda: FROZEN_NOW)
    yield FROZEN_NOW


# ---------------------------------------------------------------------
# S3 C4 fix r1 — F1: a trade-note path outside tmp_path fails loud (L1, L28)
# ---------------------------------------------------------------------


def _outside_tmp_path(path) -> str:
    return (f"L28: a trade-note path resolved outside tmp_path in a test: {path}. Nothing read or "
            "written — point the test at a tmp_path vault (trade_note_support.make_vault).")


@pytest.fixture(autouse=True)
def trade_note_path_guard(monkeypatch, tmp_path_factory):
    """Wrap the trade-note writer's ONE resolver (`upsert_trade_note` and
    `write_leg_unit` both call it): a path outside the session's pytest
    base temp is recorded and refused BEFORE any read or write. The web
    note helpers swallow every exception into a notice, so the teardown
    fails the test on any recorded path. Yields the record (a test that
    trips the guard on purpose clears it)."""
    from cobalt.prefill import trade_note as trade_note_module

    base = tmp_path_factory.getbasetemp().resolve()
    original = trade_note_module.resolve_target
    tripped: list = []

    def guarded(vault_relative_dir, filename):
        path = original(vault_relative_dir, filename)
        if not path.resolve().is_relative_to(base):
            tripped.append(path)
            raise AssertionError(_outside_tmp_path(path))
        return path

    monkeypatch.setattr(trade_note_module, "resolve_target", guarded)
    yield tripped
    if tripped:
        pytest.fail("\n".join(_outside_tmp_path(path) for path in tripped))
