"""S2-P2 radar card shape, field ownership and ladder order (STEP-4
Astra R1-7/R1-15, STEP-6 promote).
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.cards.models import CardState
from cobalt.cards.radar import (
    FIELD_OWNERS,
    OWNER_BADGES,
    LadderEntry,
    RadarCardSpec,
    ladder_order,
)
from cobalt.db_migrations import MIGRATIONS_DIR

T0 = datetime(2026, 1, 6, 16, 30, tzinfo=timezone.utc)


def _view_columns() -> list[str]:
    sql = (MIGRATIONS_DIR / "0007_radar_cards.sql").read_text()
    body = sql.split('CREATE OR REPLACE VIEW "user".radar_cards_v AS', 1)[1].split("FROM", 1)[0]
    body = body.replace("SELECT", "")
    names = []
    for item in body.split(","):
        item = item.strip()
        match = re.search(r"AS\s+([a-z0-9_]+)$", item) or re.search(r"\.([a-z0-9_]+)$", item)
        assert match, item
        names.append(match.group(1))
    return names


def test_every_card_field_is_badge_owned():
    columns = _view_columns()
    assert "trigger_price" in columns and "outside_pool" in columns
    assert set(columns) == set(FIELD_OWNERS), (
        sorted(set(columns) ^ set(FIELD_OWNERS))
    )
    assert set(FIELD_OWNERS.values()) <= OWNER_BADGES
    # formation evidence is Cobalt's; the live sizing inputs and the key are his
    assert FIELD_OWNERS["trigger_price"] == "COBALT" and FIELD_OWNERS["structural_stop"] == "COBALT"
    assert FIELD_OWNERS["tapped_grade"] == "YOU" and FIELD_OWNERS["stop"] == "YOU"
    assert FIELD_OWNERS["state"] == "LEDGER"


def _spec(**kw):
    base = dict(
        ticker="FTFT", direction="short", session="RTH", pool_member_id=11,
        trade_def_slug="anatomy-probe", trade_def_md5="a" * 32, setup_ref="overextension",
        trigger_type="bar_break", trigger_price=Decimal("2.50"), stop_ref="snapback_candle",
        structural_stop=Decimal("2.63"), formed_at=T0, expires_at=T0 + timedelta(hours=2),
        why="Extension culminating (path A) — short on a 2-bar break", radar_score_id=5,
        scan_id=1767717000000, formula_sha256="f" * 64, tunables_sha256="e" * 64,
        settings_sha256="d" * 64, proximity=Decimal("0.5"), conviction=None, card_score=None,
        score_suppressed="trail_fit: MANUAL", proposed_key=None, dots=[], evidence={"run_id": 1},
    )
    base.update(kw)
    return RadarCardSpec(**base)


def test_card_carries_setup_trade_trigger_structural_stop_proposed_key_dots_with_why():
    spec = _spec()
    assert spec.setup_ref and spec.trade_def_slug and spec.trigger_type
    assert spec.trigger_price == Decimal("2.50") and spec.structural_stop == Decimal("2.63")
    # the live sizing inputs start AT the formation evidence (R1-7)
    assert spec.entry == spec.trigger_price and spec.stop == spec.structural_stop
    assert spec.per_share_risk == Decimal("0.13")
    assert spec.why
    with pytest.raises(ValueError, match="stop"):
        _spec(structural_stop=Decimal("2.40"))
    with pytest.raises(ValueError, match="stop"):
        _spec(direction="long", structural_stop=Decimal("2.60"))
    with pytest.raises(ValueError):
        _spec(formed_at=datetime(2026, 1, 6, 16, 30))  # naive


def _e(card_id, state="WATCH", score=None, pos=None, promoted=None, ticker=None):
    return LadderEntry(
        card_id=card_id, state=CardState(state), card_score=score, pool_position=pos,
        ticker=ticker or f"T{card_id}", promoted_at=promoted, state_at=T0 + timedelta(minutes=card_id),
    )


def test_equal_scores_and_all_null_scores_order_deterministically():
    ordered = ladder_order([_e(3, score=50, pos=2), _e(1, score=50, pos=2, ticker="AAA"), _e(2, score=50, pos=1)])
    assert [p.card_id for p in ordered.active] == [2, 1, 3]
    nulls = ladder_order([_e(4), _e(2, pos=3), _e(9, pos=1), _e(1)])
    assert [p.card_id for p in nulls.active] == [9, 2, 1, 4]
    mixed = ladder_order([_e(1), _e(2, score=0), _e(3, score=10)])
    assert [p.card_id for p in mixed.active] == [3, 2, 1]  # nulls last, a 0 is a real score


def test_promote_pins_to_2_rank_chip_unchanged_release_restores():
    cards = [_e(1, score=90), _e(2, score=80), _e(3, score=70), _e(4, score=10)]
    natural = ladder_order(cards)
    assert [p.card_id for p in natural.active] == [1, 2, 3, 4]
    chips = {p.card_id: p.rank_chip for p in natural.active}
    promoted = ladder_order([*cards[:3], _e(4, score=10, promoted=T0)])
    assert [p.card_id for p in promoted.active] == [1, 4, 2, 3]
    assert {p.card_id: p.rank_chip for p in promoted.active} == chips  # rank chip unchanged
    assert next(p for p in promoted.active if p.card_id == 4).promoted
    released = ladder_order(cards)
    assert [p.card_id for p in released.active] == [1, 2, 3, 4]
    # a card already at #1 is not demoted by promotion
    top = ladder_order([_e(1, score=90, promoted=T0), _e(2, score=80)])
    assert [p.card_id for p in top.active] == [1, 2]


def test_two_pinned_cards_keep_priority_over_a_promotion():
    cards = [
        _e(1, state="ARMED", pos=3), _e(2, state="FILLED", pos=1),
        _e(3, score=90), _e(4, score=10, promoted=T0),
    ]
    ordered = ladder_order(cards)
    assert [p.card_id for p in ordered.active] == [2, 1, 4, 3]
    assert [p.rank_chip for p in ordered.active if p.card_id in (3, 4)] == [2, 1]
    assert ordered.active[0].pinned and not ordered.active[2].pinned


def test_one_promoted_card_at_most_and_terminal_cards_are_separate():
    with pytest.raises(ValueError, match="one promoted"):
        ladder_order([_e(1, promoted=T0), _e(2, promoted=T0)])
    ordered = ladder_order([_e(1, score=5), _e(2, state="EXPIRED"), _e(3, state="PASSED")])
    assert [p.card_id for p in ordered.active] == [1]
    assert {p.card_id for p in ordered.terminal} == {2, 3}
    with pytest.raises(ValueError, match="WATCH"):
        ladder_order([_e(1, state="ARMED", promoted=T0)])
