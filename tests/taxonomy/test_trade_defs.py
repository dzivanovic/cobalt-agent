"""The trade_def SCHEMA — v0.4 minus authored id/name, plus structured
quality_factors (ADR-0008 D3).

Every fixture here is the repo's one SYNTHETIC strategy note. These tests
used to mutate a copy of a real, sheet-derived trade_def out of
`configs/cobalt/taxonomy/trade_defs/`; those files are user data and are
gone (D3), so the schema is now exercised against a def written in
anatomy terms only.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from cobalt.taxonomy.defaults import TaxonomyDefaults
from cobalt.taxonomy.loader import (
    TaxonomyConfigError,
    is_ma_ref,
    iter_cfg_tokens,
    iter_stop_buffers,
    load_defaults,
    load_tunables,
    merge_tunables,
    resolve_cfg,
    resolve_ma_ref,
)
from cobalt.taxonomy.trade_def import (
    ExitLeg,
    IndicatorPlacement,
    QualityFactor,
    TradeDef,
)
from cobalt.taxonomy.tunables import TunableRegistry, TunableRow, TunableStatus, replay_backlog

from taxonomy_example import EXAMPLE_NAME, EXAMPLE_SLUG


def _build(mapping) -> TradeDef:
    return TradeDef.from_unit(mapping, slug=EXAMPLE_SLUG, name=EXAMPLE_NAME)


# ---------------------------------------------------------------------
# id / name are loader-injected (ruling a, ruling e)
# ---------------------------------------------------------------------


class TestInjectedIdentity:
    def test_from_unit_injects_slug_and_name(self, base_trade_def_dict):
        td = _build(base_trade_def_dict)
        assert td.id == EXAMPLE_SLUG
        assert td.name == EXAMPLE_NAME

    @pytest.mark.parametrize("field", ["id", "name"])
    def test_an_authored_id_or_name_fails_loud(self, base_trade_def_dict, field):
        base_trade_def_dict[field] = "whatever"
        with pytest.raises(ValueError, match="id/name come from frontmatter"):
            _build(base_trade_def_dict)

    def test_the_example_unit_authors_neither(self, base_trade_def_dict):
        """The shipped example is the contract's own worked example."""
        assert "id" not in base_trade_def_dict
        assert "name" not in base_trade_def_dict

    def test_the_model_still_requires_both(self):
        """Injected, not optional: a TradeDef always knows what it is."""
        with pytest.raises(ValidationError):
            TradeDef(family=["range_break"])  # type: ignore[call-arg]


# ---------------------------------------------------------------------
# quality_factors: the variable registry, folded in (ruling b.2)
# ---------------------------------------------------------------------


class TestQualityFactors:
    def test_a_bare_string_takes_every_default(self):
        q = QualityFactor.model_validate("rvol")
        assert q.name == "rvol"
        assert q.source == "human"
        assert q.tier == "judgment"
        assert q.status == "stub"
        assert q.frontier is False
        assert (q.scale_min, q.scale_max) == (1, 10)

    def test_a_mapping_carries_attributes(self):
        q = QualityFactor.model_validate(
            {"name": "tape_read", "source": "human", "frontier": True}
        )
        assert q.frontier is True
        assert q.name == "tape_read"

    def test_the_example_mixes_both_forms(self, base_trade_def_dict):
        td = _build(base_trade_def_dict)
        assert len(td.quality_factors) >= 4
        assert any(q.frontier for q in td.quality_factors)
        assert any(not q.frontier and q.status == "stub" for q in td.quality_factors)

    def test_unknown_attribute_is_refused(self):
        with pytest.raises(ValidationError):
            QualityFactor.model_validate({"name": "x", "vibes": 3})

    def test_standard_trio_still_required(self, base_trade_def_dict):
        base_trade_def_dict["quality_factors"] = ["range_duration"]
        with pytest.raises(ValidationError, match="standard trio"):
            _build(base_trade_def_dict)

    def test_duplicate_names_fail_loud(self, base_trade_def_dict):
        base_trade_def_dict["quality_factors"].append("setup_relation")
        with pytest.raises(ValidationError, match="duplicate quality_factors"):
            _build(base_trade_def_dict)

    def test_names_helper(self, base_trade_def_dict):
        td = _build(base_trade_def_dict)
        assert td.quality_factor_names == [q.name for q in td.quality_factors]


# ---------------------------------------------------------------------
# valid_setups: what is left of the setup x trade matrix check (b.1)
# ---------------------------------------------------------------------


class TestValidSetups:
    def test_duplicate_pairs_fail_loud(self, base_trade_def_dict):
        base_trade_def_dict["valid_setups"].append(
            dict(base_trade_def_dict["valid_setups"][0])
        )
        with pytest.raises(ValidationError, match="duplicate valid_setups"):
            _build(base_trade_def_dict)

    def test_unknown_setup_ref_fails_loud(self, base_trade_def_dict):
        base_trade_def_dict["valid_setups"][0]["setup_ref"] = "not_a_setup"
        with pytest.raises(ValidationError, match="setup_ref"):
            _build(base_trade_def_dict)

    def test_empty_is_refused(self, base_trade_def_dict):
        base_trade_def_dict["valid_setups"] = []
        with pytest.raises(ValidationError):
            _build(base_trade_def_dict)


