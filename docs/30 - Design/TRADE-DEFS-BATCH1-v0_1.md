# Trade Definitions — Batch 1 (v0.1)
Population session 2026-09-02 (closed). Schema v0.2 (TAXONOMY-DRAFT-v0_5 §10) with the amendments in §A below. All six trade_defs RULED. Source of truth: SMB cheat sheets (2 pages each, full text); Rubberband = Rev1 deck over sheet, further amended by today's rulings.
Legend: RULED = Dejan confirmed · config = editable value, default shown · dynamic = must survive archiver-corpus replay (§0 law).

---

## A. Taxonomy / schema amendments ruled today (fold into v0.6)

**Schema v0.2 field changes**
1. `family` → `family[]` — a trade may carry more than one; enum extensible. Enum: `opening_drive · continuation · range_break · reversion · time_window` (`time_window` names the family, not a clock — The 3:30 Trade is afternoon anatomy, ~14:00 onward).
2. `class` = management shape, not timeframe: `scalp` = one leg out, ≤15-min ceiling (longer is not a scalp); `move2move` = hold through a pullback for leg 2, any timeframe, no ceiling. Supersedes 09-02 ledger wording "≤15-min = scalp, beyond = move2move".
3. `stop_management` enum gains `raise_to {placement: <any stop-placement enum>, on: event}` (serves Big Dog 50%-hold and Rubberband B/E-after-1R).
4. Structural refs gain `cross_point {a, b}` — price at an indicator cross; also the trigger event's price stamp for `indicator_cross`.
5. Structural refs: `turn_low` / `snapback_candle` = the current tracked extreme of the move.

**Primitive amendments (§3)**
6. `Range.duration` (start→now) — data field. Consumed as a precondition band per trade (Hitchhiker 5–20 min; Big Dog ≥ 45 min default) and as a quality factor. Config, dynamic.
7. `Range.shape: converging | parallel` — flags are parallel channels; Big Dog accepts both.
8. `Range.wick_ratio` (avg wick / avg body over the range) — data field; "choppy consolidation" avoid threshold config.
9. `flat(indicator, window)` predicate: `slope_norm = regression slope per bar ÷ ATR(working_tf, 14)`; `abs(slope_norm) < flat_threshold[indicator]`. Separate keys for EMA9 and VWAP; window per consumer (EMA9 avoid = 15 min ÷ working TF; VWAP at trigger = 5 bars). Config, dynamic. Working-TF ATR, never daily.
10. `RangeBreak(HTF).day_count` — day-1 HTF breakout predicate (Overextension day-count machinery); avoid for Back$ide and Rubberband.
11. `Leg(impulse)` — any directional leg preceding a range; Big Dog precondition (Hitchhiker keeps `Leg(opening_drive)`).

**§4 radar-table amendments**
12. Big Dog: precondition = `Leg(impulse)` terminated by consolidation + micro-Range `shape IN {converging, parallel}` + `volatility_state: contraction` + `Range.height ≤ 50% day range` + `Range.duration ≥ config`. `above PDH` and `>75% of day above open` DEMOTED to quality factors (sheet frames them as "checks in our favor"; DELL 2026-09-02 exemplar fails both and worked).
13. Hitchhiker: precondition gains `Range.duration 5–20 min` — the discriminator between Hitchhiker and Big Dog.
14. Rubberband: ONE trigger (snapback bar-break). Variant B's HTF level = watch/checkpoint state on the radar, never a trigger — the leg may blow through it. B survives as quality factors (ATRs from open, HTF level proximity/significance, prior-session rehearsal) and as a branch-level target override. Rev1 deck needs a Rev2 note.

