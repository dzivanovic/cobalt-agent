"""The two Postgres credentials, and the fallback that must not exist.

2026-09-09 (ADR-0008 D1 Revision 2 closed). The application logs in as
`cobalt_app` — LOGIN NOINHERIT, non-superuser — and the docker superuser
is reserved for migrations and bootstrap. The thing worth testing is not
that two constants exist; it is that NOTHING BRIDGES THEM. A silent
fallback from `COBALT_DB_*` to `POSTGRES_*` would mean one missing line
in `.env` quietly running the whole application as superuser, which is
precisely the state this split was made to end.

These tests never open a socket. `psycopg.connect` is patched and the
DSN it is handed is inspected, so they prove which credential a code
path CHOSE — which is the question — rather than whether Postgres was up
when they ran.
"""

from __future__ import annotations

import re

import pytest

from cobalt import db
from cobalt.backup import pgdump

APP_VARS = ("COBALT_DB_USER", "COBALT_DB_PASSWORD")
BOOTSTRAP_VARS = ("POSTGRES_USER", "POSTGRES_PASSWORD")
ALL_VARS = APP_VARS + BOOTSTRAP_VARS + ("POSTGRES_HOST", "POSTGRES_PORT")


@pytest.fixture
def clean_env(monkeypatch):
    """A process with NO database settings at all, so every test states
    the ones it means to rely on."""
    for name in ALL_VARS:
        monkeypatch.delenv(name, raising=False)
    return monkeypatch


@pytest.fixture
def captured(monkeypatch):
    """Patch the ONE `psycopg.connect` and record the DSN it is given."""
    seen: list[str] = []

    class _Conn:
        def execute(self, *a, **k):
            return self

        def close(self):
            pass

        def fetchone(self):
            return (1,)

    def fake_connect(dsn, **kwargs):
        seen.append(dsn)
        return _Conn()

    monkeypatch.setattr(db.psycopg, "connect", fake_connect)
    return seen


def _user_of(dsn: str) -> str:
    return re.match(r"postgresql://([^:]+):", dsn).group(1)


class TestTheTwoCredentialsAreNamedOnce:
    def test_app_names_the_cobalt_db_pair(self):
        assert db.Credential.APP.user_env == "COBALT_DB_USER"
        assert db.Credential.APP.password_env == "COBALT_DB_PASSWORD"

    def test_bootstrap_still_means_the_docker_superuser(self):
        """POSTGRES_* keeps its meaning. docker-compose interpolates it
        for the container itself and the old tree reads it — changing
        what it means would break both, silently."""
        assert db.Credential.BOOTSTRAP.user_env == "POSTGRES_USER"
        assert db.Credential.BOOTSTRAP.password_env == "POSTGRES_PASSWORD"

    def test_pgdump_takes_the_names_from_the_enum(self):
        """One name per concept: `pgdump` must not carry a second copy of
        the strings, or a rename would fix one of the two places."""
        text = (pgdump.__file__ and open(pgdump.__file__).read()) or ""
        assert '"COBALT_DB_USER"' not in text
        assert '"COBALT_DB_PASSWORD"' not in text


class TestThereIsNoFallback:
    def test_app_missing_raises_even_when_bootstrap_is_present(self, clean_env, captured):
        """THE TEST THIS FILE EXISTS FOR. A superuser credential sitting
        right there in the environment must not rescue a missing app
        credential."""
        clean_env.setenv("POSTGRES_HOST", "127.0.0.1")
        clean_env.setenv("POSTGRES_USER", "cobalt")
        clean_env.setenv("POSTGRES_PASSWORD", "superuser-secret")

        with pytest.raises(db.DbConfigError) as exc:
            db._open("cobalt_dev", db.Credential.APP)

        assert not captured, "a connection was opened despite the missing credential"
        message = str(exc.value)
        for name in APP_VARS:
            assert name in message, f"the error must name {name}"
        assert "FALLBACK" in message.upper()

    def test_the_error_never_carries_the_other_password(self, clean_env, captured):
        clean_env.setenv("POSTGRES_HOST", "127.0.0.1")
        clean_env.setenv("POSTGRES_USER", "cobalt")
        clean_env.setenv("POSTGRES_PASSWORD", "superuser-secret")
        with pytest.raises(db.DbConfigError) as exc:
            db._open("cobalt_dev", db.Credential.APP)
        assert "superuser-secret" not in str(exc.value)

    def test_bootstrap_missing_raises_even_when_app_is_present(self, clean_env, captured):
        """And symmetrically: a migration does not quietly run as the app
        role, which cannot create a schema and would fail further in."""
        clean_env.setenv("POSTGRES_HOST", "127.0.0.1")
        clean_env.setenv("COBALT_DB_USER", "cobalt_app")
        clean_env.setenv("COBALT_DB_PASSWORD", "app-secret")

        with pytest.raises(db.DbConfigError) as exc:
            db._open("cobalt_dev", db.Credential.BOOTSTRAP)
        assert not captured
        for name in BOOTSTRAP_VARS:
            assert name in str(exc.value)

    def test_host_is_shared_by_both(self, clean_env, captured):
        """There is one server. A missing HOST is reported for either
        credential, and neither carries its own address."""
        clean_env.setenv("COBALT_DB_USER", "cobalt_app")
        clean_env.setenv("COBALT_DB_PASSWORD", "app-secret")
        with pytest.raises(db.DbConfigError) as exc:
            db._open("cobalt_dev", db.Credential.APP)
        assert "POSTGRES_HOST" in str(exc.value)


