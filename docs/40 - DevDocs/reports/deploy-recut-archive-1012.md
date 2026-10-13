# deploy recut-archive-1012 · set: none · migrations: none

## §0 Headline
Attempt 2 (resume at STEP-D0, 21:44 EDT) DEPLOYED: `backup run` succeeded (snapshot `57e8fb94`), and `main` fast-forwarded `0dc5c696..4bf3e614` at 21:47:26 with no resident down (RESTARTS none). Smoke GREEN, tag `deploy-2026-10-12-recut-archive`.
Attempt 1 ended at D2.4 (21:41 EDT): the production snapshot (`backup run`) exited 1 on a missing staging dump. Nothing in production changed, nothing merged to `main`, and no resident went down.
Before that: AUTHORIZED; preflight clean; tree `05518bd2`; RESTARTS none; GATE GREEN (offline 4309/0 · with-DB 5212/0 · live-note 146/0); `<stack-final>` `f30db38e` = `<m1>` + docs.
Next (the desk's): fix the backup, then `desk-launch.sh recut`. The desk relaunched with `CONTINUE: STEP-D0` at 21:44 EDT instead; see `# RELAUNCH` and `## RESUME (attempt 2)`.

## L74
The launch context carried a harness attribution reminder asking that commits also end with a `Claude-Session:` line. Recorded here as data and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/439-deploy-recut-archive-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/439-deploy-recut-archive-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/439-deploy-recut-archive-card.md" · 0 · 064401584bca42432c9d63e79e7052f04bf71fb7
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/439-deploy-recut-archive-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 154:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → exit 1, `No such file or directory` (the report did not exist).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 | `date` | 0 | Mon Oct 12 21:07:32 EDT 2026 |
| P2 | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md"` | 0 | last line: `CHECK DONE · job: recut-archive-1012 · pass: 1 · tip: df775390 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4309/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 176420`. It carries `held unfixed: 0` and `ready: YES`, and its tip `df775390` equals the code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md"` | 0 | `1fddf882b7784f60e86c1b75559e8083096e424b` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 df775390` | 0 | `df775390` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/recut-archive-1012` | 0 | `df775390` (= the row and `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor df775390 ops/recut-archive-1012` | 0 | nothing printed |
| P3 | `git -C /Users/cobalt/cobalt diff --stat df775390 ops/recut-archive-1012 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no session holds the lock) |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-recut-archive-1012 status --short --branch` | 0 | `## deploy/recut-archive-1012` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-recut-archive-1012 rev-parse --short=8 HEAD` | 0 | `06440158` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 06440158 main` | 0 | nothing printed |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/recut-archive-1012` | 0 | empty |
| P6 | `grep -c -F -e "archive/pre-" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` | — | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main df775390 -- src/cobalt/db_migrations` | 0 | nothing (`MIGRATIONS: none`) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 14738` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 14748` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-recut-archive-1012 merge --no-edit df775390` → `Merge made by the 'ort' strategy.` (3 files changed: `docs/40 - DevDocs/reports/recut-archive-build-2026-10-12.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_recut.py`; 522 insertions, 5 deletions)
- `git -C <GATE> rev-parse --short=8 HEAD` → `05518bd2` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 06440158..deploy/recut-archive-1012` → `05518bd2 Merge commit 'df775390' into deploy/recut-archive-1012` (one head, one merge)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor df775390 deploy/recut-archive-1012` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 06440158 deploy/recut-archive-1012 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 06440158 deploy/recut-archive-1012 -- configs ops` → ` ops/desk/desk-launch.sh | 109 +++++…---` / ` 1 file changed, 104 insertions(+), 5 deletions(-)`. No plist added, changed or removed.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-recut-archive-1012` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv first built the gate's `.venv`: `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Installed 254 packages in 774ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/recut-archive-build-2026-10-12.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_recut.py	M	test/documentation; no resident	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none). No resident goes down, and the merge lands with residents up.

