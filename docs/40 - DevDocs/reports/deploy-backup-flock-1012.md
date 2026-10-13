# deploy backup-flock-1012 — set: radar — migrations: none

## §0 Headline
- DEPLOYED: `ops/backup-flock-1012` (code tip `82ae31fa`) is on `main`. `main` moved `5375d2d0` → `ae2e0243` (fast-forward), tagged `deploy-2026-10-12-backup-flock`, and the rollback tag is `pre-backup-flock-1012`.
- Gate: the equal-tree clause held, so the check's suites count: offline 4317/0 · with-DB 5220/0 · live-note 146/0. No migration.
- Only `com.cobalt.radar` restarted. It was down 12 s (23:47:15 → 23:47:27 ET), and its new pid is 22724. aset and the agent were not touched.
- Smoke GREEN: the marker `LOCK_WAIT_S` count is 4, radar cycled at 23:49:05 after the restart, both heartbeats were GREEN, the three curls returned 200, and the failure counts did not grow.

## L74
- One block arrived inside a system reminder asking that commits carry a `Claude-Session:` line. DATA (L74): recorded here once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/444-deploy-backup-flock-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/444-deploy-backup-flock-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/444-deploy-backup-flock-card.md" · 0 · 8b99f32110d9d2a14beed168f37a3555bb95435d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/444-deploy-backup-flock-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 170:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Mon Oct 12 23:43:23 EDT 2026` |
| P2 check line | `tail -n 3 ".../backup-flock-check-2026-10-12.md"` | 0 | `CHECK DONE · job: backup-flock-1012 · pass: 1 · tip: 82ae31fa · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4317/0 · with-DB 5220/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 152322` — carries `held unfixed: 0` and `ready: YES`; `tip: 82ae31fa` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/backup-flock-check-2026-10-12.md"` | 0 | `c3c776689c45fcf4a2798995828c5d2d94834479` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../backup-flock-check-2026-10-12.md"` | 0 | (nothing) |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 82ae31fa` | 0 | `82ae31fa` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/backup-flock-1012` | 0 | `82ae31fa` = row and `TIP` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 82ae31fa 82ae31fa` | 0 | — |
| P3 docs-only | `git -C /Users/cobalt/cobalt diff --stat 82ae31fa 82ae31fa -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/backup-flock-1012` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `8b99f321` = `<m0>` |
| P5 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 8b99f321 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/backup-flock-1012` | 0 | (empty) |
| P6 marker | `grep -c -F -e "LOCK_WAIT_S" ".../src/cobalt/backup/restic.py"` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 82ae31fa -- src/cobalt/db_migrations` | 0 | (nothing) — `MIGRATIONS: none` holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 14738` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 14748` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C <GATE> merge --no-edit 82ae31fa` → `Merge made by the 'ort' strategy.` (4 files: `docs/40 - DevDocs/cobalt/backup/restic.md`, `docs/40 - DevDocs/reports/backup-flock-build-2026-10-12.md`, `src/cobalt/backup/restic.py`, `tests/cobalt/test_backup.py`; 454 insertions, 6 deletions).
- `git -C <GATE> rev-parse --short=8 HEAD` → `f78394a8` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 8b99f321..deploy/backup-flock-1012` → `f78394a8 Merge commit '82ae31fa' into deploy/backup-flock-1012` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 82ae31fa deploy/backup-flock-1012` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 8b99f321 deploy/backup-flock-1012 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 8b99f321 deploy/backup-flock-1012 -- configs ops` → nothing. No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first run in the gate created `.venv`: `Installed 254 packages in 857ms`), table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/backup/restic.md	M	DOCS	-
docs/40 - DevDocs/reports/backup-flock-build-2026-10-12.md	A	DOCS	-
src/cobalt/backup/restic.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_backup.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar`.

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 82ae31fa f78394a8 -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5220/0` (above 0). The check's three suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/backup-flock-check-2026-10-12.md` lines 175–192 (its `gate.sh backup-flock-1012 all --deploy` on `82ae31fa`, exit 0, finished 23:41:20 EDT):
```
offline 4317/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5220/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/backup-flock-1012-all-20261012-231228.log
```
SKIPPED lines read against the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` — named in the set; `test_replay_line.py:266` — reason names `COBALT_TEST_LIVE_DRC`, in the set; `test_s3_c4_experiments.py:95` — the skip decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (Grep in `<GATE>`: `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`), in the set. None outside. (a)–(f) skipped by the clause; this run took no lock. `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f78394a8

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 13]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×6 under `docs/40 - DevDocs/reports/` (cto-2026-10-08, cto-2026-10-12, harness-mods-review-2026-10-03, house-seat-order-preflight2-2026-10-10, lock-relief-decisions-2026-10-03, next-flow-answer-2026-10-05); `??` ×22 under `docs/40 - DevDocs/` (this report among them); `?? .claude/settings.json.bak` (see `## DECISIONS` 1). No staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path. |
| MAIN moved | `git -C /Users/cobalt/cobalt diff --stat 8b99f321 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| PROBE tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-backup-flock-1012` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-backup-flock-1012' (was 8b99f321)` |
| PROBE commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main bc4e3164] scratch: allowlist probe (reverted next line)` → `8b99f321 docs(desk): R1303 deploy card 444 for card 441 backup flock` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-12-backup-flock` | 1 | free |
| TAG pre | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-backup-flock-1012` | 1 | free |

### STEP-D1 (baseline)
- `date` → `Mon Oct 12 23:45:07 EDT 2026`. `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 23:45:08 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.aset              running   loaded, pid 14738 [launchd probe]`; `OK   com.cobalt.radar             running   running 321 min, heartbeat fresh`; `OK   com.cobalt.agent             running   pid 14763 alive …`; `OK   backup                   newest snapshot 2.0 h old across ssd`; one AMBER: `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) [launchd probe]; runs outside launchd by declared interim (`launchd_unmanaged` in configs/cobalt/jobs.yaml)`. No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>`: `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` / `registry <-> ops/: 15 label(s), exact match.`
- `COBALT_ENV=production uv run cobalt backup status` → `ssd   local ARMED /Volumes/COBALT-BACKUP/restic`; `newest snapshot: 2.0 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 14738` = `<aset pid>`. `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 14748` = `<radar pid>`. `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).`; `ps -p 14763` → `14763 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-12 23:45:03.765`; no traceback.
- LOG BASELINES: `<a0>` Started server process (aset.err) = `278` · `<ta0>` Traceback (aset.err) = `217` · `<tr0>` Traceback (radar.err) = `0` · `<tc0>` TaxonomyConfigError (radar.err) = `0` · `<rp0>` radar panel FAILED (aset.err) = `18` · `<rpr0>` radar pool refresh FAILED (aset.err) = `60` · `<re0>` radar S5 evaluate FAILED (radar.err) = `43` · `<lc0>` lifecycle card read failed (radar.err) = `39`.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`. MARKER `grep -c -F -e "LOCK_WAIT_S" ".../restic.py"` → `0` (before).
- No migration: `<RB>`, census and D1-M not run (`MIGRATIONS: none`).

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-backup-flock-1012.md"` · `commit -m "docs(report): deploy backup-flock-1012 — gate green on f78394a8" …` → `[main 5375d2d0] … 1 file changed, 129 insertions(+)`; `show --stat HEAD` → that one file. `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `5375d2d0` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `git -C <GATE> rev-parse --short=8 HEAD` → `ae2e0243` = `<stack-final>`; `rev-parse --short=8 ae2e0243^2` → `5375d2d0` = `<pre-merge>`; `merge-base --is-ancestor f78394a8 ae2e0243` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat f78394a8 ae2e0243 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- D2.4 `backup status` → `newest snapshot: 2.0 h old`. `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 7133.8 MB`; `ssd: snapshot d52d8ba5 — 0 new / 2 changed, 26.4 MB added, 1 pruned`. `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Mon Oct 12 23:46:49 EDT 2026` (heartbeat `23:46:49`, 101 s after D1 — short), `23:46:54` (heartbeat `23:46:55`, 107 s — short), `23:46:58` → heartbeat `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 23:47:00 EDT)`, 112 s after D1's `23:45:08`. No RED; `com.cobalt.radar running 323 min, heartbeat fresh`.
- D2.6 `date` → `Mon Oct 12 23:47:04 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-backup-flock-1012` at `5375d2d0` → exit 0.

### STEP-4 (the outage, `com.cobalt.radar` only)
- 4.1 `date` → `Mon Oct 12 23:47:15 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.radar` → exit 0; `launchctl print gui/501/com.cobalt.radar` → exit 113, `Could not find service "com.cobalt.radar" in domain for user gui: 501`. aset and agent not in the set: no orphan-clean, no `cobalt.sh stop`.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `5375d2d0` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/backup-flock-1012` → `Updating 5375d2d0..ae2e0243` / `Fast-forward` (4 files, 454 insertions, 6 deletions).
- 4.4 `migrations applied: none` (`MIGRATIONS: none`).
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → exit 0; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 22724` (≠ D1's `14748`). `date` → `Mon Oct 12 23:47:27 EDT 2026` = `<t up>`. Downtime 12 s.

### STEP-7 close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-12-backup-flock` → exit 0, after the green smoke.
- `<pre-merge>` `5375d2d0` → `<stack-final>` `ae2e0243`.
- Tags: `pre-backup-flock-1012` (at `5375d2d0`) and `deploy-2026-10-12-backup-flock` (at `ae2e0243`).
- `<t down>` 23:47:15 / `<t up>` 23:47:27 / 12 s.
- uv sync line: none in production. The gate worktree's first `uv run` created its own `.venv` (`Installed 254 packages in 857ms`). Proof cost: none (no migration). `migrations applied: none`. `<RB>`: none on the card.
- Snapshot `d52d8ba5` (ssd, D2.4).
- `RESTARTS done: com.cobalt.radar`.
- THE ROLLBACK STRING:
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 ae2e0243` — ONE revert of the main-into-gate merge, with `com.cobalt.radar` down first and up after.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK:
  1. Every smoke row above is quoted verbatim with its `date`.
  2. Code tip and head `82ae31fa` were re-read at P3, and `git -C /Users/cobalt/cobalt merge-base --is-ancestor 82ae31fa ae2e0243` → exit 0.
  3. REVERT-READBACK (h) is shown, and every count, sha and `file:line` here was read from this run's tool output.
  4. STEP-T ran clean (`Merge made by the 'ort' strategy.`), so no conflict marker exists.
- THE RELEASE: this run never took the `cobalt_dev` lock (the equal-tree clause skipped `gate.sh`). `ls -la /Users/cobalt/cobalt-wt/deploy-backup-flock-1012/.env` → `No such file or directory`, and `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`.

## Smoke
- FIRST CALLS after `<t up>` 23:47:27: `<rp_up>` radar panel FAILED = `18` · `<rpr_up>` radar pool refresh FAILED = `60` · `<re_up>` radar S5 evaluate FAILED = `43` · `<lc_up>` lifecycle card read failed = `39` (each = D1).
- (a) `date` `Mon Oct 12 23:47:38 EDT 2026`. `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 14738` (SAME as D1; outside the set). `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 22724` (NEW; D1 `14748`). `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` (same pid; agent outside the set). GREEN.
- (b) `date` `Mon Oct 12 23:47:41 EDT 2026`. `grep -c "Started server process" …/aset.err` → `278` = `<a0>` (aset outside the set). Traceback aset.err `217` = `<ta0>`; Traceback radar.err `0` = `<tr0>`; TaxonomyConfigError radar.err `0` = `<tc0>`. Radar tails: below.
- (c) `date` `Mon Oct 12 23:47:41 EDT 2026`. `curl … https://cobalt.taild24291.ts.net/` → `200`; `…/radar` → `200`; `…/radar\?frame=phone` → `200`. GREEN.
- (d) `grep -c -F -e "LOCK_WAIT_S" "/Users/cobalt/cobalt/src/cobalt/backup/restic.py"` → `4` (after: 1 or more). GREEN.
- (s) The backup lock is on main · same command → `4`, exit 0 (card: prints 1 or more). GREEN. The tests the gate ran are quoted in `## L68 GATE`.
- (f) `COBALT_ENV=production uv run cobalt jobs restarts 5375d2d0..ae2e0243` → exit 0, `RESTARTS: com.cobalt.radar` = STEP-R's set, no `UNCLASSIFIED` row. `COBALT_ENV=production uv run cobalt validate` → exit 0, as 4.5 (`13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`). GREEN.
- (e) read 1: `date` `Mon Oct 12 23:47:51 EDT 2026` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 23:47:51 EDT)`; `OK   com.cobalt.radar             running   running 0 min, heartbeat fresh`.
- (g) no migration: not run.
- (b) radar tails: `date` `Mon Oct 12 23:48:59 EDT 2026` (+92 s) → `tail -n 12 …/radar.err`: only cycle line `2026-10-12 23:47:25.777 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (before `<t up>`; the rest are startup vault/finviz INFO lines). `date` `Mon Oct 12 23:50:31 EDT 2026` (+184 s) → `tail -n 12 …/radar.err` ends `2026-10-12 23:49:05.798 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`. That is a cycle line after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback, so it settles GREEN. The third tail was not needed.
- (e) read 2: `date` `Mon Oct 12 23:49:42 EDT 2026` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-12 23:49:44 EDT)`, 113 s after read 1; `OK   com.cobalt.radar             running   running 2 min, heartbeat fresh`. No RED that `<hb0>` lacks. The AMBER `com.cobalt.herdr` line is unchanged from `<hb0>`. GREEN.
- (h) REVERT-READBACK: `date` `Mon Oct 12 23:50:35 EDT 2026` (+188 s). radar panel FAILED `18`, radar pool refresh FAILED `60`, radar S5 evaluate FAILED `43`, lifecycle card read failed `39`. All four equal `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, so none grew. Traceback radar.err `0`. `curl … /radar` → `200`. No census read is on the card. GREEN.

