# deploy f5-x3-values-port · SET: f5-x3-values-port · MIGRATIONS: none

## §0 Headline
- Deployed `f5-x3-values-port` to production: `main` `8fe0c3af` → `4d82f2c1`, tag `deploy-2026-10-21-f5-x3-values-port`, rollback tag `pre-f5-x3-values-port`.
- Gate green on `e83245ca`: offline 9030/0 · with-DB 5876/0 · live-note 148/0; `cobalt_dev` back at 0013 (F2 = F0).
- Restarted `com.cobalt.aset` only (41 s down, 04:30:53 → 04:31:34 ET); no migration; snapshot `c83cbf86`.
- Smoke GREEN: the four `modelaccess.yaml` markers flipped to their after values, curls 200, radar cycling, no new RED (archiver/replay RED carried from before).
- Run 03:34:58 → 04:35 ET 2026-10-21. Decisions 0, for Dejan 0.

## L74
- One line: a `Claude-Session:` commit-trailer request arrived mid-session (system reminder); recorded under `## RECORDS`, not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/968-deploy-f5-x3-values-port-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/968-deploy-f5-x3-values-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/968-deploy-f5-x3-values-port-card.md" · 0 · dfd0ae61542319f78e67c23bc1abc754dfdfaf41
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/968-deploy-f5-x3-values-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Wed Oct 21 03:34:58 EDT 2026` (outside 21:30-22:30) |
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P2 | `tail -n 3 ".../f5-x3-values-port-check-2026-10-21.md"` | 0 | `CHECK DONE · job: f5-x3-values-port · pass: 1 · tip: fc2ffb3b · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9024/0 · with-DB 5870/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 129162` — carries `held unfixed: 0`, `ready: YES`, `tip: fc2ffb3b` = row |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../f5-x3-values-port-check-2026-10-21.md"` | 0 | `e27d015ca9fea152a59eacc51bc3cccf3813ee8f` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../f5-x3-values-port-check-2026-10-21.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 fc2ffb3b` | 0 | `fc2ffb3b` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-x3-values-port` | 0 | `2672dd43` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor fc2ffb3b 2672dd43` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat fc2ffb3b 2672dd43 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/f5-x3-values-port` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `65dd81c3` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 65dd81c3 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/f5-x3-values-port` | 0 | empty |
| P6 | `grep -c -F "source: UNMEASURED" ".../modelaccess.yaml"` | 0 | `2` (before `2`) |
| P6 | `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md" ...` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "(warm model)" ...` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "cold load 8.67 s from the mainframe log (proxy, not a live cold call)" ...` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 2672dd43 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 66700` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 66719` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` | 2 | `No such file or directory` → agent not retired |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit 2672dd43` → `Merge made by the 'ort' strategy.` (6 files: `configs/cobalt/modelaccess.yaml` 8 +-, `tests/cobalt/test_checkpoints_offline.py` +36, four docs files).
- `git -C <GATE> rev-parse --short=8 HEAD` → `e83245ca` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 65dd81c3..deploy/f5-x3-values-port` → `e83245ca Merge commit '2672dd43' into deploy/f5-x3-values-port` (one line, one head).
- `merge-base --is-ancestor fc2ffb3b deploy/f5-x3-values-port` → exit 0; `merge-base --is-ancestor 2672dd43 deploy/f5-x3-values-port` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 65dd81c3 deploy/f5-x3-values-port -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 65dd81c3 deploy/f5-x3-values-port -- configs ops` → ` configs/cobalt/modelaccess.yaml | 8 ++++----` / ` 1 file changed, 4 insertions(+), 4 deletions(-)`.
- STEP-C: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 65dd81c3 deploy/f5-x3-values-port` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (from `<GATE>`, `.env` No such file) → exit 0, table whole (after uv venv creation lines `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Installed 257 packages in 944ms`):
```
path	change	rule	restart
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/cto-2026-10-21.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-x3-values-port-build-2026-10-21.md	A	DOCS	-
docs/40 - DevDocs/reports/f5-x3-values-port-build-2026-10-21.result	A	DOCS	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
- No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset`. `<deferred set>` = empty. `<launchd set>` = empty. Agent not recorded retired (P8).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat fc2ffb3b e83245ca -- . ":(exclude)docs"` → 8 files (`configs/cobalt/jobs.yaml`, `configs/cobalt/taxonomy/tunables.yaml`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/heartbeat/runner.py`, four tests): `main` moved since the check → the gate runs whole (`--deploy`).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` (`.env` No such file) → `265 passed, 163 skipped in 19.30s` — 0 failed (skips are with-DB `Postgres env settings not available` / `requires_db`).
- Deselects: the build ran `gate.sh f5-x3-values-port all --deploy` with no `--deselect` of its own (build report `:142`); its pass-1 list (`:168`) is `gate-lists.md`'s. None added. TICKERS: none. MIGRATIONS: none.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-f5-x3-values-port all --deploy --deploy-gate` launched in background (`.env` No such file) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9030/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5876/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-f5-x3-values-port-all-20261021-033823.log
```
- (a) offline `9030/0` · W line `tests/ops: run (deploy gate)`. (c)+(c3) with-DB `5876/0`; every SKIPPED line is in the allowed set (named by test and reason). (c2) no FORWARD (MIGRATIONS: none). (e) live-note `148/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- (f) log `:1048` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:2330` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (equal) · `:2384` `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `:2385-2386` `release-devdb-lock.sh deploy-f5-x3-values-port` → `lock released` (the line carries no time; read at 04:26 ET). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-f5-x3-values-port" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file. `.env: removed (L76 lock released)`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on e83245ca

## Deploy table
| step | command | exit | result verbatim |
|---|---|---|---|
| D0 MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 51]` |
| D0 MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (see RECORDS); no staged line, no dirty `src/` `tests/` `ops/` `configs/` |
| D0 MAIN | `git -C /Users/cobalt/cobalt diff --stat 65dd81c3 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 PROBE | `tag scratch-allow-probe-f5-x3-values-port` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-f5-x3-values-port' (was 623083a2)` |
| D0 PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 4319b4e4] scratch: …` · — · `623083a2 docs(desk): R2272-R2274 933 DEPLOYED 1d6f649e, 958 port deploy launched, handover to 818d62f5` (HEAD back) |
| D0 TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-21-f5-x3-values-port` · `… refs/tags/pre-f5-x3-values-port` | 1 · 1 | neither exists |
| D1 | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | 0 · — | `Wed Oct 21 04:27:29 EDT 2026` · `<hb0>` = `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-21 04:27:30 EDT)`; REDs: `RED  archiver  last run FAILED — last run 2026-10-21 00:54 UTC (7.6 h ago), rows written 3373447, exit 1` · `RED  com.cobalt.archiver  failed  RuntimeError: 5 archiver failure(s): WBD/i1: Fetch failed for WBD/i1: Finviz HTTP failed: Client error '400 Bad Request' …` · `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. `OK sheet HTTP http://127.0.0.1:5010/ -> 200`, `OK radar scanning (premarket), members 50`, `OK com.cobalt.aset running loaded, pid 66700`, `OK com.cobalt.radar running running 58 min, heartbeat fresh`. No RED on aset / sheet / radar → named, not a stop |
| D1 | `COBALT_ENV=production uv run cobalt validate` | 0 | `<val0>`: `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`; `configs/cobalt/modelaccess.yaml -> com.cobalt.aset` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 1.0 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `<aset pid>` = `66700` |
| D1 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `<radar pid>` = `66719` |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 35845` | 0 · 0 | `Cobalt is ONLINE (PID: 35845).` · `35845 ??  0:00.03 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last `2026-10-21 04:25:55.060 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792571078017`; no traceback |
| D1 LOGS | `<a0>` `Started server process` aset.err · `<ta0>` Traceback aset.err · `<tr0>` Traceback radar.err · `<tc0>` TaxonomyConfigError radar.err | 0 · 0 · 1 · 1 | `292` · `217` · `0` · `0` |
| D1 LOGS | `<rp0>` `radar panel FAILED` · `<rpr0>` `radar pool refresh FAILED` · `<re0>` `radar S5 evaluate FAILED` · `<lc0>` `lifecycle card read failed` | 0 ×4 | `18` · `60` · `43` · `39` |
| D1 | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 MARKERS | the four `## MARKERS` greps | 0 · 1 · 1 · 1 | `2` · `0` · `0` · `0` (each its `before`) |
| D1 | THE LAUNCHD SET / `<RB>` / D1-M / cos | — | `<launchd set>` empty; MIGRATIONS: none; `com.cobalt.cos` not in `<restart set>` — no reads owed |
| D2.0 | `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 65dd81c3 "<card>"` | 0 | nothing |
| D2.0 | `add` · `commit -m "docs(report): deploy f5-x3-values-port — gate green on e83245ca" …` · `show --stat HEAD` | 0 · 0 · 0 | `[main 8fe0c3af] …` · one file `.../reports/deploy-f5-x3-values-port.md | 144 +++` |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `8fe0c3af` = `<pre-merge>` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (2 docs files) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 4d82f2c1^2` · `merge-base --is-ancestor e83245ca 4d82f2c1` | 0 · 0 · 0 | `4d82f2c1` = `<stack-final>` · `8fe0c3af` = `<pre-merge>` · ancestor |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat e83245ca 4d82f2c1 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 1.0 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 9822.3 MB` · `ssd: snapshot c83cbf86 — 0 new / 2 changed, 178.2 MB added, 1 pruned` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · — | `Wed Oct 21 04:30:19 EDT 2026` (170 s after D1) · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-21 04:30:19 EDT)`: the same three REDs as `<hb0>` (archiver, com.cobalt.archiver, com.cobalt.replay); aset pid 66700, radar `running 61 min, heartbeat fresh` — no new RED |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-f5-x3-values-port` | 0 · 0 | `Wed Oct 21 04:30:24 EDT 2026` · tag at `8fe0c3af` |
| 4.1 | `date` | 0 | `Wed Oct 21 04:30:53 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print gui/501/com.cobalt.aset` | 0 · 113 | — · `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 ORPHAN | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` | 0 | `orphan-clean: aset · none found` (no kill). Agent not in the set: not stopped |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `8fe0c3af` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/f5-x3-values-port` | 0 | `Updating 8fe0c3af..4d82f2c1` / `Fast-forward` (6 files, 446+/4-) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `launchctl print gui/501/com.cobalt.aset` | 0 · 0 | — · `state = running`, `pid = 6720` (≠ 66700) |
| 4.6 | `date` | 0 | `Wed Oct 21 04:31:34 EDT 2026` = `<t up>`; downtime 41 s |
| 4.6L | — | — | `<launchd set>` empty: nothing |
| 7.1 | `git -C /Users/cobalt/cobalt tag deploy-2026-10-21-f5-x3-values-port` | 0 | after the green smoke, at `4d82f2c1` |

CLOSE: `<pre-merge>` `8fe0c3af` → `<stack-final>` `4d82f2c1` · tags `pre-f5-x3-values-port` (`8fe0c3af`), `deploy-2026-10-21-f5-x3-values-port` (`4d82f2c1`) · `<t down>` 04:30:53 / `<t up>` 04:31:34 / 41 s · uv sync line: none in production (the gate worktree's first `uv run` created its `.venv`: `Installed 257 packages in 944ms`) · proof cost: none (no migration) · `migrations applied: none` · `<RB>` before / after: none · snapshot `c83cbf86` · `RESTARTS done: com.cobalt.aset` · `LAUNCHD done: none` · no `BOOTSTRAP OWED`.

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 4d82f2c1` — `com.cobalt.aset` booted out first, bootstrapped after; no launchd label.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and the output verbatim; (2) `merge-base --is-ancestor fc2ffb3b 4d82f2c1` → exit 0 and `merge-base --is-ancestor 2672dd43 4d82f2c1` → exit 0, both re-read at close; (3) REVERT-READBACK (h) shown above, `18 · 60 · 43 · 39` re-read at 04:34:35; every sha re-read from this run's tool output; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict marker. THE RELEASE: `ls -la <GATE>/.env` → No such file at close.

