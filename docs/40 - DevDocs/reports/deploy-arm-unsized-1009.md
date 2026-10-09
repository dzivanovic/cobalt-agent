# deploy arm-unsized-1009 · SET: none · MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-09/183-deploy-arm-unsized-card.md` (committed `39130934`). Hub: `DEPLOY-HUB.md`. Session: `deploy-hub-arm-unsized-1009`.

## §0 Headline
- DEPLOYED `deploy-2026-10-09-arm-unsized`: main `b5a7f2a9` → `f355eee2` (ARM-unsized, `ops/arm-unsized-1009` code tip `676abb60`). No migration.
- Gate GREEN on `8cf7d015`: offline 4051/0 · with-DB 4938/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
- Outage 17:16:09 → 17:16:24 (15 s), aset + radar restarted on new pids; agent untouched.
- Smoke GREEN: markers 2 / 1, three curls 200, radar cycled 17:17:51, heartbeat green twice, failure counts flat at the readback.
- Rollback tag `pre-arm-unsized-1009` at `b5a7f2a9`; snapshot `b8f1c128`. One D0 decision (untracked `.claude/settings.json.bak`), not his.

## L74
- A harness attribution reminder in this session asked for a `Claude-Session:` line on commits. Recorded as data, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/183-deploy-arm-unsized-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/183-deploy-arm-unsized-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/183-deploy-arm-unsized-card.md" · 0 · 391309345ac8d65f2a9740b45a11e2c3fac9c6e0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/183-deploy-arm-unsized-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-arm-unsized-1009.md"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (whole output above) |
| P1 DATE | `date` | 0 | `Fri Oct  9 16:43:35 EDT 2026` |
| P2 check line | `tail -n 3 ".../reports/arm-unsized-check-2026-10-09.md"` | 0 | `CHECK DONE · job: arm-unsized-1009 · pass: 1 · tip: 676abb60 · … · held unfixed: 0 · open: 0 · … · suites: offline 4051/0 · with-DB 4938/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 182250` — carries `held unfixed: 0` and `ready: YES`; `tip: 676abb60` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/arm-unsized-check-2026-10-09.md"` | 0 | `ba2743790ad3e6448029137b1ca21c93783c16d3` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check report>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 676abb60` | 0 | `676abb60` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/arm-unsized-1009` | 0 | `46c96204` (= TIP) |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 676abb60 46c96204` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat 676abb60 46c96204 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no worktree holds `.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-arm-unsized-1009 status --short --branch` | 0 | `## deploy/arm-unsized-1009` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `39130934` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 39130934 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/arm-unsized-1009` | 0 | empty |
| P6 marker 1 | `grep -c -F "ARM_UNSIZED_BUTTON" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` | 1 | `0` (= before) |
| P6 marker 2 | `grep -c -F "sized=all(" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 46c96204 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 69822` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 69832` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 46c96204` → `Merge made by the 'ort' strategy.` (5 files: `radar_panel.md`, `arm-unsized-build-2026-10-09.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`, `tests/cobalt/test_s3_c3_panel_offline.py`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `8cf7d015` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 39130934..deploy/arm-unsized-1009` → `8cf7d015 Merge commit '46c96204' into deploy/arm-unsized-1009` (one line, one head).
- `merge-base --is-ancestor 676abb60 deploy/arm-unsized-1009` → exit 0 · `merge-base --is-ancestor 46c96204 deploy/arm-unsized-1009` → exit 0.
- `diff --stat 39130934 deploy/arm-unsized-1009 -- src/cobalt/db_migrations` → nothing (no migration; MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 39130934 deploy/arm-unsized-1009 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/arm-unsized-build-2026-10-09.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
(preceded by uv's venv creation lines: `Creating virtual environment at: .venv` · `Installed 253 packages in 790ms`). No `UNCLASSIFIED`. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (matches the check's line).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 676abb60 8cf7d015 -- . ":(exclude)docs"` → `ops/desk/bare-guard.py | 61 +++…` · `tests/ops/test_bare_guard.py | 145 +++…` (2 files, from `main` since the check). Not equal → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 16.61s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-arm-unsized-1009 all --deploy` (no `--deselect`: the build report `arm-unsized-build-2026-10-09.md:137` names none; TICKERS none; no migration) — launched in the background → exit 0. Verdict lines whole:
```
offline 4051/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4938/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-arm-unsized-1009-all-20261009-164523.log
```
- (a) offline `4051/0`. (c) PASS 1 skips: each inside the allowed set — `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95`, which is the `@requires_live` decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (Read `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`).
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:884`). (c2) `dev forward: APPLIED 17:08:30` (log `:1095`). (c3) with-DB `4938/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1965`) = F0 field for field → `cobalt_dev: 0013 — F2 = F0` (log `:2016`).
- THE RELEASE: log `:2017-2021` `sh …/release-devdb-lock.sh deploy-arm-unsized-1009` → `lock released` · `ls …/.env` → `No such file or directory` (the log stamps no time; after 17:08:30, before 17:13:37). Verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-arm-unsized-1009" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir). `.env: removed (L76 lock released)`.
- (e) live-note `146/0`; no skip names `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 8cf7d015

## Deploy table
| item | value |
|---|---|
| main | `b5a7f2a9` (`<pre-merge>`) → `f355eee2` (`<stack-final>`) |
| gate tree | `<m0>` `39130934` · `<m1>` `8cf7d015` |
| tags | `pre-arm-unsized-1009` at `b5a7f2a9`; `deploy-2026-10-09-arm-unsized` at `f355eee2` (STEP-7, after green smoke) |
| outage | `<t down>` 17:16:09 · `<t up>` 17:16:24 · 15 s |
| uv sync line | none in production calls; the gate worktree's first `uv run` created its own `.venv` (`Installed 253 packages in 790ms`) |
| proof cost | none (no migration, no D1-M) |
| migrations applied | none |
| `<RB>` before / after | none (MIGRATIONS: none) |
| snapshot | `b8f1c128` (ssd), dump 6592.8 MB |
| RESTARTS done | com.cobalt.aset com.cobalt.radar |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 f355eee2` — residents com.cobalt.aset and com.cobalt.radar down first, up after. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. |

