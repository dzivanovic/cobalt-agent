"""Strict engine-only radar config tests."""

from pathlib import Path

import pytest

from cobalt.radar.config import CONFIG_PATH, RadarConfigError, check, load_config


def test_shipped_config_and_all_tunables_validate():
    cfg, values = check()
    assert cfg.export.v == 152
    assert set(values) == {
        "radar.scan_interval", "radar.poll_interval", "radar.poll_overlap_bars",
        "radar.finviz_max_rpm", "radar.poll_bar_max_age_s", "db.query.timeout_s",
    }


def test_staleness_key_is_split_poller_180_heartbeat_320():
    from cobalt.taxonomy.loader import load_tunables

    by_key = load_tunables().by_key
    assert by_key["radar.poll_bar_max_age_s"].value == 180
    assert by_key["heartbeat.radar_scan_max_age_s"].value == 320
    assert "heartbeat.radar_max_age_s" not in by_key


def test_extra_key_fails_naming_file(tmp_path):
    path = tmp_path / "radar.yaml"
    path.write_text(CONFIG_PATH.read_text() + "unexpected: true\n")
    with pytest.raises(RadarConfigError, match=str(path)):
        load_config(path)


def test_live_header_capture_has_replaced_unverified_marker():
    assert "# UNVERIFIED" not in CONFIG_PATH.read_text(), (
        "step 6 header capture NOT RUN: configs/cobalt/radar.yaml is still UNVERIFIED"
    )

