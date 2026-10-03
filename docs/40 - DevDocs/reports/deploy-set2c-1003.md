# deploy set2c-1003 — set: set2c — migrations: none

## §0 Headline
- DEPLOYED: set2c (`ops/rename-follow-up-1003` @ `8c32a8d1`, `ops/deploy-steps-1003` @ `f04a1d56`) is on `main` at `44b29c63`, tag `deploy-2026-10-03-2`. Card: `prompts/2026-10-03/26-deploy-set2c-card.md`.
- Gate green on `f99d81f6`: offline 3739/0 · with-DB 4581/0 · live-note 146/0. `cobalt_dev` back at 0013 (F2 = F0); lock released.
- Outage: `com.cobalt.radar` only, 17:22:45 → 17:22:56 EDT (11 s). No migration. aset and agent were not restarted.
- Smoke GREEN: markers flipped, radar cycling after `<t up>`, the four failure counts flat, heartbeat GREEN twice.
- Run 16:50:15 → 17:26 EDT, Sat 2026-10-03 (a non-trading day).

## L74
- A system block at launch asked commits to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" …/DEPLOY-HUB.md` | 1 | nothing |
| CARD placeholder | `grep -n -E "«FIL[L]" …/26-deploy-set2c-card.md` | 1 | nothing |
| CARD committed | `git log -1 --format=%H -- …/26-deploy-set2c-card.md` | 0 | `f0583263fc929b7900dd2cf14e9ee92ed2f6f6c9` |
| CARD clean | `git diff --stat -- …/26-deploy-set2c-card.md` | 0 | nothing |
| STANDING LIST R60 (cto-2026-09-30) | `grep -n "^| R60 "` | 0 | line 46: `**HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git log -1 -S"\| R60 \|"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| STANDING RULE R38 (cto-2026-09-30) | `grep -n "^| R38 "` | 0 | line 80: `**HIS RULINGS** … deploys self-launch on clean checks + green gate … \| APPROVED \|` |
| R38 committed | `git log -1 -S"\| R38 \|"` | 0 | `65aa2b90a8e3eb2f7e94ef10ed40b60e1b2ce542` |
| RULINGS R149 (cto-2026-10-02) | `grep -n "^| R149 "` | 0 | line 156: `HIS RULING: Saturday 10-03 is not a trading day; deploys may run any time that day … \| HIS RULING · APPROVED \|` |
| R149 committed | `git log -1 -S"\| R149 \|"` | 0 | `0e4fb85d7d07902e0db790f85e204f3537b83d61` |
| RULINGS R157 (cto-2026-10-02) | `grep -n "^| R157 "` | 0 | line 164: `HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|` |
| R157 committed | `git log -1 -S"\| R157 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la <REPORT>` | 1 | `No such file or directory` |
| P1 date/window | `date` | 0 | `Sat Oct  3 16:50:15 EDT 2026` — lawful under (iii) a non-trading day (Saturday by `date`); R149 states the same day |
| P2 row 1 | `tail -n 3 …/rename-follow-up-check-2026-10-03.md` | 0 | `CHECK DONE · job: rename-follow-up · pass: 1 · tip: 393f3ad5 · … · held unfixed: 0 · open: 0 · … · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0` — tip = row's code tip |
| P2 row 1 committed / clean | `git log -1 --format=%H` / `git diff --stat` | 0 / 0 | `903bf19a094f9f4be3ff263262c4730a665330c0` / nothing |
| P2 row 2 | `tail -n 3 …/deploy-steps-check-2026-10-03.md` | 0 | `CHECK DONE · job: deploy-steps · pass: 2 · tip: f04a1d56 · … · held: 9 · fixed: 9 · held unfixed: 0 · open: 0 · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · … · RESTARTS: none · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0` — tip = row's code tip |
| P2 row 2 committed / clean | `git log -1 --format=%H` / `git diff --stat` | 0 / 0 | `f60280e8616c163691c9b51afddc3f20916192c7` / nothing |
| P3 row 1 | `rev-parse --short=8 393f3ad5` · `rev-parse --short=8 ops/rename-follow-up-1003` · `merge-base --is-ancestor 393f3ad5 8c32a8d1` · `diff --stat 393f3ad5 8c32a8d1 -- . ':(exclude)docs'` | 0 · 0 · 0 · 0 | `393f3ad5` · `8c32a8d1` · ancestor · nothing |
| P3 row 2 | `rev-parse --short=8 f04a1d56` · `rev-parse --short=8 ops/deploy-steps-1003` · `merge-base --is-ancestor f04a1d56 f04a1d56` · `diff --stat f04a1d56 f04a1d56 -- . ':(exclude)docs'` | 0 · 0 · 0 · 0 | `f04a1d56` · `f04a1d56` · ancestor · nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` (nobody holds it) |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/set2c-1003` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `f0583263` |
| P5 m0 on main | `merge-base --is-ancestor f0583263 main` | 0 | ancestor |
| P5 gate holds nothing | `log --oneline main..deploy/set2c-1003` | 0 | empty |
| P6 marker 1 | `grep -c -F "The old side of a rename/copy" …/src/cobalt/jobs/restarts.py` | 1 | `0` (= before) |
| P6 marker 2 | `ls /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` | 1 | `No such file or directory` (= before) |
| P7 head 1 | `diff --stat main 8c32a8d1 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P7 head 2 | `diff --stat main f04a1d56 -- src/cobalt/db_migrations` | 0 | nothing |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 13209` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 13225` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge head 1 | `git -C <GATE> merge --no-edit 8c32a8d1` | 0 | `Merge made by the 'ort' strategy.` (4 files, 183 insertions) |
| merge head 2 | `git -C <GATE> merge --no-edit f04a1d56` | 0 | `Merge made by the 'ort' strategy.` (9 files, 3026 insertions) |
| m1 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m1>` = `f99d81f6` |
| merges | `log --oneline --merges --first-parent f0583263..deploy/set2c-1003` | 0 | `f99d81f6 Merge commit 'f04a1d56' into deploy/set2c-1003` · `d25e4e14 Merge commit '8c32a8d1' into deploy/set2c-1003` |
| ancestry | `merge-base --is-ancestor` 393f3ad5 · 8c32a8d1 · f04a1d56 → deploy/set2c-1003 | 0 · 0 · 0 | all ancestors |
| migrations | `diff --stat f0583263 deploy/set2c-1003 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| STEP-C | `diff --stat f0583263 deploy/set2c-1003 -- configs ops` | 0 | `ops/desk/deploy-outage.sh \| 442 +` · `ops/desk/deploy-smoke.sh \| 381 +` · `ops/desk/deploy-step0.sh \| 504 +` · `3 files changed, 1327 insertions(+)` — no plist added, modified or removed |

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv: `Creating virtual environment at: .venv` · `Installed 253 packages in 784ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-steps-build-2026-10-03.md	A	DOCS	-
docs/40 - DevDocs/reports/rename-follow-up-build-2026-10-03.md	A	DOCS	-
ops/desk/deploy-outage.sh	A	operator script; no Cobalt reader	-
ops/desk/deploy-smoke.sh	A	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	A	operator script; no Cobalt reader	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/ops/conftest.py	A	test/documentation; no resident	-
tests/ops/test_conftest_guard.py	A	test/documentation; no resident	-
tests/ops/test_deploy_outage.py	A	test/documentation; no resident	-
tests/ops/test_deploy_smoke.py	A	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar`.

## L68 GATE
- Set build reports read for added deselects: `rename-follow-up-build-2026-10-03.md` (c) "executed byte for byte (no added deselect)", "This build has no with-DB test id"; `deploy-steps-build-2026-10-03.md` names no pass-1 deselect (its check: with-DB 0/0). Added: none.
- (a0) `ls -la <GATE>/.env` → No such file · the early-read command → `261 passed, 157 skipped in 15.21s`; 0 failed (every skip: `Postgres env settings not available` / `requires_db`).
- (a) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 577.39s (0:09:37)`; 0 failed, 0 errors; no uv sync line. `<p>` = 3739.
- (e) `ls -la <GATE>/.env` → No such file · live-note command → `146 passed, 1 skipped, 15 warnings in 25.03s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (allowed); no skip naming `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.
- (b) `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh deploy-1003-4 90` → `lock taken: deploy-1003-4` (exit 0). `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  3 17:02 /Users/cobalt/cobalt-wt/deploy-1003-4/.env` (ours alone).
- (d2) `COBALT_ENV=production uv run cobalt validate` → exit 0; `<jobsG>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` · `registry <-> plists: schedules and COBALT_ENV agree on every job.` · `Placement (docs/PLACEMENT.md): tree clean.`
- `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `36 table(s) probed on cobalt_dev` · tables of 0014+ (`drc_*`, `legs`, `prediction_records`, `voice_turns`) print `-` → `0013`; no `CHANGED`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: f99d81f6 (clean)`.
- (c) PASS 1 (the hub's command byte for byte, no added deselect) → `4408 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 716.55s (0:11:56)`; 0 failed, 0 errors. SKIPPED, all inside the allowed set: `test_cards_picks.py:388` (S2-P2's card_score column is present on cobalt_dev) · `test_cards_picks.py:401` (real S2-P2 0007 applied …) · `test_radar_evaluate.py:695` (COBALT_LIVE_VAULT_ROOT not set) · `test_replay_line.py:266` (COBALT_TEST_LIVE_DRC not set) · `test_s3_c4_experiments.py:95` (`test_x14_live_his_template_strips_to_the_committed_fixture`, COBALT_LIVE_VAULT_ROOT not set) · `taxonomy/test_catalyst.py:365` · `taxonomy/test_predicate.py:262`. `<d1>` = 4408.
- (c2) `COBALT_ENV=dev uv run cobalt db migrate` → applied `0001`…`0011`, `0013`, `0014`…`0022` in order; 7 tables `CREATED`; `content UNCHANGED on every table.`; no `CHANGED`; `proof cost: BEFORE 6.3 s + AFTER 6.3 s = total 12.5 s`. **dev forward: APPLIED 17:15:44 EDT**. `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, byte for byte (nothing added) → `173 passed, 1 deselected, 5 warnings in 228.72s (0:03:48)`; 0 failed, 0 errors, no SKIPPED, no `DeadlockDetected`. `<d2>` = 173; `<d>` = 4408 + 173 = 4581.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → reversed `0022` … `0014` newest first; 7 tables `DROPPED`; `content UNCHANGED on every table.` `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **cobalt_dev: 0013 — F2 = F0**. Lock and `<GATE>/.env` held to the stop line (L76).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f99d81f6 — offline 3739/0 · with-DB 4581/0 · live-note 146/0 (17:20:20 EDT)

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git status --short --branch` | 0 | `## main...origin/main [ahead 147]` |
| main porcelain | `git status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (outside the accepted and the refused lists; see `## RECORDS`). No staged line; no dirty `src/` `tests/` `ops/` `configs/` path |
| main moved since cut | `diff --stat f0583263 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `tag scratch-allow-probe-set2c-1003` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-set2c-1003' (was f0583263)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 5d3e463d] scratch: …` · — · `f0583263 docs(desk): 10-03 R135-R137 …` (HEAD back) |
| TAG free | `rev-parse --verify --quiet refs/tags/deploy-2026-10-03-2` | 1 | free |
| rollback tag free | `rev-parse --verify --quiet refs/tags/pre-set2c-1003` | 1 | free |