**Cross-cutting laws ruled today**
15. **Advisory-exit law:** every `on_cic`, `stop_management`, exit and time-stop field is a warning to the human, never an order — Cobalt never executes. Revise from real trades.
16. **Per-trade stop rules:** no uniform stop law across trades; buffers per sheet. The 08-27 minimum stop-distance floor lives in the rules gate (`floor: config` points there).
17. **Stop-nudge law (rules gate, card stage):** never exactly on the structural price, a round dollar, or a x.x0 cent level — 1–2¢ beyond. The sheets' "$0.02" is this rule (order-cluster avoidance, not a noise buffer).
18. **Sheet reading laws:** (a) every SMB scalp sheet is TF-templated — structure fixed, "1-min bar" = working TF; (b) "low of the day" = the current tracked low of the move (snapback/turn candle), not necessarily the session LOD, unless the image shows otherwise; (c) `preferred_windows[]` populated from the sheet's "ideal times" section, mapped to the RTH sub-window enum, sheet times kept as reference — window-fit variable only.
19. **Attempts:** `max_attempts` editable per trade; sheet value is the default.
20. Standard quality factors on every card: `setup_relation`, `market_alignment`, `sector_alignment`.

**Backlog entries**
- Visual-similarity conviction variable (post-MVP, after grading engine): rendered working-TF chart → local vision model (Qwen3.8-27B) or image-embedding nearest-neighbour vs exemplar library → one semaphore dot with WHY; never a trigger; n≥30 hand-graded before it lights; blind mixed-deck validation (real/failed/empty); shadow mode first.
- §13 replay additions: leg=wave alias (first consumer = Hitchhiker wave exits); Range.duration bands; flat_threshold per indicator; Range.wick_ratio threshold; break_volume_sigma_bars.

---

## B. trade_defs (RULED)

### B.1 Hitchhiker
```yaml
trade_def:
  id: hitchhiker
  name: Hitchhiker Scalp
  aliases: [HitchHiker, Hitch]
  family: [opening_drive]
  class: scalp
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config · tf_ceiling: 15-min
  entry_mode: front_side
  preconditions:
    - InPlay.state == active
    - Leg(opening_drive).terminated_by == consolidation
    - Range(micro).instantiated
    - Range(micro).duration IN [5, 20] min (config)
    - Range(micro).low >= DayRange.upper_third
  trigger: {type: range_break, params: {ref: Range(micro).bound}, confirmation_policy: intrabar}
  stop: {type: structural_extreme, params: {ref: consolidation_low, buffer: fixed 0.02, floor: config}, evaluation: touch}
  stop_management: fixed
  exit:
    - {fraction: 0.5, target_type: leg_end, params: {leg_index: 1}, evaluation: touch, computable: cobalt}
    - {fraction: 0.5, target_type: leg_end, params: {leg_index: 2}, evaluation: touch, computable: cobalt}
  on_cic: {triggers: [1,2,3,4], action: exit_all}   # advisory
  max_attempts: 1 (config)
  add_policy: none
  avoid:
    - Leg(opening_drive).terminated_by == pullback
    - Range(micro).wick_ratio > threshold (config)       # "choppy consolidation"
    - text: consolidation well beyond ~20 min
  quality_factors: [Range.duration, consolidation_height_vs_day_range, consolidation_volume_profile, drive_rvol,
                    break_bar_volume_vs_prior (+30% guide), consolidation_above_key_level (PMH/PDH),
                    drive_bar_count (one big bar = neg), prior_break_attempts (neg), setup_relation, market_alignment, sector_alignment]
  preferred_windows: [open_drive]                     # sheet: sets up before 9:59
  reference_stats: {win_rate: 55–60%, rr: 1.9}
```

