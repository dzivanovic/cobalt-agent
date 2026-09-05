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

At S1 the moves are manual: Dejan's buttons on the ASET sheet. The
TRIGGERED detector is S2/S4's, and it will call exactly the same
`store.transition()` these buttons call — the state machine does not
learn a second write path when the detector arrives.
"""

from .expire import expire_due, window_end_for
from .models import (
    ALLOWED,
    KEY_EDITABLE,
    STOP_EDITABLE,
    TERMINAL,
    Actor,
    CardState,
    IllegalTransition,
    assert_edge,
    edge_table_markdown,
    is_legal,
)
from .store import BACKFILL_MARKER, CardStateError, CardStore

__all__ = [
    "ALLOWED",
    "BACKFILL_MARKER",
    "Actor",
    "CardState",
    "CardStateError",
    "CardStore",
    "IllegalTransition",
    "KEY_EDITABLE",
    "STOP_EDITABLE",
    "TERMINAL",
    "assert_edge",
    "edge_table_markdown",
    "expire_due",
    "is_legal",
    "window_end_for",
]