### STEP-D1 (baseline, 17:20:42 EDT)
- `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 17:20:43 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.radar             running   running 1413 min, heartbeat fresh`; `AMB  com.cobalt.herdr unmanaged … by declared interim`. No RED.
- `<val0>`: validate exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · `registry <-> ops/: 15 label(s), exact match.` · `registry <-> plists: schedules and COBALT_ENV agree on every job.`
- `backup status` → `newest snapshot: 6.0 h old` (ssd ARMED).
- aset `state = running`, `<aset pid>` = 13209 · radar `state = running`, `<radar pid>` = 13225 · `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-03 17:20:25.311 | INFO | cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None`, no traceback.
- Log baselines: `<a0>` 42 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 39 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: marker 1 `0`, marker 2 `No such file or directory` (= before).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `add` + `commit … -- deploy-set2c-1003.md` → `[main bec2a990] docs(report): deploy set2c-1003 — gate green on f99d81f6` · `1 file changed, 132 insertions(+)`; `show --stat HEAD` lists that one file. `<pre-merge>` = `bec2a990`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `44b29c63`; `rev-parse --short=8 44b29c63^2` → `bec2a990` = `<pre-merge>`; `merge-base --is-ancestor f99d81f6 44b29c63` → exit 0.
- D2.3 `diff --stat f99d81f6 44b29c63 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` before → `newest snapshot: 6.0 h old`; `backup run` → `backup: cobalt_brain dumped, 4460.3 MB` · `ssd: snapshot e1955ef4 — 0 new / 3 changed, 11.3 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` 17:22:05 · heartbeat `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red (2026-10-03 17:22:06 EDT)` — 83 s after D1's; one more pair taken for the ≥110 s rule: `date` 17:22:32 · heartbeat `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red (2026-10-03 17:22:34 EDT)` — 111 s after D1's; no RED; `com.cobalt.radar running … heartbeat fresh`.
- D2.6 `date` → `Sat Oct  3 17:22:38 EDT 2026`: still a non-trading day (P1 (iii)). `git -C /Users/cobalt/cobalt tag pre-set2c-1003` at `bec2a990` → exit 0.

