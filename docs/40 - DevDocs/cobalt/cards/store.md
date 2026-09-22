# `src/cobalt/cards/store.py`

S2-P1 includes `account_mode` in open-card reads for the ASET surface.

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

---

## 2026-09-16 — S2-P2 radar cards (STEP-4/6)

**The sized-card ARM invariant lives in `transition()` (Astra R1-6).** The locked `SELECT … FOR UPDATE` now also reads `grade`, `risk_budget`, `shares` and `used_risk`. Any `-> ARMED` on a card with one of them NULL is refused by name ("UNSIZED — tap a key first"). This covers every caller, including the sheet's `/card/{id}/move`, not just the radar tap route. `transition()` also accepts `before_commit` so the S5 stage's market_reset gate reaches an expiry.

**Unsized stop edit.** `record_stop_edit` locks the row. On an unsized radar WATCH card (`risk_budget` NULL) it side-checks through `aset.engine.stop_distance` and updates `stop` and `per_share_risk` only; the sizing columns stay NULL. The old path divided by NULL. Sized and FILLED edits are unchanged.

**One creation path for an unsized radar card (Astra R1-7).** `create_radar_card(spec, *, now, before_commit)` does, in one transaction:
1. resolve the account mode;
2. `INSERT … ON CONFLICT (pool_member_id, trade_def_slug, direction) WHERE origin='radar' AND state IN (…) DO NOTHING RETURNING id`. `None` means the database already holds the open card; the partial unique index decides, not a check-then-insert (R1-14);
3. `create_state` genesis, with evidence carrying run id, formation bar ts and atoms;
4. the `card_dots` rows.

**Other radar methods:**
- `refresh_radar_card(update)` locks the row and writes proximity, last price, health and the seam id. Dots upsert with engine fields and history only, never `trader_grade`/`tapped_at`. When a tap landed after the stage read the card (`tap_version`), conviction/score/key are left to the tap's own recompute and the next scan reconciles.
- `expire_radar_card` goes through `transition(EXPIRED)`. A state that moved under it (FILLED) is logged, not raised.
- `write_receipt`, `receipts_chain(receipt_id)` (oldest first) and `receipts_for_day(pool_key, day)`.
- Reads: `open_radar_cards()` (with dots and taps), `formation_consumed(ticker, slug, direction, formed_at)`, `radar_card(id)`.

**Taps (STEP-6), each one locked transaction:**
- `tap_key(card_id, sizing)`: WATCH only (`KEY_EDITABLE`). Refuses when entry/stop moved since the size was computed. Writes tapped/sized grade, sheet, risk budget, shares, used risk and snap notice.
- `tap_dot(card_id, factor, grade, *, bands, enabled)`: appends a `card_dot_taps` row carrying `engine_grade_at_tap`, sets the trader grade, and recomputes conviction/suppression/card_score (from the stored proximity) and the proposed key. Refused on a terminal card.
- `set_promoted(card_id, bool)`: promote needs WATCH and clears any other promoted card in the same transaction; the `aset_sizings_one_promoted_radar_card` index backs it across rows.

## 2026-09-16 — S2-P2 chunk C reads (STEP-8/10/11)
All three are plain SELECTs: no schema init, no write guard.
- `radar_board_cards(trade_date)`: the `/radar` ladder's one read. Every `"user".radar_cards_v` row that is open, plus terminal rows whose `state_at` falls on `trade_date` in ET, each with its `dots` (`_dots_for`).
- `shadow_agreement(since)`: `"user".shadow_agreement_v` rows (factor × ET trading day, with every |tap − engine| delta), optionally from `since`.
- `receipt_for_run(run_id)`: the one receipt id of a run, `None` when there is none, and a loud refusal when there are two.

---

## 2026-09-17 — S2-P4 (F3 picks, rulings R2 + Astra R1-4/R1-5/R1-7)

**`fill()` returns a `FillResult`, not a bare id list.** It holds
`transition_ids` (same order as before: three on a one-click WATCH fill,
one on a strict fill), `pick_recorded`, `pick_id` and `pick_error`.

**One transaction on every route.** Before this change the strict route
(radar cards, and manual cards one edge away) called `transition()`
unwrapped, and that call committed on its own. Now `fill()` opens one USER
connection for every route and passes it to every `transition()` hop.
After the FILLED hop, still inside that transaction, `_record_pick` runs:

1. `SAVEPOINT pick`
2. `picks.record_pick(conn, card_id, <FILLED transition id>, ts)`
3. on success `RELEASE SAVEPOINT pick`. On any `Exception`:
   `ROLLBACK TO SAVEPOINT pick`, then one `logger.error` naming the card
   and the error class. The fill continues and commits.

Only `Exception` is caught, so an interrupt still aborts the whole fill. If
the savepoint rollback itself fails, or the commit fails, everything rolls
back and the error propagates: a failed fill never returns a result.

**Log destination.** The `logger.error` line goes to loguru's default
stderr sink. For the sheet process (`com.cobalt.aset`) that is
`/Users/cobalt/cobalt/logs/aset.err` (the plist's `StandardErrorPath`,
rotated by `ops/start_aset.sh`). It is a log line, not a persisted job row.
The persisted evidence of the gap is `cobalt cards picks` reporting MISSING.

**`filled_with_picks(day)`** backs `cobalt cards picks`. It returns every
`card_transitions` row with `to_state = 'FILLED'` whose `at` falls on that
ET date, joined to the card and left-joined to `picks` on `transition_id`.

**2026-09-21 — setups one build STEP-1.** `tap_dot` refuses the factor `assumed_formation`. The refusal sits beside the no-such-dot refusal, before the INSERT. It raises `CardStateError("REFUSED card <id>: assumed_formation is not graded on a card — an assumed default is ruled on the settings surface")`. No tap row is written. The dot's `trader_grade` and the card's conviction, score, suppression and proposed key are not touched. The route turns the error into `409` with that message. Tapping any other dot recomputes as before, and `suppression()` still names `assumed_formation`, so `card_score` stays null (R2-2 = B, X8's tap half).
