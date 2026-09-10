"""ADR-0008 — the two-layer data model, asserted against `cobalt_dev`.

Five things are tested here and each one closes a different way of
getting the split wrong:

1. PLACEMENT — every table that exists is on the side someone ruled on,
   and `public` still holds nothing but the old tree's frozen 17.
2. WRONG SIDE — a system-side connection cannot read user data, and a
   user-side connection cannot reach a system table without qualifying
   it. Both failures are loud and they are different failures, which is
   the point: one is a grant, the other is a search_path.
3. THE TENANT GUC — a connection that did not come through the factory
   has no `cobalt.trader_id`, and every INSERT into a user-side table
   fails rather than inventing an owner for the row.
4. LINT — one factory, one spelling of the reserved schema name, and no
   store naming another side's table unqualified. Grep tests, because
   the property is about the SOURCE, not about a run.
5. ROUND TRIP — `db migrate` twice is idempotent, and rollback then
   re-migrate lands on identical content digests.

Tests 1-3 use the `real_connect` fixture (a connection OUTSIDE the
suite's rollback transaction) because the transaction fixture hands every
store a savepoint proxy over ONE shared session, and one session cannot
demonstrate that two roles see different things. None of them writes a
row: they read, or they assert that a write is refused.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import psycopg
import pytest

from cobalt import db, env, tenant
from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import DIGEST_EXCLUDED_COLUMNS, _apply, _probe
from cobalt.db_migrations.placement import (
    MOVED_TABLES,
    OLD_TREE_PUBLIC_TABLES,
    PLACEMENT,
    SEEDED_TABLES,
    side_of,
    tables_on,
)

#: The UNPATCHED factory. `dev_db_tx` replaces `db.connect` during every
#: test; the tests about the factory's own signature need the real one,
#: and module import happens before any fixture runs.
RAW_CONNECT = db.connect

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC = REPO_ROOT / "src" / "cobalt"

#: Every module that owns a store, with the side it declares. Read from
#: the classes themselves so a store that changes its mind about its side
#: changes this list, not a second copy of it.
def _stores():
    from cobalt.archiver.store import BarStore
    from cobalt.aset.store import AsetStore
    from cobalt.cards.store import CardStore
    from cobalt.daymode.store import DayModeStore
    from cobalt.jobs.store import JobStore
    from cobalt.notify.store import EmailSendStore
    from cobalt.redact.store import RedactionStore
    from cobalt.session.store import SessionBlockStore
    from cobalt.taxonomy.store import TradeDefStore
    from cobalt.vaultwrite.store import VaultWriteStore

    return [
        BarStore, AsetStore, CardStore, DayModeStore, JobStore,
        EmailSendStore, RedactionStore, SessionBlockStore, TradeDefStore,
        VaultWriteStore,
    ]


def _relations(conn) -> dict[str, list[str]]:
    """{schema: [relation, ...]} for the three schemas that matter."""
    rows = conn.execute(
        """
        SELECT schemaname, tablename FROM pg_tables
         WHERE schemaname IN ('public', 'user', 'system')
        UNION ALL
        SELECT schemaname, viewname FROM pg_views
         WHERE schemaname IN ('public', 'user', 'system')
        """
    ).fetchall()
    out: dict[str, list[str]] = {"public": [], "user": [], "system": []}
    for schema, name in rows:
        out[schema].append(name)
    return out


# ---------------------------------------------------------------------
# 1. Placement
# ---------------------------------------------------------------------


class TestPlacement:
    def test_every_table_is_on_its_ruled_side(self, real_connect):
        conn = real_connect(side=Side.SYSTEM)
        rel = _relations(conn)
        misplaced = []
        for schema in ("user", "system"):
            for name in rel[schema]:
                if name not in PLACEMENT:
                    misplaced.append(f"{schema}.{name}: not in the placement map")
                elif PLACEMENT[name].schema != schema:
                    misplaced.append(
                        f"{schema}.{name}: ruled {PLACEMENT[name].schema}"
                    )
        assert not misplaced, (
            "ADR-0008 D2: every table is declared on exactly one side in "
            "cobalt/db_migrations/placement.py before it is created.\n  "
            + "\n  ".join(misplaced)
        )

    def test_public_holds_nothing_but_the_frozen_old_tree(self, real_connect):
        """The strangler line, as a test.

        `cobalt_dev` has none of the 17 (they only ever existed in
        `cobalt_brain`), so this asserts CONTAINMENT, not equality — and
        that is the assertion that matters either way: a NEW table landing
        in `public` fails here.
        """
        conn = real_connect(side=Side.SYSTEM)
        strays = sorted(set(_relations(conn)["public"]) - OLD_TREE_PUBLIC_TABLES)
        assert not strays, (
            f"tables in `public` that are not the old tree's: {strays}. Every "
            "new table belongs on a side (ADR-0008 D2); `public` is frozen."
        )

    def test_all_twelve_moved_tables_exist_on_their_side(self, real_connect):
        conn = real_connect(side=Side.SYSTEM)
        rel = _relations(conn)
        for table, side in {**MOVED_TABLES, **SEEDED_TABLES}.items():
            assert table in rel[side.schema], (
                f"{table} is not in {side.schema} — run `cobalt db migrate`."
            )

    def test_sql_and_python_placement_maps_agree(self):
        """0002 is the SQL copy of the map; placement.py is the Python one.

        Two copies is one more than the one-path rule likes, and this is
        the reason it is tolerable: the SQL cannot import Python and the
        test makes a drift between them a failure rather than a surprise.
        """
        sql_text = (MIGRATIONS_DIR / "0002_move_tables.sql").read_text()
        pairs = set(
            re.findall(r"\('(user|system)',\s*'([a-z_]+)'\)", sql_text)
        )
        from_sql = {table: side for side, table in pairs}
        assert from_sql == {t: s.schema for t, s in MOVED_TABLES.items()}

    def test_declared_future_tables_are_named_on_a_side(self):
        """ADR-0008 D2 names the S2/S3 tables before they are built."""
        for name in ("trade_defs", "tunables", "trader_settings",
                     "radar_pool", "radar_membership", "missed"):
            assert name in PLACEMENT, f"{name} has no ruled side"
        assert side_of("trade_defs") is Side.USER
        assert side_of("radar_membership") is Side.SYSTEM
        assert "traders" in tables_on(Side.USER)


# ---------------------------------------------------------------------
# 2. Wrong side
# ---------------------------------------------------------------------


class TestWrongSide:
    def test_system_side_cannot_read_a_user_table(self, real_connect):
        """The grant. `cobalt_system` has NOTHING on `"user"` — system
        never reads user data, which is the whole of L32 in one clause."""
        conn = real_connect(side=Side.SYSTEM)
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            conn.execute('SELECT count(*) FROM "user".aset_sizings').fetchone()

    def test_user_side_cannot_reach_a_system_table_unqualified(self, real_connect):
        """The search_path. `bars` is not on it, so the name does not
        resolve — a different failure from the one above, on purpose."""
        conn = real_connect(side=Side.USER)
        with pytest.raises(psycopg.errors.UndefinedTable):
            conn.execute("SELECT count(*) FROM bars").fetchone()

    def test_user_side_reads_a_system_table_when_it_qualifies_it(self, real_connect):
        """Cross-side reads are legal and are written schema-qualified —
        that is exactly how S2-P2's detector reads `system.bars`."""
        conn = real_connect(side=Side.USER)
        assert conn.execute("SELECT count(*) FROM system.bars").fetchone()[0] >= 0

    def test_user_side_cannot_write_a_system_table(self, real_connect):
        conn = real_connect(side=Side.USER)
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            conn.execute(
                "INSERT INTO system.cobalt_redactions (channel, pattern, hits) "
                "VALUES ('test', 'test', 1)"
            )

    def test_each_side_is_pinned_to_its_own_schema_and_role(self, real_connect):
        for side in Side:
            conn = real_connect(side=side)
            assert conn.execute("SELECT current_role").fetchone()[0] == side.role
            # `user` is reserved, so the server echoes it back quoted.
            expected = '"user"' if side is Side.USER else "system"
            assert conn.execute("SHOW search_path").fetchone()[0] == expected

    def test_every_store_declares_a_side(self):
        for store in _stores():
            assert isinstance(store.SIDE, Side), f"{store.__name__} has no SIDE"

    def test_connect_without_a_side_is_refused(self):
        with pytest.raises(TypeError):
            RAW_CONNECT(env.DEV_DB_NAME)  # type: ignore[call-arg]
        with pytest.raises(db.DbConfigError, match="side="):
            RAW_CONNECT(env.DEV_DB_NAME, side="user")  # type: ignore[arg-type]


