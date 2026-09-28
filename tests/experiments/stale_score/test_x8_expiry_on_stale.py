"""X8 (v2 §7, before S1): on stale bars the deadline still expires on the
wall clock, a stored bar through the stop still expires `stop_before_arm`,
and a stale scan does not expire `avoid` (the card's own side is
`input_stale`, never `avoided`)."""

from __future__ import annotations

from datetime import timedelta
from decimal import Decimal

from cobalt.cards.expire import radar_expiry
from cobalt.cards.models import CardState

from stale_support import SCAN0, bars_before, evaluate, member, stale_as_of


def test_x8_expiry_causes_on_a_stale_scan():
    kept = bars_before(SCAN0)
    at = stale_as_of(kept)
    ev = evaluate(member(at, kept))
    sides = {side: out.evaluation for side, out in ev.by_side.items()}
    far = at + timedelta(hours=1)
    stop_above = max(b.high for b in kept) + Decimal(1)
    touching = [b for b in kept if b.high >= kept[-1].high][:1]

    def expire(**kw):
        base = dict(state=CardState.WATCH, now=at, expires_at=far, avoided=sides["short"] == "avoided",
                    direction="short", stop=stop_above, bars_after_formation=[])
        base.update(kw)
        out = radar_expiry(**base)
        return None if out is None else out.cause

    stale_scan = expire()
    deadline = expire(now=far + timedelta(seconds=1))
    stop = expire(stop=kept[-1].high, bars_after_formation=touching)
    print(f"X8: by_side={sides} stale_scan_cause={stale_scan} past_deadline_cause={deadline} "
          f"stored_bar_through_stop_cause={stop}")
    assert set(sides.values()) == {"input_stale"}
    assert stale_scan is None and deadline == "deadline" and stop == "stop_before_arm"
