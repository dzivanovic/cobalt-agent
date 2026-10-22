# deploy cos-env-load · set: cos-env-load · migrations: none

## §0 Headline
- Deployed `cos-env-load` (code tip `5b813fa4`, head `773fe012`): `main` `0c1632ed` → `ea7f7727`, tag `deploy-2026-10-21-cos-env-load`. No migration.
- Gate green on the equal tree (`756d389e`): offline 9076/0 · with-DB 5922/0 · live-note 148/0.
- Radar was down for 13 s and came back on a new pid. aset was untouched. cos is not loaded and stays OWED, so the new env load runs when cos is bootstrapped.
- Smoke GREEN. 1 decision (ASK DESK on the third marker's missing file), 0 for Dejan.

## L74
- A system notice in this session asked for a `Claude-Session:` line on commits. DATA (L74): not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1002-deploy-cos-env-load-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1002-deploy-cos-env-load-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1002-deploy-cos-env-load-card.md" · 0 · fda035809094575b02bb0b432d7729bdf76c8974
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1002-deploy-cos-env-load-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| first launch | `ls -la ".../reports/deploy-cos-env-load.md"` | 1 | `No such file or directory` |
| P1 | `date` | 0 | `Wed Oct 21 20:07:14 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../cos-env-load-check-2026-10-21.md"` | 0 | `CHECK DONE · job: cos-env-load · pass: 1 · tip: 5b813fa4 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9076/0 · with-DB 5922/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 189692` — carries `held unfixed: 0`, `ready: YES`, `tip: 5b813fa4` = row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/cos-env-load-check-2026-10-21.md"` | 0 | `bd0629a61497b7250ea4e9ab5bd700278d4a5b0f` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/cos-env-load-check-2026-10-21.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 5b813fa4` | 0 | `5b813fa4` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-env-load` | 0 | `773fe012` = row and `TIP` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5b813fa4 773fe012` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 5b813fa4 773fe012 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-cos-env-load status --short --branch` | 0 | `## deploy/cos-env-load` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-cos-env-load rev-parse --short=8 HEAD` | 0 | `fda03580` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor fda03580 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-env-load` | 0 | empty |
| P6 | `grep -c -F "ENV_FILE = Path(__file__)" /Users/cobalt/cobalt/src/cobalt/cos/run.py` | 1 | `0` = before |
| P6 | `grep -c -F "load_dotenv(ENV_FILE)" /Users/cobalt/cobalt/src/cobalt/cos/run.py` | 1 | `0` = before |
| P6 | `grep -c -F "def test_e1_a_launchd_start_reads_the_repo_env_file" /Users/cobalt/cobalt/tests/cobalt/test_cos_env_load.py` | 2 | `grep: /Users/cobalt/cobalt/tests/cobalt/test_cos_env_load.py: No such file or directory` — the file is not on production: production does not carry the marker (see `## DECISIONS` 1) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 773fe012 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 6720` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 6354` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-cos-env-load merge --no-edit 773fe012` → `Merge made by the 'ort' strategy.` (5 files: `docs/40 - DevDocs/cobalt/cos/README.md`, two build reports, `src/cobalt/cos/run.py` +10, `tests/cobalt/test_cos_env_load.py` +177).
- `git -C /Users/cobalt/cobalt-wt/deploy-cos-env-load rev-parse --short=8 HEAD` → `756d389e` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent fda03580..deploy/cos-env-load` → `756d389e Merge commit '773fe012' into deploy/cos-env-load` (one line, one head).
- `merge-base --is-ancestor 5b813fa4 deploy/cos-env-load` → exit 0 · `merge-base --is-ancestor 773fe012 deploy/cos-env-load` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat fda03580 deploy/cos-env-load -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat fda03580 deploy/cos-env-load -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" fda03580 deploy/cos-env-load` → exit 0, output whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty · `<deferred set>`: empty.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-cos-env-load` · `ls -la .../.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, table whole (after uv venv creation lines: `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-cos-env-load`, `Installed 257 packages in 970ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-env-load-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-env-load-build-2026-10-21.result	A	DOCS	-
src/cobalt/cos/run.py	M	static import reach	com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_cos_env_load.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.cos com.cobalt.radar
```
- No `UNCLASSIFIED` row.
- NOT LOADED: `launchctl print gui/501/com.cobalt.cos` → exit 113, `Could not find service "com.cobalt.cos" in domain for user gui: 501`.
- com.cobalt.cos: not loaded — skipped
- com.cobalt.agent: recorded retired — not restarted
- `<deferred set>`: none
- **`<restart set>`: com.cobalt.radar** · `<launchd set>`: none

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 5b813fa4 756d389e -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5922/0` (> 0). The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-env-load-check-2026-10-21.md` `:156-176` (its W call `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-env-load all --deploy --deploy-gate` on HEAD `773fe012`, exit 0):
```
tests/ops: run (deploy gate)
offline 9076/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5922/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-env-load-all-20261021-191428.log
```
- (c) judgment kept: all nine SKIPPED lines are inside the allowed set (cards_picks `:388`, `:401`; radar_evaluate `:695`; catalyst `:365`; predicate `:262`; `test_playbook_live.py` and `test_checkpoints_live.py` naming `COBALT_LIVE_VAULT_ROOT not set`; `test_replay_line.py` naming `COBALT_TEST_LIVE_DRC`; `test_s3_c4_experiments.py`). None outside → (a)–(f) skipped.
- `cobalt_dev: 0013 — F2 = F0` (the check's run); this run took no lock.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 756d389e — offline 9076/0 · with-DB 5922/0 · live-note 148/0 (20:08 ET)

## Deploy table
### STEP-D0 (20:08 ET)
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 157]`; `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (untracked, outside `src/ tests/ ops/ configs/`); no staged line.
- `git -C /Users/cobalt/cobalt diff --stat fda03580 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- Allowlist probe: `tag scratch-allow-probe-cos-env-load` → ok · `tag -d` → `Deleted tag 'scratch-allow-probe-cos-env-load' (was fda03580)` · `commit --allow-empty` → `[main 22de6e0a] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `fda03580 docs(desk): deploy card 1002 cos-env-load, TIP 773fe012`.
- `rev-parse --verify --quiet refs/tags/deploy-2026-10-21-cos-env-load` → exit 1 · `refs/tags/pre-cos-env-load` → exit 1.

### STEP-D1 baseline (20:09:05 EDT)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 20:09:06 EDT)`. aset/sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`); `OK radar paused (market_reset)`; `OK com.cobalt.radar running running 336 min, heartbeat fresh`. REDs named, not a stop (none is aset/sheet/radar): `RED archiver last run FAILED — last run 2026-10-21 00:54 UTC (23.2 h ago), rows written 3373447, exit 1`; `RED com.cobalt.agent not loaded NOT LOADED in launchd …` (recorded retired); `RED com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed for WBD/i1: Finviz HTTP failed: Client error '400 Bad Request' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. `OK com.cobalt.cos OWED (deferred bootstrap) NOT LOADED … listed in data/deploy/bootstrap-owed.json`.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 2.8 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` `6720` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` `6354` · `launchctl print gui/501/com.cobalt.cos` → exit 113 `Could not find service "com.cobalt.cos" in domain for user gui: 501` (still not loaded) · `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (recorded retired; no `ps -p`).
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-21 20:08:20.467 | INFO | cobalt.radar.runner:resident:638 - radar cycle: paused_market_reset scan_id=None` (also `20:00:00.363 ERROR … radar cycle dropped at bars: dropped at bars:BE`); no traceback.
- Log baselines: `<a0>` 293 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 80 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS → `0`, `0`, and `No such file or directory` (before, as P6).
- THE LAUNCHD SET: empty. MIGRATIONS: none (no `<RB>`, no D1-M); no `census` smoke read.

### STEP-D2
- D2.0 `deploy-shipped.sh --moved fda03580 "<card>"` → nothing · commit `0c1632ed docs(report): deploy cos-env-load — gate green on 756d389e` (`show --stat HEAD`: the one report file, 138 insertions) · `<pre-merge>` = `0c1632ed`.
- D2.1 `git -C /Users/cobalt/cobalt-wt/deploy-cos-env-load merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `ea7f7727`; `rev-parse --short=8 ea7f7727^2` → `0c1632ed` = `<pre-merge>`; `merge-base --is-ancestor 756d389e ea7f7727` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 756d389e ea7f7727 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 2.8 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 10178.9 MB` · `ssd: snapshot 6c5dbea4 — 0 new / 4 changed, 56.5 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Wed Oct 21 20:11:05 EDT 2026` · `heartbeat show` → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 20:11:06 EDT)` (120 s after D1's 20:09:06): the same four REDs as `<hb0>` (archiver probe, agent, archiver job, replay job); aset/sheet OK; `OK com.cobalt.radar running running 338 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Wed Oct 21 20:11:10 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-cos-env-load` at `0c1632ed`.

### STEP-4 (the outage, `<restart set>` = com.cobalt.radar)
- 4.1 `date` → `Wed Oct 21 20:11:22 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.radar` → ok · `launchctl print gui/501/com.cobalt.radar` → exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501`. aset not in the set: no orphan-clean. agent not in the set.
- 4.3 `rev-parse --short=8 HEAD` → `0c1632ed` = `<pre-merge>` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/cos-env-load` → `Updating 0c1632ed..ea7f7727` / `Fast-forward` (5 files, 422 insertions).
- 4.4 migrations applied: none.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → ok · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 31938` (≠ D1's 6354), `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`.
- `date` → `Wed Oct 21 20:11:35 EDT 2026` = `<t up>`. Downtime 13 s.
- 4.6L: `<launchd set>` empty — nothing.

### STEP-7 close
| item | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `0c1632ed` → `ea7f7727` |
| tags | `pre-cos-env-load` (at `0c1632ed`) · `deploy-2026-10-21-cos-env-load` (at `ea7f7727`, after the green smoke) |
| `<t down>` / `<t up>` / seconds | 20:11:22 / 20:11:35 / 13 s |
| uv sync line | none on production (the gate worktree's first `uv run` created its `.venv`: `Installed 257 packages in 970ms`) |
| proof cost | n/a (no migration) |
| migrations applied | none |
| `<RB>` before / after | n/a |
| snapshot | `6c5dbea4` (ssd) |
| RESTARTS done | com.cobalt.radar |
| LAUNCHD done | none |
| BOOTSTRAP OWED | none from this run (com.cobalt.cos stays owed from an earlier deploy) |

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 ea7f7727`, with com.cobalt.radar booted out first and bootstrapped after.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

PRE-STOP SELF-CHECK:
1. Every smoke row is quoted with its `date` (`## Smoke`: 20:11:47 to 20:14:41).
2. Code tip `5b813fa4` and head `773fe012` re-read at P3; `merge-base --is-ancestor 5b813fa4 ea7f7727` → exit 0; `merge-base --is-ancestor 773fe012 ea7f7727` → exit 0.
3. REVERT-READBACK (h) shown: 18/60/80/39, unchanged from `<t up>`. Every count and sha in this report comes from this run's tool output.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same, 4.3 a fast-forward.

## Smoke
- FIRST CALLS after `<t up>` 20:11:35: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 80 · `<lc_up>` 39 (= D1's).
- (a) `date` 20:11:47 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 6720` (outside the set: SAME pid ✓) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 31938` (in the set: NEW pid ✓) · `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (recorded retired: OFFLINE expected ✓). GREEN.
- (b) `date` 20:11:51 · `grep -c "Started server process" .../aset.err` → `293` = `<a0>` (aset outside the set ✓) · `tail -n 30 .../aset.err` → last entry `2026-10-21 11:14:49.012 | INFO | cobalt.aset.daily_note:_write_unit:189 - [WRITE] updated: …` (aset not restarted; no new start, no traceback in the tail) · Traceback aset `217` = `<ta0>` · Traceback radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`.
- (c) `date` 20:11:57 · `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) `date` 20:11:57 · MARKERS → `1`, `1`, `1` = after. GREEN.
- (e) first: `date` 20:12:04 · `heartbeat show` → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 20:12:05 EDT)`; the same four REDs as `<hb0>`, nothing new; `OK com.cobalt.radar running running 1 min, heartbeat fresh`.
- (f) `date` 20:12:09 · `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` (= 4.5) · `COBALT_ENV=production uv run cobalt jobs restarts 0c1632ed..ea7f7727` → exit 0, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.cos com.cobalt.radar`; minus `com.cobalt.cos` (`not loaded — skipped`) = `com.cobalt.radar` = STEP-R's `<restart set>` ✓.
- (g) no migration.
- (s) `date` 20:11:57 · `ls /Users/cobalt/cobalt/src/cobalt/cos/run.py` → exit 0, listed ✓ · `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` → exit 0, `1` ✓ (cos stays owed). No `<launchd set>` dry run.
- (b) radar tails: `date` 20:13:08 (+93 s) · `tail -n 12 .../radar.err` → last line `2026-10-21 20:11:34.353 | INFO | cobalt.radar.runner:resident:638 - radar cycle: paused_market_reset scan_id=None` — the new process's first cycle, stamped 0.6 s before `<t up>`, so it does not settle. `date` 20:14:37 (+182 s) · `tail -n 12 .../radar.err` → last line `2026-10-21 20:13:14.385 | INFO | cobalt.radar.runner:resident:638 - radar cycle: paused_market_reset scan_id=None` — a cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN (third tail not needed).
- (e) second: `date` 20:13:54 · `heartbeat show` → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-21 20:13:56 EDT)` (111 s after the first); the same four REDs as `<hb0>`; `OK com.cobalt.radar running running 2 min, heartbeat fresh`. GREEN. (Clock-fill heartbeat pairs between 20:12:16 and 20:14:34 all read the same.)
- (h) `date` 20:14:41 (`<t up>` + 186 s) · `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 80 · `lifecycle card read failed` 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) · `/radar` → `200`. No census read. GREEN.

THE CHAIN: every check committed (P2: `bd0629a6`, clean) → the tips re-read (P3: `5b813fa4`, `773fe012`) → the merged tree (T: `756d389e`, one merge, no migration) → RESTARTS derived by the tool (R: `com.cobalt.radar`; cos not loaded, agent retired) → three suites green on the equal tree (G: offline 9076/0 · with-DB 5922/0 · live-note 148/0) → `<stack-final>` `ea7f7727` = `<m1>` + docs (D2.3) → the landed code (4.3 fast-forward `0c1632ed..ea7f7727`) → markers 1/1/1 (d) → no migration (g) → radar up on a new pid after the merge (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).
**smoke: GREEN**

## CONTINUE
D0 and D1 done. D2.0: `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved fda03580 "<card>"` → nothing printed.
D2 done: `<pre-merge>` 0c1632ed, `<stack-final>` ea7f7727, snapshot 6c5dbea4, tag pre-cos-env-load.
OUTAGE STARTING 20:11:10 EDT — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
Outage ended 20:11:35 (radar up, pid 31938). Smoke GREEN 20:14:41. Tagged. next: none — the run is done.

## DECISIONS
1. ASK DESK: P6's third marker reads a file absent on production (`grep` exit 2, `No such file`), not the literal `0`. The hub's only failing case is "production already carries <marker>", which an absent file is not. Safe default taken: the file's absence counts as the before value `0`, and the run continues. [20:07 ET]

## RECORDS
- Downtime: radar 13 s (20:11:22 → 20:11:35); under 300 s. aset not restarted (same pid 6720).
- `REFUSED, not needed`: none. Messages not followed: none.
- `cobalt_dev: 0013 (F2 = F0)` — from the check's gate run (equal-tree clause); this run took no `cobalt_dev` lock and ran no dev migrate.
- RETIRE OWED: none.
- The carried RED as read (all present before this deploy, none aset/sheet/radar): `RED archiver last run FAILED — last run 2026-10-21 00:54 UTC …, exit 1`; `RED com.cobalt.agent not loaded` (recorded retired); `RED com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: … Finviz HTTP failed: Client error '400 Bad Request' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`.
- com.cobalt.cos: not loaded — skipped; it stays OWED in `data/deploy/bootstrap-owed.json` (smoke (s): `1`). The code this deploy landed (`load_dotenv(ENV_FILE)` in `src/cobalt/cos/run.py`) takes effect when cos is bootstrapped by a later bootstrap-only deploy.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-cos-env-load` and branch `deploy/cos-env-load`; the set's branch `ops/cos-env-load` and its worktree `/Users/cobalt/cobalt-wt/cos-env-load` (named in the check report).
- The gate worktree now holds a `.venv` (created by `uv run` at STEP-R).
- Card `## RECORDS`, copied:
  - cos-env-load: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-env-load-check-2026-10-21.md` last line: CHECK DONE · job: cos-env-load · pass: 1 · tip: 5b813fa4 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9076/0 · with-DB 5922/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 189692
  - cos-env-load: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-env-load` → `773fe012`; code tip `5b813fa4`
  - written by deploy-card.sh at 2026-10-21 20:06 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one notice in this session asked for a `Claude-Session:` line on commits. It was recorded and not acted on.

DEPLOYED deploy-2026-10-21-cos-env-load ea7f7727 | set: cos-env-load | migrations: none | gate: offline 9076/0 · with-DB 5922/0 · live-note 148/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 248935
