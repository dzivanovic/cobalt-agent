"""ASET config loader tests — config errors must crash, never default."""

from decimal import Decimal

import pytest

from cobalt.aset import config as aset_config
from cobalt.aset.config import AsetConfig, ConfigError, load_config


def test_committed_dev_config_is_valid():
    cfg = load_config()
    assert cfg.account_size > 0
    assert cfg.db_name


def test_missing_file_crashes(monkeypatch, tmp_path):
    monkeypatch.setattr(aset_config, "CONFIG_PATH", tmp_path / "absent.yaml")
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", tmp_path / "absent2.yaml")
    with pytest.raises(ConfigError):
        load_config()


def test_invalid_yaml_shape_crashes(monkeypatch, tmp_path):
    bad = tmp_path / "aset.yaml"
    bad.write_text("- just\n- a\n- list\n")
    monkeypatch.setattr(aset_config, "CONFIG_PATH", bad)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", tmp_path / "absent.yaml")
    with pytest.raises(ConfigError):
        load_config()


def test_unknown_keys_rejected(monkeypatch, tmp_path):
    bad = tmp_path / "aset.yaml"
    bad.write_text("account_size: 10000\nsurprise_key: 1\n")
    monkeypatch.setattr(aset_config, "CONFIG_PATH", bad)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", tmp_path / "absent.yaml")
    with pytest.raises(ConfigError):
        load_config()


def test_non_positive_account_rejected():
    with pytest.raises(Exception):
        AsetConfig(account_size=Decimal("0"))


def test_local_override_wins(monkeypatch, tmp_path):
    base = tmp_path / "aset.yaml"
    base.write_text("account_size: 10000\n")
    local = tmp_path / "aset.local.yaml"
    local.write_text("account_size: 42000\n")
    monkeypatch.setattr(aset_config, "CONFIG_PATH", base)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", local)
    assert load_config().account_size == Decimal("42000")
