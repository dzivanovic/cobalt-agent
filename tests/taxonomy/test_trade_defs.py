"""Tests for src/cobalt/taxonomy — Batch 1 trade_def schema, loader, and
the `python -m cobalt.taxonomy.validate` CLI."""

from __future__ import annotations

import copy
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from cobalt.taxonomy.loader import TaxonomyConfigError, iter_tunables, load_trade_defs
from cobalt.taxonomy.trade_def import TradeDef, Tunable

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
}


def test_all_six_batch1_trade_defs_load():
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
    assert "6 trade_def(s) validated OK." in result.stdout
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
