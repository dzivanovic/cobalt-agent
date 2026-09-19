"""Chunk S — `ArchiverSettings`, the ONE model behind spec §10's seven keys.

Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §10.

The point of this file is the MODE FLAG. `archiver.write_mode` is the
switch between today's nightly overlay and the append-only night, and
L7 says the flip is the owner's ruling on shadow numbers — never a
default that drifted. So two things are tested here that would look
like over-testing anywhere else:

* the shipped value is PINNED to `upsert`. A commit that changes it
  fails this test, which is exactly the reviewed-commit gate L7 asks
  for.
* every near-miss spelling is REFUSED and the refusal NAMES THE KEY
  (L1): `Append`, ` upsert`, `""`, `both`, and a missing row. A silent
  coercion of `Append` to `append` would switch the write mode of the
  production archiver by typo.

Offline: nothing here opens a database or a network connection.
"""

from __future__ import annotations

import pytest

from cobalt.archiver.settings import (
    ARCHIVER_TUNABLE_UNITS,
    ArchiverSettings,
    ArchiverSettingsError,
    ShadowCompare,
    WriteMode,
    load_archiver_settings,
    validate_command_lines,
)
from cobalt.taxonomy.loader import load_tunables
from cobalt.taxonomy.tunables import TunableRow, TunableStatus, TunableUnit

# --- helpers ---------------------------------------------------------


def _row(key: str, value, unit: TunableUnit) -> TunableRow:
    return TunableRow(
        key=key,
        value=value,
        unit=unit,
        scope="global",
        dynamic=False,
        status=TunableStatus.SOLIDIFIED,
        source="ruling",
    )


def _registry(**overrides) -> dict[str, TunableRow]:
    """The shipped seven, with per-test overrides. `None` drops a row."""
    values = {
        "archiver.write_mode": "upsert",
        "archiver.shadow_compare": "on",
        "archiver.shadow_statement_timeout_s": 10,
        "archiver.shadow_retention_nights": 30,
        "archiver.repair.quiet_before_open_min": 10,
        "archiver.repair.quiet_after_cycle_min": 5,
        "archiver.repair.cycle_max_min": 30,
    }
    values.update(overrides)
    return {
        key: _row(key, value, ARCHIVER_TUNABLE_UNITS[key])
        for key, value in values.items()
        if value is not _DROP
    }


class _Drop:
    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return "<drop>"


_DROP = _Drop()


# --- the seven keys resolve from the SHIPPED file ---------------------


def test_the_seven_keys_resolve_from_the_shipped_tunables_file():
    """L3: one model, read through the existing tunables loader."""
    settings = load_archiver_settings()
    assert settings.write_mode is WriteMode.UPSERT
    assert settings.shadow_compare is ShadowCompare.ON
    assert settings.shadow_statement_timeout_s == 10
    assert settings.shadow_retention_nights == 30
    assert settings.repair.quiet_before_open_min == 10
    assert settings.repair.quiet_after_cycle_min == 5
    assert settings.repair.cycle_max_min == 30


def test_the_shipped_rows_carry_the_units_and_statuses_the_design_ruled():
    rows = load_tunables().by_key
    for key, unit in ARCHIVER_TUNABLE_UNITS.items():
        assert key in rows, f"{key} missing from the shipped tunables.yaml"
        assert rows[key].unit is unit, f"{key} has unit {rows[key].unit}"
    # §10: PROPOSED exactly where the design says PROPOSED.
    proposed = {
        "archiver.shadow_compare",
        "archiver.shadow_statement_timeout_s",
        "archiver.shadow_retention_nights",
        "archiver.repair.cycle_max_min",
    }
    for key in ARCHIVER_TUNABLE_UNITS:
        expected = (
            TunableStatus.PROPOSED if key in proposed else TunableStatus.SOLIDIFIED
        )
        assert rows[key].status is expected, f"{key} status {rows[key].status}"
    # The desk's two numbers cite the ruling that set them (§16 / R8).
    for key in (
        "archiver.repair.quiet_before_open_min",
        "archiver.repair.quiet_after_cycle_min",
    ):
        assert any(
            "cto-2026-09-19.md §16 / R8" in c for c in rows[key].consumers
        ), f"{key} does not cite the desk's ruling"


def test_the_shipped_write_mode_is_upsert_and_only_a_reviewed_commit_changes_it():
    """L7. The build DEPLOYS as `upsert` (§5). The switch to `append` is
    the owner's ruling on the shadow numbers — this assertion is the
    tripwire that makes the flip a reviewed commit rather than a drift."""
    row = load_tunables().by_key["archiver.write_mode"]
    assert row.value == "upsert"
    assert load_archiver_settings().write_mode is WriteMode.UPSERT


# --- write_mode: EXACTLY upsert | append -----------------------------


@pytest.mark.parametrize("bad", ["Append", "APPEND", " upsert", "upsert ", "", "both", "append\n"])
def test_write_mode_refuses_every_near_miss_and_names_the_key(bad):
    with pytest.raises(ArchiverSettingsError) as e:
        load_archiver_settings(_registry(**{"archiver.write_mode": bad}))
    assert "archiver.write_mode" in str(e.value)
    assert "upsert" in str(e.value) and "append" in str(e.value)


def test_write_mode_refuses_a_non_string_value_and_names_the_key():
    with pytest.raises(ArchiverSettingsError) as e:
        load_archiver_settings(_registry(**{"archiver.write_mode": 1}))
    assert "archiver.write_mode" in str(e.value)


