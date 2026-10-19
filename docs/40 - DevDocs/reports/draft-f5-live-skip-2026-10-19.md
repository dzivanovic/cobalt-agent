## §0 Headline
- Card 731 has a FIX1 row for DECISION W; edited in place, nothing committed.
- Skip `test_dry_run_finds_the_heading_in_real_notes` (`COBALT_LIVE_VAULT_ROOT not set`) goes to `DEPLOY-HUB.md` `:104` and `## ALLOWED SKIPS`; the file goes to the LIVE-NOTE line; the live test already prints no note text.
- Continue step after the row: `W`, then the check, then the deploy.
- One ASK DESK: the L9 other-house read.

## DECISIONS
1. ASK DESK: the prompt names an L9 other-house read at change "as 503 had it"; card 503's FIX1 row and records carry none (only `HOUSE B: as needed` in its header). The row says the read happens at change and `HOUSE B` stays mandatory and the desk's; no further text. Default: the desk runs the L9 read at the change, as the header's `HOUSE B: mandatory — vault notes` already requires. [09:04 EDT]

## RECORDS
- Card edited: `prompts/2026-10-18/731-f5-card.md` — row `FIX1` after `D0`, `ORDER` tail, three `## RECORDS` lines. BASE, TIP, CHECK REPORT, HOUSE B untouched. [09:04 EDT]
- `git -C /Users/cobalt/cobalt rev-parse main` → `42d456ab44895016452834348cb816fddfe15402`. `git diff --stat main` over `ops/desk/gate-lists.md`, `DEPLOY-HUB.md`, `ops/desk/gate.sh`, `tests/ops/test_gate.py` → empty. [09:03 EDT]
- Reads at `main`: `gate-lists.md` `:44-45`, `:53-54`; `DEPLOY-HUB.md` is `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (not the repo root), `:104` holds the `test_live_vault_renders_six_decks` clause and no `test_checkpoints_live`; `gate.sh:647-656`; `tests/ops/test_gate.py:307-312`.
- Reads in the worktree: build report `:7`, `:210`, `:232`; worktree `gate-lists.md:45` already ends with `test_checkpoints_live.py` (builder's); `:54` lacks the item; `tests/cobalt/test_checkpoints_live.py` read whole (59 lines): skip `:24-26`, decorator `:36`, no `print`/`capsys`/`caplog`, messages name an index.
- Time source: `date` → Mon Oct 19 09:04:22 EDT 2026.

DRAFTED · decisions: 1
