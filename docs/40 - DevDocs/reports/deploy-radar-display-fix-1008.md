# deploy radar-display-fix-1008 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED card 148 (`ops/radar-display-fix-1008` at `eb14f860`, card 118 `/radar` display fix, his R685): `main` `e9cfc513` → `752a8ce6`, tag `deploy-2026-10-08-radar-display-fix`.
- Gate green on `6da1ed7e`, run whole: offline 4003/0 · with-DB 4887/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0).
- Outage 14:23:58 → 14:24:15 EDT (17 s), `com.cobalt.aset` + `com.cobalt.radar` restarted; no migration; snapshot `013c9f6d`.
- Smoke GREEN: residents on new pids, radar cycling, `/radar` 200, markers 2 / 1, failure counts flat, heartbeat GREEN twice.
- One decision (an untracked `.claude/settings.json.bak` on `main`), not his. Rollback string under `## Deploy table`.

## L74
- The session's system context asked commits to also carry a `Claude-Session: https://claude.ai/code/session_012RCKdzpNEaPcFxiymwgWB9` line. Recorded once as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/148-deploy-radar-display-fix-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/148-deploy-radar-display-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/148-deploy-radar-display-fix-card.md" · 0 · 9c4c3b970ae21f3cebaa805d97c591fc73c24f50
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/148-deploy-radar-display-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la <REPORT>` → `No such file or directory` (exit 1) before this write.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 INSTALLED / card / AUTHORIZATION | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (whole under `## AUTHORIZATION`) |
| P1 DATE | `date` | 0 | `Thu Oct  8 13:51:07 EDT 2026` |
| P2 check, last line | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-display-fix-check-2026-10-08.md"` | 0 | `CHECK DONE · job: radar-display-fix-1008 · pass: 1 · tip: eb14f860 · house A: Sol FINDINGS: 3 · findings: 6 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 0 · suites: offline 4003/0 · with-DB 4887/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 176294` — carries `held unfixed: 0`, `ready: YES`, `tip: eb14f860` = row code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/radar-display-fix-check-2026-10-08.md"` | 0 | `758c07c9d90a873c6250086fd82264c129060961` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/radar-display-fix-check-2026-10-08.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 eb14f860` | 0 | `eb14f860` |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-display-fix-1008` | 0 | `eb14f860` (= row, = `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor eb14f860 eb14f860` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat eb14f860 eb14f860 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-radar-display-fix-1008 status --short --branch` | 0 | `## deploy/radar-display-fix-1008` |
| P5 `<m0>` | `git -C /Users/cobalt/cobalt-wt/deploy-radar-display-fix-1008 rev-parse --short=8 HEAD` | 0 | `76979452` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 76979452 main` | 0 | — |
| P5 nothing ahead | `git -C /Users/cobalt/cobalt log --oneline main..deploy/radar-display-fix-1008` | 0 | empty |
| P6 marker 1 | `grep -c -F "termOpen" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` | 1 | `0` (= before) |
| P6 marker 2 | `grep -c -F "def test_an_open_terminal_does_not_pause_the_tick" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel.py` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main eb14f860 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 37788` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 37799` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-radar-display-fix-1008 merge --no-edit eb14f860` → `Merge made by the 'ort' strategy.` (5 files: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `docs/40 - DevDocs/reports/radar-display-fix-build-2026-10-08.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`; 400 insertions, 12 deletions).
- `<m1>`: `git -C <GATE> rev-parse --short=8 HEAD` → `6da1ed7e`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 76979452..deploy/radar-display-fix-1008` → `6da1ed7e Merge commit 'eb14f860' into deploy/radar-display-fix-1008` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor eb14f860 deploy/radar-display-fix-1008` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 76979452 deploy/radar-display-fix-1008 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 76979452 deploy/radar-display-fix-1008 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a fresh `.venv` build: `Installed 253 packages in 790ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-build-2026-10-08.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar`.

## L68 GATE
- EQUAL-TREE CLAUSE does NOT hold: `git -C /Users/cobalt/cobalt diff --stat eb14f860 6da1ed7e -- . ":(exclude)docs"` → `ops/desk/bare-guard.py | 73`, `ops/desk/desk-launch.sh | 5`, `tests/ops/test_bare_guard.py | 225` (3 files, 261+/42−; `main` moved since the check's base). The gate runs whole (`--deploy`).
- Deselects: none (the build report: "no `--deselect`: this build adds no with-DB test"). `TICKERS: none`, no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 16.29s` — 0 failed (skips are with-DB tests: `Postgres env settings not available` / `requires_db`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-radar-display-fix-1008 all --deploy` (background) → exit 0. Verdict lines, whole:
```
offline 4003/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4887/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-radar-display-fix-1008-all-20261008-135251.log
```
- (a) offline `4003/0` · (c) pass 1 + (c3) → with-DB `4887/0` · (e) live-note `146/0`. No migration on the card: no (c2) forward (`dev forward` not applied).
- SKIPPED lines: all seven inside the allowed set (`test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95`, the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture():` at line 96 — Grep of the gate tree).
- (f) log: `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 880) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 1865) · `cobalt_dev: 0013 — F2 = F0` (line 1916).
- THE RELEASE: log line 1918 `lock released`, 1922 `.env: removed` (the log stamps no clock on it; the gate ended before 14:21:19 EDT). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-radar-display-fix-1008" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `0`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 6da1ed7e

