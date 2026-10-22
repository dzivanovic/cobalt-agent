# deploy-deploy-cos-restart · SET: deploy-cos-restart · MIGRATIONS: none

## §0 Headline
- Deploy hub run of card `prompts/2026-10-21/1013-deploy-deploy-cos-restart-card.md`, first launch, started Thu Oct 22 01:26:35 EDT 2026.
- DEPLOYED: `main` `7a7973f9` → `fdf478a5` (fast-forward), tag `deploy-2026-10-22-deploy-cos-restart`; rollback tag `pre-deploy-cos-restart`.
- Gate GREEN on `ea50454f`: offline 9094/0 · with-DB 5930/0 · live-note 148/0; `cobalt_dev: 0013 — F2 = F0`.
- RESTARTS: none (docs + tests only); no resident went down; smoke GREEN; snapshot `11548c08`.

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

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved b4f4e639 "<card>"` → nothing. `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-deploy-cos-restart.md"` · `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy deploy-cos-restart — gate green on ea50454f" …` → `[main 7a7973f9] docs(report): deploy deploy-cos-restart — gate green on ea50454f`; `show --stat HEAD` → the one file (162 insertions). `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `7a7973f9` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `git -C <GATE> rev-parse --short=8 HEAD` → `fdf478a5` = `<stack-final>`; `rev-parse --short=8 fdf478a5^2` → `7a7973f9` = `<pre-merge>`; `merge-base --is-ancestor ea50454f fdf478a5` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat ea50454f fdf478a5 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` before → `newest snapshot: 3.6 h old`. `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 10193.7 MB`; `ssd: snapshot 11548c08 — 0 new / 3 changed, 25.0 MB added, 1 pruned`. `backup status` after → `newest snapshot: 0.0 h old`. Snapshot id: `11548c08`.
- D2.5 `date` → `Thu Oct 22 02:19:59 EDT 2026`; `heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-22 02:20:00 EDT)` — 130 s after D1's (02:17:50); the same two REDs as `<hb0>` (com.cobalt.agent not loaded, com.cobalt.replay failed); aset / sheet / radar OK; no new RED.
- D2.6 `date` → `Thu Oct 22 02:20:04 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-deploy-cos-restart` at `7a7973f9` → exit 0.

### STEP-4 (empty `<restart set>`)
- 4.1 `date` → `Thu Oct 22 02:20:15 EDT 2026` = `<t down>` (no resident goes down).
- 4.2 nothing (empty set; aset not in it: no orphan-clean; agent retired).
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `7a7973f9` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-cos-restart` → `Updating 7a7973f9..fdf478a5` / `Fast-forward` (9 files changed, 402 insertions(+), 37 deletions(-)).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 nothing to bootstrap. `date` → `Thu Oct 22 02:20:22 EDT 2026` = `<t up>`. Downtime: none (0 residents down).
- 4.6L `<launchd set>` empty: nothing.

