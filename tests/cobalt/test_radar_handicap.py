"""Float handicap H1 (FLOAT-HANDICAP-v3, [F-12], §3, §5): the block and the
header config (STEP-2).

Every block here is CONSTRUCTED from this file's own literals (L32, L69):
thresholds 20 / 300 (the export's units: millions of shares, $ millions),
factor 0.8 — none of them his. Both Literal values of `missing`, of
`combinator` and of `mode` are exercised, so no value of his is privileged.
"""

from __future__ import annotations

import copy
from decimal import Decimal
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from cobalt.radar.config import CONFIG_PATH, RadarConfigError, load_config
from cobalt.radar.models import HandicapBlock, PoolBlock
from cobalt.radar.notes import load_sources, parse_note_bytes

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "radar"
KEYS = ("float_below_m", "market_cap_below_m", "factor", "missing", "mode", "combinator")


def block(**overrides) -> dict:
    values = {
        "float_below_m": "20",
        "market_cap_below_m": "300",
        "factor": "0.8",
        "missing": "apply",
        "mode": "shadow",
        "combinator": "any",
    }
    values.update(overrides)
    return values


def pool(**handicap) -> dict:
    raw = {
        "kind": "pool", "cap": 5, "priority": ["screens", "lists"],
        "rank_metric": {"premarket": "volume", "rth": "rvol", "aftermarket": "volume"},
        "overrides": {}, "stickiness_scans": 2,
    }
    if handicap:
        raw["handicap"] = handicap
    return raw


# ---------------------------------------------------------------------
# STEP-2 (i): HandicapBlock — exactly [F-12]'s six keys, no default
# ---------------------------------------------------------------------


def test_the_block_has_exactly_the_six_keys_and_no_default():
    assert tuple(HandicapBlock.model_fields) == KEYS
    assert all(field.is_required() for field in HandicapBlock.model_fields.values())
    parsed = HandicapBlock(**block())
    assert (parsed.float_below_m, parsed.market_cap_below_m, parsed.factor) == (
        Decimal("20"), Decimal("300"), Decimal("0.8"),
    )


@pytest.mark.parametrize("key", KEYS)
def test_a_block_missing_any_key_is_refused_naming_it(key):
    raw = block()
    del raw[key]
    with pytest.raises(ValidationError, match=key):
        HandicapBlock(**raw)


def test_a_seventh_key_is_refused():
    with pytest.raises(ValidationError, match="decisive"):
        HandicapBlock(**block(decisive=True))


@pytest.mark.parametrize("factor", ["0", "-0.1", "1.0001", "2"])
def test_factor_outside_zero_to_one_is_refused(factor):
    with pytest.raises(ValidationError, match="factor"):
        HandicapBlock(**block(factor=factor))


def test_a_yaml_float_reaches_the_block_as_its_written_digits():
    """His note is YAML: `factor: 0.8` loads as a binary float. The block
    must hold the digits he wrote, or the stored NUMERIC(6,4) factor would
    not replay the would-be rank (L57)."""
    parsed = HandicapBlock(**{**block(), "factor": 0.8, "float_below_m": 20.5, "market_cap_below_m": 300.25})
    assert (parsed.factor, parsed.float_below_m, parsed.market_cap_below_m) == (
        Decimal("0.8"), Decimal("20.5"), Decimal("300.25"),
    )


def test_a_factor_finer_than_the_stored_column_is_refused():
    """`handicap_factor` is NUMERIC(6,4) (v3 §6): a fifth decimal could not
    be stored as read, so it is refused where it is read."""
    with pytest.raises(ValidationError, match="factor"):
        HandicapBlock(**block(factor="0.12345"))
    assert HandicapBlock(**block(factor="0.1234")).factor == Decimal("0.1234")


def test_factor_one_is_accepted_and_both_thresholds_must_be_positive():
    assert HandicapBlock(**block(factor="1")).factor == Decimal("1")
    for key in ("float_below_m", "market_cap_below_m"):
        with pytest.raises(ValidationError, match=key):
            HandicapBlock(**block(**{key: "0"}))


@pytest.mark.parametrize(
    "key,good,bad",
    [("missing", ("apply", "skip"), "ignore"), ("mode", ("shadow", "live"), "off"),
     ("combinator", ("any", "all"), "or")],
)
def test_every_literal_key_takes_both_of_its_values_and_nothing_else(key, good, bad):
    for value in good:
        assert getattr(HandicapBlock(**block(**{key: value})), key) == value
    with pytest.raises(ValidationError, match=key):
        HandicapBlock(**block(**{key: bad}))


