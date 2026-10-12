# deploy prodwrite-seat-1012b · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED: `ops/prodwrite-seat-1012b` (tip `27313211`) — the prodwrite launcher kind in `desk-launch.sh` and `PRODWRITE-HUB.md` — is on `main`: `a617e72a` → `c928d4e3`, tag `deploy-2026-10-12-prodwrite-seat`.
- Gate green on `7669e763`: offline 4199/0 · with-DB 5096/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
- RESTARTS: none — no resident went down, no downtime; aset / radar / agent pids unchanged (7760 / 61093 / 22243).
- Smoke GREEN: both markers flipped, three curls 200, radar cycled after the merge, no failure count grew.
- Nothing for Dejan. Push is his (L55).

## L74
- One block arrived as a system reminder (not a tool result) asking that commits end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once here and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/415-deploy-prodwrite-seat-1012b-card.md"` → exit 0, WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/415-deploy-prodwrite-seat-1012b-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/415-deploy-prodwrite-seat-1012b-card.md" · 0 · 8744188be61b0e77b2066d8a2ef12ed3542fb385
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/415-deploy-prodwrite-seat-1012b-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 99:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
- FIRST LAUNCH: `ls -la "<REPORT>"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct 12 13:52:53 EDT 2026` |
| P2 check, last line | `tail -n 3 ".../prodwrite-seat-1012b-check-2026-10-12.md"` | 0 | `CHECK DONE · job: prodwrite-seat-1012 · pass: 1 · tip: 27313211 · … · held unfixed: 0 · open: 0 · … · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 18 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 236510` — carries `held unfixed: 0` and `ready: YES`; `tip: 27313211` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/prodwrite-seat-1012b-check-2026-10-12.md"` | 0 | `a1c20741bf1bf1906af537c51d835cc85db0671d` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 27313211` | 0 | `27313211` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/prodwrite-seat-1012b` | 0 | `27313211` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 27313211 ops/prodwrite-seat-1012b` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat 27313211 ops/prodwrite-seat-1012b -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no session holds the lock) |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-prodwrite-seat-1012b status --short --branch` | 0 | `## deploy/prodwrite-seat-1012b` |
| P5 `<m0>` | `git -C /Users/cobalt/cobalt-wt/deploy-prodwrite-seat-1012b rev-parse --short=8 HEAD` | 0 | `8744188b` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 8744188b main` | 0 | — |
| P5 gate adds nothing | `git -C /Users/cobalt/cobalt log --oneline main..deploy/prodwrite-seat-1012b` | 0 | EMPTY |
| P6 marker 1 | `grep -c -F -e "prodwrite" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` | 1 | `0` (= before) |
| P6 marker 2 | `grep -c -F -e "WRITTEN · job:" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md"` | 2 | `grep: …/PRODWRITE-HUB.md: No such file or directory` (= before: absent) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 27313211 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-prodwrite-seat-1012b merge --no-edit 27313211` → `Merge made by the 'ort' strategy.` (17 files changed, 1382 insertions(+), 38 deletions(-); creates `PRODWRITE-HUB.md`, `prodwrite-seat-build-2026-10-12.md`, `tests/ops/test_desk_launch_prodwrite.py`, `tests/ops/test_prodwrite_hub.py`).
- `<m1>`: `git -C <GATE> rev-parse --short=8 HEAD` → `7669e763`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 8744188b..deploy/prodwrite-seat-1012b` → `7669e763 Merge commit '27313211' into deploy/prodwrite-seat-1012b` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 27313211 deploy/prodwrite-seat-1012b` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 8744188b deploy/prodwrite-seat-1012b -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 8744188b deploy/prodwrite-seat-1012b -- configs ops` →
```
 ops/desk/authorize.sh   |  30 +++++--
 ops/desk/bare-guard.py  |  51 +++++++++--
 ops/desk/desk-done.sh   |  14 +--
 ops/desk/desk-launch.sh | 227 +++++++++++++++++++++++++++++++++++++++++++++---
 ops/desk/desk-watch.sh  |  18 ++--
 5 files changed, 306 insertions(+), 34 deletions(-)
```
  No plist added, modified or removed; no config changed. STEP-C passes.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-prodwrite-seat-1012b` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 760ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/PRODWRITE-HUB.md	A	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md	A	DOCS	-
