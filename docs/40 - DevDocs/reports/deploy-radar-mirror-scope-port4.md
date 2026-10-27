# deploy radar-mirror-scope-port4 · set: radar-mirror-scope-port4 · migrations: none

## §0 Headline
- DEPLOYED `ops/radar-mirror-scope-port4` (code tip `b0cca7d7`, head `421af171`) on card 1074. `main` is now `05a21999`, tagged `deploy-2026-10-26-radar-mirror-scope-port4`; the rollback tag `pre-radar-mirror-scope-port4` is at `88e2f5f9`.
- The gate was green on `247cfe42` under the equal-tree clause: offline 9144/0 · with-DB 5980/0 · live-note 148/0. Migrations: none.
- Residents `com.cobalt.aset com.cobalt.cos com.cobalt.radar` were down 58 s (20:41:40 → 20:42:38 ET). They came back with new pids, and smoke is GREEN.
- The REDs before and after are the same: agent (recorded retired) and replay (`TraderSettingsError`). Neither is new.

## L74
- The session's harness reminder asked that commits carry a `Claude-Session:` line. This is recorded as DATA and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md" · 0 · d3d669a5c715660c6e4b0e4e8bebd576503c15fb
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
First launch: `ls -la "<REPORT>"` → `No such file or directory` (exit 1).

| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 26 20:36:23 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../radar-mirror-scope-port4-check-2026-10-26.md"` | 0 | `CHECK DONE · job: radar-mirror-scope-port4 · pass: 1 · tip: b0cca7d7 · house A: Grok FINDINGS: 0 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 9144/0 · with-DB 5980/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 190063`: carries `held unfixed: 0` and `ready: YES`, and `tip: b0cca7d7` = the code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/radar-mirror-scope-port4-check-2026-10-26.md"` | 0 | `94894ab18f1d6ee9e3827da9f6e5aa23f1f6e387` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 b0cca7d7` | 0 | `b0cca7d7` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port4` | 0 | `421af171` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b0cca7d7 421af171` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat b0cca7d7 421af171 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-mirror-scope-port4` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `d3d669a5` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d3d669a5 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/radar-mirror-scope-port4` | 0 | empty |
| P6 | `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` | 2 | `grep: /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py: No such file or directory`: the file is absent, so production does not carry the marker (this is the before state; the set adds the file) |
| P6 | `grep -c -F "def warm_config" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 421af171 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 58145` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 58164` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1`: `com.cobalt.agent recorded retired` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (expected with the agent retired) |

