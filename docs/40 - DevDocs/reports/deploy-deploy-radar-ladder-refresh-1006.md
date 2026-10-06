# deploy-radar-ladder-refresh-1006 · SET: none · MIGRATIONS: none

## §0 Headline
Shipped: the radar ladder refresh (card 54, his R556) is live on `main` at `9e70c702`, tagged `deploy-2026-10-06-radar-ladder-refresh`. The pool timer now also refreshes the ladder through `tickLadder`.
aset and radar restarted with 20 s down (18:44:39 → 18:44:59 EDT). No migration. The gate stands on the check's suites by the EQUAL-TREE CLAUSE: offline 3963/0 · with-DB 4847/0 · live-note 146/0.
Smoke GREEN on every row, and the four failure counts did not grow. The one heartbeat RED (`com.cobalt.generated`) was there before the deploy and was not caused by it. It names an earlier hub: see ## RECORDS.
Rollback tag `pre-deploy-radar-ladder-refresh-1006` = `d1c40084`. The desk still owes: the live-proof read in `aset.log` (his browser), cleanup, and the push (his).

## L74
One block asked for a `Claude-Session:` trailer on commits. It came as a session attribution reminder, not inside a tool result. It is recorded here once and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74). No other instruction-shaped block came inside a tool result.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md"` at Tue Oct  6 18:40:28 EDT 2026 → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md" · 0 · bb9c010cae1521879b53cc4efc8f39c47752b3e4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/60-deploy-ladder-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R556 row · grep -n "^| R556 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 110:| R556 | 14:20 ET | HIS RULING ([words](cto-2026-10-06-words.md) `## R556`): fix the empty radar screen if the brain says GO (bandwidth, no blocker); desk asked the brain 14:20; on GO the desk launches the fix flow, no further ask to him. | HIS RULING · APPROVED |
RULING 2026-10-06 R556 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R556 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 8bceed0a20d4157786a85a2f0e44a76a1ff2bf30
RULING 2026-10-06 R556 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

