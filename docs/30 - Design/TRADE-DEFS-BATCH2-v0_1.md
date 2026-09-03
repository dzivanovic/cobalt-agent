# Trade Definitions — Batch 2 (v0.1)
Population session 2026-09-02 (closed). Schema v0.3 (TAXONOMY-DRAFT-v0_6 §10) with the amendments in §A below (→ v0.7). All seven trade_defs RULED. Source of truth: full SMB cheat sheets (2 pages each). Gap & Go excluded (setup sheet, v0.6 §12).
Legend: RULED = Dejan confirmed · DwV = decided with veto (stands unless vetoed) · config = editable value, default shown · dynamic = must survive archiver-corpus replay (§0 law) · (frontier) = human-owned until the data source lands.

---

## A. Taxonomy / schema amendments ruled today (fold into v0.7)

**Schema v0.3 field / enum changes — all RULED**
1. **`reentry_window: duration | null`** (default null) — new trade_def field. Attempt n+1 is valid only if the trigger re-fires within the window (GGG: 3 min). Rules gate intersects it with the 08-27 re-entry rule; stricter wins (same treatment as `max_attempts`).
2. **Stop placement gains `indicator {indicator: VWAP | EMA9 | EMA20/21, buffer: fixed <¢> (default 0.02), snapshot: at_entry | live, floor: config}`.** Default `snapshot: at_entry` — the hard stop is the indicator price at fill; `live` (Cobalt re-warns as the indicator drifts) exists but is not the default. Consumers: VWAP Continuation, First VWAP Pullback (VWAP), 9 EMA Scalp (EMA21).
3. **Trigger type `trendline_break {ref: Level_ref(trendline, anchor_leg), pivots: N (config, default 2), confirmation_policy}`.** Level.type `trendline` (09-01) anchored on the named leg's pivots; sloped by nature. The flat case (pullback consolidated into a micro-Range) is the same trigger with slope 0 — the break must be through the **far bound** (`Range(micro).top` for a long). **A touch of VWAP / the base is never the trigger.** One trigger per trade_def stands (no variants). Consumers: VWAP Continuation (anchor = pullback leg), Bella Fade (anchor = opening-drive leg).
4. **Trigger type `indicator_rejection {indicator, contact: touch | penetrate}`, confirmation `close_through`.** The bar that touches or penetrates the indicator and closes on the trade side IS the trigger and the entry. Next-bar continuation = tape read = human. Replaces the "tape-proxy" idea entirely. Consumers: First VWAP Pullback (VWAP), 9 EMA Scalp (EMA9).
5. **`Level.type` gains `open`** (the RTH opening print) → `bar_break {ref: Level_ref(open)}` for Back-Through Open; no new trigger type.
6. **Ruling 3 reworded (stop buffer):** `fixed 0.02` for every trade. A sheet stating a different value is **flagged as a proposal and applied only on Dejan's ruling** (BTO and Bella Fade sheets say 0.01 → ruled 0.02). Supersedes v0.6 "unless its sheet says otherwise".
7. **Structural refs gain `recent_lower_high`** — side-mirror of `recent_higher_low`; both = the micro-Range's latest counter-pivot. Bouncy Ball stop.
8. **Exit target `trail {conditions[], mode: any}`, evaluation `close_through`.** `conditions` enum: `prior_bar_break {n: 1}` · `ma_close {ma}` · `vwap_close` · `level {level_ref}` (exit-into-strength, DwV). Per-trade default set from the sheet; per-instance Dejan enables/disables on the card or branch ("based on price action"); first condition to fire exits. **MA periods are config keys** — sheets say EMA21, Dejan trades EMA20; one key `ma.slow = 20` (default) with `21` as the sheet value. Replaces the ad hoc "MA close as exit + bar trail as stop" split.
   - **1-bar trail law (RULED):** trailing = one working-TF bar (`prior_bar_break {n: 1}`), always. Applies to trails only — move2move **exits** on a double-bar break (`bar_break_reverse {bars: 2}`, GGG / Big Dog) are untouched.
   - **Stop-movement rule (RULED):** stop_management default `fixed`; the only permitted move = `raise_to {structural_extreme, ref: recent_higher_low}` (below the latest swing low), on Dejan's call. Per-sheet ladders already ruled in Batch 1 (Rubberband B/E-after-1R, Big Dog 50%-hold) stand.
   - **Batch 1 retro-fit (DwV):** Second Chance leg 2 → `trail {conditions: [ma_close {ma.slow}]}` (already noted "20 by price action"). Rubberband's `trail_ma_close` on `exit_leg(2)` was ruled as a stop and stays.

