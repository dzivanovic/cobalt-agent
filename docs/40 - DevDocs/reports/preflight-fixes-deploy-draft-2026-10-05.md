# preflight-fixes deploy card draft (2026-10-05)

## §0 Headline
- Card written: `prompts/2026-10-05/39-deploy-preflight-fixes-card.md`, no `«FILL`.
- Source: job card 20, check `ready: YES`, held unfixed 0, tip and head both `0af97be7`.
- R376, R387, R390, R412 each exist in `cto-2026-10-05.md` with `HIS RULING`. BRANCH, WORKTREE, TAG and REPORT are all absent.
- The diff holds no hub file, so SHIPS names none (the prompt said use only real files).

## CARD
- JOB `deploy-preflight-fixes-1005` · LADDER `OFF-LADDER — workflow set, R387` · BRANCH `deploy/deploy-preflight-fixes-1005` · WORKTREE `deploy-preflight-fixes-1005` · BASE `main` · TIP `0af97be7`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-preflight-fixes-1005.md` · TAG `deploy-2026-10-05-preflight-fixes` · MIGRATIONS none · SET `workflow2`
- Markers (before → after): `card 20 F2` 0 → 2 · `card 20 F1` 0 → 2 · `(recorded)` 0 → 2, all in `ops/desk/preflight.sh`. Before on main now; after counted on the branch worktree file at tip (grep), not `git show` of the tip.

## DECISIONS
- ASK DESK: the LADDER value is my choice (`OFF-LADDER — workflow set, R387`); the siblings use S3-P3 or an R47 note. [at the desk's next read] Default: keep.
- ASK DESK: the prompt named hub lines from the job card's rows; the diff has none, so none are listed. [at the desk's next read] Default: as written.

## RECORDS
- Opened: prompt 39, `areas/cobalt.md`, cards 14 and 15, the check report, the branch diff of `preflight.sh` and `test_desk_launch_brain.py`, `cto-2026-10-05.md` rows by grep. I did not open `prompts/CARD.md` and did not read `writing-rules.md`; the shape follows the report-shape lines in `areas/cobalt.md` and the siblings.
- No git write, no launch.

PREFLIGHT-FIXES DEPLOY CARD DRAFTED · decisions: 2