def test_a_missing_write_mode_row_fails_loud_naming_the_key():
    with pytest.raises(ArchiverSettingsError) as e:
        load_archiver_settings(_registry(**{"archiver.write_mode": _DROP}))
    assert "archiver.write_mode" in str(e.value)
    assert "missing" in str(e.value)


def test_append_is_accepted_so_the_switch_needs_no_code_change():
    settings = load_archiver_settings(_registry(**{"archiver.write_mode": "append"}))
    assert settings.write_mode is WriteMode.APPEND


def test_a_wrong_unit_on_a_row_fails_loud_naming_the_key():
    rows = _registry()
    rows["archiver.write_mode"] = _row(
        "archiver.write_mode", "upsert", TunableUnit.COUNT
    )
    with pytest.raises(ArchiverSettingsError) as e:
        load_archiver_settings(rows)
    assert "archiver.write_mode" in str(e.value)
    assert "unit" in str(e.value)


# --- shadow_compare --------------------------------------------------


@pytest.mark.parametrize("value,expected", [("on", ShadowCompare.ON), ("off", ShadowCompare.OFF)])
def test_shadow_compare_on_and_off(value, expected):
    settings = load_archiver_settings(_registry(**{"archiver.shadow_compare": value}))
    assert settings.shadow_compare is expected
    assert settings.shadow_enabled is (expected is ShadowCompare.ON)


@pytest.mark.parametrize("bad", ["ON", "true", "", "yes", 1])
def test_shadow_compare_refuses_anything_else_naming_the_key(bad):
    with pytest.raises(ArchiverSettingsError) as e:
        load_archiver_settings(_registry(**{"archiver.shadow_compare": bad}))
    assert "archiver.shadow_compare" in str(e.value)


def test_shadow_compare_is_ignored_in_append_mode():
    """§5: in `append` the comparison IS the gate; no shadow artifact."""
    settings = load_archiver_settings(
        _registry(**{"archiver.write_mode": "append", "archiver.shadow_compare": "on"})
    )
    assert settings.shadow_enabled is False


# --- the three repair minutes ----------------------------------------


@pytest.mark.parametrize(
    "key",
    [
        "archiver.repair.quiet_before_open_min",
        "archiver.repair.quiet_after_cycle_min",
        "archiver.repair.cycle_max_min",
    ],
)
@pytest.mark.parametrize("bad", [0, -1, 1.5, "10", None])
def test_every_repair_minute_must_be_a_positive_integer(key, bad):
    with pytest.raises(ArchiverSettingsError) as e:
        load_archiver_settings(_registry(**{key: bad}))
    assert key in str(e.value)


@pytest.mark.parametrize(
    "key",
    [
        "archiver.repair.quiet_before_open_min",
        "archiver.repair.quiet_after_cycle_min",
        "archiver.repair.cycle_max_min",
    ],
)
def test_a_missing_repair_row_fails_loud_naming_the_key(key):
    with pytest.raises(ArchiverSettingsError) as e:
        load_archiver_settings(_registry(**{key: _DROP}))
    assert key in str(e.value) and "missing" in str(e.value)


@pytest.mark.parametrize("bad", [0, -5, "10"])
def test_the_two_shadow_counts_must_be_positive_integers(bad):
    for key in ("archiver.shadow_statement_timeout_s", "archiver.shadow_retention_nights"):
        with pytest.raises(ArchiverSettingsError) as e:
            load_archiver_settings(_registry(**{key: bad}))
        assert key in str(e.value)


# --- what `cobalt validate` prints (L10) ------------------------------


def test_validate_prints_the_resolved_settings():
    """The function `cobalt validate` calls, tested directly — the CLI is
    not run here (it would sweep every config family and read the vault)."""
    lines = validate_command_lines()
    body = "\n".join(lines)
    assert "archiver.write_mode = upsert" in body
    for key in ARCHIVER_TUNABLE_UNITS:
        assert key in body, f"{key} is not printed by the gate"
    # The operator must be able to read the mode's meaning off the gate.
    assert "append" in body.lower()


def test_validate_lines_fail_loud_when_a_row_is_missing(monkeypatch):
    from cobalt.archiver import settings as settings_mod

    monkeypatch.setattr(
        settings_mod,
        "load_archiver_settings",
        lambda registry=None: (_ for _ in ()).throw(
            ArchiverSettingsError("tunables.yaml: missing archiver.write_mode")
        ),
    )
    with pytest.raises(ArchiverSettingsError):
        validate_command_lines()


# --- the model itself -------------------------------------------------


def test_the_model_is_strict_and_frozen():
    settings = load_archiver_settings()
    with pytest.raises(Exception):
        settings.write_mode = WriteMode.APPEND
    with pytest.raises(Exception):
        ArchiverSettings(
            write_mode="upsert",
            shadow_compare="on",
            shadow_statement_timeout_s=10,
            shadow_retention_nights=30,
            repair={"quiet_before_open_min": 10, "quiet_after_cycle_min": 5, "cycle_max_min": 30},
            unexpected_key=1,
        )


def test_there_is_exactly_one_yaml_reader_behind_the_settings():
    """L3. `settings.py` must not grow a second YAML loader beside
    `cobalt.taxonomy.loader`."""
    source = (
        __import__("pathlib").Path(__import__("cobalt.archiver.settings", fromlist=["x"]).__file__)
        .read_text(encoding="utf-8")
    )
    assert "import yaml" not in source and "yaml.safe_load" not in source
    assert "load_tunables" in source
