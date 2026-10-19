# draft-469-fix-round — 2026-10-19

## §0 Headline
- Added row F1 to card 469 (`prompts/2026-10-13/469-f21-vectors-card.md`): fix O1 in `load_agent` (`voice/registry.py`, `isinstance(..., Route)` guard) and drop the strict xfail at `test_voice_config.py:358`.
- `src/cobalt/voice/registry.py` is named in F1 as a one-line `files` addition; the FIXED line is in the row; CHECK ASKS X4 added; RECORDS line added.
- G1 and G2 are not written as SETTLED lines (`ASK DESK` below). Nothing committed.

## DECISIONS
- ASK DESK: G1 and G2 (REJECTED, not held): the check's `## OPEN` says each "settles by a desk SETTLED row" and describes what it confirms, but gives no SETTLED text itself. Default taken: no SETTLED line on the card; one CHECK ASKS line points here. [19:31]
- ASK DESK: the exact `AgentConfigError` message and the `Route` import path. The row names `cobalt.modelaccess.config.Route` (not exported by `modelaccess/__init__.py`) and leaves the message to the builder. Default taken: that import, lazy beside the existing one at `registry.py:99`. [19:31]

## RECORDS
- `date` → Mon Oct 19 19:31:30 EDT 2026.
- `git rev-parse ops/f21-vectors-1013` → `c678dda0eae9222e82cd1d13f75074a4f13f9b3e`.
- Read via `git show ops/f21-vectors-1013:<path>`: `voice/registry.py` (`:85`, `:99`, `:101`, `:102`), `modelaccess/config.py` (`:43`, `:47`, `:99`, `:110`, `:178`), `modelaccess/__init__.py`, `tests/cobalt/test_voice_config.py` (`:14`, `:358`, `:359-361`). Line numbers confirmed by Grep on the worktree `cobalt-wt/f21-vectors-1013` at the same tip.
- Also read: the card, the check report, `830-draft-f16-fix-round.md` and the card 790 FIX1 row (form).
- BASE, TIP, CHECK REPORT, HOUSE B, BAND untouched.

DRAFTED · decisions: 2
