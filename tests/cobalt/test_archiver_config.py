"""Lists-note-backed archiver config and fail-loud target derivation."""

import subprocess

import pytest
import yaml

from cobalt.archiver.config import ConfigError, load_config
from cobalt.archiver.models import Interval
from cobalt.radar.config import load_config as load_radar_config
from cobalt.radar.models import ListBlock
from cobalt.radar.propose import render_lists
from cobalt.radar.sources import LegacyWatchlistsConfig

FIXED_WATCHLISTS_BLOB = "bedf9bbfdadf98d85c3b3d32cdcb9fb678fb2b99"

COMPLETE = """\
# Synthetic Lists note fixture.

```yaml
list: tier_a
description: test tier a
tickers: [AAA, BBB]
radar: true
archive: [i1, i5]
backfill_default: true
enabled: true
```

```yaml
list: tier_b
description: test tier b
tickers: [SPY]
radar: true
archive: [i30]
backfill_default: false
enabled: true
```

```yaml
list: tier_c
description: test tier c
tickers: [CCC]
radar: true
archive: []
backfill_default: false
enabled: true
```
"""


@pytest.fixture
def rendered_lists_fixture(tmp_path):
    """Render the fixed pre-run YAML blob only into pytest-owned paths."""

    source = tmp_path / "legacy-watchlists.yaml"
    proc = subprocess.run(
        ["git", "cat-file", "blob", FIXED_WATCHLISTS_BLOB],
        capture_output=True,
        check=True,
    )
    source.write_bytes(proc.stdout)
    legacy = LegacyWatchlistsConfig.model_validate(yaml.safe_load(source.read_bytes()))
    vault = tmp_path / "vault"
    note = vault / load_radar_config().notes.lists
    note.parent.mkdir(parents=True)
    note.write_text(render_lists(legacy), encoding="utf-8")
    return vault, note


def _lists(config):
    return {
        item.block.list: item.block
        for item in config.note.blocks
        if isinstance(item.block, ListBlock)
    }


def test_committed_watchlists_config_is_valid(rendered_lists_fixture, monkeypatch):
    vault, _note = rendered_lists_fixture
    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: vault)
    cfg = load_config()
    lists = _lists(cfg)
    assert len(lists["tier_a"].tickers) > 0
    assert lists["tier_a"].archive == [
        Interval.I1, Interval.I2, Interval.I5, Interval.I15, Interval.I30,
    ]
    assert lists["tier_b"].archive == [Interval.I5, Interval.I30]
    assert lists["tier_c"].archive == []


def test_no_ticker_appears_in_more_than_one_tier(rendered_lists_fixture):
    _vault, note = rendered_lists_fixture
    lists = _lists(load_config(note))
    a, b, c = (
        set(lists["tier_a"].tickers),
        set(lists["tier_b"].tickers),
        set(lists["tier_c"].tickers),
    )
    assert not (a & b)
    assert not (a & c)
    assert not (b & c)


def test_vix_excluded_from_every_tier(rendered_lists_fixture):
    _vault, note = rendered_lists_fixture
    lists = _lists(load_config(note))
    all_tickers = set().union(*(item.tickers for item in lists.values()))
    assert "VIX" not in all_tickers


def test_missing_file_crashes(tmp_path):
    with pytest.raises(ConfigError, match="missing"):
        load_config(tmp_path / "absent.md")


def test_invalid_yaml_shape_crashes(tmp_path):
    bad = tmp_path / "Radar Lists.md"
    bad.write_text("```yaml\n- just\n- a\n- list\n```\n")
    with pytest.raises(ConfigError):
        load_config(bad)


def test_unknown_interval_value_rejected(tmp_path):
    bad = tmp_path / "Radar Lists.md"
    bad.write_text(COMPLETE.replace("[i1, i5]", "[i1, i7]"))
    with pytest.raises(ConfigError):
        load_config(bad)


def test_unknown_top_level_key_rejected(tmp_path):
    bad = tmp_path / "Radar Lists.md"
    bad.write_text(COMPLETE.replace("enabled: true\n```", "enabled: true\nunexpected: true\n```", 1))
    with pytest.raises(ConfigError):
        load_config(bad)


def test_archive_targets_covers_tier_a_and_b_not_c(tmp_path):
    note = tmp_path / "Radar Lists.md"
    note.write_text(COMPLETE)
    targets = load_config(note).archive_targets()
    assert set(targets) == {
        ("AAA", Interval.I1), ("AAA", Interval.I5),
        ("BBB", Interval.I1), ("BBB", Interval.I5),
        ("SPY", Interval.I30),
    }
    assert not any(t[0] == "CCC" for t in targets)


def test_backfill_targets_uses_tier_a_intervals_for_any_ticker(tmp_path):
    note = tmp_path / "Radar Lists.md"
    note.write_text(COMPLETE.replace("archive: [i1, i5]", "archive: [i1, i2, i5]"))
    targets = load_config(note).backfill_targets("NEWNAME")
    assert set(targets) == {
        ("NEWNAME", Interval.I1), ("NEWNAME", Interval.I2), ("NEWNAME", Interval.I5),
    }