STEP-D0 (17:13–17:14):
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 96]`. `status --porcelain` → ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` / `??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (see `## DECISIONS` 1). No staged line; no dirty `src/`, `tests/`, `ops/` or other `configs/` path.
- `git -C /Users/cobalt/cobalt diff --stat 39130934 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-arm-unsized-1009` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-arm-unsized-1009' (was 39130934)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 2d9a5219] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `39130934 docs(desk): deploy card 183 ARM-unsized` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-09-arm-unsized` → exit 1 · `refs/tags/pre-arm-unsized-1009` → exit 1.

STEP-D1 baseline (17:14:04):
- `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 17:14:05 EDT)`; `OK   radar                    scanning (aftermarket), members 50`; `OK   com.cobalt.aset              running   loaded, pid 69822`; `OK   com.cobalt.radar             running   running 167 min, heartbeat fresh`; `OK   com.cobalt.agent             running   pid 22243 alive`; one `AMB  com.cobalt.herdr unmanaged … runs outside launchd by declared interim`. No RED.
- `<val0>`: `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.2 h old` (ssd ARMED).
- aset `state = running`, `<aset pid>` 69822 · radar `state = running`, `<radar pid>` 69832 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last line `2026-10-09 17:14:05.076 | INFO | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791580356807` (the 7 before: `cards.expire: falling back to the session close` INFO lines). No traceback.
- LOG BASELINES: `<a0>` Started server process = 52 · `<ta0>` aset Traceback = 2 · `<tr0>` radar Traceback = 0 · `<tc0>` TaxonomyConfigError = 0 · `<rp0>` radar panel FAILED = 18 · `<rpr0>` radar pool refresh FAILED = 60 · `<re0>` radar S5 evaluate FAILED = 42 · `<lc0>` lifecycle card read failed = 39.
- `curl … /radar` → `200`. MARKERS again: `ARM_UNSIZED_BUTTON` → `0` · `sized=all(` → `0` (both = before).
- MIGRATIONS none: no `<RB>`, no census, no D1-M.

