# ADR-0010 — Missed corpus + counterfactual R + picks

Date: 2026-09-17
Status: Accepted (build; hub verification and the P4 deploy pending)
Decided: Dejan, 2026-09-15. This ADR records plan-s2-p4 rulings R1–R6 (R7 is the builder seat) and the Astra round 1–3 amendments folded into that plan. It decides nothing new.
Plan: `docs/40 - DevDocs/plans/plan-s2-p4-2026-09-15.md`
Relates to:
- ADR-0008: tenancy. `picks`/`missed` are USER tables, `movers_daily` is SYSTEM, and join J3 is `"user".missed.pool_member_id → system.radar_membership(id)`.
- ADR-0004: L28, the one vault write path.

## Context

The S2 block of the sprint ladder owes three records that the Friday review
needs before rule 10 can be loosened on evidence rather than feel:

- **F3:** Dejan's pick next to Cobalt's rank, for every card he takes.
- **F12:** the setups that fired but were not taken, with the gate that stopped each and what the trade would have made (counterfactual R).
- **F13:** what moved that day that the pool never saw.

The inputs already existed and were discarded (plan §1 F2, F5, F6). So each of these records has to be a stored, replayable number, never a derived one without its inputs (L57).

## Decision

### 1. Picks (F3, R2)

- A **pick** is any card reaching FILLED, manual now and radar later. `CardStore.fill` writes one `"user".picks` row on the FILLED hop through `record_pick`. The write happens inside the fill's single USER transaction, under `SAVEPOINT pick`.
- A pick-insert failure rolls back only the savepoint. The fill commits and `FillResult.pick_recorded = false`. The sheet shows a red "pick not recorded" banner, and `cobalt cards picks` reports the gap as MISSING (exit 1).
- The row snapshots, at pick time:
  - the admitted pool episode open at that instant: `pool_member_id`, `pool_rank`, `pool_size`, `rank_metric`, `rank_value`, scan id and time. A ticker with no open episode gets `not_in_pool = true`.
  - the card-score rank among open radar cards **plus the picked card itself**. Ties use competition ranking, and `focus_top4` is rank ≤ 4.
- `pool_basis` / `score_basis` name every null (`unavailable: <reason>`). `score_inputs` stores the cohort, so the rank replays.
- "Every FILLED card that day" means FILLED **transitions** on that ET date. It never means current state, creation date or `filled_at` (Astra R1-7).
- `system.radar_membership` gains `rank_metric` and `rank_value`, written on RETAIN/EXCLUDE/INSERT and carried on HOLD. There is **no backfill**: pre-deploy rows stay NULL and render `—` (R1).

### 2. The missed corpus (F12, R4) — one formula

Candidates are `aset_sizings` created that ET day whose `card_transitions` never reached FILLED. Bars are `system.bars` i1 for the ticker.

**Trigger:**
- The trigger is the first i1 bar starting at or after `created_at` with `high ≥ entry` (long) or `low ≤ entry` (short).
- `fill_price` = the planned entry, or that bar's **open** when it opened beyond the entry (gap-through).
- No trigger → no row.

**Exit:**
- Bars are walked from the trigger bar. The stop is touched when `low ≤ stop` (long) or `high ≥ stop` (short), and a touch on the trigger bar itself counts, so a same-bar tie goes to the stop.
- On the first touch, `exit_price = stop` and `exit_reason = stop`.
- Otherwise the exit is the close of the last eligible bar, with `exit_reason = horizon_end`.

**Counterfactual R:**

```
cf_r = (exit_price − fill_price) / |planned_entry − stop| × (+1 long, −1 short)
```

- It is rounded half-up to 4 dp, once. The numerator uses the actual counterfactual fill and the denominator the planned risk (Astra R1-9). A long planned 100 / stop 99, gap-filled at 102 and stopped, is **−3R**, not −1R.
- `stop` is read **as of the trigger**, from the stop-edit history (R1-11).
- `mfe_r` is the best favourable excursion from `fill_price` through the exit bar, in the same units. It is a bar-level **observation**, never a second R: the order of high and low inside one OHLC bar is unknowable.
- `FORMULA_VERSION = s2p4.cf_r.1` is stored on every row. A formula change is a new version, never a silent recompute.

### 3. Horizon rule (R4, Astra R1-10 / R2-4 / R3-2)

```
W = min(resolved window end, actual session close for the trade date)
H = W                    if trigger_ts ≤ W
H = actual session close otherwise (the after-window trigger still gets a horizon)
```

- The window text is resolved through the public `cards/expire.py` resolver. An explicit time is never allowed past an early close.
- i1 bars are stamped at bar **start**, so a bar is eligible only if `bar_start + 1 minute ≤ H`.
- A trigger that leaves no eligible completed bar writes no row. The same applies to bars that do not cover `created_at` through the close: both are counted `input_stale`, loud, never a fake R (Astra R1-12).

### 4. Gate order (R4, Astra R1-11)