## Smoke
| row | date | command | result verbatim |
|---|---|---|---|
| first calls | after 04:31:34 | the four failure counts | `<rp_up>` `18` · `<rpr_up>` `60` · `<re_up>` `43` · `<lc_up>` `39` (= D1) |
| (a) | 04:31:52 | `launchctl print gui/501/com.cobalt.aset` (4.6) · `launchctl print gui/501/com.cobalt.radar` · `cobalt.sh status` | aset `state = running`, `pid = 6720` (NEW, ≠ 66700) · radar `state = running`, `pid = 66719` (SAME, outside the set) · `Cobalt is ONLINE (PID: 35845).` (same pid, agent outside the set) |
| (b) | 04:31:52 | `grep -c "Started server process" .../aset.err` | `293` (> `<a0>` 292, ≤ 294) |
| (b) | 04:31:52 | `tail -n 30 .../aset.err` | last `INFO:     Started server process [6720]` → `INFO:     Application startup complete.` → `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` |
| (b) | 04:31:52 | Traceback aset.err · Traceback radar.err · TaxonomyConfigError radar.err | `217` · `0` · `0` (= baseline) |
| (b) | 04:33:06 (`<t up>` + 92 s) | `tail -n 12 .../radar.err` | `2026-10-21 04:31:48.427 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792571431723` — after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN (settled at the first tail) |
| (c) | 04:32:09 | `curl … https://cobalt.taild24291.ts.net/` · `…/radar` · `…/radar\?frame=phone` | `200` · `200` · `200` |
| (d) | 04:32:09 | the four `## MARKERS` greps | `0` · `2` · `1` · `1` (each its `after`) |
| (s) | 04:32:09 | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` | exit 0, `200` — green |
| (s) | 04:32:09 | `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` | exit 0, `/Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` (listed; heartbeat shows it `OWED (deferred bootstrap) NOT LOADED`) — green |
| (f) | 04:32:17 | `COBALT_ENV=production uv run cobalt jobs restarts 8fe0c3af..4d82f2c1` | exit 0, `RESTARTS: com.cobalt.aset` = `<restart set>`; no `UNCLASSIFIED` |
| (f) | 04:32:31 | `COBALT_ENV=production uv run cobalt validate` | exit 0, as 4.5: `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` · `Placement (docs/PLACEMENT.md): tree clean.` |
| (e) 1 | 04:32:17 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-21 04:32:17 EDT)`: REDs only archiver / com.cobalt.archiver / com.cobalt.replay (= `<hb0>`); `OK com.cobalt.aset running loaded, pid 6720`; `OK com.cobalt.radar running running 63 min, heartbeat fresh` |
| (g) | — | — | MIGRATIONS: none |
| (e) 2 | 04:34:07 (110 s after (e) 1) | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-21 04:34:07 EDT)`: the same three REDs (in `<hb0>`), no new RED; `OK com.cobalt.aset running loaded, pid 6720`; `OK com.cobalt.radar running running 65 min, heartbeat fresh` |
| (h) | 04:34:35 (`<t up>` + 181 s) | the four failure counts · `curl …/radar` | `18` · `60` · `43` · `39` (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing) · `200`. No `census` reads on the card |

THE CHAIN: every check committed (P2 `e27d015c`) → the tips re-read (P3 `fc2ffb3b` / `2672dd43`) → the merged tree `e83245ca` (T) → RESTARTS derived `com.cobalt.aset` (R) → three suites green on `e83245ca` (G: offline 9030/0 · with-DB 5876/0 · live-note 148/0) → `<stack-final>` `4d82f2c1` = `<m1>` + docs (D2.3) → the landed code `8fe0c3af..4d82f2c1` (4.3) → markers flipped (d) → no migration (g) → aset up on a new pid after the merge, radar and agent untouched (a) → radar cycling (b, e) → the set's reads green (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

smoke: GREEN

## CONTINUE
- next: STEP-D0 (gate green at 04:26:31 ET)
- OUTAGE STARTING 04:30:24 ET — residents of com.cobalt.aset going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- outage ended 04:31:34 ET, aset up (pid 6720); smoke green; closed at STEP-7.

## DECISIONS
- none.

## RECORDS
- Downtime: aset 41 s (04:30:53 → 04:31:34 ET), under 300 s. Radar and agent not restarted (outside `<restart set>`).
- `cobalt_dev: 0013 (F2 = F0)` — gate log `:2330` / `:1048`, `664 35 272c95bbb12241e3611e4b36326ccf87`; lock released, `.env` removed.
- Carried RED as read (not this deploy's, not on aset / sheet / radar): `RED archiver last run FAILED — last run 2026-10-21 00:54 UTC …, exit 1`; `RED com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: … Finviz HTTP failed: Client error '400 Bad Request' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. Unchanged from D1 through smoke.
- D0: `?? .claude/settings.json.bak` is untracked on `main`; not on D0's accepted list and not under a refused prefix (`src/` `tests/` `ops/` `configs/`), so not a stop; the desk's to clean.
- No `REFUSED, not needed` line; no `CONTINUE` message received; no `RETIRE OWED`; no `BOOTSTRAP OWED` (STEP-C `ADMITTED 0`).
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-f5-x3-values-port` and branch `deploy/f5-x3-values-port`; set branch `ops/f5-x3-values-port` and its worktree.
- Card records (the desk's, copied): f5-x3-values-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-values-port-check-2026-10-21.md` last line: CHECK DONE · job: f5-x3-values-port · pass: 1 · tip: fc2ffb3b · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9024/0 · with-DB 5870/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 129162 / head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-x3-values-port` → `2672dd43`; code tip `fc2ffb3b` / written by deploy-card.sh at 2026-10-21 03:09 ET (`date`); trial merge of the heads onto main in order: clean.
- L74: a mid-session system reminder asked for a `Claude-Session:` trailer on commits; not a tool result, but the hub (L74) rules commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only — recorded once, not acted on.

DEPLOYED deploy-2026-10-21-f5-x3-values-port 4d82f2c1 | set: f5-x3-values-port | migrations: none | gate: offline 9030/0 · with-DB 5876/0 · live-note 148/0 | RESTARTS: com.cobalt.aset | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 200935