## THE TREE
- `git -C <GATE> merge --no-edit 421af171` → `Merge made by the 'ort' strategy.` (13 files changed, 713 insertions(+), 16 deletions(-)). No conflict.
- `git -C <GATE> rev-parse --short=8 HEAD` → `247cfe42` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent d3d669a5..deploy/radar-mirror-scope-port4` → `247cfe42d Merge commit '421af171' into deploy/radar-mirror-scope-port4` (one merge for one head).
- `merge-base --is-ancestor b0cca7d7 deploy/radar-mirror-scope-port4` → exit 0; `merge-base --is-ancestor 421af171 deploy/radar-mirror-scope-port4` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat d3d669a5 deploy/radar-mirror-scope-port4 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat d3d669a5 deploy/radar-mirror-scope-port4 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" d3d669a5 deploy/radar-mirror-scope-port4` → exit 0, `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, `Installed 257 packages in 842ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port4-build-2026-10-26.md	A	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port4-build-2026-10-26.result	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_config_warmup.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- No `UNCLASSIFIED` row. `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `pid = 58158`: cos stays in the set.
- `<restart set>`: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`
- `<deferred set>`: empty
- `<launchd set>`: empty
- com.cobalt.agent: recorded retired — not restarted (the tool's set did not name it)

## L68 GATE
THE EQUAL-TREE CLAUSE holds. There is ONE branch in `TIP`, and `git -C /Users/cobalt/cobalt diff --stat b0cca7d7 247cfe42 -- . ":(exclude)docs"` prints nothing. The check's stop line carries `with-DB 5980/0` (> 0). The check's three suite lines are therefore the gate's, and (a)–(f) are skipped. They are quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port4-check-2026-10-26.md` `## Suites` (lines 225–245):
```
tests/ops: run (deploy gate)
offline 9144/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5980/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-port4-all-20261026-193449.log
```
- Skips read against the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365` and `test_predicate.py:262` are named in the set. So are the `test_checkpoints_live.py` and `test_playbook_live.py` skips (reason `COBALT_LIVE_VAULT_ROOT not set`), the `test_replay_line.py` skip (`COBALT_TEST_LIVE_DRC`) and the `test_s3_c4_experiments.py` x14 skip. All nine are inside the set.
- The lock was not taken by this run: `<GATE>/.env` was never present, and P4 found no `.env` in any worktree.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 247cfe42

## Deploy table

### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 142]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line. ` M` lines: `.claude/settings.json`, `configs/cobalt/rules.yaml` and paths under `docs/40 - DevDocs/`. `??` lines under `docs/40 - DevDocs/`, plus one `?? .claude/settings.json.bak` (see `## DECISIONS`). No dirty `src/`, `tests/` or `ops/` path. |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat d3d669a5 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-radar-mirror-scope-port4` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-radar-mirror-scope-port4' (was d3d669a5c)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 6bc2af6d2] scratch: allowlist probe (reverted next line)` → `d3d669a5c docs(desk): R2526 deploy card 1074 for port4` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-26-radar-mirror-scope-port4` | 1 | absent |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-radar-mirror-scope-port4` | 1 | absent |

### STEP-D1 (baseline)
- `date` → `Mon Oct 26 20:38:51 EDT 2026`.
- `<hb0>` from `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-26 20:38:52 EDT)`.
  - The aset, sheet and radar probes are OK: `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200`, `OK   radar                    paused (market_reset)`, `OK   com.cobalt.aset              running   loaded, pid 58145 [launchd probe]`, `OK   com.cobalt.radar             running   running 198 min, heartbeat fresh`, `OK   com.cobalt.cos               running   running 198 min, heartbeat fresh`.
  - REDs, named and not a stop:
    - `RED  com.cobalt.agent             not loaded NOT LOADED in launchd — …`: the agent is recorded retired.
    - `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`
  - `AMB  com.cobalt.herdr` is unmanaged.
  - OWED (deferred bootstrap): `prefill-refresh`, `checkpoint-0715`, `checkpoint-0745`, `checkpoint-0815`, `checkpoint-0845`, `playbook`.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`): `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`. No `docs/_inflight/` line. `<jobs0>`: `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 3.3 h old` (`ssd   local ARMED /Volumes/COBALT-BACKUP/restic`).
- `launchctl print`: aset `state = running`, `<aset pid>` 58145; radar `state = running`, `<radar pid>` 58164; cos `state = running`, `<cos pid>` 58158.
- `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (the agent is recorded retired, so there is no `ps -p`).
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: paused_market_reset scan_id=None`, the last stamped `2026-10-26 20:38:21.326`. No traceback.
- LOG BASELINES: `<a0>` 300 · `<ta0>` 217 · `<tr0>` 1 · `<tc0>` 0 · `<rp0>` 31 · `<rpr0>` 60 · `<re0>` 750 · `<lc0>` 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`.
- MARKERS again: `0` · `No such file or directory` (the file is absent, so not carried) · `0`. All are at their before values.
- THE LAUNCHD SET: empty. No migration: there is no `<RB>` and no D1-M.

### STEP-D2
- D2.0: `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved d3d669a5 "<card>"` → nothing. The report was committed as `88e2f5f93 docs(report): deploy radar-mirror-scope-port4 — gate green on 247cfe42`, and `show --stat HEAD` lists the one report file. `<pre-merge>` = `88e2f5f9`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report file only).
- D2.2: `<stack-final>` = `05a21999`. `rev-parse --short=8 05a21999^2` → `88e2f5f9` = `<pre-merge>`. `merge-base --is-ancestor 247cfe42 05a21999` → exit 0.
- D2.3: `git -C /Users/cobalt/cobalt diff --stat 247cfe42 05a21999 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4: `backup status` before → `newest snapshot: 3.4 h old`. `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 10661.4 MB` · `ssd: snapshot 86367082 — 0 new / 3 changed, 1420.8 MB added, 1 pruned`. `backup status` after → `newest snapshot: 0.0 h old`. Snapshot id: `86367082`.
- D2.5: `date` → `Mon Oct 26 20:41:17 EDT 2026`. `heartbeat show` (`2026-10-26 20:41:17 EDT`) is 145 s after D1's read. It shows the same two REDs as `<hb0>` (agent, replay) and no new RED. aset is `running loaded, pid 58145`; radar is `running 200 min, heartbeat fresh`; cos is `running 200 min, heartbeat fresh`.
- D2.6: `date` → `Mon Oct 26 20:41:23 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-radar-mirror-scope-port4` at `<pre-merge>` `88e2f5f9` → exit 0.

### STEP-4 (the outage)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `Mon Oct 26 20:41:40 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `print` | 0 · 113 | `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.cos` · `print` | 0 · 113 | `Could not find service "com.cobalt.cos" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `print` | 0 · 113 | `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.2 | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` (dry run) | 0 | `orphan-clean: aset · none found` (no kill) |
| 4.2 | agent | — | not in the set (recorded retired) |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `88e2f5f9` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/radar-mirror-scope-port4` | 0 | `Updating 88e2f5f93..05a219990` / `Fast-forward` (13 files, 713+ / 16-) |
| 4.4 | — | — | migrations applied: none |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | as `<val0>`: `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `print` | 0 · 0 | `state = running`, `pid = 76357` (≠ 58145) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` · `print` | 0 · 0 | `state = running`, `pid = 76369` (≠ 58158) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `print` | 0 · 0 | `state = running`, `pid = 76377` (≠ 58164) |
| 4.6 | `date` | 0 | `Mon Oct 26 20:42:38 EDT 2026` = `<t up>`; downtime 58 s |
| 4.6L | — | — | `<launchd set>` empty: nothing |

