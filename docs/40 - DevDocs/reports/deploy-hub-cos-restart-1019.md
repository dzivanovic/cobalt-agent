# deploy hub-cos-restart-1019 · set: hub-cos · migrations: none

## §0 Headline
- Deploy of `ops/hub-cos-restart-1019` (code tip `d59fac71`, head `d0d458c9`) through `DEPLOY-HUB.md` on card 879. In progress.

## L74
- The session's attribution reminder asked for a `Claude-Session:` line in commits. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md" · 0 · 3862ef0344f2a424a8b2075834c8e23821d6a7e2
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md" · 0 · nothing
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
| first launch | `ls -la "…/reports/deploy-hub-cos-restart-1019.md"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 19 17:16:49 EDT 2026` (outside 21:30–22:30 ET) |
| P2 | `tail -n 3 "…/reports/hub-cos-restart-1019-check-2026-10-19.md"` | 0 | `CHECK DONE · job: hub-cos-restart-1019 · pass: 1 · tip: d59fac71 · house A: Grok FINDINGS: 0 · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none (not needed) · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 190519` — carries `held unfixed: 0`, `ready: YES`, `tip: d59fac71` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/hub-cos-restart-1019-check-2026-10-19.md"` | 0 | `afafeb2e1ef682f61d3c2148702ca5145ef847a3` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/hub-cos-restart-1019-check-2026-10-19.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 d59fac71` | 0 | `d59fac71` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-1019` | 0 | `d0d458c9` (= row, = TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d59fac71 d0d458c9` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat d59fac71 d0d458c9 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no holder) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/hub-cos-restart-1019` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `3862ef03` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3862ef03 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/hub-cos-restart-1019` | 0 | empty |
| P6 | marker 1 `grep -c -F "com.cobalt.cos: not loaded — skipped" "…/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P6 | marker 2 `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)" "…/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P6 | marker 3 `grep -c -F "launchctl kickstart -k gui/501/com.cobalt.cos" "…/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main d0d458c9 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 35793` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 57565` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit d0d458c9` → `Merge made by the 'ort' strategy.` (5 files: `DEPLOY-HUB.md` 7 +-, build report + `.result`, `tests/ops/test_hub_cos_restart_1019.py` +93, `tests/ops/test_hub_deferred_1018.py` 4 +-).
- `git -C <GATE> rev-parse --short=8 HEAD` → `7988e364` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 3862ef03..deploy/hub-cos-restart-1019` → `7988e364 Merge commit 'd0d458c9' into deploy/hub-cos-restart-1019` (one line, one head).
- `merge-base --is-ancestor d59fac71 deploy/hub-cos-restart-1019` → exit 0; `merge-base --is-ancestor d0d458c9 deploy/hub-cos-restart-1019` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 3862ef03 deploy/hub-cos-restart-1019 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 3862ef03 deploy/hub-cos-restart-1019 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 3862ef03 deploy/hub-cos-restart-1019` → exit 0, whole output: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-hub-cos-restart-1019
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-hub-cos-restart-1019
Installed 257 packages in 905ms
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.result	A	DOCS	-
tests/ops/test_hub_cos_restart_1019.py	A	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>`: EMPTY (no resident goes down; the merge lands with residents up). `<deferred set>`: empty. `<launchd set>`: empty. `MIGRATIONS: none`, so an empty set is consistent.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (DB: none), so the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 19.00s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- No `--deselect` (the build report names none), no `--tickers` (`TICKERS: none`), no `--migration` (`MIGRATIONS: none`). `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-hub-cos-restart-1019 all --deploy --deploy-gate` launched in the background.
- Verdict lines WHOLE (exit 0):
```
tests/ops: run (deploy gate)
offline 8822/0
lock: waited 4 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5715/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-hub-cos-restart-1019-all-20261019-171901.log
```
- (a) offline `8822/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock taken (waited 4 min); proof-only at `0013`, nothing CHANGED.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`; `test_playbook_live.py:31` = `test_live_vault_renders_six_decks` (def at :32), reason `COBALT_LIVE_VAULT_ROOT not set`; `test_radar_evaluate.py:695`; `test_replay_line.py:266` reason `COBALT_TEST_LIVE_DRC`; `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (def at :96); `test_catalyst.py:365`; `test_predicate.py:262`.
- (c2) `grep -n -F "dev forward" <log>` → `1262:dev forward: APPLIED 18:05:25`. `grep -n -F "CHANGED" <log>` → 3 lines: `1091:proof-only: on cobalt_dev, nothing CHANGED …` and two proof tables (`1333`, `2270`) each `content UNCHANGED on every table.` — no `CHANGED` object.
- (c3)/(c) with-DB `5715/0`.
- (f) `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed`; `grep -n -F "released" <log>` → `2335:lock released` (the log stamps no time on it; gate ended before 18:10:57). `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-hub-cos-restart-1019" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `0` (the lock dir is another session's, not this worktree's).
- (e) live-note `147/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 7988e364

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 220]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` lines are `.claude/settings.json`, `configs/cobalt/rules.yaml` and `docs/40 - DevDocs/…` only; `??` lines are under `docs/40 - DevDocs/` plus `.claude/settings.json.bak` (not `src/`, `tests/`, `ops/`, `configs/`) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 3862ef03 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-hub-cos-restart-1019` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-hub-cos-restart-1019' (was 7bb031e4)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main fc8c5b39] …` · — · `7bb031e4 docs(desk): REFRESH 6cf2ce55 to f3a3ff5e, section 5 rewritten R2090` (HEAD back) |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-hub-cos-restart-1019` | 1 | — |
| TAG | `rev-parse --verify --quiet refs/tags/pre-hub-cos-restart-1019` | 1 | — |

### STEP-D1 baseline
- `date` → `Mon Oct 19 18:11:39 EDT 2026`. `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 18:11:41 EDT)`; aset pid 35793 running, radar `running 419 min, heartbeat fresh`, agent pid 35845 alive; `AMB com.cobalt.herdr unmanaged` (declared interim); `com.cobalt.cos disabled — NOT LOADED BY DESIGN`; `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)`. No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`: 13 trade_defs OK, `Placement (docs/PLACEMENT.md): tree clean.`); `<jobs0>` = `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` with `NOT LOADED BY DESIGN (1): com.cobalt.cos`.
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 6.0 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 35793` (`<aset pid>`). `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 57565` (`<radar pid>`). `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → seven `cards.expire: falling back to the session close (16:00:00)` INFO lines, last `2026-10-19 18:11:34.966 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792447804056`.
- LOG BASELINES: `<a0>` = 284 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS → `0`, `0`, `0` (each = before).
- THE LAUNCHD SET: empty — nothing. MIGRATIONS: none — no `<RB>`, no D1-M.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 3862ef03 "<card>"` → prints nothing.

## Smoke

## CONTINUE
- STEP-D0 done; STEP-D1 baseline done.
- next: STEP-D2.1 (`main` into the gate)

## DECISIONS

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it` (the gate's own verdict line already carries `.env: removed`).

(run in progress — next step under ## CONTINUE)