## Smoke
`<t up>` = Thu Oct 22 02:20:22 EDT 2026 (empty set).
- FIRST CALLS: `<rp_up>` = 18 · `<rpr_up>` = 60 · `<re_up>` = 80 · `<lc_up>` = 39 (each = its D1 baseline).
- (a) `date` 02:20:32 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 6720` (SAME as D1: outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 26270` (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is OFFLINE.` (agent recorded retired: expected). GREEN.
- (b) `date` 02:20:35 · `grep -c "Started server process" …/aset.err` → `293` = `<a0>` (aset outside the set) · `tail -n 30 …/aset.err` → last line 2026-10-21 11:14:49 daily-note write diff; no new start, no traceback · Traceback aset `217` = `<ta0>` · Traceback radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`. Radar tails: below.
- (c) `date` 02:20:35 · `curl … https://cobalt.taild24291.ts.net/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) `date` 02:20:42 · MARKERS → 1 · 1 · 1 · 0 · 1 · 1 · 1 · 1 = each its `after`. GREEN.
- (e) first: `date` 02:20:52 · `heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-22 02:20:55 EDT)`: the same two REDs as `<hb0>` (com.cobalt.agent not loaded; com.cobalt.replay failed `TraderSettingsError: invalid radar.benchmark`), no new RED; `OK   com.cobalt.radar             running   running 215 min, heartbeat fresh`.
- (f) `date` 02:20:52 · `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` · `COBALT_ENV=production uv run cobalt jobs restarts 7a7973f9..fdf478a5` → exit 0, the same 9 rows as STEP-R, `RESTARTS: none` = STEP-R's `<restart set>` (empty), no UNCLASSIFIED. GREEN.
- (g) no migration.
- (b) radar tail: `date` 02:21:52 (`<t up>` + 90 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-22 02:20:32.189 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a `radar cycle:` line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the 12 lines → settled GREEN on the first tail.
- (e) second: `date` 02:22:46 · `heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-22 02:22:48 EDT)` — 113 s after the first (02:20:55); the same two REDs as `<hb0>`, no new RED; `OK   com.cobalt.radar             running   running 217 min, heartbeat fresh`. GREEN.
- (h) REVERT-READBACK: `date` 02:23:24 (`<t up>` + 182 s, after (b) settled) · `radar panel FAILED` `18` = `<rp_up>` · `radar pool refresh FAILED` `60` = `<rpr_up>` · `radar S5 evaluate FAILED` `80` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>` (no count grew) · `curl … /radar` → `200`. No `census` reads on the card. GREEN.
- (s) `ls /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` → exit 0, `/Users/cobalt/cobalt/ops/com.cobalt.cos.plist` (listed: green) · `grep -c -F "def test_f2_a_loaded_running_cos_is_admitted_at_step_r" /Users/cobalt/cobalt/tests/ops/test_deploy_cos_restart_1021.py` → exit 0, `1` (green). The gate ran `tests/ops` (deploy gate), offline 9094/0. No `<launchd set>` dry run.

