# Deploy checkin-install · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/checkin-install-1018` (tip `964ba1b5`) on the gate `deploy/checkin-install`. Run in progress.

## L74
- none

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/782-deploy-checkin-install-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/782-deploy-checkin-install-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/782-deploy-checkin-install-card.md" · 0 · 699a09939552afd21e5f68f2407126994fb905d5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/782-deploy-checkin-install-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 84:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1854 row · grep -n "^| R1854 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 71:| R1854 | 06:45 ET | HIS RULING (brain relays, L79): fixes A-D (MVP first, DAY PLAN, check-ins 06/12/18/24 ET, owned waits, no idle nights). Words: [R1854](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at wake-up 06:46 |
RULING 2026-10-18 R1854 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1854 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 49371f09c96483d11b12eb166983c185f0f1c6f6
RULING 2026-10-18 R1854 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-checkin-install.md"` | 1 | `No such file or directory` |
| P1 | `date` | 0 | `Sun Oct 18 16:40:20 EDT 2026` (outside 21:30-22:30 ET) |
| P2 | `tail -n 3 "…/checkin-install-check-r2-2026-10-18.md"` | 0 | `CHECK DONE · job: checkin-install-1018 · pass: 1 · tip: 964ba1b5 · house A: Grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8516/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 203412` — carries `held unfixed: 0`, `ready: YES`, `tip: 964ba1b5` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/checkin-install-check-r2-2026-10-18.md"` | 0 | `0359947d2df973300f539ce79f665ff7de341e10` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/checkin-install-check-r2-2026-10-18.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 964ba1b5` | 0 | `964ba1b5` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/checkin-install-1018` | 0 | `964ba1b5` (= row, = TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 964ba1b5 ops/checkin-install-1018` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 964ba1b5 ops/checkin-install-1018 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-checkin-install status --short --branch` | 0 | `## deploy/checkin-install` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-checkin-install rev-parse --short=8 HEAD` | 0 | `370b4efe` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 370b4efe main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/checkin-install` | 0 | EMPTY |
| P6 | `grep -c -F "checkin-timer.sh" ".../prompts/CTO-DESK-WAKEUP.md"` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "MVP FIRST" ".../prompts/CTO-DESK-WAKEUP.md"` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "## CHECK-IN" ".../prompts/BRAIN-HUB.md"` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "## 10. THE CHECK-IN TIMER" ".../prompts/STANDING-LIST.md"` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 964ba1b5 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 89330` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 70450` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-checkin-install merge --no-edit 964ba1b5` → `Merge made by the 'ort' strategy.` — 9 files changed, 973 insertions(+): `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `CHECKIN-PING.md` (new), `CTO-DESK-WAKEUP.md`, `STANDING-LIST.md`, `reports/checkin-install-build-2026-10-18.md` (new), `.result` (new), `ops/desk/checkin-timer.sh` (new), `ops/desk/com.cobalt.checkin-timer.plist` (new), `tests/ops/test_checkin_install_1018.py` (new).
- `git -C /Users/cobalt/cobalt-wt/deploy-checkin-install rev-parse --short=8 HEAD` → `5a52b4f7` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 370b4efe..deploy/checkin-install` → `5a52b4f7 Merge commit '964ba1b5' into deploy/checkin-install` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 964ba1b5 deploy/checkin-install` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 370b4efe deploy/checkin-install -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 370b4efe deploy/checkin-install -- configs ops` →
```
 ops/desk/checkin-timer.sh               | 198 ++++++++++++++++++++++++++++++++
 ops/desk/com.cobalt.checkin-timer.plist |  38 ++++++
 2 files changed, 236 insertions(+)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 370b4efe deploy/checkin-install` → exit 0:
```
EXCEPTION: ops/desk/com.cobalt.checkin-timer.plist — ops/desk, Label com.cobalt.checkin-timer is no jobs.yaml label (not a launchd job of this list)
STEP-C: ADMITTED 0
```
  `<launchd set>` = empty (the card has no `## LAUNCHD`).

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-checkin-install` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-checkin-install
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-checkin-install
Installed 256 packages in 651ms
path	change	rule	restart
docs/40 - DevDocs/prompts/BRAIN-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECKIN-PING.md	A	DOCS	-
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.result	A	DOCS	-
ops/desk/checkin-timer.sh	A	operator script; no Cobalt reader	-
ops/desk/com.cobalt.checkin-timer.plist	A	operator script; no Cobalt reader	-
tests/ops/test_checkin_install_1018.py	A	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (no UNCLASSIFIED row; MIGRATIONS: none, so L66 does not apply). No resident goes down. `<launchd set>` = empty.

## L68 GATE
- THE EQUAL-TREE CLAUSE does not hold: the check's stop line carries `with-DB 0/0` → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 20.75s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: none (the build report `checkin-install-build-2026-10-18.md` names no with-DB deselect; its one `deselected` is a `-k` mutation run). TICKERS: none. Migration: none.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-checkin-install all --deploy --deploy-gate` → exit 0, its output WHOLE:
```
tests/ops: run (deploy gate)
offline 8627/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5582/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-checkin-install-all-20261018-164213.log
```
- (a) OFFLINE `offline 8627/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock waited 0 min; proof-only at `0013`, nothing CHANGED; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log line 1015).
- (c) PASS 1 whole: every SKIPPED line inside the allowed set — `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`; `test_playbook_live.py:31` is the `requires_live` mark on `test_live_vault_renders_six_decks` (def at :32), reason `COBALT_LIVE_VAULT_ROOT not set`; `test_s3_c4_experiments.py:95` is the mark on `test_x14_live_his_template_strips_to_the_committed_fixture` (def at :96); `test_replay_line.py:266` reason names `COBALT_TEST_LIVE_DRC`.
- (c2)/(c3) no migration above `0013` in this set: `with-DB 5582/0`.
- (f) `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed`; log line 2238 `lock released`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-checkin-install" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `0`.
- (e) LIVE-NOTE `live-note 147/0`; no skip names `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 5a52b4f7

## Deploy table
| step | command | result |
|---|---|---|
| D0 MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 179]`; no staged line; ` M` / `??` under `docs/40 - DevDocs/`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (not a `src/ tests/ ops/ configs/` path; recorded) |
| D0 MAIN | `git -C /Users/cobalt/cobalt diff --stat 370b4efe main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 PROBE | `tag scratch-allow-probe-checkin-install` · `tag -d …` | `Deleted tag 'scratch-allow-probe-checkin-install' (was 370b4efe)` |
| D0 PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main 13687f69] scratch: …` → `370b4efe docs(card): 730 REPORT points at the fix-round build report (fr1)` (HEAD back) |
| D0 TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-checkin-install` · `…/pre-checkin-install` | exit 1 · exit 1 |
| D1 | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | `Sun Oct 18 17:31:45 EDT 2026` · `<hb0>`: `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-18 17:31:47 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.radar             running   running 71 min, heartbeat fresh`; `AMB  com.cobalt.herdr unmanaged …` (declared interim); `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)` |
| D1 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `<jobs0>` = `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 1.2 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` | `state = running`, `pid = 89330` · `state = running`, `pid = 70450` |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 89351` | `Cobalt is ONLINE (PID: 89351).` · `89351 ??         0:00.03 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | last: `2026-10-18 17:31:10.763 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`; no traceback |
| D1 LOGS | `<a0>` `<ta0>` `<tr0>` `<tc0>` `<rp0>` `<rpr0>` `<re0>` `<lc0>` | `283` `217` `0` `0` `18` `60` `43` `39` |
| D1 | `curl … /radar` | `200` |
| D1 | `## MARKERS` again | `0` `0` `0` `0` (each its before) |
| D1 | `<launchd set>` | empty: nothing |
| D1 | migration reads | MIGRATIONS: none — `<RB>`, census and D1-M not run |

## Smoke

## CONTINUE
- next: STEP-D2 (D0 and D1 done at Sun Oct 18 17:31:45 EDT 2026)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