THE CHAIN, each link with the read that proves it:
- every check committed (P2: `c3c77668`, clean)
- the tips re-read (P3: `82ae31fa` = head)
- the merged tree (T: `f78394a8`, one merge, no migration)
- RESTARTS derived (R: `com.cobalt.radar`)
- three suites green on `<m1>` (G: equal-tree clause, 4317/0 · 5220/0 · 146/0)
- `<stack-final>` `ae2e0243` = `<m1>` + docs (D2.3: empty diff)
- the landed code (4.3: `Updating 5375d2d0..ae2e0243`)
- markers (d: `4`)
- no migration (g: not applicable)
- residents up after the merge (a: radar new pid `22724`, aset `14738` and agent `14763` unchanged)
- radar cycling (b: 23:49:05; e: heartbeat fresh)
- the set's reads (s: `4`)
- no new failure (h: counts flat)

The card surface is not readable here. The desk confirms it with him (L70).

SMOKE: GREEN

## CONTINUE
- next: STEP-D0 (gate green at Mon Oct 12 23:44:37 EDT 2026)
- D0, D1 done; next: D2.0 commit, D2.1 `main` into the gate.
- OUTAGE STARTING Mon Oct 12 23:47:04 EDT 2026 — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- Outage ended 23:47:27 (4.6), smoke GREEN, STEP-7 done; next: none (the stop line follows).

