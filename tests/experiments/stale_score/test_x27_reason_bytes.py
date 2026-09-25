"""X27 (v2 §7, before S1; X4's precondition): for a STALE card the stage's
stored `score_suppressed` text and `replay_receipt`'s recompute are
byte-identical (time format, dot-reason order). At the base the stale
sentence does not exist yet, so this records whether the two sides go
through one text path today; STEP-2 test (xii) re-proves it with the
sentence."""

from __future__ import annotations

from cobalt.radar.evaluate import replay_receipt
from cobalt.session import session_clock

from stale_support import SCAN0, bars_before, stale_as_of


def test_x27_stage_and_replay_suppression_text_are_byte_identical_on_a_stale_card():
    from test_radar_evaluate import World

    world = World()
    world.scan(SCAN0)
    kept = bars_before(SCAN0)
    world.radar.bars["FTFT"] = list(kept)
    stale_at = stale_as_of(kept)
    outcome = world.scan(stale_at)
    ev = outcome.evaluations[0]
    card = world.cards.cards[1]
    _, replayed = replay_receipt(list(world.cards.receipts), clock=session_clock())
    stage_text = card["score_suppressed"]
    replay_text = replayed[0].recomputed["score_suppressed"]
    same = stage_text is not None and stage_text.encode() == replay_text.encode()
    print(f"X27: evaluation={ev.evaluation} note={ev.note!r} cards={len(replayed)} "
          f"stage={stage_text!r} replay={replay_text!r} byte_identical={same} "
          f"published_equals_recomputed={replayed[0].published == replayed[0].recomputed}")
    assert ev.evaluation == "input_stale"
    assert same and replayed[0].published == replayed[0].recomputed
