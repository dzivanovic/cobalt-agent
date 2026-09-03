# ADR-0003 — taxonomy schema v0.4: one-stop trail slot, tunable registry, class definitions

Date: 2026-09-02
Status: Accepted

## Context

TAXONOMY-DRAFT-v0_7.md (FINAL, §14 collisions 1–2 RULED 09-02) folds
Batch 2's §A amendments into the base draft and rules three further
items that touch schema, not just data: the **one-stop law** (§14 c.1
— a trade has exactly one stop at any moment; `trail` collapses from a
retrofit exit-target shape plus a `stop_management: trail_ma_close`
ladder entry into ONE top-level slot), the **tunable registry** (§13.1
— every `config, dynamic` quantity becomes a row with `status`/`source`/
`replay` tracking instead of a bare literal inside an unparsed
`Predicate.expr` string), and **class definitions** (§14 c.2 — A.10
"trailing exit ⇒ move2move" and v0.6's "scalp = one leg out" are
STRUCK; `class` is trade shape + horizon, never exit mechanics or leg
count). Schema version bumps v0.3 → **v0.4** (v0.7 change log #23).

Same config-as-code decision as ADR-0001/ADR-0002: this is a schema +
data migration on top of the existing 13 trade_defs (Batch 1 + 2,
committed 00ff853 / 2b96611), not an engine sprint — no predicate
parser, no setup detectors, no bar logic; the old `cobalt_agent` tree is
untouched (strangler rule).

## Decision

- **`TradeDef.trail: TrailSpec | None`** — ONE slot per trade_def
  (`src/cobalt/taxonomy/trade_def.py`). `TrailSpec {conditions[]
  (existing `PriorBarBreakCondition` / `MaCloseCondition` /
  `VwapCloseCondition` / `LevelCondition` union, unchanged), mode:
  "select" (not "any" — v0.7 §10.2 explicitly supersedes A.8's
  first-to-fire), on: EventRef (default entry)}`. `PriorBarBreakCondition.n`
  is now `Literal[1] = 1` (pinned, not merely defaulted — the 1-bar
  trail law, v0.7 §0, applies wherever a bar trail is expressed).
- **`ExitLeg.target_type == trail` takes NO params.** A `model_validator`
  raises if `params` is non-empty for a trail leg; a second,
  `TradeDef`-level `model_validator` raises if any exit leg is
  `target_type=trail` while `trade_def.trail is None` — the trail slot
  is now the single source of the trade's trail conditions, never a
  per-leg copy.
- **`trail_ma_close` / `trail_bar` REMOVED from `StopManagementType`**
  (and their model classes `TrailMaCloseMgmt`/`TrailBarMgmt` deleted
  from the `StopManagementEntry` union); **standalone `ma_close` REMOVED
  from `ExitTargetType`.** All three were duplicate spellings of the
  trail slot (v0.7 change log #11, #18). A `TradeDef.model_validator(mode="before")`
  scans the raw `stop_management[]` / `exit[]` dicts for these three
  spellings BEFORE Pydantic's discriminated-union parsing runs, so the
  failure names the trail slot directly ("stop_management.type=... was
  REMOVED... express this trade_def's trail as trade_def.trail
  instead") rather than surfacing Pydantic's generic
  not-a-valid-discriminator-value message. `on_cic.tighten_to:
  "trail_bar"` is UNCHANGED — a distinct semantic (switch the stop to
  the 1-bar capability), not the removed stop-management type.
- **Tunable registry** — new `src/cobalt/taxonomy/tunables.py`
  (`TunableRow`: `key, value, unit (bars|min|atr|cents|count|pct|ratio|
  label|duration), scope (global | per_trade(<id>) | per_indicator(<ind>),
  regex-validated), dynamic, status (proposed|replay_pending|
  solidified|overridden), source (ruling|sheet|dwv), sheet_value?,
  consumers[], replay?`; `TunableRegistry` with a unique-key
  model_validator; `replay_backlog(registry)` = `[row for row in
  registry.tunables if row.dynamic and row.status != solidified]` — the
  §13 backlog as a query, not a hand-maintained list) +
  `configs/cobalt/taxonomy/tunables.yaml`, seeded with the 30 §13.1-table
  rows whose `dyn` column is `yes`. The three non-dynamic globals the
  table also lists (`working_timeframe`, `ma.fast`/`ma.slow`,
  `stop.buffer`) are deliberately excluded — §13.1's own text says they
  "stay in defaults.yaml as already built"; **`stop.buffer` is not
  actually a `defaults.yaml`/`TaxonomyDefaults` field** (it is a
  Pydantic field default on `StopBuffer.cents`, `trade_def.py`) — flagged
  here rather than silently adding a new defaults.yaml field the task
  didn't ask for; `resolve_cfg` does not special-case `stop.buffer`.
  `catalyst.grade_min`/`_max` and `<trade>.max_attempts`/
  `<trade>.reentry_window` (both `dyn: no` in the table) are also
  excluded from `tunables.yaml` — they stay exactly where they already
  lived, as `Tunable[T]` fields directly on their trade_defs.
- **`loader.resolve_cfg(key, tunables, defaults)`** — the ONE `cfg(key)`
  resolver: `tunables.yaml` row first, else `defaults.yaml`'s
  `working_timeframe` / `ma.fast` / `ma.slow` (via the existing
  `is_ma_ref`/`resolve_ma_ref`), else `TaxonomyConfigError`.
  `loader.iter_cfg_tokens(obj)` token-scans (regex `cfg\(([a-zA-Z0-9_.]+)\)`,
  no grammar parsing) every string reachable from a loaded `TradeDef`;
  `load_trade_defs()` calls `resolve_cfg` on every token found and fails
  loud, naming the file and trade id, on an unknown key.
- **Predicate/param data migration**: every place a §13.1 dynamic
  quantity appeared as a bare literal with a `# config` comment (e.g.
  `Range(micro).duration >= 45 min  # config, dynamic`, `pivots: 2  #
  config`) is rewritten to `cfg(<key>)` referencing the matching
  `tunables.yaml` row (`big_dog.range_duration_band`,
  `trendline.min_pivots`, `range.wick_ratio_max`,
  `gap_give_and_go.range_duration_band`, `gap_retrace_pct_max`,
  `range.counter_pivot_min`, `bella_fade.near_low_duration_max`,
  `dist.k.vwap`, `flat_threshold.ema9`/`.vwap`, `rubberband.bars_cleared`,
  `big_dog.bar_break_reverse_bars`, `gap_give_and_go.bar_break_reverse_bars`).
  Already-structured `Tunable[T]` fields (`TimeStopMgmt.duration_bars`,
  `max_attempts`, `reentry_window`, stop-buffer cents, ma refs) are
  **not** rewritten into `cfg()` strings — they are not predicate/param
  *strings* (the loader's token-scan is explicitly scoped to strings),
  and converting a typed `Tunable[int]` field into a bare string would
  be a bigger, unrequested type change. `tunables.yaml` still carries
  rows for the matching quantities (`backside.time_stop_bars`,
  `back_through_open.time_stop_bars`, `bouncy_ball.time_stop_bars`) as
  the canonical status/replay bookkeeping layer, decoupled from — not a
  duplicate authority over — the trade_def's own structured field.
- **`trail_fit` registry variable** added to `quality_factors[]` (and
  the matching `variables/<id>.yaml` entry, `source: cobalt, tier:
  deterministic`) of every trade_def carrying a `trail` slot:
  `second_chance`, `rubberband`, `vwap_continuation`, `ema9_scalp`,
  `back_through_open`, `bouncy_ball` (v0.7 §0 — "which capability the
  stock cleanly follows = registry variable trail_fit, cobalt-computable
  from bars"). The loader's existing quality_factors ⇔ variable-registry
  cross-check (ADR-0001) enforces both sides stay in sync.
- **Class definitions** (`TradeClass` docstring, `trade_def.py`) —
  replaced with v0.7 §0's wording verbatim: trailing vs hard exit
  defines no class, legs-out count defines no class; `scalp` = usually
  sub-15-min TF, seconds to ~45 min (`tf_ceiling: 15` the only hard
  constraint); `move2move` = a defined entry/stop/target on a momentum
  move surviving consolidation to a further target, usually 5-min+, an
  intraday swing. Enum values unchanged; all 13 populated `class`
  assignments stand (§12 population status, unchanged). Scope note: this
  ADR's docstring/enum-comment/DevDocs rewrite is a code+docs change
  only ("no data changes" per the population task) — four trade_def
  YAML files (`ema9_scalp`, `vwap_continuation`, `bouncy_ball`) had their
  `class:` line comments cleaned up as an incidental byproduct of
  editing those same files for the trail migration above (not a
  separate pass); `first_vwap_pullback.yaml`'s `# single target, one leg
  out` comment was left untouched — flagged, not silently reworded,
  since it wasn't otherwise being touched this commit.
- **`SCHEMA_VERSION = "0.4"`** constant added to `trade_def.py` (no
  prior constant existed to bump — `git blame`/ADR-0001/ADR-0002 only
  ever carried the version in docstrings; this ADR introduces the first
  literal constant).
- **`StructuralRef` docstring** gains the `Range(micro).top` / `.base`
  parametrized-ref note (ADR-0002's `Range(micro).top`
  precedent, now generalized and cited from the enum itself).
- **ruff** added as a dev dependency (`pyproject.toml`
  `[dependency-groups].dev`), minimal `[tool.ruff]` config
  (`line-length = 100`, `target-version = "py311"`), run scoped to
  `src/cobalt/taxonomy tests/taxonomy` only (not repo-wide) —
  `ruff check src/cobalt/taxonomy tests/taxonomy` is clean.

## Consequences

- The 13 committed trade_defs (Batch 1 + 2) all re-validate under
  schema v0.4 with no trade dropped and no `class`/`family`/
  `valid_setups[]` change — `python -m cobalt.taxonomy.validate` still
  reports 13/13 and now also reports the tunables/backlog counts.
  `big_dog` and `gap_give_and_go` carry no `trail` slot (their
  move2move exits are `bar_break_reverse` targets, not trails — the
  1-bar trail law explicitly leaves double-bar move2move exits
  untouched, v0.7 §0).
- The setups engine (predicate grammar parser, `cfg()` resolution at
  runtime, trail-capability selection logic) can be built against this
  schema without another data migration — the trail slot, the tunable
  registry, and the `cfg(key)` token convention are load-bearing now,
  not placeholders.
- `docs/00 - Project/BACKLOG.md`'s "Taxonomy replay validation" section
  is now a pointer to `tunables.yaml` / `replay_backlog()` instead of a
  hand-maintained itemized list — future dynamic quantities are added
  as tunable rows, not as new BACKLOG.md bullets.
- ADR-0002's trail-related decisions (exit-target `trail` with
  `mode: "any"` and per-leg `TrailExitParams`, the `trail_ma_close`
  Batch 2 retrofit) are **superseded by this ADR for trail** — noted at
  ADR-0002 directly.
