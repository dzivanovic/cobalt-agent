# `src/cobalt/replay/formations.py`

**2026-09-18 — S2-P4 chunk E2.** F12's formation half: the trade_defs that
formed on the replay day and were never taken (STEP-5, R4 as amended by
Astra R1-21). This is the positive half of R1-21 — the negative half (the
exact "not available until S2-P2" line and the loud refusal on an
incompatible contract) lives in `replay/runner.py`'s adapter.

## What it binds to

S2-P2's SHIPPED contract, recorded before a line of this module was
written:

| Fact | Shipped value |
|---|---|
| module | `cobalt.radar.evaluate_cli` |
| callable | `replay_formations(day, *, pool_key, slug_filter, radar_store, defs_source, daily_source, tunables, defaults, clock, out)` |
| writes | none — it reads membership, `system.bars` and the radar cache and re-evaluates |
| return | `ReplayReport(day, scans, formations, path_b_only, not_evaluable, counts)` |
| per formation | `ReplayFormation(seen_at, ticker, slug, direction, trigger, stop, formed_bar_ts, membership_id, trade_def_md5, score_inputs_sha256)` |
| capability marker | `cobalt.radar.evaluate.EVALUATOR_VERSION` (`"s2p2.1"`) |

The plan named the entrypoint `cobalt.radar.evaluate`. The shipped layout
splits it: the callable and its model in `evaluate_cli`, the marker in
`evaluate`. The code follows what shipped.

The last three `ReplayFormation` fields were ADDED to S2-P2 by this chunk,
additively: every one is a value `evaluate_member` already returned inside
the read-only replay (`ev.membership_id`, `ev.md5`, `ev.inputs_sha256`).
No schema changed, nothing new is written, and P2's own tests are
unchanged and green.

## Why those three fields

Migration 0009's `kind='formation'` CHECK requires `trade_def_md5`,
`formation_at` and `pool_member_id` to be NOT NULL, and
`missed_one_current_per_subject` adds `formation_at` and (for formations)
`pool_member_id` to the subject key, so two same-day formations of one
(ticker, trade_def) never collapse into one row. The mapping:

| `missed` column | From |
|---|---|
| `pool_member_id` | `ReplayFormation.membership_id` |
| `trade_def_md5` | `ReplayFormation.trade_def_md5` |
| `formation_at` | `ReplayFormation.formed_bar_ts` — the formation bar, which is P2's own dedup identity `(ticker, slug, formed_bar_ts)` |
| `trigger_ts` | the bar this replay found the trigger on — a different thing from `formation_at`, and a different column |

`entry`/`stop` take the SAME mapping the live card path takes
(`RadarCardSpec.entry = trigger_price`, `.stop = structural_stop`), so a
formation miss and the card it would have become read the same two
numbers.

## The retained score-receipt reference

`system.radar_score` is S2-P2's retained score receipt: one row per
`(run_id, membership_id, trade_def_md5)` carrying its own
`inputs_sha256`. P2's `--replay` path reads no receipt row — it writes
nothing and re-evaluates — so it cannot report a score row id. What it
CAN report, from data it already holds, is the receipt's natural key plus
that row's own digest. Every formation row's receipt therefore carries:

```json
"score_receipt": {"table": "system.radar_score", "column": "inputs_sha256",
                  "key": {"membership_id": 100, "trade_def_md5": "…"},
                  "inputs_sha256": "…64 hex…",
                  "note": "content-addressed: P2's read-only replay reads no receipt row and reports no score id"}
```

A resolver looks the row up by that key and matches the digest. A miss
means the resident's evaluation of that member × def used different
inputs — which is exactly what the reference is for, and is visible
rather than silent (L57).

## The one gate

One gate, ruled: an existing radar card for that (member, def, direction)
SUPPRESSES the miss. `MissedStore.radar_cards(trade_date)` supplies the
set — radar-origin cards CREATED that ET day, not "open now", because by
21:10 a card that formed at 10:00 may have EXPIRED and the card path
(F12) has already replayed it. Suppression keeps one event from becoming
two rows (L3). Every row this module writes therefore carries
`excluded_by = 'no_card'`.

`rule_10` is recorded `{"applies": false, "reason": …}`, never silently
passed: a formation has no card and no position of its own, and no
position-level exclusion was ruled for formations (R1-11's "uncomputed
clauses are recorded, never treated as passing"). `trade_count_band` stays
`"unset"` (plan §8 item 2). The `window` gate is recorded and cannot fire:
a formation has no card window, so `resolve_window(None, trade_date)` —
the ONE public resolver — gives the session close, and `W = session
close`.

## The arithmetic

`cards.counterfactual()`. The same trigger search, gap-through fill,
stop-wins-on-tie walk, horizon eligibility (`bar_start + 1 minute <= H`)
and half-up rounding a card gets, called with the formation's constant
stop instead of a card's as-of-trigger stop. There is no second cf-R
implementation anywhere in the package.

The trigger search starts at `seen_at`, the scan instant at which P2 saw
the formation — the formation's analogue of a card's `created_at`, and
the instant at which a radar card WOULD have been created. `formed_bar_ts`
is the subject's identity; `seen_at` is when it became actionable. Both
are in the receipt.

## Symbols

| Symbol | Role |
|---|---|
| `SUPPORTED_EVALUATORS` | the capability markers this binding was written against (`{"s2p2.1"}`) |
| `FORMATION_REQUIRED_FIELDS` | the `ReplayFormation` fields a miss row cannot be built without |
| `P2_MODULE` / `P2_CALLABLE` / `P2_MODEL` / `P2_MARKER` | recorded in every row's receipt |
| `NO_CARD`, `GATE_ORDER`, `RULE_10_NOT_APPLICABLE` | the gate vocabulary |
| `SCORE_RECEIPT_TABLE` / `SCORE_RECEIPT_COLUMN` | where the reference resolves |
| `FormationSources` | exactly P2's `replay_formations` arguments, minus day, slug filter and sink |
| `FormationContext` | `trade_date`, `session_close`, and the two lazy reads (`bars_for`, `radar_cards`) |
| `formation_candidates(report, *, evaluator_version)` | P2's formations → `FormationCandidate`s; refuses an unsupported marker or a changed model shape |
| `replay_formation(candidate, bars, *, trade_date, window, session_close, radar_cards)` | one formation → `FormationReplay` (`miss` / `suppressed` / `no_trigger` / `input_stale`). PURE |
| `replay_formation_from_receipt(receipt)` | recompute a stored row from its receipt's inputs alone (L57) |
| `formation_misses(report, *, context, evaluator_version)` | the day → `FormationOutcome`; refuses if two rows ever share one subject |

## Fail-loud (L1)

- unsupported `evaluator_version` → `ReplayError`
- a `ReplayFormation` missing a required field → `ReplayError`
- a formation stamped for another ET date → `ReplayInputError`
- a stop on the wrong side of its trigger, or equal to it → `ReplayInputError` (from `counterfactual`)
- bars that do not cover `seen_at` → close → `input_stale`, counted, no row, never a fake R
- two rows sharing one subject → `ReplayInputError` (the extended key failed to separate them)

## Tests

`tests/cobalt/test_replay_formations.py` — every formation in it comes out
of a real `replay_formations` run over S2-P2's own hub-cut bar fixture
(L45). The shipped `countertrend` def's two same-day FTFT formations never
traded through their trigger (the real no-trigger case); the `with_trend`
variant's two do, and are the R1-21 two-rows case. The end-to-end run
through `run_nightly` is in `tests/cobalt/test_replay_runner.py`.
