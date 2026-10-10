# deploy x29-fixture-1010 · SET: none · MIGRATIONS: none

## §0 Headline
- Card `docs/40 - DevDocs/prompts/2026-10-10/285-deploy-x29-card.md` · ships `ops/x29-fixture-1010` at `3c00e204` (tests only: the conftest-guard test).
- Status: in progress.

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

## Smoke

## CONTINUE
next: STEP-D2 (D0 and D1 done, 16:08)

## DECISIONS
1. ASK DESK: D0's porcelain shows `?? .claude/settings.json.bak`. That path is not on the ACCEPTED list (only ` M .claude/settings.json` is) and not on the REFUSED list (dirty `src/`, `tests/`, `ops/` or `configs/`). Is an untracked `.claude/` backup a refusal? [16:08] Safe default taken: not a refusal. The file is untracked, the `--ff-only` merge does not touch it, and it is outside the code paths the rule guards. The deploy goes on.

## RECORDS

(run in progress — next step under ## CONTINUE)
