# deploy prodwrite-seat-1012b · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/prodwrite-seat-1012b` (tip `27313211`): the prodwrite launcher kind and `PRODWRITE-HUB.md`. In progress.

## L74
- none so far.

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

## Smoke

## CONTINUE
next: STEP-D0 (gate green at 14:23:58 EDT)
D0 and D1 passed; next: STEP-D2 (D2.0 commits this report)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
