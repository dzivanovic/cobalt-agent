"""ONE vault-path resolver tests — fail-loud, env override, missing path."""

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
