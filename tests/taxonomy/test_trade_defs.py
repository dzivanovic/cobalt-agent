"""Tests for src/cobalt/taxonomy — Batch 1+2 trade_def schema, loader,
and the `python -m cobalt.taxonomy.validate` CLI."""

from __future__ import annotations

import copy
import subprocess
import sys
import warnings
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from cobalt.taxonomy.defaults import TaxonomyDefaults
from cobalt.taxonomy.loader import (
    TaxonomyConfigError,
    is_ma_ref,
    iter_stop_buffers,
    iter_tunables,
    load_trade_defs,
    resolve_ma_ref,
)
from cobalt.taxonomy.trade_def import ExitLeg, IndicatorPlacement, TradeDef, Tunable
from cobalt.taxonomy.variables import VariableRegistryEntry

REPO_ROOT = Path(__file__).resolve().parents[2]
TRADE_DEFS_DIR = REPO_ROOT / "configs" / "cobalt" / "taxonomy" / "trade_defs"
VARIABLES_DIR = REPO_ROOT / "configs" / "cobalt" / "taxonomy" / "variables"
CAMERON_GRID_PATH = REPO_ROOT / "configs" / "cobalt" / "taxonomy" / "cameron_grid.yaml"
BACKLOG_PATH = REPO_ROOT / "docs" / "00 - Project" / "BACKLOG.md"

ALL_TRADE_IDS = {
    "hitchhiker",
    "big_dog",
    "second_chance",
    "backside",
    "fashionably_late",
    "rubberband",
    "gap_give_and_go",
    "vwap_continuation",
    "first_vwap_pullback",
    "ema9_scalp",
    "back_through_open",
    "bella_fade",
    "bouncy_ball",
}


def test_all_thirteen_trade_defs_load():
    trade_defs = load_trade_defs()
    assert set(trade_defs) == ALL_TRADE_IDS
    for td in trade_defs.values():
        assert isinstance(td, TradeDef)


