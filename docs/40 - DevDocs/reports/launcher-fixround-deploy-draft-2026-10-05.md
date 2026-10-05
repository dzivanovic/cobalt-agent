# launcher-fixround deploy card draft · 2026-10-05

## §0 Headline
- Card `prompts/2026-10-05/47-deploy-launcher-fixround-card.md` written: one row, `ops/launcher-fixround-1005`, code tip and head both `a545a4d8`.
- Check r2 last line: `tip: a545a4d8`, `held unfixed: 0`, `ready: YES`. No commit after the tip touches `tests ops configs src`.
- Four markers, each before `0` on main and after `1` on the tip. `grep -c -F "«FILL"` → 0.
- `fix report` cell left empty (decision 1).

## CARD
- JOB `deploy-launcher-fixround-1005` · LADDER as card 41 · BRANCH `deploy/deploy-launcher-fixround-1005` · WORKTREE `deploy-launcher-fixround-1005` · BASE `main` · TIP `a545a4d8`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-launcher-fixround-1005.md` · RULINGS `2026-10-05 R412` · TAG `deploy-2026-10-05-launcher-fixround` · MIGRATIONS `none` · SET `workflow2`
- BRANCH, WORKTREE, TAG and REPORT are all absent today (`rev-parse --verify` fails for the branch and the tag; `ls` fails for the worktree and the report; 18:23 ET).

## DECISIONS
1. ASK DESK: the `fix report` cell is empty. The check ran on its code tip `a545a4d8`, and the fix-round tip rule is not in force on main until this deploy lands, so the row's code tip and the check's `tip:` agree. Default taken: empty cell. [18:23 ET]

## RECORDS
- Files shipped (8, `git diff --stat main...ops/launcher-fixround-1005`): three `ops/desk/` scripts, two `tests/ops/` files, `CARD.md`, `DEPLOY-HUB.md`, the builder's report. RESTARTS: none (classes from the check's `## Suites`).
- Head proof: `rev-parse ops/launcher-fixround-1005` → `a545a4d8d424c72df46d86c240b7484427f0cad2`; `git log --oneline a545a4d8..ops/launcher-fixround-1005 -- tests ops configs src` → empty.
- Markers: before counts read on main now, after counts read in `/Users/cobalt/cobalt-wt/launcher-fixround-1005` (HEAD `a545a4d8`): `is not committed and unmodified` `0`→`1`; `Fix-round row` `0`→`1`; `On a fix-round row (a small fix after the check, his R376, L75)` `0`→`1`; `| fix report |` `0`→`1`. The F4 string is the line-47 sentence, taken without its backticks.
- The builder's report last line carries `tip: dc2a80b4`, not `a545a4d8`. It is not read at deploy: the `fix report` cell is empty.
- `DEPLOY-HUB.md` merge: main's diff against `5fb0ddf5` changes the P1 line (57) and does not touch P2 (58). The branch inserts one line after 58. One unchanged line separates them, so git merges cleanly. Read from both diffs, not run.
- OWED, a later card: the check's DECISIONS 1 (`DEPLOY-HUB.md:58` names "the last column"; on the seven-column shape it is `its stop line must carry`). Copied into the card's `## RECORDS`.
- G (d2): wording as cards 39 and 41; no Grok read (R412).
- Commands: one bare command per call; pipes were refused by the bare-guard (not a refusal), so after counts were read from the branch worktree.

LAUNCHER-FIXROUND DEPLOY CARD DRAFTED · decisions: 1
