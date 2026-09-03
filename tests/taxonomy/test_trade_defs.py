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
    iter_cfg_tokens,
    iter_stop_buffers,
    load_defaults,
    load_trade_defs,
    load_tunables,
    resolve_cfg,
    resolve_ma_ref,
)
from cobalt.taxonomy.trade_def import ExitLeg, IndicatorPlacement, TradeDef
from cobalt.taxonomy.tunables import TunableRegistry, TunableStatus, replay_backlog
from cobalt.taxonomy.variables import VariableRegistryEntry

REPO_ROOT = Path(__file__).resolve().parents[2]
TRADE_DEFS_DIR = REPO_ROOT / "configs" / "cobalt" / "taxonomy" / "trade_defs"
VARIABLES_DIR = REPO_ROOT / "configs" / "cobalt" / "taxonomy" / "variables"
CAMERON_GRID_PATH = REPO_ROOT / "configs" / "cobalt" / "taxonomy" / "cameron_grid.yaml"

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


def test_trail_slot_conditions_validate(base_trade_def_dict):
    # v0.4: conditions[] live on trade_def.trail (TrailSpec), not on the
    # exit leg's params — the exit leg just points at target_type=trail
    # with no params (one-stop law, v0.7 §14 c.1 / §10.2).
    base_trade_def_dict["trail"] = {
        "conditions": [
            {"type": "prior_bar_break", "n": 1},
            {"type": "ma_close", "ma": {"value": "EMA9", "dynamic": False}},
            {"type": "vwap_close"},
            {"type": "level", "level_ref": "high_of_day"},
        ],
        "mode": "select",
    }
    base_trade_def_dict["exit"] = [
        {
            "fraction": 1.0,
            "target_type": "trail",
            "params": {},
            "evaluation": "close_through",
        }
    ]
    td = TradeDef(**base_trade_def_dict)
    assert len(td.trail.conditions) == 4
    assert td.trail.mode == "select"


def test_trail_slot_rejects_unknown_condition_type(base_trade_def_dict):
    base_trade_def_dict["trail"] = {
        "conditions": [{"type": "moon_phase"}],
        "mode": "select",
    }
    base_trade_def_dict["exit"] = [
        {
            "fraction": 1.0,
            "target_type": "trail",
            "params": {},
            "evaluation": "close_through",
        }
    ]
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "trail" in str(exc_info.value)


def test_trail_exit_leg_rejects_nonempty_params():
    # ExitLeg.target_type=trail takes NO params in schema v0.4 — the
    # trail is defined once in trade_def.trail.
    with pytest.raises(ValidationError):
        ExitLeg(
            fraction=1.0,
            target_type="trail",
            params={"conditions": [], "mode": "any"},
            evaluation="close_through",
        )


def test_trail_exit_leg_accepts_empty_params():
    leg = ExitLeg(
        fraction=1.0,
        target_type="trail",
        params={},
        evaluation="close_through",
    )
    assert leg.params == {}


def test_trail_exit_without_trail_slot_raises_loud(base_trade_def_dict):
    # one-stop law: an exit leg pointing at target_type=trail requires
    # trade_def.trail to be set.
    base_trade_def_dict["trail"] = None
    base_trade_def_dict["exit"] = [
        {
            "fraction": 1.0,
            "target_type": "trail",
            "params": {},
            "evaluation": "close_through",
        }
    ]
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "trade_def.trail" in str(exc_info.value)


@pytest.mark.parametrize(
    "stop_mgmt_type", ["trail_ma_close", "trail_bar"]
)
def test_removed_stop_management_trail_spellings_fail_loud(
    base_trade_def_dict, stop_mgmt_type
):
    base_trade_def_dict["stop_management"] = [
        {"type": stop_mgmt_type, "on": {"name": "entry"}}
    ]
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "trail" in str(exc_info.value)


def test_standalone_ma_close_exit_target_fails_loud(base_trade_def_dict):
    base_trade_def_dict["exit"] = [
        {
            "fraction": 1.0,
            "target_type": "ma_close",
            "params": {"ma": "EMA9"},
            "evaluation": "close_through",
        }
    ]
    with pytest.raises(ValidationError) as exc_info:
        TradeDef(**base_trade_def_dict)
    assert "trail" in str(exc_info.value)


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
    # v0.4: trail conditions live on trade_def.trail (TrailSpec), not on
    # the exit leg's params.
    trade_defs = load_trade_defs()
    vc_condition = trade_defs["vwap_continuation"].trail.conditions[0]
    assert vc_condition.ma.value == "ma.slow"

    sc_conditions = {c.ma.value for c in trade_defs["second_chance"].trail.conditions if c.type == "ma_close"}
    assert sc_conditions == {"ma.fast", "ma.slow"}