### B.2 Big Dog
```yaml
trade_def:
  id: big_dog
  name: Big Dog Consolidation
  aliases: [Big Dawg]
  family: [opening_drive]
  class: move2move
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config
  entry_mode: front_side
  preconditions:
    - InPlay.state == active
    - Leg(impulse).terminated_by == consolidation
    - Range(micro).instantiated AND Range(micro).shape IN {converging, parallel}
    - Range(micro).duration >= 45 min (config)
    - volatility_state == contraction
    - Range(micro).height <= 0.5 × DayRange
  trigger: {type: range_break, params: {ref: Range(micro).top}, confirmation_policy: intrabar}
  stop: {type: structural_extreme, params: {ref: range_base, buffer: fixed 0.02, floor: config}, evaluation: touch}
  stop_management:
    - {type: raise_to, params: {placement: measured_fraction {anchor_a: entry, anchor_b: leg_end(1), fraction: 0.5}}, on: event(leg_end, 1)}
  exit:
    - {fraction: 1.0, target_type: bar_break_reverse, params: {bars: 2, after: leg_end(2)}, evaluation: close_through, computable: cobalt}
  on_cic: {triggers: [1,2,3,4], action: exit_all}   # advisory
  max_attempts: 1 (config)
  add_policy: none
  avoid:
    - Range(micro).top < Level_ref(HTF resistance)
    - text: pullback after move 1 retraces >50% of entry→leg_end(1)  (mechanised via raise_to)
  quality_factors: [Range.low > PDH, pct_day_above_open (>75% guide), catalyst_present, rvol, Range.duration,
                    Range.volume_contraction (≤50% prior avg guide), break_volume_sigma_bars (consecutive bars ≥ MA+2σ),
                    crescendo_volume_at_pattern_start (neg), location_below_upper_third_or_vwap (neg),
                    pullback_depth_after_leg1 (upper ⅓ ideal), setup_relation, market_alignment, sector_alignment]
  preferred_windows: [morning, midday]                # sheet: break 11:00–13:30; DELL exemplar broke 14:00 — fit variable only
  reference_stats: null
```

### B.3 Second Chance
```yaml
trade_def:
  id: second_chance
  name: Second Chance Scalp
  aliases: [2nd Chance]
  family: [range_break]
  class: scalp
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config · tf_ceiling: 15-min
  entry_mode: backside
  preconditions:
    - RangeBreak(level).state == accepted
    - event(retest) on that RangeBreak
  trigger:
    type: sequence
    steps:
      1: {break: price close_through Level_ref, confirmation_policy: close_through}
      2: {retest: event(retest)}
      3: {turn: close_above(prior_bar), confirmation_policy: close_through}
  stop: {type: structural_extreme, params: {ref: turn_candle, buffer: fixed 0.02, floor: config}, evaluation: touch}
  stop_management:
    - {type: trail_ma_close, params: {ma: EMA9 (config; 20 by price action), tf: working}, on: event(exit_leg, 1)}
  exit:
    - {fraction: 0.5, target_type: leg_end, params: {leg_index: break_leg}, evaluation: touch, computable: cobalt}
    - {fraction: 0.5, target_type: ma_close, params: {ma: EMA9 (config), tf: working}, evaluation: close_through, computable: cobalt}
  on_cic: {triggers: [1,2,3,4], action: exit_all}   # advisory
  max_attempts: 2 (config)                            # sheet: "2 strikes, never a 3rd"
  add_policy: none
  avoid:
    - RangeBreak.state == failed_trap after event(retest)   # sheet: back inside, no recovery next candle (N=1)
    - event(stop_hit) AND price inside Range(prior) → instance dead, no re-entry on break back up
  quality_factors: [level_significance, break_leg_strength (range + volume), retest_volume (low = good), retest_depth,
                    break_leg_range_vs_Range.height (>1 = neg), rvol, setup_relation, market_alignment, sector_alignment]
  preferred_windows: [morning, midday, afternoon, close]    # sheet: 9:59–4:00
  reference_stats: {win_rate: 50–55%, rr: 1.9}
```

