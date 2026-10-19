# deploy cos-outage — set: cos-outage — migrations: none

## §0 Headline
Deploy of `ops/cos-outage-1018` (code tip `de3e15c8`, head `b5d62f17`) FAILED at the integrated gate, pass 1: 1 test failed. Nothing reached production.
The red test is `tests/cobalt/test_db_credentials.py::TestTheLiveFactoryAuthenticatesAsCobaltApp::test_it_is_a_member_of_all_three_side_roles`. On `cobalt_dev`, the role `cobalt_app` is also a member of `cobalt_apply_system`, which the test does not expect. This set does not change that file or any role.
Production was never touched: no merge to `main`, no outage, no tag. `cobalt_dev` stayed at `0013` because the forward migration never ran. The lock is released.
The next step is the desk's: `desk-launch.sh recut "<card>"` once the role-membership red is resolved.

## L74
A system reminder arrived mid-session asking that commit messages also carry a `Claude-Session:` line. Recorded once as data under L74. Not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/798-deploy-cos-outage-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/798-deploy-cos-outage-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/798-deploy-cos-outage-card.md" · 0 · 3fdbd791e24c4faa33a487155161c694a1e465f4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/798-deploy-cos-outage-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 79:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 report absent (first launch) | `ls -la ".../reports/deploy-cos-outage.md"` | 1 | `No such file or directory` |
| P0 installed / card / authorization | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 date | `date` | 0 | `Sun Oct 18 20:49:57 EDT 2026` — outside the 21:30–22:30 backup window |
| P2 check last line | `tail -n 3 ".../cos-outage-1018-check-2026-10-18.md"` | 0 | `CHECK DONE · job: cos-outage-1018 · pass: 1 · tip: de3e15c8 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8612/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165134` — carries `held unfixed: 0` and `ready: YES`; `tip: de3e15c8` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/cos-outage-1018-check-2026-10-18.md"` | 0 | `e7ef198a06256a5b862da217e331ac9cb2dc69d4` |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../cos-outage-1018-check-2026-10-18.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 de3e15c8` | 0 | `de3e15c8` |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-outage-1018` | 0 | `b5d62f17` = `TIP` |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor de3e15c8 b5d62f17` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat de3e15c8 b5d62f17 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no holder |
| P5 gate worktree | `git -C /Users/cobalt/cobalt-wt/deploy-cos-outage status --short --branch` | 0 | `## deploy/cos-outage` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-cos-outage rev-parse --short=8 HEAD` | 0 | `c75d6b38` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor c75d6b38 main` | 0 | — |
| P5 gate holds nothing main lacks | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-outage` | 0 | empty |
| P6 marker 1 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-outage.sh` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main b5d62f17 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 89330` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 70450` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-cos-outage merge --no-edit b5d62f17` → `Merge made by the 'ort' strategy.` (6 files: `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`, two build reports under docs; 416 insertions, 7 deletions).
- `git -C /Users/cobalt/cobalt-wt/deploy-cos-outage rev-parse --short=8 HEAD` → `077cac06` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent c75d6b38..deploy/cos-outage` → `077cac06 Merge commit 'b5d62f17' into deploy/cos-outage` (one line, one head).
- `merge-base --is-ancestor de3e15c8 deploy/cos-outage` → exit 0; `merge-base --is-ancestor b5d62f17 deploy/cos-outage` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat c75d6b38 deploy/cos-outage -- src/cobalt/db_migrations` → nothing (no migration; `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat c75d6b38 deploy/cos-outage -- configs ops` →
  ```
   ops/desk/deploy-outage.sh | 11 ++++++-----
   ops/desk/deploy-step0.sh  |  4 ++--
   2 files changed, 8 insertions(+), 7 deletions(-)
  ```
  `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" c75d6b38 deploy/cos-outage` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-cos-outage` · `ls -la .../deploy-cos-outage/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first run built the worktree venv: `Using CPython 3.14.3 …`, `Installed 256 packages in 817ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-outage-1018-build-2026-10-18.result	A	DOCS	-
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>`: EMPTY (no resident goes down; the merge lands with the residents up). `<deferred set>`: empty. `<launchd set>`: empty.

## L68 GATE
- Equal-tree clause: does not hold (the check's stop line carries `with-DB 0/0`); the gate runs whole (`--deploy`).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 18.63s` — 0 failed (skips are with-DB tests: `Postgres env settings not available` / `requires_db`).
- THE GATE: `ls -la .../deploy-cos-outage/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-outage all --deploy --deploy-gate` (no `--deselect`: the build report names none for with-DB; `TICKERS: none`; `MIGRATIONS: none`) → exit 1. Verdict lines whole:
  ```
  tests/ops: run (deploy gate)
  offline 8657/0
  lock: waited 0 min
  proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
  LEVEL 0013
  pass 1: whole (deploy)
  RED (exit 1): 1 failed, 5374 passed, 8 skipped, 101 deselected, 7 xfailed, 43 warnings in 836.56s (0:13:56)
  SLOTS WARN user.aset_sizings max_attnum 1350 of 1600 · dropped 1296 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)
  1 failed, 5374 passed, 8 skipped, 101 deselected, 7 xfailed, 43 warnings in 836.56s (0:13:56)
  .env: removed
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-outage-all-20261018-205148.log
  ```
