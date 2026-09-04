"""RULING 7 — the environment law, tested at every gate it claims.

The law: `COBALT_ENV` alone decides the database and the vault; unset
or unknown fails loud; a config file can no longer route production
writes into `cobalt_dev`; and a destructive helper refuses anything but
`cobalt_dev` no matter what the environment says.

These tests are the reason the law is a law rather than a convention.
The pre-RULING-7 failure was not that someone chose the wrong database
— it was that `configs/dev/aset.local.yaml:12` chose it for every
caller, silently, and the production ASET sheet had no way to say
otherwise.
"""

import pytest
import yaml

from cobalt import db, devdb, env, vault
from cobalt.aset.config import AsetConfig

# The autouse `dev_db_tx` fixture monkeypatches `db.connect` so no test can
# reach a real database. These two tests are ABOUT the factory's own guard,
# so they hold the unpatched function, bound at import time.
real_connect = db.connect


# ---------------------------------------------------------------------
# resolve_env / resolve_db_name — no defaults, anywhere
# ---------------------------------------------------------------------


class TestEnvResolution:
    def test_unset_raises_with_a_one_line_message(self, monkeypatch):
        monkeypatch.delenv(env.ENV_VAR, raising=False)
        with pytest.raises(env.EnvConfigError, match="COBALT_ENV is unset"):
            env.resolve_env()

    def test_unknown_value_raises_and_names_what_it_got(self, monkeypatch):
        monkeypatch.setenv(env.ENV_VAR, "staging")
        with pytest.raises(env.EnvConfigError, match="'staging'"):
            env.resolve_env()

    def test_empty_string_is_not_dev(self, monkeypatch):
        monkeypatch.setenv(env.ENV_VAR, "")
        with pytest.raises(env.EnvConfigError):
            env.resolve_env()

    @pytest.mark.parametrize(
        "mode,expected_db",
        [("production", "cobalt_brain"), ("dev", "cobalt_dev")],
    )
    def test_db_name_follows_the_mode(self, monkeypatch, mode, expected_db):
        monkeypatch.setenv(env.ENV_VAR, mode)
        assert env.resolve_db_name() == expected_db

    def test_db_name_raises_when_unset(self, monkeypatch):
        monkeypatch.delenv(env.ENV_VAR, raising=False)
        with pytest.raises(env.EnvConfigError):
            env.resolve_db_name()

    def test_is_production_is_not_a_silent_false_when_unset(self, monkeypatch):
        """The old `os.getenv(...) == "production"` shape answered False
        for an unset flag. That is exactly the silent default RULING 7
        removes."""
        monkeypatch.delenv(env.ENV_VAR, raising=False)
        with pytest.raises(env.EnvConfigError):
            env.is_production()


# ---------------------------------------------------------------------
# The vault half of the same resolver
# ---------------------------------------------------------------------


class TestVaultFollowsTheSameFlag:
    def test_vault_path_raises_when_env_unset(self, monkeypatch, tmp_path):
        monkeypatch.delenv(env.ENV_VAR, raising=False)
        monkeypatch.setenv(vault.ENV_OVERRIDE, str(tmp_path))
        with pytest.raises(env.EnvConfigError):
            vault.resolve_vault_path()

    def test_production_resolves_the_real_vault_with_no_override(self, monkeypatch):
        """Production no longer DEPENDS on COBALT_VAULT_PATH being set:
        a plist that lost the override still reaches Think, or fails —
        it can never silently land in the dev vault."""
        monkeypatch.setenv(env.ENV_VAR, env.PRODUCTION)
        monkeypatch.delenv(vault.ENV_OVERRIDE, raising=False)
        prod = vault.Path(vault.PROD_VAULT_PATH_REFERENCE)
        if not prod.is_dir():
            pytest.skip("production vault not present on this machine")
        assert vault.resolve_vault_path() == prod.resolve()


# ---------------------------------------------------------------------
# db.connect — cobalt_brain needs a production declaration
# ---------------------------------------------------------------------


class TestConnectionFactoryGate:
    def test_dev_cannot_open_the_production_database(self, monkeypatch):
        monkeypatch.setenv(env.ENV_VAR, env.DEV)
        with pytest.raises(db.DbConfigError, match="cobalt_brain"):
            real_connect("cobalt_brain")

    def test_unset_env_cannot_open_the_production_database(self, monkeypatch):
        """An unset flag must refuse, not explode with a different error
        — the refusal is the safety property."""
        monkeypatch.delenv(env.ENV_VAR, raising=False)
        with pytest.raises(db.DbConfigError, match="cobalt_brain"):
            real_connect("cobalt_brain")


# ---------------------------------------------------------------------
# RULING 7.1c — destructive helpers are hard-coded to cobalt_dev
# ---------------------------------------------------------------------


