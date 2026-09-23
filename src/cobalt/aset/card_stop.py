"""ONE card-stop function for the sheet and for voice (FINAL [F-06], L3).

`set_card_stop(card_id, to_stop)` is the body of the `/card/{id}/stop`
route, extracted unchanged: the dev-entry guard `_check_entry_allowed`
(IMPORTED from `aset/web.py`, never moved or copied), the open-card
lookup, the `Decimal` parse, and `CardStore.record_stop_edit` — which gates
itself (`market_reset`, `STOP_EDITABLE`) and recomputes shares / per-share
risk through the EXISTING engine (FINAL [F-26]); this function adds no
arithmetic. The route renders its result exactly as before (pinned by
`tests/cobalt/test_voice_card_stop.py`); the voice act calls the same
function after his confirmation.

It lives in its own module because `aset/web.py` includes the voice router
and the voice tool calls this — the import of `web` is deferred to call
time so neither module imports the other at load.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from cobalt.cards import CardStateError


@dataclass(frozen=True)
class StopEdit:
    card_id: int
    from_stop: Decimal
    to_stop: Decimal
    #: The expert's write reference: the `card_stop_edits` row id.
    stop_edit_id: int


def set_card_stop(card_id: int, to_stop) -> StopEdit:
    """Raises what the route renders: `DevEntryRefused`, `CardStateError`,
    `InvalidOperation`, `SessionBlocked` (and anything else, named)."""
    from cobalt.aset import web as _web

    _web._check_entry_allowed()
    store = _web.CardStore()
    store.ensure_schema()
    before = store.open_cards()
    current = next((c for c in before if c["id"] == card_id), None)
    if current is None:
        raise CardStateError(f"card {card_id} is not open — its stop is settled.")
    new_stop = Decimal(to_stop)
    edit_id = store.record_stop_edit(card_id, from_stop=current["stop"], to_stop=new_stop)
    return StopEdit(card_id=card_id, from_stop=current["stop"], to_stop=new_stop, stop_edit_id=edit_id)


__all__ = ["StopEdit", "set_card_stop"]
