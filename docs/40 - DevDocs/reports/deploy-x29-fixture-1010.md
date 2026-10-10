# deploy x29-fixture-1010 · SET: none · MIGRATIONS: none

## §0 Headline
- Card `docs/40 - DevDocs/prompts/2026-10-10/285-deploy-x29-card.md` · ships `ops/x29-fixture-1010` at `3c00e204` (tests only: the conftest-guard test).
- DEPLOYED `deploy-2026-10-10-x29-fixture`: main `3e8f954b` → `df17d8fe`, fast-forward, at 16:10:37. Tests only: the conftest-guard test, plus one line in each of four experiment conftests.
- Gate green on `aae14d6a`: offline 4199/0 · with-DB 5096/0 · live-note 146/0. RESTARTS: none, so no resident went down. MIGRATIONS: none.
- Smoke GREEN. Production carries the same three archiver/replay REDs it carried before (Finviz 429). They are not from this deploy.
- One ASK DESK (an untracked `.claude/settings.json.bak` on main); safe default taken. Not for Dejan.

## L74
- A harness system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded once as data, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/285-deploy-x29-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/285-deploy-x29-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/285-deploy-x29-card.md" · 0 · 759b12e9f8e9a4d657f81f4b74a81be09b7605fe
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/285-deploy-x29-card.md" · 0 · nothing
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
| FIRST LAUNCH | `ls -la ".../reports/deploy-x29-fixture-1010.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sat Oct 10 15:18:48 EDT 2026` |
| P2 check line | `tail -n 3 ".../reports/x29-fixture-check-2026-10-10.md"` | 0 | `CHECK DONE · job: x29-fixture-1010 · pass: 1 · tip: 3c00e204 · … · held unfixed: 0 · open: 0 · … · suites: offline 4199/0 · with-DB 5096/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 167561` — carries `held unfixed: 0` and `ready: YES`; `tip: 3c00e204` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/x29-fixture-check-2026-10-10.md"` | 0 | `2045d8b3e6798e845d8e819784b04a573a06461d` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/x29-fixture-check-2026-10-10.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 3c00e204` | 0 | `3c00e204` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x29-fixture-1010` | 0 | `3c00e204` (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3c00e204 ops/x29-fixture-1010` | 0 | — |
| P3 docs-only | `git -C /Users/cobalt/cobalt diff --stat 3c00e204 ops/x29-fixture-1010 -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` (nobody holds it) |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/x29-fixture-1010` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `759b12e9` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 759b12e9 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/x29-fixture-1010` | 0 | EMPTY |
| P6 MARKER | `ls /Users/cobalt/cobalt/tests/cobalt/test_experiment_conftests.py` | 1 | `No such file or directory` (= before) |
| P7 MIGRATIONS | `git -C /Users/cobalt/cobalt diff --stat main 3c00e204 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 3c00e204` → `Merge made by the 'ort' strategy.` (6 files, 244 insertions: the build report, `tests/cobalt/test_experiment_conftests.py` created, four `tests/experiments/*/conftest.py` +1 line each).
- `git -C <GATE> rev-parse --short=8 HEAD` → `aae14d6a` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 759b12e9..deploy/x29-fixture-1010` → `aae14d6a Merge commit '3c00e204' into deploy/x29-fixture-1010` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3c00e204 deploy/x29-fixture-1010` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 759b12e9 deploy/x29-fixture-1010 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 759b12e9 deploy/x29-fixture-1010 -- configs ops` → nothing. No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv first created the gate's `.venv`: `Installed 253 packages in 810ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/x29-fixture-build-2026-10-10.md	A	DOCS	-
tests/cobalt/test_experiment_conftests.py	A	test/documentation; no resident	-
tests/experiments/f15_p1/conftest.py	M	test/documentation; no resident	-
tests/experiments/handicap_h1/conftest.py	M	test/documentation; no resident	-
tests/experiments/setups_one/conftest.py	M	test/documentation; no resident	-
tests/experiments/stale_score/conftest.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (none). No `UNCLASSIFIED` row. MIGRATIONS none, so an empty set is consistent. No resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 3c00e204 aae14d6a -- . ":(exclude)docs"` → 4 files (`ops/desk/bare-guard.py`, `ops/desk/orphan-clean.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_orphan_clean.py`: `main` moved since the check tip). The clause does not hold, so the gate runs whole (`--deploy`).
- Deselects: none (the build report, line 114: "no `--deselect`: no with-DB test added"). TICKERS none. No `--migration`.
- (a0) THE EARLY READ: `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.90s`: 0 failed (the with-DB tests skip offline, `Postgres env settings not available` / `requires_db`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-x29-fixture-1010 all --deploy` started in the background, exit 0. Verdict lines whole:
```
offline 4199/0
lock: waited 18 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5096/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-x29-fixture-1010-all-20261010-152029.log
```
- (a) offline `4199/0`. (c)+(c3) with-DB `5096/0`. (e) live-note `146/0`.
- Skips: all seven are in the allowed set. `test_s3_c4_experiments.py:95` is the `@requires_live` decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (Grep: line 95 `@requires_live`, line 96 the def). The `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`.
- (c2) `dev forward: APPLIED 16:02:59` (log line 1110). No migration above `0013` on this card.
- (f) log `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 896) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 2030) → `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log line 2083–2088 `release-devdb-lock.sh deploy-x29-fixture-1010` → `lock released`, `.env: removed` (L76 lock released before 16:08:04, the gate's end; the log line carries no clock). `ls -la <GATE>/.env` → No such file · `grep -c -x -F "deploy-x29-fixture-1010" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on aae14d6a

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 274]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M`/`??` under `docs/40 - DevDocs/` only, plus ` M .claude/settings.json` and `?? .claude/settings.json.bak` (see `## DECISIONS` 1); no dirty `src/`, `tests/`, `ops/` or `configs/` path |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 759b12e9 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `tag scratch-allow-probe-x29-fixture-1010` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-x29-fixture-1010' (was 759b12e9)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 3cca2eae] scratch: …` → `759b12e9 docs(desk): X29 deploy card 285 markers and smoke reads` (HEAD back) |
| TAG free | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-x29-fixture` | 1 | — |
| rollback tag free | `rev-parse --verify --quiet refs/tags/pre-x29-fixture-1010` | 1 | — |

### STEP-D1 (baseline, read-only)
- `date` → `Sat Oct 10 16:08:29 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 16:08:30 EDT)`. RED lines: `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (19.2 h ago), rows written 3308843, exit 1` · `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'` (traceback in the job record). Neither is the aset, sheet or radar probe, so they are named and do not stop the run. `OK sheet HTTP … -> 200` · `OK sheet daymode` · `OK radar idle (overnight)` · `OK com.cobalt.aset running loaded, pid 7760` · `OK com.cobalt.radar running running 519 min, heartbeat fresh` · `OK com.cobalt.agent running pid 22243 alive` · `AMB com.cobalt.herdr unmanaged` (declared interim).
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>` ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.4 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, the last `2026-10-10 16:08:07.678`; no traceback.
- LOG BASELINES: `<a0>` = 277 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKER `ls /Users/cobalt/cobalt/tests/cobalt/test_experiment_conftests.py` → exit 1 (before).
- MIGRATIONS none: no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `add` + `commit -m "docs(report): deploy x29-fixture-1010 — gate green on aae14d6a"` → `[main 3e8f954b] … 1 file changed, 139 insertions(+)`; `show --stat HEAD` lists the one report file. `rev-parse --short=8 main` → `3e8f954b` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `rev-parse --short=8 HEAD` → `df17d8fe` = `<stack-final>`; `rev-parse --short=8 df17d8fe^2` → `3e8f954b` = `<pre-merge>`; `merge-base --is-ancestor aae14d6a df17d8fe` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat aae14d6a df17d8fe -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 1.4 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6693.8 MB` · `ssd: snapshot 8b428f2b — 0 new / 2 changed, 26.9 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `16:10:20` · `heartbeat show` at `16:10:22` (112 s after D1's `16:08:30`): the same three REDs as `<hb0>` (archiver, com.cobalt.archiver 429, com.cobalt.replay), nothing new. aset `pid 7760`, radar `running 521 min, heartbeat fresh`.
- D2.6 `date` → `Sat Oct 10 16:10:26 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-x29-fixture-1010` (at `3e8f954b`) → exit 0.

### STEP-4 (restart set EMPTY)
- 4.1 `date` → `Sat Oct 10 16:10:37 EDT 2026` = `<t down>` (no resident went down).
- 4.2 nothing to boot out; the agent was not stopped.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `3e8f954b` = `<pre-merge>` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/x29-fixture-1010` → `Updating 3e8f954b..df17d8fe` / `Fast-forward` (6 files, 244 insertions: the build report, `tests/cobalt/test_experiment_conftests.py`, four `tests/experiments/*/conftest.py`).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`.
- 4.6 nothing to bootstrap. `<t up>` = `16:10:37` (the empty set's rule: 4.3's time; the `date` call was 4.1's, made just before 4.3). Downtime: none.

### CLOSE
| field | value |
|---|---|
| main | `3e8f954b` (`<pre-merge>`) → `df17d8fe` (`<stack-final>`); `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `df17d8fe` |
| tags | `pre-x29-fixture-1010` at `3e8f954b` · `deploy-2026-10-10-x29-fixture` at `df17d8fe` (set after the green smoke) |
| `<t down>` / `<t up>` / seconds | none (restart set empty; no resident went down) |
| uv sync | none in production; the gate's `.venv` was created at STEP-R (`Installed 253 packages in 810ms`) |
| proof cost | none in production (no migration) |
| migrations applied | none |
| `<RB>` before / after | n/a (MIGRATIONS: none) |
| snapshot | `ssd: snapshot 8b428f2b` (D2.4) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 df17d8fe` (no resident to take down: the restart set is empty) · 2. SCHEMA: none · 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
- FIRST CALLS after `<t up>` 16:10:37: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
- (a) `date` 16:10:53 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` (SAME as D1: outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (same pid; one line). GREEN.
- (b) `date` 16:10:57 · `grep -c "Started server process" …/aset.err` → `277` = `<a0>` (aset outside the set) · `grep -c "Traceback" …/aset.err` → `217` = `<ta0>` · `grep -c "Traceback" …/radar.err` → `0` = `<tr0>` · `grep -c "TaxonomyConfigError" …/radar.err` → `0` = `<tc0>`. The `tail -n 30 …/aset.err` shows a `ScratchLocked` traceback followed by `2026-10-10 13:23:12 … Started server process [7771]` … `Uvicorn running on http://127.0.0.1:5010`. That traceback predates this run: the count is unchanged.
- (c) `date` 16:11:02 · `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200`. GREEN.
- (d) MARKER `ls /Users/cobalt/cobalt/tests/cobalt/test_experiment_conftests.py` → `/Users/cobalt/cobalt/tests/cobalt/test_experiment_conftests.py`, exit 0 (= after). GREEN.
- (s) SMOKE READ "the new test file exists on main": the same `ls` → exit 0. GREEN. The test itself ran in the gate (offline `4199/0`).
- (f) `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · `COBALT_ENV=production uv run cobalt jobs restarts 3e8f954b..df17d8fe` → exit 0, `RESTARTS: none` (= STEP-R), no `UNCLASSIFIED`. GREEN.
- (g) no migration.
- (e) heartbeat 1: `date` 16:11:12 · `heartbeat show` at `16:11:13` → the same three REDs as `<hb0>` (archiver, com.cobalt.archiver 429, com.cobalt.replay), nothing new; `com.cobalt.radar running running 522 min, heartbeat fresh`. Heartbeat 2: `date` 16:13:02 · `heartbeat show` at `16:13:04` (111 s later) → the same three REDs, nothing new; `com.cobalt.radar running running 523 min, heartbeat fresh`; aset `pid 7760`. GREEN.
- (b) radar tails: `date` 16:12:07 (`<t up>` + 90 s) · `tail -n 12 …/radar.err` → last line `2026-10-10 16:11:27.724 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, a cycle after `<t up>`. No `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback. That settles it GREEN. A second tail at `16:13:37` (+180 s) → `2026-10-10 16:13:07.754 … radar cycle: idle:overnight scan_id=None`.
- (h) REVERT-READBACK: `date` 16:13:37 (`<t up>` + 180 s) · `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39: each equals `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none grew · `curl … /radar` → `200`. No census reads (no migration). GREEN.
- THE CHAIN: every check committed (P2: `2045d8b3`, clean) → the tips re-read (P3: `3c00e204` = head = TIP) → the merged tree (T: `aae14d6a`, one merge, no migration path) → RESTARTS derived (R: none, no UNCLASSIFIED) → three suites green on `aae14d6a` (G: offline 4199/0 · with-DB 5096/0 · live-note 146/0) → `<stack-final>` `df17d8fe` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Updating 3e8f954b..df17d8fe` fast-forward) → marker after (d) → no migration (g n/a) → residents up, unchanged pids (a) → radar cycling (b, e) → the set's read (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).
- SMOKE: GREEN.