THE CHAIN: every check committed (P2: `8dea7552…`, last line `held unfixed: 0` · `ready: YES` · `tip: 3770387d`) → the tips re-read (P3: `3770387d` = code tip = branch head) → the merged tree (T: `<m1>` `ea50454f`, no migration path) → RESTARTS derived (R: `RESTARTS: none`, no UNCLASSIFIED) → three suites green on `<m1>` (G: offline 9094/0 · with-DB 5930/0 · live-note 148/0, `cobalt_dev: 0013 — F2 = F0`) → `<stack-final>` `fdf478a5` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Updating 7a7973f9..fdf478a5` / `Fast-forward`) → markers (d: all eight at `after`) → no migration (g) → residents up after the merge, same pids (a: aset 6720, radar 26270) → radar cycling (b: cycle line 02:20:32; e: no new RED, radar heartbeat fresh) → the set's reads (s: cos plist listed, admit test `1`) → no new failure (h: the four counts flat). The card surface is not readable here; the desk confirms it with him (L70).

### STEP-7 — close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-22-deploy-cos-restart` → exit 0 (after green smoke). `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `fdf478a5`.
- `<pre-merge>` `7a7973f9` → `<stack-final>` `fdf478a5`. Tags: `pre-deploy-cos-restart` (at `7a7973f9`), `deploy-2026-10-22-deploy-cos-restart` (at `fdf478a5`).
- `<t down>` / `<t up>` / seconds: none (empty `<restart set>`; 4.1 `date` 02:20:15, 4.6 `date` 02:20:22; no resident down).
- uv sync line: STEP-R in `<GATE>` created `.venv` (`Installed 257 packages in 808ms`); no uv sync line in production commands.
- proof cost: none (MIGRATIONS: none, no D1-M). `migrations applied: none`. `<RB>` before / after: none.
- Snapshot id: `11548c08` (ssd).
- RESTARTS done: none (`<restart set>` empty). LAUNCHD done: none. BOOTSTRAP OWED: none from this run.
- THE ROLLBACK STRING (the desk's, never this session's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 fdf478a5` — ONE revert of the main-into-gate merge (it carries the set's merge with it); `<restart set>` empty: no resident down or up; `<launchd set>` empty.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — git titles it `Reapply "Merge branch 'main' into deploy/deploy-cos-restart"`.

### PRE-STOP SELF-CHECK (K25)
1. Every smoke row's evidence is quoted verbatim above with its `date` (02:20:32, 02:20:35, 02:20:42, 02:20:52, 02:21:52, 02:22:46, 02:23:24).
2. Code tip and head `3770387d` re-read at P3 (`rev-parse --short=8 3770387d` → `3770387d`, `rev-parse --short=8 ops/deploy-cos-restart` → `3770387d`); `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3770387d fdf478a5` → exit 0.
3. REVERT-READBACK shown at (h); every count, sha and `file:line` in this report was read from tool output this run.
4. No conflict marker: STEP-T ran clean (`Merge made by the 'ort' strategy.`), D2.1 ran clean (`Merge made by the 'ort' strategy.`).

## CONTINUE
OUTAGE STARTING Thu Oct 22 02:20:04 EDT 2026 — residents of <restart set> going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0. (`<restart set>` is EMPTY: no resident goes down; the merge lands with residents up.)
- 4.6 ended Thu Oct 22 02:20:22 EDT 2026 with residents up (nothing went down); smoke GREEN at 02:23:24; STEP-7 closed. Nothing to continue.

## DECISIONS
none

## RECORDS
- Downtime: none (empty `<restart set>`; no resident went down).
- REFUSED, not needed: none. Messages not followed: none (no `CONTINUE` message arrived).
- `cobalt_dev: 0013 (F2 = F0)` — from the gate log; lock released (`2388:lock released`), `<GATE>/.env` absent.
- RETIRE OWED: none (STEP-C `ADMITTED 0`, no removed plist).
- The carried RED as read (D1, D2.5 and smoke (e), unchanged throughout; neither is aset / sheet / radar): `RED  com.cobalt.agent             not loaded NOT LOADED in launchd …` (com.cobalt.agent recorded retired in `ops/desk/retired-labels`) and `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`. Not this set's; the replay RED is the desk's to route.
- `com.cobalt.cos`: running and loaded throughout (heartbeat `running 340 min` → `345 min`); not in `<restart set>` (RESTARTS: none), so no `launchctl` call of this run named it. With this set landed, the hub's own line now carries the three cos restart strings for a later set that derives `com.cobalt.cos`.
- Main dirt at D0: `?? .claude/settings.json.bak` (untracked, outside docs, not staged, not src/tests/ops/configs) — not a refused class; noted for the desk.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-deploy-cos-restart` and branch `deploy/deploy-cos-restart`; the set's branch `ops/deploy-cos-restart` and any worktree of it.
- Push is his, through the desk (L55): `main` at `fdf478a5` plus this report's commit; tags `pre-deploy-cos-restart`, `deploy-2026-10-22-deploy-cos-restart`.
- From the card's `## RECORDS`:
  - deploy-cos-restart: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-restart-check-2026-10-21.md` last line: CHECK DONE · job: deploy-cos-restart · pass: 1 · tip: 3770387d · house A: Grok FINDINGS: 5 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9094/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 216150
  - deploy-cos-restart: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-cos-restart` → `3770387d`; code tip `3770387d`
  - written by deploy-card.sh at 2026-10-22 01:26 ET (`date`); trial merge of the heads onto main in order: clean
- L74: a system reminder in this session asked for a `Claude-Session:` line on commits; recorded once under `## L74`, not acted on.

DEPLOYED deploy-2026-10-22-deploy-cos-restart fdf478a5 | set: deploy-cos-restart | migrations: none | gate: offline 9094/0 · with-DB 5930/0 · live-note 148/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 231383
