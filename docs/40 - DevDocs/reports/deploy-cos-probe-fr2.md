# deploy-cos-probe-fr2 — set: cos-probe · migrations: none

## §0 Headline
- FAILED at smoke (d), rollback used: the gate was green on `09b0627b` and the merge landed (`00a3b61d..7c460d39`), but marker 4 read `2` against the card's `after 1`.
- Cause: the card's fixed string `## 2026-10-20 — cos-probe-fr2` also matches the check's heading `## 2026-10-20 — cos-probe-fr2 (check)` (README lines 52, 55). Code markers 1–3 read their `after` values.
- STEP-5: one `revert -m 2` → `ebb5020c`; code tree = `<pre-merge>` `00a3b61d` (proven). Radar is back up on the old code (pid 59996). Radar was down twice, 11 s each.
- Revert-readback: all four failure counts unchanged (18/60/43/39), curls `200`, no new RED. The re-land is the desk's call (DECISIONS).

## L74
- A system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded once; not acted on — commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/920-deploy-cos-probe-fr2-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/920-deploy-cos-probe-fr2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/920-deploy-cos-probe-fr2-card.md" · 0 · c6aa6b47f54ef810c7801312bbf1b1ee955f0274
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/920-deploy-cos-probe-fr2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la ".../reports/deploy-cos-probe-fr2.md"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 DATE | `date` | 0 | Tue Oct 20 14:46:53 EDT 2026 — outside 21:30-22:30 ET |
| P2 check last line | `tail -n 3 ".../cos-probe-fr2-check-2026-10-20.md"` | 0 | `CHECK DONE · job: cos-probe-fr2 · pass: 1 · tip: dfea631a · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 178055` — carries `held unfixed: 0` and `ready: YES`; `tip: dfea631a` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/cos-probe-fr2-check-2026-10-20.md"` | 0 | dea3e13e6f2a074097d129bd592eff0c95ee6fd0 |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../cos-probe-fr2-check-2026-10-20.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 dfea631a` | 0 | dfea631a |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-probe-fr2` | 0 | dfea631a (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor dfea631a ops/cos-probe-fr2` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat dfea631a ops/cos-probe-fr2 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds it |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-cos-probe-fr2 status --short --branch` | 0 | `## deploy/cos-probe-fr2` |
| P5 `<m0>` | `git -C /Users/cobalt/cobalt-wt/deploy-cos-probe-fr2 rev-parse --short=8 HEAD` | 0 | c6aa6b47 |
| P5 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor c6aa6b47 main` | 0 | — |
| P5 nothing main lacks | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-probe-fr2` | 0 | empty |
| P6 marker 1 | `grep -c -F "under the scratch HOME" .../src/cobalt/cos/probe.py` | 0 | 1 (before `1`) |
| P6 marker 2 | `grep -c -F ".claude.json" .../src/cobalt/cos/probe.py` | 0 | 2 (before `2`) |
| P6 marker 3 | `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes" .../tests/cobalt/test_cos_probe.py` | 1 | 0 (before `0`) |
| P6 marker 4 | `grep -c -F "## 2026-10-20 — cos-probe-fr2" ".../docs/40 - DevDocs/cobalt/cos/README.md"` | 1 | 0 (before `0`) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main dfea631a -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 77363 |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 31756 |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-cos-probe-fr2 merge --no-edit dfea631a` → `Merge made by the 'ort' strategy.` (5 files: cos/README.md, the build report and .result, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`; 442+, 44−).
- `<m1>`: `git -C .../deploy-cos-probe-fr2 rev-parse --short=8 HEAD` → `09b0627b`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent c6aa6b47..deploy/cos-probe-fr2` → `09b0627b Merge commit 'dfea631a' into deploy/cos-probe-fr2` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor dfea631a deploy/cos-probe-fr2` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat c6aa6b47 deploy/cos-probe-fr2 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat c6aa6b47 deploy/cos-probe-fr2 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" c6aa6b47 deploy/cos-probe-fr2` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-cos-probe-fr2` · `ls -la .../deploy-cos-probe-fr2/.env` → No such file or directory · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, whole (after uv's venv creation lines: `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Built cobalt-agent …`, `Installed 257 packages in 850ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.result	A	DOCS	-
src/cobalt/cos/probe.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
- No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar`. `<deferred set>` = none. `<launchd set>` = none. `com.cobalt.cos` not in the set (no NOT LOADED read).

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat dfea631a 09b0627b -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5869/0` (> 0). The check's suite lines are the gate's; (a)–(f) skipped. Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr2-check-2026-10-20.md` lines 154–176 (W on `dfea631a`, `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-probe-fr2 all --deploy --deploy-gate`, exit 0):
```
tests/ops: run (deploy gate)
offline 8970/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5869/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr2-all-20261020-135736.log
```
SKIPPED lines against the allowed set, by test and reason: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` — listed; `test_checkpoints_live.py:36` = the decorator of `test_dry_run_finds_the_heading_in_real_notes` (`grep -n -F` → line 37; the file's one test), reason `COBALT_LIVE_VAULT_ROOT not set`; `test_playbook_live.py:31` = `test_live_vault_renders_six_decks` (line 32; the file's one test), same reason; `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (line 96; the file's one `COBALT_LIVE_VAULT_ROOT not set` skip); `test_replay_line.py:266` reason names `COBALT_TEST_LIVE_DRC`. All inside; none outside.
- `cobalt_dev: 0013 — F2 = F0` · `.env: removed` (the check's gate). This run took no lock and touched no `cobalt_dev`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 09b0627b

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 146]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (not under src/, tests/, ops/, configs/ — recorded) |
| MAIN moved | `git -C /Users/cobalt/cobalt diff --stat c6aa6b47 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-cos-probe-fr2` | 0 | — |
| PROBE tag -d | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-cos-probe-fr2` | 0 | `Deleted tag 'scratch-allow-probe-cos-probe-fr2' (was c6aa6b47)` |
| PROBE commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main b02066d7] scratch: allowlist probe (reverted next line)` |
| PROBE reset | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | — |
| PROBE HEAD | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `c6aa6b47 docs(card): cos-probe-fr2 deploy card 920, R2182` |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-20-cos-probe-fr2` | 1 | free |
| TAG pre | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-cos-probe-fr2` | 1 | free |

### STEP-D1 (baseline, 14:48:52 EDT)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 3 job(s) and 2 probe(s)  (2026-10-20 14:48:53 EDT)`. Probes: database, sheet HTTP (`http://127.0.0.1:5010/ -> 200`), sheet daymode, obsidian, mainframe, herdr, seat usage, backup, vault blocks, redactions, cos, hitl — OK. RED probes: `RED  archiver                 last run FAILED — last run 2026-10-20 00:54 UTC (17.9 h ago), rows written 3369418, exit 1` (named, not a stop) · `RED  radar                    failed_stage bars: poll failures: 1; poll SNWV stale since 2026-10-20T18:43:15.206957+00:00` (THE CARRIED FAMILY: `com.cobalt.radar running 162 min, heartbeat fresh`; radar.err `2026-10-20 14:47:46.645 … radar cycle: scanning scan_id=1792521981216` inside 5 min; no traceback in the tail). RED jobs: `com.cobalt.archiver failed` (Finviz 400 on WBD/i1), `com.cobalt.replay failed` (`ReplayError: archiver not done: state 'failed'`), `com.cobalt.generated failed` (`GeneratedCommitRefused` — the pre-commit guard named a live hub `79a459de deploy-hub-hub-cos-restart-fr1`) — named, not a stop. Residents: `com.cobalt.aset running pid 77363`, `com.cobalt.agent running pid 35845`, `com.cobalt.radar running`, `com.cobalt.cos disabled … NOT LOADED BY DESIGN`; AMB `com.cobalt.herdr` unmanaged; OWED (deferred bootstrap): prefill-refresh, checkpoint-0715/0745/0815/0845, playbook.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line. `<jobs0>`: `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 2.7 h old` (ssd local ARMED; b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` 77363 · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` 31756 · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).` · `ps -p 35845` → `35845 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → seven `cards.expire: falling back to the session close (16:00:00)` INFO lines at 14:47:46 and `2026-10-20 14:47:46.645 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792521981216`.
- LOG BASELINES: `<a0>` `Started server process` aset.err = 289 · `<ta0>` Traceback aset.err = 217 · `<tr0>` Traceback radar.err = 0 · `<tc0>` TaxonomyConfigError radar.err = 0 · `<rp0>` `radar panel FAILED` aset.err = 18 · `<rpr0>` `radar pool refresh FAILED` aset.err = 60 · `<re0>` `radar S5 evaluate FAILED` radar.err = 43 · `<lc0>` `lifecycle card read failed` radar.err = 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`.
- MARKERS again: `1`, `2`, `0`, `0` — each its `before`.
- THE LAUNCHD SET: empty — nothing. MIGRATION: none — `<RB>` and D1-M not run.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved c6aa6b47 "<card>"` → exit 0, nothing printed. Report committed: `[main 00a3b61d] docs(report): deploy cos-probe-fr2 — gate green on 09b0627b`; `show --stat HEAD` → the one file (143+). `<pre-merge>` = `00a3b61d`.
- D2.1 `git -C .../deploy-cos-probe-fr2 merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report, 143+).
- D2.2 `<stack-final>` = `7c460d39`; `rev-parse --short=8 7c460d39^2` → `00a3b61d` = `<pre-merge>`; `merge-base --is-ancestor 09b0627b 7c460d39` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 09b0627b 7c460d39 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 2.7 h old`; `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 9637.9 MB` · `ssd: snapshot 746896b2 — 0 new / 3 changed, 183.4 MB added, 1 pruned` · `F17: com.cobalt.backup DONE`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` 14:50:59 · `heartbeat show` → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 14:51:00 EDT)` (127 s after D1's 14:48:53): `RED archiver` (as `<hb0>`), `OK radar scanning (rth), members 50`, `com.cobalt.radar running 164 min, heartbeat fresh`, aset pid 77363; jobs RED archiver, replay, generated as `<hb0>`. No new RED.
- D2.6 `date` → Tue Oct 20 14:51:04 EDT 2026. `git -C /Users/cobalt/cobalt tag pre-cos-probe-fr2` at `00a3b61d` (HEAD).

### STEP-4 (outage)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` Tue Oct 20 14:51:16 EDT 2026 |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` | exit 0, no output |
| 4.2 | `launchctl print gui/501/com.cobalt.radar` | exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.2 | orphan-clean / agent stop | not run — aset and agent not in `<restart set>` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `00a3b61d` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/cos-probe-fr2` | `Updating 00a3b61d..7c460d39` · `Fast-forward` (5 files, 442+, 44−) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | exit 0, no output |
| 4.6 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, pid 59687 (≠ 31756), `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` |
| 4.6 | `date` | `<t up>` Tue Oct 20 14:51:27 EDT 2026 — downtime 11 s |
| 4.6L | — | `<launchd set>` empty: nothing |

### Close
- `<pre-merge>` `00a3b61d` → `<stack-final>` `7c460d39` → reverted by `ebb5020c` (`main` now). Tags: `pre-cos-probe-fr2` at `00a3b61d`; `deploy-2026-10-20-cos-probe-fr2` NOT set (no green smoke).
- Outage 1: `<t down>` 14:51:16 → `<t up>` 14:51:27 (11 s). Outage 2 (STEP-5): 14:52:21 → 14:52:32 (11 s).
- uv sync: none in production calls (the gate worktree's first `uv run` created its own `.venv`, STEP-R). Proof cost: none (no migration). `migrations applied: none`. `<RB>`: none.
- Snapshot: `746896b2` (ssd), D2.4.
- RESTARTS done: com.cobalt.radar (twice: deploy, then rollback). LAUNCHD done: none. BOOTSTRAP OWED: none from this set.
- THE ROLLBACK STRING (used, STEP-5): 1. CODE `git -C /Users/cobalt/cobalt revert --no-edit -m 2 7c460d39` → `ebb5020c` (com.cobalt.radar down first, up after). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit ebb5020c` (git titles it `Reapply "Merge branch 'main' into deploy/cos-probe-fr2"`), with com.cobalt.radar's bootout/bootstrap — the desk's.

### PRE-STOP SELF-CHECK (K25)
1. Every smoke row is quoted from its own tool output, with its `date` (14:51:39; STEP-5 14:52:21, 14:52:32, 14:52:46, 14:54:02, 14:54:38).
2. Tip `dfea631a` re-read at P3 (`rev-parse` → `dfea631a`, head `dfea631a`); `git -C /Users/cobalt/cobalt merge-base --is-ancestor dfea631a 7c460d39` → exit 0.
3. REVERT-READBACK is shown in STEP-5 (4): the counts 18/60/43/39 match `<rp5>`…`<lc5>`. Every sha, count and `file:line` here was re-read this run (`log --oneline -3` → `ebb5020c`, `7c460d39`, `00a3b61d`).
4. No conflict marker: STEP-T, D2.1 and the revert all ran clean (`Merge made by the 'ort' strategy.` ×2, revert `[main ebb5020c]`).

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39.
- (a) `date` 14:51:39 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, pid 77363 (SAME, outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, pid 59687 (NEW) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).` — GREEN.
- (b) part: `grep -c "Started server process" aset.err` → 289 = `<a0>` (aset outside the set) · `tail -n 30 aset.err` → no new `Started server process`; last lines are 10:32 card-write INFO (vault content, not quoted) · Traceback aset.err 217 = `<ta0>` · Traceback radar.err 0 = `<tr0>` · TaxonomyConfigError radar.err 0 = `<tc0>`. Radar tails not yet taken.
- (c) `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200` — GREEN.
- (d) MARKERS: marker 1 `0` (after `0`) ✓ · marker 2 `0` (after `0`) ✓ · marker 3 `1` (after `1`) ✓ · marker 4 `grep -c -F "## 2026-10-20 — cos-probe-fr2" ".../cos/README.md"` → `2` (after `1`) — **RED**. `grep -n -F` → `52:## 2026-10-20 — cos-probe-fr2` and `55:## 2026-10-20 — cos-probe-fr2 (check)`: the fixed string also matches the check's heading. (d) wrong → STEP-5.
- (f) part: `COBALT_ENV=production uv run cobalt jobs restarts 00a3b61d..7c460d39` → exit 0, `RESTARTS: com.cobalt.radar` = `<restart set>`, no `UNCLASSIFIED`.

### STEP-5 — rollback (entered on smoke (d))
| step | command | result |
|---|---|---|
| (0) | `date` | Tue Oct 20 14:52:21 EDT 2026 |
| (1) | `launchctl bootout gui/501/com.cobalt.radar` | exit 0 |
| (1) | `launchctl print gui/501/com.cobalt.radar` | exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| (1) | four counts | `<rp5>` 18 · `<rpr5>` 60 · `<re5>` 43 · `<lc5>` 39 |
| (1L) | — | `<launchd set>` empty |
| (2) | `git -C /Users/cobalt/cobalt log --oneline -1` | `7c460d39 Merge branch 'main' into deploy/cos-probe-fr2` = `<stack-final>` |
| (2) | `git -C /Users/cobalt/cobalt revert --no-edit -m 2 7c460d39` | `[main ebb5020c] Revert "Merge branch 'main' into deploy/cos-probe-fr2"` · 5 files, 44+, 442− |
| (2) PROOF | `git -C /Users/cobalt/cobalt diff --stat 00a3b61d HEAD -- . ':(exclude)docs'` | nothing — `<pre-merge>` restored |
| (3) | orphan-clean | not run — aset not booted out |
| (3) | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | exit 0 |
| (3) | `date` | restore Tue Oct 20 14:52:32 EDT 2026 — second outage 11 s (14:52:21 → 14:52:32) |
| (4)(a) | `launchctl print` radar / aset · `cobalt.sh status` | radar `state = running` pid 59996 (new); aset `state = running` pid 77363 (same); `Cobalt is ONLINE (PID: 35845).` |
| (4)(b) | counts | Started server process 289 = `<a0>` · Traceback aset 217 · Traceback radar 0 · TaxonomyConfigError 0 — all = baseline |
| (4)(c) | three curls | `200` · `200` · `200` |
| (4)(f) | `validate` · `jobs restarts 00a3b61d..7c460d39` | validate exit 0, `Jobs (F17): 22 registered — 7 resident, 15 one-shot.` ends `tree clean.`; restarts exit 0 `RESTARTS: com.cobalt.radar`, no `UNCLASSIFIED` |
| (4)(e) 1 | `date` 14:52:46 · `heartbeat show` | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 14:52:47 EDT)`: `RED archiver` (as `<hb0>`), `OK radar scanning (rth), members 50`, `com.cobalt.radar running 0 min, heartbeat fresh`; jobs RED archiver, replay, generated as `<hb0>`. No new RED |
| (4)(g) | — | no migration |
| (4)(b) tail | `date` 14:54:02 · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | `2026-10-20 14:53:58.499 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792522352332`, after the 14:52:32 restore; preceded by eleven `cards.expire: falling back to the session close (16:00:00)` INFO lines at 14:53:57; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN on the first tail |
| (4) READBACK | four counts after the settled tail | `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 = `<rp5>` `<rpr5>` `<re5>` `<lc5>` — no growth; Traceback radar.err 0 |
| (4)(e) 2 | `date` 14:54:38 · `heartbeat show` (112 s after read 1) | `HEARTBEAT RED — 3 job(s) and 2 probe(s)  (2026-10-20 14:54:39 EDT)`: `RED archiver` (as `<hb0>`), `RED  radar                    failed_stage bars: poll failures: 1` — THE CARRIED FAMILY (as `<hb0>`; `com.cobalt.radar running 2 min, heartbeat fresh`; radar.err cycle line 14:53:58, no traceback); jobs RED archiver, replay, generated as `<hb0>`. No new RED |
| (4) | `curl … /radar` | `200` |
| (5) | the last line | below |

