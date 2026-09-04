"""ASET config loader tests — config errors must crash, never default.

Iteration 4 (ruled by Dejan, 2026-08-28): broker_hard_stop and
daily_stop_default retired from AsetConfig (the daily-stop x percentage
model they served is gone). Sheet-mode fixed dollar risk moved to its
own config, configs/cobalt/aset.yaml (SheetModesConfig /
load_sheet_modes_config) — see the tests at the bottom of this file.

Config-completion follow-up (2026-08-28): the grade ladder is now
A_plus/A/B/C/D in full, D always $0 (enforced by a field validator, not
just convention), plus a separate `enabled_grades` field controlling
UI/compute availability.
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
from cobalt.aset.models import Grade

COMPLETE = """\
account_size: 10000
daily_note:
  daily_notes_dir: "1 - Trading/1- Daily Notes"
"""

COMPLETE_SHEET_MODES = """\
sheet_modes:
  full:
    A_plus: 345
    A: 135
    B: 60
    C: 21
    D: 0
  half:
    A_plus: 170
    A: 70
    B: 30
    C: 11
    D: 0
  enabled_grades: [A, B]
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
        for grades in (cfg.full, cfg.half):
            assert grades.A_plus > 0
            assert grades.A > 0
            assert grades.B > 0
            assert grades.C > 0
            assert grades.D == 0
        assert set(cfg.enabled_grades) == {Grade.A, Grade.B}

    def test_dollars_for_matches_das_hotkey_values(self):
        cfg = load_sheet_modes_config()
        assert cfg.dollars_for("full", "B") == Decimal("60")
        assert cfg.dollars_for("full", "A") == Decimal("135")
        assert cfg.dollars_for("half", "B") == Decimal("30")
        assert cfg.dollars_for("half", "A") == Decimal("70")

    def test_dollars_for_resolves_the_full_ladder(self):
        # A+/C/D are real numbers now (D always 0) — dollars_for doesn't
        # reject them; UI/compute availability is enabled_grades' job.
        cfg = load_sheet_modes_config()
        assert cfg.dollars_for("full", "A+") == Decimal("345")
        assert cfg.dollars_for("full", "C") == Decimal("21")
        assert cfg.dollars_for("full", "D") == Decimal("0")
        assert cfg.dollars_for("half", "A+") == Decimal("170")
        assert cfg.dollars_for("half", "C") == Decimal("11")

    def test_is_enabled_reflects_committed_config(self):
        cfg = load_sheet_modes_config()
        assert cfg.is_enabled("A")
        assert cfg.is_enabled("B")
        assert not cfg.is_enabled("A+")
        assert not cfg.is_enabled("C")
        assert not cfg.is_enabled("D")

    def test_missing_file_crashes(self, monkeypatch, tmp_path):
        monkeypatch.setattr(aset_config, "SHEET_MODES_CONFIG_PATH", tmp_path / "absent.yaml")
        with pytest.raises(ConfigError):
            load_sheet_modes_config()

    def test_missing_grade_crashes(self, monkeypatch, tmp_path):
        bad = tmp_path / "aset.yaml"
        bad.write_text(
            COMPLETE_SHEET_MODES.replace("    D: 0\n  half:", "  half:", 1)
        )
        monkeypatch.setattr(aset_config, "SHEET_MODES_CONFIG_PATH", bad)
        with pytest.raises(ConfigError):
            load_sheet_modes_config()

    def test_missing_enabled_grades_crashes(self, monkeypatch, tmp_path):
        bad = tmp_path / "aset.yaml"
        bad.write_text(COMPLETE_SHEET_MODES.replace("  enabled_grades: [A, B]\n", ""))
        monkeypatch.setattr(aset_config, "SHEET_MODES_CONFIG_PATH", bad)
        with pytest.raises(ConfigError):
            load_sheet_modes_config()

    def test_non_positive_dollars_rejected(self):
        with pytest.raises(Exception):
            SheetModesConfig(
                full={"A_plus": Decimal("345"), "A": Decimal("135"), "B": Decimal("0"), "C": Decimal("21"), "D": Decimal("0")},
                half={"A_plus": Decimal("170"), "A": Decimal("70"), "B": Decimal("30"), "C": Decimal("11"), "D": Decimal("0")},
                enabled_grades=["A", "B"],
            )

    def test_nonzero_d_rejected(self):
        # The SAW principle enforced at load time, not just by convention.
        with pytest.raises(Exception):
            SheetModesConfig(
                full={"A_plus": Decimal("345"), "A": Decimal("135"), "B": Decimal("60"), "C": Decimal("21"), "D": Decimal("5")},
                half={"A_plus": Decimal("170"), "A": Decimal("70"), "B": Decimal("30"), "C": Decimal("11"), "D": Decimal("0")},
                enabled_grades=["A", "B"],
            )

    def test_empty_enabled_grades_rejected(self):
        with pytest.raises(Exception):
            SheetModesConfig(
                full={"A_plus": Decimal("345"), "A": Decimal("135"), "B": Decimal("60"), "C": Decimal("21"), "D": Decimal("0")},
                half={"A_plus": Decimal("170"), "A": Decimal("70"), "B": Decimal("30"), "C": Decimal("11"), "D": Decimal("0")},
                enabled_grades=[],
            )