STEP-D2:
- D2.0 `add` + `commit -m "docs(report): deploy arm-unsized-1009 — gate green on 8cf7d015" …` → `[main b5a7f2a9]`; `show --stat HEAD` → one file, `.../reports/deploy-arm-unsized-1009.md | 135 +++`. `rev-parse --short=8 main` → `b5a7f2a9` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `f355eee2`; `rev-parse --short=8 f355eee2^2` → `b5a7f2a9` = `<pre-merge>`; `merge-base --is-ancestor 8cf7d015 f355eee2` → exit 0.
- D2.3 `diff --stat 8cf7d015 f355eee2 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` before → `newest snapshot: 1.3 h old`. `backup run` (17:14:56–17:15:39) → `backup: cobalt_brain dumped, 6592.8 MB` · `ssd: snapshot b8f1c128 — 0 new / 2 changed, 107.7 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 17:15:53 `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 17:15:55 EDT)` — 110 s after D1's 17:14:05; no RED.
- D2.6 `date` → `Fri Oct  9 17:15:59 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-arm-unsized-1009` at `b5a7f2a9`.

STEP-4 (the outage):
- 4.1 `date` → `Fri Oct  9 17:16:09 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → ok; `launchctl print gui/501/com.cobalt.aset` → exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501`. `launchctl bootout gui/501/com.cobalt.radar` → ok; print → exit 113 `Could not find service "com.cobalt.radar" …`. Agent not in the set: untouched.
- 4.3 `rev-parse --short=8 HEAD` → `b5a7f2a9` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/arm-unsized-1009` → `Updating b5a7f2a9..f355eee2` / `Fast-forward` (5 files: `radar_panel.md`, `arm-unsized-build-2026-10-09.md`, `src/cobalt/aset/radar_panel.py`, two tests).
- 4.4 `migrations applied: none` (MIGRATIONS: none).
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → ok · `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → ok. aset `state = running`, `pid = 93108` (≠ 69822) · radar `state = running`, `pid = 93120` (≠ 69832). `date` → `Fri Oct  9 17:16:24 EDT 2026` = `<t up>`. Downtime 15 s.

## Smoke
FIRST CALLS after `<t up>` 17:16:24: `radar panel FAILED` → 18 = `<rp_up>` · `radar pool refresh FAILED` → 60 = `<rpr_up>` · `radar S5 evaluate FAILED` → 42 = `<re_up>` · `lifecycle card read failed` → 39 = `<lc_up>` (each = its D1 baseline).
- (a) [17:16:35] aset `state = running` pid 93108 (new, ≠ 69822) · radar `state = running` pid 93120 (new, ≠ 69832) (4.6's prints) · `cobalt.sh status` → `  Cobalt is ONLINE (PID: 22243).` (agent not in the set: same pid). GREEN.
- (b) [17:16:35] `grep -c "Started server process" aset.err` → `53` (`<a0>` 52 +1, ≤ +2). `tail -n 30 aset.err` → last start `INFO:     Started server process [93114]` · `2026-10-09 17:16:20.943 | INFO | cobalt.voice.web:voice_startup:183 - voice: scratch dir … locked by this process; start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`. aset Traceback `2` = `<ta0>` · radar Traceback `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`. Spaced tail 1 [17:17:54, `<t up>` + 90 s] `tail -n 12 radar.err` → last line `2026-10-09 17:17:51.299 | INFO | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791580582358` (stamped after `<t up>`); the 11 above are `cards.expire: falling back to the session close` INFO lines; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN.
- (c) [17:16:35] `curl … /` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `grep -c -F "ARM_UNSIZED_BUTTON" …/radar_panel.py` → `2` (after `2`) · `grep -c -F "sized=all(" …/radar_panel.py` → `1` (after `1`). GREEN.
- (e) read 1 [17:16:45] `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 17:16:46 EDT)`; `OK   com.cobalt.aset              running   loaded, pid 93108`; `OK   com.cobalt.radar             running   running 0 min, heartbeat fresh`; `OK   radar                    scanning (aftermarket), members 50`. Read 2 [17:18:39] → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 17:18:41 EDT)` (115 s after read 1); `OK   com.cobalt.radar             running   running 2 min, heartbeat fresh`; aset pid 93108. No RED in either; the only non-OK line is the `AMB com.cobalt.herdr` line already in `<hb0>`. GREEN. (A fill read at 17:18:35 was 109 s after read 1, short of 110, and is not counted.)
- (f) [17:16:45] `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` · `jobs restarts b5a7f2a9..f355eee2` → exit 0, the same 5 rows as STEP-R, `RESTARTS: com.cobalt.aset com.cobalt.radar` = `<restart set>`, no `UNCLASSIFIED`. GREEN.
- (g) no migration: not run.
- (s) SMOKE READS: inert ARM button `grep -c -F "ARM_UNSIZED_BUTTON" …` → exit 0, `2` (≥1, green) · sized flag `grep -c -F "sized=all(" …` → exit 0, `1` (≥1, green). Tests the gate ran on `8cf7d015`: the build's offline tests in `test_radar_panel_cards.py` / `test_s3_c3_panel_offline.py` are inside `offline 4051/0`, its with-DB neighbour inside `with-DB 4938/0`.
- (h) REVERT-READBACK [17:19:26, `<t up>` + 182 s]: `radar panel FAILED` → 18 = `<rp_up>` · `radar pool refresh FAILED` → 60 = `<rpr_up>` · `radar S5 evaluate FAILED` → 42 = `<re_up>` · `lifecycle card read failed` → 39 = `<lc_up>` (none growing) · `curl … /radar` → `200` · radar Traceback `0`, aset Traceback `2` (= baselines). Spaced tail 2 `tail -n 12 radar.err` → last line still `2026-10-09 17:17:51.299 | INFO | … radar cycle: scanning scan_id=1791580582358`, no failure line. No census reads (no migration). GREEN.