## Deploy table
STEP-D0 (14:21 EDT):
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 129]`.
- `git -C /Users/cobalt/cobalt status --porcelain` → no staged line; ` M` lines: `.claude/settings.json` and six under `docs/40 - DevDocs/reports/`; `??` lines all under `docs/40 - DevDocs/` except `.claude/settings.json.bak` (see `## DECISIONS` 1). No dirty `src/`, `tests/`, `ops/`, `configs/` path.
- `git -C /Users/cobalt/cobalt diff --stat 76979452 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-radar-display-fix-1008` → ok; `tag -d …` → `Deleted tag 'scratch-allow-probe-radar-display-fix-1008' (was 76979452)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main caedff0f] …`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `76979452 docs(desk): card 137 TIP f105b82e and check report filled` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-08-radar-display-fix` → exit 1; `… refs/tags/pre-radar-display-fix-1008` → exit 1.

STEP-D1 (baseline, read-only):
- `date` → `Thu Oct  8 14:21:47 EDT 2026` · `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 14:21:48 EDT)`; `OK   radar                    scanning (rth), members 50`; `OK   com.cobalt.radar             running   running 1342 min, heartbeat fresh`; `OK   com.cobalt.aset              running   loaded, pid 37788 [launchd probe]`; only non-OK row `AMB  com.cobalt.herdr             unmanaged AMBER …` (declared interim). No RED.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 0.8 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` `37788` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` `37799` · `cobalt.sh status` → `  Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-08 14:20:41.249 | INFO     | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791483555250` (seven `cards.expire: falling back to the session close` INFO lines above it); no traceback.
- LOG BASELINES: `<a0>` Started server process (aset.err) `49` · `<ta0>` Traceback (aset.err) `2` · `<tr0>` Traceback (radar.err) `0` · `<tc0>` TaxonomyConfigError (radar.err) `0` · `<rp0>` radar panel FAILED `17` · `<rpr0>` radar pool refresh FAILED `59` · `<re0>` radar S5 evaluate FAILED `41` · `<lc0>` lifecycle card read failed `39`.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`. MARKERS: `termOpen` → `0`; `def test_an_open_terminal_does_not_pause_the_tick` → `0` (both = before).
- `MIGRATIONS: none` → no `<RB>`, no census, no D1-M.

STEP-D2:
- D2.0 `git add` + `git commit -m "docs(report): deploy radar-display-fix-1008 — gate green on 6da1ed7e" …` → `[main e9cfc513] …`; `show --stat HEAD` → one file, `.../reports/deploy-radar-display-fix-1008.md | 134 +++`. `<pre-merge>` = `e9cfc513`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `752a8ce6`; `rev-parse --short=8 752a8ce6^2` → `e9cfc513` (= `<pre-merge>`); `merge-base --is-ancestor 6da1ed7e 752a8ce6` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 6da1ed7e 752a8ce6 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs-only).
- D2.4 `backup status` → `newest snapshot: 0.8 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain dumped, 6035.3 MB` · `ssd: snapshot 013c9f6d — 0 new / 4 changed, 79.9 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 heartbeat reads at 14:23:26, 14:23:31, 14:23:37 (98, 103, 109 s after D1's 14:21:48: under 110) and `date` `Thu Oct  8 14:23:41 EDT 2026` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 14:23:43 EDT)` (115 s). No RED.
- D2.6 `date` → `Thu Oct  8 14:23:46 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-radar-display-fix-1008` at `e9cfc513`.