# ---------------------------------------------------------------------
# 3. The tenant GUC
# ---------------------------------------------------------------------


class TestTenantGuc:
    def test_the_factory_sets_the_configured_trader(self, real_connect):
        conn = real_connect(side=Side.USER)
        got = conn.execute(
            "SELECT current_setting(%s)", (tenant.TRADER_GUC,)
        ).fetchone()[0]
        assert got == str(tenant.trader_id())

    def test_an_insert_without_the_guc_fails_loud(self, real_connect):
        """No literal default anywhere: a connection that did not pass
        through the factory cannot write a user-side row at all."""
        conn = real_connect(side=Side.USER)
        conn.autocommit = False
        try:
            conn.execute("SELECT set_config(%s, '', false)", (tenant.TRADER_GUC,))
            with pytest.raises(psycopg.errors.InvalidTextRepresentation):
                conn.execute(
                    "INSERT INTO vault_writes "
                    "(note, hash_after, writer, run_id, session) "
                    "VALUES ('TENANCY-TEST', 'h', 'w', 'r', 'rth')"
                )
        finally:
            conn.rollback()

    def test_every_user_table_carries_user_id_not_null_with_the_guc_default(
        self, real_connect
    ):
        conn = real_connect(side=Side.USER)
        rows = conn.execute(
            """
            SELECT table_name, is_nullable, column_default
              FROM information_schema.columns
             WHERE table_schema = 'user' AND column_name = 'user_id'
            """
        ).fetchall()
        found = {r[0]: (r[1], r[2]) for r in rows}
        for table in MOVED_TABLES:
            if MOVED_TABLES[table] is not Side.USER:
                continue
            assert table in found, f"{table} has no user_id column"
            nullable, default = found[table]
            assert nullable == "NO"
            assert "current_setting" in default and "cobalt.trader_id" in default
            assert not re.search(r"DEFAULT\s+\d", default or "")

    def test_traders_is_seeded_with_exactly_the_configured_id(self, real_connect):
        conn = real_connect(side=Side.USER)
        row = conn.execute(
            "SELECT handle FROM traders WHERE id = %s", (tenant.trader_id(),)
        ).fetchone()
        assert row is not None and row[0] == "primary"

    def test_tenant_config_is_committed_and_validated(self):
        assert tenant.CONFIG_PATH.exists()
        assert tenant.load_tenant_config().trader_id >= 1

    def test_tenant_config_fails_loud_on_a_bad_value(self, tmp_path):
        bad = tmp_path / "tenant.yaml"
        bad.write_text("trader_id: 0\n")
        with pytest.raises(tenant.TenantConfigError):
            tenant.load_tenant_config(path=bad)
        missing = tmp_path / "nope.yaml"
        with pytest.raises(tenant.TenantConfigError):
            tenant.load_tenant_config(path=missing)