### B.4 Back$ide
```yaml
trade_def:
  id: backside
  name: Back$ide Scalp
  aliases: [Backside Scalp]
  family: [reversion]
  class: scalp
  sides: long+short (inverted)
  valid_setups: [{gap_down_into_support, countertrend}, {gap_up_into_resistance, countertrend}, {day2_continuation, with_trend}, {overextension, countertrend}, {volatility_in_range, countertrend}]
  instance_direction: computed
  working_timeframe: config · tf_ceiling: 15-min
  entry_mode: backside
  preconditions:
    - Extension.state == backside                       # ≥1 HH + ≥1 HL above rising 9 EMA
    - Range(micro).instantiated AND Range(micro).low > EMA9 AND EMA9.slope > 0
  trigger: {type: range_break, params: {ref: Range(micro).top}, confirmation_policy: intrabar}
  stop: {type: structural_extreme, params: {ref: recent_higher_low (micro-Range base pivot), buffer: fixed 0.02, floor: config}, evaluation: touch}
  stop_management:
    - {type: time_stop, params: {duration: 2 bars (config), condition: no progress from entry in trade direction}}
  exit:
    - {fraction: 1.0, target_type: vwap, evaluation: touch, computable: cobalt}
  on_cic: {triggers: [1,2,3,4], action: exit_all}   # advisory
  max_attempts: 1 (fixed)
  add_policy: none
  avoid:
    - RangeBreak(HTF).day_count == 1                    # "never on a day-1 HTF breakout"
  quality_factors: [extension_distance_from_vwap, Extension.leg_count, rvol, Range.duration, hh_hl_count,
                    pct_bars_above_ema9_since_low, Range.position_lod_to_vwap (>0.5 good), price_action_consistency (text),
                    catalyst_ambiguity (sheet: increase), setup_relation, market_alignment, sector_alignment]
  preferred_windows: [morning, midday]                # sheet: 10:00–13:30
  reference_stats: {win_rate: 50–60%, rr: 1.4}
```

### B.5 Fashionably Late
```yaml
trade_def:
  id: fashionably_late
  name: Fashionably Late Scalp
  aliases: [Fash Late, FL]
  family: [reversion, continuation]
  class: scalp
  sides: long+short (inverted)
  valid_setups: [{gap_down_into_support, countertrend}, {gap_up_into_resistance, countertrend}, {day2_continuation, with_trend}, {overextension, countertrend}, {volatility_in_range, countertrend}]
  instance_direction: computed
  working_timeframe: config · tf_ceiling: 15-min
  entry_mode: backside
  preconditions:
    - Extension.state IN {reverting, backside}
    - slope_norm(EMA9) > flat_threshold.ema9 AND slope_norm(VWAP) <= flat_threshold.vwap
  trigger: {type: indicator_cross, params: {a: EMA9, b: VWAP, direction: a_crosses_above_b}, confirmation_policy: intrabar}   # stamps cross_point
  stop: {type: measured_fraction, params: {anchor_a: entry_price, anchor_b: turn_low, fraction: 0.33}, evaluation: touch}   # stop = entry − ⅓·(entry − turn_low)
  stop_management: fixed
  exit:
    - {fraction: 1.0, target_type: measured_move, params: {anchor_a: turn_low, anchor_b: cross_point, projected_from: cross_point, multiple: 1.0}, evaluation: touch, computable: cobalt}
  on_cic: {triggers: [1,2,3,4], action: exit_all}   # advisory
  max_attempts: 1
  add_policy: none
  avoid:
    - flat(EMA9, window: 15 min ÷ working_tf) between turn and cross
  quality_factors: [volume_convergence_vs_divergence, speed_after_turn (pct bars holding above EMA9), pause_at_cross_point (neg),
                    Range.wick_ratio after turn (neg), measured_move_vs_atr, Extension.leg_count, rvol, setup_relation, market_alignment, sector_alignment]
  preferred_windows: [morning, midday]                # sheet: 10:00–13:30
  reference_stats: {win_rate: 60%, rr: 3.0}
```

