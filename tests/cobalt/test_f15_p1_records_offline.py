"""F15 P1 — the prediction record, offline (card 61 rows M1, M2, W1, G1,
H2, H3; FINAL §3, `[F-32]`, `[F-37]`, `[F-38]`, `[F-40]`).

The DDL's behaviour and the three hooks are `test_f15_p1_records_db.py`
(with-DB). This file pins the seams other lanes cite: the registry and the
side of `0022`, the digest tuple, the Pydantic shapes validated before
INSERT (L10), `grade_why`'s purity, and the two store signatures.
Every value is constructed (L32).
"""

from __future__ import annotations

import inspect
from datetime import timedelta

import pytest
from pydantic import ValidationError

from cobalt.db import Side


def test_0022_is_registered_second_last_and_placed_user_side():
    from cobalt.db_migrations import FORWARD, REVERSE
    from cobalt.db_migrations.placement import CREATED_TABLES, DECLARED_TABLES

    # The price floor's 0023 (R692) now follows it.
    assert FORWARD[-1].name == "0023_radar_price_floor.sql"
    assert REVERSE[0].name == "0023_radar_price_floor.rollback.sql"
    assert FORWARD[-2].name == "0022_prediction_records.sql"
    assert REVERSE[1].name == "0022_prediction_records.rollback.sql"
    assert FORWARD[-2].exists() and REVERSE[1].exists()
    assert CREATED_TABLES["prediction_records"] is Side.USER
    assert "prediction_records" not in DECLARED_TABLES, "built now: it leaves DECLARED"


def test_last_price_bar_ts_is_excluded_from_the_aset_sizings_digest():
    from cobalt.db_migrations.cli import TABLE_DIGEST_EXCLUDED_COLUMNS

    assert "last_price_bar_ts" in TABLE_DIGEST_EXCLUDED_COLUMNS["aset_sizings"]


SCAN_INPUTS = {"taps_moved": False, "locked": None}
TAP_INPUTS = {
    "tap_id": 7,
    "dots": [{"factor": "trail_fit", "source": "cobalt", "tier": "deterministic", "na_reason": "MANUAL",
              "engine_grade": None, "trader_grade": 8}],
    "proximity": "0.5",
    "score_suppressed_before": None,
    "bands": {"a_plus_min": "0.9", "a_min": "0.8", "b_min": "0.6", "c_min": "0.4"},
    "enabled": ["A", "B", "C"],
}
OUTPUT = {"proximity": "0.5", "conviction": "0.8", "card_score": 40, "score_suppressed": None,
          "proposed_key": "A", "proposed_key_reason": None,
          "dots": [{"factor": "trail_fit", "engine_value": None, "engine_grade": None, "na_reason": "MANUAL",
                    "trader_grade": 8}]}


def _record(**over):
    from datetime import datetime, timezone

    values = dict(card_id=1, seq=1, transition_id=1, kind="refresh", at=datetime(2026, 1, 6, 16, 30, tzinfo=timezone.utc),
                  scorer_id="card_grade", scorer_version="s2p2.3", formula_sha256="a" * 64, settings_sha256="b" * 64,
                  run_id=11, inputs=SCAN_INPUTS, output=OUTPUT, why="w")
    values.update(over)
    return values


def test_record_inputs_refuses_a_missing_or_extra_key_and_a_non_hex_sha():
    from cobalt.cards.predictions import PredictionRecord, RecordInputs

    assert RecordInputs.model_validate({"kind": "refresh", "inputs": SCAN_INPUTS}).inputs.taps_moved is False
    assert RecordInputs.model_validate({"kind": "tap", "inputs": TAP_INPUTS}).inputs.tap_id == 7
    locked = {"taps_moved": True, "locked": {"conviction": "0.8", "score_suppressed": None, "proposed_key": "A"}}
    assert RecordInputs.model_validate({"kind": "refresh", "inputs": locked}).inputs.locked.proposed_key == "A"
    for kind, bad in (
        ("create", {"taps_moved": False}),  # a missing key: `locked` is required even when null
        ("refresh", {**SCAN_INPUTS, "card": {}}),  # an extra key
        ("refresh", {"taps_moved": True, "locked": {"conviction": "0.8", "score_suppressed": None}}),  # locked w/o key
        ("tap", {k: v for k, v in TAP_INPUTS.items() if k != "bands"}),  # a tap without bands
        ("tap", {k: v for k, v in TAP_INPUTS.items() if k != "enabled"}),  # a tap without enabled
        ("tap", SCAN_INPUTS),  # a scan shape under the tap kind
        ("scan", SCAN_INPUTS),  # no such kind
    ):
        with pytest.raises(ValidationError):
            RecordInputs.model_validate({"kind": kind, "inputs": bad})
    assert PredictionRecord.model_validate(_record()).seq == 1
    for over in (
        {"settings_sha256": "B" * 64},  # not lowercase hex
        {"settings_sha256": "b" * 63},
        {"formula_sha256": "z" * 64},
        {"kind": "tap", "run_id": 11, "inputs": TAP_INPUTS},  # a tap carries no run
        {"kind": "refresh", "run_id": None},  # a scan record names its run
        {"output": {**OUTPUT, "extra": 1}},
        {"scorer_id": "swing"},
    ):
        with pytest.raises(ValidationError):
            PredictionRecord.model_validate(_record(**over))


def test_grade_why_is_pure_and_deterministic():
    from cobalt.cards.scoring import grade_why

    first = grade_why(OUTPUT)
    assert first == grade_why(dict(OUTPUT)) and isinstance(first, str) and first
    assert grade_why({**OUTPUT, "card_score": 41}) != first
    suppressed = grade_why({**OUTPUT, "card_score": None, "score_suppressed": "bars stale — no proximity"})
    assert "bars stale — no proximity" in suppressed
    assert "trail_fit" in first


def test_refresh_radar_card_requires_run_id_and_card_update_carries_the_bar_start():
    from cobalt.aset.models import Grade
    from cobalt.cards.store import CardStore
    from cobalt.radar.evaluate import refresh_card
    from cobalt.settings.card import CardSettings

    import radar_p2_support as sup
    from test_radar_evaluate import ENABLED_CARD, SCAN0, World

    run_id = inspect.signature(CardStore.refresh_radar_card).parameters["run_id"]
    assert run_id.kind is inspect.Parameter.KEYWORD_ONLY and run_id.default is inspect.Parameter.empty
    world = World()
    world.scan(SCAN0)
    card = world.cards.open_radar_cards()[0]
    later = world.scan(SCAN0 + timedelta(seconds=100))
    ev = next(e for e in later.evaluations if e.membership_id == card.pool_member_id)
    assert ev.last_bar_ts is not None
    update = refresh_card(card, ev, sup.loaded(), CardSettings.from_rows(sup.fixture_settings_rows(**ENABLED_CARD)),
                          list(Grade), at=SCAN0 + timedelta(seconds=100), thresholds=None)
    assert update.last_price_bar_ts == ev.last_bar_ts
    assert update.last_price == ev.last_price


def test_tap_dot_takes_settings_not_bands():
    from cobalt.cards.store import CardStore

    params = inspect.signature(CardStore.tap_dot).parameters
    assert "bands" not in params
    for name in ("settings", "enabled"):
        assert params[name].kind is inspect.Parameter.KEYWORD_ONLY, name
        assert params[name].default is inspect.Parameter.empty, name
