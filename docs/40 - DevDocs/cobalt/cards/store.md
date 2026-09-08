# `src/cobalt/cards/store.py`

## What it does
Persists card state: `aset_sizings.state`/`state_at` plus the
`card_transitions` ledger and the `card_stop_edits` side-table.
Database from `COBALT_ENV` via `env.resolve_db_name()` (RULING 7/9);
`db_name` is the test/tooling seam only.

## The one invariant
`state` and its ledger row are written in **one database transaction or
neither**. A card whose column says `ARMED` with no `ARMED` row in the
ledger is a card whose DRC count is a guess.

## The order of gates, and why it is the order
1. **F1 session guard** — `assert_writable(...)` first. A write refused
   in `market_reset` must leave *no trace of having been attempted*.
   Tested by asserting that an **illegal** move inside `market_reset`
   raises `SessionBlocked`, not `IllegalTransition` — proof that nothing
   downstream ran.
2. **Edge legality** — checked against the state re-read under
   `SELECT ... FOR UPDATE`, not against whatever the caller last saw.
3. **Reason requirement** — `MISSED` and `disarm` carry one or they do
   not happen.
4. The two writes, atomically.

## Why `FOR UPDATE`
The sheet and the 16:05 expiry job can touch the same card in the same
second. Without the row lock both would read `WATCH`, both would find
their edge legal, and the ledger would record two different next states
for one card. With it, the second re-reads `ARMED` and is refused by
name — the correct answer.

## Stop edits (decision 11)
`record_stop_edit()` writes **no transition row** — a stop edit is not a
state change. It lands in `card_stop_edits`, and the *next* transition
folds every unfolded edit into its `evidence` JSON under `stop_edits`,
then marks them `folded_into` so one edit is never counted twice.
Refused unless the card is in `STOP_EDITABLE` (`WATCH`, `FILLED`).

## Backfill
`backfill(today=...)` classifies every state-less card: `status='FILLED'`
-> `FILLED`; otherwise trade date `< today` -> `EXPIRED`, `== today` ->
`WATCH`. Each gets **one genesis row** marked
`evidence->>'backfill' = 'S1-P2'`.

**A FILLED row is not given a synthetic `WATCH -> ... -> FILLED`
history.** Inventing four transitions that never happened would put
fabricated rows in the ledger the DRC counts. One genesis row landing
directly on `FILLED` is the honest shape: Cobalt knows where the card
ended and does not know how it got there.

## Key methods
`ensure_schema` · `state_of` · `history` · `open_cards` ·
`state_distribution` · `transition` · `create_state` ·
`record_stop_edit` · `backfill`

## Who calls it
`aset/store.py` (`save` creates the genesis row in its own transaction;
`mark_filled` is now a `TRIGGERED -> FILLED` transition), `aset/web.py`
(the button routes), `cards/expire.py`, `cards/cli.py`.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

Declares `SIDE = Side.USER` (ADR-0008 D2 — the side is chosen PER STORE, never per process).
the card's own history sits where the card sits.

`_connect()` passes it to the factory; `ensure_schema()` asserts the two-layer schemas exist before running its own DDL, naming `cobalt db migrate` if they do not.