### B.6 Rubberband
```yaml
trade_def:
  id: rubberband
  name: Rubber Band Scalp
  aliases: [Rubberband, RB, snapback]
  family: [reversion]
  class: scalp
  sides: long+short (inverted)
  valid_setups: [{gap_down_into_support, countertrend}, {gap_up_into_resistance, countertrend}, {day2_continuation, with_trend}, {overextension, countertrend}, {volatility_in_range, countertrend}]
  instance_direction: computed
  working_timeframe: config · tf_ceiling: 15-min
  entry_mode: front_side
  preconditions:
    - Extension.state == culminating                    # §3.2 path A (bar character) or B (≥1.25 ATR from open, no catalyst)
  trigger: {type: bar_break, params: {bars_cleared: 2 preceding, both must be cleared, direction: any}, confirmation_policy: intrabar}
  stop: {type: structural_extreme, params: {ref: snapback_candle, buffer: fixed 0.02, floor: config}, evaluation: touch}
  stop_management:
    - {type: raise_to, params: {placement: breakeven}, on: event(exit_leg, 1)}
    - {type: trail_ma_close, params: {ma: EMA9, tf: working}, on: event(exit_leg, 2)}     # deck hard exit — a stop, not a target
  exit:
    - {fraction: 0.33, target_type: rr_multiple, params: {r: 1}, evaluation: touch, computable: cobalt}
    - {fraction: 0.33, target_type: rr_multiple, params: {r: 2}, evaluation: touch, computable: cobalt}
    - {fraction: 0.34, target_type: vwap, evaluation: touch, computable: cobalt}          # branch may override to level (next prior-day structure)
  on_cic: {triggers: [1,2,3,4], action: exit_all}   # advisory
  max_attempts: 2 (config)                            # sheet + deck
  add_policy: none                                    # puppy-dawg add stays PARKED (§10.6)
  avoid:
    - NOT Extension.instantiated                      # not extended from VWAP / no acceleration
    - RangeBreak(HTF).day_count == 1                  # shared with Back$ide
    - fresh_negative_news_against (text)
  quality_factors: [atrs_from_open (sheet >3 guide), rvol (sheet 5+ guide; factor not gate), last_leg_range_and_volume_expansion,
                    snapback_bar_volume_rank (top-5 day), pause_bar_in_cleared_set (doji = pos), Extension.leg_count,
                    htf_level_proximity, htf_level_significance, prior_session_rehearsal, short_interest_float,
                    Range.wick_ratio (neg), setup_relation, market_alignment, sector_alignment]
  radar_watch: Extension.culminating near Level_ref(HTF) → watch state (checkpoint, never entry)
  preferred_windows: [morning, midday]                # sheet: 10:00–10:45 · 10:45–13:30; open_drive valid only if already HTF-extended
  reference_stats: {win_rate: 60–65%, rr: 1.6}        # SMB; own stats at n ≥ 30 / side
```

---

## C. valid_setups[] — Cameron H grid, 21 trades (data)
Setup refs: `gap_and_go · gap_down_into_support · gap_up_into_resistance · day2_continuation · overextension · volatility_in_range · range_break`. W = with_trend, C = countertrend.

```
second_chance:        gap_and_go W · range_break W
fashionably_late:     gap_down_into_support C · gap_up_into_resistance C · day2_continuation W · overextension C · volatility_in_range C
hitchhiker:           gap_and_go W · range_break W
backside:             gap_down_into_support C · gap_up_into_resistance C · day2_continuation W · overextension C · volatility_in_range C
rubberband:           gap_down_into_support C · gap_up_into_resistance C · day2_continuation W · overextension C · volatility_in_range C
back_through_open:    gap_and_go W · gap_down_into_support C · gap_up_into_resistance C · day2_continuation W · range_break W
opening_drive_pmh:    gap_and_go W · day2_continuation W · range_break W
opening_range_break:  gap_and_go W · gap_down_into_support C · gap_up_into_resistance C · day2_continuation W · overextension C · range_break W
first_move_down:      gap_down_into_support C · day2_continuation W · overextension C · volatility_in_range C · range_break W
first_move_up:        gap_up_into_resistance C · day2_continuation W · overextension C · volatility_in_range C · range_break W
ema9_scalp:           gap_and_go W · range_break W
vwap_continuation:    gap_and_go W · range_break W
spencer_scalp:        day2_continuation W · range_break W
bella_fade:           gap_down_into_support C · gap_up_into_resistance C · day2_continuation W · overextension C · volatility_in_range C · range_break W
off_sides:            gap_down_into_support C · gap_up_into_resistance C · overextension C · volatility_in_range C
gap_give_and_go:      gap_and_go W · range_break W
first_vwap_pullback:  gap_and_go W · range_break W
big_dog:              gap_and_go W · range_break W
bouncy_ball:          gap_and_go W · overextension C · range_break W
the_330_trade:        gap_and_go W
ema9_reclaim:         gap_and_go W · range_break W
```