First launch: `ls -la` of this report → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (## AUTHORIZATION) |
| P1 DATE | `date` | 0 | `Tue Oct  6 18:40:28 EDT 2026` (no window binds, L43) |
| P2 tail | `tail -n 3 ".../radar-ladder-refresh-check-2026-10-06.md"` | 0 | `CHECK DONE · job: radar-ladder-refresh · pass: 1 · tip: ed19060f · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181164` — both literals present, `tip: ed19060f` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "<check report>"` | 0 | `02b15e1f07a9f44bb7885b680db0f3e91abc5fda` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check report>"` | 0 | (nothing) |
| P3 code tip | `rev-parse --short=8 ed19060f` | 0 | `ed19060f` |
| P3 head | `rev-parse --short=8 ops/radar-ladder-refresh-1006` | 0 | `ed19060f` (= TIP) |
| P3 ancestor | `merge-base --is-ancestor ed19060f ed19060f` | 0 | — |
| P3 diff | `diff --stat ed19060f ed19060f -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` (no session holds the lock) |
| P5 status | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-radar-ladder-refresh-1006` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `e177280b` = `<m0>` |
| P5 ancestor | `merge-base --is-ancestor e177280b main` | 0 | — |
| P5 empty | `log --oneline main..deploy/deploy-radar-ladder-refresh-1006` | 0 | (empty) |
| P6 marker 1 | `grep -c -F "tickLadder" .../radar_panel.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "window.setInterval(tickLadder,interval)" ...` | 1 | `0` = before |
| P6 marker 3 | `grep -c -F "window.setInterval(refreshPool,interval)" ...` | 0 | `1` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main ed19060f -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 83925` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 83936` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit ed19060f` → `Merge made by the 'ort' strategy.` (4 files, 483 insertions, 2 deletions; no conflict).
- `git -C <GATE> rev-parse --short=8 HEAD` → `46a587c9` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent e177280b..deploy/deploy-radar-ladder-refresh-1006` → `46a587c9 Merge commit 'ed19060f' into deploy/deploy-radar-ladder-refresh-1006` (one line, one head).
- `merge-base --is-ancestor ed19060f deploy/deploy-radar-ladder-refresh-1006` → exit 0.
- `diff --stat e177280b deploy/deploy-radar-ladder-refresh-1006 -- src/cobalt/db_migrations` → (nothing): no migration path, MIGRATIONS: none.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat e177280b deploy/deploy-radar-ladder-refresh-1006 -- configs ops` → (nothing): no plist added, modified or removed; no RETIRE OWED.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a first-run `uv` venv build in the gate: `Installed 253 packages in 815ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (matches the card).

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat ed19060f 46a587c9 -- . ":(exclude)docs"` → (nothing); the check's stop line carries `with-DB 4847/0` (> 0). The check's suite lines are the gate's; (a)–(f) skipped, no `cobalt_dev` lock taken by this run. Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-ladder-refresh-check-2026-10-06.md` lines 191–208 (its `gate.sh radar-ladder-refresh-1006 all --deploy` on tip `ed19060f`, exit 0):
```
offline 3963/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4847/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-ladder-refresh-1006-all-20261006-180724.log
```
Skips read against the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` — each in the set; `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC` — in the set; `test_s3_c4_experiments.py:95` — read in `<GATE>`: line 95 `@requires_live`, line 96 `def test_x14_live_his_template_strips_to_the_committed_fixture():` — in the set. None outside.
`cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `cobalt_dev: 0013 — F2 = F0` (the check's gate).

GATE GREEN on 46a587c9 (Tue Oct  6 18:41:50 EDT 2026) — offline 3963/0 · with-DB 4847/0 · live-note 146/0

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 222]`; `status --porcelain` → only ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/`, plus `?? .claude/settings.json.bak` (see ## DECISIONS 1); no staged line, no dirty `src/` `tests/` `ops/` `configs/` path other than `rules.yaml`.
- `git -C /Users/cobalt/cobalt diff --stat e177280b main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- ALLOWLIST PROBE: `tag scratch-allow-probe-deploy-radar-ladder-refresh-1006` → ok; `tag -d …` → `Deleted tag 'scratch-allow-probe-deploy-radar-ladder-refresh-1006' (was e177280b)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 474dc9a6] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `e177280b docs(desk): card 54 deploy preflight ready YES, deploy launching; R581` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-06-radar-ladder-refresh` → exit 1; `… refs/tags/pre-deploy-radar-ladder-refresh-1006` → exit 1.

### STEP-D1 baseline (Tue Oct  6 18:42:24 EDT 2026)
- `<hb0>` (`heartbeat show`, 18:42:25 EDT): `HEARTBEAT RED — 1 job(s)`. Every probe OK (database, sheet HTTP 200, sheet daymode, radar `scanning (aftermarket), members 50`, `com.cobalt.aset running loaded, pid 83925`, `com.cobalt.agent running pid 22243`, `com.cobalt.radar running running 277 min, heartbeat fresh`, …) except `AMB com.cobalt.herdr unmanaged` (declared interim) and `RED com.cobalt.generated failed GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`. Not an aset / sheet / radar probe: named, not a stop (## RECORDS).
- `<val0>` (`validate`): exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 4.6 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `83925`; `…/com.cobalt.radar` → `state = running`, `<radar pid>` = `83936`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 logs/radar.err` → last line `2026-10-06 18:41:20.480 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791326392928`; no traceback.
- Log baselines: `<a0>` = 46 · `<ta0>` = 2 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 17 · `<rpr0>` = 58 · `<re0>` = 40 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS again → `0` / `0` / `1` (each its before).
- No migration: `<RB>`, census and D1-M not run.

### STEP-D2
- D2.0: `git -C /Users/cobalt/cobalt commit … -- "<REPORT>"` → `[main d1c40084] docs(report): deploy deploy-radar-ladder-refresh-1006 — gate green on 46a587c9`; `show --stat HEAD` → the report alone (`1 file changed, 128 insertions(+)`). `<pre-merge>` = `d1c40084`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2: `<stack-final>` = `9e70c702`; `rev-parse --short=8 9e70c702^2` → `d1c40084` = `<pre-merge>`; `merge-base --is-ancestor 46a587c9 9e70c702` → exit 0.
- D2.3: `diff --stat 46a587c9 9e70c702 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing): docs-only.
- D2.4: `backup status` before → `newest snapshot: 4.6 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 5262.9 MB` · `ssd: snapshot 05f14987 — 0 new / 3 changed, 173.3 MB added, 1 pruned`; `backup status` after → `newest snapshot: 0.0 h old`. Snapshot id `05f14987`.
- D2.5: `date` 18:44:17 EDT, `heartbeat show` at 18:44:19 EDT (114 s after D1's 18:42:25): same probes OK, the same one RED (`com.cobalt.generated`), no new RED on aset or radar; `com.cobalt.radar running running 279 min, heartbeat fresh`. (Two filler pairs at 18:44:07 / 18:44:12, same reading.)
- D2.6: `date` → `Tue Oct  6 18:44:24 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-deploy-radar-ladder-refresh-1006` → ok; `rev-parse --short=8 pre-deploy-radar-ladder-refresh-1006` → `d1c40084`.

### STEP-4 the outage
| step | call | result |
|---|---|---|
| 4.1 | `date` | `Tue Oct  6 18:44:39 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print gui/501/com.cobalt.aset` | ok · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | ok · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `d1c40084` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-radar-ladder-refresh-1006` | `Updating d1c40084..9e70c702` / `Fast-forward` (4 files, 483 insertions, 2 deletions) |
| 4.4 | — | `migrations applied: none` (MIGRATIONS: none) |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · print | ok · `state = running`, `pid = 64112` (≠ 83925) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · print | ok · `state = running`, `pid = 64129` (≠ 83936) |
| 4.6 | `date` | `Tue Oct  6 18:44:59 EDT 2026` = `<t up>`; downtime 20 s |

### STEP-7 close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-06-radar-ladder-refresh` (after the green smoke) → ok; `rev-parse --short=8 deploy-2026-10-06-radar-ladder-refresh` → `9e70c702`.
- `<pre-merge>` `d1c40084` → `<stack-final>` `9e70c702` (`main` at `9e70c702`).
- Tags: `pre-deploy-radar-ladder-refresh-1006` = `d1c40084` · `deploy-2026-10-06-radar-ladder-refresh` = `9e70c702`.
- `<t down>` 18:44:39 / `<t up>` 18:44:59 EDT / 20 s.
- uv sync line: none in production (the gate venv build at STEP-R only).
- Proof cost: none (no migration, no proof-only run).
- `migrations applied: none`. `<RB>` before / after: not applicable (MIGRATIONS: none).
- Snapshot id: `05f14987` (ssd).
- `RESTARTS done: com.cobalt.aset com.cobalt.radar`.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 9e70c702`. This is ONE revert of the main-into-gate merge. `com.cobalt.aset` and `com.cobalt.radar` go down first and come up after.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK:
  1. Every smoke row is quoted verbatim with its `date` (## Smoke: 18:45:16, 18:45:19, 18:46:29, 18:45:25, 18:45:33, 18:45:38, 18:45:42, 18:47:31, 18:48:00).
  2. `ed19060f` was re-read at P3. `git -C /Users/cobalt/cobalt merge-base --is-ancestor ed19060f 9e70c702` → exit 0.
  3. REVERT-READBACK is shown at (h): 17 / 58 / 40 / 39, unchanged. Every count, sha and `file:line` in this report was read from tool output this run. `rev-parse --short=8 main` → `9e70c702`.
  4. STEP-T ran clean (`Merge made by the 'ort' strategy.`, no conflict). `grep -c -F "<<<<<<<" …/radar_panel.py` → `0`.
- THE RELEASE: not needed. This run never took the `cobalt_dev` lock (the EQUAL-TREE CLAUSE). `ls -la /Users/cobalt/cobalt-wt/*/.env` at P4 → no match. The gate's `.env` was never created.

## Smoke
`<t up>` = 18:44:59 EDT. `<restart set>` = `com.cobalt.aset com.cobalt.radar`.
- FIRST CALLS: `<rp_up>` = 17 · `<rpr_up>` = 58 · `<re_up>` = 40 · `<lc_up>` = 39 (each = D1).
- (a) 18:45:16 — `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 64112` (new; D1 83925); `…/com.cobalt.radar` → `state = running`, `pid = 64129` (new; D1 83936); `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent outside the set: same pid). GREEN.
- (b) 18:45:19 — `grep -c "Started server process" logs/aset.err` → `47` (`<a0>` 46 + 1); `tail -n 30 logs/aset.err` → `INFO:     Started server process [64118]` … `2026-10-06 18:44:54.734 | INFO | cobalt.voice.web:voice_startup:183 - voice: scratch dir … locked by this process; start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`; Traceback aset.err `2` (= `<ta0>`), Traceback radar.err `0` (= `<tr0>`), TaxonomyConfigError `0` (= `<tc0>`). Radar tails below.
- (c) 18:45:25 — `curl … http://127.0.0.1:5010/` → `200`; `…/radar` → `200`; `…/radar\?frame=phone` → `200` (each first attempt). GREEN.
- (d) 18:45:25 — MARKERS: `tickLadder` → `2` (after `2`); `window.setInterval(tickLadder,interval)` → `1` (after `1`); `window.setInterval(refreshPool,interval)` → `1` (after `1`). GREEN.
- (f) 18:45:33 — `COBALT_ENV=production uv run cobalt jobs restarts d1c40084..9e70c702` → exit 0, the same four rows as STEP-R, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= `<restart set>`); `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`). GREEN.
- (g) no migration: not run.
- (s) 18:45:38 — the ladder tick function `grep -c -F "tickLadder" …/radar_panel.py` → exit 0, `2`; the ladder timer line `grep -c -F "window.setInterval(tickLadder,interval)" …` → exit 0, `1`; the pool timer line `grep -c -F "window.setInterval(refreshPool,interval)" …` → exit 0, `1`. Each a count of 1 or more: GREEN. The tests behind them are quoted from the gate (## L68 GATE).
- (b) radar tail 1, `date` 18:46:29 (`<t up>` + 90 s) — `tail -n 12 logs/radar.err` → restart lines from 18:44:56 (`Vault secrets loaded into runtime RAM and vault locked.`, finviz token resolved), six `cards.expire: falling back to the session close` INFO lines at 18:46:23, then `2026-10-06 18:46:24.703 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791326696590`. A cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback: settled GREEN on the first tail.
- (e) read 1, 18:45:43 EDT — `HEARTBEAT RED — 1 job(s)`: the same single RED as `<hb0>` (`com.cobalt.generated`); `com.cobalt.aset running loaded, pid 64112`; `radar scanning (aftermarket), members 50`; `com.cobalt.radar running running 1 min, heartbeat fresh`. No new RED.
- (e) read 2, `date` 18:47:31, `heartbeat show` 18:47:33 EDT (110 s after read 1) — `HEARTBEAT RED — 1 job(s)`: the same single RED (`com.cobalt.generated`); `com.cobalt.aset running loaded, pid 64112`; `radar scanning (aftermarket), members 50`; `com.cobalt.radar running running 3 min, heartbeat fresh`. No new RED: GREEN. (Filler pairs 18:46:01–18:47:27, same reading each.)
- (h) REVERT-READBACK, `date` 18:48:00 (`<t up>` + 181 s, after (b) settled): `radar panel FAILED` → `17` (= `<rp_up>`), `radar pool refresh FAILED` → `58` (= `<rpr_up>`), `radar S5 evaluate FAILED` → `40` (= `<re_up>`), `lifecycle card read failed` → `39` (= `<lc_up>`); none grew. `curl … /radar` → `200`. No census read (no migration). GREEN.

THE CHAIN: every check committed (P2: `02b15e1f`, clean) → the tips re-read (P3: `ed19060f` = code tip = head) → the merged tree (T: `46a587c9`, one merge, no migration, no configs/ops change) → RESTARTS derived (R: aset + radar, no UNCLASSIFIED) → three suites green on the check's equal tree (G: offline 3963/0 · with-DB 4847/0 · live-note 146/0) → `<stack-final>` `9e70c702` = `<m1>` + docs (D2.3) → the landed code (4.3: `d1c40084..9e70c702` fast-forward) → markers 2 / 1 / 1 (d) → no migration (g) → residents up on new pids 64112 / 64129 after the merge (a) → radar cycling at 18:46:24 and heartbeat fresh (b, e) → the set's reads (s) → no new failure (h). The card surface (the ladder refreshing on his open page) is not readable here. The desk confirms it with him (L70).

## CONTINUE
next: STEP-D2 (D0, D1 green; gate green at 18:41:50 EDT)
OUTAGE STARTING 18:44:24 EDT — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED 18:44:59 EDT — aset pid 64112, radar pid 64129 running on 9e70c702.
Smoke GREEN 18:48:00 EDT; tagged; STEP-7 closed. next: none — this run is over (the desk: live-proof read, cleanup, push).

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main` (present at session start). D0's ACCEPTED list does not name it and its REFUSED classes (staged; dirty `src/` `tests/` `ops/` `configs/`) do not cover it. Safe default taken: not a refusal, the run goes on; the file is not touched. [18:42 EDT]

## RECORDS
- Downtime: 20 s (18:44:39 → 18:44:59 EDT); under 300 s.
- `cobalt_dev: 0013 (F2 = F0)` — from the check's gate (EQUAL-TREE CLAUSE); this run took no lock and touched no `cobalt_dev`.
- No `REFUSED, not needed` line; no message received from another session; no `RETIRE OWED`.
- Carried RED as read (D1, D2.5, smoke (e)): `RED com.cobalt.generated failed GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 …`. Not of the aset / sheet / radar probes; it names an EARLIER hub (`deploy-hub-deploy-p2-1005`), not this one — the desk's to read (a stale live-hub marker may be blocking `com.cobalt.generated`).
- First `uv` use in the fresh gate worktree built its venv (`Creating virtual environment at: .venv` · `Installed 253 packages in 815ms`) at STEP-R; production `uv` calls printed no sync line.
- Cleanup owed (L46), the desk's: the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-ladder-refresh-1006` and branch `deploy/deploy-radar-ladder-refresh-1006`; the set's worktree `/Users/cobalt/cobalt-wt/radar-ladder-refresh-1006` and branch `ops/radar-ladder-refresh-1006`.
- Session tokens at 18:46 EDT: `context 157521 of 400000 — ok`; at close, `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 3d1fd4e1` → `context 176943 of 400000 — ok`.
- The card's `## RECORDS`, copied:
  - radar-ladder-refresh: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-ladder-refresh-check-2026-10-06.md` last line: CHECK DONE · job: radar-ladder-refresh · pass: 1 · tip: ed19060f · house A: Sol FINDINGS: 6 · findings: 12 · dropped: 0 · held: 11 · fixed: 11 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 3 · suites: offline 3963/0 · with-DB 4847/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181164
  - radar-ladder-refresh: build report `/Users/cobalt/cobalt-wt/radar-ladder-refresh-1006/docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md` last line: BUILT · job: radar-ladder-refresh | tip: d2330003 | on 8c554d77 | migration: none | offline 3952/0 | with-DB 4836/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 172093
  - Tips: build `d2330003`; ship `ed19060f` (the check's fix commit, also the code tip and the branch head). The gate on `ed19060f`: offline 3963/0, with-DB 4847/0, live-note 146/0, `cobalt_dev: 0013`, `.env: removed`.
  - The build report existed only in the worktree; the deploy merge added it to `main` with no add/add (confirmed: 4.3's fast-forward `create mode 100644 docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md`).
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut. (Not met: no gate ran in this session.)
  - The `post()` race the build report names (its DECISION 2) was closed by the check (O3 = A1 = B1, `sendGeneration`); a record only.
  - FOLLOW-UP for him, NOT part of this deploy: the X29 control `tests/experiments/stale_score/test_x29_ladder_render.py` errors at setup (`fixture 'offline_skip_guard' not found`, `tests/cobalt/conftest.py:262`), UNPROVEN, a card of its own (the check's DECISION 1).
  - FOLLOW-UP for the desk, NOT part of this deploy: the live proof (card 54 decision 4) — `logs/aset.log` showing `GET /radar` at the pool's interval from a loaded page — needs his browser open after the restart; the desk reads it after the deploy.
  - AFTER / BEFORE marker values: drafted from `git show ed19060f:src/cobalt/aset/radar_panel.py` and main's tree; this run re-proved BEFORE (P6, D1: 0 / 0 / 1) and AFTER (smoke (d): 2 / 1 / 1) on the production path.
  - Absent before launch: the gate branch, the tag, the gate worktree and the report (this run's P5, D0 TAG NAMES and first-launch `ls` agree).
  - one feature per deploy (his R390).

DEPLOYED deploy-2026-10-06-radar-ladder-refresh 9e70c702 | set: none | migrations: none | gate: offline 3963/0 · with-DB 4847/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 176943
