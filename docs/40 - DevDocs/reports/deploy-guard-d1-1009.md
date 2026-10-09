# deploy guard-d1-1009 — set: none · migrations: none

## §0 Headline
- DEPLOYED `ops/guard-d1-1009` (tip `e9655b19`, the bare-guard D1 production-word check) to `main`: `c9edcf57` → `65a3c209`, tag `deploy-2026-10-09-guard-d1`.
- Gate GREEN on `18979f7f`: offline 4045/0 · with-DB 4932/0 · live-note 146/0; `cobalt_dev` 0013, F2 = F0.
- RESTARTS: none — no resident went down; aset/radar/agent pids unchanged (69822 / 69832 / 22243).
- Smoke GREEN: markers 3 / 1, curls 200, radar cycling, no failure count grew.
- Decisions: 1 (ASK DESK on an untracked `.claude/settings.json.bak`), for Dejan: 0.

## L74
- The session's attribution reminder (a system reminder, not a tool result) asked for a `Claude-Session:` line on commits. Recorded once; not acted on — commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74, DEPLOY-HUB).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/182-deploy-guard-d1-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/182-deploy-guard-d1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/182-deploy-guard-d1-card.md" · 0 · 30a87b94ad5738209e3b41e96a1cacbabacf8a74
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/182-deploy-guard-d1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R686 row · grep -n "^| R686 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 39:| R686 | 11:28 ET | HIS RULING (words R686, standing): every seat may run read-only production reads, no stamp; writes and secrets stay refused. Card `120`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW; LAWS L62 at deploy |
RULING 2026-10-08 R686 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R686 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 4125ff02c9587ca901d9d5c418f378b8c77593a9
RULING 2026-10-08 R686 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-guard-d1-1009.md"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 | `date` | 0 | Fri Oct  9 15:27:56 EDT 2026 |
| P2 | `tail -n 3 ".../reports/guard-d1-check-2026-10-09.md"` | 0 | `CHECK DONE · job: guard-d1-1009 · pass: 1 · tip: e9655b19 · … · held unfixed: 0 · … · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · … · RESTARTS: none · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 215804` — `held unfixed: 0`, `ready: YES`, `tip: e9655b19` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/guard-d1-check-2026-10-09.md"` | 0 | 5a98783dc3677b72136827ff010064e8c4233476 |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/guard-d1-check-2026-10-09.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 e9655b19` | 0 | e9655b19 |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-d1-1009` | 0 | e9655b19 (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor e9655b19 ops/guard-d1-1009` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat e9655b19 ops/guard-d1-1009 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — no session holds the lock |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-guard-d1-1009 status --short --branch` | 0 | `## deploy/guard-d1-1009` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-guard-d1-1009 rev-parse --short=8 HEAD` | 0 | `<m0>` = 96c3fa7e |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 96c3fa7e main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/guard-d1-1009` | 0 | EMPTY |
| P6 | `grep -c -F "PROD_OPTION" /Users/cobalt/cobalt/ops/desk/bare-guard.py` | 1 | 0 (= before) |
| P6 | `grep -c -F "def prod_word" /Users/cobalt/cobalt/ops/desk/bare-guard.py` | 1 | 0 (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main e9655b19 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · pid 69822 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · pid 69832 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-guard-d1-1009 merge --no-edit e9655b19` → `Merge made by the 'ort' strategy.` (3 files: `docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md`, `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`; 346 insertions, 2 deletions)
- `git -C /Users/cobalt/cobalt-wt/deploy-guard-d1-1009 rev-parse --short=8 HEAD` → `<m1>` = 18979f7f
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 96c3fa7e..deploy/guard-d1-1009` → `18979f7f Merge commit 'e9655b19' into deploy/guard-d1-1009` (one per head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor e9655b19 deploy/guard-d1-1009` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 96c3fa7e deploy/guard-d1-1009 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 96c3fa7e deploy/guard-d1-1009 -- configs ops` → ` ops/desk/bare-guard.py | 61 ++++++++++++++++++++++++++++++++++++++++++++++++--` / ` 1 file changed, 59 insertions(+), 2 deletions(-)` — no plist added, modified or removed.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-guard-d1-1009` · `ls -la …/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a fresh `.venv` build: `Installed 253 packages in 786ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (none). No UNCLASSIFIED row. No resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0` (not above 0) → the gate runs whole (`--deploy`).
- (a0) `ls -la …/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the 17 listed files) → `262 passed, 163 skipped in 16.26s` — 0 failed; every skip is a Postgres-env / `requires_db` skip.
- deselects: none (build report `guard-d1-build-2026-10-09.md`: `with-DB: not run (DB: none)`) · `--tickers`: none · `--migration`: none.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-guard-d1-1009 all --deploy` → exit 0, verdict lines whole:
```
offline 4045/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4932/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-guard-d1-1009-all-20261009-152925.log
```
- (a) offline `4045/0` → `<p>` = 4045.
- (c) pass 1 at `0013`, the seven SKIPPED lines all inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F … tests/cobalt/test_s3_c4_experiments.py` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, its decorator line 95). No migration in the set: the with-DB total is `4932/0` → `<d>` = 4932.
- (f) `cobalt_dev: 0013 — F2 = F0` (log `884:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`).
- THE RELEASE: `.env: removed` (gate line; the release time is not read from the log — see `## RECORDS`). `ls -la /Users/cobalt/cobalt-wt/deploy-guard-d1-1009/.env` → No such file; `grep -c -x -F "deploy-guard-d1-1009" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) live-note `146/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg → `<l>` = 146.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 18979f7f

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 83]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` lines under `docs/40 - DevDocs/` only, and `?? .claude/settings.json.bak` (see `## DECISIONS` 1); no staged line, no dirty `src/` `tests/` `ops/` `configs/` path |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 96c3fa7e main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-guard-d1-1009` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-guard-d1-1009` | 0 | `Deleted tag 'scratch-allow-probe-guard-d1-1009' (was 96c3fa7e)` |
| PROBE | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 51f399a1] scratch: allowlist probe (reverted next line)` |
| PROBE | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `96c3fa7e docs(desk): OWED item names its asking row R752` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-09-guard-d1` | 1 | free |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-guard-d1-1009` | 1 | free |

### STEP-D1 (baseline, read-only)
- `date` → `Fri Oct  9 15:57:55 EDT 2026`
- `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 15:57:56 EDT)`; `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200`; `OK   radar                    scanning (rth), members 50`; `OK   com.cobalt.aset              running   loaded, pid 69822 [launchd probe]`; `OK   com.cobalt.agent             running   pid 22243 alive …`; `OK   com.cobalt.radar             running   running 91 min, heartbeat fresh`; `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …` (declared interim, not RED). No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 → `<val0>`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`; ends `Placement (docs/PLACEMENT.md): tree clean.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.5 h old`
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = 69822 · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = 69832 · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last cycle `2026-10-09 15:55:35.034 | INFO | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791575646955`, then price-floor lines to 15:57:27; no traceback.
- LOG BASELINES: `<a0>` = 52 · `<ta0>` = 2 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 42 · `<lc0>` = 39
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`
- MARKERS: `PROD_OPTION` → 0 · `def prod_word` → 0 (both = before)
- MIGRATIONS: none → no `<RB>`, no D1-M.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-guard-d1-1009.md"` · `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy guard-d1-1009 — gate green on 18979f7f" …` → `[main c9edcf57] …`; `show --stat HEAD` → one file (`docs/40 - DevDocs/reports/deploy-guard-d1-1009.md | 144 +`). `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `<pre-merge>` = c9edcf57.
- D2.1 `git -C /Users/cobalt/cobalt-wt/deploy-guard-d1-1009 merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `rev-parse --short=8 HEAD` (gate) → `<stack-final>` = 65a3c209 · `git -C /Users/cobalt/cobalt rev-parse --short=8 65a3c209^2` → c9edcf57 (= `<pre-merge>`) · `merge-base --is-ancestor 18979f7f 65a3c209` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 18979f7f 65a3c209 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` → `newest snapshot: 1.6 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain dumped, 6560.1 MB` · `ssd: snapshot 84a6cac7 — 0 new / 3 changed, 132.0 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Fri Oct  9 15:59:45 EDT 2026` · `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 15:59:47 EDT)` — 111 s after D1's 15:57:56; no RED; aset pid 69822, radar `running 93 min, heartbeat fresh`. (A fill read at 15:59:41, also GREEN, preceded it.)
- D2.6 `date` → `Fri Oct  9 15:59:51 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-guard-d1-1009` at c9edcf57 → exit 0.

### STEP-4 (restart set EMPTY — no resident down)
- 4.1 `date` → `<t down>` = `Fri Oct  9 16:00:03 EDT 2026`
- 4.2 nothing (set empty): no bootout, no `cobalt.sh stop`.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → c9edcf57 (= `<pre-merge>`) · `git -C /Users/cobalt/cobalt merge --ff-only deploy/guard-d1-1009` → `Updating c9edcf57..65a3c209` / `Fast-forward` (`ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, `docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md`; 346 insertions, 2 deletions).
- 4.4 migrations applied: none.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 nothing to bootstrap (set empty). `<t up>` = 4.3's `date` = `Fri Oct  9 16:00:03 EDT 2026`. Downtime: none.

