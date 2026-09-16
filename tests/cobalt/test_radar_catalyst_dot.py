"""S2-P2 STEP-9, declared treatment (Astra R2-4): a card that already
exists when its trade_def acquires `catalyst`.

D2 precedes D3/D4, so this is the normal case. Adding the `- catalyst`
line changes the Definition unit's bytes and therefore the def's md5; the
open card still carries the md5 it formed under (immutable formation
evidence). The next evaluate cycle refreshes the card against the def of
the SAME slug, adds the missing `catalyst` dot once — hollow/shadow,
`source: cobalt-degraded`, `na_reason: DESK_NA`, no trader grade — keeps
every tap and the formation evidence, and records which definition and
run added it.
"""

from __future__ import annotations

from datetime import timedelta

import pytest

import radar_p2_support as sup
from cobalt.radar.evaluate import replay_receipt
from cobalt.session import session_clock
from test_radar_evaluate import SCAN0, World

CATALYST_MD5 = "c" * 32


def _with_catalyst():
    return sup.loaded(sup.anatomy_def(quality_factors=[*sup.ANATOMY_FACTORS, "catalyst"]), md5=CATALYST_MD5)


def test_a_card_formed_before_the_def_gained_catalyst_gets_one_hollow_desk_na_dot():
    world = World()
    world.scan(SCAN0)
    card = world.cards.cards[1]
    evidence = {k: card[k] for k in ("trade_def_md5", "trigger_price", "structural_stop", "formed_at")}
    assert "catalyst" not in {d.factor for d in card["dots"]}
    world.cards.tap(1, "setup_relation", 8)

    world.defs = [_with_catalyst()]
    outcome = world.scan(SCAN0 + timedelta(seconds=100))
    assert outcome.refreshed == [1] and not outcome.refusals, outcome.refusals
    card = world.cards.cards[1]
    dots = {d.factor: d for d in card["dots"]}
    dot = dots["catalyst"]
    assert (dot.role, dot.source, dot.na_reason, dot.trader_grade) == ("shadow", "cobalt-degraded", "DESK_NA", None)
    assert dots["setup_relation"].trader_grade == 8  # the tap survives
    assert {k: card[k] for k in evidence} == evidence  # formation evidence untouched
    added = [h for h in dot.history if h["label"] == "factor_added"]
    assert added == [{"label": "factor_added", "at": (SCAN0 + timedelta(seconds=100)).isoformat(),
                      "definition_md5": CATALYST_MD5, "run_id": 2}]

    # a repeated refresh is idempotent: one dot, one history record
    world.scan(SCAN0 + timedelta(seconds=200))
    dots = [d for d in world.cards.cards[1]["dots"] if d.factor == "catalyst"]
    assert len(dots) == 1 and len([h for h in dots[0].history if h["label"] == "factor_added"]) == 1


def test_the_receipt_names_the_definition_used_and_replays_after_the_def_changed():
    world = World()
    world.scan(SCAN0)
    world.defs = [_with_catalyst()]
    world.scan(SCAN0 + timedelta(seconds=100))
    receipt = world.cards.receipts[-1]
    card = receipt["tap_versions"]["cards"][0]
    assert card["trade_def_md5"] != CATALYST_MD5 and card["definition_md5"] == CATALYST_MD5
    _evaluations, replayed = replay_receipt(world.cards.receipts, clock=session_clock())
    assert replayed and all(r.recomputed == r.published for r in replayed)


def test_a_card_formed_after_the_def_gained_catalyst_carries_it_from_birth():
    world = World(defs=[_with_catalyst()])
    world.scan(SCAN0)
    dot = next(d for d in world.cards.cards[1]["dots"] if d.factor == "catalyst")
    assert dot.na_reason == "DESK_NA" and not [h for h in dot.history if h["label"] == "factor_added"]


def test_a_catalyst_only_edit_refreshes_from_the_formation_def_stored_in_the_receipt():
    world = World()
    world.scan(SCAN0)
    world.defs = [_with_catalyst()]
    world.stage._formation_defs.clear()  # prove the receipt read, not a memo
    outcome = world.scan(SCAN0 + timedelta(seconds=100))
    assert outcome.refreshed == [1] and not outcome.refusals, outcome.refusals


@pytest.mark.parametrize("edit", [
    {"preconditions": [{"expr": "Extension.state == exhausted"}]},
    {"trigger": {"type": "bar_break", "params": {"bars_cleared": 3, "direction": "any"},
                 "confirmation_policy": {"type": "intrabar"}}},
    "stop",
], ids=["preconditions", "trigger", "stop"])
def test_a_formation_field_edit_under_the_same_slug_is_refused_never_adopted(edit):
    world = World()
    world.scan(SCAN0)
    before = dict(world.cards.cards[1])
    if edit == "stop":
        td = sup.anatomy_def(quality_factors=[*sup.ANATOMY_FACTORS, "catalyst"])
        stop = td.model_dump(mode="json", by_alias=True)["stop"]
        stop["placement"]["ref"] = "turn_candle"
        td = sup.anatomy_def(quality_factors=[*sup.ANATOMY_FACTORS, "catalyst"], stop=stop)
    else:
        td = sup.anatomy_def(quality_factors=[*sup.ANATOMY_FACTORS, "catalyst"], **edit)
    field = "stop" if edit == "stop" else next(iter(edit))
    world.defs = [sup.loaded(td, md5=CATALYST_MD5)]
    outcome = world.scan(SCAN0 + timedelta(seconds=100))
    assert outcome.refreshed == []
    assert any("card 1" in r and "no longer loaded" in r and f"{field} changed since formation" in r
               for r in outcome.refusals), outcome.refusals
    assert world.cards.cards[1]["dots"] == before["dots"]  # the new def drove nothing
    assert "catalyst" not in {d.factor for d in world.cards.cards[1]["dots"]}


def test_a_def_gone_from_the_loaded_set_is_still_a_loud_refusal():
    world = World()
    world.scan(SCAN0)
    world.defs = [sup.loaded(sup.anatomy_def(), md5="d" * 32).model_copy(update={"slug": "example-other"})]
    outcome = world.scan(SCAN0 + timedelta(seconds=100))
    assert outcome.refreshed == [] and any("no longer loaded" in r for r in outcome.refusals)
