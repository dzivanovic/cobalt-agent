"""Strict engine-only radar config tests."""

import copy
from pathlib import Path

import pytest
import yaml

from cobalt.radar.config import (
    CONFIG_PATH,
    NotEquityConfig,
    RadarConfigError,
    check,
    is_not_equity,
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


# ---------------------------------------------------------------------
# S2-P4 FR-2 — R16 "C": the two-column not-equity rule
# ---------------------------------------------------------------------

#: The shape `radar.yaml` carried until R16 was ruled, and the shape it
#: carries now. Both are written out here so the rejection test builds
#: the old file from the shipped one rather than from a hand-kept copy.
OLD_NOT_EQUITY = "not_equity:\n  header: Asset Type\n  values: [Exchange Traded Fund]\n"
NEW_NOT_EQUITY = (
    "not_equity:\n"
    "  asset_type_header: Asset Type\n"
    "  industry_header: Industry\n"
    "  industry_values: [Exchange Traded Fund]\n"
)


def test_the_shipped_config_carries_the_two_column_not_equity_rule():
    cfg = load_config()
    assert cfg.not_equity.asset_type_header == "Asset Type"
    assert cfg.not_equity.industry_header == "Industry"
    assert cfg.not_equity.industry_values == ["Exchange Traded Fund"]
    assert {"Asset Type", "Industry"} <= set(cfg.export.required_headers)


def test_the_old_one_column_not_equity_shape_is_refused_naming_its_keys(tmp_path):
    """L10/L42: the rule reads two columns now, so a config still on the
    one-column shape is a different rule, not a subset of this one. It is
    refused by name — both the keys that no longer exist and the three
    that must."""
    text = CONFIG_PATH.read_text()
    assert NEW_NOT_EQUITY in text, "the shipped radar.yaml is not on the R16 shape"
    path = tmp_path / "radar.yaml"
    path.write_text(text.replace(NEW_NOT_EQUITY, OLD_NOT_EQUITY))
    with pytest.raises(RadarConfigError) as excinfo:
        load_config(path)
    message = str(excinfo.value)
    for key in ("not_equity.header", "not_equity.values", "not_equity.asset_type_header",
                "not_equity.industry_header", "not_equity.industry_values"):
        assert key in message, key


def test_required_headers_must_carry_both_not_equity_headers(tmp_path):
    """Both columns are read on every row now, so `export.required_headers`
    has to declare both — the same message shape as any other configured
    header missing from the export."""
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    for header in ("Asset Type", "Industry"):
        narrowed = copy.deepcopy(raw)
        narrowed["export"]["required_headers"] = [
            name for name in raw["export"]["required_headers"] if name != header
        ]
        path = tmp_path / "radar.yaml"
        path.write_text(yaml.safe_dump(narrowed, sort_keys=False))
        with pytest.raises(RadarConfigError, match=rf"required_headers missing configured headers \['{header}'\]"):
            load_config(path)


def test_the_not_equity_comment_block_records_the_evidence_not_an_open_question():
    """The block above the rule was a watch item ("unresolved, watch the
    first live run"). The evidence run answered it, so the comment states
    what was counted and where the count lives — counts only (L32)."""
    text = CONFIG_PATH.read_text()
    assert "unresolved, watch the first live run" not in text
    assert "s2-p4-verify-2026-09-19.md" in text
    for phrase in ("5,702 distinct fund tickers", "28 distinct non-blank",
                   "0 stock", "8 distinct funds", "= 16 rows"):
        assert phrase in text, phrase


def test_the_one_evaluator_reads_both_columns_and_strips():
    """`is_not_equity` IS the rule (L3): non-blank `Asset Type` OR a fund
    `Industry`. A missing key, a `None` and a whitespace-only cell are all
    blank; nothing here guesses."""
    rule = NotEquityConfig(asset_type_header="Asset Type", industry_header="Industry",
                           industry_values=["Exchange Traded Fund"])
    assert is_not_equity({"Asset Type": "Equities (Stocks)", "Industry": "Exchange Traded Fund"}, rule) is True
    assert is_not_equity({"Asset Type": "", "Industry": "Exchange Traded Fund"}, rule) is True
    assert is_not_equity({"Asset Type": "Preferred Stock", "Industry": "Capital Markets"}, rule) is True
    assert is_not_equity({"Asset Type": "", "Industry": "Capital Markets"}, rule) is False
    assert is_not_equity({"Asset Type": "   ", "Industry": "  Exchange Traded Fund  "}, rule) is True
    assert is_not_equity({"Asset Type": None, "Industry": None}, rule) is False
    assert is_not_equity({}, rule) is False


def test_the_not_equity_config_refuses_an_empty_header_or_value_list():
    for bad in (
        {"asset_type_header": "", "industry_header": "Industry", "industry_values": ["Exchange Traded Fund"]},
        {"asset_type_header": "Asset Type", "industry_header": "", "industry_values": ["Exchange Traded Fund"]},
        {"asset_type_header": "Asset Type", "industry_header": "Industry", "industry_values": []},
        {"asset_type_header": "Asset Type", "industry_header": "Industry",
         "industry_values": ["Exchange Traded Fund"], "header": "Asset Type"},
    ):
        with pytest.raises(Exception):
            NotEquityConfig(**bad)


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
