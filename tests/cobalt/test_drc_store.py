"""DRC D1-5 — migration `0016_drc` and `DrcStore`.

OFFLINE half: the SQL, the registry and the placement map.

WITH-DB half (`requires_db`, skipped offline): the migration is applied
ONLY inside this module's own never-committed transaction on
`cobalt_dev` — the harness's migration connection, rolled back at the
end of every test — and `DrcStore` is exercised through a savepoint proxy
over that same connection. Nothing here commits a migration.
"""

from __future__ import annotations

import hashlib
import os
import re
from datetime import date, datetime, timezone
from pathlib import Path

import psycopg
import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import _apply, _rollback_paths
from cobalt.db_migrations.placement import CREATED_TABLES, DECLARED_TABLES, PLACEMENT, side_of
from cobalt.drc import trading_log
from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Kind, OpenPosition, Outcome, PairingError, SeedBook
from cobalt.drc.pairing import build_day, pair_day
from cobalt.drc.stats_log import StatsLogSource
from cobalt.drc.store import DrcStore
from cobalt.drc.trading_log import TradingLogSource

SQL = MIGRATIONS_DIR / "0016_drc.sql"
ROLLBACK = MIGRATIONS_DIR / "0016_drc.rollback.sql"
TABLES = ("drc_imports", "drc_fills", "drc_rows")

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures" / "drc"
E1 = FIXTURES / "trading_log_e1.csv"
STATS = FIXTURES / "stats_log_e1.csv"
DAY1 = FIXTURES / "trading_log_carry_day1.csv"
SEED = FIXTURES / "trading_log_carry_seed.csv"
D = date(2001, 1, 2)
D_NEXT = date(2001, 1, 3)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _code(path: Path) -> str:
    return "\n".join(l for l in path.read_text().splitlines() if not l.strip().startswith("--"))


# ---------------------------------------------------------------------
# OFFLINE — the SQL
# ---------------------------------------------------------------------


