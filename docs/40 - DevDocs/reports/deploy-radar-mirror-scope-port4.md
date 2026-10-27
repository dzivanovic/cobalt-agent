# deploy radar-mirror-scope-port4 · set: radar-mirror-scope-port4 · migrations: none

## §0 Headline
- Deploy of `ops/radar-mirror-scope-port4` (code tip `b0cca7d7`, head `421af171`) on card 1074, started 2026-10-26 20:36 ET.

## L74
- The session's harness reminder asked that commits carry a `Claude-Session:` line. This is recorded as DATA and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md" · 0 · d3d669a5c715660c6e4b0e4e8bebd576503c15fb
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1074-deploy-radar-mirror-scope-port4-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
AUTHORIZED
```
RULINGS: none.

## PREFLIGHT
First launch: `ls -la "<REPORT>"` → `No such file or directory` (exit 1).

| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 26 20:36:23 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../radar-mirror-scope-port4-check-2026-10-26.md"` | 0 | `CHECK DONE · job: radar-mirror-scope-port4 · pass: 1 · tip: b0cca7d7 · house A: Grok FINDINGS: 0 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 9144/0 · with-DB 5980/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 190063`: carries `held unfixed: 0` and `ready: YES`, and `tip: b0cca7d7` = the code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/radar-mirror-scope-port4-check-2026-10-26.md"` | 0 | `94894ab18f1d6ee9e3827da9f6e5aa23f1f6e387` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 b0cca7d7` | 0 | `b0cca7d7` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port4` | 0 | `421af171` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b0cca7d7 421af171` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat b0cca7d7 421af171 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-mirror-scope-port4` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `d3d669a5` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d3d669a5 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/radar-mirror-scope-port4` | 0 | empty |
| P6 | `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` | 2 | `grep: /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py: No such file or directory`: the file is absent, so production does not carry the marker (this is the before state; the set adds the file) |
| P6 | `grep -c -F "def warm_config" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 421af171 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 58145` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 58164` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 0 | `1`: `com.cobalt.agent recorded retired` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `  Cobalt is OFFLINE.` (expected with the agent retired) |

## THE TREE
- `git -C <GATE> merge --no-edit 421af171` → `Merge made by the 'ort' strategy.` (13 files changed, 713 insertions(+), 16 deletions(-)). No conflict.
- `git -C <GATE> rev-parse --short=8 HEAD` → `247cfe42` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent d3d669a5..deploy/radar-mirror-scope-port4` → `247cfe42d Merge commit '421af171' into deploy/radar-mirror-scope-port4` (one merge for one head).
- `merge-base --is-ancestor b0cca7d7 deploy/radar-mirror-scope-port4` → exit 0; `merge-base --is-ancestor 421af171 deploy/radar-mirror-scope-port4` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat d3d669a5 deploy/radar-mirror-scope-port4 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat d3d669a5 deploy/radar-mirror-scope-port4 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" d3d669a5 deploy/radar-mirror-scope-port4` → exit 0, `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, `Installed 257 packages in 842ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port4-build-2026-10-26.md	A	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port4-build-2026-10-26.result	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_config_warmup.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
- No `UNCLASSIFIED` row. `launchctl print gui/501/com.cobalt.cos` → exit 0, `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `pid = 58158`: cos stays in the set.
- `<restart set>`: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`
- `<deferred set>`: empty
- `<launchd set>`: empty
- com.cobalt.agent: recorded retired — not restarted (the tool's set did not name it)

## L68 GATE
THE EQUAL-TREE CLAUSE holds. There is ONE branch in `TIP`, and `git -C /Users/cobalt/cobalt diff --stat b0cca7d7 247cfe42 -- . ":(exclude)docs"` prints nothing. The check's stop line carries `with-DB 5980/0` (> 0). The check's three suite lines are therefore the gate's, and (a)–(f) are skipped. They are quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port4-check-2026-10-26.md` `## Suites` (lines 225–245):
```
tests/ops: run (deploy gate)
offline 9144/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5980/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-port4-all-20261026-193449.log
```
- Skips read against the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365` and `test_predicate.py:262` are named in the set. So are the `test_checkpoints_live.py` and `test_playbook_live.py` skips (reason `COBALT_LIVE_VAULT_ROOT not set`), the `test_replay_line.py` skip (`COBALT_TEST_LIVE_DRC`) and the `test_s3_c4_experiments.py` x14 skip. All nine are inside the set.
- The lock was not taken by this run: `<GATE>/.env` was never present, and P4 found no `.env` in any worktree.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 247cfe42

## Deploy table

### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 142]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line. ` M` lines: `.claude/settings.json`, `configs/cobalt/rules.yaml` and paths under `docs/40 - DevDocs/`. `??` lines under `docs/40 - DevDocs/`, plus one `?? .claude/settings.json.bak` (see `## DECISIONS`). No dirty `src/`, `tests/` or `ops/` path. |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat d3d669a5 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-radar-mirror-scope-port4` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-radar-mirror-scope-port4' (was d3d669a5c)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 6bc2af6d2] scratch: allowlist probe (reverted next line)` → `d3d669a5c docs(desk): R2526 deploy card 1074 for port4` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-26-radar-mirror-scope-port4` | 1 | absent |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-radar-mirror-scope-port4` | 1 | absent |

### STEP-D1 (baseline)
- `date` → `Mon Oct 26 20:38:51 EDT 2026`.
- `<hb0>` from `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s)  (2026-10-26 20:38:52 EDT)`.
  - The aset, sheet and radar probes are OK: `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200`, `OK   radar                    paused (market_reset)`, `OK   com.cobalt.aset              running   loaded, pid 58145 [launchd probe]`, `OK   com.cobalt.radar             running   running 198 min, heartbeat fresh`, `OK   com.cobalt.cos               running   running 198 min, heartbeat fresh`.
  - REDs, named and not a stop:
    - `RED  com.cobalt.agent             not loaded NOT LOADED in launchd — …`: the agent is recorded retired.
    - `RED  com.cobalt.replay            failed    StepFailed: step movers failed — TraderSettingsError: invalid radar.benchmark: 7 validation errors for BenchmarkSettings top_n Field required …`
  - `AMB  com.cobalt.herdr` is unmanaged.
  - OWED (deferred bootstrap): `prefill-refresh`, `checkpoint-0715`, `checkpoint-0745`, `checkpoint-0815`, `checkpoint-0845`, `playbook`.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`): `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`. No `docs/_inflight/` line. `<jobs0>`: `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 3.3 h old` (`ssd   local ARMED /Volumes/COBALT-BACKUP/restic`).
- `launchctl print`: aset `state = running`, `<aset pid>` 58145; radar `state = running`, `<radar pid>` 58164; cos `state = running`, `<cos pid>` 58158.
- `/Users/cobalt/cobalt/cobalt.sh status` → `  Cobalt is OFFLINE.` (the agent is recorded retired, so there is no `ps -p`).
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: paused_market_reset scan_id=None`, the last stamped `2026-10-26 20:38:21.326`. No traceback.
- LOG BASELINES: `<a0>` 300 · `<ta0>` 217 · `<tr0>` 1 · `<tc0>` 0 · `<rp0>` 31 · `<rpr0>` 60 · `<re0>` 750 · `<lc0>` 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`.
- MARKERS again: `0` · `No such file or directory` (the file is absent, so not carried) · `0`. All are at their before values.
- THE LAUNCHD SET: empty. No migration: there is no `<RB>` and no D1-M.

## Smoke

## CONTINUE
- next: STEP-D0 (gate green at Mon Oct 26 20:37:59 EDT 2026)
- D0 and D1 done; next: STEP-D2 (D2.0 report commit)

## DECISIONS
- ASK DESK: `?? .claude/settings.json.bak` on `main` is outside D0's ACCEPTED list. It is not a staged line and not a dirty `src/`/`tests/`/`ops/`/`configs/` path, so it is outside the REFUSED list too. Safe default taken: not a stop; the untracked file is left untouched. [Mon Oct 26 20:38:51 EDT 2026]

## RECORDS

(run in progress — next step under ## CONTINUE)
