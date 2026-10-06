# guard-g2 deploy card draft (2026-10-06)

## §0 Headline
- Wrote `prompts/2026-10-06/34-deploy-guard-g2-card.md`: one feature, `ops/guard-g2-1006`, code tip and branch head `19f75dc6`.
- Check last line: `held unfixed: 0`, `ready: YES`, `RESTARTS: none`. 5 files, all `ops/`, `tests/ops/` or DOCS; no `src/`, no migration.
- BRANCH, WORKTREE, TAG and REPORT are all absent today. R511, R412 and R474 all exist on main.
- No install step: the desk copies of both scripts are symlinks into the repo.
- No `«FILL` token (count 0). 1 decision, with a default.

## CARD
- JOB `deploy-guard-g2-1006` · LADDER `OFF-LADDER — cto-2026-10-06.md R511`
- BRANCH `deploy/deploy-guard-g2-1006` · WORKTREE `deploy-guard-g2-1006` · BASE `main` · TIP `19f75dc6`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-guard-g2-1006.md`
- RULINGS `2026-10-06 R511, 2026-10-05 R412, 2026-10-05 R474` · TAG `deploy-2026-10-06-guard-g2` · MIGRATIONS none · SET none
- 8 MARKERS and 4 SMOKE READS; BEFORE values counted on main, AFTER values on the worktree at `19f75dc6`.

## DECISIONS
1. ASK DESK: R511 reads `APPROVED — pending fold` on main (`cto-2026-10-06.md` line 38), not a plain `APPROVED`. Default taken: the card cites it as is; the deploy proceeds as the check's authorization did. [08:39 from date]

Settled, no ask:
- `ops/desk/install-fixed.sh` installs a prompt-title token and copies no desk script, so the deploy hub does not run it. `DEPLOY-HUB.md` does not name it. `desk-launch.sh` and `bare-guard.py` reach `/Users/cobalt/.claude/ops/` by symlink, so merging to main is the whole install. No new command.
- BRANCH, WORKTREE, TAG and REPORT: none exist.

## RECORDS
- Check report: `reports/guard-g2-check-2026-10-06.md`, last line `ready: YES`, tip `19f75dc6`. Head log: `19f75dc6`, `5093b1ca`, `61999cc5`, `ce19a3fd`.
- Follow-ups for him (not in this deploy), written into the card: check OPEN A3, A4, B3 and DECISIONS 3 (`ruling_row` accepts `DISAPPROVED`) and 4 (the `desk` kind has no `PROD-READ:` test).
- The card carries the G (d2) wording (R412), the autovacuum note (R479) and R390.
- Bash calls were one bare command each, all on the allow line, plus Grep for the AFTER counts on the worktree. No git write, no launch.

GUARD-G2 DEPLOY CARD DRAFTED · decisions: 1
