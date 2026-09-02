# ADR-0001 — trade_defs and variable registries are YAML data, Pydantic-validated on load

Date: 2026-09-02
Status: Accepted

## Context

TAXONOMY-DRAFT-v0_6.md §10.1 (schema v0.3) defines the `trade_def`
registry shape. TRADE-DEFS-BATCH1-v0_1.md §B populates six trade_defs
(Hitchhiker, Big Dog, Second Chance, Back$ide, Fashionably Late,
Rubberband) from full SMB cheat sheets, plus the Cameron H grid (§C, 21
trades) as `valid_setups[]` data.

This is a data + schema commit, not an engine sprint (TRIAGE / CLAUDE.md
strangler rules: "never build a massive codebase ahead of testing and
approval"). No predicate parser, no setup detectors, no bar logic exist
yet — the setups engine that consumes this data is a future sprint.

## Decision

- `trade_def` and its per-trade variable registry live as YAML data
  under `configs/cobalt/taxonomy/` (`trade_defs/`, `variables/`,
  `cameron_grid.yaml`), not as Python literals or database rows.
  `configs/cobalt/` is the sanctioned new-core config location for
  shared new-core data (CLAUDE.md's config boundary law; matches the
  existing `configs/cobalt/watchlists.yaml` pattern) — **not**
  `config/taxonomy/` as the population task originally specified,
  since no top-level `config/` directory exists and creating one would
  violate the documented boundary. Flagged in the population report.
- `src/cobalt/taxonomy/trade_def.py` and `variables.py` carry the
  Pydantic v2 schema only. Enums (`Family`, `TradeClass`, `Relation`,
  `EntryMode`, `SetupRef`, `RTHWindow`, `RangeBoundType`, `TriggerType`,
  `ConfirmationPolicyType`, `EvaluationType`, `StructuralRef`,
  `StopManagementType`, `ExitTargetType`, `Event`, `OnCicActionType`)
  are the single source of truth for the taxonomy vocabulary — YAML data
  must match them exactly; an out-of-vocabulary value fails loud, is
  never silently coerced.
- `Predicate.expr` stores the v0.6 §10.5 grammar string UNPARSED.
  Grammar evaluation is deferred to the setups-engine sprint.
- `Tunable[T] = {value, dynamic, note}` marks editable values;
  `dynamic=True` is reserved for the v0.6 §0 "Dynamic definitions" law
  items (consolidation touches, leg=wave alias, Extension A/B
  thresholds, pivot N, Range.duration bands, flat_threshold,
  Range.wick_ratio threshold, break_volume_sigma_bars) and must appear
  in the §13 replay backlog (`docs/00 - Project/BACKLOG.md` § "Taxonomy
  replay validation (v0.6 §13)"). In Batch 1, every such quantity lives
  inside an unparsed `Predicate.expr` string rather than a structured
  `Tunable` field, so no live Batch 1 tunable is currently `dynamic=True`
  — the enforcement test (`tests/taxonomy/test_trade_defs.py::
  test_dynamic_tunables_appear_in_replay_backlog`) stays in place for
  when a future trade_def introduces one.
- `src/cobalt/taxonomy/loader.py` loads + validates every trade_def,
  cross-checking `valid_setups[]` against `cameron_grid.yaml` and
  `quality_factors[]` against the variable registry, entirely on load.
  A bad or missing file raises `TaxonomyConfigError` with file + field
  path — no partial loads, no default fallback (config-as-code law).
  `python -m cobalt.taxonomy.validate` is the CLI entry point.
- **Advisory-exit law** (v0.6 §0 / TRADE-DEFS-BATCH1-v0_1.md §A.15):
  every `on_cic`, `stop_management`, `exit`, and time-stop field this
  schema carries is a warning to the human, never an order — Cobalt
  never executes against a trading platform (CLAUDE.md absolute
  boundary). No part of this commit changes that; nothing here is
  wired to any platform integration.

## Consequences

- The setups engine (predicate grammar parser, detectors, bar-level
  triggering) can be built against this schema without another data
  migration — enums, discriminated stop/stop_management unions, and the
  loader's cross-file checks are already load-bearing.
- Batch 2 (9 EMA Scalp, Back-Through Open, Bella Fade, Bouncy Ball,
  First VWAP Pullback, Gap Give and Go, VWAP Continuation) follows the
  same population + loader pattern once Dejan supplies sheets.
- Mismatches and ambiguities surfaced during Batch 1 population (Second
  Chance's step-2 missing `confirmation_policy`, Rubberband's
  `raise_to.placement: breakeven` shorthand, Fashionably Late's
  `entry_price` vs. the canonical `entry` structural ref) are recorded
  as code comments at their source YAML and in the population report —
  none were silently resolved by inventing a new enum value. All three
  are now CONFIRMED (2026-09-02, TRADE-DEFS-BATCH2-v0_1.md item 0 /
  ADR-0002): Second Chance's optional step confirmation and Rubberband's
  `level{level_ref: entry}` encoding stand as originally written;
  Fashionably Late's `stop.anchor_a` is renamed `entry_price` → `entry`.
