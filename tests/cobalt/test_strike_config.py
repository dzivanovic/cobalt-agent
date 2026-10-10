"""S4-P1 T1: the strike numbers live in tunables.yaml, unit-checked (offline)."""

from __future__ import annotations

import argparse

import pytest
import yaml

from cobalt import cli
from cobalt.taxonomy.loader import TUNABLES_PATH


def _copy_without(tmp_path, key, *, unit=None):
    raw = yaml.safe_load(TUNABLES_PATH.read_text())
    rows = raw["tunables"] if "tunables" in raw else raw[next(iter(raw))]
    if unit is None:
        rows[:] = [row for row in rows if row["key"] != key]
    else:
        for row in rows:
            if row["key"] == key:
                row["unit"] = unit
    path = tmp_path / "tunables.yaml"
    path.write_text(yaml.safe_dump(raw, sort_keys=False))
    return path


def test_the_repo_tunables_pass_and_carry_the_ruled_values():
    from cobalt.strike.config import STRIKE_TUNABLE_UNITS, check

    settings = check()
    assert set(STRIKE_TUNABLE_UNITS) == {
        "strike.poll_interval_min", "strike.max_armed", "strike.alert_criterion_s", "strike.missed_sweep_interval",
    }
    assert settings.poll_interval_min == 2
    assert settings.max_armed == 5
    assert settings.alert_criterion_s == 5
    assert settings.missed_sweep_interval == 100


def test_no_second_ceiling_and_no_fixed_interval():
    from cobalt.taxonomy.loader import load_tunables

    keys = set(load_tunables().by_key)
    assert "strike.finviz_max_rpm" not in keys
    assert "strike.poll_interval" not in keys


def test_a_missing_row_is_named(tmp_path):
    from cobalt.strike.config import StrikeConfigError, check

    path = _copy_without(tmp_path, "strike.poll_interval_min")
    with pytest.raises(StrikeConfigError, match="strike.poll_interval_min"):
        check(path)


def test_a_wrong_unit_is_named(tmp_path):
    from cobalt.strike.config import StrikeConfigError, check

    path = _copy_without(tmp_path, "strike.poll_interval_min", unit="count")
    with pytest.raises(StrikeConfigError, match="unit count"):
        check(path)


@pytest.fixture
def _no_db(monkeypatch):
    for name in ("POSTGRES_HOST", "COBALT_DB_USER", "COBALT_DB_PASSWORD", "POSTGRES_PORT"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(cli.taxonomy_validate, "main", lambda: 0)


def test_validate_fails_naming_the_key(monkeypatch, capsys, _no_db):
    import cobalt.strike.config as strike_config

    def _bad(*_a, **_k):
        raise strike_config.StrikeConfigError("tunables.yaml: missing strike.poll_interval_min")

    monkeypatch.setattr(strike_config, "check", _bad)
    with pytest.raises(SystemExit) as exc:
        cli._cmd_validate(argparse.Namespace(no_db=True))
    assert exc.value.code == 1
    assert "strike.poll_interval_min" in capsys.readouterr().out


def test_validate_prints_the_strike_block(capsys, _no_db):
    cli._cmd_validate(argparse.Namespace(no_db=True))
    out = capsys.readouterr().out
    assert "Strike (S4-P1): 4 tunables rows resolved." in out


# ---------------------------------------------------------------------
# S4-P2 S5 — the delivery config (`configs/cobalt/strike.yaml`) and the hotkey
# ---------------------------------------------------------------------


def test_the_repo_delivery_file_loads_with_the_carded_values():
    from cobalt.strike.delivery_config import CONFIG_PATH, load_delivery_config

    assert CONFIG_PATH.exists()
    settings = load_delivery_config()
    assert (settings.stream_tail_ms, settings.keepalive_s, settings.dm_after_s) == (500, 15, 10)
    assert settings.hotkey_template == "{DAYMODE}-{KEY}-{SIDE}"


def test_the_delivery_file_is_registered_as_the_sheets_read():
    from cobalt.jobs.config import load_job_registry

    readers = load_job_registry().readers_of("configs/cobalt/strike.yaml")
    assert [r.label for r in readers] == ["com.cobalt.aset"]


def test_an_extra_key_is_refused_by_name(tmp_path):
    from cobalt.strike.delivery_config import DeliveryConfigError, load_delivery_config

    path = tmp_path / "strike.yaml"
    path.write_text("stream_tail_ms: 500\ndm_after_seconds: 10\n")
    with pytest.raises(DeliveryConfigError, match="dm_after_seconds"):
        load_delivery_config(path)


def test_a_missing_file_gives_the_model_defaults_and_one_logged_line(tmp_path):
    from loguru import logger

    from cobalt.strike.delivery_config import DeliverySettings, load_delivery_config

    lines: list[str] = []
    sink = logger.add(lines.append, format="{message}")
    try:
        settings = load_delivery_config(tmp_path / "absent.yaml")
    finally:
        logger.remove(sink)
    assert settings == DeliverySettings()
    assert len([line for line in lines if "absent.yaml" in line]) == 1


def test_a_missing_key_takes_its_default(tmp_path):
    from cobalt.strike.delivery_config import load_delivery_config

    path = tmp_path / "strike.yaml"
    path.write_text("keepalive_s: 20\n")
    settings = load_delivery_config(path)
    assert settings.keepalive_s == 20 and settings.dm_after_s == 10


def test_a_template_naming_an_unknown_field_is_refused(tmp_path):
    from cobalt.strike.delivery_config import DeliveryConfigError, load_delivery_config

    path = tmp_path / "strike.yaml"
    path.write_text('hotkey_template: "{DAYMODE}-{GRADE}"\n')
    with pytest.raises(DeliveryConfigError, match="hotkey_template"):
        load_delivery_config(path)


def test_the_hotkey_is_the_template_filled_upper_cased():
    from cobalt.strike.delivery_config import hotkey

    assert hotkey("{DAYMODE}-{KEY}-{SIDE}", sheet_mode="half", sized_grade="B", direction="long") == "HALF-B-LONG"
    assert hotkey("{DAYMODE}-{KEY}-{SIDE}", sheet_mode="full", sized_grade="a+", direction="short") == "FULL-A+-SHORT"


@pytest.mark.parametrize("mode, grade", [(None, "B"), ("half", None), ("", "B")])
def test_an_unsized_card_says_so_and_never_guesses(mode, grade):
    from cobalt.strike.delivery_config import UNSIZED, hotkey

    assert UNSIZED == "n/a — unsized"
    assert hotkey("{DAYMODE}-{KEY}-{SIDE}", sheet_mode=mode, sized_grade=grade, direction="long") == UNSIZED
