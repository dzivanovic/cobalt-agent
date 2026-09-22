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

## 2026-09-21 — setups one build STEP-2 (FINAL C2): the Frame, the registries, one published row, the closure
- **The Frame.** `evaluate_member` builds one `anatomy.frame.Frame` per side: long is the stored bars, short is the mirrored bars and mirrored daily series. It evaluates the def's LONG-side text on each frame (`on_side`) and asks the frame for atoms. It no longer runs a detector itself. Trigger and stop come from the registries (`formation.triggers.TRIGGERS`, `formation.stops.STOPS` / `STRUCTURAL_REFS`) in frame coordinates. They are un-mirrored (`.unmirrored(side)`) before they reach `Formation`, so the formation and the card are in real-world prices. The geometry guard runs once, in frame coordinates, on every placement.
- **A-01 in frame language.** A def whose preconditions name an unqualified Extension forms in a frame only when that frame's Extension runs DOWN. A real up-run therefore forms on the mirrored (short) frame. The long frame's row is `not_formed`, note `the unqualified Extension runs with this side (A-01)`.
- **R2-4 = B (the launch row R50), `publish_frames`.** `MemberEvaluation.by_side = {long, short} -> SideOutcome(evaluation, formation, note)`. The ONE published row is:
  - the frame that formed, when exactly one did;
  - `not_formed`, note `both_sides`, with the long frame's detail, when both did;
  - the LONG frame's evaluation, when neither did. No order is defined among the non-formed states.
  Per-card decisions read the card's own side. The avoid that expires an open card is `by_side[card.direction]`. The refresh reads only frame-independent inputs: the observations are computed once on the real bars (R2-4.2 B), plus the last price, the working bars and EMA9. The other frame is not stored; replay re-derives it from the receipt's inputs (X21).
