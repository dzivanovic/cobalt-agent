# deploy-guard-b-1005 · SET: workflow2 · MIGRATIONS: none

## §0 Headline
- DEPLOYED `deploy-2026-10-05-guard-b`: main `28b243d0` → `69920ad3`, one branch `ops/cobalt-guard-b-1004` at `47ec01c5` (card `docs/40 - DevDocs/prompts/2026-10-05/15-deploy-guard-b-card.md`).
- Gate green on `c0227b27`: offline 3782/0 · with-DB 4634/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0), lock released.
- RESTARTS: none, no downtime, no migration; window (v) at 10:06 ET on a trading day. Smoke GREEN; marker `@include` 0 → 3.
- One ASK DESK (an untracked `.claude/settings.json.bak` on main); none for Dejan.

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

### STEP-D2
- D2.0 `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-deploy-guard-b-1005.md"` → `[main 28b243d0] docs(report): deploy deploy-guard-b-1005 — gate green on c0227b27` · `show --stat HEAD` → that one file (146 insertions) · `rev-parse --short=8 main` → `28b243d0` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `rev-parse --short=8 HEAD` → `69920ad3` = `<stack-final>` · `rev-parse --short=8 69920ad3^2` → `28b243d0` (= `<pre-merge>`) · `merge-base --is-ancestor c0227b27 69920ad3` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat c0227b27 69920ad3 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs-only).
- D2.4 `backup status` → `newest snapshot: 12.4 h old` · `backup run` (foreground) → `backup: cobalt_brain via pg_dump inside cobalt_memory — 4617.0 MB` · `ssd: snapshot 6679e7f0 — 9 new / 10 changed, 323.2 MB added, 0 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `10:06:14` · `heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-05 10:06:16 EDT)` (113 s after D1's 10:04:23): only `RED  radar  failed_stage bars: poll failures: 1; poll SDEV stale since 2026-10-05T13:59:03.792443+00:00` — the carried family (`com.cobalt.radar running … heartbeat fresh`); aset / sheet OK. No new RED. (Clock fillers at 10:05:58 and 10:06:04 read the same family, `poll failures: 4; poll SDEV stale since …`.)
- D2.6 `date` → `Mon Oct  5 10:06:21 EDT 2026` — window (v) holds (empty restart set, no migration; any hour). `git -C /Users/cobalt/cobalt tag pre-deploy-guard-b-1005` at `28b243d0` → exit 0.

### STEP-4 (empty restart set)
- 4.1 `date` → `Mon Oct  5 10:06:35 EDT 2026` = `<t down>` (nothing goes down; = `<t up>`).
- 4.2 acts on nothing (set empty).
- 4.3 `rev-parse --short=8 HEAD` → `28b243d0` (= `<pre-merge>`) · `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-guard-b-1005` → `Updating 28b243d0..69920ad3` / `Fast-forward` (`cobalt-guard-b-build-2026-10-04.md`, `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`; 932 insertions, 20 deletions).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`.
- 4.6 acts on nothing. `<t up>` = 10:06:35 · downtime: none.

### STEP-7 summary
| item | value |
|---|---|
| main | `<pre-merge>` `28b243d0` → `<stack-final>` `69920ad3` (`rev-parse --short=8 main` → `69920ad3`) |
| tags | `pre-deploy-guard-b-1005` at `28b243d0` · `deploy-2026-10-05-guard-b` at `69920ad3` (set after the green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty set; merge at 10:06:35) |
| uv sync line | none in production; the gate's first `uv run` built `<GATE>/.venv` (`Installed 253 packages`) |
| proof cost | none (no migration; the gate's dev proof-only: `Proof cost: total 6.4 s`) |
| migrations applied | none |
| `<RB>` before / after | not applicable (`MIGRATIONS: none`) |
| snapshot | `ssd: snapshot 6679e7f0` (cobalt_brain 4617.0 MB; 323.2 MB added) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 69920ad3` — no resident to take down or bring up (empty set). 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. |

PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and the output verbatim. (2) `rev-parse --short=8 47ec01c5` / `ops/cobalt-guard-b-1004` → `47ec01c5` (P3); `git -C /Users/cobalt/cobalt merge-base --is-ancestor 47ec01c5 69920ad3` → exit 0. (3) REVERT-READBACK is (h) above; every count, sha and `file:line` here was read from tool output this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); `git -C <GATE> status --short` → nothing.

## Smoke
- FIRST CALLS (after `<t up>` 10:06:35): `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 39 · `<lc_up>` 39 (= D1).
- (a) `date` 10:06:51 · `launchctl print …aset` → `state = running`, `pid = 13209` (SAME, outside the set) · `…radar` → `state = running`, `pid = 36907` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (same). GREEN.
- (b) `date` 10:06:54 · `Started server process` = 42 (= `<a0>`, aset outside the set) · aset Traceback 2 (= `<ta0>`) · radar Traceback 0 (= `<tr0>`) · TaxonomyConfigError 0 (= `<tc0>`). Radar tails below.
- (c) `date` 10:06:54 · `curl …/` → `200` · `curl …/radar` → `200` · `curl …/radar\?frame=phone` → `200`. GREEN.
- (d) `date` 10:06:54 · `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` → `3` (= after). GREEN.
- (s) cobalt-guard-b awk fence · the same read → exit 0, `3` (≥ 1). GREEN. The guard's tests are quoted from the gate (offline 3782/0).
- (f) `date` 10:07:04 · `COBALT_ENV=production uv run cobalt jobs restarts 28b243d0..69920ad3` → exit 0, the same three rows, `RESTARTS: none` (= STEP-R), no `UNCLASSIFIED` · `validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`, `Placement (docs/PLACEMENT.md): tree clean.` GREEN.
- (e) read 1 `heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-05 10:07:06 EDT)`: only `RED  radar  failed_stage bars: poll failures: 1; poll SDEV stale since 2026-10-05T13:59:03.792443+00:00` (the carried family) · `com.cobalt.radar  running  running 1048 min, heartbeat fresh`.
- (g) no migration: not run.
- (e) read 2 `date` 10:08:56 · `heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-05 10:08:58 EDT)` (112 s after read 1): only the carried family `RED  radar  failed_stage bars: poll failures: 1; poll SDEV stale since 2026-10-05T13:59:03.792443+00:00`; `com.cobalt.radar  running  running 1050 min, heartbeat fresh`. No new RED. GREEN. (From 10:09:16 the fillers read `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red` with `OK   radar  scanning (rth), members 50`.)
- (b) RADAR TAILS: tail 1 `date` 10:08:05 (`<t up>` + 90 s) → last cycle `2026-10-05 10:06:23.261 … radar cycle: scanning scan_id=1791209102994` (before `<t up>`) · tail 2 `date` 10:09:37 (+ 182 s) → `2026-10-05 10:09:23.734 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791209283293`, stamped after `<t up>`, with only `cards.expire` INFO lines around it; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback. SETTLED GREEN (no third tail needed).
- (h) REVERT-READBACK `date` 10:09:41 (`<t up>` + 186 s, after (b) settled): radar panel FAILED 17 · pool refresh FAILED 58 · S5 evaluate FAILED 39 · lifecycle card read failed 39 — each = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) · `curl …/radar` → `200`. No census read (no migration). GREEN.

