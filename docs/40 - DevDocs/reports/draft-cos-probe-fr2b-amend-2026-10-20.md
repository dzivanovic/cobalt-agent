# draft-cos-probe-fr2b-amend — card 923 amended

## §0 Headline
- FAIL 11 fixed by dropping `## DEPLOY PROOF` row 5 (`grep -n -F`, unmapped by `deploy-smoke.sh`); marker 4 already proves both headings (`grep -c -F` on `dfea631a` → `2`).
- NOTE 1 fixed: the card's one "Write of the whole file, or Edit hunk by hunk" is now "Edit hunk by hunk" and `HOW: Edit and Write ONLY` is now `Edit ONLY`. Markers 1-4, BASE and the rest are untouched.
- The card has no PORT, DONE WHEN or CHECK ASKS line with that wording; the only hit was in the WHY/HOW paragraph.

## DECISIONS
- ASK DESK: `BUILD-HUB.md:16` says an `Edit(<glob>)` rule also governs the Write tool on the same glob, so Write is in fact allowed in the worktree, which `:14` alone does not show. I followed the order and removed Write anyway. Default: keep "Edit hunk by hunk". Restore Write only if you want whole-file writes. [15:05]
- ASK DESK: row 5 was dropped, not rewritten, because a `(check)` count would repeat marker 4. Default: dropped. [15:05]

## RECORDS
- 2026-10-20 15:03-15:06 (`date`).
- Read: card 923; `reports/cos-probe-fr2b-preflight-2026-10-20.md` (`## ISSUES`, row 11); `ops/desk/deploy-smoke.sh` lines 105-155 (`shape()` maps `ls`, `grep -c -F "<s>" <path>`, curl, db query only); `prompts/BUILD-HUB.md` lines 10-16.
- Proof: `git -C /Users/cobalt/cobalt grep -c -F "## 2026-10-20 — cos-probe-fr2" dfea631a -- "docs/40 - DevDocs/cobalt/cos/README.md"` → `2`. On main it is `0` (card `## RECORDS`).
- Other builder commands re-checked against `BUILD-HUB.md:14`: `git show`, `git diff`, `uv run pytest`, `uv run cobalt jobs restarts`, `git add`/`git commit`, `grep`, `ls`. All are allowed. No command was added.
- Edits: card 923 only, in place. Nothing committed.

DRAFTED · decisions: 2
