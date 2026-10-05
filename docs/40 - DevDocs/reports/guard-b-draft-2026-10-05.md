## §0 Headline
- Guard-b single-feature deploy card written: `prompts/2026-10-05/15-deploy-guard-b-card.md`.
- Branch, worktree, tag and report path are all absent today.
- Head and tip of `ops/cobalt-guard-b-1004` are `47ec01c5`; check report ends `held unfixed: 0` · `ready: YES`.
- Marker before-count on main is `0`, same as card `02`.

## CARD
- JOB `deploy-guard-b-1005` · LADDER `S3-P3 · F14` (as card `02`) · BRANCH `deploy/deploy-guard-b-1005` · WORKTREE `deploy-guard-b-1005`
- BASE `main` · TIP `47ec01c5` · TAG `deploy-2026-10-05-guard-b` · MIGRATIONS `none` · SET `workflow2`
- RULINGS 2026-10-05 R390, R391, R392
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-guard-b-1005.md`

## DECISIONS
- none

## RECORDS
- `git rev-parse --verify` of the branch and of the tag: exit 128 (absent). `ls` of the worktree and of the report: No such file.
- `grep -c -F "@include" ops/desk/bare-guard.py` on main now → `0`; card `02` before `0`; no difference.
- Head `git rev-parse --short=8 ops/cobalt-guard-b-1004` → `47ec01c5`.
- `grep -c -F "«FILL"` on the card → 0 (none written).

GUARD-B CARD DRAFTED · decisions: 0
