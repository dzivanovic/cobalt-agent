# Deploy f20-cos (attempt 2) · SET: cos · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/f20-cos-fr1` (head `83919213`, code tip `753094da`) through gate branch `deploy/f20-cos-attempt2`.
- Started `Mon Oct 19 05:30:11 EDT 2026`.

## L74
- An attribution note in a system reminder asked for a `Claude-Session:` line on commits. Recorded here as data. Not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md"` → exit 0, whole output:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/808-deploy-f20-cos-card.md" · 0 · 40e646edf7264b21191b2b63f5fbbb2dede793c7
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
First launch: `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f20-cos-attempt2.md"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Mon Oct 19 05:30:11 EDT 2026`, outside 21:30-22:30 ET |
| P2 tail | `tail -n 3 ".../reports/f20-cos-fr1-check-2026-10-19.md"` | 0 | `CHECK DONE · job: f20-cos-fr1 · pass: 1 · tip: 753094da · house A: Grok FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8725/0 · with-DB 5663/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 6 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 193794`. It carries `held unfixed: 0` and `ready: YES`, and `tip: 753094da` = the code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md"` | 0 | `186bcca02e9786a245e81c41eafcf66adb3c0391` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 753094da` | 0 | `753094da` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f20-cos-fr1` | 0 | `83919213` = row = `TIP` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 753094da 83919213` | 0 | ancestor |
| P3 reports only | `git -C /Users/cobalt/cobalt diff --stat 753094da 83919213 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 status | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos-attempt2 status --short --branch` | 0 | `## deploy/f20-cos-attempt2` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos-attempt2 rev-parse --short=8 HEAD` | 0 | `<m0>` = `40e646ed` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 40e646ed main` | 0 | ancestor |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f20-cos-attempt2` | 0 | empty |
| P6 marker 1 | `grep -c -F "label: com.cobalt.cos" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` | 0 | `0` = before |
| P6 marker 2 | `grep -c -F "hitl_dirs:" /Users/cobalt/cobalt/configs/cobalt/generated.yaml` | 0 | `0` = before |
| P6 marker 3 | `grep -c -F "claude-agent-sdk==" /Users/cobalt/cobalt/pyproject.toml` | 0 | `0` = before |
| P7 two-dot | `git -C /Users/cobalt/cobalt diff --stat main 83919213 -- src/cobalt/db_migrations` | 0 | `0025_dml_roles.rollback.sql 33 -` · `0025_dml_roles.sql 77 -` · `__init__.py 8 -` · `placement.py 6 +`. The 0025 lines belong to `main`. They show as removals because `main` has moved past the head's base (DECISIONS 1) |
| P7 head's own | `git -C /Users/cobalt/cobalt diff --stat main...83919213 -- src/cobalt/db_migrations` | 0 | `src/cobalt/db_migrations/placement.py | 6 ++++++`. This is CODE, not a migration, so `MIGRATIONS: none` holds. STEP-T's `<m0>..<BRANCH>` stat is the binding check |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 89330` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 86221` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| T merge | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos-attempt2 merge --no-edit 83919213` | 0 | `Merge made by the 'ort' strategy.` (66 files changed, 4873 insertions(+), 11 deletions(-)) |
| T m1 | `git -C /Users/cobalt/cobalt-wt/deploy-f20-cos-attempt2 rev-parse --short=8 HEAD` | 0 | `<m1>` = `dd360826` |
| T merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 40e646ed..deploy/f20-cos-attempt2` | 0 | `dd360826 Merge commit '83919213' into deploy/f20-cos-attempt2` |
| T code tip | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 753094da deploy/f20-cos-attempt2` | 0 | ancestor |
| T head | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 83919213 deploy/f20-cos-attempt2` | 0 | ancestor |
| T migrations | `git -C /Users/cobalt/cobalt diff --stat 40e646ed deploy/f20-cos-attempt2 -- src/cobalt/db_migrations` | 0 | `src/cobalt/db_migrations/placement.py | 6 ++++++`. CODE only, no migration path, so `MIGRATIONS: none` holds |
| C configs/ops | `git -C /Users/cobalt/cobalt diff --stat 40e646ed deploy/f20-cos-attempt2 -- configs ops` | 0 | `configs/cobalt/agents/cos.yaml | 34` · `configs/cobalt/generated.yaml | 8` · `configs/cobalt/jobs.yaml | 31` · `configs/cobalt/taxonomy/tunables.yaml | 64` · `ops/com.cobalt.cos.plist | 37` · `ops/start_cos.sh | 32` · `6 files changed, 206 insertions(+)` |
| C script | `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 40e646ed deploy/f20-cos-attempt2` | 0 | `ADMITTED: com.cobalt.cos · add · deferred` / `BOOTSTRAP OWED: com.cobalt.cos — D14, agent stopped, X1, X13, X2, X10, X3, X14, X11, X12, X15, X17, X18, X20` / `STEP-C: ADMITTED 1` |

`<launchd set>`: empty. `<deferred set>`: `com.cobalt.cos`.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-f20-cos-attempt2` · `ls -la .../.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0. The first run created the worktree `.venv` (`Installed 257 packages in 922ms`). Table, whole:
```
path	change	rule	restart
configs/cobalt/agents/cos.yaml	A	resident reads	com.cobalt.cos
configs/cobalt/generated.yaml	M	no resident reads (one-shot: com.cobalt.generated)	-
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/40 - DevDocs/cobalt/agents/README.md	A	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cos/README.md	A	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/placement.md	M	DOCS	-
docs/40 - DevDocs/cobalt/generated/committer.md	M	DOCS	-
docs/40 - DevDocs/cobalt/generated/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/hitl/README.md	A	DOCS	-
docs/40 - DevDocs/reports/f20-cos-fr1-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/f20-cos-fr1-build-2026-10-18.result	A	DOCS	-
ops/com.cobalt.cos.plist	A	plist in diff	com.cobalt.cos
ops/start_cos.sh	A	resident reads	com.cobalt.cos
pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/agents/__init__.py	A	static import reach	com.cobalt.radar
src/cobalt/agents/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/agents/registry.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/cos/__init__.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/cos/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/cos/listener.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/cos/migrations/0001_cobalt_cos.sql	A	non-Python src asset	-
src/cobalt/cos/run.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/cos/session.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/cos/store.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/cos/tools.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/generated/committer.py	M	static import reach	com.cobalt.radar
src/cobalt/generated/config.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/runner.py	M	static import reach	com.cobalt.radar
src/cobalt/hitl/__init__.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/actions.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/card.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/hitl/executor.py	A	static import reach	com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/migrations/0001_cobalt_hitl.sql	A	non-Python src asset	-
src/cobalt/hitl/models.py	A	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/store.py	A	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/fixtures/cos/dm-posts.redacted.json	A	test/documentation; no resident	-
tests/cobalt/hitl_support.py	A	test/documentation; no resident	-
tests/cobalt/test_agents_registry.py	A	test/documentation; no resident	-
tests/cobalt/test_cos_db.py	A	test/documentation; no resident	-
tests/cobalt/test_cos_listener.py	A	test/documentation; no resident	-
tests/cobalt/test_cos_offline.py	A	test/documentation; no resident	-
tests/cobalt/test_cos_probes.py	A	test/documentation; no resident	-
tests/cobalt/test_cos_registry.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_web_seam.py	M	test/documentation; no resident	-
tests/cobalt/test_generated_hitl_dirs.py	A	test/documentation; no resident	-
tests/cobalt/test_hitl_db.py	A	test/documentation; no resident	-
tests/cobalt/test_hitl_executor.py	A	test/documentation; no resident	-
tests/cobalt/test_hitl_offline.py	A	test/documentation; no resident	-
tests/cobalt/test_hitl_web.py	A	test/documentation; no resident	-
tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. `RESTARTS:` minus `<deferred set>` (`com.cobalt.cos`) → `<restart set>` = `com.cobalt.agent com.cobalt.aset com.cobalt.radar`.
`<deferred set>` = `com.cobalt.cos` (merged, not loaded, `BOOTSTRAP OWED`).
`<launchd set>` = empty.

