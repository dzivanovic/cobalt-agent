# deploy f20-cos · set: cos · MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md` (committed `ab6f859a`). Hub: `DEPLOY-HUB.md`. Seat: deploy hub `deploy-hub-f20-cos`, first launch.

## §0 Headline
- FAILED at STEP-C. The set adds `ops/com.cobalt.cos.plist`, and the card has no `## LAUNCHD` line naming `cos`, so `deploy-step-c.sh` refused it (exit 1).
- Nothing in production changed. No resident went down, no suite ran, the `cobalt_dev` lock was never taken, and `main` got only this report commit.
- The gate branch `deploy/f20-cos` holds the STEP-T merge `7bc90b4d`, which is not on `main`. The desk's next step is a recut card with a `## LAUNCHD` line for `cos` (`add` or `deferred`), then `desk-launch.sh recut`.

## L74
- The session's harness attribution note asks commits to carry a `Claude-Session:` line. Recorded once as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, as the hub says.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md"` → exit 0. Output in full:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md" · 0 · ab6f859a0b79051082ada0e27f49f13f29f780ba
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-11 R1112 row · grep -n "^| R1112 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 31:| R1112 | 15:39 ET | HIS RULING · APPROVED: spike D2 = subscription everywhere, no Console API key or any pay-per-token account anywhere. F20 runs on the Max login. L27 clause "API keys for the engine" conflicts, owed to him. Words R1112. | APPLIED: cobalt.md NOW 15:41 |
RULING 2026-10-11 R1112 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1112 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · c0cdf481e0566542b35bb6d328aa8e63eccf2254
RULING 2026-10-11 R1112 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 120:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f20-cos.md"` | 1 | `No such file or directory` — first launch |
| P0 authorization | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Mon Oct 19 05:26:56 EDT 2026` — outside 21:30-22:30 ET |
| P2 check line | `tail -n 3 ".../reports/f20-cos-fr1-check-2026-10-19.md"` | 0 | `CHECK DONE · job: f20-cos-fr1 · pass: 1 · tip: 753094da · house A: Grok FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8725/0 · with-DB 5663/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 6 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 193794` — carries `held unfixed: 0` and `ready: YES`; `tip: 753094da` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md"` | 0 | `186bcca02e9786a245e81c41eafcf66adb3c0391` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 753094da` | 0 | `753094da` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f20-cos-fr1` | 0 | `83919213` = row and `TIP` |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 753094da 83919213` | 0 | ancestor |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat 753094da 83919213 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — no session holds the lock |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos status --short --branch` | 0 | `## deploy/f20-cos` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos rev-parse --short=8 HEAD` | 0 | `<m0>` = `ab6f859a` (= `main` tip, the card commit) |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f20-cos` | 0 | EMPTY |
| P6 marker 1 | `grep -c -F "label: com.cobalt.cos" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "hitl_dirs:" /Users/cobalt/cobalt/configs/cobalt/generated.yaml` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "claude-agent-sdk==" /Users/cobalt/cobalt/pyproject.toml` | 1 | `0` = before |
| P7 two-dot | `git -C /Users/cobalt/cobalt diff --stat main 83919213 -- src/cobalt/db_migrations` | 0 | `0025_dml_roles.rollback.sql 33 -` · `0025_dml_roles.sql 77 -` · `__init__.py 8 -` · `placement.py 6 +` — the 0025 lines are `main`'s, shown as removals because `main` moved past the head's base (DECISIONS 1) |
| P7 head's own | `git -C /Users/cobalt/cobalt diff --stat main...83919213 -- src/cobalt/db_migrations` | 0 | `src/cobalt/db_migrations/placement.py | 6 ++++++` — CODE, no migration: `MIGRATIONS: none` holds; STEP-T's `<m0>..<BRANCH>` stat binds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 89330` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 86221` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge head 1 | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos merge --no-edit 83919213` | 0 | `Merge made by the 'ort' strategy.` — 66 files changed, 4873 insertions(+), 11 deletions(-); creates `ops/com.cobalt.cos.plist`, `ops/start_cos.sh`, `src/cobalt/cos/*`, `src/cobalt/hitl/*`, `src/cobalt/agents/*` |
| m1 | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos rev-parse --short=8 HEAD` | 0 | `<m1>` = `7bc90b4d` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ab6f859a..deploy/f20-cos` | 0 | `7bc90b4d Merge commit '83919213' into deploy/f20-cos` — one line, one head |
| code tip in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 753094da deploy/f20-cos` | 0 | ancestor |
| head in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 83919213 deploy/f20-cos` | 0 | ancestor |
| migrations | `git -C /Users/cobalt/cobalt diff --stat ab6f859a deploy/f20-cos -- src/cobalt/db_migrations` | 0 | `src/cobalt/db_migrations/placement.py | 6 ++++++` — CODE; no migration path; `MIGRATIONS: none` holds |