---

## D. Not populated
- Day 3 liquidity trap — no sheet; stays PLACEHOLDER (§11).
- 15 remaining grid trades — sheets not in hand; `valid_setups[]` only.
- Trade classes swing / options — defined when taken up.

---

## LEDGER APPENDIX (paste into PROJECT-LEDGER.md)

### 09-02 (Trade population, Batch 1, closed)
- Six trade_defs RULED and populated from full 2-page SMB sheets:
  Hitchhiker, Big Dog, Second Chance, Back$ide, Fashionably Late,
  Rubberband → TRADE-DEFS-BATCH1-v0_1.md (30 - Design/). Cameron H
  grid captured as valid_setups[] data for all 21 trades.
- SCHEMA: family -> family[] (enum opening_drive/continuation/
  range_break/reversion/time_window, extensible); class = management
  shape (scalp = one leg, <=15-min; move2move = hold for leg 2, any
  TF) — supersedes 09-02 "beyond 15-min = move2move"; stop_management
  gains raise_to{placement,on:event}; refs gain cross_point,
  turn_low.
- PRIMITIVES: Range.duration (precondition band per trade + quality
  factor), Range.shape converging|parallel, Range.wick_ratio;
  flat() = ATR-normalised regression slope (working-TF ATR, never
  daily), thresholds per indicator; RangeBreak(HTF).day_count;
  Leg(impulse). All config/dynamic → §13 replay.
- §4 AMENDED: Big Dog = Leg(impulse) + micro-Range converging|parallel
  + contraction + <=50% day range + duration>=config; PDH and 75%-
  above-open DEMOTED to quality factors (DELL 09-02 exemplar).
  Hitchhiker gains duration 5–20 min = the Hitchhiker/Big Dog
  discriminator. Rubberband = ONE trigger (snapback bar-break, both
  preceding candles cleared, any colour, doji = plus); HTF level =
  radar checkpoint never trigger; Variant B folded into quality
  factors + branch target override; Rev1 deck needs Rev2 note.
- LAWS: advisory-exit (every exit/CiC/time-stop field warns the
  human, Cobalt never executes); per-trade stop rules (no uniform
  law; 08-27 floor lives in rules gate); stop-nudge (never on
  structural price / round dollar / x.x0 — 1–2c beyond; sheets'
  "$0.02" is this rule); sheet reading laws (TF-templated "1-min";
  "low of day" = current tracked low; preferred_windows from
  sheets, fit variable only); max_attempts per trade, sheet =
  default.
- Rulings of note: Second Chance attempts 2 (sheet) and stop 2c under
  turn candle; Fashionably Late stop = entry − 1/3 (entry→turn_low),
  full exit at 1 measured move, intrabar cross; Back$ide time_stop
  2 bars no-progress; Big Dog exit = double-bar-break close_through
  after wave 2, 50%-hold via raise_to.
- BACKLOG: visual-similarity conviction variable (post-MVP, local
  vision/embeddings vs exemplar library, never a trigger, n>=30,
  blind-deck validated, shadow first).
- NEXT: fold amendments into TAXONOMY-DRAFT-v0_6.md; Code prompt to
  commit trade_defs as YAML data (config-as-code, Pydantic on load)
  with variable registry stub; Batch 2 when Dejan picks sheets.