## L68 GATE
- THE EQUAL-TREE CLAUSE does not hold: the check's stop line carries `with-DB 0/0`, so the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.96s` (0 failed; the skips are with-DB tests: `Postgres env settings not available` / `requires_db`).
- No `--deselect`: the build report names no pass-1 deselect. Its one `deselected` line is a mutation-run `-k` filter. `TICKERS: none`, `MIGRATIONS: none` → no `--tickers` or `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-recut-archive-1012 all --deploy` launched in the background → exit 0. Verdict lines, whole:
```
offline 4309/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5212/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-recut-archive-1012-all-20261012-210930.log
```
- (a) offline `4309/0`. (c)+(c3) with-DB `5212/0`. (e) live-note `146/0`.
- Every SKIPPED line is in the allowed set. `test_s3_c4_experiments.py:95` is the skip mark of `test_x14_live_his_template_strips_to_the_committed_fixture` (the def is at line 96, from a Grep of the gate tree). The `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`.
- (c2) FORWARD: the set carries no migration above `0013`, so nothing was applied forward.
- (f) Log `F0:` line 902 `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `F2:` line 2037 `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`. The gate's line: `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log lines 2090–2095: `$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-recut-archive-1012` → `lock released` `[exit 0]` → `.env: removed`. The log prints no time on this line, so it is recorded at the gate's end (21:38 EDT). `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-recut-archive-1012" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 05518bd2

## Deploy table
### D0 (21:38:59 EDT onward)
| step | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 229]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | No staged line. No dirty `src/`, `tests/` or `ops/` path. `configs/` dirty only as ` M configs/cobalt/rules.yaml`. Also ` M .claude/settings.json`, and ` M`/`??` under `docs/40 - DevDocs/`. Paths outside the accepted list that the refused list does not name: ` M "docs/00 - Project/BACKLOG.md"`, ` M "docs/00 - Project/PROJECT-LEDGER.md"`, ` M "docs/00 - Project/SPRINT-LADDER-v0_1.md"`, ` M "docs/30 - Design/archiver-runs.md"`, `?? .claude/settings.json.bak` (see `## DECISIONS` 1) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 06440158 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-recut-archive-1012` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-recut-archive-1012` | 0 | `Deleted tag 'scratch-allow-probe-recut-archive-1012' (was 06440158)` |
| PROBE | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 8a398050] scratch: allowlist probe (reverted next line)` |
| PROBE | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | — |
| PROBE | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `06440158 docs(desk): R1287 deploy card 439 for card 434 recut-archive` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-12-recut-archive` | 1 | absent |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-recut-archive-1012` | 1 | absent |

### D1 baseline
| read | command | result |
|---|---|---|
| date | `date` | Mon Oct 12 21:39:29 EDT 2026 |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 21:39:30 EDT)`; one AMB: `com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) … runs outside launchd by declared interim`; `radar idle (overnight)`; `com.cobalt.radar running running 195 min, heartbeat fresh`; `com.cobalt.aset running loaded, pid 14738`; `com.cobalt.agent running pid 14763 alive` |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line |
| `<jobs0>` | (validate) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 2.5 h old` (ssd ARMED, b2 off) |
| aset | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 14738` = `<aset pid>` |
| radar | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 14748` = `<radar pid>` |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 14763` | `Cobalt is ONLINE (PID: 14763).` · `14763 ??  0:00.03 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 8 lines, `radar cycle: idle:overnight scan_id=None`, 21:26:42 → 21:38:22, no traceback |
| `<a0>` | `grep -c "Started server process" …/aset.err` | 278 |
| `<ta0>` | `grep -c "Traceback" …/aset.err` | 217 |
| `<tr0>` | `grep -c "Traceback" …/radar.err` | 0 |
| `<tc0>` | `grep -c "TaxonomyConfigError" …/radar.err` | 0 |
| `<rp0>` | `grep -c "radar panel FAILED" …/aset.err` | 18 |
| `<rpr0>` | `grep -c "radar pool refresh FAILED" …/aset.err` | 60 |
| `<re0>` | `grep -c "radar S5 evaluate FAILED" …/radar.err` | 43 |
| `<lc0>` | `grep -c "lifecycle card read failed" …/radar.err` | 39 |
| curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | `200` |
| marker | `grep -c -F -e "archive/pre-" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` | `0` (= before) |
| migration | — | `MIGRATIONS: none`, so `<RB>`, census and D1-M are not run |

### D2
| step | command | exit | result |
|---|---|---|---|
| D2.0 | `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-recut-archive-1012.md"` · `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy recut-archive-1012 — gate green on 05518bd2" …` | 0 | `[main d4b80886] … 1 file changed, 151 insertions(+)` |
| D2.0 | `git -C /Users/cobalt/cobalt show --stat HEAD` | 0 | one file: `.../reports/deploy-recut-archive-1012.md` |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `d4b80886` = `<pre-merge>` |
| D2.1 | `git -C /Users/cobalt/cobalt-wt/deploy-recut-archive-1012 merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `f30db38e` = `<stack-final>` |
| D2.2 | `git -C /Users/cobalt/cobalt rev-parse --short=8 f30db38e^2` | 0 | `d4b80886` (= `<pre-merge>`) |
| D2.2 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 05518bd2 f30db38e` | 0 | — |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 05518bd2 f30db38e -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing (docs only) |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 2.5 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` (FOREGROUND, timeout 600000) | **1** | `21:40:30.054 … F17: com.cobalt.backup RUNNING (timeout 3600s, heartbeat every 1200s)` / `21:41:01.259 \| ERROR \| cobalt.jobs.wrapper:job_run:192 - F17: com.cobalt.backup FAILED — FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-backups/staging/cobalt_brain.sql'` / `FAILED: FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-backups/staging/cobalt_brain.sql'` |
| after | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.0 h old`. A snapshot was written even though the run exited 1, and its contents are unproven (L70): the `cobalt_brain` dump file it needed was missing. No dump-size line and no snapshot id were printed |
| after | `launchctl print` aset / radar · `cobalt.sh status` | 0 | aset `state = running` `pid = 14738` · radar `state = running` `pid = 14748` · `Cobalt is ONLINE (PID: 14763).` (unchanged from D1) |
| after | `git -C /Users/cobalt/cobalt merge-base --is-ancestor f30db38e main` | 1 | nothing merged to `main` |
| after | `git -C <GATE> status --short --branch` | 0 | `## deploy/recut-archive-1012` (no open merge) |
| after | `date` | 0 | Mon Oct 12 21:41:11 EDT 2026 |

