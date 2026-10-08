# deploy radar-display-fix-1008 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of card 148 (`ops/radar-display-fix-1008` at `eb14f860`), started 2026-10-08 13:51:07 EDT. In progress.

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

## Smoke

## CONTINUE
gate green at 14:21:19 EDT; STEP-D0 and D1 done.
next: STEP-D2

## DECISIONS
1. ASK DESK: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak` — on neither D0's ACCEPTED list (it accepts ` M .claude/settings.json`, not its untracked `.bak`) nor its REFUSED list (`src/`, `tests/`, `ops/`, `configs/`, staged). Safe default taken: not a refusal; it is untracked, outside the code tree, and does not enter the merge (D2.3 proves the landed tree). Went on. [14:21:47 EDT]

## RECORDS

(run in progress — next step under ## CONTINUE)