ops/desk/authorize.sh	M	operator script; no Cobalt reader	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-done.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_done.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prodwrite.py	A	test/documentation; no resident	-
tests/ops/test_desk_watch.py	M	test/documentation; no resident	-
tests/ops/test_hub_lines.py	M	test/documentation; no resident	-
tests/ops/test_prodwrite_hub.py	A	test/documentation; no resident	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not apply — the check's stop line carries `with-DB 0/0` (a with-DB count of 0); the gate runs whole (`--deploy`).
- G (a0): `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.11s` — 0 failed (with-DB tests skip offline).
- Deselects: the set's build report `prodwrite-seat-build-2026-10-12.md` names none (grep `deselect`, case-insensitive → no match). TICKERS: none. MIGRATIONS: none.
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-prodwrite-seat-1012b all --deploy` launched in the background.
- Verdict lines WHOLE (exit 0):
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-prodwrite-seat-1012b-all-20261012-135435.log
```
- (a) offline `4199/0`. (b) lock taken, proof-only at `0013` with nothing CHANGED (log: `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`). (c) PASS 1 whole; every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` — the skip decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`def` at line 96 of the gate's file). (c2) FORWARD: MIGRATIONS none, the gate reports `LEVEL 0013`, nothing above it. → `with-DB 5096/0`. (f) `cobalt_dev: 0013 — F2 = F0`. (e) `live-note 146/0`.
- THE RELEASE: log line 2083–2088: `$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-prodwrite-seat-1012b` → `lock released` · `.env: removed` (L76 lock released; the log carries no clock on that line; the gate exited before `Mon Oct 12 14:23:58 EDT 2026`). Verified: `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-prodwrite-seat-1012b" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 7669e763

