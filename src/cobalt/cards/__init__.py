"""F7 card state machine — a card is a state, and a state is a ledger row.

Charter §3 F7 (M5-M8): "WATCH -> ARMED -> TRIGGERED -> FILLED -> CLOSED
/ PASSED / EXPIRED / MISSED, every transition persisted with evidence;
trigger while unarmed = MISSED, counted not hidden."

Four pieces, one law each:

* `models.py` — the EDGE TABLE, in one place, as data. Illegal edges are
  refused by name, never coerced to the nearest legal state.
* `store.py`  — the card's `state` and its `card_transitions` row are
  written in ONE transaction or neither. The F1 session guard runs
  BEFORE any state logic, so a refused write leaves no trace.
* `expire.py` — a window that closed is an ACT with an actor and
  evidence, not a predicate evaluated on read.
* `cli.py`    — `cobalt cards state/history/backfill/expire/edges`.

ONE-CLICK FILL (S1-P3, CTO review). `store.fill()` is the single entry
point to FILLED. On a card whose `origin` is `manual` it walks the rest
of the legal route itself — inserting the ARMED/TRIGGERED rows Cobalt
never watched happen, marked `actor=cobalt`, evidence
`{"auto": "manual_fill"}`, at the fill's own timestamp. The route comes
from `fill_path()`, a walk of the SAME edge table, so the shortcut adds
no edge; a `radar` card gets no shortcut at all.

At S1 the moves are manual: Dejan's buttons on the ASET sheet. The
TRIGGERED detector is S2/S4's, and it will call exactly the same
`store.transition()` these buttons call — the state machine does not
learn a second write path when the detector arrives.
"""

from .expire import expire_due, window_end_for
from .models import (
    ALLOWED,
    FILL_TARGET,
    KEY_EDITABLE,
    STOP_EDITABLE,
    TERMINAL,
    Actor,
    CardState,
    IllegalTransition,
    Origin,
    assert_edge,
    edge_table_markdown,
    fill_path,
    is_legal,
)
from .store import AUTO_FILL_EVIDENCE, BACKFILL_MARKER, CardStateError, CardStore

__all__ = [
    "ALLOWED",
    "AUTO_FILL_EVIDENCE",
    "BACKFILL_MARKER",
    "FILL_TARGET",
    "Actor",
    "CardState",
    "CardStateError",
    "CardStore",
    "IllegalTransition",
    "KEY_EDITABLE",
    "Origin",
    "STOP_EDITABLE",
    "TERMINAL",
    "assert_edge",
    "edge_table_markdown",
    "expire_due",
    "fill_path",
    "is_legal",
    "window_end_for",
]