THE CHAIN: every check committed (P2: `e3202c78`, clean, `held unfixed: 0 · ready: YES`) → the tip re-read (P3: `47ec01c5` = head) → the merged tree (T: `c0227b27`, one merge, no migration) → RESTARTS derived (R: none) → three suites green on `c0227b27` (G: offline 3782/0 · with-DB 4634/0 · live-note 146/0) → `<stack-final>` `69920ad3` = `<m1>` + docs (D2.3) → the landed code (4.3: `28b243d0..69920ad3` fast-forward) → markers (d: `@include` 0 → 3) → no migration (g) → residents untouched and up after the merge (a: same pids) → radar cycling (b, e) → the set's read (s: `3`) → no new failure (h). The guard's live behaviour on a session's calls is not a production read here; the desk confirms it with him (L70).

## CONTINUE
- done: STEP-7 at 10:10 ET; nothing further.
- (history) OUTAGE STARTING 10:06:21 ET — residents of <restart set> = none going down (the set is empty: no resident goes down; the merge lands with the residents up); if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0

## DECISIONS
1. ASK DESK: STEP-D0 MAIN shows `?? .claude/settings.json.bak` — an untracked file the hub's porcelain rule neither accepts nor refuses (refused = a staged line or a dirty `src/`, `tests/`, `ops/`, `configs/` path). Should it be ruled? [10:04 ET] Safe default taken: continue — it is untracked, outside every refused path, and is in no commit or merge of this run; `merge --ff-only` does not touch it.

## RECORDS
- 09:36 ET a clock-filler `COBALT_ENV=production uv run cobalt heartbeat show` typed with cwd still `<GATE>` (no `.env` there) → exit 1 `DbConfigError: Missing Postgres settings for the APP credential`. A cwd slip, not a refusal and not a production read; production reads run from `/Users/cobalt/cobalt` (D1 on).
- Downtime: none (empty restart set; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both.
- RETIRE OWED: none (no plist removed).
- THE CARRIED RED as read: `RED  radar  failed_stage bars: poll failures: <n>` with, from 10:05:58 on, `; poll SDEV stale since 2026-10-05T13:59:03.792443+00:00` — at D1 (`n` 4), D2.5 (`n` 1) and every smoke read; radar `running … heartbeat fresh` throughout.
- CLEANUP OWED (L46, the desk's): the gate worktree `/Users/cobalt/cobalt-wt/deploy-guard-b-1005` and branch `deploy/deploy-guard-b-1005`; the set's branch `ops/cobalt-guard-b-1004` and its worktree if any; the gate's `.venv` was built in the gate worktree at STEP-R.
- The deploy changed `ops/desk/bare-guard.py`, the PreToolUse hook that guards this session's own Bash calls; every call after 4.3 went through the new guard and none was refused.
- Card `## RECORDS` (the desk's, copied):
  - cobalt-guard-b: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cobalt-guard-b-check-2026-10-04-r3.md` last line: CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 47ec01c5 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3782/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0
  - cobalt-guard-b: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cobalt-guard-b-1004` → `47ec01c5`; code tip `47ec01c5`
  - G (d2) SKIPPED this run only (his R391): main's hub still runs the old (d2) until 03d ships. No Grok read.
- The L74 line: one `Claude-Session:` attribution block arrived (see `## L74`); not acted on.
- REFUSED, not needed: `grep -n -F ".env" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Read the release with `grep -n -F "released"` instead.

DEPLOYED deploy-2026-10-05-guard-b 69920ad3 | set: workflow2 | migrations: none | gate: offline 3782/0 · with-DB 4634/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0
