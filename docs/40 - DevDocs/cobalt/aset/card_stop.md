# `src/cobalt/aset/card_stop.py`

## What it does
`set_card_stop(card_id, to_stop)` — the ONE card-stop function, shared by
the sheet's `/card/{id}/stop` route and the voice act (FINAL [F-06], L3).
It is the route's former body, extracted unchanged: the dev-entry guard
`_check_entry_allowed` (imported from `aset/web.py`, never moved or
copied), the open-card lookup, the `Decimal` parse, and
`CardStore.record_stop_edit`, which gates itself (`market_reset`,
`STOP_EDITABLE`) and recomputes shares / per-share risk through the
EXISTING engine (FINAL [F-26]). Returns a `StopEdit` whose
`stop_edit_id` (the `card_stop_edits` row) is voice's write reference.

Since fix r2 (RUN-2) it takes a keyword `expect_from_stop`, passed only by
the voice act: when the stop it reads differs from the stop the confirmed
read-back was computed from, it raises `StopMoved` (a `CardStateError`
carrying the fresh card row) BEFORE any stop edit is recorded. The route
never passes it, so its behaviour and rendered output are unchanged.

## Why its own module
`aset/web.py` includes the voice router and the voice tool calls this;
`web` is imported at call time, so neither module imports the other at
load. It reads `CardStore` from `aset.web`'s namespace — the class the
sheet itself uses.

## The pin
`tests/cobalt/test_voice_card_stop.py` holds the route's output for an
open card, a card that is not open, a bad decimal, the dev refusal and a
store refusal, captured on the base as literal strings — byte-identical
after the extraction.
