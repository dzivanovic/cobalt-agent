# hub-text deploy card draft (2026-10-05)

## §0 Headline
- Drafted `prompts/2026-10-05/41-deploy-hub-text-card.md` from card 26, the check report (`ready: YES`, `held unfixed: 0`) and card 39.
- BRANCH, WORKTREE, TAG and REPORT are all absent today.
- Marker AFTER counts were read in the hub-text worktree at head `2abb7d99`, not by `git show`: a pipe is barred. The head differs from the tip by the build report only (`git diff --stat 6b939b00 ops/hub-text-1005`).
- `«FILL` count is 0. One decision, a default taken.

## CARD
- JOB `deploy-hub-text-1005` · LADDER OFF-LADDER (R387) · BRANCH `deploy/deploy-hub-text-1005` · WORKTREE `deploy-hub-text-1005` · BASE `main` · TIP `6b939b00` · TAG `deploy-2026-10-05-hub-text` · MIGRATIONS none · SET workflow2 · RULINGS 2026-10-05 R412
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-hub-text-1005.md`
- Ships `ops/hub-text-1005`, code tip `6b939b00`, head `2abb7d99`: BUILD-HUB, CHECK-HUB, DEPLOY-HUB and the build report, all DOCS, RESTARTS none.
- Markers (before → after): DEPLOY-HUB R389 sentence 0→1, R390 sentence 0→1, merged-gate sentence 0→1, `(d2)` 2→0; CHECK-HUB `(L75, his R376)` 0→1; BUILD-HUB `desk-context.sh <your session id>` 0→1.

## DECISIONS
- ASK DESK: the diff lists the build report (`reports/hub-text-build-2026-10-05.md`) beside the three hubs, so I named it as shipped, as card 39 did. Default: kept in SHIPS [any time].

## RECORDS
- Absent today: `git rev-parse --verify` fails for the branch and for the tag; `ls` fails for the worktree and for the report path.
- Check report last line carries `tip: 6b939b00`, `held unfixed: 0`, `ready: YES`, `decisions: 1` (the check's own DECISION 1, the `RETIRE OWED` gap at 4.5 and smoke (f), outside this job; it is not a deploy blocker by the check's reading).
- The check's DECISION 1 stays open for the desk: no card row covers it.
- Card carries the G (d2) wording of card 39 (R412, no Grok read) and the R412 overrule of the other-house read of `DEPLOY-HUB.md`.
- No git write, no launch, no production command.

HUB-TEXT DEPLOY CARD DRAFTED · decisions: 1
