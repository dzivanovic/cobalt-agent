"""ONE vault-path resolver tests — fail-loud, env override, missing path."""

from pathlib import Path

import pytest

from cobalt import vault as vault_module
from cobalt.vault import VaultConfigError, resolve_vault_path


def test_committed_config_resolves_the_real_vault():
    # The real, ambient config — asserts loose invariants only, so this
    # stays true regardless of exactly where the vault lives.
    path = resolve_vault_path()
    assert path.is_dir()


def test_env_override_wins_over_config(monkeypatch, tmp_path):
    monkeypatch.setenv(vault_module.ENV_OVERRIDE, str(tmp_path))
    assert resolve_vault_path() == tmp_path.resolve()


def test_env_override_rejects_missing_path(monkeypatch, tmp_path):
    monkeypatch.setenv(vault_module.ENV_OVERRIDE, str(tmp_path / "does-not-exist"))
    with pytest.raises(VaultConfigError, match="does not exist"):
        resolve_vault_path()


def test_missing_config_and_no_env_crashes(monkeypatch, tmp_path):
    monkeypatch.delenv(vault_module.ENV_OVERRIDE, raising=False)
    monkeypatch.setattr(vault_module, "CONFIG_PATH", tmp_path / "absent.yaml")
    with pytest.raises(VaultConfigError, match="not found"):
        resolve_vault_path()


def test_config_pointing_at_missing_path_crashes(monkeypatch, tmp_path):
    monkeypatch.delenv(vault_module.ENV_OVERRIDE, raising=False)
    bad = tmp_path / "vault.yaml"
    bad.write_text(f"obsidian_vault_path: {tmp_path / 'nope'}\n")
    monkeypatch.setattr(vault_module, "CONFIG_PATH", bad)
    with pytest.raises(VaultConfigError, match="does not exist"):
        resolve_vault_path()


def test_config_resolves_a_real_directory(monkeypatch, tmp_path):
    monkeypatch.delenv(vault_module.ENV_OVERRIDE, raising=False)
    real_dir = tmp_path / "vault-root"
    real_dir.mkdir()
    cfg_file = tmp_path / "vault.yaml"
    cfg_file.write_text(f"obsidian_vault_path: {real_dir}\n")
    monkeypatch.setattr(vault_module, "CONFIG_PATH", cfg_file)
    assert resolve_vault_path() == real_dir.resolve()


def test_unknown_key_rejected(monkeypatch, tmp_path):
    monkeypatch.delenv(vault_module.ENV_OVERRIDE, raising=False)
    bad = tmp_path / "vault.yaml"
    bad.write_text(f"obsidian_vault_path: {tmp_path}\nsurprise_key: 1\n")
    monkeypatch.setattr(vault_module, "CONFIG_PATH", bad)
    with pytest.raises(VaultConfigError, match="invalid vault config"):
        resolve_vault_path()


class TestProductionGate:
    """Defect 1 (2026-09-01): a stale ASET process ran for 6+ hours
    against ~/dev-vault-cobalt after ops/start_aset.sh gained its
    COBALT_VAULT_PATH override, because nobody restarted it — the fix
    landed in a file the process had already read at launch. This gate
    is COBALT_ENV=production's own explicit "I am a production process"
    declaration: resolve_vault_path() refuses outright if that flag is
    set but the resolved root isn't the real vault, so a misconfigured
    production run fails loud on its very next resolve."""

    def test_production_env_refuses_non_prod_root(self, monkeypatch, tmp_path):
        monkeypatch.setenv(vault_module.ENV_MODE, vault_module.PROD_ENV_VALUE)
        monkeypatch.setenv(vault_module.ENV_OVERRIDE, str(tmp_path))
        with pytest.raises(VaultConfigError, match="REFUSED.*COBALT_ENV=production"):
            resolve_vault_path()

    def test_production_env_accepts_the_real_root(self, monkeypatch):
        monkeypatch.setenv(vault_module.ENV_MODE, vault_module.PROD_ENV_VALUE)
        monkeypatch.setenv(
            vault_module.ENV_OVERRIDE, vault_module.PROD_VAULT_PATH_REFERENCE
        )
        assert resolve_vault_path() == Path(
            vault_module.PROD_VAULT_PATH_REFERENCE
        ).resolve()

    def test_dev_env_unaffected_by_gate(self, monkeypatch, tmp_path):
        # COBALT_ENV unset (the dev default) — a non-Think root must
        # still resolve cleanly, or the NN#16 dev-safe default breaks.
        monkeypatch.setenv(vault_module.ENV_MODE, "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.setenv(vault_module.ENV_OVERRIDE, str(tmp_path))
        assert resolve_vault_path() == tmp_path.resolve()


class TestInverseGate:
    """2026-09-02 ("TSLA id 127") incident follow-up: the forward gate
    above only refused a PRODUCTION-declared process resolving outside
    Think. It never refused the symmetric case — a non-production run
    resolving INTO Think — so that gap is closed here, guarded by
    COBALT_ALLOW_DEV_ENTRY=1 for a deliberate override."""

    def test_dev_env_refuses_the_prod_root(self, monkeypatch):
        monkeypatch.setenv(vault_module.ENV_MODE, "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.delenv(vault_module.ALLOW_DEV_ENTRY_ENV, raising=False)
        monkeypatch.setenv(
            vault_module.ENV_OVERRIDE, vault_module.PROD_VAULT_PATH_REFERENCE
        )
        with pytest.raises(VaultConfigError, match="REFUSED.*non-production"):
            resolve_vault_path()

    def test_dev_env_with_explicit_override_allows_the_prod_root(self, monkeypatch):
        monkeypatch.setenv(vault_module.ENV_MODE, "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.setenv(vault_module.ALLOW_DEV_ENTRY_ENV, "1")
        monkeypatch.setenv(
            vault_module.ENV_OVERRIDE, vault_module.PROD_VAULT_PATH_REFERENCE
        )
        assert resolve_vault_path() == Path(
            vault_module.PROD_VAULT_PATH_REFERENCE
        ).resolve()

    def test_dev_env_resolving_outside_prod_is_unaffected(self, monkeypatch, tmp_path):
        # The ordinary, expected dev case must not be caught by the new gate.
        monkeypatch.setenv(vault_module.ENV_MODE, "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.delenv(vault_module.ALLOW_DEV_ENTRY_ENV, raising=False)
        monkeypatch.setenv(vault_module.ENV_OVERRIDE, str(tmp_path))
        assert resolve_vault_path() == tmp_path.resolve()

    def test_production_env_still_refuses_wrong_root_even_with_dev_entry_set(
        self, monkeypatch, tmp_path
    ):
        # COBALT_ALLOW_DEV_ENTRY must never weaken the forward (production)
        # gate — it only ever loosens the inverse (dev) one.
        monkeypatch.setenv(vault_module.ENV_MODE, vault_module.PROD_ENV_VALUE)
        monkeypatch.setenv(vault_module.ALLOW_DEV_ENTRY_ENV, "1")
        monkeypatch.setenv(vault_module.ENV_OVERRIDE, str(tmp_path))
        with pytest.raises(VaultConfigError, match="REFUSED.*COBALT_ENV=production"):
            resolve_vault_path()
