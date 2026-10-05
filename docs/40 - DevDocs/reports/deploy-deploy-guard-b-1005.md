# deploy-guard-b-1005 · SET: workflow2 · MIGRATIONS: none

## §0 Headline
- Run in progress. Card `docs/40 - DevDocs/prompts/2026-10-05/15-deploy-guard-b-card.md`, one branch `ops/cobalt-guard-b-1004` at `47ec01c5`.

## L74
- One block arrived asking for a `Claude-Session:` line on commits (a harness attribution reminder at session start). Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/15-deploy-guard-b-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/15-deploy-guard-b-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/15-deploy-guard-b-card.md" · 0 · 7e5f86e52c43325df9c7ae355c7d2d2e5315a0fa
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/15-deploy-guard-b-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R390 row · grep -n "^| R390 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 67:| R390 | 10-05 08:54 ET | HIS RULING (L79, via brain; his word again in desk chat): one feature per deploy, in sequence; a failed combined deploy is split, each alone on its existing check ([words](cto-2026-10-05-words.md#r390)). | APPROVED — pending fold (NOW done; LAWS L68 owed) |
RULING 2026-10-05 R390 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R390 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · ed3cf41a8392be824396ace29672e7d92b8abaa4
RULING 2026-10-05 R390 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R391 row · grep -n "^| R391 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 68:| R391 | 10-05 09:00 ET | HIS RULING (desk chat): commit R389 and R390; go on with the P6 read and the guard-b drafter; (d2) SKIPPED for the workflow deploy too (as R368). | APPROVED |
RULING 2026-10-05 R391 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R391 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · ed3cf41a8392be824396ace29672e7d92b8abaa4
RULING 2026-10-05 R391 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R392 row · grep -n "^| R392 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 70:| R392 | 10-05 09:03 ET | HIS RULING (desk chat): NO Grok read for 03d (the tip-file stage copy was classifier-denied); deploy 03d now; start the guard-b drafter. | APPROVED |
RULING 2026-10-05 R392 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R392 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 5583ead30b4f44f3d46aad3a8ee0f2bf043520d1
RULING 2026-10-05 R392 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| FIRST LAUNCH | `ls -la ".../reports/deploy-deploy-guard-b-1005.md"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (whole under `## AUTHORIZATION`) |
| P1 | `date` | 0 | `Mon Oct  5 09:34:17 EDT 2026` — a trading day outside (i)–(iii); no RULINGS row overrules L66/L43 for this JOB; `MIGRATIONS: none` → **window: (v) provisional** |
| P2 | `tail -n 3 ".../cobalt-guard-b-check-2026-10-04-r3.md"` | 0 | `CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 47ec01c5 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3782/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0` — carries `held unfixed: 0`, `ready: YES`, `tip: 47ec01c5` = row |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../cobalt-guard-b-check-2026-10-04-r3.md"` | 0 | `e3202c78dbdfddd8e50bf70c0bcf5c76a668aed8` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../cobalt-guard-b-check-2026-10-04-r3.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 47ec01c5` | 0 | `47ec01c5` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cobalt-guard-b-1004` | 0 | `47ec01c5` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 47ec01c5 47ec01c5` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 47ec01c5 47ec01c5 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no worktree holds `.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-guard-b-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `faffac00` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor faffac00 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-guard-b-1005` | 0 | empty |
| P6 | `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` | 0 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 47ec01c5 -- src/cobalt/db_migrations` | 0 | nothing — no migration (= `none`) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 13209` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 36907` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 47ec01c5` → `Auto-merging ops/desk/bare-guard.py` / `Merge made by the 'ort' strategy.` (3 files: the build report, `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`; 932 insertions, 20 deletions)
- `git -C <GATE> rev-parse --short=8 HEAD` → `c0227b27` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent faffac00..deploy/deploy-guard-b-1005` → `c0227b27 Merge commit '47ec01c5' into deploy/deploy-guard-b-1005` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 47ec01c5 deploy/deploy-guard-b-1005` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat faffac00 deploy/deploy-guard-b-1005 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`)
- STEP-C `git -C /Users/cobalt/cobalt diff --stat faffac00 deploy/deploy-guard-b-1005 -- configs ops` → ` ops/desk/bare-guard.py | 301 ++++…---` / ` 1 file changed, 284 insertions(+), 17 deletions(-)` — no plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a first `uv` venv build in the gate: `Installed 253 packages`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>` = none (empty). No `UNCLASSIFIED` row.
- P1 (v) RE-READ: the derived set is empty → **window: (v) holds**.

