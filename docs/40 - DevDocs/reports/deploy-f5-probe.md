# deploy f5-probe — SET: f5-probe · MIGRATIONS: none

## §0 Headline
- DEPLOYED `ops/f5-probe` (`a25a4f91`): main `9d22f711` → `41be0e80`, tag `deploy-2026-10-21-f5-probe`, rollback tag `pre-f5-probe`.
- Gate: the check's (equal-tree clause) — offline 9070/0 · with-DB 5916/0 · live-note 148/0. MIGRATIONS: none.
- RESTARTS: com.cobalt.radar only; 30 s down (14:32:34 → 14:33:04 ET). aset and agent untouched.
- Smoke GREEN: radar cycling on the new code, markers at their after values, no new RED, no failure count grew.
- 1 decision (desk's, not his): an untracked `.claude/settings.json.bak` on main, not a stop.

## L74
- One harness system reminder (not a tool result) asked commit messages to end with a `Claude-Session:` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/984-deploy-f5-probe-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/984-deploy-f5-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/984-deploy-f5-probe-card.md" · 0 · 1c2da55fd4868d410d62b7571e5f520bd82b1cde
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/984-deploy-f5-probe-card.md" · 0 · nothing
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
| P0 | authorize.sh (above); `ls -la` the report | 0 · 1 | `AUTHORIZED`; report `No such file or directory` (first launch) |
| P1 | `date` | 0 | `Wed Oct 21 14:27:10 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 ".../f5-probe-check-2026-10-21.md"` | 0 | `CHECK DONE · job: f5-probe · pass: 1 · tip: a25a4f91 · … · held unfixed: 0 · … · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 211581` |
| P2 | `git log -1 --format=%H -- <check report>` | 0 | `98b8b1bd5d0a0a595d421f19b36fd2c542bceb5e` |
| P2 | `git diff --stat -- <check report>` | 0 | nothing |
| P3 | `rev-parse --short=8 a25a4f91` · `rev-parse --short=8 ops/f5-probe` | 0 · 0 | `a25a4f91` · `a25a4f91` |
| P3 | `merge-base --is-ancestor a25a4f91 a25a4f91` · `diff --stat a25a4f91 a25a4f91 -- . ':(exclude)docs'` | 0 · 0 | exit 0 · nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (lock free) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f5-probe` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `1c2da55f` |
| P5 | `merge-base --is-ancestor 1c2da55f main` · `log --oneline main..deploy/f5-probe` | 0 · 0 | exit 0 · empty |
| P6 | `ls .../prefill/checkpoint_probe.py` | 1 | `No such file or directory` (before) |
| P6 | `grep -c -F "PROBE_ITEMS = (" .../prefill/checkpoints.py` | 1 | `0` (before) |
| P6 | `ls .../tests/cobalt/test_checkpoint_probe.py` | 1 | `No such file or directory` (before) |
| P7 | `diff --stat main a25a4f91 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 6720 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 66719 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" .../ops/desk/retired-labels` | 2 | `No such file or directory` = not retired |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit a25a4f91` → `Merge made by the 'ort' strategy.` (8 files, 1139 insertions, 7 deletions; code: `src/cobalt/prefill/checkpoint_probe.py` A, `src/cobalt/prefill/checkpoints.py` M, `tests/cobalt/test_checkpoint_probe.py` A, `tests/cobalt/test_checkpoints_offline.py` M).
- `<m1>` = `8a3ea6ed`.
- `log --oneline --merges --first-parent 1c2da55f..deploy/f5-probe` → `8a3ea6ed Merge commit 'a25a4f91' into deploy/f5-probe`.
- `merge-base --is-ancestor a25a4f91 deploy/f5-probe` → exit 0.
- `diff --stat 1c2da55f deploy/f5-probe -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `diff --stat 1c2da55f deploy/f5-probe -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 1c2da55f deploy/f5-probe` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, `Installed 257 packages in 757ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-probe-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-probe-build-2026-10-21.result	A	DOCS	-
src/cobalt/prefill/checkpoint_probe.py	A	static import reach	com.cobalt.radar
src/cobalt/prefill/checkpoints.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_checkpoint_probe.py	A	test/documentation; no resident	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
- No UNCLASSIFIED row. `<restart set>` = `com.cobalt.radar`. `<deferred set>` = none. `<launchd set>` = none.

## L68 GATE
THE EQUAL-TREE CLAUSE holds: one branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat a25a4f91 8a3ea6ed -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5916/0` (> 0). The check's suite lines are the gate's; (a)–(f) skipped. Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-check-2026-10-21.md` lines 160-180 (`gate.sh f5-probe all --deploy --deploy-gate`, exit 0, on `a25a4f91`):
```
tests/ops: run (deploy gate)
offline 9070/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5916/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-probe-all-20261021-133310.log
```
- SKIPPED read against the allowed set: every line inside it. `test_checkpoints_live.py:36` = `@requires_live` on `test_dry_run_finds_the_heading_in_real_notes` (line 37); `test_playbook_live.py:31` = `test_live_vault_renders_six_decks` (line 32); `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (line 96); the rest by file:line and reason as listed.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 8a3ea6ed

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `status --short --branch` | 0 | `## main...origin/main [ahead 81]` |
| MAIN | `status --porcelain` | 0 | no staged line; ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (see `## DECISIONS` 1) |
| MAIN | `diff --stat 1c2da55f main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-f5-probe` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-f5-probe' (was 1c2da55f)` |
| PROBE | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 6ffe2b74] …` · — · `1c2da55f docs(desk): deploy card 984 f5-probe, R2295-R2296` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-21-f5-probe` · `…/pre-f5-probe` | 1 · 1 | absent · absent |

