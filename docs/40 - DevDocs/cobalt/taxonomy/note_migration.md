# `src/cobalt/taxonomy/note_migration.py`

## What it does
The ONE-OFF that puts the strategy notes into the ADR-0008 D3 shape:
`cobalt taxonomy migrate-strategy-notes --dry-run|--apply`. Three edits
per note, all through `VaultWriter` (L28) — the definition unit, an
optional tunables unit, and the frontmatter.

## Key functions/classes
- `edit_definition_unit(body, fm_name=, registry=)` — drops `id:`/`name:`,
  appends the old YAML name to `aliases[]` where it differed, folds the
  variable registry into `quality_factors[]`.
- `edit_frontmatter(lines, trade_class=, families=)` — `category:` out
  (only if blank), `class:`/`family:` in after `name:`.
- `lift_per_trade_rows(...)` — moves `per_trade(...)` rows out of
  `tunables.yaml` into their notes, comments and all.
- `add_alias_to_unit(body, alias)` — idempotent, one line edited.
- `plan_notes(...)` / `apply_plans(...)` / `migrate_strategy_template(...)`.

## Textual, never a re-serialisation
`yaml.safe_dump` would reorder keys, drop every comment a human wrote
beside a rule, and re-flow every block. The rule is "touch the lines that
change and no others", and the tests assert it.

## It proves itself
Every populated note's canonical md5 is compared before and after with
`id`/`name` stripped and `quality_factors` reduced to names — the
pre-deletion proof's canonicalisation. `aliases[]` is asserted exactly
rather than hashed, because ruling e changes that list on purpose. Any
drift fails the whole run before a byte is written.

## Where its inputs come from
The setup×trade matrix and the variable registries were deleted with the
YAMLs; the per-trade tunable rows left `tunables.yaml` in the same
sprint. All are read out of git at a named revision — they are user data,
and putting them back in the working tree would undo the deletion. The
matrix file is FOUND rather than named (its filename carried a person's
name, L31).

## Gotchas
Ruled pairings that no rule derives arrive as arguments —
`--matrix-alias`, `--tunable-alias` — so the ruling is recorded in the
run's report, not written into this repo.