# ---------------------------------------------------------------------
# 4. Lint — properties of the source, not of a run
# ---------------------------------------------------------------------


def _python_files() -> list[Path]:
    return sorted(p for p in SRC.rglob("*.py") if "__pycache__" not in p.parts)


def _sql_files() -> list[Path]:
    return sorted(SRC.rglob("*.sql"))


class TestOneFactoryLint:
    def test_no_psycopg_connect_outside_db_py(self):
        offenders = [
            f"{p.relative_to(REPO_ROOT)}:{i}"
            for p in _python_files()
            if p.name != "db.py"
            for i, line in enumerate(p.read_text().splitlines(), 1)
            if re.search(r"\bpsycopg\.connect\(", line)
        ]
        assert not offenders, (
            "TRIAGE secrets law + ADR-0008 D1: `cobalt.db` is the ONE connection "
            f"factory. Second `psycopg.connect` at: {offenders}"
        )

    def test_db_py_has_exactly_one_psycopg_connect(self):
        text = (SRC / "db.py").read_text()
        assert len(re.findall(r"\bpsycopg\.connect\(", text)) == 1

    #: `connect_migration()` is the ONE documented exception to
    #: `connect(side=...)`: it opens a session with no `SET ROLE`, which is
    #: the privilege model switched off. It exists because 0001 creates the
    #: schemas, roles and ownership that neither side role may touch — and
    #: for no other reason. So it gets the same treatment as
    #: `psycopg.connect`: exactly one caller, named here, and a second one
    #: fails the suite rather than quietly becoming a habit.
    MIGRATION_CALLER = "src/cobalt/db_migrations/cli.py"

    def test_connect_migration_has_exactly_one_caller(self):
        callers = [
            f"{p.relative_to(REPO_ROOT)}:{i}"
            for p in _python_files()
            if p.name != "db.py"
            for i, line in enumerate(p.read_text().splitlines(), 1)
            if re.search(r"\bconnect_migration\(", line)
        ]
        assert len(callers) == 1 and callers[0].startswith(self.MIGRATION_CALLER), (
            "ADR-0008 D1: `db.connect_migration()` opens a session with NO SET "
            "ROLE. Its one caller is the migration harness "
            f"({self.MIGRATION_CALLER}) — every other path takes a side. "
            f"Found: {callers}"
        )