### STEP-D1 (`date` → `Wed Oct 21 14:29:44 EDT 2026`)
- `<hb0>` (`heartbeat show`, 14:29:45 EDT): `HEARTBEAT RED — 2 job(s) and 2 probe(s)`. OK: database, `sheet HTTP http://127.0.0.1:5010/ -> 200`, sheet daymode, obsidian, mainframe, herdr, seat usage, backup, vault blocks, redactions, `com.cobalt.aset running loaded, pid 6720`, `com.cobalt.agent running pid 35845`, `com.cobalt.radar running running 660 min, heartbeat fresh`. RED (named, not a stop): `RED  archiver  last run FAILED — last run 2026-10-21 00:54 UTC (17.6 h ago), rows written 3373447, exit 1`; `RED  com.cobalt.archiver  failed  RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed … Finviz HTTP failed: Client error '400 Bad Request' …`; `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. CARRIED FAMILY (quoted whole): `RED  radar                    failed_stage bars: poll failures: 1` — radar `running`, `heartbeat fresh`, `radar.err` `14:27:41.561 … radar cycle: scanning scan_id=1792607175624` (inside 5 min), no traceback. AMB `com.cobalt.herdr` unmanaged (declared interim). OWED (deferred bootstrap, not red): cos, hitl, prefill-refresh, checkpoint-0715/0745/0815/0845, playbook.
- `<val0>`: `validate` exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 10.0 h old` (ssd ARMED).
- `launchctl print … aset` → `state = running`, `<aset pid>` 6720 · `… radar` → `state = running`, `<radar pid>` 66719 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).` · `ps -p 35845` → `35845 ?? 0:00.03 uv run src/cobalt_agent/main.py`. `com.cobalt.cos` not in `<restart set>` (no read).
- `tail -n 8 radar.err`: last lines `14:29:33.732 … radar price floor 5.0: …` (no traceback).
- LOG BASELINES: `<a0>` 293 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again: `No such file or directory` · `0` · `No such file or directory` (before values).
- THE LAUNCHD SET: empty. No migration: no `<RB>`, no D1-M.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 1c2da55f "<card>"` → nothing. `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-f5-probe.md"` → `[main 9d22f711] docs(report): deploy f5-probe — gate green on 8a3ea6ed`, `1 file changed, 138 insertions(+)`; `show --stat HEAD` lists that one file. `<pre-merge>` = `9d22f711`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `41be0e80`; `rev-parse --short=8 41be0e80^2` → `9d22f711` = `<pre-merge>`; `merge-base --is-ancestor 8a3ea6ed 41be0e80` → exit 0.
- D2.3 `diff --stat 8a3ea6ed 41be0e80 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 10.0 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 10076.5 MB`, `ssd: snapshot 1a1f423d — 15 new / 2 changed, 361.3 MB added, 1 pruned`, `F17: com.cobalt.backup DONE`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Wed Oct 21 14:32:13 EDT 2026` (149 s after D1's 14:29:44); `heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)`: aset / sheet OK, `OK   radar  scanning (rth), members 50`, `com.cobalt.radar running running 663 min, heartbeat fresh`; RED only archiver, com.cobalt.archiver, com.cobalt.replay (all in `<hb0>`). No new RED.
- D2.6 `date` → `Wed Oct 21 14:32:20 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-f5-probe` at `9d22f711` → exit 0.

### STEP-4 (the outage, `<restart set>` = com.cobalt.radar)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = `Wed Oct 21 14:32:34 EDT 2026` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501`. aset not in the set: no orphan-clean; agent not in the set. |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/f5-probe` | `9d22f711` = `<pre-merge>` · `Updating 9d22f711..41be0e80` / `Fast-forward` (8 files, 1139+, 7-) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print …` | exit 0 · `state = running`, `pid = 6354` (≠ D1's 66719), `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` |
| 4.6 | `date` | `<t up>` = `Wed Oct 21 14:33:04 EDT 2026` · downtime 30 s |
| 4.6L | — | `<launchd set>` empty: nothing |

### Summary
- `<pre-merge>` `9d22f711` → `<stack-final>` `41be0e80` (main). Tags: `pre-f5-probe` at `9d22f711`; `deploy-2026-10-21-f5-probe` at `41be0e80` (STEP-7, after green smoke).
- `<t down>` 14:32:34 · `<t up>` 14:33:04 · 30 s.
- uv sync: none on production (STEP-R's `.venv` creation was in `<GATE>`). Proof cost: none (no migration). `migrations applied: none`. `<RB>`: none.
- Snapshot: `ssd: snapshot 1a1f423d`.
- RESTARTS done: com.cobalt.radar. LAUNCHD done: none. BOOTSTRAP OWED: none.
- ROLLBACK STRING (the desk's): 1. CODE: `launchctl bootout gui/501/com.cobalt.radar`, then `git -C /Users/cobalt/cobalt revert --no-edit -m 2 41be0e80`, then `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
| row | `date` | command | result |
|---|---|---|---|
| first | 14:33:04 (`<t up>`) | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 |
| (a) | 14:33:18 | `launchctl print … aset` · `… radar` · `cobalt.sh status` | aset `state = running`, `pid = 6720` (SAME, outside the set) · radar `state = running`, `pid = 6354` (NEW, ≠ 66719) · `Cobalt is ONLINE (PID: 35845).` |
| (b) | 14:33:23 | `grep -c "Started server process" aset.err` · `tail -n 30 aset.err` · Traceback aset / radar · TaxonomyConfigError | `293` = `<a0>` (aset outside the set) · last entry `11:14:49 … [WRITE] updated … card-20261021T111448`, no traceback · `217` = `<ta0>` · `0` = `<tr0>` · `0` = `<tc0>` |
| (c) | 14:33:30 | `curl … /` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` |
| (d) | 14:33:30 | the three `## MARKERS` | `/Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` · `1` · `/Users/cobalt/cobalt/tests/cobalt/test_checkpoint_probe.py` (each its `after`) |
| (s) | 14:33:30 | `ls …/prefill/checkpoint_probe.py` · `ls …/ops/com.cobalt.checkpoint-0715.plist` | exit 0, listed · exit 0, `/Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` (heartbeat: checkpoint-0715 `OWED (deferred bootstrap) NOT LOADED`, unloaded as the card says) |
| (f) | 14:33:39 | `jobs restarts 9d22f711..41be0e80` · `validate` | exit 0, `RESTARTS: com.cobalt.radar` = `<restart set>`, no UNCLASSIFIED · exit 0, `Jobs (F17): 22 registered — 7 resident, 15 one-shot.` = `<jobs0>`, `tree clean.` |
| (e) 1 | 14:33:50 | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)`: RED archiver, com.cobalt.archiver, com.cobalt.replay (all in `<hb0>`); `OK radar scanning (rth), members 50`; `com.cobalt.radar running running 1 min, heartbeat fresh`. No new RED. |
| (g) | — | — | no migration |
| (b) tail 2 | 14:35:57 (`<t up>` + 173 s) | `tail -n 12 radar.err` | same 12 lines, last `14:34:25.581 … radar cycle: scanning scan_id=1792607578890`; no failure line, no traceback |
| (b) tail 1 | 14:34:36 (`<t up>` + 92 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | `2026-10-21 14:34:25.581 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792607578890` (after `<t up>`); the other 11 lines `cards.expire: falling back to the session close …` INFO; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN, settled |
| (e) 2 | 14:35:41 (heartbeat 14:35:47, 117 s after read 1) | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)`: same three REDs as `<hb0>`; `OK radar scanning (rth), members 50`; `com.cobalt.radar running running 3 min, heartbeat fresh`. No new RED. |
| (h) | 14:36:11 (`<t up>` + 187 s) | the four failure counts · `curl … /radar` · radar Traceback | `18` `60` `43` `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200` · `0`. No `census` reads on the card. |

SMOKE: GREEN.

THE CHAIN: every check committed (P2: `98b8b1bd…`, `ready: YES`, `held unfixed: 0`) → the tip re-read (P3: `a25a4f91` = head) → the merged tree (T: `8a3ea6ed`, clean) → RESTARTS derived (R: `com.cobalt.radar`) → three suites green on `<m1>` (G, equal-tree clause: offline 9070/0 · with-DB 5916/0 · live-note 148/0) → `<stack-final>` `41be0e80` = `<m1>` + docs (D2.3: nothing) → the landed code (4.3: `Updating 9d22f711..41be0e80`) → markers (d: after values) → no migration (g) → residents up after the merge (a: radar pid 6354 new, aset 6720 same, agent ONLINE) → radar cycling (b: `14:34:25 radar cycle: scanning`; e: two reads, no new RED) → the set's reads (s: both listed) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and the verbatim output. (2) `rev-parse --short=8 a25a4f91` / `ops/f5-probe` → `a25a4f91` (P3); `merge-base --is-ancestor a25a4f91 41be0e80` → exit 0; `rev-parse --short=8 HEAD` → `41be0e80`. (3) REVERT-READBACK on green = (h) above; every count and sha in this report was read from tool output this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); `git -C <GATE> status --short --branch` → `## deploy/f5-probe` (no conflict).
THE RELEASE: this run never took the lock. `ls -la <GATE>/.env` → `No such file or directory`; the lock dir exists (`owner`, 14:28, another session's) and `grep -c -x -F "deploy-f5-probe" …/.cobalt_dev.lock/owner` → `0` (not this worktree's).
STEP-7: `git -C /Users/cobalt/cobalt tag deploy-2026-10-21-f5-probe` → exit 0 (at `41be0e80`).

## CONTINUE
next: STEP-D0 (gate green at 14:28:49 ET)
- D0 and D1 done 14:29-14:31 ET. next: D2.0 commit, then D2.1.
- OUTAGE STARTING 14:32:20 ET — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- Outage ended 14:33:04 ET (radar up, pid 6354). Smoke GREEN 14:36:11 ET. next: none — deploy closed.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main` and outside D0's ACCEPTED list, but it is not in `src/`, `tests/`, `ops/` or `configs/`, so the REFUSED rule does not apply. Safe default taken: not a stop (it is untracked and outside the tree that lands). [14:29:44 ET]

## RECORDS
- Downtime: radar 30 s (14:32:34 → 14:33:04 ET); aset and agent not restarted.
- REFUSED, not needed: none. Messages not followed: none.
- `cobalt_dev: 0013 (F2 = F0)` — from the check's gate (equal-tree clause); this run took no lock and touched no dev DB.
- RETIRE OWED: none. BOOTSTRAP OWED: none from this run (STEP-C `ADMITTED 0`).
- The carried RED as read at D1: `RED  radar  failed_stage bars: poll failures: 1` (cleared by D2.5: `OK radar scanning (rth), members 50`). Standing REDs not of this set: archiver (`last run FAILED … exit 1`), com.cobalt.archiver (`Finviz HTTP failed: Client error '400 Bad Request'` on WBD/i1), com.cobalt.replay (`archiver not done: state 'failed'`).
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-f5-probe` and branch `deploy/f5-probe`; the set's branch `ops/f5-probe` and its worktree.
- Card `## RECORDS` (the desk's):
  - f5-probe: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-check-2026-10-21.md` last line: CHECK DONE · job: f5-probe · pass: 1 · tip: a25a4f91 · house A: Grok FINDINGS: 6 · findings: 7 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 5 · house B: none available · suites: offline 9070/0 · with-DB 5916/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 211581
  - f5-probe: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-probe` → `a25a4f91`; code tip `a25a4f91`
  - written by deploy-card.sh at 2026-10-21 14:26 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one harness reminder asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on.

DEPLOYED deploy-2026-10-21-f5-probe 41be0e80 | set: f5-probe | migrations: none | gate: offline 9070/0 · with-DB 5916/0 · live-note 148/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 185187