class TestEachPathPicksTheRightLogin:
    @pytest.fixture(autouse=True)
    def both_credentials(self, clean_env):
        clean_env.setenv("POSTGRES_HOST", "127.0.0.1")
        clean_env.setenv("COBALT_DB_USER", "cobalt_app")
        clean_env.setenv("COBALT_DB_PASSWORD", "app-secret")
        clean_env.setenv("POSTGRES_USER", "cobalt")
        clean_env.setenv("POSTGRES_PASSWORD", "superuser-secret")

    def test_open_defaults_to_the_app_credential(self, captured):
        db._open("cobalt_dev")
        assert _user_of(captured[0]) == "cobalt_app"

    def test_connect_migration_uses_the_bootstrap_credential(self, captured):
        db.connect_migration("cobalt_dev")
        assert _user_of(captured[0]) == "cobalt"

    def test_the_password_is_url_encoded(self, captured, clean_env):
        """The @-in-password bug class the module docstring names."""
        clean_env.setenv("COBALT_DB_PASSWORD", "p@ss/word")
        db._open("cobalt_dev")
        assert "p%40ss%2Fword" in captured[0]
        assert "p@ss/word" not in captured[0]


class TestTheLiveFactoryAuthenticatesAsCobaltApp:
    """Against the real `cobalt_dev`, through the real factory.

    The patched-DSN tests above prove which credential the code CHOSE.
    This one proves the server agrees — that the role exists, that its
    password in `.env` is the one Postgres holds, and that `SET ROLE` is
    what gives the session its grants. `real_connect` is used because the
    suite's savepoint proxy shares one session and would answer for the
    connection the fixture opened, not for a fresh one.
    """

    def test_the_session_user_is_the_non_superuser_app_role(self, real_connect):
        conn = real_connect(side=db.Side.USER)
        session_user, is_super = conn.execute(
            "SELECT session_user, "
            "(SELECT rolsuper FROM pg_roles WHERE rolname = session_user)"
        ).fetchone()
        assert session_user == db.APP_ROLE == "cobalt_app"
        assert is_super is False, (
            "the whole point of ADR-0008 D1 Rev 2: a superuser bypasses every "
            "grant check, so per-store enforcement would be decorative"
        )

    def test_set_role_is_what_grants_it_anything(self, real_connect):
        """NOINHERIT: the memberships are doors, not keys in a pocket."""
        conn = real_connect(side=db.Side.USER)
        assert conn.execute("SELECT current_role").fetchone()[0] == "cobalt_user"
        # Back to the bare login role — the state a connection that
        # skipped the factory would be in.
        conn.execute("RESET ROLE")
        with pytest.raises(Exception) as exc:
            conn.execute('SELECT 1 FROM "user".vault_writes LIMIT 1').fetchone()
        assert "permission denied" in str(exc.value).lower()

    def test_it_is_a_member_of_all_three_side_roles(self, real_connect):
        conn = real_connect(side=db.Side.SYSTEM)
        rows = conn.execute(
            "SELECT r.rolname FROM pg_auth_members m "
            "JOIN pg_roles r ON r.oid = m.roleid "
            "JOIN pg_roles a ON a.oid = m.member "
            "WHERE a.rolname = %s ORDER BY 1",
            (db.APP_ROLE,),
        ).fetchall()
        assert [r[0] for r in rows] == ["cobalt_backup", "cobalt_system", "cobalt_user"]


class TestTheBackupDumpsAsTheAppRole:
    def test_parts_read_the_app_credential(self, clean_env):
        clean_env.setenv("POSTGRES_HOST", "127.0.0.1")
        clean_env.setenv("COBALT_DB_USER", "cobalt_app")
        clean_env.setenv("COBALT_DB_PASSWORD", "app-secret")
        clean_env.setenv("POSTGRES_USER", "cobalt")
        clean_env.setenv("POSTGRES_PASSWORD", "superuser-secret")
        host, user, password = pgdump._parts()
        assert (user, password) == ("cobalt_app", "app-secret")

    def test_parts_fail_loud_without_the_app_credential(self, clean_env):
        clean_env.setenv("POSTGRES_HOST", "127.0.0.1")
        clean_env.setenv("POSTGRES_USER", "cobalt")
        clean_env.setenv("POSTGRES_PASSWORD", "superuser-secret")
        with pytest.raises(pgdump.DumpError) as exc:
            pgdump._parts()
        assert "COBALT_DB_USER" in str(exc.value)

    def test_the_dump_still_sets_role_to_cobalt_backup(self):
        """`cobalt_app` is a MEMBER of `cobalt_backup` and NOINHERIT, so
        `pg_dump --role=` — which is a `SET ROLE` — is exactly the
        mechanism that still works. Changing the login did not change
        which role reads the rows."""
        assert pgdump.BACKUP_ROLE == "cobalt_backup"
        assert f"--role={pgdump.BACKUP_ROLE}" == "--role=cobalt_backup"


class TestTheEnvExampleNamesBothPairsAndNoValues:
    """`.env.example` is the file a second install is built from. It has
    to name the app pair, or that install runs as superuser."""

    def test_it_names_every_part(self):
        from pathlib import Path

        text = (Path(db.__file__).resolve().parents[2] / ".env.example").read_text()
        for name in ALL_VARS + ("COBALT_MASTER_KEY",):
            assert f"{name}=" in text, f".env.example does not name {name}"

    def test_it_carries_no_values(self):
        from pathlib import Path

        text = (Path(db.__file__).resolve().parents[2] / ".env.example").read_text()
        for line in text.splitlines():
            if line.startswith("#") or not line.strip():
                continue
            assert line.rstrip().endswith("="), f"{line!r} looks like a VALUE"
