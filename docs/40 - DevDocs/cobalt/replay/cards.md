# `src/cobalt/replay/cards.py`

F12 (S2-P4 STEP-5, R4 as amended by R1-9/R1-10/R1-11/R1-12/R2-4/R3-2). This
module replays the day's unfilled cards over stored i1 bars. For each miss
it records the gate that excluded it and one counterfactual R, with every
input stored.

## `counterfactual(...)` — the ONE formula (added 2026-09-18, chunk E2)

`counterfactual(todays, *, subject, direction, entry, stop_at, start_at,
window_end, session_close) -> CfOutcome` holds steps 2–5 below and is
called by BOTH `replay_card` and `replay/formations.py`. A card and a
formation differ in their gates and their receipt, never in their
arithmetic (L3) — there is one trigger search, one gap-through fill rule,
one stop-wins-on-tie walk and one rounding in the package.

`stop_at(trigger_ts)` is how the two differ where they must: a card walks
its own `card_stop_edits` history back to the trigger (R1-11), a formation
hands over S2-P2's structural stop unchanged. `CfOutcome.status` is `ok`
(with a `Counterfactual`), `no_trigger` or `input_stale`; `subject` is the
string every refusal names (`card 302`, `formation MU example-… @ …`).

`bar_json(bar)` is public for the same reason: a receipt bar has one
spelling here.

## The pure core
`replay_card(card, bars, *, trade_date, window, session_close, positions)`
reads no clock, database or config.

1. **Coverage (R1-12).** Bars are filtered to the ET trade date (duplicate
   timestamps refuse). The card is covered only when a bar starts at or
   before `created_at` and a bar's minute ends at or after the close.
   Otherwise the result is `input_stale` and no row is written. Interior
   gaps are recorded (`max_gap_min`) but not gated, because a minute with no
   trade has no bar.
2. **Trigger.** The first bar starting at or after `created_at` with
   `high >= entry` (long) or `low <= entry` (short). `fill_price` is the
   planned entry, or the bar's open when it opened beyond the entry. No
   trigger means `no_trigger`.
3. **Horizon.** `W = min(resolved window end, session close)`. `H = W` if
   `trigger_ts <= W`, else the session close. A bar is eligible only if
   `bar_start + 1 minute <= H`. A trigger with no eligible bar is
   `input_stale`.
4. **Exit.** Walk the eligible bars from the trigger bar. The first stop
   touch exits at the stop; a touch on the trigger bar counts, so a
   same-bar tie goes to the stop. Otherwise the exit is the close of the
   last eligible bar (`horizon_end`).
5. **R.** `cf_r = (exit − fill_price) / |planned entry − stop| × ±1`,
   rounded half-up to 4 dp once. A gapped long 100/99 filled at 102 and
   stopped is −3R. `mfe_r` is the best favourable excursion through the
   exit bar. It is a bar-level observation, never a second R.
6. **Gates**, first match in `GATE_ORDER`:
   - `rule_10`: at least two OTHER positions open at `trigger_ts`. This is
     the two-open-position proxy; the rule's stop-at-card-level exemption
     is recorded `unavailable`.
   - `window`: `trigger_ts > W`.
   - state at `trigger_ts` via `STATE_GATE`. That map is exhaustive over
     `CardState` (tested): WATCH/MISSED → `unarmed`, PASSED → `passed`,
     ARMED/TRIGGERED → `not_filled`, EXPIRED → `window`, FILLED/CLOSED →
     refused.

   `gate_detail` records every gate, plus `trade_count_band: "unset"`,
   which is never an `excluded_by`.

The stop is read **as of the trigger** (`stop_as_of`): the current stop,
walked back through every later `card_stop_edits` row. State comes from
`state_at`, ordered by `(at, id)`. If tied rows have no id, the order is
unknowable and the call refuses.

## The receipt (R1-8, L57)
`receipt = {"inputs", "outputs"}`. The inputs hold the formula version,
card, transitions, stop edits, window resolution, session close, positions,
the eligibility rule and the consumed bars. The consumed bars are the bar
proving start coverage, every searched bar, and the bar proving close
coverage. `inputs_sha256 = sha256_json(inputs)`.
`replay_from_receipt(receipt)` rebuilds every value from the inputs alone
and returns an identical `MissRow` (tested on the real fixture day).
`bars_watermark` is the newest consumed bar.

## Resolution helpers
- `resolve_window(ref, day)` wraps `cards.expire.window_end_for`, the one
  public resolver. Manual cards carry no ref, so it resolves to the session
  close.
- `session_close_for(day)` gives the ACTUAL RTH close from the session
  clock, early-close aware.

## `MissedStore` (USER side)
- `candidates(day)`: cards created that ET day
  (`created_at AT TIME ZONE 'America/New_York'`) with no FILLED transition,
  plus their transitions and stop edits.
- `positions(day)`: cards FILLED by the day and not CLOSED before it,
  overnight holds included.
- `radar_cards(day)` (2026-09-18, chunk E2): every radar-origin
  `aset_sizings` row CREATED that ET day, as `RadarCardRef`s, for the
  formation step's suppression gate. Created that day, not "open now": by
  21:10 a card that formed at 10:00 may have EXPIRED, and its formation is
  still not a separate miss because the card path already replayed it.
- `current(day, kind)`: the CURRENT rows. The miss line publishes only
  these.
- `reconcile(run_id, trade_date, kind, rows)`: one serialized transaction
  (advisory lock on the day) in the ruled order. (1) Retire every replaced
  or dropped predecessor (`is_current=false`, `retired_by_run_id`).
  (2) Insert the replacements with `run_seq = predecessor + 1`. (3) Link
  `superseded_by`. A subject whose `inputs_sha256` and `excluded_by` are
  unchanged is left alone, so an identical rerun writes nothing.
  `before_commit(stage)` is a test seam.

No connection here writes the system schema. Bars, movers and membership are
read by SYSTEM stores and passed in as values.

## Tests
`tests/cobalt/test_replay_cards.py`, on the hub-cut fixtures. The fixture
day is an EDT day shifted to 2026-02-10, so tests pass its real 20:00 UTC
close explicitly.