class TestReservedWordLint:
    #: `user` is reserved (PG16, pg_get_keywords catcode R). Anything that
    #: reaches the server naming that schema must be quoted. The negative
    #: lookbehind lets `session_user.`, `current_user.` and `"user".`
    #: through and catches a bare `user.`.
    UNQUOTED = re.compile(r'(?<![\w"])user\.')

    def test_no_unquoted_user_schema_reference_in_python(self):
        offenders = []
        for path in _python_files():
            for i, line in enumerate(path.read_text().splitlines(), 1):
                if self.UNQUOTED.search(line):
                    offenders.append(f"{path.relative_to(REPO_ROOT)}:{i}")
        assert not offenders, (
            'ADR-0008 ruling 0: the `"user"` schema is ALWAYS quoted — '
            f"`sql.Identifier` in Python. Unquoted at: {offenders}"
        )

    def test_no_unquoted_user_schema_reference_in_sql(self):
        offenders = []
        for path in _sql_files():
            for i, line in enumerate(path.read_text().splitlines(), 1):
                if line.strip().startswith("--"):
                    continue
                if self.UNQUOTED.search(line):
                    offenders.append(f"{path.relative_to(REPO_ROOT)}:{i}")
        assert not offenders, (
            f'ADR-0008 ruling 0: quote the `"user"` schema. Unquoted at: {offenders}'
        )

    def test_the_lint_would_actually_catch_one(self):
        """A lint nobody has seen fail is a lint nobody should trust."""
        assert self.UNQUOTED.search("SELECT * FROM user.aset_sizings")
        assert not self.UNQUOTED.search('SELECT * FROM "user".aset_sizings')
        assert not self.UNQUOTED.search("SELECT session_user.foo")


class TestStoresNameOnlyTheirOwnSide:
    #: Table position in the SQL the stores and migrations actually write.
    NAMED = re.compile(
        r"\b(?:FROM|JOIN|INTO|UPDATE|TABLE)\s+"
        r"(?:IF\s+NOT\s+EXISTS\s+)?(?:ONLY\s+)?"
        r'("?[A-Za-z_][A-Za-z0-9_]*"?(?:\.[A-Za-z_][A-Za-z0-9_]*)?)',
        re.IGNORECASE,
    )

    def _sources(self, store) -> list[Path]:
        module_dir = Path(sys.modules[store.__module__].__file__).parent
        return [module_dir / "store.py", *sorted(
            (module_dir / "migrations").glob("*.sql")
        )]

    def test_every_reference_is_own_side_or_qualified(self):
        offenders = []
        for store in _stores():
            for path in self._sources(store):
                if not path.exists():
                    continue
                text = "\n".join(
                    line for line in path.read_text().splitlines()
                    if not line.strip().startswith("--")
                )
                for raw in self.NAMED.findall(text):
                    if "." in raw:
                        qualifier = raw.split(".", 1)[0].strip('"')
                        if qualifier not in ("user", "system"):
                            continue  # not a schema qualifier we rule on
                        continue      # a qualified cross-side read is legal
                    name = raw.strip('"')
                    if name not in PLACEMENT:
                        continue      # pg_catalog, a CTE, a keyword
                    if PLACEMENT[name] is not store.SIDE:
                        offenders.append(
                            f"{path.relative_to(REPO_ROOT)}: {store.__name__} "
                            f"(SIDE={store.SIDE.value}) names {name} "
                            f"({PLACEMENT[name].value}) unqualified"
                        )
        assert not offenders, (
            "ADR-0008 D1: a store names only its OWN side's tables unqualified; "
            "every cross-side reference is schema-qualified.\n  "
            + "\n  ".join(sorted(set(offenders)))
        )

    def test_the_regex_finds_the_tables_it_is_supposed_to(self):
        found = self.NAMED.findall(
            "INSERT INTO bars (x) SELECT 1 FROM aset_sizings "
            'JOIN "user".vault_writes ON true'
        )
        assert found == ["bars", "aset_sizings", '"user".vault_writes']