`excluded_by` is the **first** match, in this fixed order:

1. **`rule_10`**: ≥ 2 other cards FILLED and not CLOSED at `trigger_ts`. This is labelled the two-open-position **proxy** for rule 10. The rule's stop-at-card-level exemption is not computed and is recorded `unavailable`, never treated as passing.
2. **`window`**: `trigger_ts > W`.
3. **State at `trigger_ts`**, from `card_transitions` ordered by `(at, id)`:
   - WATCH or MISSED → `unarmed`
   - PASSED → `passed`
   - ARMED or TRIGGERED → `not_filled`
   - EXPIRED → `window`
   - FILLED or CLOSED cannot occur for a candidate and refuse loud.

`gate_detail` records every gate's evaluation. `trade_count_band` is recorded `unset` while its tunables are null, and it is **never** an `excluded_by` value (plan §8 item 2).

**Movers (F13, R5)** are benchmarked, not gated:
- The unfiltered top `radar.benchmark.top_n` per side are fetched from the gainers/losers exports and stored in `system.movers_daily`. Rows are never deleted: `active = false` on a rerun.
- Movers with `|change_pct| ≥ min_move_pct` are compared against that day's `radar_membership` episodes:
  - any admitted episode → in play, no row;
  - only never-admitted episodes → `excluded_by` = the most recent one's value (`config_cap` / `not_equity` / `screen_inactive` / `manual`);
  - no episode → `not_in_any_source`.
- A mover row has no cf_r: there is no trigger without a trade_def.
- `radar.benchmark` lives in `"user".trader_settings`, applied by Dejan (L53). It is not a `SETTING_KEYS` member.
- [amended 2026-09-24, cto-2026-09-23.md R113] A fetched mover whose source i1 bars do not span the session is archived-partial: its bars are kept, it stays bars_archived = false, the replay's job row names it (archive_partial, by side) and the S2 smoke's K9 is green only with that marker; zero bars on the day stays incomplete, a fetch failure stays a failure.

**Formations** reuse S2-P2's evaluator once it ships. Until then the job logs exactly `trade_def replay: not available until S2-P2` and writes no rows. A present-but-incompatible P2 fails loud (Astra R1-21).

### 5. Receipts and versioning (L57, Astra R1-8 / R2-1 / R3-1)

- Every `"user".missed` row carries an immutable `receipt` (JSONB) and its `inputs_sha256`. The receipt holds the consumed OHLC bars, entry/stop as evaluated (with stop-edit history), window text and resolution, horizon, state and position history, the benchmark/settings inputs and the cutoff policy.
- `replay_from_receipt` recomputes every stored number from the receipt alone.
- A rerun never overwrites a receipt. One serialized USER transaction does three things, in order:
  1. `is_current = false` on every recomputed subject;
  2. INSERT the replacements;
  3. link `superseded_by`.
- A subject whose miss disappears is retired with step 1 only, with `retired_by_run_id` recorded.
- The partial unique index `missed_one_current_per_subject … WHERE is_current` enforces one current row per subject.

### 6. The job and the line

- `com.cobalt.replay` is a one-shot at 21:05 ET, Mon–Fri. It refuses unless **tonight's** 20:30 archiver occurrence finished `done` with exit 0.
- Its order is movers → cards → miss line, each with its own per-side commit boundary. An enforced deadline sits `replay.backup_margin_s` before the 21:40 backup.
- It writes ONE line, as unit `drc-misses/miss_line`, into that day's existing DRC note through `VaultWriter.upsert_unit`. The unit is placed zero-width after the `drc-rules` section. The write is versioned, diffed, human-wins, and never creates the note (L28).
- The cf-R sum always carries its n. An average renders only at n ≥ 30 (L8).
- The plist is new, so `cobalt jobs restarts` derives **bootstrap once**, no restart (R1-22/R2-6).

## Consequences

- The corpus answers "what did discipline cost" with numbers that replay, and it says `input_stale` rather than guessing when the bars cannot support an answer.
- `cobalt smoke s2` (STEP-9, R6) checks this corpus on the S2 close. K6 checks picks, K7 the replay job, K8 missed rows equal `job.result` with zero `input_stale`, K9 movers and K10 the miss line (K17, cobalt validate, left the S2 smoke 2026-09-24 — R114).
- **Open, not decided here** (plan §8, the build C report's ESCALATE):
  - The L53 total-demand gate refuses the archiver and replay under the unchanged `finviz_max_rpm` ceiling. This is a deploy gate, and the ceiling number is Dejan's ruling.
  - `trade_count_band` values are unset.
  - Binding P2's formation contract (`ReplayFormation` lacks member id, md5 and receipt reference).
- Rollback is by migration number, never "whatever came before" (plan §6 rollback, items 1, 2 and 7):
  - `--down-to 0008` reverses 0009 (the USER tables `picks` and `missed`).
  - `--down-to 0007 --allow-prod` reverses 0008 (SYSTEM `movers_daily` and the two membership columns).