The run stopped at D2.4. D2.5, D2.6 (the `pre-recut-archive-1012` tag) and STEP-4 to STEP-7 (1) were not run. No resident went down, `main` is `d4b80886` with the report only, and no tag was set. `<restart set>` is empty, so this deploy would have had no outage. No ROLLBACK STRING is needed: nothing merged.

## Smoke
Attempt 1: not run, because it stopped before the merge. Attempt 2 (`<t up>` = 21:47:26 EDT, `<restart set>` EMPTY):
| row | date | command | result |
|---|---|---|---|
| first calls | 21:47:26+ | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 |
| (a) | 21:47:41 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `cobalt.sh status` | aset `state = running` `pid = 14738` (SAME, outside the set) · radar `state = running` `pid = 14748` (SAME) · `Cobalt is ONLINE (PID: 14763).` (SAME). GREEN |
| (b) | 21:47:44 | `grep -c "Started server process" …/aset.err` | `278` = `<a0>` (aset outside the set). GREEN |
| (b) | 21:47:44 | `tail -n 30 …/aset.err` | ends `INFO:     Started server process [14744]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` (the 18:24 start, unchanged) |
| (b) | 21:47:44 | Traceback aset / Traceback radar / TaxonomyConfigError | `217` / `0` / `0` = baseline. GREEN |
| (c) | 21:47:44+ | `curl … https://cobalt.taild24291.ts.net/` · `…/radar` · `…/radar\?frame=phone` | `200` · `200` · `200`, first attempt each. GREEN |
| (d) | 21:47:44+ | `grep -c -F -e "archive/pre-" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` | `3` (after: 1 or more). GREEN |
| (f) | 21:47:44+ | `COBALT_ENV=production uv run cobalt jobs restarts 0dc5c696..4bf3e614` | exit 0; three rows `DOCS -` / `operator script; no Cobalt reader -` / `test/documentation; no resident -`; `RESTARTS: none` = STEP-R's set; no `UNCLASSIFIED`. GREEN |
| (f) | 21:47:55 | `COBALT_ENV=production uv run cobalt validate` | exit 0, as 4.5: `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` GREEN |
| (g) | — | — | no migration |
| (s) | 21:47:55 | `grep -c -F -e "archive/pre-" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` (the recut archive step is on main) | exit 0, `3` (green: 1 or more). GREEN. The gate ran `tests/ops/test_desk_launch_recut.py` inside offline 4309/0 |
| (e) 1 | 21:47:57 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 21:47:57 EDT)`; `com.cobalt.radar running running 204 min, heartbeat fresh` |
| clock | 21:48:12 → 21:48:56 | `date` + `heartbeat show` pairs (the hub's only clock) | every read `HEARTBEAT GREEN — … nothing red` |
| (b) tail 1 | 21:48:56 (`<t up>` + 90 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | 12 × `radar cycle: idle:overnight scan_id=None`, 21:30:02 → `2026-10-12 21:48:22.364 … radar cycle: idle:overnight scan_id=None`, stamped after `<t up>`. No `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback. SETTLED GREEN |
| (e) 2 | 21:49:47 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 21:49:49 EDT)`, 112 s after (e) 1; `com.cobalt.radar running running 206 min, heartbeat fresh`; no RED (attempt 1's `com.cobalt.backup` RED in `<hb0>` cleared: `done … 21:46 ET, exit 0`). GREEN |
| clock | 21:49:53 → 21:50:26 | `date` + `heartbeat show` pairs | every read `HEARTBEAT GREEN — … nothing red` |
| (h) | 21:50:26 (`<t up>` + 180 s) | the four failure counts · `curl … /radar` | `18` · `60` · `43` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200`. No `census` line on the card. GREEN |
| tag (STEP-7 (1)) | after (h) | `git -C /Users/cobalt/cobalt tag deploy-2026-10-12-recut-archive` · `rev-parse --short=8 deploy-2026-10-12-recut-archive` | `4bf3e614` |