# ---------------------------------------------------------------------
# v0.4 schema, unchanged by ADR-0008
# ---------------------------------------------------------------------


def test_unknown_enum_value_raises_loud_with_field_path(base_trade_def_dict):
    base_trade_def_dict["class"] = "not_a_real_class"
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
    assert "class" in str(exc_info.value)


def test_exit_fractions_summing_to_point_nine_raises_loud(base_trade_def_dict):
    base_trade_def_dict["exit"][0]["fraction"] = 0.4
    base_trade_def_dict["exit"][1]["fraction"] = 0.5  # 0.9, outside +/-0.01
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
    assert "exit fractions sum to" in str(exc_info.value)


def test_stop_buffer_spread_is_rejected_with_field_path(base_trade_def_dict):
    base_trade_def_dict["stop"]["placement"]["buffer"]["type"] = "spread"
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
    assert "buffer" in str(exc_info.value)


def test_indicator_placement_accepts_known_indicator(base_trade_def_dict):
    base_trade_def_dict["stop"]["placement"] = {
        "type": "indicator",
        "indicator": "EMA21",
        "snapshot": "live",
    }
    td = _build(base_trade_def_dict)
    assert isinstance(td.stop.placement, IndicatorPlacement)
    assert td.stop.placement.indicator == "EMA21"
    assert td.stop.placement.snapshot == "live"
    assert td.stop.placement.buffer.cents.value == "cfg(stop.buffer)"


def test_indicator_placement_rejects_unknown_indicator(base_trade_def_dict):
    base_trade_def_dict["stop"]["placement"] = {"type": "indicator", "indicator": "SMA50"}
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
    assert "indicator" in str(exc_info.value)


@pytest.mark.parametrize("trigger_type", ["trendline_break", "indicator_rejection"])
def test_new_trigger_types_load(base_trade_def_dict, trigger_type):
    base_trade_def_dict["trigger"] = {
        "type": trigger_type,
        "params": {"indicator": "VWAP"},
        "confirmation_policy": {"type": "close_through"},
    }
    td = _build(base_trade_def_dict)
    assert td.trigger.type == trigger_type


def test_trail_slot_conditions_validate(base_trade_def_dict):
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
        {"fraction": 1.0, "target_type": "trail", "params": {}, "evaluation": "close_through"}
    ]
    td = _build(base_trade_def_dict)
    assert len(td.trail.conditions) == 4
    assert td.trail.mode == "select"


def test_trail_slot_rejects_unknown_condition_type(base_trade_def_dict):
    base_trade_def_dict["trail"] = {"conditions": [{"type": "moon_phase"}], "mode": "select"}
    base_trade_def_dict["exit"] = [
        {"fraction": 1.0, "target_type": "trail", "params": {}, "evaluation": "close_through"}
    ]
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
    assert "trail" in str(exc_info.value)


def test_trail_exit_leg_rejects_nonempty_params():
    with pytest.raises(ValidationError):
        ExitLeg(
            fraction=1.0,
            target_type="trail",
            params={"conditions": [], "mode": "any"},
            evaluation="close_through",
        )


def test_trail_exit_leg_accepts_empty_params():
    leg = ExitLeg(fraction=1.0, target_type="trail", params={}, evaluation="close_through")
    assert leg.params == {}


def test_trail_exit_without_trail_slot_raises_loud(base_trade_def_dict):
    base_trade_def_dict["trail"] = None
    base_trade_def_dict["exit"] = [
        {"fraction": 1.0, "target_type": "trail", "params": {}, "evaluation": "close_through"}
    ]
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
    assert "trade_def.trail" in str(exc_info.value)


@pytest.mark.parametrize("stop_mgmt_type", ["trail_ma_close", "trail_bar"])
def test_removed_stop_management_trail_spellings_fail_loud(
    base_trade_def_dict, stop_mgmt_type
):
    base_trade_def_dict["stop_management"] = [
        {"type": stop_mgmt_type, "on": {"name": "entry"}}
    ]
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
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
        _build(base_trade_def_dict)
    assert "trail" in str(exc_info.value)


def test_reentry_window_accepts_duration_string(base_trade_def_dict):
    base_trade_def_dict["reentry_window"] = {"value": "3 min", "dynamic": False}
    assert _build(base_trade_def_dict).reentry_window.value == "3 min"


def test_reentry_window_rejects_bad_format(base_trade_def_dict):
    base_trade_def_dict["reentry_window"] = {"value": "soon", "dynamic": False}
    with pytest.raises(ValidationError) as exc_info:
        _build(base_trade_def_dict)
    assert "reentry_window" in str(exc_info.value)


