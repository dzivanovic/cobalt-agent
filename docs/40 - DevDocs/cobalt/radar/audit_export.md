# `src/cobalt/radar/audit_export.py`

## What it does
`cobalt radar audit-export --run <id> | --replay <date> --out <dir>` writes the frozen L52-d audit bundle (S2-P2 STEP-11; R11). Another house (network off, its own checker) recomputes `card_score` and every dot from it; a mismatch blocks enable. This module produces the bundle and nothing else.

## The bundle
One canonical JSON file each (sorted keys, 2-space indent, trailing newline):

| file | `--run` | `--replay` |
|---|---|---|
| `bars.json` | per member: closed i1 rows consumed, daily rows, RVOL (rebuilt from the receipt chain) | per admitted member: the day's stored i1 rows and cached daily rows; no RVOL |
| `settings.json` | the receipt's settings snapshot (card keys, mode, sheet, enabled keys) | the current card settings |
| `tunables.json` | the receipt's tunable rows + defaults | the merged rows read + defaults |
| `ast.json` | per def: preconditions / avoid / radar_watch with `expr`, parsed AST (`node` = type name) and required atoms; quality factors | same |
| `definitions.json` | the definitions as evaluated | same |
| `cards.json` | published card rows (entry, stop, taps, published numbers); a dark run says so with an empty list | CANDIDATE rows per first-seen formation (`published: false`): detail, observations, dots against current curves, null conviction/score |
| `seam.json` | the `radar_score_run` row, its `radar_score` rows, the pool unit | scans, evaluation counts, not-evaluable defs, path-B-only lines |
| `receipts.json` | the receipt chain, verbatim | — |
| `formulas.json` | formulas in words (card_score, conviction, proximity, dot grade, suppression, proposed key, desk dots), `formula_sha256`, per-file source sha256, and whether the run's formula hash matches the current code | same, no run hash |
| `manifest.json` | sha256 of every file, `bundle_sha256` (of the canonical file→hash map), hashes, self-check, notes | same, no self-check |

## Key functions/classes
- `export_run(run_id, *, radar_store, card_store, out, clock, generated_at)`:
  1. the run must exist and be `complete`, and must have exactly one receipt (`card_store.receipt_for_run`); else refuse;
  2. resolve the receipt chain's snapshots and rebuild the members (`evaluate.rebuild_members`) — a chain that does not verify refuses;
  3. re-derive `tunables_sha256`, `settings_sha256`, `cohort_sha256` and `pool_unit_sha256` from the retained VALUES and compare with what the run stored — any mismatch refuses;
  4. `evaluate.replay_receipt` must reproduce every published card number and every seam evaluation label — otherwise refuse ("Cobalt's replay disagrees"); a bundle Cobalt cannot reproduce is not handed to another house;
  5. write.
- `export_replay(day, *, pool_key, slug_filter, radar_store, defs_source, daily_source, tunables, defaults, settings_values, clock, out, generated_at)` runs `evaluate_cli.replay_formations` (writes nothing), re-evaluates each formation at the scan it was first seen, and bundles candidates.
- `ast_payload`, `formulas_payload`, `BundleManifest`, `add_arguments`, `command`.

## Frozen
`_write_bundle` builds every blob in memory first, refuses an `--out` that exists and is not an empty directory, then writes. Every refusal above happens before the directory is created.

## Config it reads
`--run`: nothing current — only stored rows. `--replay`: radar config (pool key, cache dir), loaded trade_defs, engine tunables/defaults, trader settings.

## Gotchas
- Runs audited before D2 are dark or carry null scores (curves unset); the enable gate needs the candidate-harness run (`radar evaluate --candidate` on cobalt_dev, Astra R1-11) exported with `--run`.
- The bundle carries the trader's definitions and settings (user data): it belongs in a gitignored scratch path, never in a commit.
