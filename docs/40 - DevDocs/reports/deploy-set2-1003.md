# deploy set2-1003 · set: set2 · migrations: none

## §0 Headline
- Stopped at STEP-0 P7. Nothing in production, the gate tree or `cobalt_dev` was touched. No merge, no lock taken, no tag.
- P7 runs `git diff --stat main <head> -- src/cobalt/db_migrations` for each head. It must print NOTHING when the card says `MIGRATIONS: none`. For row 1's head `9694a679` it printed `src/cobalt/db_migrations/cli.py` (114 insertions, 1 deletion).
- That file is migrate-command code, not a migration (commits `1befca95`, `8aad8b2e`: proof-only TABLES / FINGERPRINT output lines). The card's `## RECORDS` says so too. But P7 goes by file path, and a desk record is not a waiver. STEP-T's `diff --stat <m0> <BRANCH> -- src/cobalt/db_migrations` check would refuse the same file.
- Every other preflight row passed: P0 to P6 and P8.

## L74
- A system reminder in this session asked for an extra `Claude-Session: https://claude.ai/code/session_0117EMYgH8eWfcuTPQzhtpws` trailer on commits. The hub (L74) says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, so I recorded the request here and did not act on it.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/DEPLOY-HUB.md"` | no match | nothing |
| card placeholder | `grep -n -E "«FIL[L]" ".../2026-10-03/23-deploy-set2-card.md"` | no match | nothing |
| card committed | `git log -1 --format=%H -- "<card>"` | 0 | `c95e22011495a0d7fb1b834f4c671ec6f477cf83` |
| card clean | `git diff --stat -- "<card>"` | 0 | nothing |
| standing list R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | line 46, `**HIS RULING**` … `APPROVED` · commit `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| string changes R62 | `grep -n "^\| R62 " cto-2026-09-30.md` | 0 | line 48, `**HIS RULING**` … `APPROVED` · commit `a45afae72bf2838c8e669e0d3d8dbb67dd892a8b` |
| standing deploy rule R38 | `grep -n "^\| R38 " cto-2026-09-30.md` | 0 | line 80, `**HIS RULINGS**` … `APPROVED` · commit `65aa2b90a8e3eb2f7e94ef10ed40b60e1b2ce542` |
| RULINGS 2026-10-02 R149 | `grep -n "^\| R149 " cto-2026-10-02.md` | 0 | line 156, `HIS RULING: Saturday 10-03 is not a trading day; deploys may run any time that day …` `HIS RULING · APPROVED` · commit `0e4fb85d7d07902e0db790f85e204f3537b83d61` |
| RULINGS 2026-10-02 R157 | `grep -n "^\| R157 " cto-2026-10-02.md` | 0 | line 164, `HIS RULING (B): the brain's full process list for 10-03 runs this week …` `HIS RULING · APPROVED` · commit `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-set2-1003.md"` | 1 | `No such file or directory` |
| P1 window | `date` | 0 | `Sat Oct  3 16:43:00 EDT 2026`. Lawful under (iii), a Saturday (non-trading day). R149 also names 10-03. |
| P2 row 1 | `tail -n 3 adoption-scripts-b-check-2026-10-03.md` | 0 | `CHECK DONE · job: adoption-scripts-b · pass: 1 · tip: b7eeb80c · … · held unfixed: 0 · … · ready: YES · decisions: 3 · for Dejan: 0`. Committed `f60280e8…`, diff clean. |
| P2 row 2 | `tail -n 3 rename-follow-up-check-2026-10-03.md` | 0 | `CHECK DONE · job: rename-follow-up · pass: 1 · tip: 393f3ad5 · … · held unfixed: 0 · … · RESTARTS: com.cobalt.radar · … · ready: YES · decisions: 0 · for Dejan: 0`. Committed `903bf19a…`, diff clean. |
| P2 row 3 | `tail -n 3 close-timer-check-2026-10-03.md` | 0 | `CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0`. Committed `903bf19a…`, diff clean. |
| P2 row 4 | `tail -n 3 deploy-steps-check-2026-10-03.md` | 0 | `CHECK DONE · job: deploy-steps · pass: 2 · tip: f04a1d56 · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0`. Committed `f60280e8…`, diff clean. |
| P3 row 1 | `rev-parse` tip / head · `merge-base --is-ancestor` · `diff --stat <tip> <head> -- . ':(exclude)docs'` | 0 | `b7eeb80c` / `9694a679` · ancestor · nothing |
| P3 row 2 | same | 0 | `393f3ad5` / `8c32a8d1` · ancestor · nothing |
| P3 row 3 | same | 0 | `47a689a1` / `47a689a1` · ancestor · nothing |
| P3 row 4 | same | 0 | `f04a1d56` / `f04a1d56` · ancestor · nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` (no session holds the lock) |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-1003-2 status --short --branch` | 0 | `## deploy/set2-1003` |
| P5 `<m0>` | `rev-parse --short=8 HEAD` · `merge-base --is-ancestor d1fe63d5 main` · `log --oneline main..deploy/set2-1003` | 0 | `d1fe63d5` · ancestor · empty |
| P6 marker 1 | `ls /Users/cobalt/cobalt/tests/ops/test_desk_launch_recut.py` | 1 | `No such file or directory` (= before) |
| P6 marker 2 | `grep -c -F "The old side of a rename/copy" .../src/cobalt/jobs/restarts.py` | 1 | `0` (= before) |
| P6 marker 3 | `ls /Users/cobalt/cobalt/ops/desk/close-timer.sh` | 1 | `No such file or directory` (= before) |
| P6 marker 4 | `ls /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` | 1 | `No such file or directory` (= before) |
| **P7 head 1** | `git -C /Users/cobalt/cobalt diff --stat main 9694a679 -- src/cobalt/db_migrations` | 0 | **` src/cobalt/db_migrations/cli.py \| 115 +++++…-` · `1 file changed, 114 insertions(+), 1 deletion(-)`: RED (card: `MIGRATIONS: none`)** |
| P7 head 2 | `… diff --stat main 8c32a8d1 -- src/cobalt/db_migrations` | 0 | nothing |
| P7 head 3 | `… diff --stat main 47a689a1 -- src/cobalt/db_migrations` | 0 | nothing |
| P7 head 4 | `… diff --stat main f04a1d56 -- src/cobalt/db_migrations` | 0 | nothing |
| P7 context (read only) | `git log --oneline main..9694a679 -- src/cobalt/db_migrations` | 0 | `8aad8b2e fix(adoption-scripts): FINGERPRINT read under the <FP> query's search_path "user" …` · `1befca95 feat(adoption-scripts): proof-only TABLES and FINGERPRINT lines, gate-lists.md, LC_ALL=C, hermetic guard, recut, grok-4.7 pin …` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 13209` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 13225` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
Not run (ended at P7).