### STEP-7 close
- `<pre-merge>` `88e2f5f9` → `<stack-final>` `05a21999` (main tip).
- Tags: `pre-radar-mirror-scope-port4` at `88e2f5f9`; `deploy-2026-10-26-radar-mirror-scope-port4` at `05a21999`, set after the green smoke.
- `<t down>` `20:41:40` / `<t up>` `20:42:38` / 58 s.
- uv sync: none in production. The gate worktree's first `uv run` created `.venv`: `Installed 257 packages in 842ms`. The aset log shows `Resolved 267 packages` / `Audited 257 packages`.
- Proof cost: none (no migration). Migrations applied: none. `<RB>`: none.
- Snapshot id: `86367082` (ssd).
- RESTARTS done: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
- LAUNCHD done: none. BOOTSTRAP OWED: none from this set.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 05a21999`. Boot out `com.cobalt.aset`, `com.cobalt.cos` and `com.cobalt.radar` first, and bootstrap them after. There are no launchd-set labels.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 31 · `<rpr_up>` 60 · `<re_up>` 750 · `<lc_up>` 39 (each equals the D1 baseline).
- (a) [`Mon Oct 26 20:42:57 EDT 2026`] the 4.6 prints show aset `state = running`, pid 76357 (≠ 58145); cos `state = running`, pid 76369 (≠ 58158); radar `state = running`, pid 76377 (≠ 58164). `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (the agent is recorded retired, so OFFLINE is green). GREEN.
- (b) [`Mon Oct 26 20:42:57 EDT 2026`] `grep -c "Started server process" …/aset.err` → `301` (> 300, ≤ 302). `tail -n 30 …/aset.err` → `INFO:     Started server process [76357]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)`. Traceback aset `217` = `<ta0>`; Traceback radar `1` = `<tr0>`; TaxonomyConfigError `0` = `<tc0>`.
- (c) [`Mon Oct 26 20:43:06 EDT 2026`] `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) [`Mon Oct 26 20:43:06 EDT 2026`] MARKERS after: `MIRROR_SOURCE_PREFIX = ` → `1`; `def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical` → `1`; `def warm_config` → `1`. GREEN.
- (s) [`Mon Oct 26 20:43:06 EDT 2026`] `ls /Users/cobalt/cobalt/src/cobalt/radar/notes.py` → listed; `ls /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` → listed; `ls /Users/cobalt/cobalt/tests/cobalt/test_radar_config_warmup.py` → listed (exit 0 each). GREEN. `<launchd set>` is empty, so there is no dry run.
- (f) [`Mon Oct 26 20:43:18 EDT 2026`] `COBALT_ENV=production uv run cobalt jobs restarts 88e2f5f9..05a21999` → exit 0, the same 13 rows as STEP-R, `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` = `<restart set>`, no `UNCLASSIFIED`. `COBALT_ENV=production uv run cobalt validate` → exit 0, as 4.5 (`13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`). GREEN.
- (g) no migration.
- (b, radar tails) [`Mon Oct 26 20:44:12 EDT 2026`, `<t up>` + 94 s] `tail -n 12 /Users/cobalt/cobalt/logs/radar.err`:
  - Startup vault/finviz lines from `20:42:30`.
  - `2026-10-26 20:42:30.669 | INFO     | cobalt.radar.runner:resident:645 - radar cycle: paused_market_reset scan_id=None`
  - `2026-10-26 20:44:10.693 | INFO     | cobalt.radar.runner:resident:645 - radar cycle: paused_market_reset scan_id=None`
  - The `20:44:10` cycle line is stamped after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback in the tail. This settles (b) GREEN on the first spaced tail.
- (e) The two reads are `HEARTBEAT RED — 2 job(s)  (2026-10-26 20:43:19 EDT)` [`date` `20:43:18`] and `HEARTBEAT RED — 2 job(s)  (2026-10-26 20:45:11 EDT)` [`date` before it `20:45:00`], 112 s apart. Both show:
  - The same two REDs as `<hb0>`: `RED  com.cobalt.agent             not loaded …` and `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: …`. There is no new RED.
  - `OK   com.cobalt.radar             running   running 3 min, heartbeat fresh`, `OK   com.cobalt.cos               running   running 3 min, heartbeat fresh`, `OK   com.cobalt.aset              running   loaded, pid 76357 [launchd probe]`.
  - (e) is GREEN. The clock was filled only with `date` + `heartbeat show` pairs, each showing the same lines.
- (h) REVERT-READBACK [`Mon Oct 26 20:45:38 EDT 2026`, `<t up>` + 180 s]: `radar panel FAILED` `31` = `<rp_up>` · `radar pool refresh FAILED` `60` = `<rpr_up>` · `radar S5 evaluate FAILED` `750` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>`; no count grew. `/radar` curl → `200`. No `census` reads on the card. GREEN.