### PRE-STOP SELF-CHECK (K25)
1. Every smoke row is quoted above with its `date` (16:10:53, 16:10:57, 16:11:02, 16:11:12, 16:12:07, 16:13:02, 16:13:37).
2. Tip `3c00e204` re-read at P3; `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3c00e204 df17d8fe` → exit 0; `rev-parse --short=8 main` → `df17d8fe`.
3. REVERT-READBACK (h) shown: the four counts 18/60/43/39 re-read at 16:13:37. Every count, sha and `file:line` in this report comes from tool output in this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.` and D2.1 the same; `git -C <GATE> status --short --branch` → `## deploy/x29-fixture-1010` (clean).

## CONTINUE
next: STEP-D2 (D0 and D1 done, 16:08)
OUTAGE STARTING 16:10:26 — residents of none (the restart set is empty) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
Merge landed 16:10:37 and smoke was GREEN at 16:13:37. The tag is set; the run is closed. Nothing is next for this session.

## DECISIONS
1. ASK DESK: D0's porcelain shows `?? .claude/settings.json.bak`. That path is not on the ACCEPTED list (only ` M .claude/settings.json` is) and not on the REFUSED list (dirty `src/`, `tests/`, `ops/` or `configs/`). Is an untracked `.claude/` backup a refusal? [16:08] Safe default taken: not a refusal. The file is untracked, the `--ff-only` merge does not touch it, and it is outside the code paths the rule guards. The deploy goes on.

