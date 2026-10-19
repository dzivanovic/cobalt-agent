# Card 731 FIX1 — preflight (read-only) · 2026-10-19

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <card>`; `git log --oneline -1 -- <card>` | empty; last commit `8efd4f01` (the FIX1 draft commit). Card committed, diff against HEAD empty | OK |
| 2 | `git diff cccdd69f 8efd4f01 -- <card>` | three hunks only: the new `FIX1` row, the ORDER tail, three `## RECORDS` lines. No hunk touches the header (BASE `40e646ed`, TIP empty, CHECK REPORT, HOUSE B) or any other row | OK |
| 3 | `grep -c "«FILL" <card>` | `0` | OK |
| 4 | row adds the skip to the hub: `grep -n "SKIPPED line inside the allowed set" DEPLOY-HUB.md` | `:104` only (`- (c) PASS 1 at 0013 …`); order is `test_predicate.py:262`, `test_live_vault_renders_six_decks` clause, `test_replay_line.py` clause, then x14. No `test_checkpoints_live` yet. The row's slot (after the playbook clause, before the replay clause) exists | OK |
| 5 | `gate-lists.md` on main: `grep -n` for `## LIVE-NOTE`, `## ALLOWED SKIPS` | `:44` and `:45` (pytest line, last file `tests/cobalt/test_playbook_live.py`); `:53` and `:54` (last item `tests/cobalt/test_playbook_live.py test_live_vault_renders_six_decks COBALT_LIVE_VAULT_ROOT not set`). Cites match the row | OK |
| 6 | worktree `gate-lists.md` | `:45` ends `… test_playbook_live.py tests/cobalt/test_checkpoints_live.py` (part 2 is verify-only). `## ALLOWED SKIPS` has no checkpoints item (part 1 needed). The worktree diff against main in this file is 3 lines (LIVE-NOTE, PASS 1, PASS 2 from K12/K13); ALLOWED SKIPS is not among them | OK |
| 7 | `gate.sh:647-656` read | `covered`: item path plus `:` on the skip line, and every other non-`test_` word on it. Item `tests/cobalt/test_checkpoints_live.py test_dry_run_finds_the_heading_in_real_notes COBALT_LIVE_VAULT_ROOT not set` covers `SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — …` (build report `:181`) | OK |
| 8 | `tests/ops/test_gate.py:307-312` read | one hub line holds the marker; every `:`-split word of every ALLOWED SKIPS item must be on it. So the hub clause must name `test_dry_run_finds_the_heading_in_real_notes`, `tests/cobalt/test_checkpoints_live.py` and the words `COBALT_LIVE_VAULT_ROOT not set`, exactly what the row asks | OK |
| 9 | RED/GREEN reason | RED: the gate prints `OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36` (build report `:181`, `:232`). GREEN: item present, same line prints without the prefix. The row states both, plus the offline `test_gate.py` test | OK |
| 10 | worktree `tests/cobalt/test_checkpoints_live.py` read whole; `grep -n -e print -e capsys -e caplog` | grep prints nothing. Skip `:24-26`, decorator `:36`, test `:37`, assertions `:41-58`. Messages: `:42` (no file or text), `:44` comment, `:46` and `:52` name an index, `:56-58` fixed text. Assertions are heading line, action and exit code, diff marker line, sha equal. Part 3 is verify-only | OK |
| 11 | files for the two fixed files | row `files`: DEPLOY-HUB.md (`:104` only) and `gate-lists.md` (ALLOWED SKIPS item, LIVE-NOTE line only). RECORDS names the classes (`docs/` → DOCS, `ops/desk/gate-lists.md` → operator script) and the unchanged RESTARTS `com.cobalt.aset com.cobalt.radar` | OK |
| 12 | continue step | row and ORDER both say `W` again, then the check, then the deploy. Matches build report `:210` | OK |
| 13 | `git rev-parse main HEAD`; `git diff --stat 42d456ab 8efd4f01 -- <hub, gate-lists, gate.sh, test_gate.py>` | main = HEAD = `8efd4f01`. The card's cited main `42d456ab` is older, but the four files are byte-equal between the two, so every cite holds | OK |
| 14 | precedent `503-f23-card.md` FIX1 | same three parts, same files and RED/GREEN shape. This row adds the "after the `test_live_vault_renders_six_decks` clause" slot and the L9 sentence | OK |

## ISSUES
- NOTE (decision 1, L9 other-house read): default acceptable. 503's FIX1 carries no such read. The row says the desk runs it at the change, and `HOUSE B: mandatory` already requires it. It blocks nothing.
- NOTE (main moved): the drafter read `main` at `42d456ab`. `main` is now `8efd4f01`. The four gate files are unchanged, so no re-read is needed.
- NOTE (what blocks CONTINUE): no FAIL. Two things to settle first: (a) the build report `:210` and `:213` say "after the desk amends `DEPLOY-HUB.md:104`", but the row lists that file in the builder's `files`. The desk should say which of them edits `:104`. The hub clause and the ALLOWED SKIPS item must be word-consistent, and `test_gate.py` reads the hub from the tree it runs in. (b) The builder worktree branch `ops/f5-checkpoints-1018` is at `97dd4b2e`, not the report's `a43ef10c`. The CONTINUE must start from that tip. K0 still stops while `FORWARD` ends `0025` (Genesis merges first), per the desk's OWED line.
- NOTE: the card has no `«FILL`, no other-row change, and a clean diff against HEAD. The header is untouched.

PREFLIGHT DONE · card: f5-checkpoints-1018 · checks: 14 · fails: 0 · ready: YES
