# deploy recut-archive-1012 · set: none · migrations: none

## §0 Headline
In progress. Started 2026-10-12 21:07 EDT. AUTHORIZED.

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

## CONTINUE
next: STEP-D2 (D2.0 report commit)

## DECISIONS
1. ASK DESK: at D0, `status --porcelain` shows dirty paths that the accepted list does not name and the refused list does not name either: ` M` under `docs/00 - Project/` and `docs/30 - Design/`, and `?? .claude/settings.json.bak`. BACKLOG, SPRINT-LADDER and `cto-2026-10-12.md` were not dirty in the launch snapshot. All of them are unstaged working-tree edits, none is in `src/`, `tests/`, `ops/` or `configs/`, and none enters the merge, which lands only committed trees. Safe default taken: not a refusal, go on. [21:39 EDT]

## RECORDS
- (filled at close)

(run in progress — next step under ## CONTINUE)
