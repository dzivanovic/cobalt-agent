"""Config loader tests: rules.yaml / strategies.yaml / prefill.yaml all
load and validate against the real committed files (config-as-code —
these are fixtures in their own right, not fakes)."""

from cobalt.prefill.config import (
    load_prefill_paths,
    load_rules_config,
    load_strategies_config,
)


def test_rules_config_loads_and_has_known_ids():
    cfg = load_rules_config()
    ids = {r.id for r in cfg.rules}
    # SLICE 2.1: ids are rule_NN, positional off Rules.md's own numbering
    # (the source of truth) — no more hand-authored semantic ids.
    assert "rule_01" in ids
    assert "rule_12" in ids
    assert len(cfg.rules) == 12
    assert any(m.id == "tape_check" for m in cfg.mantras)
    assert cfg.generated.source.endswith("Rules.md")
    assert len(cfg.generated.source_sha256) == 64


def test_rules_have_valid_categories():
    cfg = load_rules_config()
    categories = {r.category for r in cfg.rules}
    assert categories <= {
        "process", "sizing", "time_window", "re_entry", "circuit_breaker", "hard_stop",
    }


def test_strategies_config_reversion_lookup():
    cfg = load_strategies_config()
    assert cfg.is_reversion("Rubber Band Scalp") is True
    assert cfg.is_reversion("VWAP Continuation") is False
    assert cfg.is_reversion("Not A Real Strategy") is False
    assert cfg.is_reversion(None) is False
    assert cfg.is_reversion("") is False


def test_prefill_paths_config_loads():
    cfg = load_prefill_paths()
    assert cfg.trades_dir == "1 - Trading/2 - Trades"
    assert cfg.review_dir == "1 - Trading/5 - Review"
    assert "%Y-%m-%d" in cfg.drc_filename_pattern
    assert "{ticker}" in cfg.trade_filename_pattern