STEP-4 (the outage, `<restart set>` = `com.cobalt.aset com.cobalt.radar`):
- 4.1 `date` → `<t down>` `Thu Oct  8 14:23:58 EDT 2026`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → ok; print → `Could not find service "com.cobalt.aset" in domain for user gui: 501` (exit 113). `launchctl bootout gui/501/com.cobalt.radar` → ok; print → `Could not find service "com.cobalt.radar" in domain for user gui: 501` (exit 113). Agent not in the set: untouched.
- 4.3 `rev-parse --short=8 HEAD` → `e9cfc513` (= `<pre-merge>`). `git -C /Users/cobalt/cobalt merge --ff-only deploy/radar-display-fix-1008` → `Updating e9cfc513..752a8ce6` / `Fast-forward` (5 files, 400+/12−).
- 4.4 `migrations applied: none` (`MIGRATIONS: none`).
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → ok; `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → ok. print aset → `state = running`, `pid = 39461` (≠ 37788); print radar → `state = running`, `pid = 39471` (≠ 37799). `<t up>` `Thu Oct  8 14:24:15 EDT 2026`. Downtime 17 s.

SUMMARY:
| field | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `e9cfc513` → `752a8ce6` |
| tags | rollback `pre-radar-display-fix-1008` (at `e9cfc513`); deploy `deploy-2026-10-08-radar-display-fix` (STEP-7, after green smoke) |
| `<t down>` / `<t up>` / seconds | 14:23:58 / 14:24:15 / 17 |
| uv sync line | none in production (the gate tree built its own `.venv`: `Installed 253 packages in 790ms`) |
| proof cost | n/a (no migration) |
| migrations applied | none |
| `<RB>` before / after | n/a |
| snapshot | `013c9f6d` (ssd), `cobalt_brain` 6035.3 MB |
| RESTARTS done | `com.cobalt.aset com.cobalt.radar` |

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 752a8ce6` — `com.cobalt.aset` and `com.cobalt.radar` down first, up after.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — git titles it `Reapply "Merge branch 'main' into deploy/radar-display-fix-1008"`.

## Smoke
`<t up>` = 14:24:15 EDT. FIRST CALLS: `<rp_up>` `17` · `<rpr_up>` `59` · `<re_up>` `41` · `<lc_up>` `39` (each = its D1 baseline).

| row | `date` | command | result | verdict |
|---|---|---|---|---|
| (a) | 14:24:30 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 39461` (D1 37788: NEW) | GREEN |
| (a) | 14:24:30 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 39471` (D1 37799: NEW) | GREEN |
| (a) | 14:24:30 | `/Users/cobalt/cobalt/cobalt.sh status` | `  Cobalt is ONLINE (PID: 22243).` (agent outside the set: SAME pid) | GREEN |
| (b) | 14:24:33 | `grep -c "Started server process" /Users/cobalt/cobalt/logs/aset.err` | `50` (`<a0>` 49: +1, ≤ +2) | GREEN |
| (b) | 14:24:33 | `tail -n 30 /Users/cobalt/cobalt/logs/aset.err` | `INFO:     Started server process [39467]` … `INFO:     Application startup complete.` / `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` | GREEN |
| (b) | 14:24:33 | Traceback aset.err · Traceback radar.err · TaxonomyConfigError radar.err | `2` · `0` · `0` (= `<ta0>` `<tr0>` `<tc0>`) | GREEN |
| (c) | 14:24:38 | `curl … http://127.0.0.1:5010/` · `…/radar` · `…/radar\?frame=phone` | `200` · `200` · `200` (first attempt each) | GREEN |
| (d) | 14:24:38 | `grep -c -F "termOpen" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` | `2` (after `2`) | GREEN |
| (d) | 14:24:38 | `grep -c -F "def test_an_open_terminal_does_not_pause_the_tick" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel.py` | `1` (after `1`) | GREEN |
| (s) | 14:24:38 | the open-terminal keep: `grep -c -F "termOpen" …/radar_panel.py` | exit 0, `2` (1 or more) | GREEN |
| (s) | 14:24:38 | the control test: `grep -c -F "def test_an_open_terminal_does_not_pause_the_tick" …/test_radar_panel.py` | exit 0, `1` (1 or more); the test itself ran green in the gate (with-DB 4887/0, offline 4003/0) | GREEN |
| (f) | 14:24:43 | `COBALT_ENV=production uv run cobalt jobs restarts e9cfc513..752a8ce6` | exit 0, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= STEP-R), no `UNCLASSIFIED` | GREEN |
| (f) | 14:24:43 | `COBALT_ENV=production uv run cobalt validate` | exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`, `Placement (docs/PLACEMENT.md): tree clean.` | GREEN |
| (e) 1 | 14:24:49 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 14:24:51 EDT)`; `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh`; `OK   com.cobalt.aset              running   loaded, pid 39461` | GREEN |
| (b) radar tail 1 | 14:25:45 (`<t up>` + 90 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last line `2026-10-08 14:25:41.208 | INFO     | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791483853058` (after `<t up>`); eleven `cards.expire: falling back to the session close` INFO lines above; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback — settles GREEN | GREEN |
| (e) 2 | 14:26:43 | `COBALT_ENV=production uv run cobalt heartbeat show` (114 s after (e) 1; clock filled with `date` + heartbeat pairs, all `HEARTBEAT GREEN`) | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 14:26:45 EDT)`; `OK   com.cobalt.radar             running   running 3 min, heartbeat fresh`; `OK   radar                    scanning (rth), members 50` — no RED | GREEN |
| (g) | — | no migration | — | n/a |
| (h) | 14:27:18 (`<t up>` + 183 s) | the four failure counts | `17` · `59` · `41` · `39` (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`; none grew) | GREEN |
| (h) | 14:27:18 | `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` | `200` | GREEN |
| (h) | 14:27:18 | Traceback radar.err · Traceback aset.err | `0` · `2` (= baseline) | GREEN |

