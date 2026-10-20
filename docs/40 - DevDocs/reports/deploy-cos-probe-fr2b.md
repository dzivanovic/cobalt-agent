# deploy-cos-probe-fr2b — set: cos-probe · MIGRATIONS: none

## §0 Headline
- In progress: preflight green at 17:15 ET.

## L74
- A system reminder at session start asked for a `Claude-Session:` line in commits. Recorded as data; no action taken. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/927-deploy-cos-probe-fr2b-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/927-deploy-cos-probe-fr2b-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/927-deploy-cos-probe-fr2b-card.md" · 0 · b85d8f24a18ef73a76f49d9bf6163c4d51230683
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/927-deploy-cos-probe-fr2b-card.md" · 0 · nothing
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
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Tue Oct 20 17:15:32 EDT 2026`, outside 21:30-22:30 |
| P2 | `tail -n 3 ".../cos-probe-fr2b-check-2026-10-20.md"` | 0 | `CHECK DONE · job: cos-probe-fr2b · pass: 1 · tip: 9b912c83 · house A: Grok FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165122`: carries `held unfixed: 0`, `ready: YES`, `tip: 9b912c83` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/cos-probe-fr2b-check-2026-10-20.md"` | 0 | `f54a5a44f28840c5e32fc06c7382a3421487a964` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 9b912c83` | 0 | `9b912c83` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-probe-fr2b` | 0 | `cdac46c5` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9b912c83 cdac46c5` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 9b912c83 cdac46c5 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/cos-probe-fr2b` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `b85d8f24` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b85d8f24 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-probe-fr2b` | 0 | empty |
| P6 | marker 1 `grep -c -F "under the scratch HOME" .../probe.py` | 0 | `1` (before `1`) |
| P6 | marker 2 `grep -c -F ".claude.json" .../probe.py` | 0 | `2` (before `2`) |
| P6 | marker 3 `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes" .../test_cos_probe.py` | 1 | `0` (before `0`) |
| P6 | marker 4 `grep -c -F "## 2026-10-20 — cos-probe-fr2" ".../cos/README.md"` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main cdac46c5 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 77363` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 59996` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit cdac46c5` → `Merge made by the 'ort' strategy.` (5 files: cos/README.md, two build reports, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `b82f1ef4` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent b85d8f24..deploy/cos-probe-fr2b` → `b82f1ef4 Merge commit 'cdac46c5' into deploy/cos-probe-fr2b`.
- `merge-base --is-ancestor 9b912c83 deploy/cos-probe-fr2b` → 0 · `merge-base --is-ancestor cdac46c5 deploy/cos-probe-fr2b` → 0.
- `git -C /Users/cobalt/cobalt diff --stat b85d8f24 deploy/cos-probe-fr2b -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat b85d8f24 deploy/cos-probe-fr2b -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" b85d8f24 deploy/cos-probe-fr2b` → `STEP-C: ADMITTED 0`. `<launchd set>`: empty · `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after uv created `.venv` and installed 257 packages):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.result	A	DOCS	-
src/cobalt/cos/probe.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
- `<restart set>`: `com.cobalt.radar` · `<deferred set>`: empty · `<launchd set>`: empty. No UNCLASSIFIED row.

## L68 GATE
- EQUAL-TREE CLAUSE: one branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 9b912c83 b82f1ef4 -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5869/0` (above 0). The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr2b-check-2026-10-20.md` lines 223-248 (gate.sh `cos-probe-fr2b all --deploy --deploy-gate` on `9b912c83`, exit 0):
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr2b-all-20261020-162528.log
```
- SKIPPED judgment (c): each line is inside the allowed set, named by test. At the gate tree: `test_checkpoints_live.py:36` is the decorator of `test_dry_run_finds_the_heading_in_real_notes` (line 37); `test_playbook_live.py:31` decorates `test_live_vault_renders_six_decks` (line 32); `test_s3_c4_experiments.py:95` decorates `test_x14_live_his_template_strips_to_the_committed_fixture` (line 96); the others are listed by file:line and reason in the hub. The live-note skip is `COBALT_TEST_LIVE_DRC` (check log `:2456`).
- (a0) EARLY READ, run here: `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <17 files>` → `265 passed, 163 skipped in 19.76s` (0 failed; every skip is a with-DB skip: `Postgres env settings not available` / `requires_db: needs cobalt_dev`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- Lock: this run took no lock (the clause skipped (b)-(f)); `cobalt_dev: 0013 — F2 = F0` is the check's.
- GATE GREEN on b82f1ef4

## Deploy table
STEP-D0:
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 176]`; `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (untracked, not `src/`, `tests/`, `ops/`, `configs/`); no staged line.
- `git -C /Users/cobalt/cobalt diff --stat b85d8f24 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- Allowlist probe: `tag scratch-allow-probe-cos-probe-fr2b` → ok; `tag -d` → `Deleted tag 'scratch-allow-probe-cos-probe-fr2b' (was b85d8f24)`; `commit --allow-empty` → `[main b53bb079] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `b85d8f24 docs(prompts): 927 deploy card cos-probe-fr2b; R2193`.
- `rev-parse --verify --quiet refs/tags/deploy-2026-10-20-cos-probe-fr2b` → exit 1 · `refs/tags/pre-cos-probe-fr2b` → exit 1.

STEP-D1 (baseline):
- `date` → `Tue Oct 20 17:18:05 EDT 2026`. `<hb0>` = `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 17:18:07 EDT)`. OK: database, sheet HTTP (`http://127.0.0.1:5010/ -> 200`), sheet daymode, obsidian, mainframe, herdr, seat usage, backup, vault blocks, redactions, `radar  scanning (aftermarket), members 50`, `com.cobalt.aset running loaded, pid 77363`, `com.cobalt.agent running pid 35845`, `com.cobalt.radar running running 146 min, heartbeat fresh`, `com.cobalt.cos disabled … NOT LOADED BY DESIGN`. RED (named, not a stop: not the aset/sheet or radar probe): `RED  archiver  last run FAILED — last run 2026-10-20 00:54 UTC (20.4 h ago), rows written 3369418, exit 1`; `RED  com.cobalt.archiver  failed  RuntimeError: 5 archiver failure(s): WBD/i1: … Finviz HTTP failed: Client error '400 Bad Request' …`; `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`; `RED  com.cobalt.generated  failed  GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 79a459de deploy-hub-hub-cos-restart-fr1 …`. AMB: `com.cobalt.herdr unmanaged`. OWED (deferred bootstrap): prefill-refresh, checkpoint-0715/0745/0815/0845, playbook.
- `<val0>` = `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 2.5 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 77363` = `<aset pid>`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 59996` = `<radar pid>`; `launchctl print gui/501/com.cobalt.cos` → exit 113 `Could not find service "com.cobalt.cos" in domain for user gui: 501` (not in `<restart set>`; not loaded). `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ??  0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 7 `cards.expire: falling back to the session close` INFO lines, last `2026-10-20 17:18:04.689 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792530997131`.
- Log baselines: `<a0>` 289 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. Markers again: `1` · `2` · `0` · `0` (each its `before`).
- `<launchd set>` empty: nothing. MIGRATIONS: none: no `<RB>`, no D1-M.

## Smoke

## CONTINUE
- next: STEP-D2 (D2.0 report commit)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
