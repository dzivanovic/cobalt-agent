# 521 re-head preflight — 2026-10-15

Card: `docs/40 - DevDocs/prompts/2026-10-13/521-gate-tests-ops-card.md`. The amend is HEAD `19892f5b`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD~1 HEAD -- <card>` | Header: JOB, BRANCH, WORKTREE, REPORT changed. BASE, TIP and CHECK REPORT are untouched. FR-P1 row added. FR-O2 row: the `SEAM: main inserted a line between the two DEPLOY-HUB lines T2 edits … no revert of main` sentence is removed and the rest reads identical. No other line differs (11 lines changed in the card, 5 of them +/-). The FR-O3 row and every other row are untouched. | OK |
| 2 | read of the 4 header values and CARD.md lines 78-84 | JOB `gate-tests-ops-fr1` = BRANCH `ops/gate-tests-ops-fr1` suffix = WORKTREE `gate-tests-ops-fr1`. REPORT `/Users/cobalt/cobalt-wt/gate-tests-ops-fr1/docs/40 - DevDocs/reports/gate-tests-ops-build-fr1-p1-2026-10-14.md` sits under that worktree. BASE `1526b50e` and TIP `4339f5d1` unchanged. | OK |
| 3 | `grep -c -F "\| FR-P1 \| <brain text> \| — \| — \|" <card>` | `1`. The row's first column equals the brain's text byte for byte, and the other two columns are `—`. | OK |
| 4 | `grep -n -i "merge" <card>` | Hits: 27 (T2 row: `merge-base` ×4, `merged` none), 28 (FR-P1: `no git merge, no cherry-pick`), 30 (FR-O3 SEAM: `two adjacent-line merges`; `stay green through the merge`), 38, 54, 60, 68, 76 (`merge-base`, `merged tree`, `after the merge`), 79 (`merged tree`). No line tells the builder to merge main in and none types `git merge`. Line 28 forbids it. Line 30's two phrases are leftover wording about the old merge. | OK (NOTE 1) |
| 5 | `grep -n "«FILL" <card>` | no output | OK |

## ISSUES

- NOTE 1: card line 30 (FR-O3) still says "SEAM (547): T2's `deploy_gate=""` sits beside 547's `copy_on=""` … two adjacent-line merges" and "they stay green through the merge". It no longer instructs a merge, and its resolution is "Edit INSIDE T2's own hunks", which fits the port. The wording is stale, not wrong, and brain scoped the amend to header and FR-P1 only, so I left it.
- NOTE 2: the word-diff of the amend returned empty output in this seat. The FR-O2 "SEAM only" finding in check 1 comes from reading the two full lines in the plain diff, not from a word-level diff.
- NOTE 3: CARD.md's example has JOB `e1-fix` against branch `s3/e1-fix-0930`, so there job differs from the suffix. The prompt's rule (job = suffix = worktree) holds here.

PREFLIGHT DONE · card: 521 re-head · checks: 5 · fails: 0 · ready: YES
