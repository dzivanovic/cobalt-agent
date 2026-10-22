# deploy-deploy-cos-restart · SET: deploy-cos-restart · MIGRATIONS: none

## §0 Headline
- Deploy hub run of card `prompts/2026-10-21/1013-deploy-deploy-cos-restart-card.md`, first launch, started Thu Oct 22 01:26:35 EDT 2026.

## L74
- A system reminder in this session asked that commits also carry a `Claude-Session:` line. Recorded once here as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1013-deploy-deploy-cos-restart-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1013-deploy-deploy-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1013-deploy-deploy-cos-restart-card.md" · 0 · b4f4e639f0ad44220e4507c85ffb8dbd9d2ae27a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1013-deploy-deploy-cos-restart-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-20 R2240 row · grep -n "^| R2240 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · 43:| R2240 | 20:57 ET | HIS RULING · APPROVED (via brain): the three R60 launchctl restart strings for a loaded com.cobalt.cos ("Okay with R60 restart commands"); words: cto-2026-10-20-words.md R2240. 929 has no R60 FILL row; :38 stays. | APPLIED: areas/cobalt.md NOW at 20:57 ET |
RULING 2026-10-20 R2240 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2240 |" -- "docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · f70be7320ae0b8be99317efecf7122b508c95f72
RULING 2026-10-20 R2240 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-20.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-cos-restart.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Thu Oct 22 01:26:35 EDT 2026` — outside 21:30-22:30 ET |
| P2 | `tail -n 3 "<check report>"` | 0 | `CHECK DONE · job: deploy-cos-restart · pass: 1 · tip: 3770387d · house A: Grok FINDINGS: 5 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9094/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 216150` — carries `held unfixed: 0`, `ready: YES`, tip = code tip `3770387d` |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/deploy-cos-restart-check-2026-10-21.md"` | 0 | `8dea75528386a82202ccc0793deb78f4ed230293` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 3770387d` | 0 | `3770387d` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-cos-restart` | 0 | `3770387d` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3770387d ops/deploy-cos-restart` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 3770387d ops/deploy-cos-restart -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-cos-restart` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `b4f4e639` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b4f4e639 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-cos-restart` | 0 | empty |
| P6 | marker 1 `Bash(launchctl bootout gui/501/com.cobalt.cos)` in DEPLOY-HUB.md | 1 | `0` (before `0`) |
| P6 | marker 2 `Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist)` in DEPLOY-HUB.md | 1 | `0` (before `0`) |
| P6 | marker 3 `Bash(launchctl kickstart -k gui/501/com.cobalt.cos)` in DEPLOY-HUB.md | 1 | `0` (before `0`) |
| P6 | marker 4 `com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)` in DEPLOY-HUB.md | 0 | `1` (before `1`) |
| P6 | marker 5 `Bash(launchctl kickstart -k gui/501/com.cobalt.cos)` in STANDING-LIST.md | 1 | `0` (before `0`) |
| P6 | marker 6 `(a cos outside it is not read)` in DEPLOY-HUB.md | 1 | `0` (before `0`) |
| P6 | marker 7 `— cos: <UP\|DOWN>` in DEPLOY-HUB.md | 1 | `0` (before `0`) |
| P6 | marker 8 `cos: DOWN` in DEPLOY-HUB.md | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main ops/deploy-cos-restart -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 6720` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 26270` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — com.cobalt.agent recorded retired |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is OFFLINE.` (retired: expected) |