class TestDestructiveGuard:
    @pytest.mark.parametrize(
        "target", ["cobalt_brain", "postgres", "template1", "COBALT_DEV", "cobalt_dev2", ""]
    )
    def test_refuses_everything_but_cobalt_dev(self, target):
        with pytest.raises(env.EnvConfigError, match="REFUSED"):
            env.assert_destructive_target(target)

    def test_allows_cobalt_dev(self):
        env.assert_destructive_target("cobalt_dev")  # must not raise

    def test_guard_is_hard_coded_not_keyed_on_the_environment(self, monkeypatch):
        """The whole point: inside a production shell, where every other
        guard has already stood aside, a truncate against cobalt_brain
        must STILL refuse."""
        monkeypatch.setenv(env.ENV_VAR, env.PRODUCTION)
        with pytest.raises(env.EnvConfigError, match="REFUSED"):
            env.assert_destructive_target(env.PROD_DB_NAME)
        # The database guard fires first, so this surfaces as
        # EnvConfigError rather than DestructiveRefused. Either is a
        # refusal; what matters is that nothing executes.
        with pytest.raises((env.EnvConfigError, devdb.DestructiveRefused), match="REFUSED"):
            devdb.truncate(["aset_sizings"], db_name=env.PROD_DB_NAME, confirm=True)

    def test_truncate_refuses_a_table_outside_the_allowlist(self):
        with pytest.raises(devdb.DestructiveRefused, match="allowlist"):
            devdb.truncate(["bars"], confirm=True)

    def test_truncate_refuses_without_explicit_confirmation(self):
        with pytest.raises(devdb.DestructiveRefused, match="confirmation"):
            devdb.truncate(["aset_sizings"])

    def test_truncate_refuses_an_empty_table_list(self):
        with pytest.raises(devdb.DestructiveRefused):
            devdb.truncate([], confirm=True)

    def test_even_the_read_path_is_guarded(self):
        """`counts()` is read-only, but a typo'd database name must not
        be reachable through the destructive tool at all."""
        with pytest.raises(env.EnvConfigError, match="REFUSED"):
            devdb.counts(["aset_sizings"], db_name=env.PROD_DB_NAME)


# ---------------------------------------------------------------------
# The config file cannot choose the database again
# ---------------------------------------------------------------------


class TestConfigCannotRouteTheDatabase:
    def test_db_name_key_is_now_a_loud_crash(self):
        """`configs/dev/aset.local.yaml:12` is how production came to
        write into cobalt_dev. Re-adding that key must fail the config
        load, not be quietly honoured."""
        raw = yaml.safe_load(
            """
            account_size: 10000
            db_name: cobalt_dev
            daily_note:
              daily_notes_dir: "x"
              filename_pattern: "%Y-%m-%d.md"
            """
        )
        with pytest.raises(Exception) as exc:
            AsetConfig(**raw)
        assert "db_name" in str(exc.value)

    def test_aset_config_has_no_db_name_attribute(self):
        assert not hasattr(AsetConfig, "db_name")
        assert "db_name" not in AsetConfig.model_fields

    def test_the_shipped_config_files_carry_no_db_name(self):
        """Guards the actual files on disk, not just the schema."""
        from cobalt.aset import config as config_module

        for path in (config_module.CONFIG_PATH, config_module.LOCAL_CONFIG_PATH):
            if not path.exists():
                continue
            data = yaml.safe_load(path.read_text()) or {}
            assert "db_name" not in data, f"{path} still routes the database"


# ---------------------------------------------------------------------
# The stores take the database from the resolver
# ---------------------------------------------------------------------


class TestStoresFollowTheResolver:
    def test_aset_store_defaults_to_the_resolved_database(self, monkeypatch):
        from cobalt.aset.store import AsetStore

        monkeypatch.setenv(env.ENV_VAR, env.PRODUCTION)
        assert AsetStore().db_name == "cobalt_brain"
        monkeypatch.setenv(env.ENV_VAR, env.DEV)
        assert AsetStore().db_name == "cobalt_dev"

    def test_vault_write_store_defaults_to_the_resolved_database(self, monkeypatch):
        from cobalt.vaultwrite import VaultWriteStore

        monkeypatch.setenv(env.ENV_VAR, env.PRODUCTION)
        assert VaultWriteStore().db_name == "cobalt_brain"
        monkeypatch.setenv(env.ENV_VAR, env.DEV)
        assert VaultWriteStore().db_name == "cobalt_dev"

    def test_stores_raise_rather_than_default_when_env_is_unset(self, monkeypatch):
        from cobalt.aset.store import AsetStore
        from cobalt.vaultwrite import VaultWriteStore

        monkeypatch.delenv(env.ENV_VAR, raising=False)
        with pytest.raises(env.EnvConfigError):
            AsetStore()
        with pytest.raises(env.EnvConfigError):
            VaultWriteStore()