## RECORDS
- Downtime: none (restart set empty; no resident went down).
- `REFUSED, not needed`: none. Messages not followed: none (no `CONTINUE` arrived).
- `cobalt_dev: 0013 (F2 = F0)`: F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87` (gate log lines 896, 2030). L76 lock released by the gate; no `.env` and no lock dir remained.
- RETIRE OWED: none (STEP-C: no plist touched).
- Carried RED as read (not of this deploy, not a stop): `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC …` · `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2 … Finviz … '429 Too Many Requests'` · `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. The same three at D1, D2.5 and smoke (e). The radar probe was OK throughout (`idle (overnight)`).
- Pre-existing in `logs/aset.err`: a `cobalt.voice.scratch.ScratchLocked` traceback before the 13:23:12 aset start (pid 7771 then; launchd pid now 7760). It predates this run, and the Traceback count did not move (217).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-x29-fixture-1010` with its `.venv`, branch `deploy/x29-fixture-1010`, and the set's branch `ops/x29-fixture-1010` (and its worktree, if the build left one).
- The card's `## RECORDS`, copied:
  - x29-fixture-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x29-fixture-check-2026-10-10.md` last line: CHECK DONE · job: x29-fixture-1010 · pass: 1 · tip: 3c00e204 · house A: Sol FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 0 · suites: offline 4199/0 · with-DB 5096/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 167561
  - x29-fixture-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x29-fixture-1010` → `3c00e204`; code tip `3c00e204`
  - written by deploy-card.sh at 2026-10-10 15:17 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one harness reminder asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on.
- The gate waited 18 min for the `cobalt_dev` lock (`lock: waited 18 min`).

DEPLOYED deploy-2026-10-10-x29-fixture df17d8fe | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 198551