## THE TREE
- `git -C <GATE> merge --no-edit 3770387d` → `Merge made by the 'ort' strategy.` (9 files changed, 402 insertions(+), 37 deletions(-): DEPLOY-HUB.md, STANDING-LIST.md, the build report and result, tests/ops ×5)
- `git -C <GATE> rev-parse --short=8 HEAD` → `ea50454f` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent b4f4e639..deploy/deploy-cos-restart` → `ea50454f Merge commit '3770387d' into deploy/deploy-cos-restart`
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3770387d deploy/deploy-cos-restart` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat b4f4e639 deploy/deploy-cos-restart -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat b4f4e639 deploy/deploy-cos-restart -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" b4f4e639 deploy/deploy-cos-restart` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, whole (after uv venv creation lines: `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Built cobalt-agent …`, `Installed 257 packages in 808ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.result	A	DOCS	-
tests/ops/test_deploy_cos_restart_1021.py	A	test/documentation; no resident	-
tests/ops/test_deploy_smoke_string_1014.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_launchd.py	M	test/documentation; no resident	-
tests/ops/test_hub_cos_restart_1019.py	M	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>`: EMPTY (no UNCLASSIFIED row). No resident goes down; the merge lands with residents up.
- `<deferred set>`: empty. `<launchd set>`: empty.
- com.cobalt.agent: recorded retired — not restarted (not derived here in any case).

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0` (count not above 0); the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `265 passed, 163 skipped in 19.62s` — 0 failed (every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: the build report `deploy-cos-restart-build-2026-10-21.md` names none (`grep deselect` → no match). TICKERS none, MIGRATIONS none → no `--tickers`, no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-deploy-cos-restart all --deploy --deploy-gate` (background) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9094/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5930/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-deploy-cos-restart-all-20261022-012844.log
```
- (a) offline 9094/0; W line `tests/ops: run (deploy gate)`.
- (c) pass 1 at 0013: every SKIPPED line inside the allowed set, by test and reason: `test_cards_picks.py:388`, `:401`; `test_radar_evaluate.py:695`; `test_catalyst.py:365`; `test_predicate.py:262`; `test_playbook_live.py:31` = the skip of `test_live_vault_renders_six_decks` (def at `:32`), reason `COBALT_LIVE_VAULT_ROOT not set`; `test_checkpoints_live.py:36` = `test_dry_run_finds_the_heading_in_real_notes` (def at `:37`), same reason; `test_replay_line.py:266` reason names `COBALT_TEST_LIVE_DRC`; `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (def at `:96`).
- (c2) FORWARD: none (MIGRATIONS: none; no migration above 0013 in the merged tree). with-DB 5930/0.
- (f) `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-deploy-cos-restart" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (exit 2); log line `2388:lock released` (L76 lock released by 02:17 ET; the log line carries no time).
- (e) live-note 148/0, no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on ea50454f

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 10]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` lines under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (untracked, not staged, not src/tests/ops/configs — recorded); no staged line |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat b4f4e639 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-deploy-cos-restart` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-deploy-cos-restart` | 0 | `Deleted tag 'scratch-allow-probe-deploy-cos-restart' (was b4f4e639)` |
| PROBE | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main e3728f77] scratch: allowlist probe (reverted next line)` |
| PROBE | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `b4f4e639 docs(desk): R2372 deploy card 1013 deploy-cos-restart` — HEAD back |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-22-deploy-cos-restart` | 1 | absent |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-deploy-cos-restart` | 1 | absent |

### STEP-D1 (Thu Oct 22 02:17:49 EDT 2026)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-22 02:17:50 EDT)`. aset / sheet / radar probes OK: `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200`, `OK   radar                    idle (overnight)`, `OK   com.cobalt.aset              running   loaded, pid 6720 [launchd probe]`, `OK   com.cobalt.radar             running   running 212 min, heartbeat fresh`, `OK   com.cobalt.cos               running   running 340 min, heartbeat fresh`. The two REDs, named (neither is aset / sheet / radar, not a stop):
  - `RED  com.cobalt.agent             not loaded NOT LOADED in launchd — `launchctl list` does not know this label, so it will never fire again. Reload it: launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.agent.plist` (agent recorded retired)
  - `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required [type=missing, input_value={'block': None, 'error': ...e, 'block_sha256': None}, input_type=dict] …`
  - Also listed OK as `OWED (deferred bootstrap)`: prefill-refresh, checkpoint-0715/0745/0815/0845, playbook. `AMB com.cobalt.herdr unmanaged`.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0; ends `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line. `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 3.6 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = 6720. `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = 26270. com.cobalt.cos not in `<restart set>` and not recorded `not loaded — skipped`: no cos print. `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is OFFLINE.` (agent recorded retired; no `ps -p`).
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-22 02:17:12.161`; no traceback.
- LOG BASELINES: `<a0>` = 293 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 80 · `<lc0>` = 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`.
- MARKERS again → 0 · 0 · 0 · 1 · 0 · 0 · 0 · 0 (each its `before`).
- THE LAUNCHD SET: empty. MIGRATION: none (no `<RB>`, no D1-M).

## CONTINUE
next: STEP-D2.0

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
