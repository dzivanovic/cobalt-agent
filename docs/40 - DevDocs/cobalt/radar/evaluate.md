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