### STEP-7 summary
| item | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | c9edcf57 → 65a3c209 (main tip 65a3c209) |
| tags | `pre-guard-d1-1009` (at c9edcf57) · `deploy-2026-10-09-guard-d1` (at 65a3c209, after the green smoke) |
| `<t down>` / `<t up>` / seconds | none (restart set empty) |
| uv sync line | none in production calls (the gate worktree built its own `.venv`: `Installed 253 packages in 786ms`) |
| proof cost | none (no migration) |
| migrations applied | none |
| `<RB>` before / after | n/a (no migration) |
| snapshot id | `84a6cac7` (ssd) |
| RESTARTS done | none |

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 65a3c209` — ONE revert of the main-into-gate merge; restart set empty, so no resident goes down or up.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` (`Reapply "Merge branch 'main' into deploy/guard-d1-1009"`).

## Smoke
`<t up>` = Fri Oct  9 16:00:03 EDT 2026 (4.3's `date`; restart set empty).
- FIRST CALLS [16:00:16]: `<rp_up>` = 18 · `<rpr_up>` = 60 · `<re_up>` = 42 · `<lc_up>` = 39 (all = D1 baseline).
- (a) [16:00:20] `launchctl print gui/501/com.cobalt.aset` → `state = running`, pid 69822 (SAME as D1; outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, pid 69832 (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (SAME). GREEN.
- (b) [16:00:24] `grep -c "Started server process" …/aset.err` → 52 (= `<a0>`; aset outside the set) · `tail -n 30 …/aset.err` → last `INFO:     Started server process [69828]` … `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` (the 14:26 start, unchanged) · Traceback aset 2 (= `<ta0>`), radar 0 (= `<tr0>`), TaxonomyConfigError 0 (= `<tc0>`).
- (c) [16:00:28] `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) [16:00:28] `grep -c -F "PROD_OPTION" /Users/cobalt/cobalt/ops/desk/bare-guard.py` → `3` (= after) · `grep -c -F "def prod_word" /Users/cobalt/cobalt/ops/desk/bare-guard.py` → `1` (= after). GREEN.
- (s) the same two reads: `PROD_OPTION` → exit 0, `3` (≥1) · `def prod_word` → exit 0, `1` (≥1). GREEN.
- (f) [16:00:34] `COBALT_ENV=production uv run cobalt jobs restarts c9edcf57..65a3c209` → exit 0, `RESTARTS: none` (= STEP-R), no UNCLASSIFIED · `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` GREEN.
- (g) no migration.
- (e) read 1 [16:00:39] `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 16:00:40 EDT)`; `com.cobalt.radar running running 94 min, heartbeat fresh`; `radar scanning (aftermarket), members 50`.
- (e) read 2 [16:02:33] `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 16:02:34 EDT)` (114 s after read 1); `com.cobalt.radar running running 96 min, heartbeat fresh`. No RED not in `<hb0>`. GREEN. (Clock-fill heartbeat reads between 16:00:56 and 16:03:02 were all `HEARTBEAT GREEN … nothing red`.)
- (b) radar tails: tail 1 [16:01:38, `<t up>`+95 s] → last `radar cycle: scanning scan_id=1791575835064` at 15:58:42 (before `<t up>`), price-floor lines to 16:00:35, no failure, no traceback — not yet settled · tail 2 [16:03:06, `<t up>`+183 s] → `2026-10-09 16:01:50.862 | INFO | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791576022872` (after `<t up>`), no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → SETTLED GREEN; the third tail is not needed.
- (h) [16:03:09, `<t up>`+186 s] four counts 18 / 60 / 42 / 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `curl … /radar` → `200` · radar Traceback 0 · no `census` reads on this card. GREEN.

THE CHAIN: every check committed (P2: `5a98783d`, clean) → the tips (P3: e9655b19 = head) → the merged tree (T: 18979f7f, one merge, no migration) → RESTARTS derived (R: none) → three suites green on 18979f7f (G: 4045/0 · 4932/0 · 146/0) → `<stack-final>` 65a3c209 = 18979f7f + docs (D2.3) → landed code (4.3 fast-forward c9edcf57..65a3c209) → markers 3 / 1 (d) → no migration (g) → residents unchanged and up (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and verbatim output; (2) `git -C /Users/cobalt/cobalt merge-base --is-ancestor e9655b19 65a3c209` → exit 0 (code tip = head, re-read at P3); (3) REVERT-READBACK (h) shown; every count, sha and `file:line` here was read from tool output this run; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict marker.

## CONTINUE
- STEP-T done (m1 18979f7f); STEP-C done; STEP-R done (set: none).
- STEP-D0 (gate green at Fri Oct  9 15:57:25 EDT 2026) done; STEP-D1 done.
- STEP-D2 done.
- OUTAGE STARTING Fri Oct  9 15:59:51 EDT 2026 — residents of none going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- STEP-4 done (nothing down; merged 16:00:03); STEP-4.7 smoke GREEN; STEP-7 done.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main`; it is outside D0's ACCEPTED list but in none of its REFUSED classes (not staged, not under `src/` `tests/` `ops/` `configs/`), and it was present at session start. Safe default taken: not a stop; left untouched. [Fri Oct  9 15:57:55 EDT 2026]

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" /Users/cobalt/cobalt-wt/.gate-logs/deploy-guard-d1-1009-all-20261009-152925.log` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Not re-spelled; the release is proven by the gate's `.env: removed` line, `ls -la` (No such file) and the absent lock dir.
- `cobalt_dev: 0013 (F2 = F0)`.
- Downtime: none (restart set empty; no resident stopped).
- RETIRE OWED: none (no plist removed).
- Carried RED: none — `<hb0>` and every later heartbeat were `HEARTBEAT GREEN … nothing red`; `com.cobalt.herdr` AMBER is the declared `launchd_unmanaged` interim, not RED.
- Messages not followed: none received.
- L74: one line (see `## L74`).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-guard-d1-1009` and branch `deploy/guard-d1-1009`; the set's branch `ops/guard-d1-1009` and its worktree if any. The gate worktree holds an untracked `.venv` built by `uv run` at STEP-R.
- Push is his, through the desk (L55): `main` is at 65a3c209 plus this report's commit, unpushed; tags `pre-guard-d1-1009` and `deploy-2026-10-09-guard-d1` are local.
- Card's `## RECORDS`, copied:
  - guard-d1-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d1-check-2026-10-09.md` last line: CHECK DONE · job: guard-d1-1009 · pass: 1 · tip: e9655b19 · house A: Sol FINDINGS: 9 · findings: 15 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 4 · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 215804
  - guard-d1-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-d1-1009` → `e9655b19`; code tip `e9655b19`
  - written by deploy-card.sh at 2026-10-09 15:17 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-09-guard-d1 65a3c209 | set: none | migrations: none | gate: offline 4045/0 · with-DB 4932/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 192383