### STEP-4 (restart set: com.cobalt.radar)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = 17:22:45 EDT |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print …radar` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/set2c-1003` | `bec2a990` = `<pre-merge>` · `Updating bec2a990..44b29c63` `Fast-forward` (13 files, 3209 insertions) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`; `registry <-> ops/: 15 label(s), exact match.`; `Placement … tree clean.` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print …radar` | exit 0 · `state = running`, `pid = 18818` (≠ 13225) |
| t up | `date` | `<t up>` = 17:22:56 EDT · downtime 11 s |

### STEP-7 summary
| item | value |
|---|---|
| main | `<pre-merge>` `bec2a990` → `<stack-final>` `44b29c63` (`rev-parse --short=8 HEAD` → `44b29c63`) |
| tags | `pre-set2c-1003` at `bec2a990` · `deploy-2026-10-03-2` at `44b29c63` (set after the green smoke) |
| outage | `<t down>` 17:22:45 · `<t up>` 17:22:56 · 11 s |
| uv sync | none in production; gate venv created once at STEP-R (`Installed 253 packages in 784ms`) |
| proof cost | not applicable (no production migration); dev forward and rollback each `total 12.x s` |
| migrations applied | none |
| `<RB>` | none (no migration) |
| snapshot | `e1955ef4` (ssd), taken at D2.4 |
| RESTARTS done | `com.cobalt.radar` |

