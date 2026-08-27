"""ASET config loader tests — config errors must crash, never default.

Iteration 4 (ruled by Dejan, 2026-08-28): broker_hard_stop and
daily_stop_default retired from AsetConfig (the daily-stop x percentage
model they served is gone). Sheet-mode fixed dollar risk moved to its
own config, configs/cobalt/aset.yaml (SheetModesConfig /
load_sheet_modes_config) — see the tests at the bottom of this file.
"""

from decimal import Decimal

import pytest

from cobalt.aset import config as aset_config
from cobalt.aset.config import (
    AsetConfig,
    ConfigError,
    ServerConfig,
    SheetModesConfig,
    load_config,
    load_sheet_modes_config,
)

COMPLETE = """\
account_size: 10000
db_name: cobalt_dev
daily_note:
  daily_notes_dir: "1 - Trading/1- Daily Notes"
"""

COMPLETE_SHEET_MODES = """\
sheet_modes:
  full:
    A: 135
    B: 60
  half:
    A: 70
    B: 30
"""


def test_committed_dev_config_is_valid():
    cfg = load_config()
    assert cfg.account_size > 0
    assert cfg.daily_note.daily_notes_dir


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


def test_missing_account_size_crashes(monkeypatch, tmp_path):
    bad = tmp_path / "aset.yaml"
    bad.write_text(COMPLETE.replace("account_size: 10000\n", ""))
    monkeypatch.setattr(aset_config, "CONFIG_PATH", bad)
    monkeypatch.setattr(aset_config, "LOCAL_CONFIG_PATH", tmp_path / "absent.yaml")
    with pytest.raises(ConfigError):
        load_config()


def test_non_positive_account_rejected():
    with pytest.raises(Exception):
        AsetConfig(
            account_size=Decimal("0"),
            daily_note={"daily_notes_dir": "1 - Trading/1- Daily Notes"},
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


class TestSheetModesConfig:
    def test_committed_config_is_valid(self):
        cfg = load_sheet_modes_config()
        assert cfg.full.A > 0
        assert cfg.full.B > 0
        assert cfg.half.A > 0
        assert cfg.half.B > 0

    def test_dollars_for_matches_das_hotkey_values(self):
        cfg = load_sheet_modes_config()
        assert cfg.dollars_for("full", "B") == Decimal("60")
        assert cfg.dollars_for("full", "A") == Decimal("135")
        assert cfg.dollars_for("half", "B") == Decimal("30")
        assert cfg.dollars_for("half", "A") == Decimal("70")

    def test_dollars_for_rejects_non_tradeable_grade(self):
        cfg = load_sheet_modes_config()
        with pytest.raises(ConfigError):
            cfg.dollars_for("full", "C")

    def test_missing_file_crashes(self, monkeypatch, tmp_path):
        monkeypatch.setattr(aset_config, "SHEET_MODES_CONFIG_PATH", tmp_path / "absent.yaml")
        with pytest.raises(ConfigError):
            load_sheet_modes_config()

    def test_missing_grade_crashes(self, monkeypatch, tmp_path):
        bad = tmp_path / "aset.yaml"
        bad.write_text("sheet_modes:\n  full:\n    A: 135\n  half:\n    A: 70\n    B: 30\n")
        monkeypatch.setattr(aset_config, "SHEET_MODES_CONFIG_PATH", bad)
        with pytest.raises(ConfigError):
            load_sheet_modes_config()

    def test_non_positive_dollars_rejected(self):
        with pytest.raises(Exception):
            SheetModesConfig(
                full={"A": Decimal("135"), "B": Decimal("0")},
                half={"A": Decimal("70"), "B": Decimal("30")},
            )