SMOKE: GREEN.

THE CHAIN: every check committed (P2: `ba274379`) · the tips re-read (P3: `676abb60`, `46c96204`) · the merged tree (T: `8cf7d015`, one merge, clean) · RESTARTS derived (R: aset + radar) · three suites green on `<m1>` (G) · `<stack-final>` `f355eee2` = `<m1>` + docs (D2.3) · the landed code (4.3: `Updating b5a7f2a9..f355eee2`) · markers 2 / 1 (d) · no migration (g) · residents up on new pids after the merge (a) · radar cycling (b, e) · the set's reads (s) · no new failure (h). The card surface (the inert ARM button on an unsized card in `/radar`) is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row is quoted verbatim with its `date` (17:16:35, 17:16:45, 17:17:54, 17:18:39, 17:19:26).
2. `merge-base --is-ancestor 676abb60 f355eee2` → exit 0 · `merge-base --is-ancestor 46c96204 f355eee2` → exit 0 (both re-read at P3).
3. REVERT-READBACK shown at (h); every count, sha and `file:line` here comes from tool output in this run.
4. No conflict marker: STEP-T merged clean, D2.1 merged clean; `git -C <GATE> status --short --branch` at close → `## deploy/arm-unsized-1009` alone.

## CONTINUE
next: STEP-D2 (gate green at 17:13:37; D0 and D1 done)
OUTAGE STARTING 17:15:59 — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
outage ended 17:16:24, residents up; smoke green 17:19:26; tagged `deploy-2026-10-09-arm-unsized` at `f355eee2`. Nothing left to run.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is an untracked file on `main` that D0's accepted list does not name and its refused list (`src/`, `tests/`, `ops/`, `configs/`, staged) does not name either [17:13]. Safe default taken: not refused — it is untracked, outside every refused root, was present at session start (the launch's git snapshot lists it), and `merge --ff-only` does not touch it.

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Read instead with `grep -n -F "lock released"` and the Read tool on the log.
- Downtime 15 s (17:16:09 → 17:16:24), under 300 s.
- `cobalt_dev: 0013 (F2 = F0)`; L76 lock released by `gate.sh`, `<GATE>/.env` absent at close.
- RETIRE OWED: none (no plist removed).
- Carried RED: none; every heartbeat read was GREEN. The standing `AMB com.cobalt.herdr unmanaged` line is amber, not red, and was in `<hb0>`.
- Messages not followed: none from another session. The L74 attribution line is under `## L74`.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-arm-unsized-1009` and branch `deploy/arm-unsized-1009`; the set's branch `ops/arm-unsized-1009` and its worktree if any. The gate's `.venv` was created by this run's first `uv run`.
- Push is his (L55): `main` is ahead of `origin/main`; tags `pre-arm-unsized-1009` and `deploy-2026-10-09-arm-unsized` are local.
- From the card: arm-unsized-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/arm-unsized-check-2026-10-09.md` last line: CHECK DONE · job: arm-unsized-1009 · pass: 1 · tip: 676abb60 · house A: Sol FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 0 · suites: offline 4051/0 · with-DB 4938/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 182250
- From the card: arm-unsized-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/arm-unsized-1009` → `46c96204`; code tip `676abb60`
- From the card: written by deploy-card.sh at 2026-10-09 16:43 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-09-arm-unsized f355eee2 | set: none | migrations: none | gate: offline 4051/0 · with-DB 4938/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 194815
