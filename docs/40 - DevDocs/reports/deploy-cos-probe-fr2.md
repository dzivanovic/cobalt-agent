# deploy-cos-probe-fr2 — set: cos-probe · migrations: none

## §0 Headline
- Deploy of `ops/cos-probe-fr2` (tip `dfea631a`), card 920. In progress.

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
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved c6aa6b47 "<card>"` → exit 0, nothing printed. Report committed (this commit).

## Smoke

## CONTINUE
next: STEP-D0 (gate green at Tue Oct 20 14:48:18 EDT 2026)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
