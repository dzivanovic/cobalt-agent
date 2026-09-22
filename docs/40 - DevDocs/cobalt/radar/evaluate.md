# `src/cobalt/radar/evaluate.py`

## What it does
Scan-job stage **S5 evaluate** (S2-P2 STEP-4; rulings R1, R2, R4, R9). It runs after S4 bars inside `com.cobalt.radar`, behind the same market_reset commit gate, and costs zero tokens. Every loaded trade_def is evaluated against every admitted pool member, using stored i1 bars aggregated to the working timeframe. A formation on an evaluable def lands an unsized WATCH card when `radar.cards_enabled` is true. Every run, dark or not, writes the system seam rows (`radar_score_run`, `radar_score`) and one user-side receipt (`radar_score_receipt`).

## Key functions/classes
- `evaluate_member(ld, member, *, tunables, defaults, scan_interval, clock)` is pure. It evaluates one member against one def and returns a `MemberEvaluation`:
  - an `evaluation`: `formed`, `not_formed`, `avoided`, `not_evaluable` or `input_stale`;
  - the closed seam payload (`seam.RadarScoreDetail`);
  - the `Formation`: Extension direction, trade direction, setup ref, `TriggerLevel`, `TrackedExtreme`, `StructuralStop` and formation bar;
  - the computed-factor `FactorObservation`s;
  - the consumed bar rows, the i1 bars after the formation bar, the working bars and EMA9.
- `evaluate_node` is a three-valued (Kleene) interpreter over the §10.5 AST.
  - An atom the detectors could not measure is unknown, never False.
  - `RangeBreak(HTF).day_count` on a day with no break is a definite null: `== 1` is False.
  - An AST shape no S2 detector serves raises `Unsupported`, which becomes `not_evaluable` with a generic seam atom.
- Outcome rules:
  - Preconditions form only when all are True.
  - An unknown precondition becomes `not_evaluable` for a path-B-only run (R4), `input_stale` when daily bars are missing or stale, and `not_formed` otherwise.
  - Any True avoid gives `avoided`.
- Direction comes from `valid_setups[].relation`. All countertrend trades against the Extension (an up run is a short); all with_trend trades with it. A def that mixes both is `not_evaluable` (`Setup(relation)`).
- `seam_atom` rewrites the registry's `trigger:<type>` as `Trigger(<type>)` and `stop:<type>:<ref>` as `Stop(<type>).<ref>`. These generic spellings pass `seam.validate_atom`. The full human list stays on `MemberEvaluation.missing`.
- `FACTOR_COMPUTERS` names the computed dots S2 can measure: `atrs_from_open`, `rvol`, `Extension.leg_count` and `htf_level_proximity`. Any other computed factor (today `trail_fit`) is `MANUAL` in `cards.scoring`.
- `refresh_card` produces the per-scan `CardUpdate`: fresh dots merged with stored taps and history, then `score_card` on the LIVE `entry`/`stop`. For a FILLED card it adds the entry snapshot (captured once) and the health pills.
- `EvaluateStage.run(...)` is the orchestration, in publish order (Astra R1-14):
  1. Read the card settings (per cycle), the defs and the merged tunables.
  2. Abandon any stale `running` run.
  3. Open the run.
  4. Evaluate, and write the seam rows.
  5. When enabled: refresh and expire the open cards, create new cards, and copy the card values back onto the seam rows.
  6. Write the receipt.
  7. Mark the run `complete`.
  - A failure marks the run `failed` and raises `EvaluateError`.
  - A `StageDropped` (market_reset) propagates with the run left `running`; the next cycle abandons it.
  - A per-card refusal (e.g. account mode unresolved) is collected in `StageOutcome.refusals`. The run still publishes, and the runner stamps `failed_stage='evaluate'`.
- `EvaluateStage.lifecycle_tickers(admitted)` lists the tickers of open radar cards whose member left the pool, so S4 keeps polling them (R1-15).
- Card creation checks, in order:
  - no open card for (ticker, slug, direction) — ticker, not member id, so a re-entered name's old card blocks a second one;
  - `formation_consumed` — any card, in any state, made from the same formation bar;
  - the persisted deadline `cards.expire.radar_deadline(preferred_windows_ref)` not already past;
  - no closed bar since the formation bar printing through the current structural stop. If one does, the run is still extending: no card this scan, and the formation is not consumed.
- Receipts (L57, Astra R1-10):
  - `build_receipt` and `chain_commit` write the retained values. Bars new or changed since the chain's previous receipt go in `rows_delta`, with each member's full row count and sha256. An unchanged snapshot is `{"unchanged_since_receipt", "sha256"}`. `valid_until` is 2 × scan_interval for intraday bars and the session boundary for daily bars.
  - `rebuild_members` and `replay_receipt` recompute every seam evaluation and published card number from a receipt chain alone, and refuse (`ReplayError`) a chain whose rebuilt rows do not hash to what it recorded.
- `formula_sha256()` hashes the source bytes of `FORMULA_FILES` (evaluate, anatomy, cards scoring/health/radar/expire, aset engine), sorted by path.

## Config it reads
Tunables: `radar.scan_interval`, the `extension.*` rows, `stop.buffer`, `card.dot.*`, `card.health.*`, plus the trader's per-trade rows (merged via `merge_tunables`). Defaults: `working_timeframe`, `ma.fast` (EMA9). Trader settings: the five card keys (`settings.card`) and the day-mode rung for enabled grades (`rung_source`).

