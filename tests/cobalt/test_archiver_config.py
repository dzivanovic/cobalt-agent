"""Watchlist config loader tests — fail-loud, and the archive/backfill
target-derivation logic."""

import pytest

from cobalt.archiver import config as archiver_config
from cobalt.archiver.config import ConfigError, WatchlistsConfig, load_config
from cobalt.archiver.models import Interval

COMPLETE = """\
tier_a:
  description: "test tier a"
  intervals: [i1, i5]
  tickers: [AAA, BBB]
tier_b:
  description: "test tier b"
  intervals: [i5]
  tickers: [SPY]
tier_c:
  description: "test tier c"
  intervals: []
  tickers: [CCC]
"""


def test_committed_watchlists_config_is_valid():
    cfg = load_config()
    assert len(cfg.tier_a.tickers) > 0
    assert cfg.tier_a.intervals == [Interval.I1, Interval.I2, Interval.I5, Interval.I15, Interval.I30]
    assert cfg.tier_b.intervals == [Interval.I5, Interval.I30]
    assert cfg.tier_c.intervals == []


def test_no_ticker_appears_in_more_than_one_tier():
    cfg = load_config()
    a, b, c = set(cfg.tier_a.tickers), set(cfg.tier_b.tickers), set(cfg.tier_c.tickers)
    assert not (a & b)
    assert not (a & c)
    assert not (b & c)


def test_vix_excluded_from_every_tier():
    cfg = load_config()
    all_tickers = set(cfg.tier_a.tickers) | set(cfg.tier_b.tickers) | set(cfg.tier_c.tickers)
    assert "VIX" not in all_tickers


def test_missing_file_crashes(monkeypatch, tmp_path):
    monkeypatch.setattr(archiver_config, "CONFIG_PATH", tmp_path / "absent.yaml")
    with pytest.raises(ConfigError, match="not found"):
        load_config()


def test_invalid_yaml_shape_crashes(monkeypatch, tmp_path):
    bad = tmp_path / "watchlists.yaml"
    bad.write_text("- just\n- a\n- list\n")
    monkeypatch.setattr(archiver_config, "CONFIG_PATH", bad)
    with pytest.raises(ConfigError):
        load_config()


def test_unknown_interval_value_rejected(monkeypatch, tmp_path):
    bad = tmp_path / "watchlists.yaml"
    bad.write_text(COMPLETE.replace("[i1, i5]", "[i1, i7]"))
    monkeypatch.setattr(archiver_config, "CONFIG_PATH", bad)
    with pytest.raises(ConfigError):
        load_config()


def test_unknown_top_level_key_rejected(monkeypatch, tmp_path):
    bad = tmp_path / "watchlists.yaml"
    bad.write_text(COMPLETE + "tier_d:\n  description: x\n  intervals: []\n  tickers: []\n")
    monkeypatch.setattr(archiver_config, "CONFIG_PATH", bad)
    with pytest.raises(ConfigError):
        load_config()


def test_archive_targets_covers_tier_a_and_b_not_c():
    cfg = WatchlistsConfig.model_validate(
        {
            "tier_a": {"description": "a", "intervals": ["i1", "i5"], "tickers": ["AAA", "BBB"]},
            "tier_b": {"description": "b", "intervals": ["i30"], "tickers": ["SPY"]},
            "tier_c": {"description": "c", "intervals": [], "tickers": ["CCC"]},
        }
    )
    targets = cfg.archive_targets()
    assert set(targets) == {
        ("AAA", Interval.I1), ("AAA", Interval.I5),
        ("BBB", Interval.I1), ("BBB", Interval.I5),
        ("SPY", Interval.I30),
    }
    assert not any(t[0] == "CCC" for t in targets)


def test_backfill_targets_uses_tier_a_intervals_for_any_ticker():
    cfg = WatchlistsConfig.model_validate(
        {
            "tier_a": {"description": "a", "intervals": ["i1", "i2", "i5"], "tickers": []},
            "tier_b": {"description": "b", "intervals": ["i30"], "tickers": []},
            "tier_c": {"description": "c", "intervals": [], "tickers": []},
        }
    )
    targets = cfg.backfill_targets("NEWNAME")
    assert set(targets) == {
        ("NEWNAME", Interval.I1), ("NEWNAME", Interval.I2), ("NEWNAME", Interval.I5),
    }