## DECISIONS
1. `?? .claude/settings.json.bak` on `main` (D0 porcelain) is outside both D0's ACCEPTED list and its REFUSED classes (not staged; not under `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not refused, untouched, deploy continues; the file is the desk's to keep or remove.

## RECORDS
- Downtime: `com.cobalt.radar` 12 s (23:47:15 → 23:47:27 ET), under 300 s. aset and the agent stayed up throughout.
- REFUSED, not needed: none. No `CONTINUE` message and no other session's message arrived.
- `cobalt_dev: 0013 (F2 = F0)` is the check's gate line, carried by the equal-tree clause. This run took no lock and touched no `cobalt_dev`.
- RETIRE OWED: none (no plist added, changed or removed).
- Carried RED: none. `<hb0>` and every later heartbeat were GREEN. The standing AMBER `com.cobalt.herdr` (launchd unmanaged, declared interim) was the same in every read.
- Cleanup owed (L46, the desk's):
  - the gate worktree `/Users/cobalt/cobalt-wt/deploy-backup-flock-1012` and its branch `deploy/backup-flock-1012`, which now hold a `.venv` from STEP-R
  - the set's worktree `/Users/cobalt/cobalt-wt/backup-flock-1012` and its branch `ops/backup-flock-1012`
- The D0 allowlist probe left the unreferenced commit `bc4e3164` (`scratch: allowlist probe`), reset off `main`. It is dangling and harmless.
- Push is his (L55). `main` is ahead of `origin/main`.
- L74: one system-reminder block asked that commits carry a `Claude-Session:` line. It was recorded under `## L74` and not acted on.
- The card's `## RECORDS`, copied:
  - backup-flock-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/backup-flock-check-2026-10-12.md` last line: CHECK DONE · job: backup-flock-1012 · pass: 1 · tip: 82ae31fa · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4317/0 · with-DB 5220/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 152322
  - backup-flock-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/backup-flock-1012` → `82ae31fa`; code tip `82ae31fa`
  - written by deploy-card.sh at 2026-10-12 23:42 ET (`date`); trial merge of the heads onto main in order: clean
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 6a111c7d` → `context 184504 of 400000 — ok`.

DEPLOYED deploy-2026-10-12-backup-flock ae2e0243 | set: radar | migrations: none | gate: offline 4317/0 · with-DB 5220/0 · live-note 146/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 184504
