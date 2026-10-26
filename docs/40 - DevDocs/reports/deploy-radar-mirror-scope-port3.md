# Deploy radar-mirror-scope-port3 · set: radar-mirror-scope-port3-r2 · migrations: none

## §0 Headline
- (in progress)

## L74
- A system notice in this session asked commits to also carry a `Claude-Session:` line. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1066-deploy-radar-mirror-scope-port3-r2-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1066-deploy-radar-mirror-scope-port3-r2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1066-deploy-radar-mirror-scope-port3-r2-card.md" · 0 · 1c934ecca4d6cf0e5d7e8b6ee6e661855a8aeb94
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1066-deploy-radar-mirror-scope-port3-r2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
First launch: `ls -la "<REPORT>"` → exit 1, `No such file or directory`.

| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 26 16:22:02 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../radar-mirror-scope-port3-check-2026-10-24.md"` | 0 | `CHECK DONE · job: radar-mirror-scope-port3 · pass: 1 · tip: 671e0215 · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165034` — carries `held unfixed: 0`, `ready: YES`, `tip: 671e0215` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/radar-mirror-scope-port3-check-2026-10-24.md"` | 0 | `ba9f463499a38337a90f4baf1f252ddd3297e17e` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 671e0215` | 0 | `671e0215` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port3` | 0 | `304a0b03` = row = `TIP` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 671e0215 304a0b03` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 671e0215 304a0b03 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no holder |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-mirror-scope-port3` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `e9c2ce13` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor e9c2ce13 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/radar-mirror-scope-port3` | 0 | empty |
| P6 | `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` | 1 | `0` = before |
| P6 | `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` | 2 | `grep: /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py: No such file or directory` — the file is new with this set; production does not carry the marker (`## DECISIONS` 1) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 304a0b03 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 36927` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 36944` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1` — com.cobalt.agent recorded retired |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` — expected (retired) |

## THE TREE
- `git -C <GATE> merge --no-edit 304a0b03` → `Merge made by the 'ort' strategy.` (9 files changed, 561 insertions(+), 16 deletions(-): `src/cobalt/radar/notes.py`, `tests/cobalt/test_radar_{evaluate,mirror_scope (new),notes,replay,runner}.py`, three docs)
- `git -C <GATE> rev-parse --short=8 HEAD` → `2ece355e` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent e9c2ce13..deploy/radar-mirror-scope-port3` → `2ece355e8 Merge commit '304a0b03' into deploy/radar-mirror-scope-port3` (one line, one head)
- `merge-base --is-ancestor 671e0215 deploy/radar-mirror-scope-port3` → exit 0 · `merge-base --is-ancestor 304a0b03 deploy/radar-mirror-scope-port3` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat e9c2ce13 deploy/radar-mirror-scope-port3 -- src/cobalt/db_migrations` → nothing (`MIGRATIONS: none`)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat e9c2ce13 deploy/radar-mirror-scope-port3 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" e9c2ce13 deploy/radar-mirror-scope-port3` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty · `<deferred set>`: empty.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (exit 0; uv created the gate `.venv`, `Installed 257 packages in 656ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port3-build-2026-10-24.md	A	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port3-build-2026-10-24.result	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- No `UNCLASSIFIED` row. NOT LOADED read: `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `pid = 36938` → kept.
- `<restart set>`: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`
- `<deferred set>`: none · `<launchd set>`: none
- com.cobalt.agent: recorded retired — not restarted (not derived by this range either)

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 671e0215 2ece355e -- . ":(exclude)docs"` → `src/cobalt/prefill/cli.py | 12 +`, `src/cobalt/prefill/refresh_probe.py | 458 +++`, `tests/cobalt/test_prefill_refresh.py | 46 ++++`, `tests/cobalt/test_refresh_probe.py | 253 +++` (4 files, 769 insertions; `main` moved since the check) → clause does not hold; the gate runs whole.
- Deselects: none (the build adds no with-DB test, per try1's read of `radar-mirror-scope-port3-build-2026-10-24.md:166`). `TICKERS: none` → no `--tickers`. No `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `265 passed, 163 skipped in 20.16s` — 0 failed (every skip is a with-DB `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-radar-mirror-scope-port3-r2 all --deploy --deploy-gate` → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9141/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5977/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-radar-mirror-scope-port3-r2-all-20261026-162415.log
```
- (a) OFFLINE `offline 9141/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock waited 0 min; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1049`); proof-only at `0013`, nothing CHANGED.
- (c) PASS 1 whole; all nine SKIPPED lines are inside the allowed set (test and reason match the hub's list; the `test_checkpoints_live.py`, `test_playbook_live.py` and `test_s3_c4_experiments.py` skips are the named tests with reason `COBALT_LIVE_VAULT_ROOT not set`; `test_replay_line.py` names `COBALT_TEST_LIVE_DRC`).
- (c2) `dev forward: APPLIED 17:10:12` (log `:1279`). (c3) PASS 2 green: `with-DB 5977/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log `:2388`; FINGERPRINT `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` at `:2385` = F0).
- THE RELEASE: `.env: removed (L76 lock released, log :2390, gate ended by 17:15:59)`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-radar-mirror-scope-port3-r2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) LIVE-NOTE `live-note 148/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 2ece355e

## Deploy table
STEP-D0:
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 109]`. `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (untracked, outside `src/ tests/ ops/ configs/`; not a refused line). No staged line.
- `git -C /Users/cobalt/cobalt diff --stat e9c2ce13 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-radar-mirror-scope-port3` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-radar-mirror-scope-port3' (was e9c2ce13f)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 112c640a9] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `e9c2ce13f docs(desk): keep failed port3 deploy report as try1` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-26-radar-mirror-scope-port3` → exit 1 · `… refs/tags/pre-radar-mirror-scope-port3` → exit 1.

