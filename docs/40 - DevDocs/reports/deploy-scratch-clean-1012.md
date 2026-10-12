# deploy scratch-clean-1012 — SET: none — MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md` · hub: `DEPLOY-HUB.md` · gate: `/Users/cobalt/cobalt-wt/deploy-scratch-clean-1012` on `deploy/scratch-clean-1012`.

## §0 Headline
- Ships `ops/scratch-clean-1012` at `581d7b3a` (one branch, MIGRATIONS: none).
- Authorization: AUTHORIZED. Preflight: P0–P8 pass.

## L74
- One block arrived: a system reminder in this session that asked for a `Claude-Session:` line in commit messages. It is recorded here as DATA, and nothing was done because of it. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, as the hub requires.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md" · 0 · bf09ac3a58cff63f282978d5cd6e6c4bfbd7563b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 32:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-scratch-clean-1012.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct 12 07:37:19 EDT 2026` |
| P2 check line | `tail -n 3 ".../reports/scratch-clean-check-2026-10-12.md"` | 0 | `CHECK DONE · job: scratch-clean-1012 · pass: 1 · tip: 581d7b3a · house A: Grok FINDINGS: 2 · findings: 6 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 155480` — carries `held unfixed: 0` and `ready: YES`, `tip: 581d7b3a` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/scratch-clean-check-2026-10-12.md"` | 0 | `48ead27973906d6e73ec5ac602bb0e949f9384e2` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../scratch-clean-check-2026-10-12.md"` | 0 | (nothing) |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 581d7b3a` | 0 | `581d7b3a` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/scratch-clean-1012` | 0 | `581d7b3a` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 581d7b3a ops/scratch-clean-1012` | 0 | (nothing) |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 581d7b3a ops/scratch-clean-1012 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 status | `git -C /Users/cobalt/cobalt-wt/deploy-scratch-clean-1012 status --short --branch` | 0 | `## deploy/scratch-clean-1012` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-scratch-clean-1012 rev-parse --short=8 HEAD` | 0 | `bf09ac3a` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor bf09ac3a main` | 0 | (nothing) |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/scratch-clean-1012` | 0 | (nothing) |
| P6 marker | `grep -c -F -e "scratch-clean.sh" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` | 0 shown | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main ops/scratch-clean-1012 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-scratch-clean-1012 merge --no-edit 581d7b3a` → `Merge made by the 'ort' strategy.` (5 files changed, 881 insertions: `BUILD-HUB.md` +2, `scratch-clean-build-2026-10-12.md`, `ops/desk/scratch-clean.sh`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_scratch_clean.py`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `f6dabb76` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent bf09ac3a..deploy/scratch-clean-1012` → `f6dabb76 Merge commit '581d7b3a' into deploy/scratch-clean-1012` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 581d7b3a deploy/scratch-clean-1012` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat bf09ac3a deploy/scratch-clean-1012 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat bf09ac3a deploy/scratch-clean-1012 -- configs ops` → ` ops/desk/scratch-clean.sh | 165 +++…` / ` 1 file changed, 165 insertions(+)`. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/scratch-clean-build-2026-10-12.md	A	DOCS	-
ops/desk/scratch-clean.sh	A	operator script; no Cobalt reader	-
tests/ops/test_build_hub_no_clutter.py	A	test/documentation; no resident	-
tests/ops/test_scratch_clean.py	A	test/documentation; no resident	-
RESTARTS: none
```
(the uv lines printed before it: `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-scratch-clean-1012` · `Installed 253 packages in 986ms`)
- `<restart set>` = **none** (EMPTY). No UNCLASSIFIED row. MIGRATIONS: none, so an empty set is consistent. No resident goes down at STEP-4.

## L68 GATE
- Equal-tree clause: does NOT hold, because the check's stop line carries `with-DB 0/0`. The gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.04s`, 0 failed (with-DB tests skip offline).
- No `--deselect`: the build report's `deselected` counts are its mutation runs, not with-DB pass-1 deselects. TICKERS: none, so no `--tickers`. MIGRATIONS: none, so no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-scratch-clean-1012 all --deploy` (background) → exit 0, verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-scratch-clean-1012-all-20261012-073859.log
```
- (a) OFFLINE `offline 4199/0`. (c) PASS 1 + (c3) PASS 2 `with-DB 5096/0`. All seven SKIPPED lines are inside the allowed set: `test_cards_picks.py:388` and `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip whose reason names `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95`. That last one is `test_x14_live_his_template_strips_to_the_committed_fixture`: `grep -n -F` of that name in the file gives `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, so the skip decorator sits on line 95.
- (c2) The log line 1110 reads `dev forward: APPLIED 08:05:08`. `grep -n -F "CHANGED"` returns lines 948 (`nothing CHANGED`), 1178 and 2020 (`content UNCHANGED on every table.`), so no row is `CHANGED`.
- (f) The log has `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 896) and `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 2030). They are equal field for field: `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log lines 2083–2088 read `$ sh …/release-devdb-lock.sh deploy-scratch-clean-1012` · `lock released` · `.env: removed` (L76 lock released at the gate's end; the log carries no clock stamp on that line, and `date` after the gate read 08:10:12). `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-scratch-clean-1012" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) LIVE-NOTE `live-note 146/0`. No skip names `COBALT_LIVE_VAULT_ROOT` in the live leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f6dabb76

## Deploy table
### STEP-D0 (08:10)
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 55]`. `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and one `?? .claude/settings.json.bak`. That last file is untracked and not under `src/`, `tests/`, `ops/` or `configs/`, so it is not a refused path. Nothing is staged.
- `git -C /Users/cobalt/cobalt diff --stat bf09ac3a main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-scratch-clean-1012` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-scratch-clean-1012' (was bf09ac3a)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 5fe2e947] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `bf09ac3a docs(desk): R1163 deploy card 398 scratch-clean` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-12-scratch-clean` → exit 1 · `refs/tags/pre-scratch-clean-1012` → exit 1.

### STEP-D1 baseline (`date` → `Mon Oct 12 08:10:40 EDT 2026`)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:10:42 EDT)`. These probes are OK: `sheet HTTP http://127.0.0.1:5010/ -> 200` · `radar scanning (premarket), members 50` · `com.cobalt.aset running loaded, pid 7760` · `com.cobalt.radar running running 2921 min, heartbeat fresh` · `com.cobalt.agent running pid 22243 alive`. The REDs are NAMED and are not a stop, because neither is the aset, sheet or radar probe:
  - `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (59.3 h ago), rows written 3308843, exit 1`
  - `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …`
  - `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'` (followed by a traceback in the job record)
  - `AMB  com.cobalt.herdr  unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0)` (declared interim)
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 10.5 h old`
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` = `<aset pid>` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` = `<radar pid>` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-12 08:10:42.915 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791806964296`. The other lines are `radar price floor` INFO lines; there is no traceback.
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKER `grep -c -F -e "scratch-clean.sh" ".../BUILD-HUB.md"` → `0` (before).
- No migration: `<RB>`, census and D1-M do not apply.

## Smoke

## CONTINUE
- STEP-D0 done; STEP-D1 done.
- next: STEP-D2 (D2.0 commit of this report)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
