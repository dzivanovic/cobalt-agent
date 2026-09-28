"""X7 (v2 §7, before S1): the ladder with a stale (NULL-score) WATCH card —
a promoted stale WATCH card is still promoted; the pinned order does not
change; a NULL sinks below every scored WATCH card (R37's existing rule)."""

from __future__ import annotations

from datetime import datetime, timezone

from cobalt.cards.models import CardState
from cobalt.cards.radar import LadderEntry, ladder_order

AT = datetime(2026, 1, 6, 16, 30, tzinfo=timezone.utc)


def _entry(card_id, state, score, pool, promoted=False):
    return LadderEntry(card_id=card_id, state=state, card_score=score, pool_position=pool, ticker=f"T{card_id}",
                       promoted_at=AT if promoted else None, state_at=AT)


def test_x7_promoted_stale_watch_card_stays_promoted_and_pinned_order_is_unchanged():
    pinned = [_entry(1, CardState.ARMED, 40, 3), _entry(2, CardState.FILLED, None, 1)]
    scored = [_entry(3, CardState.WATCH, 80, 5), _entry(4, CardState.WATCH, 55, 2)]
    fresh = ladder_order([*pinned, *scored, _entry(5, CardState.WATCH, 90, 4, promoted=True)])
    stale = ladder_order([*pinned, *scored, _entry(5, CardState.WATCH, None, 4, promoted=True)])
    unpromoted = ladder_order([*pinned, *scored, _entry(5, CardState.WATCH, None, 4)])
    pin = lambda order: [p.card_id for p in order.active if p.pinned]  # noqa: E731
    promoted = [p.card_id for p in stale.active if p.promoted]
    print(f"X7: fresh_active={[p.card_id for p in fresh.active]} stale_active={[p.card_id for p in stale.active]} "
          f"unpromoted_active={[p.card_id for p in unpromoted.active]} promoted={promoted} "
          f"pinned_fresh={pin(fresh)} pinned_stale={pin(stale)} "
          f"null_chip={[p.rank_chip for p in unpromoted.active if p.card_id == 5]}")
    assert promoted == [5] and pin(stale) == pin(fresh)
    assert [p.card_id for p in unpromoted.active][-1] == 5  # a NULL WATCH sinks below every scored one
