# Adding a setup — definitions are data, the bricks are code

A setup is a **definition** in a strategy note; the radar evaluates it with the bricks below, and **no source line names a setup** (the Lego test, `tests/cobalt/test_setups_lego.py`). Adding one is writing a note, never a code change — until it asks for a brick that does not exist.

## Where a definition lives

- The note: `1 - Trading/4 - Strategies/<note>.md` in the vault. Frontmatter `trade_def: <slug>` and `name:`.
- The `<!-- cobalt:section definition -->` section holds the `trade_def:<slug>` unit (YAML, the `TradeDef` schema) and, optionally, the `tunables:<slug>` unit — its own per-trade rows (`vault_loader.py:10-49`).
- A definition carries: `valid_setups` (setup refs + relation), `preconditions` and `avoid` (predicates: `expr` for the radar, `text` for a human read), one `trigger`, one `stop.placement`, exits, trail, `quality_factors`, preferred windows.

## Where its dials go

- Its own numbers: its `tunables:<slug>` unit, keys `<trade_key>.<field>`, scope `per_trade(<trade_key>)`.
- Engine rows: `configs/cobalt/taxonomy/tunables.yaml` — anatomy keys only; a new key lands `value: null`, `status: proposed`. Never a trader's number.
- An assumed default: `1 - Trading/Assumed Defaults.md`, unit `tunables:assumed`, `source: assumed` until the owner rules it (`ruling`). It fills an engine hole only of the same scope and unit (`per_indicator` holes stay null — F1). A formation on an assumed key carries the untappable `assumed_formation` dot and no score.

## How to check it before it goes live

1. `cobalt taxonomy validate` / `cobalt taxonomy load` — the note parses and loads.
2. `cobalt taxonomy tunables --assumed` — every assumed row and who consumes it.
3. `cobalt radar evaluate` — the dry-run prints each def's evaluability line.
4. `cobalt radar evaluate --replay <day> --trade-def <slug> --expect-formed` — it forms on a stored day.

## Discoverable or not

No per-setup switch exists. The only switch is the global `radar.cards_enabled` (`settings/card.py:63`). A per-setup switch is an OPEN ITEM for the owner / tribunal (build report, ESCALATE).

## When a definition asks for a brick that does not exist

`registry.evaluability` names it and the def is `not_evaluable` — "this needs a build, a feature for later": an atom verbatim · a relation word · `trigger:<type>` · `stop:<type>[:<ref>]` · `<atom>∌<value>` (a symbol outside the atom's domain) · `Unsupported(<shape>)` (a shape the interpreter cannot evaluate).

## The bricks

The ONE place each brick is registered (`cobalt.radar.formation`); a new brick is one row there.

### Triggers (`TRIGGERS`)
- `bar_break` — `{bars_cleared}`: clears the last n working bars.
- `range_break` — `{ref: Range(micro).bound | .top}`: the micro-Range's trade-side bound.
- `indicator_cross` — `{a, b, direction}`: the latest cross; stamps `cross_point`.
- `indicator_rejection` — `{indicator, contact}`: the last bar touches and closes back through.
- `trendline_break` — `{ref: Level_ref(trendline), anchor_leg, pivots}`: flat case = the micro-Range top.
- `sequence` — break close-through → retest → a close above the prior bar.

### Stop placements (`STOPS`)
- `structural_extreme` — a structural ref, less `cfg(stop.buffer)`, nudged off round prices.
- `measured_fraction` — `anchor_a − fraction × (anchor_a − anchor_b)`; `entry` = the trigger price.
- `indicator` — the indicator's value at entry (`snapshot: at_entry`).

### Structural refs (`STRUCTURAL_REFS`)
- `snapback_candle` — the move's tracked extreme.
- `turn_low` — the same object.
- `consolidation_low` — the micro-Range base.
- `range_base` — the same object.
- `recent_higher_low` — the latest pivot low inside the micro-Range.
- `turn_candle` — the low of the break-retest-turn bar.

### Relations (`RELATIONS`)
- `between` — `flat(<ind>, window) between turn and cross`.
- `touched` — a leg's extreme reached an indicator.
- `on` — `<Extension atom> on Leg(pre_test)`; `event(retest) on that RangeBreak`.
- `after` — a RangeBreak state after `event(retest)`.
- `inside` — `price inside Range(prior)`.

### Atoms (`ATOMS`)
- `price` · `EMA9` · `EMA21` · `EMA9.slope` · `slope_norm(EMA9)` · `slope_norm(VWAP)` · `VWAP` · `ATR(working_tf)` — seeded from the premarket.
- `DayRange.high` · `DayRange.low` · `DayRange.upper_third` · `PMH` · `PML` · `PDH` · `PDL` — session levels.
- `InPlay.state` — pool admission.
- `catalyst_ref` — THE ONE BRICK THAT STANDS IN FOR MISSING DATA (`A-13`): read from the pool admission, always marked assumed.
- `Extension.state` · `Extension.instantiated` · `Extension.leg_count` — the Extension and its lifecycle.
- `RangeBreak(HTF).day_count` — the daily range break.
- `Range(micro).instantiated` · `Range(micro).duration` · `Range(micro).low` · `Range(micro).top` · `Range(micro).base` · `Range(micro).bound` · `Range(micro).height` · `Range(micro).wick_ratio` — the micro-Range.
- `Leg(opening_drive).direction` · `Leg(opening_drive).terminated_by` · `Leg(pullback).direction` · `Leg(pullback).end` · `Leg(pullback).index` · `Leg(impulse).direction` · `Leg(opening_drive OR impulse).direction` — leg roles.
- `Level_ref(resistance).rejected` — the level set's rejection.
- `RangeBreak(level).state` · `RangeBreak.state` · `event(retest)` · `event(stop_hit)` — the level break lifecycle.

Also served as values, not atoms: `trade_direction`, `opposite(x)`, `against(x)`, `dist(a, b)`, `null`, `cfg(<key>)`, `<atom> IN cfg(band) <unit>`, `*` and `/`.

## Worked example — the eighth definition

`example-lego-eighth` (built in `tests/cobalt/test_setups_lego.py` from data alone): preconditions `InPlay.state == active`, `price > EMA21`, `Range(micro).instantiated`; trigger `bar_break {bars_cleared: 3}`; stop `structural_extreme` on `range_base`. No def of the corpus combines these. It loads, `evaluability` is True, and it forms long on a drive-then-range series — and does not form on the same series cut before the range. No source changed.
