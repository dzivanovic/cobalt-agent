# deploy x15-hitl-probe-port · SET: x15-hitl-probe-port · MIGRATIONS: none

## §0 Headline
- DEPLOYED: x15-hitl-probe-port is on `main` at `b9906932` (was `3f617499`); tag `deploy-2026-10-21-x15-hitl-probe-port-attempt2`; rollback tag `pre-x15-hitl-probe-port`.
- Gate green on `d3651e95`: offline 9110/0 · with-DB 5946/0 · live-note 148/0; `cobalt_dev: 0013 — F2 = F0`.
- aset, cos and radar were restarted. Downtime was 21 s (03:19:26 → 03:19:47 ET). No migration.
- Smoke GREEN. `/hitl/x15-probe` returns `200` and all three markers read `1`.

## L74
- One block arrived as a system reminder (2026-10-22 02:25 ET), asking that commits end with a `Claude-Session:` line. It is data: not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md" · 0 · 43b2ead5761c3f669a4c719d41471d63d3463fb4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1006-deploy-x15-hitl-probe-port-card.md" · 0 · nothing
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
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy` | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Thu Oct 22 02:25:52 EDT 2026` (outside 21:30-22:30) |
| P2 check | `tail -n 3 "…/x15-hitl-probe-port-check-2026-10-21.md"` | 0 | `CHECK DONE · job: x15-hitl-probe-port · pass: 1 · tip: 304d5f3b · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9086/0 · with-DB 5932/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 157088` — carries `held unfixed: 0`, `ready: YES`, `tip: 304d5f3b` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/x15-hitl-probe-port-check-2026-10-21.md"` | 0 | `20f9db1dedf2232da182cd05e9181c6182edced9` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 304d5f3b` | 0 | `304d5f3b` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x15-hitl-probe-port` | 0 | `c062baf7` = row = `TIP` |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 304d5f3b c062baf7` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 304d5f3b c062baf7 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no worktree holds `.env` |
| P5 status | `git -C <GATE> status --short --branch` | 0 | `## deploy/x15-hitl-probe-port-attempt2` |
| P5 `<m0>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `43b2ead5` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 43b2ead5 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/x15-hitl-probe-port-attempt2` | 0 | empty |
| P6 marker 1 | `grep -c -F "def _hitl_key_script" /Users/cobalt/cobalt/src/cobalt/aset/web.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F '@app.get("/hitl/x15-probe"' /Users/cobalt/cobalt/src/cobalt/aset/web.py` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F 'add_parser("x15-send"' /Users/cobalt/cobalt/src/cobalt/hitl/cli.py` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main c062baf7 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 6720` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 26270` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is OFFLINE.` |
| P8 retired | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — `com.cobalt.agent recorded retired`; OFFLINE is expected |

## THE TREE
- `git -C <GATE> merge --no-edit c062baf7` → `Merge made by the 'ort' strategy.` (9 files, 564 insertions, 6 deletions)
- `<m1>` = `d3651e95`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 43b2ead5..deploy/x15-hitl-probe-port-attempt2` → `d3651e95 Merge commit 'c062baf7' into deploy/x15-hitl-probe-port-attempt2`
- `merge-base --is-ancestor 304d5f3b deploy/x15-hitl-probe-port-attempt2` → exit 0; `… c062baf7 …` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 43b2ead5 deploy/x15-hitl-probe-port-attempt2 -- src/cobalt/db_migrations` → nothing (no migration)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 43b2ead5 deploy/x15-hitl-probe-port-attempt2 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 43b2ead5 deploy/x15-hitl-probe-port-attempt2` → exit 0, `STEP-C: ADMITTED 0`. `<launchd set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-x15-hitl-probe-port-attempt2
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-x15-hitl-probe-port-attempt2
Installed 257 packages in 683ms
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/hitl/README.md	M	DOCS	-
docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/x15-hitl-probe-port-build-2026-10-21.result	A	DOCS	-
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/hitl/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_hitl_x15.py	A	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- NOT LOADED read: `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `pid = 40998` → stays in the set.
- `<restart set>`: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`
- `<deferred set>`: empty
- `com.cobalt.agent: recorded retired — not restarted`

