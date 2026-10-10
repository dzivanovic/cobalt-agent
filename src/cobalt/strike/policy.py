"""The card's confirmation policy over i1 bars — pure (S4-P1 C1).

    crossed(policy, direction, entry, bars, since, now) -> Cross | Unwatchable | None

Bars are stamped at their START, UTC (`archiver/collector.py`). Only a bar
whose start is at or after `since` counts — no floor: a bar that started
before `since` never counts, even when it touched.

* `intrabar` — the first bar whose high >= entry (long) / low <= entry
  (short), the forming bar included. THE SAME RULE as the F12 replay's
  trigger (`replay/cards.py` `counterfactual`, `_touches_entry`): one formula
  (L3); only the start differs (replay: `created_at`; the detector: the
  ARMED `at`; the MISSED sweep: `created_at`).
* `close_through` — the first COMPLETED bar (`ts + 1 min <= now`, as
  `radar/poller.py`) closing beyond entry (close > entry long, < short).
* `two_bar` — two consecutive completed closes beyond.
* `acceptance` — `bars` consecutive completed closes beyond, or `time`
  ("<n> min", the def's own duration form) held beyond as n consecutive
  completed i1 closes; both given → the longer.

`Cross.cross_price`: intrabar → the bar's high (long) / low (short), the
price that reached entry; the close-based policies → the confirming close.
`Cross.bar_ts` is the bar that completed the confirmation.

A `SequenceTrigger`, a missing policy, or an acceptance with nothing to
count → `Unwatchable(reason)`, never a guess (DECISION D5).
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional, Union

from cobalt.archiver.models import Bar
from cobalt.replay.cards import _touches_entry
from cobalt.taxonomy.trade_def import ConfirmationPolicy, ConfirmationPolicyType, SequenceTrigger

MINUTE = timedelta(minutes=1)
_DURATION = re.compile(r"^(\d+) min$")


@dataclass(frozen=True)
class Cross:
    policy: str
    bar_ts: datetime
    bar_close_at: datetime
    cross_price: Decimal


@dataclass(frozen=True)
class Unwatchable:
    reason: str


def policy_of(trigger) -> Union[ConfirmationPolicy, Unwatchable]:
    """The trigger's policy, or why there is none to watch."""
    if isinstance(trigger, SequenceTrigger):
        return Unwatchable(f"sequence trigger ({len(trigger.steps)} steps) — price-cross only (Charter F9)")
    policy = getattr(trigger, "confirmation_policy", None)
    if policy is None:
        return Unwatchable(f"{getattr(trigger, 'type', '?')} trigger carries no confirmation_policy")
    return policy


def _beyond(close: Decimal, direction: str, entry: Decimal) -> bool:
    return close > entry if direction == "long" else close < entry


def _run_of(bars: Sequence[Bar], need: int, direction: str, entry: Decimal) -> Optional[Bar]:
    """The bar that completes the first run of `need` consecutive closes beyond."""
    run = 0
    for b in bars:
        run = run + 1 if _beyond(b.close, direction, entry) else 0
        if run >= need:
            return b
    return None


def _acceptance_bars(policy: ConfirmationPolicy) -> Union[int, Unwatchable]:
    counts: list[int] = []
    if policy.bars is not None:
        counts.append(int(policy.bars))
    if policy.time is not None:
        m = _DURATION.match(policy.time.strip())
        if m is None:
            return Unwatchable(f"acceptance time {policy.time!r} is not '<n> min'")
        counts.append(int(m.group(1)))
    if not counts or max(counts) < 1:
        return Unwatchable("acceptance names neither bars nor time")
    return max(counts)


def crossed(
    policy: Optional[ConfirmationPolicy],
    direction: str,
    entry: Decimal,
    bars: Sequence[Bar],
    since: datetime,
    now: datetime,
) -> Union[Cross, Unwatchable, None]:
    if policy is None:
        return Unwatchable("no confirmation policy")
    if direction not in ("long", "short"):
        return Unwatchable(f"direction {direction!r} is neither long nor short")
    eligible = sorted((b for b in bars if b.ts >= since), key=lambda b: b.ts)
    kind = policy.type

    if kind is ConfirmationPolicyType.INTRABAR:
        hit = next((b for b in eligible if _touches_entry(b, direction, entry)), None)
        if hit is None:
            return None
        return Cross(kind.value, hit.ts, hit.ts + MINUTE, hit.high if direction == "long" else hit.low)

    completed = [b for b in eligible if b.ts + MINUTE <= now]
    if kind is ConfirmationPolicyType.CLOSE_THROUGH:
        need: Union[int, Unwatchable] = 1
    elif kind is ConfirmationPolicyType.TWO_BAR:
        need = 2
    elif kind is ConfirmationPolicyType.ACCEPTANCE:
        need = _acceptance_bars(policy)
    else:
        return Unwatchable(f"confirmation policy {kind!r} is not watched")
    if isinstance(need, Unwatchable):
        return need
    hit = _run_of(completed, need, direction, entry)
    if hit is None:
        return None
    return Cross(kind.value, hit.ts, hit.ts + MINUTE, hit.close)


__all__ = ["Cross", "Unwatchable", "crossed", "policy_of"]