Census reads: none on the card. The radar tail settled GREEN at the first spaced read; the second and third tails are not needed (RED only when the third shows no cycle line).

THE CHAIN: every check committed (P2: `758c07c9…`, clean) · the tips (P3: `eb14f860` = head = `TIP`) · the merged tree (T: `6da1ed7e`, one merge, no migration path) · RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`, no UNCLASSIFIED) · three suites green on `<m1>` (G: offline 4003/0 · with-DB 4887/0 · live-note 146/0) · `<stack-final>` `752a8ce6` = `<m1>` + docs (D2.3) · the landed code (4.3: `Updating e9cfc513..752a8ce6`) · markers (d: `2`, `1`) · the migration read back (g: none) · residents up after the merge (a: pids 39461, 39471) · radar cycling (b: 14:25:41 cycle; e: `heartbeat fresh` twice) · the set's reads (s) · no new failure (h). The card surface (`/radar` with an open TERMINAL across the swap) is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row carries its `date` and the verbatim tool output above.
2. Code tip and head `eb14f860` re-read at P3; `git -C /Users/cobalt/cobalt merge-base --is-ancestor eb14f860 752a8ce6` → exit 0.
3. REVERT-READBACK (h) shown: four counts unchanged from `<t up>`. Every count, sha and `file:line` here was read from tool output in this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same; no conflict path.
5. THE RELEASE: `ls -la /Users/cobalt/cobalt-wt/deploy-radar-display-fix-1008/.env` → No such file; the lock was released by `gate.sh` at the gate's end.

STEP-7: `git -C /Users/cobalt/cobalt tag deploy-2026-10-08-radar-display-fix` → ok, at `752a8ce6` (`git -C /Users/cobalt/cobalt log --oneline -1` → `752a8ce6 Merge branch 'main' into deploy/radar-display-fix-1008`).

## CONTINUE
gate green at 14:21:19 EDT; STEP-D0 and D1 done.
STEP-D2 done (pre-merge e9cfc513, stack-final 752a8ce6, tag pre-radar-display-fix-1008).
OUTAGE STARTING 14:23:46 EDT — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED 14:24:15 EDT — merged 752a8ce6, both residents running on new pids.
Smoke GREEN at 14:27:18 EDT; tagged deploy-2026-10-08-radar-display-fix. Run complete.

## DECISIONS
1. ASK DESK: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak` — on neither D0's ACCEPTED list (it accepts ` M .claude/settings.json`, not its untracked `.bak`) nor its REFUSED list (`src/`, `tests/`, `ops/`, `configs/`, staged). Safe default taken: not a refusal; it is untracked, outside the code tree, and does not enter the merge (D2.3 proves the landed tree). Went on. [14:21:47 EDT]

## RECORDS
- Downtime: 14:23:58 → 14:24:15 EDT, 17 s (under 300 s).
- `cobalt_dev: 0013 (F2 = F0)` — `F0`/`F2` `664 35 272c95bbb12241e3611e4b36326ccf87`; `.env: removed`, lock released by `gate.sh`.
- No `REFUSED, not needed` line; no message received or not followed; no `RETIRE OWED` (no plist changed).
- Carried RED: none — `<hb0>` was `HEARTBEAT GREEN … nothing red`.
- L74: one block in the session's system context asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-display-fix-1008` and branch `deploy/radar-display-fix-1008`; the set's branch `ops/radar-display-fix-1008` and its build worktree. The desk's.
- `main` is ahead of `origin/main` (push is his, L55).
- Card's `## RECORDS`, copied:
  - radar-display-fix-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-display-fix-check-2026-10-08.md` last line: CHECK DONE · job: radar-display-fix-1008 · pass: 1 · tip: eb14f860 · house A: Sol FINDINGS: 3 · findings: 6 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 0 · suites: offline 4003/0 · with-DB 4887/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 176294
  - radar-display-fix-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-display-fix-1008` → `eb14f860`; code tip `eb14f860`
  - written by deploy-card.sh at 2026-10-08 13:39 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-08-radar-display-fix 752a8ce6 | set: none | migrations: none | gate: offline 4003/0 · with-DB 4887/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 193747