## L68 GATE
- THE EQUAL-TREE CLAUSE does not hold: `git -C /Users/cobalt/cobalt diff --stat 304d5f3b d3651e95 -- . ":(exclude)docs"` → 11 files (`configs/cobalt/rules.yaml`, `ops/desk/retired-labels`, `src/cobalt/cos/run.py`, `src/cobalt/prefill/checkpoint_probe.py`, 7 test files; `main` moved since the check) → the gate runs whole.
- Deselects: none (build report `x15-hitl-probe-port-build-2026-10-21.md:135` "no `--deselect`: this build adds no with-DB test"). TICKERS: none. Migration: none.
- (a0) `uv run pytest -q -rs -p no:cacheprovider <17 files>` → `265 passed, 163 skipped in 19.54s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-x15-hitl-probe-port-attempt2 all --deploy --deploy-gate` launched in the background (`date` right after: `Thu Oct 22 02:28:27 EDT 2026`). Exit 0. Verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 9110/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5946/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-x15-hitl-probe-port-attempt2-all-20261022-022813.log
```
- (a) `offline 9110/0`; W line `tests/ops: run (deploy gate)`.
- (c) the nine SKIPPED lines are each inside the allowed set (`test_cards_picks.py:388`, `:401`, `test_checkpoints_live.py` live-vault, `test_playbook_live.py` live-vault, `test_radar_evaluate.py:695`, `test_replay_line.py` `COBALT_TEST_LIVE_DRC`, `test_s3_c4_experiments.py` x14 live template, `test_catalyst.py:365`, `test_predicate.py:262`).
- (c2) no migration on the card: no forward. `with-DB 5946/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` — log `:1049 F0: 664 35 272c95bbb12241e3611e4b36326ccf87`, `:2332 F2: 664 35 272c95bbb12241e3611e4b36326ccf87`.
- THE RELEASE: `.env: removed` (L76 lock released, log `:2388 lock released`); `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-x15-hitl-probe-port-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) `live-note 148/0`; no `COBALT_LIVE_VAULT_ROOT` skip there.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on d3651e95

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 20]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; one `?? .claude/settings.json.bak` (see DECISIONS); no staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 43b2ead5 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `tag scratch-allow-probe-x15-hitl-probe-port` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-x15-hitl-probe-port' (was 43b2ead5)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 86856ddf] …` · — · `43b2ead5 docs(desk): RECUT x15-hitl-probe-port attempt 2` |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-21-x15-hitl-probe-port-attempt2` | 1 | free |
| pre tag | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-x15-hitl-probe-port` | 1 | free |

### STEP-D1 (baseline, `date` `Thu Oct 22 03:17:08 EDT 2026`)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-22 03:17:09 EDT)`. Aset/sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`; `com.cobalt.aset running loaded, pid 6720`); radar `OK radar idle (overnight)`, `com.cobalt.radar running 272 min, heartbeat fresh`; `com.cobalt.cos running 399 min, heartbeat fresh`. The two REDs, named, not a stop (neither is the aset / sheet / radar probe):
  - `RED  com.cobalt.agent             not loaded NOT LOADED in launchd …` (agent recorded retired)
  - `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`
  - five `OWED (deferred bootstrap)` rows are OK (prefill-refresh, checkpoint-0715/0745/0815/0845, playbook).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.0 h old`