**Laws / notes — RULED unless marked**
9. **Working timeframe default (DwV):** `config/taxonomy/defaults.yaml: working_timeframe: 2m`, global, per-trade override. Sheets' "1-min" remains a template note only [A.18a].
10. **Class rule reaffirmed:** scalp ⇒ working TF ≤ 15-min; TF ≤ 15 ⇏ scalp; move2move / swing enter on any TF. **Trailing-exit trades are move2move**; scalp = one leg out (VWAP Continuation settled the pre-flagged question).
11. **TF audit (Dejan's check, DwV):** nothing in v0.6 / Batch 1 is pinned to 1-min. Bar-denominated params (bar_break_reverse 2, time_stop 2 bars, bars_cleared 2, pivot N=2, two_bar confirmation, 2-touch Range, MA trails, ATR(working_tf, 14)) follow the working TF — on 2-min a double-bar break = 4 minutes. Minute-denominated params (Range.duration bands 3–7 / 5–20 / ≥45, flat() windows, reentry_window) are TF-independent. Both kept as-is: SMB counts bars; Dejan trades bars on i2.
12. **Tape = frontier, not nature (RULED note under the tape law):** the human-only tape dot is a capability-frontier flag (08-31 per-field ownership: cobalt / cobalt-degraded / human), not a permanent law. Every tape-class read is a registry variable now with `source: human (frontier)` — `bids_hold`, `tape_flip`, `tape_read`, `buyers_defending_zone` — so it flips to Cobalt when an L2 / time-&-sales feed is ingested, no schema change. Triggers stay bar-defined; a tape-defined trigger enters only as an amendment backed by data.

**New grammar atoms / registry fields (DwV)**
13. `dist(a, b)` in working-TF ATR units → "near VWAP" = `dist(price, VWAP) <= k·ATR(working_tf, 14)`, k config.
14. `Catalyst.grade` (1–10, the LLM catalyst call) and `Catalyst.polarity` as predicate fields — BTO requires ≥ 8, Bella Fade ≤ 8 (config).
15. `Regime.label` in avoid predicates (09-01 SMB 2×2 label) — BTO avoids `range_bound | fading`.
16. `Range(micro).counter_pivot_count` — number of successively shallower counter-pivots (Bouncy Ball ≥ 2, config).
17. `gap_retrace_pct = Leg(opening_drive).range ÷ Gap.size` — GGG avoid > 0.5 (config) + quality factor.
18. `Leg(pullback).index` — ordinal of pullback legs since RTH open (FVP requires 1).

**§13 replay additions:** Range.duration 3–7 band (GGG) · trendline pivots N · dist() k per indicator · counter_pivot_count · gap_retrace_pct threshold · trail-condition sets per trade (outcome-tuned) · time_stop 2-bar no-progress (BTO, Bouncy Ball).

---

## B. trade_defs (RULED)

### B.1 Gap, Give and Go
```yaml
trade_def:
  id: gap_give_and_go
  name: Gap, Give and Go
  aliases: [GGG, Gap Give & Go]
  family: [opening_drive, continuation]
  class: move2move
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config (default 2m)
  entry_mode: front_side
  preconditions:
    - InPlay.state == active                            # "never on a stock that is not In-Play"
    - Gap.instantiated
    - Leg(opening_drive).direction == opposite(Gap.direction)   # the "give"
    - Leg(opening_drive).terminated_by == consolidation
    - Range(micro).instantiated
    - Range(micro).duration IN [3, 7] min (config)
    - Range(micro).low > Level_ref(support)             # PML / HTF resistance-turned-support; "never below a key support level"
    - Range(micro).height <= 0.5 × Leg(opening_drive).range   # "never when the consolidation > 50% of the opening move"
  trigger: {type: range_break, params: {ref: Range(micro).top}, confirmation_policy: intrabar}   # "don't wait for the bar to close"
  stop: {type: structural_extreme, params: {ref: consolidation_low, buffer: fixed 0.02, floor: config}, evaluation: touch}
  stop_management:
    - {type: raise_to, params: {placement: structural_extreme {ref: Range(micro).top, buffer: fixed 0.02}}, on: event(leg_end, 1)}   # "pullback MUST hold the consolidation highs"
  exit:
    - {fraction: 1.0, target_type: bar_break_reverse, params: {bars: 2, after: leg_end(2)}, evaluation: close_through, computable: cobalt}   # move2move exit — untouched by the 1-bar trail law
  on_cic: {triggers: [1,2,3,4], action: exit_all}     # advisory
  max_attempts: 2 (config)                             # sheet: "potential of 2 attempts"
  reentry_window: 3 min (config)                       # A.1
  add_policy: none
  avoid:
    - gap_retrace_pct > 0.5 (config)                    # sheet "very careful"
  quality_factors: [break_bar_volume_vs_consolidation, Range.volume_contraction (≤50% guide), Range.duration,
                    Range.height_vs_opening_leg, support_level_significance, gap_retrace_pct (neg),
                    prior_break_attempts (neg, before consolidation), Range.position_vs_vwap_ema9,
                    setup_relation, market_alignment (SPY/QQQ/IWM), sector_alignment]
  preferred_windows: [open_drive]
  preferred_windows_ref: "opening drive trade — starts at the open, triggers before 9:45 ET"
  reference_stats: null
```

### B.2 VWAP Continuation
```yaml
trade_def:
  id: vwap_continuation
  name: VWAP Continuation
  aliases: [VWAP Cont, VC]
  family: [continuation]
  class: move2move                                     # RULED: trailing exit = move2move
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config (default 2m)
  entry_mode: backside
  preconditions:
    - InPlay.state == active
    - Leg(opening_drive | impulse).direction == trade_direction   # "strong move in the morning"
    - Leg(pullback).direction == opposite AND dist(Leg(pullback).end, VWAP) <= k·ATR(working_tf) (config)
  trigger: {type: trendline_break, params: {ref: Level_ref(trendline, anchor_leg: Leg(pullback)), pivots: 2 (config)}, confirmation_policy: intrabar}   # A.3; flat case = break of Range(micro).top; VWAP touch never triggers
  stop: {type: indicator, params: {indicator: VWAP, buffer: fixed 0.02, snapshot: at_entry, floor: config}, evaluation: touch}   # A.2 — "just below VWAP", hard stop
  stop_management: fixed
  exit:
    - {fraction: 0.5, target_type: level, params: {level_ref: high_of_day}, evaluation: touch, computable: cobalt}   # "sell half into the high of the day"
    - {fraction: 0.5, target_type: trail, params: {conditions: [ma_close {ma.slow (config 20; sheet 21)}], mode: any}, evaluation: close_through, computable: cobalt}   # A.8 — "trail the rest with the 21 EMA"
  on_cic: {triggers: [1,2,3,4], action: exit_all}     # advisory
  max_attempts: 1 (config)                             # sheet silent
  add_policy: none
  avoid:
    - text: opening auction choppy / not definitive
    - Level_ref(resistance).rejected                    # "rejection of an important resistance level"
  quality_factors: [drive_definitiveness, pullback_depth_vs_vwap, vwap_hold_bar_count, catalyst_class (changing fundamentals = pos; weak/uneventful = neg),
                    htf_level_breakout, resistance_rejection (neg), rvol, setup_relation, market_alignment (strong/weak market), sector_alignment]
  preferred_windows: [morning, midday]
  preferred_windows_ref: "late morning 10–11 AM · mid-day 11 AM–2 PM"
  reference_stats: null
```

### B.3 First VWAP Pullback
```yaml
trade_def:
  id: first_vwap_pullback
  name: First VWAP Pullback
  aliases: [1st VWAP Pullback, FVP]
  family: [opening_drive, continuation]
  class: scalp                                         # single target, one leg out
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config (default 2m) · tf_ceiling: 15-min
  entry_mode: front_side
  preconditions:
    - InPlay.state == active
    - Leg(opening_drive).direction == trade_direction
    - Leg(pullback).index == 1                          # the FIRST pullback since the open
    - Leg(pullback) touched VWAP                        # contact, not proximity
  trigger: {type: indicator_rejection, params: {indicator: VWAP, contact: touch | penetrate}, confirmation_policy: close_through}   # A.4 — the rejection bar is trigger + entry
  stop: {type: indicator, params: {indicator: VWAP, buffer: fixed 0.02, snapshot: at_entry, floor: config}, evaluation: touch}   # A.2 — "just below VWAP"
  stop_management: fixed
  exit:
    - {fraction: 1.0, target_type: measured_move, params: {anchor_a: Leg(opening_drive).start, anchor_b: Leg(opening_drive).end, projected_from: turn_low, multiple: 1.0}, evaluation: touch, computable: cobalt}   # "measured move of the first leg"
  on_cic: {triggers: [1,2,3,4], action: exit_all}     # advisory
  max_attempts: 1 (config)
  add_policy: none
  avoid:
    - Extension.instantiated on Leg(opening_drive)     # "too extended / parabolic"
    - Leg(pullback).low < VWAP (close_through)          # "pullback should not be below VWAP"
    - Leg(pullback).low < Level_ref(PMH) (close_through)   # "pull in below the PM high = failed breakout"
    - text: opening auction choppy or slow
  quality_factors: [drive_strength (range + volume), drive_definitiveness, pullback_speed (quick = pos), pullback_depth_vs_vwap,
                    pmh_hold_after_pullback, tape_read (human, frontier), catalyst_class, rvol,
                    setup_relation, market_alignment, sector_alignment]
  preferred_windows: [open_drive]
  preferred_windows_ref: "Open 9:35–9:45 AM"
  reference_stats: null
```

### B.4 9 EMA Scalp
```yaml
trade_def:
  id: ema9_scalp
  name: 9 EMA Scalp
  aliases: [9 EMA, EMA9 Scalp]
  family: [continuation]
  class: scalp                                         # one leg out; HOD or EMA9 trail = the same single exit (A.8 conditions)
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config (default 2m) · tf_ceiling: 15-min
  entry_mode: front_side
  preconditions:
    - InPlay.state == active
    - catalyst_ref != null                              # "avoid entirely without a strong catalyst or setup"
    - Leg(opening_drive | impulse).direction == trade_direction
    - Leg(pullback) touched EMA9 AND price > EMA21      # the 9 EMA test, 21 still below
  trigger: {type: indicator_rejection, params: {indicator: EMA9, contact: touch | penetrate}, confirmation_policy: close_through}   # A.4 — sheet "when the bids start to hold"
  stop: {type: indicator, params: {indicator: EMA21 (ma.slow config), buffer: fixed 0.02, snapshot: at_entry, floor: config}, evaluation: touch}   # A.2 — "just below the 21 EMA"
  stop_management: fixed
  exit:
    - {fraction: 1.0, target_type: trail, params: {conditions: [level {high_of_day} (close_through = exit into momentum after the break), ma_close {EMA9}], mode: any}, evaluation: close_through, computable: cobalt}   # A.8 — "after the HOD break or a 9 EMA trail"
  on_cic: {triggers: [1,2,3,4], action: exit_all}     # advisory
  max_attempts: 1 (config)
  add_policy: none
  avoid:
    - Extension.instantiated on the leg before the test   # "too big of a move before the 9 EMA test"
    - text: choppy opening move
  quality_factors: [catalyst_class (changing fundamentals = pos), drive_strength, drive_definitiveness, daily_level_breakout,
                    move_size_before_test (ATRs, neg), pullback_depth_vs_ema9, bids_hold (human, frontier), rvol,
                    setup_relation, market_alignment, sector_alignment]
  preferred_windows: [open_drive, morning]
  preferred_windows_ref: "Opening Auction 9:35–9:45 AM · Morning 9:45–11 AM"
  reference_stats: null
```

### B.5 Back-Through Open
```yaml
trade_def:
  id: back_through_open
  name: Back-Through Open
  aliases: [BTO, Back Through Open]
  family: [opening_drive, continuation]
  class: move2move                                     # RULED
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {gap_down_into_support, countertrend}, {gap_up_into_resistance, countertrend}, {day2_continuation, with_trend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config (default 2m)
  entry_mode: front_side
  preconditions:
    - InPlay.state == active
    - Gap.instantiated                                  # "big gap up"
    - Catalyst.grade >= 8 (config)                      # "avoid entirely if the catalyst is not at least an 8+"
    - Leg(opening_drive).direction == opposite(Gap.direction)   # the initial downtick
  trigger: {type: bar_break, params: {ref: Level_ref(open)}, confirmation_policy: intrabar}   # A.5 — "aggressively when price crosses back through the opening price"
  stop: {type: structural_extreme, params: {ref: turn_low, buffer: fixed 0.02, floor: config}, evaluation: touch}   # sheet 0.01 → RULED 0.02 (A.6); "LOD" = tracked low
  stop_management:
    - {type: time_stop, params: {duration: 2 bars (config), condition: no progress from entry}}   # "should work right away — no chop or pause after entry"
  exit:
    - {fraction: 1.0, target_type: trail, params: {conditions: [prior_bar_break {n: 1}, ma_close {EMA9}], mode: any}, evaluation: close_through, computable: cobalt}   # A.8 — "close below the 9 EMA or a two-bar break" → 1-bar trail law
  on_cic: {triggers: [1,2,3,4], action: exit_all}     # advisory
  max_attempts: 1 (fixed)                              # sheet: "we will only try this trade once"
  add_policy: none
  avoid:
    - Regime.label IN {range_bound, fading} (config)    # "does not work in a range-bound market or one fading moves"
    - text: chop or pause after entry (mechanised via time_stop)
  quality_factors: [catalyst_grade, cross_time_since_open (≤5 min guide), downtick_depth (small = pos), post_cross_momentum,
                    daily_chart_breakout, market_momentum (aggressive = pos), rvol,
                    setup_relation, market_alignment (opposite trend = neg), sector_alignment]
  preferred_windows: [open_drive]
  preferred_windows_ref: "First 5 minutes of the trading day"
  reference_stats: null
```

### B.6 Bella Fade
```yaml
trade_def:
  id: bella_fade
  name: Bella Fade
  aliases: [Bella]
  family: [opening_drive, reversion]
  class: move2move                                     # "two waves" = hold through the pullback for leg 2
  sides: long+short (inverted)
  valid_setups: [{gap_down_into_support, countertrend}, {gap_up_into_resistance, countertrend}, {day2_continuation, with_trend}, {overextension, countertrend}, {volatility_in_range, countertrend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config (default 2m)
  entry_mode: front_side
  preconditions:
    - InPlay.state == active
    - Leg(opening_drive).direction == opposite(trade_direction)   # the institutional order's move
    - Catalyst.grade <= 8 (config)                      # "avoid entirely if the catalyst is more than an 8"
  trigger: {type: trendline_break, params: {ref: Level_ref(trendline, anchor_leg: Leg(opening_drive)), pivots: 2 (config)}, confirmation_policy: intrabar}   # A.3 — "aggressively on the trendline break"
  stop: {type: structural_extreme, params: {ref: turn_low, buffer: fixed 0.02, floor: config}, evaluation: touch}   # sheet 0.01 → RULED 0.02 (A.6)
  stop_management: fixed
  exit:
    - {fraction: 0.5, target_type: leg_end, params: {leg_index: 1}, evaluation: touch, computable: cobalt}   # "half into the first wave"
    - {fraction: 0.5, target_type: leg_end, params: {leg_index: 2}, evaluation: touch, computable: cobalt}   # "the other half into the second wave"
  on_cic: {triggers: [1,2,3,4], action: exit_all}     # advisory
  max_attempts: 2 (config)                             # sheet: two tries — "breaks the LOD but rebids immediately"; rules gate intersects 08-27
  add_policy: none
  avoid:
    - RangeBreak(Level_ref(HTF)).state == accepted against trade_direction   # "breaking a strong technical level" / "breaks support"
    - Range(micro) near turn_low AND Range.duration > threshold (config)     # "consolidates near the lows for long = selling pressure remains"
    - Catalyst.polarity == against trade_direction      # "negative catalyst weighing on the stock"
  quality_factors: [tape_flip (human, frontier), speed_away_from_low (quick = pos), support_level_proximity, support_level_significance,
                    drive_volume_climax (order ending), catalyst_grade, catalyst_polarity, time_near_lows (neg), rvol,
                    setup_relation, market_alignment, sector_alignment]
  preferred_windows: [open_drive]
  preferred_windows_ref: "First 15 minutes of the trading day"
  reference_stats: null
```

### B.7 Bouncy Ball
Sheet written short-side (breakdown); def side-symmetric, long = inverted.
```yaml
trade_def:
  id: bouncy_ball
  name: Bouncy Ball
  aliases: [BB, Bouncy Ball Breakdown]
  family: [continuation, range_break]
  class: move2move                                     # trail-only exit
  sides: long+short (inverted)
  valid_setups: [{gap_and_go, with_trend}, {overextension, countertrend}, {range_break, with_trend}]
  instance_direction: computed
  working_timeframe: config (default 2m)
  entry_mode: front_side
  preconditions:
    - InPlay.state == active
    - Leg(impulse).direction == trade_direction         # "significant move in one direction"
    - Range(micro).instantiated AND Range(micro).bound_type == converging   # shallower bounces against a flat low
    - Range(micro).counter_pivot_count >= 2 (config)    # ≥2 lower highs (short) / higher lows (long)
  trigger: {type: range_break, params: {ref: Range(micro).base}, confirmation_policy: intrabar}   # "aggressively when the support breaks"
  stop: {type: structural_extreme, params: {ref: recent_lower_high, buffer: fixed 0.02, floor: config}, evaluation: touch}   # A.7 — "just above the lower high"; sheet gives no number
  stop_management:
    - {type: time_stop, params: {duration: 2 bars (config), condition: no progress from entry}}   # "we do not want to see a rebid once support breaks"
  exit:
    - {fraction: 1.0, target_type: trail, params: {conditions: [prior_bar_break {n: 1}, ma_close {EMA9}], mode: any}, evaluation: close_through, computable: cobalt}   # A.8 — "new 2-min high or reclaim of the 9 EMA" → RULED: one working-TF bar
  on_cic: {triggers: [1,2,3,4], action: exit_all}     # advisory
  max_attempts: 1 (config)
  add_policy: none
  avoid:
    - Extension.instantiated on the opening leg         # "opening drop overextended from VWAP"
    - text: rebid after the break (mechanised via time_stop)
  quality_factors: [break_bar_volume_vs_prior (increasing = pos), post_break_speed (quick = pos), post_break_volume (decreasing = neg),
                    bounce_count, bounce_shallowing_rate, Range.duration, extension_distance_from_vwap (neg), rvol,
                    setup_relation, market_alignment, sector_alignment]
  preferred_windows: [morning, midday, afternoon, close]
  preferred_windows_ref: "Late morning 10:30–11:59 · Mid-day 12–2 PM · Power hour 3 PM–close"
  reference_stats: null
```

---

## C. Population status
- Populated to date: 13 of 21 grid trades (Batch 1: 6 · Batch 2: 7).
- Not populated (sheets not in hand): opening_drive_pmh, opening_range_break, first_move_down, first_move_up, spencer_scalp, off_sides, the_330_trade, ema9_reclaim — `valid_setups[]` only (Batch 1 §C).
- Day 3 liquidity trap — PLACEHOLDER (§11).
- Gap & Go — setup sheet, excluded (v0.6 §12).

---

## LEDGER APPENDIX (paste into PROJECT-LEDGER.md)

### 09-02 (Trade population, Batch 2, closed)
- Seven trade_defs RULED from full SMB sheets: Gap Give and Go, VWAP
  Continuation, First VWAP Pullback, 9 EMA Scalp, Back-Through Open,
  Bella Fade, Bouncy Ball → TRADE-DEFS-BATCH2-v0_1.md (30 - Design/).
  13 of 21 grid trades now populated. Gap & Go excluded (setup sheet).
- SCHEMA v0.3 → v0.7 amendments A.1–A.8, all RULED: reentry_window
  field (GGG 3 min); indicator stop placement {VWAP|EMA, buffer,
  snapshot at_entry default}; trendline_break trigger (anchored on a
  named leg, sloped by nature, flat case = far-bound break, touch
  never triggers); indicator_rejection trigger (bar touches/penetrates
  indicator, closes trade-side = trigger + entry — replaces any tape
  proxy); Level.type gains open (BTO trigger = bar_break on open);
  Ruling 3 reworded — 0.02 for every trade, sheet deviations FLAGGED
  and applied only on ruling (BTO/Bella 0.01 → 0.02); recent_lower_high
  ref; exit type trail {conditions[]: prior_bar_break 1 | ma_close |
  vwap_close | level, mode any} — per-trade default set, per-instance
  enable on card/branch, MA periods config (sheet 21 / Dejan 20).
- LAWS: 1-bar trail law (trailing = one working-TF bar; move2move
  double-bar EXITS untouched); stop default fixed, only move =
  raise_to below latest swing low, on his call; class rule reaffirmed
  (scalp ⇒ TF ≤15; not converse; trailing exit = move2move, scalp =
  one leg out — settled at VWAP Continuation).
- DwV: working_timeframe config default 2m (defaults.yaml), per-trade
  override; TF audit — nothing pinned to 1-min, bar params follow the
  working TF (2-bar = 4 min on i2), minute params TF-independent.
- TAPE = FRONTIER: human-only tape dot is a capability-frontier flag
  (08-31 ownership model), not a permanent law — tape-class reads are
  registry variables with source: human (frontier), flip to Cobalt
  when L2/T&S ingestion lands; triggers stay bar-defined until data
  justifies a tape trigger.
- New grammar/registry fields (DwV): dist(a,b) in ATR units;
  Catalyst.grade + Catalyst.polarity; Regime.label in avoid;
  Range.counter_pivot_count; gap_retrace_pct; Leg(pullback).index.
  Second Chance leg-2 retro-fit to trail exit at the Code commit.
- Code commit for Batch 1 still in flight at close; Batch 2 Code
  prompt issued assuming clean — fold any reported mismatches first.
- NEXT: Code commit Batch 2 → v0.7 fold session (A.1–A.8 into
  TAXONOMY-DRAFT-v0_7.md, FINAL) → remaining 8 grid trades when
  sheets are found; Product Definition sittings resume.