## CONTINUE
next: STEP-D0 (gate green at Tue Oct 20 14:48:18 EDT 2026)
OUTAGE STARTING Tue Oct 20 14:51:04 EDT 2026 — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — the run ended at STEP-5 (residents up on the reverted tree, 14:54:57).

## DECISIONS
1. Marker 4's `after` value is wrong on the card. `grep -c -F "## 2026-10-20 — cos-probe-fr2"` counts two headings on the merged README: line 52 `## 2026-10-20 — cos-probe-fr2` (build) and line 55 `## 2026-10-20 — cos-probe-fr2 (check)` (check). The code landed as the gate proved it (markers 1–3 read their `after` values, D2.3 docs-only). Safe default taken: the hub's rule — (d) wrong is RED → STEP-5, one revert, nothing re-landed. The desk owns the re-land: either the RE-LAND string `git -C /Users/cobalt/cobalt revert --no-edit ebb5020c` with radar's restart, or `desk-launch.sh recut` on a card whose marker 4 is `after 2` (or a fixed string unique to one heading). Not his: no scope, money or schema change.

## RECORDS
- Downtime: com.cobalt.radar 11 s (14:51:16–14:51:27) + 11 s (14:52:21–14:52:32). Neither is over 300 s.
- `cobalt_dev`: not touched by this run (equal-tree clause). The check's gate recorded `cobalt_dev: 0013 — F2 = F0`, `.env: removed`. P4 found no `.env` under `cobalt-wt/*`.
- Carried RED, as read: `RED  radar  failed_stage bars: poll failures: 1; poll SNWV stale since 2026-10-20T18:43:15.206957+00:00` (D1), then `RED  radar  failed_stage bars: poll failures: 1` (STEP-5 (4)). Same family, radar running with a fresh heartbeat.
- Other RED named at D1 and unchanged throughout: probe `archiver` (last run FAILED 00:54 UTC, exit 1), jobs `com.cobalt.archiver` (Finviz 400 on WBD/i1), `com.cobalt.replay` (`archiver not done`), `com.cobalt.generated` (`GeneratedCommitRefused` — the pre-commit guard named a live hub `79a459de deploy-hub-hub-cos-restart-fr1`).
- D0: `?? .claude/settings.json.bak` is untracked on `main`. It is neither in D0's accepted list nor under a refused root (src/, tests/, ops/, configs/), so it was not a stop.
- Commits on `main` from this session: `00a3b61d` (D2.0 report); the ff-merge to `7c460d39`; `ebb5020c` (STEP-5 revert); this report's close commit. The allowlist probe's `b02066d7` was reset off at once (`reset --soft HEAD~1`, HEAD back to `c6aa6b47`).
- RETIRE OWED: none. BOOTSTRAP OWED: none.
- Cleanup owed (L46, desk's): gate worktree `/Users/cobalt/cobalt-wt/deploy-cos-probe-fr2` and branch `deploy/cos-probe-fr2` (its `.venv` was created by STEP-R's `uv run`); the set's worktree `/Users/cobalt/cobalt-wt/cos-probe-fr2` and branch `ops/cos-probe-fr2` — keep until the re-land is decided; tag `pre-cos-probe-fr2`.
- L74: a system reminder asked for a `Claude-Session:` line in commits. Recorded once under `## L74`; commits carry `Co-Authored-By` only.
- Card's `## RECORDS` (the desk's facts, copied): cos-probe-fr2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr2-check-2026-10-20.md` last line: CHECK DONE · job: cos-probe-fr2 · pass: 1 · tip: dfea631a · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 178055 / cos-probe-fr2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-probe-fr2` → `dfea631a`; code tip `dfea631a` / written by deploy-card.sh at 2026-10-20 14:46 ET (`date`); trial merge of the heads onto main in order: clean.
- THE RELEASE: no lock held by this run (no `.env` in the gate; `ls -la …/deploy-cos-probe-fr2/.env` → No such file at STEP-R).

FAILED: 4.7 (d) — marker 4 `grep -c -F "## 2026-10-20 — cos-probe-fr2" README.md` read 2, card after 1 (the string also matches the check's heading) · rollback: used — migrations applied: none — aset: not in the set — radar: UP — launchd: none · decisions: 1 · for Dejan: 0 · tokens: 229692