# ---------------------------------------------------------------------
# STEP-2 (ii): PoolBlock.handicap — optional, absent = None = OFF
# ---------------------------------------------------------------------


def test_an_absent_block_is_none_and_leaves_the_pool_dump_byte_identical():
    parsed = PoolBlock(**pool())
    assert parsed.handicap is None
    assert "handicap" not in parsed.model_dump(mode="json")
    assert set(parsed.model_dump(mode="json")) == {
        "kind", "cap", "priority", "rank_metric", "overrides", "stickiness_scans",
    }


def test_a_present_block_parses_nested_and_dumps():
    parsed = PoolBlock(**pool(**block()))
    assert isinstance(parsed.handicap, HandicapBlock)
    assert parsed.model_dump(mode="json")["handicap"]["combinator"] == "any"


# ---------------------------------------------------------------------
# STEP-2 (iii): the loud refusal through the real reader (L1, F14)
# ---------------------------------------------------------------------


def _note_with(handicap_yaml: bytes | None) -> bytes:
    """The committed screens note that carries a pool block, with the
    `handicap:` sub-block appended as the pool block's last key."""
    payload = (FIXTURES / "radar-screens.example.md").read_bytes()
    if handicap_yaml is None:
        return payload
    start = payload.index(b"kind: pool")
    end = payload.index(b"\n```", start)
    return payload[: end + 1] + handicap_yaml.rstrip(b"\n") + payload[end:]


def _yaml(values: dict) -> bytes:
    return yaml.safe_dump({"handicap": values}, sort_keys=False).encode()


def _load(tmp_path, payload: bytes):
    screens = tmp_path / "screens.md"
    screens.write_bytes(payload)
    return load_sources(
        screens, FIXTURES / "radar-lists.example.md", scan_interval=60, poll_interval=60,
        finviz_max_rpm=None, list_chunk_size=1, context_tickers=0,
    )


def test_a_present_block_missing_combinator_freezes_the_pool_naming_it(tmp_path):
    raw = block()
    del raw["combinator"]
    payload = _note_with(_yaml(raw))
    note = parse_note_bytes(Path("screens.md"), "screens", payload)
    assert any("combinator" in error for error in note.errors)
    parsed = _load(tmp_path, payload)
    assert parsed.pool_error is not None and "combinator" in parsed.pool_error
    assert parsed.frozen


def test_an_absent_block_parses_with_handicap_none():
    note = parse_note_bytes(Path("screens.md"), "screens", _note_with(None))
    assert not note.errors
    (pool_block,) = [item.block for item in note.blocks if item.key == "pool"]
    assert pool_block.handicap is None


@pytest.mark.parametrize("combinator", ["any", "all"])
@pytest.mark.parametrize("missing", ["apply", "skip"])
def test_a_complete_block_parses(missing, combinator):
    note = parse_note_bytes(
        Path("screens.md"), "screens", _note_with(_yaml(block(missing=missing, combinator=combinator)))
    )
    assert not note.errors
    (pool_block,) = [item.block for item in note.blocks if item.key == "pool"]
    assert (pool_block.handicap.missing, pool_block.handicap.combinator) == (missing, combinator)


# ---------------------------------------------------------------------
# STEP-2 (iv): export.handicap_headers — engine config, required
# ---------------------------------------------------------------------


def test_the_shipped_config_names_both_handicap_headers_outside_required_headers():
    cfg = load_config()
    headers = cfg.export.handicap_headers
    assert (headers.float, headers.market_cap) == ("Shares Float", "Market Cap")
    assert not {headers.float, headers.market_cap} & set(cfg.export.required_headers)


def test_a_config_without_handicap_headers_is_refused_naming_it(tmp_path):
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    broken = copy.deepcopy(raw)
    del broken["export"]["handicap_headers"]
    path = tmp_path / "radar.yaml"
    path.write_text(yaml.safe_dump(broken))
    with pytest.raises(RadarConfigError, match="handicap_headers"):
        load_config(path)


@pytest.mark.parametrize("key", ["float", "market_cap"])
def test_a_config_missing_one_header_name_is_refused(tmp_path, key):
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    del raw["export"]["handicap_headers"][key]
    path = tmp_path / "radar.yaml"
    path.write_text(yaml.safe_dump(raw))
    with pytest.raises(RadarConfigError, match=key):
        load_config(path)