ROLLBACK STRING (the desk's):
1. CODE: `launchctl bootout gui/501/com.cobalt.radar`, then `git -C /Users/cobalt/cobalt revert --no-edit -m 2 44b29c63`, then `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

PRE-STOP SELF-CHECK: (1) every smoke row above is quoted with its `date`. (2) `merge-base --is-ancestor` 393f3ad5, 8c32a8d1, f04a1d56 → 44b29c63: exit 0 each. (3) REVERT-READBACK (h) is shown; every count and sha in this report was copied from this run's tool output. (4) STEP-T ran clean (two `ort` merges); `git -C <GATE> status --short --branch` → `## deploy/set2c-1003` (no conflict state).

## Smoke
- FIRST CALLS after `<t up>` (17:22:56): `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 39 · `<lc_up>` 39 (= D1 baselines).
- (a) 17:23:09 — aset `state = running`, `pid = 13209` (SAME; outside the set) · radar `state = running`, `pid = 18818` (NEW; in the set) · `Cobalt is ONLINE (PID: 22243).` (same; outside the set). GREEN.
- (b) 17:23:13 — `grep -c "Started server process" aset.err` → `42` = `<a0>` (aset outside the set) · `tail -n 30 aset.err` → last start `INFO:     Started server process [13215]` (2026-10-02 17:47) then `Uvicorn running on http://0.0.0.0:5010`; no new start · Tracebacks aset `2` = `<ta0>` · radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`. Radar tails: below.
- (c) 17:23:18 — `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200`. GREEN.
- (d) 17:23:18 — marker 1 `grep -c -F "The old side of a rename/copy" …/restarts.py` → `1` (after `1`) · marker 2 `ls …/ops/desk/deploy-step0.sh` → listed. GREEN.
- (s) 17:23:23 — rename old-side test: `grep -c -F "def test_" …/tests/cobalt/test_jobs_restarts.py` → `19`, exit 0 (≥ 1) · deploy step scripts: `ls …/deploy-outage.sh …/deploy-smoke.sh` → both listed, exit 0. GREEN.
- (f) 17:23:2x — `cobalt jobs restarts bec2a990..44b29c63` → exit 0, `RESTARTS: com.cobalt.radar` = STEP-R's set, no `UNCLASSIFIED` · `cobalt validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`, `registry <-> ops/: 15 label(s), exact match.`, `Placement … tree clean.` (as 4.5). GREEN.
- (e) read 1 — `date` 17:23:26 · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 17:23:27 EDT)`; `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh`.
- (g) no migration.
- (b) radar tails: tail 1 at `date` 17:24:28 (`<t up>`+92 s) → last cycle `2026-10-03 17:22:55.400 … radar cycle: idle:overnight scan_id=None` (before `<t up>` by under 1 s; not counted) · tail 2 at `date` 17:25:59 (`<t up>`+183 s) → `2026-10-03 17:24:35.422 | INFO | cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None`, after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the tail → GREEN (settled; tail 3 not needed).
- (e) read 2 — `date` 17:25:21 · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 17:25:22 EDT)` (115 s after read 1); `OK   com.cobalt.radar             running   running 2 min, heartbeat fresh`. No RED. GREEN. (The clock between reads was filled with `date` + `heartbeat show` pairs; every one read GREEN.)
- (h) REVERT-READBACK at `date` 17:26:03 (`<t up>`+187 s, after (b) settled): `radar panel FAILED` 17 · `radar pool refresh FAILED` 58 · `radar S5 evaluate FAILED` 39 · `lifecycle card read failed` 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `/radar` `200` · radar Traceback `0`. No census reads (no migration). GREEN.