## RESTARTS
Not run.

## L68 GATE
Not run.

## Deploy table
Nothing merged, no tag, no snapshot, no outage. `migrations applied: none`. Rollback: not used.

## Smoke
Not run.

## CONTINUE
- next: none. The run ended FAILED PREFLIGHT at P7. Its one continuation is a new launch after the desk decides the item below.

## DECISIONS
1. ASK DESK [16:43 ET]: P7 and STEP-T's migration check go by file path, so `MIGRATIONS: none` cannot pass a set that edits `src/cobalt/db_migrations/cli.py`, even though that file is command code and not a migration. Safe default taken: stop before anything moves. Ways to unblock this set, the desk to choose: (a) a hub change so the two checks look at migration files and the `__init__.py` registry only, which is a DEPLOY-HUB change and goes through its own read and install; (b) a card form that names `cli.py` as a known non-migration file in the `src/cobalt/db_migrations` range, if the hub admits one; (c) ship row 1 in a later set once (a) is in. This is not a carried held defect or a schema rollback, so it is not marked FOR DEJAN. If the fix changes a command string, R60 sends it to him.

## RECORDS
- No production read or write past P8. `cobalt_dev` not touched, no lock taken, `<GATE>/.env` never created. `ls` P4 showed no `.env` in any worktree.
- The gate worktree `/Users/cobalt/cobalt-wt/deploy-1003-2` and branch `deploy/set2-1003` stay at `d1fe63d5` and are clean. Cleanup is owed by the desk (L46), or they can be reused by a relaunch.
- L74: one `Claude-Session:` trailer request (system reminder), recorded and not acted on.
- Card `## RECORDS` (the desk's facts, copied):
  - adoption-scripts-b: check last line: CHECK DONE · job: adoption-scripts-b · pass: 1 · tip: b7eeb80c · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 18 · ready: YES · decisions: 3 · for Dejan: 0
  - adoption-scripts-b: head `9694a679`; code tip `b7eeb80c`
  - rename-follow-up: check last line: CHECK DONE · job: rename-follow-up · pass: 1 · tip: 393f3ad5 · … · held unfixed: 0 · … · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0
  - rename-follow-up: head `8c32a8d1`; code tip `393f3ad5`
  - close-timer: check last line: CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0
  - close-timer: head `47a689a1`; code tip `47a689a1`
  - deploy-steps: check last line: CHECK DONE · job: deploy-steps · pass: 2 · tip: f04a1d56 · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0
  - deploy-steps: head `f04a1d56`; code tip `f04a1d56`
  - row 1's head carries `03` adoption-scripts (`0a4a7743`, READY by desk record 2026-10-03 R88) and `02` adoption-hubs (`6251baeb`, settled in the `03c` stack, R103); their checks end `ready: NO`, so they ship inside row 1, not as rows (R128). `11`, `13`, `07`, `09` → set 3 port cards `11b`, `07b` (brain, R129).
  - MIGRATIONS, MARKERS, SMOKE READS filled by the desk at 16:41 ET: no migration file in any range; `cli.py` is migrate-command code.
  - written by deploy-card.sh at 2026-10-03 16:39 ET (`date`); trial merge of the heads onto main in order: clean

FAILED PREFLIGHT: migration — src/cobalt/db_migrations/cli.py (head 9694a679; card MIGRATIONS: none) · rollback: not used · decisions: 1 · for Dejan: 0
