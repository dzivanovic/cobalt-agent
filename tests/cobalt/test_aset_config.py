"""ASET config loader tests — config errors must crash, never default."""

from decimal import Decimal

import pytest

from cobalt.aset import config as aset_config
from cobalt.aset.config import AsetConfig, ConfigError, ServerConfig, load_config

COMPLETE = """\
account_size: 10000
broker_hard_stop: 430
db_name: cobalt_dev
daily_note:
  vault_path: docs
  inbox_dir: "0 - Inbox"
"""


def test_committed_dev_config_is_valid():
    cfg = load_config()
    assert cfg.account_size > 0
    assert cfg.broker_hard_stop > 0
    assert cfg.daily_note.vault_path


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
    bad.write_text(COMPLETE + "surprise_key: 1\n")
    monkeypatch.setattr(aset_config, "CONFIG_PATH", bad)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", tmp_path / "absent.yaml")
    with pytest.raises(ConfigError):
        load_config()


def test_missing_broker_hard_stop_crashes(monkeypatch, tmp_path):
    bad = tmp_path / "aset.yaml"
    bad.write_text(COMPLETE.replace("broker_hard_stop: 430\n", ""))
    monkeypatch.setattr(aset_config, "CONFIG_PATH", bad)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", tmp_path / "absent.yaml")
    with pytest.raises(ConfigError):
        load_config()


def test_non_positive_account_rejected():
    with pytest.raises(Exception):
        AsetConfig(
            account_size=Decimal("0"),
            broker_hard_stop=Decimal("430"),
            daily_note={"vault_path": "docs", "inbox_dir": "0 - Inbox"},
        )


def test_server_defaults_to_loopback():
    # Unit-level, independent of whichever bind mode is active in
    # configs/dev/aset.local.yaml (e.g. Dejan may have it set to "lan").
    s = ServerConfig()
    assert s.bind == "loopback"
    assert s.host == "127.0.0.1"
    assert s.port == 5010


def test_server_lan_bind_resolves_to_all_interfaces():
    s = ServerConfig(bind="lan")
    assert s.host == "0.0.0.0"


def test_server_rejects_unknown_bind_value():
    with pytest.raises(Exception):
        ServerConfig(bind="everywhere")


def test_server_rejects_out_of_range_port():
    with pytest.raises(Exception):
        ServerConfig(port=0)
    with pytest.raises(Exception):
        ServerConfig(port=70000)


def test_missing_server_section_falls_back_to_loopback_default(monkeypatch, tmp_path):
    # server: is optional — old configs without it must still load, bound
    # to loopback only (never silently exposed to the LAN).
    bare = tmp_path / "aset.yaml"
    bare.write_text(COMPLETE)
    monkeypatch.setattr(aset_config, "CONFIG_PATH", bare)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", tmp_path / "absent.yaml")
    cfg = load_config()
    assert cfg.server.bind == "loopback"


def test_local_override_wins_and_must_be_complete(monkeypatch, tmp_path):
    base = tmp_path / "aset.yaml"
    base.write_text(COMPLETE)
    local = tmp_path / "aset.local.yaml"
    local.write_text(COMPLETE.replace("account_size: 10000", "account_size: 42000"))
    monkeypatch.setattr(aset_config, "CONFIG_PATH", base)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", local)
    assert load_config().account_size == Decimal("42000")

    # incomplete local file = crash, not silent merge with the base file
    local.write_text("account_size: 42000\n")
    with pytest.raises(ConfigError):
        load_config()
