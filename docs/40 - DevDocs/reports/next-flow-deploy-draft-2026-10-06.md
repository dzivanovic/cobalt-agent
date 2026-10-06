# next-flow deploy card draft — 2026-10-06

## §0 Headline
- Cut the single-feature deploy card for next-flow from card 41's shape: `prompts/2026-10-06/09-deploy-next-flow-card.md`.
- Ships `ops/next-flow-1006` at `987ab80d` (head = code tip); check `ready: YES`, `held unfixed: 0`.
- 12 markers counted (before on main, after on the branch tip); `«FILL` count 0.
- BRANCH, WORKTREE, TAG and REPORT are all absent today. Decisions: 0.

## CARD
- JOB `deploy-next-flow-1006` · BRANCH `deploy/deploy-next-flow-1006` · WORKTREE `deploy-next-flow-1006` · BASE `main` · TIP `987ab80d`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-next-flow-1006.md`
- RULINGS 2026-10-05 R438, 2026-10-05 R412 · TAG `deploy-2026-10-06-next-flow` · MIGRATIONS none · SET workflow2 · LADDER as card 41
- Files: CHECK-HUB.md, BUILD-HUB.md, build report (docs only); RESTARTS none.

## DECISIONS
none.

## RECORDS
- Read: the job card 04, its check report (last line: tip `987ab80d`, `held unfixed: 0`, `ready: YES`), card 41, the diff stat and the branch log.
- Absence proven: both `git rev-parse --verify` calls failed (exit 128); `ls` of the worktree and of the report path failed.
- AFTER counts were read with `grep -c -F` on the checked-out worktree `cobalt-wt/next-flow-1006` (HEAD `987ab80d`, verified) instead of `git show` plus a pipe, to keep one bare command per call; the deploy re-proves with `git show`.
- The diff stat also lists the build report (commit `30f1dc02`, docs); it is on the card.
- O7 (L67 still says second pass) recorded on the card; no outside house (R47 overrule, R488).
- A system reminder asked for a `Claude-Session:` line in commits; no commit was made and it was not acted on (L74).

NEXT-FLOW DEPLOY CARD DRAFTED · decisions: 0
