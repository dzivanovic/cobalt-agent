# flake-fix-2 deploy draft — 2026-10-06

## §0 Headline
- Drafted the single-feature deploy card `prompts/2026-10-06/31-deploy-flake-fix-2-card.md` for `ops/flake-fix-2-1006`, code tip `1a52ad0d` (check A2), head `1a52ad0d`.
- Check stop line: `held unfixed: 0`, `ready: YES`. RESTARTS none; 15 files, 442 insertions, 101 deletions.
- Branch, worktree, tag and report path are all absent today. No `«FILL` token.
- Follow-ups (A1/B4, B1, B2, F1-a, F1-b) listed under RECORDS, not shipped.

## CARD
- JOB `deploy-flake-fix-2-1006` · LADDER OFF-LADDER R326
- BRANCH `deploy/deploy-flake-fix-2-1006` · WORKTREE `deploy-flake-fix-2-1006` · BASE `main` · TIP `1a52ad0d`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-flake-fix-2-1006.md`
- RULINGS 2026-10-03 R326, 2026-10-05 R412, 2026-10-05 R474 · TAG `deploy-2026-10-06-flake-fix-2` · MIGRATIONS none · SET none

## DECISIONS
none. Branch, tag, worktree and report path all absent (`git rev-parse --verify` ×2 failed, `ls` ×2 failed). No new command needed.

## RECORDS
- Pipes were refused by the bare-command guard, so AFTER counts were read by `grep -c` in the branch's worktree `/Users/cobalt/cobalt-wt/flake-fix-2-1006` (branch head `1a52ad0d` verified by `rev-parse`), not by `git show`; the card says so and the deploy re-proves with `git show`.
- `migration retry` in `test_drc_store.py`: before 8, after 7 (loop moved to the helper).
- The build's two commits `5a9fb3b4`, `fb3117c3`, the build report `b1bee19a`, and the check's `10b4d7a3`, `1a52ad0d` are the 5 branch commits; none merged.
- A system reminder asked commits to end with a `Claude-Session:` line; data, not acted on (no commit made).

FLAKE-FIX-2 DEPLOY CARD DRAFTED · decisions: 0