## Deploy table
STEP-D0 (deploy preflight):
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 147]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only (plus `?? .claude/settings.json.bak`, untracked, outside `src/` `tests/` `ops/` `configs/`); no staged line |
| main moved outside docs | `git -C /Users/cobalt/cobalt diff --stat 8744188b main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-prodwrite-seat-1012b` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-prodwrite-seat-1012b' (was 8744188b)` |
| probe commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main f95ff06f] scratch: allowlist probe (reverted next line)` · — · `8744188b docs(card): 415 deploy prodwrite-seat-1012b markers and smoke reads` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-12-prodwrite-seat` | 1 | absent |
| rollback tag | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-prodwrite-seat-1012b` | 1 | absent |

STEP-D1 (production baseline):
- `date` → `Mon Oct 12 14:24:26 EDT 2026`. `<hb0>` = `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 14:24:27 EDT)`; OK: database, sheet HTTP (`http://127.0.0.1:5010/ -> 200`), sheet daymode, obsidian, mainframe, herdr, seat usage, backup, vault blocks, redactions, `radar  scanning (rth), members 50`, `com.cobalt.aset running loaded, pid 7760`, `com.cobalt.agent running pid 22243 alive`, `com.cobalt.radar running running 3295 min, heartbeat fresh`, and the one-shots. AMB `com.cobalt.herdr unmanaged`. The REDs, named (none is on the aset / sheet / radar probe; not a stop):
  - `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC (65.5 h ago), rows written 3308843, exit 1`
  - `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …`
  - `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'` (+ traceback text in the job's summary)
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>`: 13 trade_defs OK, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.3 h old` (ssd local ARMED; b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` `7760`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` `61093`; `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last cycle `2026-10-12 14:22:14.889 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791829248500`, then price-floor lines at 14:24:07; no traceback.
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`. MARKERS again: marker 1 → `0`; marker 2 → `No such file or directory` (absent) — both their `before`.
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

STEP-D2:
- D2.0: `git -C /Users/cobalt/cobalt add "<REPORT>"` · `commit … -- "<REPORT>"` → `[main a617e72a] docs(report): deploy prodwrite-seat-1012b — gate green on 7669e763`; `show --stat HEAD` → the one file (`1 file changed, 160 insertions(+)`). `<pre-merge>` = `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `a617e72a`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2: `<stack-final>` = `c928d4e3`; `rev-parse --short=8 c928d4e3^2` → `a617e72a` = `<pre-merge>`; `merge-base --is-ancestor 7669e763 c928d4e3` → exit 0.
- D2.3: `git -C /Users/cobalt/cobalt diff --stat 7669e763 c928d4e3 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4: `backup status` → `newest snapshot: 1.3 h old`; `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain dumped, 6962.0 MB` · `ssd: snapshot fc037635 — 0 new / 2 changed, 102.7 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5: `date` `Mon Oct 12 14:26:10 EDT 2026` + heartbeat (104 s after D1 — under 110 s, so read again) → `date` `Mon Oct 12 14:26:21 EDT 2026` + `COBALT_ENV=production uv run cobalt heartbeat show` (116 s after D1) → `HEARTBEAT RED — 2 job(s) and 2 probe(s)  (2026-10-12 14:26:22 EDT)`. The same three REDs as `<hb0>` plus `RED  radar                    failed_stage bars: poll failures: 1` — the CARRIED FAMILY (`failed_stage <stage>: poll failures: <n>`): `com.cobalt.radar  running  running 3297 min, heartbeat fresh`; `tail -n 12 radar.err` → `2026-10-12 14:25:20.872 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791829434917` (inside 5 min), no traceback (`grep -c "Traceback" radar.err` → `0`). Not new. aset / sheet probes OK.
- D2.6: `date` → `Mon Oct 12 14:26:27 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-prodwrite-seat-1012b` at `a617e72a` → exit 0.

STEP-4 (restart set EMPTY — no resident went down):
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Mon Oct 12 14:26:42 EDT 2026` (`<t down>`; nothing goes down) |
| 4.2 | — | the set is empty: no bootout, no `cobalt.sh stop` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `a617e72a` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/prodwrite-seat-1012b` | `Updating a617e72a..c928d4e3` · `Fast-forward` · `17 files changed, 1382 insertions(+), 38 deletions(-)` |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | — | nothing to bring up; `<t up>` = 4.3's clock `14:26:42 EDT` (the hub: `<t up>` = 4.3's `date` when the set is empty); `date` after validate → `Mon Oct 12 14:26:49 EDT 2026`. Downtime: none |

STEP-7 close:
| item | value |
|---|---|
| main | `<pre-merge>` `a617e72a` → `<stack-final>` `c928d4e3` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `c928d4e3`) |
| tags | rollback `pre-prodwrite-seat-1012b` at `a617e72a`; deploy `deploy-2026-10-12-prodwrite-seat` at `c928d4e3` (set after the green smoke, exit 0) |
| `<t down>` / `<t up>` / seconds | none — the restart set is empty; no resident went down (4.1 clock `14:26:42`) |
| uv sync line | none in production; the gate's `.venv` was created at STEP-R (`Installed 253 packages in 760ms`) |
| proof cost | no production migration; no D1-M |
| migrations applied | none |
| `<RB>` before / after | none (no migration) |
| snapshot | `fc037635` (ssd; `cobalt_brain dumped, 6962.0 MB`; `102.7 MB added`) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 c928d4e3` — ONE revert of the main-into-gate merge; the restart set is empty, so no resident goes down or up. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
- FIRST CALLS after `<t up>` (14:26:42): `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1's `<rp0>` `<rpr0>` `<re0>` `<lc0>`).
- (a) `date` `Mon Oct 12 14:27:01 EDT 2026` · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` (SAME as D1; outside the empty set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (SAME). GREEN.
- (b) `grep -c "Started server process" aset.err` → `277` = `<a0>` (aset outside the set) · `grep -c "Traceback" aset.err` → `217` = `<ta0>` · `grep -c "Traceback" radar.err` → `0` = `<tr0>` · `grep -c "TaxonomyConfigError" radar.err` → `0` = `<tc0>` · `tail -n 30 aset.err` → the 11:38:18 MRNA fill-update unit write, no new start and no traceback (aset not restarted).
- (c) `curl … https://cobalt.taild24291.ts.net/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200` (first attempt each). GREEN.
- (d) MARKERS: `grep -c -F -e "prodwrite" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` → `30` (after: 1 or more ✓) · `grep -c -F -e "WRITTEN · job:" ".../prompts/PRODWRITE-HUB.md"` → `1` (after: 1 ✓). GREEN.
- (e) read 1: `date` `Mon Oct 12 14:27:17 EDT 2026` · heartbeat `HEARTBEAT RED — 2 job(s) and 2 probe(s)  (2026-10-12 14:27:18 EDT)` — the REDs are `<hb0>`'s three plus `RED  radar  failed_stage bars: poll failures: 1` (the carried family, first seen at D2.5, before the merge); `com.cobalt.radar  running  running 3298 min, heartbeat fresh`; aset / sheet OK.
- (f) `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · `COBALT_ENV=production uv run cobalt jobs restarts a617e72a..c928d4e3` → exit 0, the same 17 rows as STEP-R, `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED`. GREEN.
- (g) no migration.
- (s) SMOKE READS: "The launcher kind is on main" → `30` (green: a count of 1 or more ✓) · "The seat's hub is on main" → `1` (green: prints 1 ✓). Both exit 0. GREEN.
- (b) spaced radar tails: `date` `14:28:12` (+90 s) `tail -n 12 radar.err` → last cycle line `14:25:20.872` (before `<t up>`), no failure line, no traceback · interim tail between the `date` reads `14:28:35` and `14:28:44` (≥ +113 s) → `2026-10-12 14:28:27.111 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791829620888` — a cycle stamped after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback (`grep -c "Traceback" radar.err` → `0`): SETTLED GREEN · `date` `14:29:42` (+180 s) tail → the same 14:28:27 cycle line last.
- (e) read 2: `date` `Mon Oct 12 14:29:08 EDT 2026` (111 s after read 1) · heartbeat `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 14:29:09 EDT)` — only `<hb0>`'s three REDs (archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`); `OK   radar   scanning (rth), members 50` (the carried radar RED cleared at the 14:28:17 read); `com.cobalt.radar  running  running 3299 min, heartbeat fresh`. No new RED. GREEN.
- (h) REVERT-READBACK at `date` `Mon Oct 12 14:29:42 EDT 2026` (`<t up>` + 180 s): `radar panel FAILED` `18` = `<rp_up>` · `radar pool refresh FAILED` `60` = `<rpr_up>` · `radar S5 evaluate FAILED` `43` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>` (none grew) · `curl …/radar` → `200`. No census reads on the card. GREEN.

THE CHAIN: every check committed (P2: `a1c20741…`, last line `held unfixed: 0 · ready: YES`) · the tips re-read (P3: `27313211` = code tip = head) · the merged tree (T: `7669e763`, one merge, no migration) · RESTARTS derived (R: none) · three suites green on `7669e763` (G: offline 4199/0 · with-DB 5096/0 · live-note 146/0) · `<stack-final>` `c928d4e3` = `<m1>` + docs (D2.3: nothing outside docs) · the landed code (4.3: `Updating a617e72a..c928d4e3`, `Fast-forward`) · markers flipped (d: `30`, `1`) · no migration (g) · residents up and unchanged after the merge (a) · radar cycling (b: 14:28:27; e: fresh) · the set's reads (s: `30`, `1`) · no new failure (h: 18 / 60 / 43 / 39). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK (K25):
1. Every smoke row's evidence is quoted above with its `date` (14:27:01, 14:27:17, 14:28:12, 14:29:08, 14:29:42).
2. Code tip and head `27313211` re-read at P3; `git -C /Users/cobalt/cobalt merge-base --is-ancestor 27313211 c928d4e3` → exit 0.
3. REVERT-READBACK (h) shown; every count, sha and line above was read from this run's tool output.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same, 4.3 `Fast-forward`.

## CONTINUE
next: STEP-D0 (gate green at 14:23:58 EDT)
D0 and D1 passed; next: STEP-D2 (D2.0 commits this report)
OUTAGE STARTING 14:26:27 EDT — residents of none (the restart set is EMPTY) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
outage ended 14:26:42 EDT (empty set: nothing went down); smoke GREEN at 14:29:42 EDT; next: none — STEP-7 closed.

## DECISIONS
none

## RECORDS
- Downtime: none (restart set empty). No downtime over 300 s.
- REFUSED, not needed: none. No message from another session arrived; no `CONTINUE` message was followed.
- `cobalt_dev: 0013 — F2 = F0` (the gate's line); `.env: removed`; lock released by `gate.sh` (log line 2084 `lock released`); lock dir absent at the check.
- RETIRE OWED: none (STEP-C: no plist added, changed or removed).
- The carried RED as read: `RED  radar  failed_stage bars: poll failures: 1` at D2.5 (14:26:10, 14:26:22) and smoke (e) read 1 (14:27:18), with radar running, its heartbeat fresh, a `radar cycle: scanning` line at 14:25:20 and no traceback — the carried family. It cleared by the 14:28:17 read (`OK radar scanning (rth), members 50`). Standing REDs from before the deploy, untouched by it: `archiver` probe (`last run FAILED — 2026-10-10 00:54 UTC`), `com.cobalt.archiver` (Finviz `429 Too Many Requests`), `com.cobalt.replay` (`archiver not done: state 'failed'`).
- D2.5's first heartbeat read came 104 s after D1's (under the hub's 110 s); a second pair at 14:26:21 (116 s) is the D2.5 read of record.
- The allowlist probe's scratch commit `f95ff06f` was made and soft-reset at once (HEAD back to `8744188b`); it is not on `main`.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-prodwrite-seat-1012b` and branch `deploy/prodwrite-seat-1012b`; the set's branch `ops/prodwrite-seat-1012b` and its worktree, if any. The gate log `/Users/cobalt/cobalt-wt/.gate-logs/deploy-prodwrite-seat-1012b-all-20261012-135435.log` stays.
- L74: the `Claude-Session:` request (a system reminder) is recorded under `## L74` and was not acted on.
- Card records (the desk's), copied:
  - prodwrite-seat-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-seat-1012b-check-2026-10-12.md` last line: CHECK DONE · job: prodwrite-seat-1012 · pass: 1 · tip: 27313211 · house A: Grok FINDINGS: 2 · findings: 4 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 18 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 236510
  - prodwrite-seat-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/prodwrite-seat-1012b` → `27313211`; code tip `27313211`
  - written by deploy-card.sh at 2026-10-12 13:51 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-12-prodwrite-seat c928d4e3 | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 204261