def test_the_pair_exists_and_is_registered_last():
    assert SQL.exists() and ROLLBACK.exists()
    assert FORWARD[-5] == SQL and [p.name for p in FORWARD[-4:-2]] == [
        "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
    assert REVERSE[4] == ROLLBACK and [p.name for p in REVERSE[2:4]] == [
        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]


def test_three_tables_on_the_user_side_and_no_fourth():
    code = _code(SQL)
    created = re.findall(r'CREATE TABLE IF NOT EXISTS "user"\.(\w+)', code)
    assert created == list(TABLES)
    assert "CREATE TABLE" not in code.replace('CREATE TABLE IF NOT EXISTS "user".', "")


def test_it_creates_neither_fills_nor_order_fills():
    code = _code(SQL)
    assert '"user".fills ' not in code and '"user".fills(' not in code
    assert "order_fills" not in code


@pytest.mark.parametrize("table", TABLES)
def test_every_table_carries_user_id_not_null_the_guc_default_and_the_fk(table):
    body = re.search(rf'CREATE TABLE IF NOT EXISTS "user"\.{table} \((.*?)\n\);', _code(SQL), re.S).group(1)
    assert re.search(
        r"user_id\s+INTEGER NOT NULL\s+DEFAULT \(current_setting\('cobalt\.trader_id'\)::int\)\s+"
        r'REFERENCES "user"\.traders\(id\)',
        body,
    ), table
    assert f'ALTER TABLE "user".{table} OWNER TO cobalt_user;' in _code(SQL)


def _domain(column: str) -> set[str]:
    m = re.search(rf"{column}\s+TEXT[^,]*CHECK \({column} IN \(([^)]*)\)\)", _code(SQL))
    assert m, column
    return {p.strip().strip("'") for p in m.group(1).split(",")}


def test_the_import_row_domains():
    assert _domain("kind") == {"trading_log", "stats_log", "screenshot"}
    assert _domain("parse_status") == {"parsed", "partial", "failed"}
    assert _domain("event_state") == {"pending", "running", "done", "failed"}


def test_the_import_row_carries_what_v2_names():
    body = re.search(r'"user"\.drc_imports \((.*?)\n\);', _code(SQL), re.S).group(1)
    for column in ("import_date", "kind", "name", "sha256", "trade_key", "parse_status",
                   "reason", "supersedes", "event_state"):
        assert re.search(rf"^\s+{column}\s", body, re.M), column
    assert 'supersedes      BIGINT REFERENCES "user".drc_imports(id)' in body


def test_a_fill_belongs_to_one_import_and_a_row_carries_inputs_derived_and_fn_version():
    code = _code(SQL)
    fills = re.search(r'"user"\.drc_fills \((.*?)\n\);', code, re.S).group(1)
    assert 'import_id       BIGINT NOT NULL REFERENCES "user".drc_imports(id)' in fills
    rows = re.search(r'"user"\.drc_rows \((.*?)\n\);', code, re.S).group(1)
    for column in ("kind", "inputs", "derived", "fn_version"):
        assert re.search(rf"^\s+{column}\s", rows, re.M), column
    assert _domain_of(rows, "kind") == {"trade", "open_position", "stats_row", "day"}


def _domain_of(body: str, column: str) -> set[str]:
    m = re.search(rf"{column}\s+TEXT[^,]*CHECK \({column} IN \(([^)]*)\)\)", body)
    return {p.strip().strip("'") for p in m.group(1).split(",")}


def test_the_migration_is_idempotent():
    for kind, rest in re.findall(r"CREATE (TABLE|UNIQUE INDEX|INDEX)([^;]*);", _code(SQL)):
        assert "IF NOT EXISTS" in rest, (kind, rest[:60])


def test_the_rollback_drops_exactly_the_three_tables_children_first():
    code = _code(ROLLBACK)
    assert re.findall(r'DROP TABLE IF EXISTS "user"\.(\w+);', code) == ["drc_rows", "drc_fills", "drc_imports"]
    assert code.count("DROP") == 3


def test_down_to_0011_on_this_tree_selects_only_this_rollback():
    assert [p.name for p in _rollback_paths("0011")] == [
        "0020_drc_build_kinds.rollback.sql",
        "0019_drc_events.rollback.sql",
        "0018_drc_stated_books.rollback.sql",
        "0017_voice_turns.rollback.sql",
        "0016_drc.rollback.sql",
        "0015_shadow_agreement_stale.rollback.sql",
        "0014_radar_handicap.rollback.sql",
        "0013_tunables_slug_nullable.rollback.sql",
    ]


# ---------------------------------------------------------------------
# OFFLINE — placement
# ---------------------------------------------------------------------


@pytest.mark.parametrize("table", TABLES)
def test_the_three_tables_are_built_user_side(table):
    assert side_of(table) is Side.USER
    assert CREATED_TABLES[table] is Side.USER
    assert table not in DECLARED_TABLES


def test_fills_stays_declared_and_unbuilt():
    assert DECLARED_TABLES["fills"] is Side.USER and "fills" not in CREATED_TABLES
    assert PLACEMENT["drc_rows"] is Side.USER


def test_the_store_is_user_side_and_the_only_drc_writer():
    assert DrcStore.SIDE is Side.USER
    src = Path(db.__file__).parent
    writers = [
        p.relative_to(src).as_posix()
        for p in src.rglob("*.py")
        if re.search(r"(INSERT INTO|UPDATE|DELETE FROM)\s+(\"user\"\.)?drc_", p.read_text())
    ]
    assert writers == ["drc/store.py"], writers


# ---------------------------------------------------------------------
# WITH-DB — inside one never-committed transaction
# ---------------------------------------------------------------------


class _Proxy:
    """A savepoint over the test's ONE migration connection, so the store
    sees the uncommitted tables. Never commits, never closes."""

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


@pytest.fixture
def migrated(monkeypatch):
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    counter = iter(range(10_000))
    try:
        _apply(conn, FORWARD)

        def _connect(dbname, *, side, allow_prod=False):
            assert dbname == env.DEV_DB_NAME
            proxy = _Proxy(conn, f"drc_sp_{next(counter)}")
            db.apply_side(proxy, side)
            return proxy

        monkeypatch.setattr(db, "connect", _connect)
        yield conn
    finally:
        conn.rollback()
        conn.close()


@pytest.fixture
def weekday_calendar(monkeypatch):
    """The shipped NYSE calendar covers recent years only; the fixtures'
    constructed 2001 dates get a constructed rule: the prior weekday."""
    import importlib
    from datetime import timedelta

    def _prior(day: date) -> date:
        probe = day - timedelta(days=1)
        while probe.weekday() >= 5:
            probe -= timedelta(days=1)
        return probe

    # By MODULE object: `cobalt.daymode` re-exports a function named
    # `propose`, so the dotted-string form resolves the wrong object.
    module = importlib.import_module("cobalt.daymode.propose")
    monkeypatch.setattr(module, "prior_trading_day", _prior)


def _trading(path: Path, day: date = D):
    data = path.read_bytes()
    return data, TradingLogSource().parse(data, day, detect_kind(path.name, data))


def _stats():
    data = STATS.read_bytes()
    return data, StatsLogSource().parse(data, detect_kind(STATS.name, data))


#: 10:00 ET on a constructed trading day — outside market_reset (K1).
_TEN_ET = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def _stated_flat(store: DrcStore, day: date = D) -> SeedBook:
    """K1: every recorded day names its book — here his recorded flat
    `opening` statement for `day`, as the `SeedBook` it seeds."""
    row = store.record_stated_book(day, "opening", [], via="cli", now=_TEN_ET)
    return SeedBook(source="stated", positions=[], stated_book_id=row.id, from_book_sha256=row.book_sha256)


@requires_db
def test_forward_creates_the_three_tables_user_side_with_the_tenant_column(migrated):
    for table in TABLES:
        assert migrated.execute("SELECT to_regclass(%s)", (f'"user".{table}',)).fetchone()[0]
        assert migrated.execute("SELECT to_regclass(%s)", (f"system.{table}",)).fetchone()[0] is None
    rows = migrated.execute(
        "SELECT table_name, is_nullable, column_default FROM information_schema.columns "
        "WHERE table_schema = 'user' AND column_name = 'user_id' AND table_name = ANY(%s)",
        (list(TABLES),),
    ).fetchall()
    assert {r[0] for r in rows} == set(TABLES)
    assert all(r[1] == "NO" and "cobalt.trader_id" in r[2] for r in rows)


@requires_db
def test_every_created_user_table_carries_the_tenant_column_inside_the_transaction(migrated):
    """`test_tenancy`'s live user_id assertion, run here on the migrated
    transaction (the three tables never reach `cobalt_dev` from this
    build — no committed migration)."""
    rows = migrated.execute(
        "SELECT table_name FROM information_schema.columns "
        "WHERE table_schema = 'user' AND column_name = 'user_id' AND is_nullable = 'NO'"
    ).fetchall()
    found = {r[0] for r in rows}
    for table, side in CREATED_TABLES.items():
        if side is Side.USER:
            assert table in found, table


@requires_db
def test_the_rollback_drops_them_and_forward_brings_them_back(migrated):
    # D2 fix r1: 0019's `drc_events` references `drc_imports`; its rollback goes first.
    _apply(migrated, [MIGRATIONS_DIR / "0019_drc_events.rollback.sql", ROLLBACK])
    for table in TABLES:
        assert migrated.execute("SELECT to_regclass(%s)", (f'"user".{table}',)).fetchone()[0] is None
    _apply(migrated, FORWARD)
    _apply(migrated, FORWARD)
    for table in TABLES:
        assert migrated.execute("SELECT to_regclass(%s)", (f'"user".{table}',)).fetchone()[0]


@requires_db
def test_a_parsed_trading_log_stores_one_import_row_and_every_fill(migrated):
    store = DrcStore()
    store.ensure_schema()
    data, parsed = _trading(E1)
    import_id = store.record_import(D, parsed.result, data, parsed.executions)
    row = migrated.execute(
        'SELECT kind, name, sha256, parse_status, reason, supersedes FROM "user".drc_imports WHERE id = %s',
        (import_id,),
    ).fetchone()
    assert row == ("trading_log", E1.name, hashlib.sha256(data).hexdigest(), "parsed", "", None)
    fills = migrated.execute(
        'SELECT line, symbol, side, price, qty, account FROM "user".drc_fills WHERE import_id = %s ORDER BY line',
        (import_id,),
    ).fetchall()
    assert len(fills) == 14 and fills[0][:3] == (2, "AAA", "S")


@requires_db
def test_a_failed_file_stores_its_reason_and_line_and_zero_fills(migrated):
    data = E1.read_bytes().replace(b"50.6,50", b"50.6,0", 1)
    parsed = TradingLogSource().parse(data, D, detect_kind("bad.md", data))
    assert parsed.result.outcome is Outcome.FAILED
    import_id = DrcStore().record_import(D, parsed.result, data, parsed.executions)
    status, reason, line = migrated.execute(
        'SELECT parse_status, reason, failed_line FROM "user".drc_imports WHERE id = %s', (import_id,)
    ).fetchone()
    assert status == "failed" and "line 2" in reason and line == 2
    assert migrated.execute(
        'SELECT count(*) FROM "user".drc_fills WHERE import_id = %s', (import_id,)
    ).fetchone()[0] == 0


@requires_db
def test_a_partial_file_stores_its_partial_flag_as_the_reason(migrated):
    records = E1.read_text().splitlines()
    data = ("\n".join(",".join(r.split(",")[:7] + r.split(",")[8:]) for r in records) + "\n").encode()
    parsed = TradingLogSource().parse(data, D, detect_kind("half.md", data))
    import_id = DrcStore().record_import(D, parsed.result, data, parsed.executions)
    status, reason = migrated.execute(
        'SELECT parse_status, reason FROM "user".drc_imports WHERE id = %s', (import_id,)
    ).fetchone()
    # `54` row 9: the exact reason, naming the column removed (index 7).
    assert status == "partial" and reason == f"PARTIAL — missing: {trading_log.ACCOUNT}"


@requires_db
def test_a_second_file_of_one_kind_for_one_day_supersedes_the_first(migrated):
    store = DrcStore()
    data, parsed = _trading(E1)
    first = store.record_import(D, parsed.result, data, parsed.executions)
    second = store.record_import(D, parsed.result, data, parsed.executions)
    assert migrated.execute(
        'SELECT supersedes FROM "user".drc_imports WHERE id = %s', (second,)
    ).fetchone()[0] == first


@requires_db
def test_a_day_stores_every_trade_stats_row_and_the_day_with_inputs_and_fn_version(migrated):
    """The `fn_version` pin moves to `drc.pairing/4` with K2 fix r1 (its
    `FN_VERSION` row)."""
    store = DrcStore()
    t_data, trading = _trading(E1)
    s_data, stats = _stats()
    ids = {
        Kind.TRADING_LOG: store.record_import(D, trading.result, t_data, trading.executions),
        Kind.STATS_LOG: store.record_import(D, stats.result, s_data),
    }
    seed = _stated_flat(store)
    day = build_day(trading, stats, seed=())
    written = store.record_day(day, ids, seed)
    kinds = dict(migrated.execute(
        'SELECT kind, count(*) FROM "user".drc_rows WHERE day = %s GROUP BY kind', (D,)
    ).fetchall())
    assert kinds == {"trade": 4, "stats_row": 4, "day": 1, "seed": 1, "book_close": 1}
    assert written == 11
    inputs, derived, fn = migrated.execute(
        """SELECT inputs, derived, fn_version FROM "user".drc_rows
           WHERE day = %s AND kind = 'trade' AND ref LIKE 'AAA-%%'""", (D,)
    ).fetchone()
    assert inputs["trading_log_import_id"] == ids[Kind.TRADING_LOG]
    assert sorted(inputs["fill_lines"]) == [2, 3, 4, 6, 7, 8, 9]
    assert derived["playbooks"] == ["Alpha Setup Long", "Beta Setup Long"]
    assert derived["stats"]["stop"] is None
    assert fn == "drc.pairing/4"
    # Recording the same day again replaces, never duplicates.
    store.record_day(day, ids, seed)
    assert migrated.execute(
        'SELECT count(*) FROM "user".drc_rows WHERE day = %s', (D,)
    ).fetchone()[0] == 11


@requires_db
def test_the_seed_round_trips_through_the_store(migrated, weekday_calendar):
    store = DrcStore()
    data, day1 = _trading(DAY1, D)
    ids = {Kind.TRADING_LOG: store.record_import(D, day1.result, data, day1.executions)}
    store.record_day(build_day(day1, seed=()), ids, _stated_flat(store))
    seed = store.seed_for(D_NEXT).positions
    assert [(p.symbol, p.held_shares) for p in seed] == [("DDD", 30)]
    assert isinstance(seed[0], OpenPosition)
    _, day2 = _trading(SEED, D_NEXT)
    closed = pair_day(day2.executions, D_NEXT, seed)
    (ddd,) = [t for t in closed.trades if t.symbol == "DDD"]
    assert ddd.status.value == "closed" and ddd.trade_id == seed[0].trade_id


@requires_db
def test_a_skipped_prior_trading_day_fails_the_seed_loudly(migrated, weekday_calendar):
    store = DrcStore()
    data, day1 = _trading(DAY1, D)
    ids = {Kind.TRADING_LOG: store.record_import(D, day1.result, data, day1.executions)}
    store.record_day(build_day(day1, seed=()), ids, _stated_flat(store))
    with pytest.raises(PairingError, match="prior trading day 2001-01-03 has no import"):
        store.seed_for(date(2001, 1, 4))


@requires_db
def test_the_first_import_ever_has_an_empty_seed(migrated, weekday_calendar):
    assert DrcStore().seed_for(D) is None


@requires_db
def test_the_system_role_cannot_read_the_drc_tables(migrated):
    """`54` row 7: schema-qualified, so a missing relation cannot pass."""
    migrated.execute("SAVEPOINT wrong_side")
    db.apply_side(migrated, Side.SYSTEM)
    with pytest.raises(psycopg.errors.InsufficientPrivilege):
        migrated.execute('SELECT 1 FROM "user".drc_imports')
    migrated.execute("ROLLBACK TO SAVEPOINT wrong_side")


@requires_db
def test_a_prior_day_whose_pairing_was_not_computed_fails_the_seed(migrated, weekday_calendar):
    """`54` row 2: a prior day recorded with pairing NOT computed has
    unknown open positions — the seed fails, never assumed flat."""
    records = DAY1.read_text().splitlines()
    data = ("\n".join(",".join(r.split(",")[:1] + r.split(",")[2:]) for r in records) + "\n").encode()
    day1 = TradingLogSource().parse(data, D, detect_kind("half.md", data))
    day = build_day(day1, seed=())
    assert "pairing" in day.not_computed
    store = DrcStore()
    ids = {Kind.TRADING_LOG: store.record_import(D, day1.result, data, day1.executions)}
    store.record_day(day, ids, _stated_flat(store))
    with pytest.raises(PairingError, match="2001-01-02 has pairing not computed"):
        store.seed_for(D_NEXT)


@requires_db
def test_an_open_position_row_carries_its_trades_inputs(migrated):
    """`54` row 14 (L57): the open position's inputs are its trade's."""
    store = DrcStore()
    data, day1 = _trading(DAY1, D)
    ids = {Kind.TRADING_LOG: store.record_import(D, day1.result, data, day1.executions)}
    store.record_day(build_day(day1, seed=()), ids, _stated_flat(store))
    rows = migrated.execute(
        """SELECT kind, ref, inputs FROM "user".drc_rows
           WHERE day = %s AND kind IN ('trade', 'open_position')""", (D,)
    ).fetchall()
    positions = [(ref, inputs) for kind, ref, inputs in rows if kind == "open_position"]
    trades = {ref: inputs for kind, ref, inputs in rows if kind == "trade"}
    assert len(positions) == 1
    for ref, inputs in positions:
        assert inputs == trades[ref]
        assert {"trading_log_import_id", "fill_lines", "carried_lots"} <= set(inputs)


@requires_db
def test_a_degraded_file_stores_the_names_it_added(migrated):
    """`54` row 15: `degraded` names the added column, not the bare flag.
    Widened exactly as `test_drc_trading_log.py`'s extra-column test."""
    records = E1.read_text().splitlines()
    data = ("\n".join(
        ",".join(r.split(",")[:-1] + (["Added"] if i == 0 else ["x"]) + [""]) for i, r in enumerate(records)
    ) + "\n").encode()
    parsed = TradingLogSource().parse(data, D, detect_kind("wide.md", data))
    assert parsed.result.extras == ["Added"]
    import_id = DrcStore().record_import(D, parsed.result, data, parsed.executions)
    assert migrated.execute(
        'SELECT degraded FROM "user".drc_imports WHERE id = %s', (import_id,)
    ).fetchone()[0] == "trading_log_shape: Added"