THE CHAIN:
1. Every check was committed (P2: `94894ab18…`, clean, `held unfixed: 0`, `ready: YES`).
2. The tips were re-read (P3: `b0cca7d7`, `421af171`).
3. The tree merged clean (T: `<m1>` `247cfe42`).
4. RESTARTS was derived by the tool (R: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`).
5. The three suites were green on `<m1>`, under the equal-tree clause: offline 9144/0 · with-DB 5980/0 · live-note 148/0.
6. `<stack-final>` `05a21999` = `<m1>` + docs (D2.3).
7. The code landed (4.3: `Updating 88e2f5f93..05a219990`, `Fast-forward`).
8. The markers read `1`/`1`/`1` (d).
9. No migration (g).
10. The residents came up after the merge with new pids (a).
11. Radar is cycling (b, e).
12. The set's reads were listed (s).
13. No new failure (h).

The card surface is not readable here; the desk confirms it with him (L70). **smoke: GREEN**

PRE-STOP SELF-CHECK (K25):
1. Every smoke row's evidence is quoted above with its `date`.
2. The code tip `b0cca7d7` and head `421af171` were re-read at P3. `merge-base --is-ancestor b0cca7d7 05a21999` → exit 0 and `merge-base --is-ancestor 421af171 05a21999` → exit 0. `git -C /Users/cobalt/cobalt log --oneline -1` → `05a219990 Merge branch 'main' into deploy/radar-mirror-scope-port4`.
3. The REVERT-READBACK is shown in (h). Every count and sha above was re-read from this run's tool output.
4. No conflict marker exists: STEP-T and D2.1 ran clean (`Merge made by the 'ort' strategy.` each).

## CONTINUE
- next: STEP-D0 (gate green at Mon Oct 26 20:37:59 EDT 2026)
- D0 and D1 done; next: STEP-D2 (D2.0 report commit)
- OUTAGE STARTING Mon Oct 26 20:41:23 EDT 2026 — residents of com.cobalt.aset com.cobalt.cos com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 done at Mon Oct 26 20:42:38 EDT 2026: residents up. Smoke GREEN; STEP-7 closed. next: none (the stop line below)

## DECISIONS
- ASK DESK: `?? .claude/settings.json.bak` on `main` is outside D0's ACCEPTED list. It is not a staged line and not a dirty `src/`/`tests/`/`ops/`/`configs/` path, so it is outside the REFUSED list too. Safe default taken: not a stop; the untracked file is left untouched. [Mon Oct 26 20:38:51 EDT 2026]

## RECORDS
- Downtime: 58 s (under 300 s).
- REFUSED, not needed: none. Messages not followed: none.
- `cobalt_dev`: not touched by this run (equal-tree clause; the gate is the check's `cobalt_dev: 0013 — F2 = F0`).
- RETIRE OWED: none. BOOTSTRAP OWED from this set: none.
- Carried RED as read: no radar RED (`OK   radar                    paused (market_reset)` throughout). These standing REDs were named at D1 and are unchanged after the merge:
  - `RED  com.cobalt.agent             not loaded …`: the agent is recorded retired.
  - `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`
- P6/D1: the marker `def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical` read `No such file or directory` (exit 2) before the merge, because the set adds the file. After the merge it reads `1`.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-mirror-scope-port4` and branch `deploy/radar-mirror-scope-port4`, plus the set's branch `ops/radar-mirror-scope-port4` and its worktree. The gate worktree now holds a `.venv` created by `uv run`.
- Card `## RECORDS` (the desk's, copied):
  - radar-mirror-scope-port4: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port4-check-2026-10-26.md` last line: CHECK DONE · job: radar-mirror-scope-port4 · pass: 1 · tip: b0cca7d7 · house A: Grok FINDINGS: 0 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 9144/0 · with-DB 5980/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 190063
  - radar-mirror-scope-port4: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port4` → `421af171`; code tip `b0cca7d7`
  - written by deploy-card.sh at 2026-10-26 20:29 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one harness reminder asked that commits carry a `Claude-Session:` line. It was recorded under `## L74` and not acted on.
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 130ac2a2` → `context 208868 of 400000 — ok`.
- Push is his, through the desk (L55): `main` is ahead of `origin/main`.

DEPLOYED deploy-2026-10-26-radar-mirror-scope-port4 05a21999 | set: radar-mirror-scope-port4 | migrations: none | gate: offline 9144/0 · with-DB 5980/0 · live-note 148/0 | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 208868
