---
trade_def: example-range-break
name: Example Range Break
class: scalp
family: [range_break]
sides: [long, short]
working_timeframe: 2m
status: defined
source: synthetic example shipped with Cobalt
---
## Why it works

<!-- This note is the ONE trade_def the Cobalt repo ships, and it is
     SYNTHETIC. It names no trader, cites no cheat sheet and encodes no
     rule anyone paid for: every term in it comes from the taxonomy's own
     anatomy vocabulary (Range, Leg, Extension, the session clock). That
     is ADR-0008 D3's last line — the product installs EMPTY, and a
     trader's real strategies are their own data, living in their own
     vault, never in this repo.

     It is also load-bearing: the test suite reads this exact file as its
     loader fixture, and `docs/40 - DevDocs/taxonomy-authoring-a-trade-def.md`
     walks through it line by line. If you change the shape of a strategy
     note, change it here first. -->

A range that holds while the day's leg structure stays intact tends to
resolve in the direction of that structure. This example takes the break
of a micro range that formed inside the upper third of the day's range,
with the stop under the range base.

## Rules

Anatomy only. Nothing here is a trading recommendation.

## My rulings

(A trader's own notes live here. Cobalt never writes in this section.)

## Definition
<!-- cobalt:section definition -->
<!-- cobalt:unit trade_def:example-range-break -->
```yaml
# The def carries NO `id:` and NO `name:` — both come from this note's
# frontmatter (`trade_def:` is the id, `name:` is the display name) and
# the loader injects them. A unit that authors either fails loud.
trade_def:
  aliases: [Example Break]
  family: [range_break]
  class: scalp
  valid_setups:
    - {setup_ref: range_break, relation: with_trend}
    - {setup_ref: volatility_in_range, relation: with_trend}
  tf_ceiling: 15
  entry_mode: front_side
  preconditions:
    - expr: "Range(micro).instantiated"
    - expr: "Range(micro).duration IN cfg(example_range_break.range_duration_band) min"
    - expr: "Range(micro).low >= DayRange.upper_third"
    - text: "the leg into the range did not end in a full retrace"
  radar_watch:
    - expr: "Range(micro).wick_ratio <= cfg(range.wick_ratio_max)"
  trigger:
    type: range_break
    params: {ref: "Range(micro).bound"}
    confirmation_policy: {type: intrabar}
  stop:
    placement:
      type: structural_extreme
      ref: range_base
      buffer: {type: fixed, cents: {value: "cfg(stop.buffer)", dynamic: false}}
      floor: config
    evaluation: touch
  stop_management:
    - type: fixed
      "on": {name: entry}
    - type: breakeven_at
      r: 1.0
      "on": {name: exit_leg, n: 1}
  exit:
    - fraction: 0.5
      target_type: rr_multiple
      params: {r: 1.0}
      evaluation: touch
      computable: cobalt
    - fraction: 0.5
      target_type: trail
      evaluation: touch
      computable: cobalt
  trail:
    mode: select
    "on": {name: exit_leg, n: 1}
    conditions:
      - {type: prior_bar_break, n: 1}
      - {type: ma_close, ma: {value: "ma.fast", dynamic: false}}
  on_cic: {triggers: [1, 2, 3, 4], action: exit_all}
  max_attempts: {value: 2, dynamic: false}
  reentry_window: {value: "3 min", dynamic: false}
  add_policy: {type: none}
  avoid:
    - expr: "Extension(day).state == exhausted"
  quality_factors:
    # A bare string takes every default (source: human, tier: judgment,
    # frontier: false, status: stub) — which is what most factors are
    # until the grading engine fills in a why_template.
    - range_duration
    - range_height_vs_day_range
    - break_bar_volume_vs_prior
    # A mapping is for a factor that has earned an attribute. `frontier`
    # marks a human-only tape read that flips to source: cobalt the day
    # an L2/T&S feed is ingested — no schema change (§12).
    - {name: tape_absorption_at_bound, source: human, tier: judgment, frontier: true}
    # The standard trio every def carries.
    - setup_relation
    - market_alignment
    - sector_alignment
  preferred_windows: [morning]
  preferred_windows_ref: "anatomy: the micro range needs a formed day range"
```
<!-- /cobalt:unit trade_def:example-range-break -->
<!-- cobalt:unit tunables:example-range-break -->
```yaml
# This trader's OWN rows for this trade — user data, loaded into
# "user".tunables. A separate unit from the def on purpose: replay writes
# a row's `status`, and a status write that re-rendered the Definition
# unit would rewrite the def and every comment in it.
#
# Scope must be per_trade(<trade_key(slug)>) — kebab is illegal in the
# §13.1 key grammar, so `example-range-break` spells `example_range_break`.
# A row here may only ADD a key; shadowing an engine key in
# configs/cobalt/taxonomy/tunables.yaml is a loud collision.
tunables:
  - key: example_range_break.range_duration_band
    value: [4, 20]
    unit: min
    scope: per_trade(example_range_break)
    dynamic: true
    status: proposed
    source: ruling
    consumers: ["preconditions: Range(micro).duration band"]
```
<!-- /cobalt:unit tunables:example-range-break -->
<!-- /cobalt:section definition -->

## Instances
```dataview
TABLE date, side, result_r, grade FROM "1 - Trading/2 - Trades"
WHERE trade_def = "example-range-break" SORT date DESC
```

## Stats
<!-- cobalt:section stats -->
<!-- cobalt:unit stats:example-range-break -->
n: insufficient data (n<30)
<!-- /cobalt:unit stats:example-range-break -->
<!-- /cobalt:section stats -->

## Notes & research