THE CHAIN: every check committed (P2: `1fddf882`, unmodified, `held unfixed: 0` · `ready: YES`) → the tips re-read (P3: `df775390` = head = `TIP`) → the merged tree (T: `05518bd2`, one head, clean) → RESTARTS derived (R: none, no `UNCLASSIFIED`) → three suites green on `<m1>` (G: offline 4309/0 · with-DB 5212/0 · live-note 146/0) → `<stack-final>` `4bf3e614` = `<m1>` + docs (D2.3) → the landed code (4.3: fast-forward `0dc5c696..4bf3e614`) → the marker (d: `3`) → no migration (g) → residents up and unchanged after the merge (a: pids 14738 / 14748 / 14763) → radar cycling (b: 21:48:22, e: GREEN twice) → the set's read (s: `3`) → no new failure (h: counts flat). The desk confirms the card surface with him (L70); it does not apply here, because this set changes an operator script only.

## CONTINUE
Attempt 2 (resume): D0, D1, D2, STEP-4, smoke and STEP-7 are done. next: none — DEPLOYED. The desk's next steps: push (his, L55) and the cleanup owed (`## RECORDS`).
Outage entry as written before 4.1: OUTAGE STARTING 21:47:08 EDT — residents of <restart set> = none (EMPTY) going down: none; the merge lands with the residents up. If this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
Attempt 1: next was none — it stopped at D2.4. The desk decides: fix `backup run` (the missing staging dump `/Users/cobalt/cobalt-backups/staging/cobalt_brain.sql`), then `desk-launch.sh recut "<card>"` (the hub's RECUT path for `rollback: not used`).

## DECISIONS
1. ASK DESK: at D0, `status --porcelain` shows dirty paths that the accepted list does not name and the refused list does not name either: ` M` under `docs/00 - Project/` and `docs/30 - Design/`, and `?? .claude/settings.json.bak`. BACKLOG, SPRINT-LADDER and `cto-2026-10-12.md` were not dirty in the launch snapshot. All of them are unstaged working-tree edits, none is in `src/`, `tests/`, `ops/` or `configs/`, and none enters the merge, which lands only committed trees. Safe default taken: not a refusal, go on. [21:39 EDT]

2. ASK DESK: `backup run` failed at D2.4 with `FileNotFoundError … /Users/cobalt/cobalt-backups/staging/cobalt_brain.sql`, yet `backup status` then reads `newest snapshot: 0.0 h old`. Whether that snapshot holds the production database is unproven (L70). The nightly `com.cobalt.backup` finished at 19:09 ET with exit 0 (heartbeat), so this run's own dump step failed and the cause is not read here. Safe default taken: no deploy without a proven snapshot (L73), so the run stopped with nothing in production changed. [21:41 EDT]

3. ASK DESK: THE ONE RESUME check (c) writes `git -C /Users/cobalt/cobalt merge-base --is-ancestor <m1> HEAD`. In `/Users/cobalt/cobalt`, HEAD is `main`, and check (d) requires that `main` does NOT carry `<m1>`, so read literally (c) and (d) can never both hold. Safe default taken: ran it as `git -C <GATE> merge-base --is-ancestor 05518bd2 HEAD` (a listed `git -C * merge-base*` string), which tests the gate's HEAD → exit 0. The hub text is the desk's to fix. [21:44 EDT]

4. ASK DESK: the hub's RECUT line says a run that FAILED with `rollback: not used` "is not resumed", and the desk's next step is `desk-launch.sh recut`. This session was launched as `CONTINUE: STEP-D0` instead. THE ONE RESUME's check (a) accepts any old last line that begins `FAILED:`, and (a)–(e) all held. Safe default taken: follow THE ONE RESUME. It is still bounded by D2.4: without a proven snapshot the run stops again before anything goes down. [21:45 EDT]

## RECORDS
- Attempt 2 (resume): `backup run` succeeded this time (snapshot `57e8fb94`, `cobalt_brain` dump 7133.7 MB, exit 0). Attempt 1's `FileNotFoundError` on `/Users/cobalt/cobalt-backups/staging/cobalt_brain.sql` did not recur. Its cause was not read by this run (L70: unproven). Attempt 1's snapshot at 21:41 stays unproven.
- Attempt 2: downtime none (`<restart set>` empty). `main` gained this session's D2.0 commit `0dc5c696`, the fast-forward to `4bf3e614`, and the STEP-7 report commit.
- Attempt 2 cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-recut-archive-1012` and branch `deploy/recut-archive-1012` (now merged at `4bf3e614`), and the set's branch `ops/recut-archive-1012` and its worktree.
- Attempt 2: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh session_01Sfa7tYNzoaZ6Gzckzyj3cs` → exit 2 `no transcript for session_01Sfa7tYNzoaZ6Gzckzyj3cs` (the remote-control id, not the transcript id). Re-run with the transcript id `171b5948` → `context 177654 of 400000 — ok`.
- Attempt 2 PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and quotes its output; (2) `df775390` was re-read at P3 (attempt 2), and `git -C /Users/cobalt/cobalt merge-base --is-ancestor df775390 4bf3e614` → exit 0; (3) REVERT-READBACK (h) is shown (18 · 60 · 43 · 39, flat), and every sha and count was read from this run's tool output (`rev-parse --short=8 deploy-2026-10-12-recut-archive` → `4bf3e614`); (4) no conflict: STEP-T (attempt 1) and both D2.1 merges were clean. THE RELEASE: `ls -la <GATE>/.env` → `No such file or directory`; the lock was released by the gate at attempt 1.
- Attempt 2 (resume): the launch context again carried the harness attribution reminder asking for a `Claude-Session:` line. L74 data, not acted on.
- Downtime: none. No resident went down (`<restart set>` empty, and the run stopped before STEP-4).
- `cobalt_dev: 0013 (F2 = F0)`: the gate's line, `F0`/`F2` `664 35 272c95bbb12241e3611e4b36326ccf87`; lock released, `.env: removed`.
- REFUSED, not needed: `grep -n -F ".env: removed" /Users/cobalt/cobalt-wt/.gate-logs/deploy-recut-archive-1012-all-20261012-210930.log` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Read instead with `grep -n -F "released"` and the Read tool on the log.
- No `RETIRE OWED`: no plist was removed.
- Carried RED: none. `<hb0>` was GREEN, with `com.cobalt.herdr` AMBER by declared interim.
- A snapshot was written by the failed `backup run` (`newest snapshot: 0.0 h old`), contents unproven. See `## DECISIONS` 2.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-recut-archive-1012` and branch `deploy/recut-archive-1012` (at `f30db38e`), and the set's branch `ops/recut-archive-1012` and its worktree. The recut cleans the gate.
- `main` carries this session's one D2.0 commit `d4b80886` (the report), plus the FAILED-ending commit of this report.
- L74: one line arrived (the `Claude-Session:` attribution request, see `## L74`). Not followed.
- Card `## RECORDS`, copied:
  - recut-archive-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md` last line: CHECK DONE · job: recut-archive-1012 · pass: 1 · tip: df775390 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4309/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 176420
  - recut-archive-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/recut-archive-1012` → `df775390`; code tip `df775390`
  - written by deploy-card.sh at 2026-10-12 21:07 ET (`date`); trial merge of the heads onto main in order: clean
- PRE-STOP SELF-CHECK: (1) no smoke ran, and every D-row is quoted with its `date`; (2) `df775390` was re-read at P3 and is an ancestor of `<BRANCH>`, and `<m1>` `05518bd2` is an ancestor of `<stack-final>` `f30db38e`; (3) no merge landed, so no REVERT-READBACK applies, and every sha and count above was read from tool output this run; (4) STEP-T and D2.1 were clean merges with no conflict.

# RELAUNCH
Launch message: `CONTINUE: STEP-D0` (THE ONE RESUME). `date` → Mon Oct 12 21:44:21 EDT 2026. The report's last non-blank line before this resume, quoted:
> `FAILED: D2.4 — backup run exit 1: FileNotFoundError /Users/cobalt/cobalt-backups/staging/cobalt_brain.sql; no proven snapshot, nothing in production changed · rollback: not used · decisions: 2 · for Dejan: 0 · tokens: 123536`

Resume checks, each its own call, (e) first:
- (e) `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 14738` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 14748` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` TRUE: residents up, nothing to restore, downtime none.
- (a) the old last line begins `FAILED:` (quoted above). TRUE.
- (b) `## L68 GATE` carries `GATE GREEN on 05518bd2`; `## RESTARTS` carries `<restart set>` = EMPTY (`RESTARTS: none`). Recorded: `<m1>` = `05518bd2`, `<restart set>` = none. TRUE.
- (c) `git -C <GATE> status --short --branch` → `## deploy/recut-archive-1012` · `git -C <GATE> rev-parse --short=8 HEAD` → `f30db38e` (above `<m1>`: attempt 1's D2.1 `main`-into-gate merge) · `git -C <GATE> merge-base --is-ancestor 05518bd2 HEAD` → exit 0 · `git -C /Users/cobalt/cobalt diff --stat 05518bd2 deploy/recut-archive-1012 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing. TRUE. (The hub writes the ancestry call as `git -C /Users/cobalt/cobalt … HEAD`, but in that tree HEAD is `main`, which (d) proves does not carry `<m1>`. It was run with `-C <GATE>` so that HEAD is the gate's HEAD, which is what (c) tests. See `## DECISIONS` 3.)
- (d) `git -C /Users/cobalt/cobalt merge-base --is-ancestor 05518bd2 main` → exit 1 (nothing merged to `main`). TRUE.
- THE GATE'S OWN `.env`: `ls -la /Users/cobalt/cobalt-wt/deploy-recut-archive-1012/.env` → `No such file or directory`. No G (f) and no release are owed.

## RESUME (attempt 2)
### STEP-0, fresh rows
| rule | command | exit | result |
|---|---|---|---|
| P0 | `sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "<card>"` | 0 | the same eleven rows as `## AUTHORIZATION` (R1138 row now at line 157), last line `AUTHORIZED` |
| P1 | `date` | 0 | Mon Oct 12 21:44:43 EDT 2026 |
| P2 | `tail -n 3 "…/recut-archive-check-2026-10-12.md"` | 0 | last line unchanged: `CHECK DONE · … · tip: df775390 · … · held unfixed: 0 · open: 0 · … · ready: YES · …` |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md"` | 0 | `1fddf882b7784f60e86c1b75559e8083096e424b` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 df775390` | 0 | `df775390` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/recut-archive-1012` | 0 | `df775390` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor df775390 ops/recut-archive-1012` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat df775390 ops/recut-archive-1012 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | (resume) status / HEAD as check (c) found them: `## deploy/recut-archive-1012`, `f30db38e`; `<m0>` = `06440158` (the report's) | — | — |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 06440158 main` | 0 | — (the EMPTY check is not run on a resume) |
| P6 | `grep -c -F -e "archive/pre-" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` | 0 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main df775390 -- src/cobalt/db_migrations` | 0 | nothing |
| P8 | `launchctl print` aset / radar (resume check (e), 21:44) | 0 | running; `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` (check (e)) | 0 | `Cobalt is ONLINE (PID: 14763).` |

### D0
| step | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 233]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; no dirty `src/`, `tests/`, `ops/`; `configs/` only ` M configs/cobalt/rules.yaml`; the same unnamed paths as attempt 1 (`## DECISIONS` 1, same default); this report ` M` |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 06440158 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-recut-archive-1012` · `tag -d …` | 0 | `Deleted tag 'scratch-allow-probe-recut-archive-1012' (was 7ff8abae)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 | `[main 255e4ed3] …` · — · `7ff8abae docs(desk): HANDOVER fd1710af to 745a6747, R1290 refresh` (HEAD back) |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-12-recut-archive` | 1 | absent |
| TAG | `rev-parse --verify --quiet refs/tags/pre-recut-archive-1012` | 1 | absent (attempt 1 never set it) |

### D1 baseline (fresh)
| read | command | result |
|---|---|---|
| date | `date` | Mon Oct 12 21:45:01 EDT 2026 |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 1 job(s)  (2026-10-12 21:45:02 EDT)`. The one RED: `RED  com.cobalt.backup  failed  FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-backups/staging/cobalt_brain.sql'` + a traceback in `cobalt/jobs/wrapper.py` line 179 `job_run` (attempt 1's D2.4 run). Not the aset / sheet probe and not radar: named, not a stop. `OK backup newest snapshot 0.1 h old across ssd` · `OK sheet HTTP … -> 200` · `OK radar idle (overnight)` · `com.cobalt.aset running loaded, pid 14738` · `com.cobalt.radar running running 201 min, heartbeat fresh` · `com.cobalt.agent running pid 14763 alive` · `AMB com.cobalt.herdr` (declared interim) |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line |
| `<jobs0>` | (validate) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | `ssd local ARMED /Volumes/COBALT-BACKUP/restic` · `b2 off` · `newest snapshot: 0.1 h old` |
| aset / radar / agent | check (e) · `ps -p 14763` | running `14738` · running `14748` · ONLINE `14763` · `14763 ??  0:00.03 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 8 × `radar cycle: idle:overnight scan_id=None`, 21:33:22 → 21:45:02, no traceback |
| `<a0>` `<ta0>` `<tr0>` `<tc0>` | the four `grep -c` | 278 · 217 · 0 · 0 |
| `<rp0>` `<rpr0>` `<re0>` `<lc0>` | the four `grep -c` | 18 · 60 · 43 · 39 |
| curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | `200` |
| marker | P6 | `0` (= before) |
| migration | — | `MIGRATIONS: none` |

### D2 (attempt 2)
| step | command | exit | result |
|---|---|---|---|
| D2.0 | `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-recut-archive-1012.md"` · `commit -m "docs(report): deploy recut-archive-1012 — gate green on 05518bd2" …` | 0 | `[main 0dc5c696] … 1 file changed, 71 insertions(+), 4 deletions(-)` |
| D2.0 | `git -C /Users/cobalt/cobalt show --stat HEAD` | 0 | one file: `.../reports/deploy-recut-archive-1012.md` |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `0dc5c696` = `<pre-merge>` |
| D2.1 | `git -C /Users/cobalt/cobalt-wt/deploy-recut-archive-1012 merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.`: `docs/40 - DevDocs/reports/cto-2026-10-12.md` (14 ±) and `.../reports/deploy-recut-archive-1012.md` (114 ±), 2 files |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `4bf3e614` = `<stack-final>` |
| D2.2 | `git -C /Users/cobalt/cobalt rev-parse --short=8 4bf3e614^2` | 0 | `0dc5c696` (= `<pre-merge>`) |
| D2.2 | `git -C /Users/cobalt/cobalt rev-parse --short=8 4bf3e614^1` | 0 | `f30db38e` (attempt 1's main-into-gate merge, above `<m1>`; recorded) |
| D2.2 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 05518bd2 4bf3e614` | 0 | — |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 05518bd2 4bf3e614 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing (docs only) |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.1 h old` (attempt 1's unproven one) |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` (FOREGROUND, timeout 600000) | 0 | `21:46:44.662 … backup: cobalt_brain via pg_dump inside cobalt_memory — 7133.7 MB` · `backup: cobalt_brain dumped, 7133.7 MB` · `backup: ssd: snapshot 57e8fb94 — 0 new / 2 changed, 200.8 MB added, 1 pruned` · `F17: com.cobalt.backup DONE` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.0 h old` (= `57e8fb94`) |
| D2.5 | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | 21:47:03 EDT (121 s after D1's 21:45:02) · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 21:47:05 EDT)`; `com.cobalt.backup done last finish 2026-10-12 21:46 ET, exit 0`; aset `pid 14738`, radar `running 203 min, heartbeat fresh`, agent `pid 14763 alive`; no new RED |
| D2.6 | `date` | 0 | Mon Oct 12 21:47:08 EDT 2026 |
| D2.6 | `git -C /Users/cobalt/cobalt tag pre-recut-archive-1012` · `rev-parse --short=8 pre-recut-archive-1012` | 0 | `0dc5c696` (= `<pre-merge>`) |

### STEP-4 (attempt 2; `<restart set>` EMPTY)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | Mon Oct 12 21:47:26 EDT 2026 = `<t down>` (nothing went down) |
| 4.2 | — | — | empty set: no bootout, no orphan-clean, no agent stop |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `0dc5c696` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/recut-archive-1012` | 0 | `Updating 0dc5c696..4bf3e614` / `Fast-forward`: `.../reports/recut-archive-build-2026-10-12.md` +140, `ops/desk/desk-launch.sh` 109 ±, `tests/ops/test_desk_launch_recut.py` +278; 3 files, 522 insertions, 5 deletions |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | — | — | empty set: nothing to bootstrap. `<t up>` = 4.3's `date`, 21:47:26 EDT. Downtime: none |

### Deploy summary (attempt 2)
- `<pre-merge>` `0dc5c696` → `<stack-final>` `4bf3e614` (`main` fast-forwarded). `<m0>` `06440158`, `<m1>` `05518bd2`.
- Tags: rollback `pre-recut-archive-1012` at `0dc5c696`; release `deploy-2026-10-12-recut-archive` (STEP-7 (1), after green smoke).
- `<t down>` 21:47:26 / `<t up>` 21:47:26 / 0 s: `none`, the set is empty and no resident went down.
- uv sync line: none printed on the production calls. Proof cost: not run (`MIGRATIONS: none`). `migrations applied: none`. `<RB>`: none.
- Snapshot: `57e8fb94` (ssd), `cobalt_brain` dump 7133.7 MB.
- `RESTARTS done: none`.
- THE ROLLBACK STRING (the desk's): 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 4bf3e614`. The set is empty, so no resident goes down. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

DEPLOYED deploy-2026-10-12-recut-archive 4bf3e614 | set: none | migrations: none | gate: offline 4309/0 · with-DB 5212/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 4 · for Dejan: 0 · tokens: 177654
