"""Strict engine-only radar config tests."""

from pathlib import Path

import pytest

from cobalt.radar.config import (
    CONFIG_PATH,
    RadarConfigError,
    check,
    load_config,
    screener_columns,
    screener_columns_param,
)


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



def test_screener_columns_parses_the_two_declarations_the_radar_uses():
    """`a-b` is inclusive at both ends; a comma list is itself. These are
    the only two shapes Finviz's `c=` takes, and both reach this one
    function — `configs/cobalt/radar.yaml`'s `export.columns` and a
    screen note's own column declaration (L3)."""
    assert screener_columns("0-150") == list(range(0, 151))
    assert screener_columns("0-3") == [0, 1, 2, 3]
    assert screener_columns("7") == [7]
    assert screener_columns("0,1,65") == [0, 1, 65]
    assert screener_columns_param("0-3") == "0,1,2,3"
    assert screener_columns_param(load_config().export.columns) == ",".join(str(i) for i in range(151))


@pytest.mark.parametrize(
    "bad",
    ["", "0-", "-150", "0-150,7", "0..150", "a-b", "150-0", "0, 1", "<same columns>", "0-150 "],
)
def test_a_malformed_column_declaration_crashes(bad):
    """L1: a column set that is silently wrong ships an export whose shape
    nobody notices, so a declaration that is not one of the two shapes is
    a config error, never a best-effort parse. The function tidies
    nothing — `"0-150 "` is malformed; stripping markdown backticks and
    whitespace off a trader's note belongs to the note parser."""
    with pytest.raises(RadarConfigError, match="column declaration"):
        screener_columns(bad)


def test_finviz_ceiling_is_the_ruled_50():
    """Ruled A by Dejan 2026-09-16 07:18 ET (L53: his number): 40 -> 45,
    then 45 -> 50 on 2026-09-17 (R17) so the ceiling IS the archiver's
    pacing bound 60/GENTLE_SLEEP_SECONDS = 60/1.2 = 50.0 rpm — at exactly
    the ceiling the gate passes (`50.0 > 50` is False). The 09-16 ruling
    stays on the row: consumers is the audit trail, not the current value.
    """
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key["radar.finviz_max_rpm"]
    assert row.value == 50
    assert row.source == "ruling"
    assert any("ruled 45 on 2026-09-16" in c for c in row.consumers)
    assert any("ruled 50 on 2026-09-17" in c for c in row.consumers)
