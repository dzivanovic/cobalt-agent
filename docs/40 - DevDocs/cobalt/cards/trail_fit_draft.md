# `src/cobalt/cards/trail_fit_draft.py`

## What it does
`cobalt cards trail-fit-draft [--out <file>]` — writes a review DRAFT of the `trail_fit → source: human` note change and nothing else (S2-P2 STEP-8; ruling R5).

Why: notes declare `trail_fit` as `source: cobalt`, but S2 has no computer for it, so the dot is N/A (`MANUAL`) and, untapped, suppresses `card_score`. R5 rules the fix is the trader's hand in his own notes; Cobalt drafts, never applies. There is no apply command in P2, and this module holds no vault writer.

## Key functions/classes
- `draft_trail_fit(vault_root, *, today) -> TrailFitDraft` reads every defined note whose def carries `trail_fit`, finds the item by line (`taxonomy.factor_lines`) and produces a `DraftRow`: the current item lines, the proposed single-line flow mapping with `source: human` (every other key kept), and whether that proposed item validates as a `QualityFactor`. A factor already `source: human` is listed as such with no proposal. No note carrying `trail_fit` at all is a loud `TrailFitDraftError`, never an empty draft.
- `render_draft(draft)` — markdown headed DRAFT, one section per def.
- `write_draft(vault_root, out, *, today)` creates the file exclusively; an existing file is refused. The CLI default is `docs/40 - DevDocs/reports/trail-fit-draft-<ET date>.md`.

## Config it reads
The vault through `load_vault_trade_defs` (and so the engine tunables).

## Gotchas
The test `test_trail_fit_draft_never_applied` asserts that no note byte moves, that the module source names no `VaultWriter`/`upsert`, and that `cobalt cards` has no other trail command.