def test_validate_cli_exits_zero():
    result = subprocess.run(
        [sys.executable, "-m", "cobalt.taxonomy.validate"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "13 trade_def(s) validated OK." in result.stdout
    for trade_id in ALL_TRADE_IDS:
        assert trade_id in result.stdout


@pytest.fixture
def base_trade_def_dict() -> dict:
    """A known-valid trade_def dict (hitchhiker) to mutate per bad-fixture test."""
    raw = yaml.safe_load((TRADE_DEFS_DIR / "hitchhiker.yaml").read_text())
    return copy.deepcopy(raw["trade_def"])


def test_unknown_enum_value_raises_loud_with_field_path(base_trade_def_dict):
    base_trade_def_dict["class"] = "not_a_real_class"
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "class" in str(exc_info.value)


def test_exit_fractions_summing_to_point_nine_raises_loud(base_trade_def_dict):
    base_trade_def_dict["exit"][0]["fraction"] = 0.4
    base_trade_def_dict["exit"][1]["fraction"] = 0.5  # sums to 0.9, outside +/-0.01
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "exit fractions sum to" in str(exc_info.value)


def test_stop_buffer_spread_is_rejected_with_field_path(base_trade_def_dict):
    base_trade_def_dict["stop"]["placement"]["buffer"]["type"] = "spread"
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "buffer" in str(exc_info.value)


def test_quality_factor_missing_from_registry_raises_loud(tmp_path):
    trade_defs_dir = tmp_path / "trade_defs"
    variables_dir = tmp_path / "variables"
    trade_defs_dir.mkdir()
    variables_dir.mkdir()

    raw = yaml.safe_load((TRADE_DEFS_DIR / "hitchhiker.yaml").read_text())
    raw["trade_def"]["quality_factors"].append("totally_unregistered_factor")
    (trade_defs_dir / "hitchhiker.yaml").write_text(yaml.safe_dump(raw))

    registry_raw = yaml.safe_load((VARIABLES_DIR / "hitchhiker.yaml").read_text())
    (variables_dir / "hitchhiker.yaml").write_text(yaml.safe_dump(registry_raw))

    with pytest.raises(TaxonomyConfigError) as exc_info:
        load_trade_defs(
            trade_defs_dir=trade_defs_dir,
            variables_dir=variables_dir,
            cameron_grid_path=CAMERON_GRID_PATH,
        )
    message = str(exc_info.value)
    assert "totally_unregistered_factor" in message
    assert "hitchhiker.yaml" in message


# --- Batch 2 / v0.7 schema extensions ---------------------------------------


def test_indicator_placement_accepts_known_indicator(base_trade_def_dict):
    base_trade_def_dict["stop"]["placement"] = {
        "type": "indicator",
        "indicator": "EMA21",
        "snapshot": "live",
    }
    td = TradeDef(**base_trade_def_dict)
    assert isinstance(td.stop.placement, IndicatorPlacement)
    assert td.stop.placement.indicator == "EMA21"
    assert td.stop.placement.snapshot == "live"
    assert td.stop.placement.buffer.cents.value == 0.02  # default


def test_indicator_placement_rejects_unknown_indicator(base_trade_def_dict):
    base_trade_def_dict["stop"]["placement"] = {
        "type": "indicator",
        "indicator": "SMA50",
    }
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "indicator" in str(exc_info.value)


@pytest.mark.parametrize("trigger_type", ["trendline_break", "indicator_rejection"])
def test_new_trigger_types_load(base_trade_def_dict, trigger_type):
    base_trade_def_dict["trigger"] = {
        "type": trigger_type,
        "params": {"indicator": "VWAP"},
        "confirmation_policy": {"type": "close_through"},
    }
    td = TradeDef(**base_trade_def_dict)
    assert td.trigger.type == trigger_type


def test_trail_exit_conditions_validate(base_trade_def_dict):
    base_trade_def_dict["exit"] = [
        {
            "fraction": 1.0,
            "target_type": "trail",
            "params": {
                "conditions": [
                    {"type": "prior_bar_break", "n": 1},
                    {"type": "ma_close", "ma": {"value": "EMA9", "dynamic": False}},
                    {"type": "vwap_close"},
                    {"type": "level", "level_ref": "high_of_day"},
                ],
                "mode": "any",
            },
            "evaluation": "close_through",
        }
    ]
    td = TradeDef(**base_trade_def_dict)
    assert len(td.exit[0].params["conditions"]) == 4


def test_trail_exit_rejects_unknown_condition_type(base_trade_def_dict):
    base_trade_def_dict["exit"] = [
        {
            "fraction": 1.0,
            "target_type": "trail",
            "params": {"conditions": [{"type": "moon_phase"}], "mode": "any"},
            "evaluation": "close_through",
        }
    ]
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "trail" in str(exc_info.value)


def test_trail_exit_directly_via_exit_leg():
    with pytest.raises(ValidationError):
        ExitLeg(
            fraction=1.0,
            target_type="trail",
            params={"conditions": [], "mode": "any"},
            evaluation="close_through",
        )


def test_reentry_window_accepts_duration_string(base_trade_def_dict):
    base_trade_def_dict["reentry_window"] = {"value": "3 min", "dynamic": False}
    td = TradeDef(**base_trade_def_dict)
    assert td.reentry_window.value == "3 min"


def test_reentry_window_rejects_bad_format(base_trade_def_dict):
    base_trade_def_dict["reentry_window"] = {"value": "soon", "dynamic": False}
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "reentry_window" in str(exc_info.value)


def test_resolve_ma_ref_resolves_configured_keys():
    defaults = TaxonomyDefaults(working_timeframe="2m", ma={"fast": 9, "slow": 20})
    assert resolve_ma_ref("ma.slow", defaults) == 20
    assert resolve_ma_ref("ma.fast", defaults) == 9


def test_resolve_ma_ref_rejects_unknown_key():
    defaults = TaxonomyDefaults(working_timeframe="2m", ma={"fast": 9, "slow": 20})
    with pytest.raises(TaxonomyConfigError):
        resolve_ma_ref("ma.medium", defaults)


def test_is_ma_ref():
    assert is_ma_ref("ma.slow")
    assert is_ma_ref("ma.fast")
    assert not is_ma_ref("EMA9")


def test_variable_registry_entry_frontier_defaults_false_and_round_trips():
    default_entry = VariableRegistryEntry(name="rvol")
    assert default_entry.frontier is False

    frontier_entry = VariableRegistryEntry(
        name="tape_read", source="human", frontier=True
    )
    assert frontier_entry.frontier is True


def test_stop_buffer_differing_from_default_warns_not_raises(tmp_path):
    trade_defs_dir = tmp_path / "trade_defs"
    variables_dir = tmp_path / "variables"
    trade_defs_dir.mkdir()
    variables_dir.mkdir()

    raw = yaml.safe_load((TRADE_DEFS_DIR / "hitchhiker.yaml").read_text())
    raw["trade_def"]["stop"]["placement"]["buffer"]["cents"]["value"] = 0.05
    (trade_defs_dir / "hitchhiker.yaml").write_text(yaml.safe_dump(raw))

    registry_raw = yaml.safe_load((VARIABLES_DIR / "hitchhiker.yaml").read_text())
    (variables_dir / "hitchhiker.yaml").write_text(yaml.safe_dump(registry_raw))

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        trade_defs = load_trade_defs(
            trade_defs_dir=trade_defs_dir,
            variables_dir=variables_dir,
            cameron_grid_path=CAMERON_GRID_PATH,
        )
    assert "hitchhiker" in trade_defs  # loaded, not rejected — WARNS not fails
    messages = [str(w.message) for w in caught]
    assert any("0.05" in m and "A.6" in m for m in messages)


def test_iter_stop_buffers_finds_every_buffer_in_a_trade_def():
    trade_defs = load_trade_defs()
    buffers = list(iter_stop_buffers(trade_defs["gap_give_and_go"]))
    assert len(buffers) >= 2  # stop.placement.buffer + raise_to.placement.buffer
    assert all(b.cents.value == 0.02 for b in buffers)


def test_batch2_ma_slow_refs_resolve_at_load_time():
    trade_defs = load_trade_defs()
    vc_condition = trade_defs["vwap_continuation"].exit[1].params["conditions"][0]
    assert vc_condition["ma"]["value"] == "ma.slow"

    sc_condition = trade_defs["second_chance"].exit[1].params["conditions"][0]
    assert sc_condition["ma"]["value"] == "ma.slow"


def test_dynamic_tunables_appear_in_replay_backlog():
    """Live-data pass: every dynamic=True Tunable actually loaded from
    Batch 1 must have a matching entry in the §13 replay backlog.

    Currently vacuous for Batch 1 — every quantity the v0.6 §0 "Dynamic
    definitions" law names (Range.duration bands, flat_threshold, etc.)
    lives inside an unparsed Predicate.expr string, not a structured
    Tunable field, so no Batch 1 trade_def actually produces a
    dynamic=True Tunable yet. The walk stays in place so it fires the
    moment a future trade_def (Batch 2+) introduces one.
    """
    backlog_text = BACKLOG_PATH.read_text()
    trade_defs = load_trade_defs()
    checked = 0
    for td in trade_defs.values():
        for tunable in iter_tunables(td):
            if tunable.dynamic:
                checked += 1
                assert tunable.note, (
                    f"{td.id}: dynamic tunable with no note to cross-check against the backlog"
                )
                assert tunable.note in backlog_text, (
                    f"{td.id}: dynamic tunable {tunable.note!r} has no matching entry in {BACKLOG_PATH}"
                )
    assert checked == 0, (
        "Batch 1 introduced a dynamic tunable — update this test's docstring/assumption"
    )


def test_dynamic_tunable_backlog_matching_actually_discriminates():
    """Unit-level proof that the membership check above is real, not
    vacuously true: a note copied from the backlog matches, a made-up one
    does not."""
    backlog_text = BACKLOG_PATH.read_text()

    known = Tunable(
        value=5, dynamic=True, note="Range.duration bands (5-20 / >=45 min)"
    )
    assert known.note in backlog_text

    orphan = Tunable(
        value=1,
        dynamic=True,
        note="a made-up dynamic value with no backlog entry, for testing",
    )
    assert orphan.note not in backlog_text
