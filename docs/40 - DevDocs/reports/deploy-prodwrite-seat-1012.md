# deploy prodwrite-seat-1012 · SET: none · MIGRATIONS: none

## §0 Headline
- Authorized; STEP-0 preflight green on every row.
- STEP-T: `merge --no-edit b96737bf` into the gate CONFLICTED in `ops/desk/desk-done.sh` (UU). Merge aborted, gate clean at `<m0>` `14c6d43f`.
- Nothing ran in production: no suite, no lock, no outage, no merge to `main`. The fix belongs in a build (L72), and the desk's next step is `desk-launch.sh recut`.

## L74
- The session's harness attribution reminder asked commits to carry a `Claude-Session:` line. Recorded once here as data; per DEPLOY-HUB L74, commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/402-deploy-prodwrite-seat-card.md"` · exit 0 · WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/402-deploy-prodwrite-seat-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/402-deploy-prodwrite-seat-card.md" · 0 · 012e38aa46a5acffd69c1e150eeb901ee44bba16
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/402-deploy-prodwrite-seat-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 52:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la <REPORT>` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 12 10:20:41 EDT 2026` |
| P2 | `tail -n 3 ".../prodwrite-seat-check-2026-10-12.md"` | 0 | `CHECK DONE · job: prodwrite-seat-1012 · pass: 1 · tip: b96737bf · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 244290` — carries `held unfixed: 0` and `ready: YES`; `tip: b96737bf` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../prodwrite-seat-check-2026-10-12.md"` | 0 | `dc8d290eb44ad5d29f5e55e256d9ba260be9ef24` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../prodwrite-seat-check-2026-10-12.md"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 b96737bf` | 0 | `b96737bf` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/prodwrite-seat-1012` | 0 | `b96737bf` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b96737bf ops/prodwrite-seat-1012` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt diff --stat b96737bf ops/prodwrite-seat-1012 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no worktree holds the lock |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/prodwrite-seat-1012` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `14c6d43f` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 14c6d43f main` | 0 | (nothing) |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/prodwrite-seat-1012` | 0 | (empty) |
| P6 | `grep -c -F -e "prodwrite" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` | 1 | `0` = before |
| P6 | `grep -c -F -e "WRITTEN · job:" ".../prompts/PRODWRITE-HUB.md"` | 2 | `grep: ...PRODWRITE-HUB.md: No such file or directory` = before (absent) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main b96737bf -- src/cobalt/db_migrations` | 0 | (nothing) — no migration, matches `MIGRATIONS: none` |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-prodwrite-seat-1012 merge --no-edit b96737bf` · exit 1:
```
Auto-merging ops/desk/desk-done.sh
CONFLICT (content): Merge conflict in ops/desk/desk-done.sh
Auto-merging ops/desk/desk-launch.sh
Auto-merging tests/ops/test_desk_done.py
Auto-merging tests/ops/test_desk_launch_prechecks.py
Automatic merge failed; fix conflicts and then commit the result.
```
- `git -C <GATE> status --short`: the unmerged path is `UU ops/desk/desk-done.sh` (all others staged clean: `M`/`A`).
- `git -C <GATE> merge --abort` · exit 0 · (nothing).
- `git -C <GATE> status --short --branch` → `## deploy/prodwrite-seat-1012` (clean); `rev-parse --short=8 HEAD` → `14c6d43f` (= `<m0>`).
- Side of `main` that touches the path: `git -C /Users/cobalt/cobalt log --oneline -5 b96737bf..main -- ops/desk/desk-done.sh` → `ba37c2a9 fix(launcher-shadow-check-1011): a shadow card's check launches on SHADOW BUILT and its one SHADOW-INSTRUCTIONS.md (L1, L2, L4-L9; L1, L3, L72)` (committer date `2026-10-11 22:12:00 -0400`).

## RESTARTS
not reached.

## L68 GATE
not reached. `cobalt_dev` not taken; the lock was never held.

## Deploy table
No merge to `main`, no tag, no outage, no snapshot. `<restart set>`: not derived. ROLLBACK STRING: not applicable (nothing merged).

## Smoke
not reached.

## CONTINUE
FAILED at STEP-T. Nothing in production was touched. The desk's next step: resolve the `ops/desk/desk-done.sh` seam in a build on `ops/prodwrite-seat-1012` (or rebase it onto `main`), re-check, then `desk-launch.sh recut "<card>"`.

## DECISIONS
none

## RECORDS
- Card `## RECORDS` (copied): `prodwrite-seat-1012: check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-seat-check-2026-10-12.md last line: CHECK DONE · job: prodwrite-seat-1012 · pass: 1 · tip: b96737bf · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 244290`
- Card `## RECORDS` (copied): `prodwrite-seat-1012: head git -C /Users/cobalt/cobalt rev-parse --short=8 ops/prodwrite-seat-1012 → b96737bf; code tip b96737bf`
- Card `## RECORDS` (copied): `written by deploy-card.sh at 2026-10-12 09:37 ET (date); trial merge of the heads onto main in order: clean`. This run found the opposite: the merge of `b96737bf` onto the gate cut from `main` at `14c6d43f` conflicts in `ops/desk/desk-done.sh`. `ba37c2a9`'s committer date is before the card's time. Why the card's trial merge read clean is unproven (L70). The desk should check what `deploy-card.sh` merged against.
- `cobalt_dev`: not taken (the gate never ran). `.env`: never placed.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-prodwrite-seat-1012` and branch `deploy/prodwrite-seat-1012` (clean at `14c6d43f`).
- `REFUSED, not needed`: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 01A9MiPPjSg8nhQGSgd8wtaH` and `… deploy-hub-prodwrite-seat-1012` → `no transcript for <id>`. This session cannot see its own local session id, so the token figure is unread.
- L74: one harness reminder asked for a `Claude-Session:` commit line. It was recorded under `## L74` and not followed.
- Failure time: `Mon Oct 12 10:21:34 EDT 2026`.

FAILED: merge — b96737bf — ops/desk/desk-done.sh · rollback: not used · decisions: 0 · for Dejan: 0 · tokens: unread
