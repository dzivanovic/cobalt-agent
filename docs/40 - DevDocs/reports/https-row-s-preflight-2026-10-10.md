# https-only-1009 row S preflight — 2026-10-10

Card: `docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md` (`ba100db9`). Read-only.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat ba100db9~1 ba100db9 -- <card>` | `1 file changed, 2 insertions(+)`; `-U0` hunks: `@@ -24,0 +25 @@` (row S, in `## ROWS`) and `@@ -71,0 +73 @@` (one `- ROW S (R842 …)` line in `## RECORDS`). No deletions, no other bytes touched | OK |
| 2a | `git show main:docs/40 - DevDocs/cobalt/aset/__main__.md` | file is the aset `__main__.md`; headings at main's tip: `## 2026-10-09 — s4-p2-1009` and `## 2026-10-10 — strike-fallback-env-1010`, both at the file's end | OK |
| 2b | `git rev-parse --verify a1b99495^{commit}` / `411f85b2^{commit}` | `a1b99495353a259cfcf9627794b25c8cf9f5863a` / `411f85b28c464878b17a44d6f1ef916ff917c23f` | OK |
| 2c | `git diff --stat a1b99495 411f85b2 -- . ':(exclude)docs'` | (nothing) | OK |
| 3 | read row S | "With the Edit tool only"; "No code, test or config change"; adds no command. The literal words "git merge" appear nowhere in the card (see ISSUES) | OK (NOTE) |
| 4 | read row S PROOF cell | uses `git diff main...HEAD -- <file>` and `git diff --stat a1b99495 HEAD -- . ':(exclude)docs'` only: both `git diff` forms | OK |
| 5a | `grep -c "«FILL" <card>` | `0` | OK |
| 5b | header lines (`BASE e4586978`, `TIP a1b99495`, `CHECK REPORT`, `HOUSE B as needed`, `RULINGS 2026-10-09 R718`, `HOST cobalt.taild24291.ts.net`) vs the `ba100db9~1` diff | the diff touches only rows/records lines, so every header value is unchanged | OK |
| 5c | `git diff HEAD --stat -- <card>` | (nothing); HEAD is `84b96a1f`, card committed state equals HEAD | OK |
| 6 | read RECORDS line | states "docs only, a fix round after the check (L75, card 154 precedent): no re-check", and names the STEP-G gate on the merged tree | OK |

## ISSUES

- NOTE: row S does not spell out "no `git merge`" (R411/R412). "Edit tool only" plus no added command excludes it by implication, and the card has no `git merge` text. Add the words if the desk wants it literal.
- NOTE: BASE `e4586978` is older than main HEAD `84b96a1f`. That is expected, and it is not a FAIL.

PREFLIGHT DONE · card: https-only-1009 · checks: 10 · fails: 0 · ready: YES
