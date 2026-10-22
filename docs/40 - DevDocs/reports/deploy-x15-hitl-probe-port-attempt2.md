# deploy x15-hitl-probe-port · SET: x15-hitl-probe-port · MIGRATIONS: none

## §0 Headline
- Run in progress.

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

## Smoke

## CONTINUE
- STEP-D0 (gate green at Thu Oct 22 03:16:34 EDT 2026) done; STEP-D1 done.
- next: STEP-D2

## DECISIONS
- D0 porcelain shows `?? .claude/settings.json.bak` — not among the ACCEPTED lines, and not in the REFUSED classes (staged, or `src/` / `tests/` / `ops/` / `configs/`). Safe default taken: not a stop (untracked, outside every path this set ships); the desk may remove or track it.

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it` (read the release from `lock released` instead).

(run in progress — next step under ## CONTINUE)