def test_stop_buffer_cents_must_be_cfg_ref(base_trade_def_dict):
    base_trade_def_dict["stop"]["placement"]["buffer"]["cents"] = {
        "value": 0.05,
        "dynamic": False,
    }
    with pytest.raises(ValidationError):
        _build(base_trade_def_dict)


def test_iter_stop_buffers_finds_every_buffer_in_a_trade_def(base_trade_def_dict):
    base_trade_def_dict["stop_management"].append(
        {
            "type": "raise_to",
            "on": {"name": "exit_leg", "n": 1},
            "placement": {"type": "structural_extreme", "ref": "entry"},
        }
    )
    buffers = list(iter_stop_buffers(_build(base_trade_def_dict)))
    assert len(buffers) >= 2  # stop.placement.buffer + raise_to.placement.buffer
    assert all(b.cents.value == "cfg(stop.buffer)" for b in buffers)


# ---------------------------------------------------------------------
# ma refs / cfg resolution
# ---------------------------------------------------------------------


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


def test_stop_buffer_global_row_resolves():
    assert resolve_cfg("stop.buffer", load_tunables().by_key, load_defaults()) == 0.02


def test_stop_buffer_row_removed_fails_loud():
    with pytest.raises(TaxonomyConfigError):
        resolve_cfg("stop.buffer", {}, load_defaults())


def test_cfg_key_present_in_tunables_resolves():
    assert resolve_cfg("gap_retrace_pct_max", load_tunables().by_key, load_defaults()) == 0.5


def test_cfg_key_defaults_only_resolves_via_fallback():
    # working_timeframe and ma.fast/ma.slow are deliberately NOT
    # tunables.yaml rows (§13.1) — cfg() must fall back to defaults.yaml.
    registry = load_tunables()
    defaults = load_defaults()
    assert "working_timeframe" not in registry.by_key
    assert resolve_cfg("working_timeframe", registry.by_key, defaults) == "2m"
    assert resolve_cfg("ma.slow", registry.by_key, defaults) == 20


def test_the_example_defs_cfg_tokens_all_resolve(base_trade_def_dict):
    """Not vacuous: the example deliberately references BOTH an engine key
    and a key that only its own note's tunables unit defines."""
    tokens = set(iter_cfg_tokens(_build(base_trade_def_dict)))
    assert "stop.buffer" in tokens
    assert "range.wick_ratio_max" in tokens
    assert "example_range_break.range_duration_band" in tokens


# ---------------------------------------------------------------------
# engine ∪ user tunables (ruling b.3 / d)
# ---------------------------------------------------------------------


def _row(key: str, scope: str = "global") -> TunableRow:
    return TunableRow(
        key=key, value=1, unit="count", scope=scope,
        dynamic=False, status="proposed", source="ruling",
    )


class TestMergeTunables:
    def test_union_of_disjoint_sets(self):
        merged = merge_tunables(
            {"engine.key": _row("engine.key")},
            {"example_x.key": _row("example_x.key", "per_trade(example_x)")},
        )
        assert set(merged) == {"engine.key", "example_x.key"}

    def test_a_user_row_shadowing_an_engine_key_is_a_collision(self):
        with pytest.raises(TaxonomyConfigError, match="shadow engine keys"):
            merge_tunables({"stop.buffer": _row("stop.buffer")},
                           {"stop.buffer": _row("stop.buffer")})

    def test_resolve_cfg_reads_the_union(self):
        merged = merge_tunables(load_tunables().by_key, {"example_x.band": _row("example_x.band")})
        assert resolve_cfg("example_x.band", merged, load_defaults()) == 1
        assert resolve_cfg("stop.buffer", merged, load_defaults()) == 0.02

    def test_an_unknown_key_is_still_loud(self):
        with pytest.raises(TaxonomyConfigError, match="no.such.key"):
            resolve_cfg("no.such.key", load_tunables().by_key, load_defaults())


# ---------------------------------------------------------------------
# replay backlog (unchanged)
# ---------------------------------------------------------------------


def test_dynamic_tunables_appear_in_replay_backlog():
    registry = load_tunables()
    backlog = replay_backlog(registry)
    assert backlog, "tunables.yaml seeded no dynamic, non-solidified rows"
    assert all(row.dynamic for row in backlog)
    assert all(row.status != TunableStatus.SOLIDIFIED for row in backlog)
    assert "gap_retrace_pct_max" in {row.key for row in backlog}


def test_dynamic_tunable_backlog_matching_actually_discriminates():
    """Unit-level proof the backlog query is real, not vacuously true."""
    registry = TunableRegistry(
        tunables=[
            {"key": "included.row", "value": 1, "unit": "count", "scope": "global",
             "dynamic": True, "status": "proposed", "source": "dwv"},
            {"key": "excluded.solidified", "value": 1, "unit": "count", "scope": "global",
             "dynamic": True, "status": "solidified", "source": "ruling"},
            {"key": "excluded.not_dynamic", "value": 1, "unit": "count", "scope": "global",
             "dynamic": False, "status": "proposed", "source": "sheet"},
        ]
    )
    assert {row.key for row in replay_backlog(registry)} == {"included.row"}
