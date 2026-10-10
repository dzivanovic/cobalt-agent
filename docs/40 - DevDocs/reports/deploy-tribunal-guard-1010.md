# deploy tribunal-guard-1010 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `tribunal-guard-1010` (`ops/tribunal-guard-1010`, code tip `2e680273`): the bare-guard tribunal-hub house call (marker `G9 (R877)`) is live in `ops/desk/bare-guard.py` on `main` at `230b2463`.
- Gate GREEN on `2146f1ad`: offline 4196/0 · with-DB 5093/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`; lock released.
- RESTARTS: none: no resident went down, there was no downtime, and aset / radar / agent pids are unchanged. Smoke GREEN, marker 0 → 1.
- Rollback tag `pre-tribunal-guard-1010` at `3291ef83`; snapshot `2b99b966`. Push is his (L55).

## L74
- A system reminder in this session asked that commit messages also carry a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/255-deploy-tribunal-guard-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/255-deploy-tribunal-guard-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/255-deploy-tribunal-guard-card.md" · 0 · a9883590381db4c3aadb5bc7f6cba960a41129f9
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/255-deploy-tribunal-guard-card.md" · 0 · nothing
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
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sat Oct 10 10:50:26 EDT 2026` |
| P2 check | `tail -n 3 ".../tribunal-guard-check-2026-10-10.md"` | 0 | `CHECK DONE · job: tribunal-guard-1010 · pass: 1 · tip: 2e680273 · house A: Sol FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 0 · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 168237` — carries `held unfixed: 0`, `ready: YES`, `tip: 2e680273` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/tribunal-guard-check-2026-10-10.md"` | 0 | `63ad3142c191ea3d9ec3a03f53084f8031455d3a` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 2e680273` | 0 | `2e680273` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/tribunal-guard-1010` | 0 | `8a7a938f` (= `TIP`) |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 2e680273 8a7a938f` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 2e680273 8a7a938f -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-tribunal-guard-1010 status --short --branch` | 0 | `## deploy/tribunal-guard-1010` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `7dd569c0` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 7dd569c0 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/tribunal-guard-1010` | 0 | empty |
| P6 marker | `grep -c -F "G9 (R877)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 8a7a938f -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 66658` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-tribunal-guard-1010 merge --no-edit 8a7a938f` → `Merge made by the 'ort' strategy.` (`ops/desk/bare-guard.py | 12 +-`, `tests/ops/test_bare_guard.py | 62 +`, `docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md | 146 +`; 3 files changed, 216 insertions(+), 4 deletions(-))
- `git -C <GATE> rev-parse --short=8 HEAD` → `2146f1ad` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 7dd569c0..deploy/tribunal-guard-1010` → `2146f1ad Merge commit '8a7a938f' into deploy/tribunal-guard-1010` (one line, one head)
- `merge-base --is-ancestor 2e680273 deploy/tribunal-guard-1010` → exit 0 · `merge-base --is-ancestor 8a7a938f deploy/tribunal-guard-1010` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 7dd569c0 deploy/tribunal-guard-1010 -- src/cobalt/db_migrations` → nothing (no migration path; MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 7dd569c0 deploy/tribunal-guard-1010 -- configs ops` → ` ops/desk/bare-guard.py | 12 ++++++++----` / ` 1 file changed, 8 insertions(+), 4 deletions(-)`. No plist added, modified or removed.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-tribunal-guard-1010` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14` · `Creating virtual environment at: .venv` · `Installed 253 packages in 890ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>` = EMPTY (none). No `UNCLASSIFIED` row. No resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold (the check's stop line carries `with-DB 0/0`) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.96s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- No with-DB `--deselect` named by the set's build report (its one `deselected` line is a `-k` RED-first run on `BASE`). TICKERS: none → no `--tickers`. MIGRATIONS: none → no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-tribunal-guard-1010 all --deploy` (background) → exit 0. Verdict lines whole:
```
offline 4196/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-tribunal-guard-1010-all-20261010-105218.log
```
- (c) SKIPPED lines, each inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95`, the skip decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture():` at line 96 (Grep of the gate tree's file). (e) no skip naming `COBALT_LIVE_VAULT_ROOT` in live-note (live-note runs after the list above; `live-note 146/0`).
- (c2) log line 1110: `dev forward: APPLIED 11:16:34`. (f) log 896 `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · log 2030 `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0` (log 2082).
- THE RELEASE: log 2083–2088 `$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-tribunal-guard-1010` → `lock released` → `.env: removed` (L76 lock released; the log stamps no clock on that line; between 11:16:34 and the gate's end, before 11:21:39). `ls -la <GATE>/.env` → No such file · `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 2146f1ad — offline 4196/0 · with-DB 5093/0 · live-note 146/0

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 195]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`; ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (outside `src/ tests/ ops/ configs/`; recorded) |
| main since cut | `git -C /Users/cobalt/cobalt diff --stat 7dd569c0 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-tribunal-guard-1010` | 0 | — |
| probe tag -d | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-tribunal-guard-1010` | 0 | `Deleted tag 'scratch-allow-probe-tribunal-guard-1010' (was 7dd569c0)` |
| probe commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 7c7d60c6] scratch: allowlist probe (reverted next line)` |
| probe reset | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | — |
| HEAD back | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `7dd569c0 docs(desk): R890 launcher built b71837f2, all builds done` |
| TAG free | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-10-tribunal-guard` | 1 | — |
| pre-tag free | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-tribunal-guard-1010` | 1 | — |

### STEP-D1 (baseline)
- `date` → `Sat Oct 10 11:22:13 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 11:22:14 EDT)`. Every aset / sheet / radar probe OK: `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200` · `OK   sheet daymode …` · `OK   radar                    idle (overnight)` · `OK   com.cobalt.aset              running   loaded, pid 66658 [launchd probe]` · `OK   com.cobalt.agent             running   pid 22243 alive …` · `OK   com.cobalt.radar             running   running 233 min, heartbeat fresh`. REDs NAMED, not a stop (not aset / sheet / radar): `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC (14.5 h ago), rows written 3308843, exit 1` · `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'`. AMB: `com.cobalt.herdr unmanaged` (declared interim).
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`: `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`); `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 3.9 h old` (ssd local ARMED; b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 66658` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, 11:09:43 → `2026-10-10 11:21:23.657 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`; no traceback.
- LOG BASELINES: `<a0>` Started server process = `182` · `<ta0>` aset Traceback = `123` · `<tr0>` radar Traceback = `0` · `<tc0>` TaxonomyConfigError = `0` · `<rp0>` radar panel FAILED = `18` · `<rpr0>` radar pool refresh FAILED = `60` · `<re0>` radar S5 evaluate FAILED = `43` · `<lc0>` lifecycle card read failed = `39`.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`. MARKER `grep -c -F "G9 (R877)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` → `0` (= before).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-tribunal-guard-1010.md"` · `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy tribunal-guard-1010 — gate green on 2146f1ad" …` → `[main 3291ef83] docs(report): deploy tribunal-guard-1010 — gate green on 2146f1ad` · `show --stat HEAD` → one file, `.../reports/deploy-tribunal-guard-1010.md | 137 +++` · `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `3291ef83` = `<pre-merge>`.
- D2.1 `git -C /Users/cobalt/cobalt-wt/deploy-tribunal-guard-1010 merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report, 137 +).
- D2.2 `rev-parse --short=8 HEAD` → `230b2463` = `<stack-final>` · `rev-parse --short=8 230b2463^2` → `3291ef83` (= `<pre-merge>`) · `merge-base --is-ancestor 2146f1ad 230b2463` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 2146f1ad 230b2463 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 3.9 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6694.1 MB` · `ssd: snapshot 2b99b966 — 0 new / 3 changed, 27.2 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Sat Oct 10 11:24:20 EDT 2026` · `heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 11:24:21 EDT)` (127 s after D1's 11:22:14); the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver` 429, `com.cobalt.replay`); aset / sheet / radar probes OK (`com.cobalt.radar running 235 min, heartbeat fresh`). No new RED.
- D2.6 `date` → `Sat Oct 10 11:24:26 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-tribunal-guard-1010` → exit 0, at `3291ef83`.

### STEP-4 (empty `<restart set>`)
- 4.1 `date` → `Sat Oct 10 11:24:38 EDT 2026` = `<t down>` (nothing went down).
- 4.2 no label in the set: no bootout, no `cobalt.sh stop`.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `3291ef83` (= `<pre-merge>`) · `git -C /Users/cobalt/cobalt merge --ff-only deploy/tribunal-guard-1010` → `Updating 3291ef83..230b2463` / `Fast-forward` (`tribunal-guard-build-2026-10-10.md | 146 +`, `ops/desk/bare-guard.py | 12 +-`, `tests/ops/test_bare_guard.py | 62 +`; 3 files changed, 216 insertions(+), 4 deletions(-)).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 no label taken down: no bootstrap. `date` → `Sat Oct 10 11:24:45 EDT 2026` = `<t up>`. Downtime: none.

### STEP-7 summary
| field | value |
|---|---|
| merge | `<pre-merge>` `3291ef83` → `<stack-final>` `230b2463` (fast-forward) |
| tags | `pre-tribunal-guard-1010` at `3291ef83`; `deploy-2026-10-10-tribunal-guard` at `230b2463` (`git -C /Users/cobalt/cobalt tag deploy-2026-10-10-tribunal-guard` exit 0, 11:28:00 after green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty set; merge between 11:24:38 and 11:24:45) |
| uv sync line | none in production (the gate tree's `.venv` was created at STEP-R: `Installed 253 packages in 890ms`) |
| proof cost | none (MIGRATIONS: none) |
| migrations applied | none |
| `<RB>` before / after | none |
| snapshot | `2b99b966` (ssd; `0 new / 3 changed, 27.2 MB added, 1 pruned`; dump 6694.1 MB) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 230b2463` (no resident to take down: RESTARTS none). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
- FIRST CALLS after `<t up>` 11:24:45: `<rp_up>` radar panel FAILED = `18` · `<rpr_up>` radar pool refresh FAILED = `60` · `<re_up>` radar S5 evaluate FAILED = `43` · `<lc_up>` lifecycle card read failed = `39` (each = D1's).
- (a) `date` → `Sat Oct 10 11:24:59 EDT 2026` · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 66658` (SAME, outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is ONLINE (PID: 22243).` (SAME). GREEN.
- (b) `grep -c "Started server process" …/aset.err` → `182` (= `<a0>`, aset outside the set) · aset Traceback `123` (= `<ta0>`) · radar Traceback `0` (= `<tr0>`) · TaxonomyConfigError `0` (= `<tc0>`) · `tail -n 30 /Users/cobalt/cobalt/logs/aset.err` → ends `INFO:     Started server process [66667]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` (the 07:51 start; the `ScratchLocked` traceback above it is of 07:51, before this deploy, inside `<ta0>`).
- (c) `date` → `Sat Oct 10 11:25:06 EDT 2026` · `curl … https://cobalt.taild24291.ts.net/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKER `grep -c -F "G9 (R877)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` → `1` (= after). GREEN.
- (f) `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `COBALT_ENV=production uv run cobalt jobs restarts 3291ef83..230b2463` → exit 0, `RESTARTS: none` (= STEP-R's), no `UNCLASSIFIED`. GREEN.
- (g) MIGRATIONS: none → no `<RB>`.
- (s) THE SET'S SMOKE READS: the guard's tribunal-hub marker · `grep -c -F "G9 (R877)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` → exit 0, `1` (green: a count of 1 or more). GREEN. The guard's tests ran in the gate (offline 4196/0 includes `tests/ops/test_bare_guard.py`).
- (e) heartbeat 1: `date` → `Sat Oct 10 11:25:23 EDT 2026` · `heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 11:25:23 EDT)`; the same three REDs as `<hb0>`; `OK   com.cobalt.radar             running   running 236 min, heartbeat fresh`. Heartbeat 2: `date` 11:27:12 → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 11:27:15 EDT)` (112 s after heartbeat 1); the same three REDs (archiver probe, `com.cobalt.archiver` 429, `com.cobalt.replay`), no new RED; `OK   com.cobalt.radar             running   running 238 min, heartbeat fresh`. GREEN.
- (b) RADAR TAILS: tail 1 `date` 11:26:16 (`<t up>` + 91 s) → newest `2026-10-10 11:24:43.702 … radar cycle: idle:overnight scan_id=None` (before `<t up>`; not yet settled) · tail 2 `date` 11:27:45 (`<t up>` + 180 s) → newest `2026-10-10 11:26:23.722 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, stamped after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → SETTLED GREEN (no third tail needed).
- (h) REVERT-READBACK at `<t up>` + 180 s or later (after tail 2, 11:27:45+): radar panel FAILED `18` · pool refresh FAILED `60` · S5 evaluate FAILED `43` · lifecycle card read failed `39` (each = `<…_up>`; nothing grew) · `curl … /radar` → `200`. No census (no migration). GREEN.

THE CHAIN: every check committed (P2: `63ad3142`) → the tips re-read (P3: `2e680273`, `8a7a938f`) → the merged tree (T: `2146f1ad`, one merge, no conflict) → RESTARTS derived (R: none) → three suites green on `2146f1ad` (G: offline 4196/0 · with-DB 5093/0 · live-note 146/0) → `<stack-final>` `230b2463` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Updating 3291ef83..230b2463`, `main` HEAD `230b2463`) → marker (d) `1` → no migration (g) → residents up and unchanged after the merge (a) → radar cycling (b, e) → the set's read (s) `1` → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK (K25): (1) every smoke row above carries its `date` and quoted output; (2) `merge-base --is-ancestor 2e680273 230b2463` → exit 0, `merge-base --is-ancestor 8a7a938f 230b2463` → exit 0, both re-read at P3; (3) REVERT-READBACK shown at (h); every count, sha and `file:line` here was re-read from this run's tool output; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), D2.1 clean, no conflict marker can exist.

## CONTINUE
STEP-D0 (gate green at 11:21:39) done · D1 done.
STEP-D2 done.
OUTAGE STARTING 11:24:26 — residents of <restart set> = none going down (empty set: no resident goes down; the merge lands with the residents up); if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
STEP-4 done 11:24:45 (merge landed, nothing down) · STEP-4.7 smoke GREEN 11:27:45+ · STEP-7 closed 11:28:00. Nothing next for this session.

## DECISIONS
none

## RECORDS
- Downtime: none (RESTARTS: none; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`; L76 lock released by `gate.sh` (`lock released`, `.env: removed`).
- RETIRE OWED: none (no plist removed).
- The carried RED as read (not of the radar family; named, not a stop): `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (14.5 h ago), rows written 3308843, exit 1` · `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`; unchanged from D1 through smoke (e).
- `com.cobalt.aset` launchd reads `runs = 120`, `last exit code = 3` at P8, D1 and smoke (a), the same before and after; the aset.err tail shows a 07:51 `ScratchLocked` startup failure followed by a clean start `[66667]` (pid 66658 today). It predates this deploy; recorded for the desk, not acted on (see `aset-orphan-check-2026-10-10.md`, already on the desk).
- `?? .claude/settings.json.bak` on `main` at D0: untracked, outside `docs/40 - DevDocs/` and outside `src/ tests/ ops/ configs/`; not refused, recorded.
- An added read at smoke (f), `grep -c -F "13 trade_def(s) validated OK from the vault." /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-tribunal-guard-1010.md` (path unquoted), exited 2 (`grep: /Users/cobalt/cobalt/docs/40: No such file or directory`). Not needed, nothing touched; (f)'s validate ran on its own call.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-tribunal-guard-1010` and branch `deploy/tribunal-guard-1010`; the set's branch `ops/tribunal-guard-1010` and its worktree, if any. The desk's.
- Card `## RECORDS`, copied:
  - tribunal-guard-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/tribunal-guard-check-2026-10-10.md` last line: CHECK DONE · job: tribunal-guard-1010 · pass: 1 · tip: 2e680273 · house A: Sol FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 0 · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 168237
  - tribunal-guard-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/tribunal-guard-1010` → `8a7a938f`; code tip `2e680273`
  - written by deploy-card.sh at 2026-10-10 09:31 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one system reminder asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on.
- No `CONTINUE` message and no message from another session arrived.
- An added clock-fill read while the gate ran, `COBALT_ENV=production uv run cobalt heartbeat show` at 10:52:27 from the cwd `<GATE>` (no `.env` there), exited 1: `FAILED: DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. …`. Not needed; a wrong-cwd read, nothing touched. D1's heartbeat runs from `/Users/cobalt/cobalt`.

DEPLOYED deploy-2026-10-10-tribunal-guard 230b2463 | set: none | migrations: none | gate: offline 4196/0 · with-DB 5093/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 194445
