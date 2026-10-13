# deploy backup-flock-1012 — set: radar — migrations: none

## §0 Headline
- Deploy of `ops/backup-flock-1012` (code tip `82ae31fa`) onto `main` via gate `deploy/backup-flock-1012`. In progress.

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

## Smoke

## CONTINUE
- next: STEP-D0 (gate green at Mon Oct 12 23:44:37 EDT 2026)
- D0, D1 done; next: D2.0 commit, D2.1 `main` into the gate.

## DECISIONS
1. `?? .claude/settings.json.bak` on `main` (D0 porcelain) is outside both D0's ACCEPTED list and its REFUSED classes (not staged; not under `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not refused, untouched, deploy continues; the file is the desk's to keep or remove.

## RECORDS

(run in progress — next step under ## CONTINUE)