- **`Formation` gains** `side_frame` (`long | mirrored`), `anchor` (§2.4 — `extension_direction` stays for byte identity), `trigger_outcome` and `stop_outcome`, all in real coordinates.
- **The closure (R2-2.2 B).** `closure_keys(td)` is the union of:
  - `iter_cfg_tokens(td)`;
  - the `TUNABLE_KEYS` of every detector serving an atom the def names (`ATOMS[...].tunable_keys`);
  - the conventions (`ASSUMED_CONVENTIONS` for an Extension-anchored def, plus any atom's own).

  `assumed_closure(td, tunables)` = the closure keys whose resolved row reads `source: assumed`, plus every convention whose row is still null. It is computed ONCE at formation. Conventions are rows: A-01 is `anatomy.orientation.extension` (`tunables.yaml`, unit `label`, value null). `CONVENTION_LABELS` names the one label the code implements. Any other non-null label is `not_evaluable`, missing `<key>=<label>`. A convention with no row is a loud `EvaluateError`. X22 shows every tunable key the resolvers read is inside the declared closure.
- **Byte identity (Lego (ii)).** The rubberband shapes and the shipped example produce byte-identical evaluations and card specs through the registries (`tests/cobalt/test_setups_registries.py`). Only named fields are excluded: the added fields above; `formula_sha256`; the dot's key spelling; and `tunables_sha256`, mapped because committed config gained the convention row. The one by-design content change: an already-not-evaluable def now names `Unsupported(<kind>)` (E9).

The ONE `EVALUATOR_VERSION` bump of STEP-1 covers this step. Nothing deploys between the one build's steps (R44).

## 2026-09-21 — D1 and the warm-up (setups one build STEP-3; FINAL C3a, §5, [F-10], [F-11])

- **One frame builder.** `_build_frames` serves both `evaluate_member` and the new `member_frames(member, tunables=, defaults=, clock=)`. It hands each frame its `SessionInputs`: the complete premarket buckets, the premarket and RTH i1 bars, and the pool admission. It also passes the tunables, so the frame's lazy D1 atoms can read `slope_norm.bars` when a def names them. `_closed_i1` and `_daily_ok` are extracted helpers; their behaviour is unchanged.
- **[F-10].**
  - `ema9` now takes the long frame's `EMA9` atom: seeded from the premarket, falling back to RTH-only when the seed is short.
  - `atr_seeded` (the frame's `ATR(working_tf)`) is a NEW seam observation. It sits beside `atr_working`, which keeps its name and meaning (the Extension's RTH-run ATR).
- **Conventions.** `CONVENTION_LABELS` names the label the code implements for `frame.warmup_source`, `dayrange.session` and `vwap.anchor`. All three rows are null in committed config, so a def naming their atoms carries them as assumed keys.
- **[F-11], as tests** (`tests/cobalt/test_setups_d1.py`, pins captured on the start-of-step code). The Extension, `atrs_from_open`, `leg_count`, the dots and `card_score` do not move. X14 PASS: 138 refreshes of a FILLED card built on the committed day; no number but `health` moved.
- **Deploy note (F-10).** The `health` of open cards moves, because EMA9 is now seeded. The ONE `EVALUATOR_VERSION` bump of STEP-1 covers it: nothing deploys between steps (R44).

## 2026-09-22 — the anchor, the band shape, the generic why (setups one build STEP-4; FINAL C3b)

- **The anchor (FINAL §2.4).** `on_side` forms on `formation.anchors.anchor_for(td)`: the first anchor whose object the def's preconditions name.
  - The Extension anchor is byte-identical: the same notes, the same A-01 check, the same values.
  - The `Range(micro)` anchor forms at the Range's instantiation bar.
  - `Formation.formed_bar_ts` / `anchor` come from the anchor. `extension_direction` stays for byte identity and carries the anchor's real direction.
  - A def with no anchor object reads `not_formed`, note `no formation anchor`.
  - `detail.extension_path` and the avoided-bar stamp are an Extension formation's evidence only. They are `None` for another anchor, and unchanged for Extension defs and for defs with no anchor.
- **The band shape (§4 row 1).** `evaluate_node` gains a keyword `units=` (the tunable row's unit). `_in_band` evaluates `<atom> IN cfg(band) <unit>` as an inclusive `[lo, hi]`. The atom's unit, the Quantity's and the row's must agree; a mismatch is `Unsupported(unit:…)`, named. An absent band row still fails loud in `cfg()`. Any other band value is `Unsupported(band)`. An `Unsupported` raised in the interpreter now reaches the seam through `seam_safe_missing_atoms` (a unit name is not an atom spelling). The atom names that were already valid are unchanged.
- **`card_why` (F-05)** keeps the Extension sentence byte for byte. For another anchor it is assembled from the trigger's and the stop's own `why` fragments.

## 2026-09-22 — Arith, a null cfg, `between`, the stop's entry (setups one build STEP-5; FINAL C4)

- **Arith `*` / `/`** is evaluated in Decimal at the indicator module's precision. A zero divisor is unknown, `division_by_zero`, never inf.
- **A null `cfg(<key>)`** is unknown, `<key>_unset`. It used to be compared as `None` and raise `Unsupported` (`not_evaluable`): a latent defect that would have hit the drive-then-range shape's wick-ratio avoid at production defaults.
- **`evaluate_node(context=)`** carries the frame, the tunables, the def's trigger and the working minutes. The `Between` branch (`_between`) uses them: `flat(<ind>, window) between turn and cross` over the frame's series. Its thresholds are the `per_indicator` rows (F1: null → `flat_threshold.<ind>_unset`), and its events are the turn and the def's own cross.
- **The stop resolver gets `trigger=`**, so `measured_fraction` can anchor at `entry`. `Formation.stop_ref` is the stop outcome's `ref`.

## 2026-09-22 — bound symbols, `null`, `touched`, `on`, A-13's label (setups one build STEP-6; FINAL C5)

- `_value` reads `null`, `trade_direction` (→ `up`) and `opposite(…)` / `against(…)`.
- A comparison of two nulls is equal. So `catalyst_ref != null` is False for a departed member; it only arises with a `null` literal, which was `Unsupported` before.
- `_touched`: a leg's extreme reached the indicator on one of its bars.
- `_on`: `Extension.instantiated` of `detect_extension` over `Leg(pre_test)`'s bars. No pullback → False; too few bars → unknown with the detector's reason.
- `_conventions` also reads a used relation's own conventions.
- `CONVENTION_LABELS` gains `catalyst_ref.resolver` → `radar_in_play_admission` (A-13), `leg.pre_test` → `session_open_to_pullback_start` (A-14) and `extension.on_leg.form` → `extension_detector_over_leg_bars` (A-15).

## 2026-09-22 — `dist`, the level labels (setups one build STEP-7; FINAL C6)

- `_value` evaluates `dist(a, b)` as `|a − b|`: unknown and null propagate, and a non-number is `Unsupported(dist)`.
- `CONVENTION_LABELS` gains `levels.set` → `pmh_pdh` (A-17) and `level.rejected.rule` → `wick_through_close_back_below_still_below` (A-18).

## 2026-09-22 — events, the anaphora, `after`, `inside` (setups one build STEP-8; FINAL C7)

- **Events.** `evaluate_node` evaluates an `EventAtom` as the frame's boolean atom.
- **The anaphora.** `on_side` records `context["antecedent"] = "RangeBreak"` when a precondition naming a RangeBreak evaluates True. `_on_that_range_break` needs that antecedent, else it is unknown (`no_antecedent`), never "any".
- **`_after`:** the state holds AND its trap close came after the retest bar.
- **`_inside`:** the last close is back under the broken level, above `Range(prior)`'s floor.
- **Labels.** `CONVENTION_LABELS` gains `range_prior.rule` → `session_low_before_break_to_level` (A-21), `event.stop_hit.source` → `computed_from_bars_turn_low_less_buffer` (A-22) and `turn_candle.rule` → `turn_bar_low` (A-23).