## L68 GATE
- THE EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (and main's `bare-guard.py` auto-merged at T). The gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.60s` — 0 failed (every skip a with-DB skip: `Postgres env settings not available` / `requires_db`).
- (d2) SKIPPED this run only (his R391, card `## RECORDS`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-guard-b-1005 all --deploy` (no `--deselect`: the build deselected no with-DB test; no `--tickers`, no `--migration` on the card) — exit 0. Verdict lines whole:
```
offline 3782/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4634/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-guard-b-1005-all-20261005-093606.log
```
- (a) OFFLINE `offline 3782/0` → `<p>` = 3782.
- (c) PASS 1 (log line 1050): `4461 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 734.61s (0:12:14)`. All seven SKIPPED lines are inside the allowed set: `test_s3_c4_experiments.py:95` is the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`def` at :96, read in the gate tree); `test_replay_line.py:266` names `COBALT_TEST_LIVE_DRC`.
- (c2) `dev forward: APPLIED 09:58:32` (log line 1052).
- (c3) with pass 2: `with-DB 4634/0` → `<d>` = 4634.
- (f) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log 845) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log 1674) → `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log 1726–1728 `sh …/release-devdb-lock.sh deploy-guard-b-1005` → `lock released` [exit 0]; `.env: removed (L76 lock released before 10:03 ET; the log line carries no clock)`. Verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-guard-b-1005" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- (e) LIVE-NOTE `live-note 146/0` → `<l>` = 146; no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on c0227b27

## Deploy table
### STEP-D0 (10:04 ET)
| check | command | exit | result verbatim |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 43]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×5 and `??` ×11 under `docs/40 - DevDocs/` (this report among them); `?? .claude/settings.json.bak` (see `## DECISIONS` 1). No staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path. |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat faffac00 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-deploy-guard-b-1005` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-deploy-guard-b-1005' (was faffac00)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main e1c311b5] scratch: …` · — · `faffac00 docs(desk): R390 status APPROVED pending fold (launch script reads it)` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-guard-b` | 1 | — |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-deploy-guard-b-1005` | 1 | — |

### STEP-D1 baseline (`date` → `Mon Oct  5 10:04:22 EDT 2026`)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-05 10:04:23 EDT)`; every probe OK but `RED  radar                    failed_stage bars: poll failures: 4` (THE CARRIED FAMILY: `com.cobalt.radar  running  running 1045 min, heartbeat fresh`; `radar.err` `2026-10-05 10:03:22.962 … radar cycle: scanning scan_id=1791208922629`, inside 5 min, no traceback in the tail) and `AMB  com.cobalt.herdr  unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …; runs outside launchd by declared interim`. aset / sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (`registry <-> ops/: 15 label(s), exact match.` · `registry <-> plists: schedules and COBALT_ENV agree on every job.`)
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 12.4 h old` (`ssd   local ARMED /Volumes/COBALT-BACKUP/restic`).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = 13209 · `…/com.cobalt.radar` → `state = running`, `<radar pid>` = 36907 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → two `radar cycle: scanning` lines (10:00:22, 10:03:22) and six `cards.expire: falling back to the session close (16:00:00)` INFO lines; no traceback.
- LOG BASELINES: `<a0>` Started server process = 42 · `<ta0>` aset Traceback = 2 · `<tr0>` radar Traceback = 0 · `<tc0>` TaxonomyConfigError = 0 · `<rp0>` radar panel FAILED = 17 · `<rpr0>` radar pool refresh FAILED = 58 · `<re0>` radar S5 evaluate FAILED = 39 · `<lc0>` lifecycle card read failed = 39.
- `curl … http://127.0.0.1:5010/radar` → `200` · MARKER `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` → `0` (= before).
- No migration: `<RB>`, census reads and D1-M not run (`MIGRATIONS: none`).

## Smoke

## CONTINUE
- next: STEP-D2 (D0 and D1 done at 10:05 ET)

## DECISIONS
1. ASK DESK: STEP-D0 MAIN shows `?? .claude/settings.json.bak` — an untracked file the hub's porcelain rule neither accepts nor refuses (refused = a staged line or a dirty `src/`, `tests/`, `ops/`, `configs/` path). Should it be ruled? [10:04 ET] Safe default taken: continue — it is untracked, outside every refused path, and is in no commit or merge of this run; `merge --ff-only` does not touch it.

## RECORDS
- 09:36 ET a clock-filler `COBALT_ENV=production uv run cobalt heartbeat show` typed with cwd still `<GATE>` (no `.env` there) → exit 1 `DbConfigError: Missing Postgres settings for the APP credential`. A cwd slip, not a refusal and not a production read; production reads run from `/Users/cobalt/cobalt` (D1 on).
- REFUSED, not needed: `grep -n -F ".env" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Read the release with `grep -n -F "released"` instead.

(run in progress — next step under ## CONTINUE)
