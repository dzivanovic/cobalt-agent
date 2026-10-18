## §0 Headline
Card 503 gains row FIX1 (DECISION W fix round): the live-test skip joins DEPLOY-HUB STEP-G (c) and `gate-lists.md` ALLOWED SKIPS; the test file is checked on the LIVE-NOTE line and for no printed note text.
Continue step after the row: W again, then the check, then the deploy. BASE, TIP, CHECK REPORT, HOUSE B untouched.
Part 2 is already in the builder's tree (P8): the row says verify once, add only if absent.
Commit nothing.

## DECISIONS
- ASK DESK: part 2 (test file appended to the LIVE-NOTE line) is already done in the worktree `ops/desk/gate-lists.md:45` by P8; the row says verify it, add only if absent. Default: as written [08:52]
- ASK DESK: part 3 needs no edit (the test already asserts names, counts, mtime snapshot, no print); the row makes the builder quote the check and edit only on a hit. The run prints draft slugs (note file names, not text) to captured stdout via `render`. Default: kept [08:52]
- ASK DESK: `tests/ops/test_gate.py:307-312` requires every word of the new ALLOWED SKIPS item on the hub's STEP-G (c) line; the row names this so the two edits match. Default: the item `tests/cobalt/test_playbook_live.py test_live_vault_renders_six_decks COBALT_LIVE_VAULT_ROOT not set` [08:52]

## RECORDS
- `git diff --stat main -- ops/desk/gate-lists.md "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "…/503-f23-card.md"` → empty (tree equals main `7258e6b8`) [08:44]
- `gate-lists.md:44-45`, `:53-54`; `DEPLOY-HUB.md:98`, `:104`, `:109`; `tests/ops/test_gate.py:307-312`; `ops/desk/gate.sh:647-656` read [08:46]
- Build report `:6`, `:79`, `:110`, `:183`, `:236`; worktree `gate-lists.md:45`, `test_playbook_live.py:19-32,62-71` read [08:48]
- Card 503 edited: row FIX1 after D0, three `## RECORDS` lines before the `DB` line [08:50]

DRAFTED · decisions: 3