# ---------------------------------------------------------------------
# 5. Round trip
# ---------------------------------------------------------------------


def test_heartbeat_migration_is_registered_with_a_named_rollback():
    assert FORWARD[-1].name == "0003_heartbeat_vault_outcome.sql"
    assert REVERSE[0].name == "0003_heartbeat_vault_outcome.rollback.sql"
    assert "cobalt_jobs" in FORWARD[-1].read_text()
    rollback = REVERSE[0].read_text()
    assert "DROP COLUMN IF EXISTS vault_outcome" in rollback
    assert "DROP COLUMN IF EXISTS vault_reason" in rollback
    assert {"vault_outcome", "vault_reason"} <= set(DIGEST_EXCLUDED_COLUMNS)


def test_populated_job_row_digest_is_unchanged_by_heartbeat_migration():
    """Exercise 0003 and its rollback around a real populated row.

    PostgreSQL DDL is transactional, so the inserted proof row and both shape
    changes disappear together at the end of this test.
    """
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    try:
        _apply(conn, [FORWARD[-1]])
        conn.execute(
            "INSERT INTO system.cobalt_jobs "
            "(label, kind, timeout_s, heartbeat_source, last_result) "
            "VALUES (%s, 'one-shot', 300, 'self', %s::jsonb) "
            "ON CONFLICT (label) DO UPDATE SET last_result = EXCLUDED.last_result",
            ("com.cobalt.digest-proof", '{"green": true}'),
        )
        _apply(conn, [REVERSE[0]])
        before = _probe(conn, "cobalt_jobs")
        _apply(conn, [FORWARD[-1]])
        after = _probe(conn, "cobalt_jobs")

        assert before["rows"] and before["rows"] > 0
        assert after["rows"] == before["rows"]
        assert after["digest"] == before["digest"]
    finally:
        conn.rollback()
        conn.close()


def _migrate(*args: str) -> str:
    """Run the real CLI in a child process, against `cobalt_dev`."""
    proc = subprocess.run(
        [sys.executable, "-m", "cobalt.cli", "db", "migrate", *args],
        cwd=REPO_ROOT,
        env={**__import__("os").environ, env.ENV_VAR: env.DEV},
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    return proc.stdout


def _digests(out: str) -> dict[str, str]:
    """{table: digest-after} from a proof table."""
    rows = {}
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 9 and parts[1] in ("user", "system"):
            rows[parts[0]] = parts[-2]
    return rows


class TestMigrationRoundTrip:
    """The migration harness, exercised for real on `cobalt_dev`.

    Runs the CLI in a SUBPROCESS: `db migrate` commits, and the suite's
    rollback transaction must not be the thing that decides whether a
    migration happened. It ends with the database migrated, which is the
    state every other test in the suite needs.
    """

    def test_twice_is_idempotent_and_the_rollback_round_trips(self):
        first = _digests(_migrate())
        second = _digests(_migrate())
        assert first and first == second, "db migrate is not idempotent"

        rolled_back = _migrate("--rollback")
        assert "-> public" in rolled_back
        again = _digests(_migrate())
        assert again == first, (
            "rollback + re-migrate changed the content digests — the reverse "
            "script is not catalog-only"
        )

    def test_the_proof_table_names_every_ruled_table(self):
        out = _migrate()
        for table in {**MOVED_TABLES, **SEEDED_TABLES}:
            assert table in out
        assert "content UNCHANGED on every table." in out


# ---------------------------------------------------------------------
# ensure_schema refuses to run on an unmigrated database
# ---------------------------------------------------------------------


def test_assert_schemas_exist_names_the_command(real_connect):
    conn = real_connect(side=Side.SYSTEM)
    db.assert_schemas_exist(conn)  # migrated: silent

    class _Fake:
        def execute(self, *_a, **_k):
            class _R:
                def fetchall(self):
                    return [("system",)]
            return _R()

    with pytest.raises(db.SchemaMissingError, match="cobalt db migrate"):
        db.assert_schemas_exist(_Fake())