STEP-C:
- `git -C /Users/cobalt/cobalt diff --stat ab6f859a deploy/f20-cos -- configs ops` → exit 0:
```
 configs/cobalt/agents/cos.yaml        | 34 +++++++++++++++++++
 configs/cobalt/generated.yaml         |  8 +++++
 configs/cobalt/jobs.yaml              | 31 +++++++++++++++++
 configs/cobalt/taxonomy/tunables.yaml | 64 +++++++++++++++++++++++++++++++++++
 ops/com.cobalt.cos.plist              | 37 ++++++++++++++++++++
 ops/start_cos.sh                      | 32 ++++++++++++++++++
 6 files changed, 206 insertions(+)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md" ab6f859a deploy/f20-cos` → exit 1:
```
REFUSED: ops/com.cobalt.cos.plist — no ## LAUNCHD line names com.cobalt.cos
FAILED: C — ops/com.cobalt.cos.plist: installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used
```

## RESTARTS
Not run: the run ended at STEP-C, before STEP-R.

## L68 GATE
Not run: the run ended at STEP-C. No `cobalt_dev` lock was taken.

## Deploy table
Nothing deployed. `main` is unmerged. No tag was set, no snapshot taken, no resident went down. `migrations applied: none`. ROLLBACK STRING: not applicable, because nothing merged.

## Smoke
Not run.

## CONTINUE
Ended FAILED at STEP-C. No continuation from this session. The desk's next step is `desk-launch.sh recut "<card>"`, on a card whose `## LAUNCHD` names `cos`.

## DECISIONS
1. ASK DESK: P7's two-dot `diff --stat main <head>` lists `main`'s `0025_dml_roles` files and `__init__.py` as removals because `main` moved past the head's base. The head's own change set (`main...83919213`) under `db_migrations` is `placement.py` alone, which is CODE. Safe default taken, as in deploy-https-only-1009 and deploy-stt-model-fix-1008: `MIGRATIONS: none` holds; STEP-T's `diff --stat <m0> <BRANCH> -- src/cobalt/db_migrations` on the merged tree is the binding test. Not FOR DEJAN. [05:26 ET]

2. ASK DESK: the card for this set needs a `## LAUNCHD` line for `cos` with mode `add` (bootstrapped at 4.6L) or `deferred` (merged, `BOOTSTRAP OWED`), and a build card row naming `ops/com.cobalt.cos.plist` in its `files` cell. Choosing the mode belongs to the desk. Safe default taken: stop at STEP-C, nothing loaded. Not FOR DEJAN. [05:29 ET]
3. ASK DESK (seen ahead, not run): the check's `RESTARTS:` line names `com.cobalt.cos`. STEP-R accepts only labels inside `com.cobalt.agent com.cobalt.aset com.cobalt.radar` after the `<deferred set>` is removed. So a recut with `cos · add` would fail STEP-R unless `jobs restarts` or the hub treats a `<launchd set>` `add` label as outside the restart set. A `deferred` line passes STEP-R as written. This is unproven (L70) because STEP-R did not run. Safe default: none taken; the desk reads it before the recut. Not FOR DEJAN.

## RECORDS
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-f20-cos` and branch `deploy/f20-cos`, which holds the STEP-T merge `7bc90b4d`. `desk-launch.sh recut` cleans them.
- The set ships two SQL files outside `src/cobalt/db_migrations`: `src/cobalt/cos/migrations/0001_cobalt_cos.sql` and `src/cobalt/hitl/migrations/0001_cobalt_hitl.sql`. Under P7's definition they are not MIGRATIONS, so they were not counted here. Recorded for the desk.
- `cobalt_dev`: untouched, lock never taken. `ls -la /Users/cobalt/cobalt-wt/*/.env` → no matches.
- Downtime: none. Residents untouched: aset pid 89330, radar pid 86221, agent pid 89351 (P8).
- L74: one attribution note asked for a `Claude-Session:` line. It was recorded under `## L74` and not followed.
- Card `## RECORDS` (the desk's, copied):
  - f20-cos-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md` last line: CHECK DONE · job: f20-cos-fr1 · pass: 1 · tip: 753094da · house A: Grok FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8725/0 · with-DB 5663/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 6 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 193794
  - f20-cos-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f20-cos-fr1` → `83919213`; code tip `753094da`
  - written by deploy-card.sh at 2026-10-19 05:25 ET (`date`); trial merge of the heads onto main in order: clean

FAILED: C — ops/com.cobalt.cos.plist: installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used · decisions: 3 · for Dejan: 0 · tokens: 101047