## L68 GATE
THE EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 753094da dd360826 -- . ":(exclude)docs"` → 31 files (`main`'s 0025 dml_roles set, `db_apply.py`, `ops/desk/*`, tests), so the trees are not equal and the gate runs whole (`--deploy`). Deselects: none. The build report `f20-cos-fr1-build-2026-10-18.md:134` says its with-DB files ran in pass 1 at 0013 and none was deselected. `TICKERS: none` → no `--tickers`. `MIGRATIONS: none` → no `--migration`.
- (a0) `ls -la .../.env` (No such file) · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 19.57s`, 0 failed. Every skip names `Postgres env settings not available` or `requires_db: needs cobalt_dev` (with-DB, offline).
- THE GATE: `ls -la .../.env` (No such file) · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f20-cos-attempt2 all --deploy --deploy-gate`, run in the background → exit 0. Verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8744/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5691/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f20-cos-attempt2-all-20261019-053233.log
```
- (a) offline `8744/0`. W line: `tests/ops: run (deploy gate)`.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:1031). The proof-only at 0013 shows no `CHANGED` (log:1083).
- (c) pass 1 → `5458 passed, 8 skipped, 127 deselected, 7 xfailed, 43 warnings in 893.94s` (log:1252). All 8 skips are inside the allowed set: `test_cards_picks.py:388` and `:401`, `test_playbook_live.py` (`COBALT_LIVE_VAULT_ROOT not set`), `test_radar_evaluate.py:695`, `test_replay_line.py` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` (the live template read), `test_catalyst.py:365` and `test_predicate.py:262`.
- (c2) `dev forward: APPLIED 06:15:29` (log:1254). The proof table reads `content UNCHANGED on every table` (log:1323).
- (c3) pass 2 → `233 passed, 1 deselected, 5 warnings in 244.17s` (log:2174). with-DB `5691/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:2243) = F0 · `cobalt_dev: 0013 — F2 = F0` (log:2295).
- THE RELEASE: `release-devdb-lock.sh deploy-f20-cos-attempt2` → `lock released` (log:2297) · `.env: removed` (log:2301). The log line carries no time stamp; the release came after 06:15:29 and before 06:20:56. Checked here: `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-f20-cos-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- (e) live-note `147/0` (`147 passed, 1 skipped`, log:2367; the one skip is the allowed `COBALT_TEST_LIVE_DRC` one).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on dd360826

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 55]`. Dirty lines: ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` / `??` under `docs/40 - DevDocs/`, and `?? .claude/settings.json.bak` (not under `src/`, `tests/`, `ops/` or `configs/`; RECORDS) |
| D0 porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line, no dirty `src/`, `tests/`, `ops/` or `configs/` path other than `configs/cobalt/rules.yaml` |
| D0 moved | `git -C /Users/cobalt/cobalt diff --stat 40e646ed main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 probe | `tag scratch-allow-probe-f20-cos` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-f20-cos' (was a6899a57)` |
| D0 probe | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main b68aa7bd] scratch: allowlist probe (reverted next line)`, then HEAD back at `a6899a57 docs(desk): preflight r4 ready YES, F5 731 CONTINUE E2, R1983` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-f20-cos-attempt2` · `… refs/tags/pre-f20-cos` | 1 · 1 | both free |
| D1 date | `date` | 0 | `Mon Oct 19 06:21:25 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-19 06:21:26 EDT)`. Radar `scanning (premarket), members 50`; `com.cobalt.radar running 271 min, heartbeat fresh`; aset pid 89330; agent pid 89351. `AMB com.cobalt.herdr unmanaged` (declared interim). `com.cobalt.prefill-refresh` and `com.cobalt.playbook` are `OWED (deferred bootstrap)`. No RED |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` No failing line |
| D1 `<jobs0>` | (validate) | 0 | `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 17 label(s), exact match.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 3.5 h old` (ssd ARMED) |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `pid = 89330` |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `pid = 86221` |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 89351` | 0 · 0 | `Cobalt is ONLINE (PID: 89351).` · `89351 ?? 0:00.03 uv run src/cobalt_agent/main.py` |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last `2026-10-19 06:21:13.244 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792405194619`, no traceback |
| D1 baselines | `grep -c` × 8 | 0 | `<a0>` 283 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 markers | the three `## MARKERS` greps | 0 | `0` · `0` · `0` = before |
| D1 launchd set | (empty) | — | nothing |
| D1 migration | `MIGRATIONS: none` | — | `<RB>`, census and D1-M not run |
| D2.0 shipped | `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 40e646ed "<card>"` | 0 | nothing |

## Smoke

## CONTINUE
next: STEP-D2 (D2.0 report commit, then D2.1 main into the gate)

## DECISIONS
1. P7 reads the two-dot diff `main 83919213`. That diff shows `main`'s own `0025_dml_roles` files and `__init__.py` lines as removals, because `main` has moved since the head's base. The head's own diff (`main...83919213`) adds no migration, only `placement.py` (CODE). Safe default, the same as attempt 1: P7 passes, and STEP-T's `<m0>..<BRANCH>` stat is the binding check. Not FOR DEJAN.

## RECORDS
- Card `## RECORDS` (the desk's, copied):
  - f20-cos-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md` last line: CHECK DONE · job: f20-cos-fr1 · pass: 1 · tip: 753094da · house A: Grok FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8725/0 · with-DB 5663/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 6 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 193794
  - f20-cos-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f20-cos-fr1` → `83919213`; code tip `753094da`
  - written by deploy-card.sh at 2026-10-19 05:25 ET (`date`); trial merge of the heads onto main in order: clean

(run in progress — next step under ## CONTINUE)
