# deploy launcher-1010 — set: none — migrations: none

## §0 Headline
(in progress)

## L74
none

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/286-deploy-launcher-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/286-deploy-launcher-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/286-deploy-launcher-card.md" · 0 · 3c41aba9311afa1111071ea0af4a24862e0914eb
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/286-deploy-launcher-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | INSTALLED / card / proofs | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Sat Oct 10 16:15:51 EDT 2026` |
| P2 check line | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-check-2026-10-10.md"` | 0 | `CHECK DONE · job: launcher-1010 · pass: 1 · tip: 9e624360 · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 149022` — carries `held unfixed: 0`, `ready: YES`, `tip: 9e624360` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/launcher-check-2026-10-10.md"` | 0 | `0891e0839400e2c80abacc648f6eb72f00c6d937` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/launcher-check-2026-10-10.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 9e624360` | 0 | `9e624360` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-1010` | 0 | `9e624360` (= row, = `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9e624360 ops/launcher-1010` | 0 | — |
| P3 docs-only | `git -C /Users/cobalt/cobalt diff --stat 9e624360 ops/launcher-1010 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-launcher-1010 status --short --branch` | 0 | `## deploy/launcher-1010` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-launcher-1010 rev-parse --short=8 HEAD` | 0 | `3c41aba9` = `<m0>` |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3c41aba9 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/launcher-1010` | 0 | empty |
| P6 marker | `grep -F -e "--fix-report" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` | 1 | no match (= before); `grep -c -F -e "--fix-report" …` → `0` |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 9e624360 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-launcher-1010 merge --no-edit 9e624360` → `Merge made by the 'ort' strategy.` (3 files: `docs/40 - DevDocs/reports/launcher-build-2026-10-10.md` +178, `ops/desk/deploy-card.sh` 70 ±, `tests/ops/test_deploy_card.py` +169).
- `git -C /Users/cobalt/cobalt-wt/deploy-launcher-1010 rev-parse --short=8 HEAD` → `edcb1519` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 3c41aba9..deploy/launcher-1010` → `edcb1519 Merge commit '9e624360' into deploy/launcher-1010`.
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9e624360 deploy/launcher-1010` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 3c41aba9 deploy/launcher-1010 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C `git -C /Users/cobalt/cobalt diff --stat 3c41aba9 deploy/launcher-1010 -- configs ops` → WHOLE: ` ops/desk/deploy-card.sh | 70 +++++++++++++++++++++++++++++++++++++++++++++----` / ` 1 file changed, 65 insertions(+), 5 deletions(-)`. No plist added, modified or removed.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-launcher-1010` · `ls -la …/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, table WHOLE (after uv venv creation lines `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Installed 253 packages in 797ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/launcher-build-2026-10-10.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (none). No `UNCLASSIFIED`. No resident goes down.

## L68 GATE
- EQUAL-TREE CLAUSE: does NOT hold — `git -C /Users/cobalt/cobalt diff --stat 9e624360 edcb1519 -- . ":(exclude)docs"` prints 9 files (`ops/desk/bare-guard.py`, `ops/desk/orphan-clean.sh`, `tests/cobalt/test_experiment_conftests.py`, four `tests/experiments/*/conftest.py`, `tests/ops/test_bare_guard.py`, `tests/ops/test_orphan_clean.py`; 1054 insertions, 4 deletions — `main` moved since the check). The gate runs whole.
- (a0) `ls -la …/.env` (No such file) · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.60s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: the build report `launcher-build-2026-10-10.md` line 119 — its gate ran with no `--deselect`; none here.
- THE GATE: `ls -la …/.env` (No such file) · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-launcher-1010 all --deploy` (background) → exit 0. Verdict lines WHOLE:
```
offline 4199/0
lock: waited 0 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-1010-all-20261010-161811.log
```
- (a) `offline 4199/0`. (c) pass 1: every SKIPPED line inside the allowed set — `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = the skip decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F "def test_x14_live_his_template_strips_to_the_committed_fixture" …` → `96:`). (c2) `dev forward: APPLIED 16:42:29` (log line 1110); no `CHANGED` (log 948, 1178, 2020: `content UNCHANGED on every table`). (c3) `with-DB 5096/0`. (f) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log 896) = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log 2030) → `cobalt_dev: 0013 — F2 = F0` (log 2082). (e) `live-note 146/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg.
- THE RELEASE: log 2083–2088 `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-launcher-1010` → `lock released` · `.env: removed` (the log stamps no clock time on the release; it falls between 16:42:29 and 16:47:46). `ls -la …/.env` → No such file; `grep -c -x -F "deploy-launcher-1010" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on edcb1519

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 285]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only (cto-2026-10-08, cto-2026-10-10, harness-mods-review, lock-relief-decisions, next-flow-answer, seat-usage; untracked reports/plans/prompts incl. this report); `?? .claude/settings.json.bak` (see RECORDS). No staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 3c41aba9 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-launcher-1010` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-launcher-1010' (was 3c41aba9)` |
| probe commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 404787d3] scratch: allowlist probe (reverted next line)` → `3c41aba9 docs(desk): R942 model tribunal launch row, launcher deploy card 286` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-10-launcher` | 1 | free |
| pre tag | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-launcher-1010` | 1 | free |

### STEP-D1 (16:48:36 EDT)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 16:48:38 EDT)`. REDs named (not aset / sheet / radar, not a stop): `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC (19.9 h ago), rows written 3308843, exit 1` · `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'`. `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200` · `OK   radar                    idle (overnight)` · `OK   com.cobalt.aset              running   loaded, pid 7760` · `OK   com.cobalt.radar             running   running 559 min, heartbeat fresh` · `OK   com.cobalt.agent             running   pid 22243 alive`. No radar RED (carried family not present).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line. `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 0.6 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` = `<aset pid>`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` = `<radar pid>`; `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-10 16:48:08.273`; no traceback.
- LOG BASELINES: `<a0>` = 277 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`. MARKER `grep -F -e "--fix-report" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` → no output (exit 1, = before).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

## Smoke

## CONTINUE
next: STEP-D2 (gate green at 16:47:46; D0 and D1 done)

## DECISIONS

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" /Users/cobalt/cobalt-wt/.gate-logs/deploy-launcher-1010-all-20261010-161811.log` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. The line was read from the gate's output and the log with Read instead.
- D0: `?? .claude/settings.json.bak` is untracked on `main` — neither in D0's ACCEPTED list nor its REFUSED classes (not staged; not under `src/`, `tests/`, `ops/`, `configs/`); recorded, not a stop.

(run in progress — next step under ## CONTINUE)