def test_dynamic_tunables_appear_in_replay_backlog():
    """v0.7 §13.1: the replay backlog is now a query over tunables.yaml
    (`dynamic=True AND status != solidified`), not a hand-maintained
    BACKLOG.md list cross-checked against trade_def Tunable[T] notes
    (the old mechanism — every §13.1 dynamic row lives in tunables.yaml
    now, not inside an unparsed Predicate.expr string)."""
    registry = load_tunables()
    backlog = replay_backlog(registry)
    assert backlog, "tunables.yaml seeded no dynamic, non-solidified rows"
    assert all(row.dynamic for row in backlog)
    assert all(row.status != TunableStatus.SOLIDIFIED for row in backlog)
    # spot-check known dynamic rows are present
    backlog_keys = {row.key for row in backlog}
    assert "gap_retrace_pct_max" in backlog_keys
    assert "second_chance.trail_conditions" in backlog_keys


def test_dynamic_tunable_backlog_matching_actually_discriminates():
    """Unit-level proof the backlog query is real, not vacuously true: a
    solidified or non-dynamic row is excluded."""
    registry = TunableRegistry(
        tunables=[
            {
                "key": "included.row",
                "value": 1,
                "unit": "count",
                "scope": "global",
                "dynamic": True,
                "status": "proposed",
                "source": "dwv",
            },
            {
                "key": "excluded.solidified",
                "value": 1,
                "unit": "count",
                "scope": "global",
                "dynamic": True,
                "status": "solidified",
                "source": "ruling",
            },
            {
                "key": "excluded.not_dynamic",
                "value": 1,
                "unit": "count",
                "scope": "global",
                "dynamic": False,
                "status": "proposed",
                "source": "sheet",
            },
        ]
    )
    keys = {row.key for row in replay_backlog(registry)}
    assert keys == {"included.row"}


def test_cfg_unknown_key_fails_loud(tmp_path, base_trade_def_dict):
    trade_defs_dir = tmp_path / "trade_defs"
    variables_dir = tmp_path / "variables"
    trade_defs_dir.mkdir()
    variables_dir.mkdir()

    base_trade_def_dict["avoid"] = [
        {"expr": "Range(micro).duration >= cfg(no.such.key) min"}
    ]
    (trade_defs_dir / "hitchhiker.yaml").write_text(
        yaml.safe_dump({"trade_def": base_trade_def_dict})
    )
    registry_raw = yaml.safe_load((VARIABLES_DIR / "hitchhiker.yaml").read_text())
    (variables_dir / "hitchhiker.yaml").write_text(yaml.safe_dump(registry_raw))

    with pytest.raises(TaxonomyConfigError) as exc_info:
        load_trade_defs(
            trade_defs_dir=trade_defs_dir,
            variables_dir=variables_dir,
            cameron_grid_path=CAMERON_GRID_PATH,
        )
    assert "no.such.key" in str(exc_info.value)


def test_cfg_key_present_in_tunables_resolves():
    registry = load_tunables()
    defaults = load_defaults()
    assert resolve_cfg("gap_retrace_pct_max", registry.by_key, defaults) == 0.5


def test_cfg_key_defaults_only_resolves_via_fallback():
    # working_timeframe and ma.fast/ma.slow are deliberately NOT
    # tunables.yaml rows (§13.1) — cfg() must fall back to defaults.yaml.
    registry = load_tunables()
    defaults = load_defaults()
    assert "working_timeframe" not in registry.by_key
    assert resolve_cfg("working_timeframe", registry.by_key, defaults) == "2m"
    assert resolve_cfg("ma.slow", registry.by_key, defaults) == 20


def test_cfg_tokens_used_across_committed_trade_defs_all_resolve():
    """Live-data pass: every cfg(key) token actually committed in the 13
    trade_defs resolves (tunables.yaml first, defaults.yaml fallback) —
    load_trade_defs() already fails loud on load if not; this asserts
    the token set is non-empty so the check isn't vacuous."""
    trade_defs = load_trade_defs()
    tokens = {key for td in trade_defs.values() for key in iter_cfg_tokens(td)}
    assert tokens  # not vacuous
    assert "gap_retrace_pct_max" in tokens
    assert "trendline.min_pivots" in tokens