STEP-D1 (`date` → `Mon Oct 26 17:16:38 EDT 2026`):
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-26 17:16:39 EDT)`. OK: database, sheet HTTP `http://127.0.0.1:5010/ -> 200`, sheet daymode, radar `scanning (aftermarket), members 50`, cos `loop stamping (8s ago)`, `com.cobalt.aset running loaded, pid 36927`, `com.cobalt.radar running running 2553 min, heartbeat fresh`, `com.cobalt.cos running running 2553 min, heartbeat fresh`. The two REDs, named (neither aset / sheet / radar; not a stop): `RED  com.cobalt.agent             not loaded NOT LOADED in launchd — …` (recorded retired) · `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings …`. AMB `com.cobalt.herdr` unmanaged (declared interim). OWED (deferred bootstrap): prefill-refresh, checkpoint-0715/0745/0815/0845, playbook. No radar RED, so the carried family is not in play.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>` `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 6.3 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` `36927` · `…/com.cobalt.radar` → `state = running`, `<radar pid>` `36944` · `…/com.cobalt.cos` → `state = running`, `<cos pid>` `36938` · `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (com.cobalt.agent recorded retired; no `ps -p`).
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last cycle `2026-10-26 17:14:41.880 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1793049192527`, then price-floor lines at 17:16:34; no traceback.
- LOG BASELINES: `<a0>` 298 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 31 · `<rpr0>` 60 · `<re0>` 750 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS → `0`; marker 2 `No such file or directory` (exit 2; DECISIONS 1).
- THE LAUNCHD SET: empty → nothing. No migration → no `<RB>`, no D1-M.

## Smoke

## CONTINUE
- next: STEP-D2 (gate green at Mon Oct 26 17:15:59 EDT 2026; D0, D1 done; D2.0 `deploy-shipped.sh --moved e9c2ce13` → nothing)

## DECISIONS
1. ASK DESK: card `## MARKERS` line 2 gives `before 0`, but `tests/cobalt/test_radar_mirror_scope.py` is new with this set, so on production `grep -c -F` exits 2 `No such file or directory` rather than printing `0`. Production does not carry the marker. Safe default taken: read as `before` (absent = not carried), continue; smoke (d)'s `after 1` stands as written. [Mon Oct 26 16:22:02 EDT 2026]

## RECORDS

(run in progress — next step under ## CONTINUE)
