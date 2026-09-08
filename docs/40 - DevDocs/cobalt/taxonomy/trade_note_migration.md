# `src/cobalt/taxonomy/trade_note_migration.py`

## What it does
`cobalt taxonomy migrate-trade-notes --dry-run|--apply [--note PATH]`.
Inserts exactly ONE line, `trade_def: <slug>`, immediately after
`strategy:` in every trade note, through `VaultWriter.upsert_region`.
`strategy:` is left VERBATIM — it is a human's line and it stays one.

## Key functions/classes
- `build_alias_index(vault_root)` — every string that names a trade, read
  from the strategy notes: slug, frontmatter `name:`, the def's (or a
  draft's) `aliases[]`, and any legacy `strategy:` key of its own.
- `normalise(value)` — trim, strip surrounding quotes REPEATEDLY,
  casefold.
- `AliasIndex.match(value)` — the one slug, or None. Two is a loud error.
- `insert_trade_def_line`, `plan_trade_notes`, `apply_trade_notes`,
  `migrate_trade_template`.

## The index is derived from the vault
A trade name is user data, so this module contains none. That also makes
the mapping self-maintaining: add an alias to a note and the next run
matches it.

## Gotchas
The repeated quote-strip is not decorative — the corpus contains a quoted
string inside a quoted string with leading spaces, written by a Templater
dropdown; stripping one layer matches nothing. Interior punctuation is
never touched: `Gap, Give and Go` and `Gap Give and Go` are different
names.

An unmatched value gets an EMPTY `trade_def:` on purpose — a clause-2a
cell a human fills in later, which is a different thing from a note
nobody considered. A note already carrying `trade_def:` is skipped
(idempotent); one with no `strategy:` key is reported, not touched.
