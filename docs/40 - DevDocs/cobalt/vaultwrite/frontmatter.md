# `src/cobalt/vaultwrite/frontmatter.py`

## What it does
The ONE frontmatter reader for the vault: the regex, the split, and the
`locate` helper every `upsert_region` call passes.

## Key functions/classes
- `FRONTMATTER_RE` — `\A---\n(.*?\n)---\n`. `\A`: it is the head of the
  file or it is not frontmatter.
- `split_frontmatter(content)` — `(mapping | None, body)`.
- `frontmatter_span(lines)` — `(0, i+1)`, INCLUDING both `---` lines, so
  a body written back must include them too.

## Why it exists
The same regex was written out twice (`prefill/trade_note.py`,
`prefill/drc.py`) and ADR-0008's vault loader would have been the third
copy. Three parsers of the same bytes is three chances to disagree about
what a note says.

## Gotchas
`None` means no frontmatter block at all — a fact, not an error. A block
that IS present but does not parse as a mapping raises: silently treating
a malformed header as absent is how a note ends up written as if it had
no `trade_def:` key.

READ-ONLY. A frontmatter WRITE goes through `VaultWriter.upsert_region`
and only through it (L28 / ADR-0004).