## Gotchas
- "Formation" in the acceptance test means formed AND its stop still untouched. While a run extends, that flickers minute by minute (the stop re-anchors 2¢ over each new closed high). A 100 s scan can miss a one-minute valid window, so the guarantee is: no scan at which the formation is valid passes without a card.
- A dark run (`cards_enabled=false`) reads no cards and writes no card or dot rows. It still writes seam rows and a receipt.
- A crash between the user-side card write and publish leaves the card in place. The retry cannot duplicate it: the partial unique index answers "already open".
- The receipt chain lives in the resident's process; a restart starts a new full base.

## 2026-09-16 — S2-P2 chunk C: a def edited under an open card (STEP-9, Astra R2-4)
Adding `- catalyst` to a note (the R10 batch) changes its Definition unit's bytes, so the def's md5 changes while open cards still carry the md5 they formed under. Before this change the stage refused to refresh such a card ("no longer loaded") for the rest of its life.
- The stage now finds a card's def by its formation md5 first and, failing that, by its **slug** — the def's identity (ADR-0008 D3 a). The evaluation it refreshes from is keyed on the def actually used. Departed-member lifecycle coverage keys on slug for the same reason.
- `refresh_card(..., run_id=)` hands `refresh_dots` an `added_by = {definition_md5, run_id}`; a factor the def gained lands once, untapped, with a `factor_added` history record. `trigger_price`, `structural_stop`, `formed_at` and `trade_def_md5` are never touched.
- Each receipt card carries `definition_md5` (the def used this scan) next to `trade_def_md5` (formation evidence). `replay_receipt` evaluates with `definition_md5` when present.
- A slug that is gone from the loaded set is still a loud refusal, not a silent skip.

`radar_cards_v` joins its board columns on `radar_score_id` (the card's own latest refresh) instead of the md5, for the same reason.

## 2026-09-16 — the slug fallback is scoped to catalyst-review edits (chunk C fix 1)
The review found that the slug fallback above accepted any edit under the slug, so a changed precondition, trigger or stop could quietly start driving an already-open card's scoring. Now the fallback only substitutes the current def when `formation_changes(original, current)` comes back empty: every `TradeDef` field outside `CATALYST_REVIEW_FIELDS` (`quality_factors`, `preferred_windows`, `preferred_windows_ref`, `aliases`, `name`, `reference_stats`) must match the def the card formed under. The stage finds that original def in `EvaluateStage._formation_definition`, which reads it by the card's `trade_def_md5` from the `definitions_snapshot` of the formation day's receipts (`card_store.receipts_for_day`, the value the formation run already stored). It checks each snapshot's sha256 before use and keeps a found def in memory, since an md5 names content that never changes. If a formation field changed, a snapshot fails its hash check, or no receipt holds the md5, the card gets the same loud "no longer loaded — not refreshed" refusal as before, with the reason added (e.g. `trigger changed since formation`). The card is never refreshed from the new def, and the run is not lost.

## 2026-09-21 — setups one build STEP-1 (FINAL C1): direction from anatomy, the untappable `assumed_formation` dot
- **Direction from anatomy (FINAL §1, `A-01`).** `valid_setups[].relation` is never read. A def written long-side trades against an unqualified Extension: up-run → short, down-run → long. The old `not_evaluable: Setup(relation)` return and the order-dependent `setup_ref` label are deleted, not replaced. A def that mixes relations (the rubberband shape, 4 countertrend + 1 with_trend) now forms.
- **`UNCLASSIFIED_SETUP = "unclassified"`** is a module constant. It is not a `SetupRef` member, so no def can list it. Every formation carries it as `setup_ref`, and `card_why` starts with it. No setup is detected.
- **Geometry guard (FINAL §9 point (5)).** `stop_on_protective_side` requires long: stop < min(trigger, last close) and short: stop > max(trigger, last close). Otherwise the result is `not_formed`, note `stop_wrong_side`, and no card. X17 chose this branch: on the committed day it refused all 71 with-trend control formations and none of the 71 countertrend ones.
- **`card_dots(ld, ev, settings, at, assumed_keys, *, previous=None, added_by=None)`** is the one builder of a card's dots at all four sites: create, `refresh_card`, `replay_receipt` and `audit_export`. It returns the quality-factor dots, carried through `refresh_dots` when `previous` is given. When keys are present it then appends one `assumed_formation` dot (`cobalt-degraded`, `deterministic`, `shadow`, `na_reason` `ASSUMED`, `engine_inputs = {"assumed_keys": [...]}`). Where the keys come from: at CREATE, `Formation.assumed_keys`, set from `ASSUMED_CONVENTIONS = ("A-01",)` at this step; at REFRESH, the card's own stored dot (`assumed_keys_of(card.dots)`); no stored dot means no keys. At REPLAY they come from the receipt card entry's new `"assumed_keys"` list, which both receipt writers put beside `"taps"`. Live tunables are never read for this, so a row ruled later does not lift an open card. X27 showed the need: on the start-of-step code a dot appended outside `quality_factors` was dropped by `refresh_card`.
- **Gate 5.** `replay_receipt` refuses any receipt in the chain whose `observations.evaluator_version` is not `EVALUATOR_VERSION`. It raises `ReplayError` naming both versions and does not recompute. `EVALUATOR_VERSION` is bumped ONCE for the whole one build, `s2p2.1` → `s2p2.2` (the file's own scheme: the next minor of `s2p2`). `DESK_FORMULA_VERSION` is untouched.

**Every card formed on an assumed value shows NO score for its life.** It carries the untappable `assumed_formation` dot, and `card_score` stays null until he rules the rows it rests on. Rubberband's first cards rest on the convention `A-01` alone. That is the design (FINAL §10, R40), not a defect.
