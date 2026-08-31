# `src/cobalt/prefill/trade_note.py`

## What it does
Creates/updates "1 - Trading/2 - Trades/&lt;Trade-...&gt;.md" for every
computed ASET card, using the Individual Trade Template's frontmatter
shape, so the daily note's Trade Execution dataview table lights up.
Cobalt owns exactly five frontmatter fields (date, symbol, direction,
stop_price, entry_price); everything else (exit_price, entry_time,
exit_time, profit_loss, strategy, RVOL) is created blank and, on any
later re-run against the same filename, is read back and preserved
verbatim — only the five owned keys refresh. RVOL is always blank
today: ASET's sizing engine doesn't fetch it (see `aset/prefill.py`),
so blank is the honest state, not a guess.

## Key functions/classes
- `upsert_trade_note(result, when, prefill_paths) -> (Path, "created" | "updated")`.
- `_cobalt_fields`, `_render_frontmatter`, `_render_body` — pure formatting.
- `_split_frontmatter(content) -> (dict | None, body_str)` — YAML
  frontmatter parse for the update path; `None` fm on a file with no
  recognizable frontmatter block raises `VaultWriteError` rather than
  guessing how to merge into it.

## Data flow in/out
**In:** an `aset.models.SizingResult` + its card timestamp + the
resolved trades directory (`vault_writer.resolve_target`). **Out:** a
created or in-place-frontmatter-updated file, or `VaultWriteError`.

## Config it reads
`configs/cobalt/prefill.yaml` (trades_dir, trade_filename_pattern) via
the caller-supplied `PrefillPathsConfig`.