THE CHAIN: every check committed (P2: `903bf19a`, `f60280e8`) → tips re-read (P3: `393f3ad5`/`8c32a8d1`, `f04a1d56`) → merged tree `f99d81f6` (T, two clean `ort` merges) → RESTARTS derived `com.cobalt.radar` (R) → three suites green on `f99d81f6` (G) → `44b29c63` = `f99d81f6` + docs (D2.3) → landed by fast-forward `bec2a990..44b29c63` (4.3) → markers after (d) → no migration (g) → radar up on a new pid, aset and agent unchanged (a) → radar cycling and heartbeat GREEN (b, e) → set reads green (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

**smoke: GREEN**

## CONTINUE
- STEP-D0 done; STEP-D1 done; STEP-D2 done.
- OUTAGE STARTING 17:22:38 EDT — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- OUTAGE ENDED 17:22:56 EDT — radar up (pid 18818) on 44b29c63.
- Smoke GREEN 17:26:03; tag set; lock released 17:26:16. Run closed.

## DECISIONS
none

## RECORDS
- Downtime: 11 s (`com.cobalt.radar` only); under 300 s.
- `cobalt_dev: 0013 (F2 = F0)` — `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` before and after.
- `.env: removed (L76 lock released 17:26:16 EDT)` — `release-devdb-lock.sh deploy-1003-4` → `lock released`; `ls -la <GATE>/.env` → No such file.
- RETIRE OWED: none (no plist removed).
- Carried RED: none; every heartbeat this run read `HEARTBEAT GREEN … nothing red`. The standing `AMB com.cobalt.herdr unmanaged` line was in `<hb0>` and stayed the same.
- REFUSED, not needed: none. No `CONTINUE` message or message from another session arrived.
- Cleanup owed (L46, the desk's): gate worktree `/Users/cobalt/cobalt-wt/deploy-1003-4` and branch `deploy/set2c-1003`; the set's branches `ops/rename-follow-up-1003`, `ops/deploy-steps-1003` and their worktrees.
- Push is his (L55): `main` is ahead of `origin/main`; the tags `pre-set2c-1003`, `deploy-2026-10-03-2` are local.
- L74: one `Claude-Session:` request, recorded under `## L74`; not acted on.
- Card `## RECORDS`, copied:
  - rename-follow-up: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rename-follow-up-check-2026-10-03.md` last line: CHECK DONE · job: rename-follow-up · pass: 1 · tip: 393f3ad5 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0
  - rename-follow-up: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/rename-follow-up-1003` → `8c32a8d1`; code tip `393f3ad5`
  - deploy-steps: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-steps-check-2026-10-03.md` last line: CHECK DONE · job: deploy-steps · pass: 2 · tip: f04a1d56 · house B: Sol FINDINGS: 11 · findings: 11 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 0 · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0
  - deploy-steps: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-steps-1003` → `f04a1d56`; code tip `f04a1d56`
  - re-cut of card `25` (deploy `set2b-1003` FAILED at STEP-C on `05`'s plist); rows unchanged from card `23` rows 2 and 4, preflighted (R131); neither adds a plist or a `db_migrations` file. MARKERS, SMOKE READS filled by the desk at 16:49 ET.
  - written by deploy-card.sh at 2026-10-03 16:49 ET (`date`); trial merge of the heads onto main in order: clean
- D0: `?? .claude/settings.json.bak` is untracked on `main`; D0 neither accepts nor refuses it (not under `docs/40 - DevDocs/`, not `src/` `tests/` `ops/` `configs/`, not staged). Recorded, not a stop; the file is the desk's.

DEPLOYED deploy-2026-10-03-2 44b29c63 | set: set2c | migrations: none | gate: offline 3739/0 · with-DB 4581/0 · live-note 146/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0
