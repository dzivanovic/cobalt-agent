## §0 Headline
Check card written: `prompts/2026-10-17/710-gemini-builder-row-port-check-card.md`, scoped to PORT and FR-2 of card 671.
Tip `52a0600d` on BASE `13bcd579` (merge-base proved); head `5fea0cc4` adds only the build report (no non-docs diff).
Rows: S0, P1, P2, F2, A1, R3, G3. Header from card 687 with the values you gave. Nothing run, nothing committed.

## DECISIONS
- ASK DESK: `## DEPLOY PROOF` line 4 adds `tests/ops/test_band_routing_1015.py` to the shadow-tests command (card 671 lists three files; FR-2 touches a fourth). Default: keep the four-file form. [18:25 EDT]
- ASK DESK: row F2 has the checker undo-and-restore the old test by Edit for the red (no worktree checkout is on the allow line). Default: Edit, undo proved by `git diff --stat 52a0600d`. [18:25 EDT]

## RECORDS
- `date` → Sat Oct 17 18:19:03 EDT 2026; `main` `7ae1ba99`.
- `git log --oneline ops/gemini-builder-row-fr1 -5` → `5fea0cc4`, `52a0600d`, `395a9e77`, `13bcd579`, `9569ac1b`.
- `git merge-base main ops/gemini-builder-row-fr1` → `13bcd579e916603976b7faee758355dfa07d8022`.
- `git diff --stat 52a0600d 5fea0cc4 -- . ":(exclude)docs"` → nothing; `git diff --stat 13bcd579 52a0600d` → 7 files, 189 insertions, 20 deletions.
- `git diff --stat 7f415a4f main -- <three test files>` → nothing; `git diff --stat 13bcd579 7ae1ba99 -- ops tests <hub>` → nothing.
- Build report found at the worktree path only (`ls` of the main-tree copy: absent). Stop line, `## DECISIONS` (none) read.
- Worktree Grep lines: `desk-launch.sh:377`, `:404`; `bare-guard.py:1204`, `:1206`, `:1284`; `SHADOW-HUB.md:15`; `test_band_routing_1015.py:112`. Not re-proved with `git show` (worktree copy; the card tells the checker to).
- The card carries the sentence telling the checker to quote any refusal as a finding (rows' lead-in and X6).

DRAFTED · decisions: 2