- (a) OFFLINE → `offline 8657/0`, green; W line `tests/ops: run (deploy gate)`.
- (b) lock taken (log 1003–1004: `lock taken: deploy-cos-outage`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log 1015); proof-only at `0013`, nothing CHANGED.
- (c) PASS 1 → **RED**. The one failure (log 1150–1171):
  ```
  _ TestTheLiveFactoryAuthenticatesAsCobaltApp.test_it_is_a_member_of_all_three_side_roles _
  >       assert [r[0] for r in rows] == ["cobalt_backup", "cobalt_system", "cobalt_user"]
  E       AssertionError: assert ['cobalt_appl...'cobalt_user'] == ['cobalt_back...'cobalt_user']
  E         At index 0 diff: 'cobalt_apply_system' != 'cobalt_backup'
  E         Left contains 2 more items, first extra item: 'cobalt_system'
  tests/cobalt/test_db_credentials.py:211: AssertionError
  ```
  `cobalt_app` on `cobalt_dev` is a member of `cobalt_apply_system` (and at least one more role) beyond the three side roles the test expects. Every SKIPPED line of pass 1 (log summary) is inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_playbook_live.py:31` (`COBALT_LIVE_VAULT_ROOT not set`), `test_radar_evaluate.py:695`, `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95`, `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2), (c3), (e): not run — the gate stops at the pass-1 red. `dev forward:` never APPLIED, so no rollback was owed.
- (f) / THE RELEASE: log 1281–1282 `$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-cos-outage` → `lock released`; gate printed `.env: removed`. Verified: `ls -la .../deploy-cos-outage/.env` → No such file; `grep -c -x -F "deploy-cos-outage" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- GATE RED on `077cac06` — no `GATE GREEN` line.

## Deploy table
Not reached. `main` not moved by a merge; no `pre-cos-outage` tag, no `deploy-2026-10-18-cos-outage` tag; no snapshot; no outage (`<restart set>` empty in any case); `migrations applied: none`. No ROLLBACK STRING: nothing merged.

## Smoke
Not reached.

## CONTINUE
Ended at STEP-G (c), 21:33 ET. Not resumable here (RECUT): the desk's next step is `desk-launch.sh recut "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/798-deploy-cos-outage-card.md"` after the red is resolved.

## DECISIONS
1. ASK DESK: the gate red `test_db_credentials.py::…::test_it_is_a_member_of_all_three_side_roles` is in a file this set does not ship (the set touches only `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh` and their two `tests/ops` files). The likely cause is the shared `cobalt_dev` role state: `cobalt_app` also holds `cobalt_apply_system`, maybe from DML-role work such as card 448. That cause is UNPROVEN (L70). Is the fix in that build or in `cobalt_dev`? [Sun Oct 18 21:33:30 EDT 2026]. Safe default taken: the run ends FAILED, nothing was carried as "known" (L68, L70), and nothing in `cobalt_dev` or production was touched.

## RECORDS
- Downtime: none (the outage never began).
- `cobalt_dev`: lock taken and released by `gate.sh`; forward never applied, so it stayed at `0013`. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`.
- The gate also printed `SLOTS WARN user.aset_sizings max_attnum 1350 of 1600 · dropped 1296 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)`. It is information only and not this run's to act on.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-cos-outage` and branch `deploy/cos-outage` (now at `077cac06`); the set's branch `ops/cos-outage-1018` stays for the recut.
- L74: a system reminder asked for a `Claude-Session:` line on commits. It was recorded under `## L74` and not acted on.
- Card `## RECORDS` (desk's), copied:
  - cos-outage-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-outage-1018-check-2026-10-18.md` last line: CHECK DONE · job: cos-outage-1018 · pass: 1 · tip: de3e15c8 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8612/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165134
  - cos-outage-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-outage-1018` → `b5d62f17`; code tip `de3e15c8`
  - written by deploy-card.sh at 2026-10-18 19:56 ET (`date`); trial merge of the heads onto main in order: clean
- PRE-STOP SELF-CHECK: (1) no smoke ran; (2) P3 re-read both tips, and STEP-T proved them ancestors of `deploy/cos-outage`; `<stack-final>` was never made; (3) no revert-readback is owed because nothing merged; every sha and count above is quoted from this run's tool output; (4) STEP-T merged clean (`Merge made by the 'ort' strategy.`), so no conflict marker exists.

FAILED: gate — G (c) — tests/cobalt/test_db_credentials.py::TestTheLiveFactoryAuthenticatesAsCobaltApp::test_it_is_a_member_of_all_three_side_roles · rollback: not used · decisions: 1 · for Dejan: 0 · tokens: 112285