- aset `state = running`, `<aset pid>` 6720 · radar `state = running`, `<radar pid>` 26270 · cos `state = running`, `<cos pid>` 40998 · `cobalt.sh status` → `Cobalt is OFFLINE.` (agent recorded retired; no `ps -p`)
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-22 03:17:12.866`
- baselines: `<a0>` 293 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 80 · `<lc0>` 39
- `curl … /radar` → `200`. MARKERS → `0` · `0` · `0` (= before).
- THE LAUNCHD SET: empty. No migration: no `<RB>`, no D1-M.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 43b2ead5 "<card>"` → nothing. Report committed `3f617499` (`docs(report): deploy x15-hitl-probe-port — gate green on d3651e95`); `show --stat HEAD` → one file. `<pre-merge>` = `3f617499`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only)
- D2.2 `<stack-final>` = `b9906932`; `b9906932^2` → `3f617499` = `<pre-merge>`; `merge-base --is-ancestor d3651e95 b9906932` → exit 0
- D2.3 `git -C /Users/cobalt/cobalt diff --stat d3651e95 b9906932 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing
- D2.4 `backup status` → `newest snapshot: 1.0 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 10193.7 MB` · `ssd: snapshot 3f1f062c — 0 new / 1 changed, 12.1 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`
- D2.5 `date` `Thu Oct 22 03:19:11 EDT 2026` (122 s after D1's), `heartbeat show` → `HEARTBEAT RED — 2 job(s)`, the same two REDs (`com.cobalt.agent`, `com.cobalt.replay`); aset, sheet, radar, cos OK — no new RED
- D2.6 `date` `Thu Oct 22 03:19:16 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-x15-hitl-probe-port` at `3f617499`

### STEP-4 — THE OUTAGE
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `<t down>` `Thu Oct 22 03:19:26 EDT 2026` |
| 4.2 aset | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print …` | 0 · 113 | — · `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 cos | `launchctl bootout gui/501/com.cobalt.cos` · `launchctl print …` | 0 · 113 | — · `Could not find service "com.cobalt.cos" …` |
| 4.2 radar | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print …` | 0 · 113 | — · `Could not find service "com.cobalt.radar" …` |
| 4.2 orphan | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` | 0 | `orphan-clean: aset · none found` (no kill) |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `3f617499` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/x15-hitl-probe-port-attempt2` | 0 | `Updating 3f617499..b9906932` / `Fast-forward` (9 files, 564+, 6-) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 aset | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · print | 0 · 0 | `state = running`, pid 53218 (≠ 6720) |
| 4.6 cos | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` · print | 0 · 0 | `state = running`, pid 53231 (≠ 40998) |
| 4.6 radar | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · print | 0 · 0 | `state = running`, pid 53248 (≠ 26270) |
| 4.6 | `date` | 0 | `<t up>` `Thu Oct 22 03:19:47 EDT 2026` — downtime 21 s |
| 4.6L | — | — | `<launchd set>` empty: nothing |

### SUMMARY
- `<pre-merge>` `3f617499` → `<stack-final>` `b9906932`; tags `pre-x15-hitl-probe-port` (at `3f617499`), `deploy-2026-10-21-x15-hitl-probe-port-attempt2` (after green smoke; `main` = `b9906932`)
- `<t down>` 03:19:26 / `<t up>` 03:19:47 / 21 s
- uv sync line: none in production (STEP-R's `.venv` creation was in `<GATE>`)
- proof cost: n/a (no migration) · `migrations applied: none` · `<RB>`: none
- snapshot: `ssd: snapshot 3f1f062c`
- RESTARTS done: com.cobalt.aset com.cobalt.cos com.cobalt.radar
- LAUNCHD done: none · BOOTSTRAP OWED: none

### THE ROLLBACK STRING (the desk's)
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 b9906932` — residents `com.cobalt.aset com.cobalt.cos com.cobalt.radar` down first, up after; no `<launchd set>` label.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 80 · `<lc_up>` 39 (= D1 baselines)
- (a) `date` `Thu Oct 22 03:20:03 EDT 2026` · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 53218` (D1 6720) · `…/com.cobalt.radar` → `state = running`, `pid = 53248` (D1 26270) · `…/com.cobalt.cos` → `state = running`, `pid = 53231` (D1 40998) · `cobalt.sh status` → `Cobalt is OFFLINE.` (agent recorded retired: OFFLINE is green) — GREEN
- (b) `date` `Thu Oct 22 03:20:06 EDT 2026` · `grep -c "Started server process" …/aset.err` → `294` (`<a0>` 293 → +1) · `tail -n 30 …/aset.err` → `INFO:     Finished server process [6720]` … `INFO:     Started server process [53218]` … `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` · Traceback aset `217` = `<ta0>` · Traceback radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`
- (c) `date` `Thu Oct 22 03:20:12 EDT 2026` · `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200` — GREEN
- (d) MARKERS → `1` · `1` · `1` (= after) — GREEN
- (s) `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/hitl/x15-probe` → exit 0, `200` (card's green: `200`) · `curl … https://cobalt.taild24291.ts.net/` → exit 0, `200` — GREEN. No `<launchd set>` dry run.
- (e) read 1: `date` `Thu Oct 22 03:20:20 EDT 2026` · `heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-22 03:20:21 EDT)`, the same two REDs as `<hb0>` (`com.cobalt.agent` not loaded, `com.cobalt.replay` failed TraderSettingsError); `com.cobalt.aset running loaded, pid 53218`; `com.cobalt.radar running running 1 min, heartbeat fresh`; `com.cobalt.cos running running 1 min, heartbeat fresh`; `radar idle (overnight)`
- (e) read 2: `date` `Thu Oct 22 03:22:12 EDT 2026` · `heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-22 03:22:14 EDT)` (113 s after read 1), the same two REDs as `<hb0>` and nothing else red; `com.cobalt.radar running running 2 min, heartbeat fresh`; `com.cobalt.cos running running 3 min, heartbeat fresh`; `com.cobalt.aset running loaded, pid 53218` — GREEN
- (f) `validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 22 registered — 7 resident, 15 one-shot.` = `<jobs0>` · `COBALT_ENV=production uv run cobalt jobs restarts 3f617499..b9906932` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` = `<restart set>` (no deferred, agent not in it, nothing skipped), no `UNCLASSIFIED` — GREEN
- (g) no migration.
- (b) radar tail 1, `date` `Thu Oct 22 03:21:17 EDT 2026` (`<t up>` + 90 s): `tail -n 12 …/radar.err` → the new process's start lines (vault unlock, finviz token resolved, 03:19:44) and `2026-10-22 03:19:44.529 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — stamped 3 s before `<t up>` (the bootstrap ran before the `date`); no traceback, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`. Not yet settled.
- (b) radar tail 2, `date` `Thu Oct 22 03:22:47 EDT 2026` (`<t up>` + 180 s): `tail -n 12 …/radar.err` → last line `2026-10-22 03:21:24.553 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN (settled; the third tail is not needed).
- (h) REVERT-READBACK at `<t up>` + 180 s: `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 80 · `lifecycle card read failed` 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew); `curl … /radar` → `200`; no `census` reads on the card — GREEN

THE CHAIN: every check committed (P2 `20f9db1d…`) · tips re-read (P3 `304d5f3b`, `c062baf7`) · merged tree (T, `<m1>` `d3651e95`) · RESTARTS derived (R: aset cos radar) · three suites green on `<m1>` (G: offline 9110/0, with-DB 5946/0, live-note 148/0) · `<stack-final>` `b9906932` = `<m1>` + docs (D2.3) · landed code (4.3 `Updating 3f617499..b9906932`) · markers `1`/`1`/`1` (d) · no migration (g) · residents up with new pids after the merge (a) · radar cycling (b 03:21:24, e) · the set's reads `200`/`200` (s) · no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

**smoke: GREEN**

## CONTINUE
- STEP-D0 (gate green at Thu Oct 22 03:16:34 EDT 2026) done; STEP-D1 done.
- STEP-D2 done.
- OUTAGE STARTING Thu Oct 22 03:19:16 EDT 2026 — residents of com.cobalt.aset com.cobalt.cos com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- OUTAGE ENDED Thu Oct 22 03:19:47 EDT 2026 — residents up on b9906932 (merged).
- STEP-4.7 smoke GREEN; STEP-7 closed. Nothing next for this session.

## DECISIONS
- D0 porcelain shows `?? .claude/settings.json.bak` — not among the ACCEPTED lines, and not in the REFUSED classes (staged, or `src/` / `tests/` / `ops/` / `configs/`). Safe default taken: not a stop (untracked, outside every path this set ships); the desk may remove or track it.

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it` (read the release from `lock released` instead).
- Downtime: 21 s (not over 300 s).
- `cobalt_dev: 0013 (F2 = F0)`.
- RETIRE OWED: none. BOOTSTRAP OWED: none.
- Carried RED as read (not new, not of this set): `RED  com.cobalt.replay  failed  StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …` and `RED  com.cobalt.agent  not loaded` (agent recorded retired). Both in `<hb0>` and unchanged through smoke.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-x15-hitl-probe-port-attempt2` and branch `deploy/x15-hitl-probe-port-attempt2`; the set's branch `ops/x15-hitl-probe-port` and its worktree.
- Messages not followed: none. L74: one line (see `## L74`).
- Card `## RECORDS`, copied:
  - x15-hitl-probe-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x15-hitl-probe-port-check-2026-10-21.md` last line: CHECK DONE · job: x15-hitl-probe-port · pass: 1 · tip: 304d5f3b · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9086/0 · with-DB 5932/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 157088
  - x15-hitl-probe-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x15-hitl-probe-port` → `c062baf7`; code tip `304d5f3b`
  - written by deploy-card.sh at 2026-10-21 20:42 ET (`date`); trial merge of the heads onto main in order: clean

### PRE-STOP SELF-CHECK (K25)
1. Every smoke row is quoted with its `date`: (a) 03:20:03, (b) 03:20:06, (c)/(d)/(s) 03:20:12, (e) 03:20:20 and 03:22:12, radar tails 03:21:17 and 03:22:47, (h) after 03:22:47.
2. Tips re-read at P3; `merge-base --is-ancestor 304d5f3b b9906932` → exit 0; `merge-base --is-ancestor c062baf7 b9906932` → exit 0.
3. REVERT-READBACK shown at (h): 18/60/80/39. Every count and sha in this report was read from tool output this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same, 4.3 fast-forward.
- THE RELEASE: the gate released the lock at its end (`.env: removed`, `lock released`); no lock is held.

DEPLOYED deploy-2026-10-21-x15-hitl-probe-port-attempt2 b9906932 | set: x15-hitl-probe-port | migrations: none | gate: offline 9110/0 · with-DB 5946/0 · live-note 148/0 | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 242986
