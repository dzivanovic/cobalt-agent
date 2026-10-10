# deploy archiver-429-1009 · SET: none · MIGRATIONS: none

## §0 Headline
- Deployed `ops/archiver-429-1009` (tip `a4aef3a0`), which adds a typed Finviz 429 error to the archiver collector. `main` is now `b690235c`, tagged `deploy-2026-10-10-archiver-429`. Rollback tag `pre-archiver-429-1009` is at `3589655d`.
- The gate is the check's own run, under the equal-tree clause: offline 4145/0 · with-DB 5034/0 · live-note 146/0. No migration.
- aset and radar were down 15 s (01:37:20 → 01:37:35 ET). Smoke is GREEN. Snapshot `26e53e66` was taken before the merge.
- The archiver and replay REDs from 00:54 UTC remain until the archiver's next run on the new code.

## L74
- A system block after launch asked that commits carry a `Claude-Session:` line. Recorded once here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/212-deploy-archiver-429-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/212-deploy-archiver-429-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/212-deploy-archiver-429-card.md" · 0 · d192d7f09446a90209a057984686c56991a4829c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/212-deploy-archiver-429-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Sat Oct 10 01:33:28 EDT 2026` |
| P2 | `tail -n 3 ".../reports/archiver-429-check-2026-10-10.md"` | 0 | `CHECK DONE · job: archiver-429-1009 · pass: 1 · tip: a4aef3a0 · house A: Sol FINDINGS: 5 · findings: 9 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 2 · suites: offline 4145/0 · with-DB 5034/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 22 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 207006` — carries `held unfixed: 0` and `ready: YES`; `tip: a4aef3a0` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/archiver-429-check-2026-10-10.md"` | 0 | `2b243142f85784ac6e1ce1df066f370995e01f9e` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 a4aef3a0` | 0 | `a4aef3a0` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/archiver-429-1009` | 0 | `a4aef3a0` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a4aef3a0 ops/archiver-429-1009` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat a4aef3a0 ops/archiver-429-1009 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-archiver-429-1009 status --short --branch` | 0 | `## deploy/archiver-429-1009` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `d192d7f0` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d192d7f0 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/archiver-429-1009` | 0 | empty |
| P6 | `grep -c -F "class FinvizRateLimited" /Users/cobalt/cobalt/src/cobalt/archiver/collector.py` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main a4aef3a0 -- src/cobalt/db_migrations` | 0 | nothing — `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 79051` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 79064` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-archiver-429-1009 merge --no-edit a4aef3a0` → `Merge made by the 'ort' strategy.` (10 files, 732 insertions, 10 deletions: archiver `collector.py`, `report.py`, `runner.py`, their three tests, three DevDocs, the build report).
- `git -C <GATE> rev-parse --short=8 HEAD` → `905aef7a` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent d192d7f0..deploy/archiver-429-1009` → `905aef7a Merge commit 'a4aef3a0' into deploy/archiver-429-1009` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor a4aef3a0 deploy/archiver-429-1009` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat d192d7f0 deploy/archiver-429-1009 -- src/cobalt/db_migrations` → nothing (`MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat d192d7f0 deploy/archiver-429-1009 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first lines: uv created `.venv` in the gate, `Installed 253 packages in 796ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/archiver/collector.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/report.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/archiver-429-build-2026-10-09.md	A	DOCS	-
src/cobalt/archiver/collector.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/archiver/report.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/archiver/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_archiver_collector.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_report.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (the agent is not in the set).

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat a4aef3a0 905aef7a -- . ":(exclude)docs"` → nothing; the check's stop line carries `with-DB 5034/0` (above 0). The check's three suite lines are the gate's; (a)–(f) not run here. Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/archiver-429-check-2026-10-10.md` lines 194–211 (its `gate.sh archiver-429-1009 all --deploy` on tip `a4aef3a0`, exit 0):
```
offline 4145/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5034/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/archiver-429-1009-all-20261010-010159.log
```
(c) judgment kept, each skip against the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` named in the set; `test_replay_line.py:266` reason names `COBALT_TEST_LIVE_DRC`; `test_s3_c4_experiments.py:95` is `@requires_live` on `def test_x14_live_his_template_strips_to_the_committed_fixture` (grep in the gate: line 96). All seven inside the set. The live-note leg carries no skip naming `COBALT_LIVE_VAULT_ROOT`.
- `cobalt_dev: 0013 — F2 = F0` · `.env: removed` (the check's gate). This run took no lock and touched no `cobalt_dev`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 905aef7a

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 62]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (see `## RECORDS`). No staged line, no dirty `src/` `tests/` `ops/` `configs/` path |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat d192d7f0 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-archiver-429-1009` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-archiver-429-1009' (was d192d7f0)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 778f9f3b] …` · — · `d192d7f0 docs(desk): archiver 429 card 212 written, S4-P2 check launched (R821, R822)` (HEAD back) |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-archiver-429` | 1 | absent |
| TAG | `rev-parse --verify --quiet refs/tags/pre-archiver-429-1009` | 1 | absent |

### STEP-D1 (baseline, 01:35:09 EDT)
- `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>` (`HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 01:35:10 EDT)`). The REDs, quoted, none on the aset / sheet or radar probe:
  - `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC (4.7 h ago), rows written 3308843, exit 1`
  - `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' for url 'https://elite.finviz.com/export/stock?t=DKNG&p=i2&auth=[REDACTED:url_query_secret]'`
  - `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'` (a traceback excerpt from `jobs/wrapper.py` follows in the probe text)
  - the 429 is the defect this set fixes; named, not a stop. `OK   sheet HTTP … -> 200`, `OK   radar                    idle (overnight)`, `OK   com.cobalt.aset running loaded, pid 79051`, `OK   com.cobalt.radar running 133 min, heartbeat fresh`, `OK   com.cobalt.agent running pid 22243`. No carried radar family RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>`: `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line. `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` / `registry <-> ops/: 15 label(s), exact match.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 2.2 h old` (ssd ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 79051` = `<aset pid>`; `…/com.cobalt.radar` → `state = running`, `pid = 79064` = `<radar pid>`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-10 01:33:56.771`.
- LOG BASELINES: `<a0>` = 56 · `<ta0>` = 2 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … http://127.0.0.1:5010/radar` → `200`. MARKER `grep -c -F "class FinvizRateLimited" …/collector.py` → `0` (before).
- No migration: `<RB>`, census and D1-M not run.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy archiver-429-1009 — gate green on 905aef7a" …` → `[main 3589655d]`, `show --stat HEAD` lists the one report file (133 insertions). `rev-parse --short=8 main` → `3589655d` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `rev-parse --short=8 HEAD` → `b690235c` = `<stack-final>`; `b690235c^2` → `3589655d` = `<pre-merge>`; `merge-base --is-ancestor 905aef7a b690235c` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 905aef7a b690235c -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 2.2 h old`; `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6694.4 MB` · `ssd: snapshot 26e53e66 — 0 new / 3 changed, 27.5 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`. Snapshot id `26e53e66`.
- D2.5 `date` 01:36:46 → heartbeat at 01:36:47 (97 s, short); filled with `date` + heartbeat pairs (01:36:53, 01:36:58); the read at `2026-10-10 01:37:04 EDT` is 114 s after D1's 01:35:10: the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver` 429, `com.cobalt.replay`), nothing new; aset pid 79051, radar `running 135 min, heartbeat fresh`.
- D2.6 `date` → `Sat Oct 10 01:37:08 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-archiver-429-1009` → `rev-parse --short=8 pre-archiver-429-1009` → `3589655d`.

### STEP-4 (the outage)
- 4.1 `date` → `Sat Oct 10 01:37:20 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → exit 0; `launchctl print …/com.cobalt.aset` → `Could not find service "com.cobalt.aset" in domain for user gui: 501` (exit 113). `launchctl bootout gui/501/com.cobalt.radar` → exit 0; print → `Could not find service "com.cobalt.radar" …` (exit 113). Agent not in the set: untouched.
- 4.3 `rev-parse --short=8 HEAD` → `3589655d` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/archiver-429-1009` → `Updating 3589655d..b690235c` / `Fast-forward` (10 files, 732 insertions, 10 deletions).
- 4.4 `migrations applied: none` (`MIGRATIONS: none`).
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, same as `<val0>` (`13 trade_def(s) validated OK` … `Placement (docs/PLACEMENT.md): tree clean.`); `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`.
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → exit 0; `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → exit 0. `launchctl print` aset → `state = running`, `pid = 51224` (≠ 79051); radar → `state = running`, `pid = 51235` (≠ 79064). `date` → `Sat Oct 10 01:37:35 EDT 2026` = `<t up>`. Downtime 15 s.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` = 18 · `<rpr_up>` = 60 · `<re_up>` = 43 · `<lc_up>` = 39 (= D1's baselines).
- (a) `date` 01:37:55 · `launchctl print` aset → `state = running`, `pid = 51224` (NEW, ≠ 79051); radar → `state = running`, `pid = 51235` (NEW, ≠ 79064); `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent outside the set, same pid). GREEN.
- (b) `date` 01:37:58 · `grep -c "Started server process" …/aset.err` → `57` (> `<a0>` 56, ≤ 58) · `tail -n 30 …/aset.err` → last `INFO:     Started server process [51231]` then `2026-10-10 01:37:32.662 | INFO | cobalt.voice.web:voice_startup:183 - voice: scratch dir … locked by this process; start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` · Traceback aset `2` (= `<ta0>`), radar `0` (= `<tr0>`), TaxonomyConfigError `0` (= `<tc0>`).
- (c) `date` 01:38:03 · `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200`. GREEN.
- (d) MARKER `grep -c -F "class FinvizRateLimited" /Users/cobalt/cobalt/src/cobalt/archiver/collector.py` → `1` (after `1`). GREEN.
- (s) SMOKE READ, the typed 429 error: the same command → exit 0, count `1` (green: 1 or more). GREEN.
- (e) read 1, `date` 01:38:08 · heartbeat `2026-10-10 01:38:09 EDT`: the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver` 429 of 00:54 UTC, `com.cobalt.replay`), nothing new; `OK   com.cobalt.aset running loaded, pid 51224` · `OK   com.cobalt.radar running running 1 min, heartbeat fresh`.
- (f) `COBALT_ENV=production uv run cobalt jobs restarts 3589655d..b690235c` → exit 0, the same 10 rows as STEP-R, `RESTARTS: com.cobalt.aset com.cobalt.radar` = `<restart set>`, no `UNCLASSIFIED`. `COBALT_ENV=production uv run cobalt validate` → exit 0, as 4.5 (`Jobs (F17): 15 registered — 6 resident, 9 one-shot.`).
- (g) no migration: not run.
- (b) radar tails, spaced: tail 1 at `date` 01:39:06 (`<t up>` + 91 s) → last line `2026-10-10 01:37:33.366 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, 2 s BEFORE `<t up>` (the bootstrap ran before 4.6's `date`): not settling. Tail 2 at `date` 01:40:35 (`<t up>` + 180 s) → last line `2026-10-10 01:39:13.389 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, stamped after `<t up>`; the 12 lines carry no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback (startup vault/finviz-token lines only). GREEN; the third tail not needed.
- (e) read 2, heartbeat `2026-10-10 01:40:00 EDT` (111 s after read 1): the same three REDs as `<hb0>`, nothing new; `OK   com.cobalt.radar             running   running 2 min, heartbeat fresh`; aset pid 51224. GREEN. (Clock filled 01:38:17–01:40:31 with `date` + heartbeat pairs only; every one of them read the same.)
- (h) REVERT-READBACK at `date` 01:40:35 (`<t up>` + 180 s), after (b) settled: `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing; `curl … /radar` → `200`. No `census` line on the card. GREEN.
- THE CHAIN: the check committed (P2, `2b243142`) · tip `a4aef3a0` re-read and = head (P3) · merged tree `905aef7a`, one merge, no migration (T) · RESTARTS `com.cobalt.aset com.cobalt.radar` from the tool (R) · three suites green on the equal tree, offline 4145/0 · with-DB 5034/0 · live-note 146/0 (G, the equal-tree clause) · `<stack-final>` `b690235c` = `905aef7a` + docs (D2.3) · landed by fast-forward `3589655d..b690235c` (4.3) · marker 0 → 1 (d) · no migration (g) · both residents up on new pids (a) · radar cycling after `<t up>` (b, e) · the typed 429 read 1 (s) · no failure count grew (h). What the deploy fixes, the archiver's 429 handling, is read on the next archiver run, not here. The card surface cannot be read from here; the desk confirms it with him (L70).

### STEP-7
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-10-archiver-429` → exit 0; `rev-parse --short=8 deploy-2026-10-10-archiver-429` → `b690235c` = `rev-parse --short=8 main`.
- `<pre-merge>` `3589655d` → `<stack-final>` `b690235c` · tags `pre-archiver-429-1009` (at `3589655d`) and `deploy-2026-10-10-archiver-429` (at `b690235c`) · `<t down>` 01:37:20 / `<t up>` 01:37:35 / 15 s · uv sync: the gate's first `uv run` created `.venv` (`Installed 253 packages in 796ms`); the production tree printed no sync line · proof cost: none (no migration) · `migrations applied: none` · `<RB>`: none on the card · snapshot `26e53e66` · `RESTARTS done: com.cobalt.aset com.cobalt.radar`.
- THE ROLLBACK STRING: (1) CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 b690235c`, with `com.cobalt.aset` and `com.cobalt.radar` booted out first and bootstrapped after. (2) SCHEMA: none (no migration). (3) RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and its output verbatim. (2) `rev-parse --short=8 a4aef3a0` / `ops/archiver-429-1009` → `a4aef3a0` (P3); `merge-base --is-ancestor a4aef3a0 b690235c` → exit 0. (3) REVERT-READBACK shown at (h); every count, sha and line in this report was read from tool output in this run. (4) STEP-T printed `Merge made by the 'ort' strategy.` with no conflict; D2.1 the same.
- THE RELEASE: this run never took the lock. `ls -la /Users/cobalt/cobalt-wt/deploy-archiver-429-1009/.env` → `No such file or directory`.

## CONTINUE
OUTAGE STARTING 01:37:08 EDT — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED 01:37:35 EDT — residents up on b690235c.
next: none, deployed green.

## DECISIONS
1. D0's porcelain read lists `?? .claude/settings.json.bak`, an untracked file outside the accepted set (`docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`) and outside the refused classes (staged, `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not a refusal. It is untracked and not in the landed tree (D2.3 printed nothing), so it does not touch the deploy. Recorded for the desk, which decides whether to remove it or add it to the accepted list.

## RECORDS
- Downtime 15 s (01:37:20 → 01:37:35), under 300 s.
- `cobalt_dev`: untouched by this run. The gate evidence is the check's (`cobalt_dev: 0013 — F2 = F0`, `.env: removed`, log `/Users/cobalt/cobalt-wt/.gate-logs/archiver-429-1009-all-20261010-010159.log`).
- No `REFUSED` call and no message from another session.
- No `RETIRE OWED` (STEP-C: no plist changed).
- Carried RED, as read at D1 and unchanged through smoke: the `archiver` probe (`last run FAILED — last run 2026-10-10 00:54 UTC … exit 1`), `com.cobalt.archiver` (`429 Too Many Requests` for DKNG/i2) and `com.cobalt.replay` (`archiver not done: state 'failed'`). This set fixes that failure. Those REDs clear only when the archiver runs again on `b690235c`. Production radar is `idle (overnight)`: there is no carried radar-family RED.
- The radar's first cycle line after the bootstrap (01:37:33.366) came 2 s before 4.6's `date` (`<t up>` 01:37:35), so the 01:39:13 cycle settled (b).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-archiver-429-1009` and branch `deploy/archiver-429-1009`; the set's worktree `/Users/cobalt/cobalt-wt/archiver-429-1009` and branch `ops/archiver-429-1009`. The gate worktree now holds a `.venv` (uv created it at STEP-R).
- The card's `## RECORDS`, copied:
  - archiver-429-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/archiver-429-check-2026-10-10.md` last line: CHECK DONE · job: archiver-429-1009 · pass: 1 · tip: a4aef3a0 · house A: Sol FINDINGS: 5 · findings: 9 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 2 · suites: offline 4145/0 · with-DB 5034/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 22 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 207006
  - archiver-429-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/archiver-429-1009` → `a4aef3a0`; code tip `a4aef3a0`
  - written by deploy-card.sh at 2026-10-10 01:32 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one block, a system notice asking that commits carry a `Claude-Session:` line, recorded under `## L74`; not acted on.

DEPLOYED deploy-2026-10-10-archiver-429 b690235c | set: none | migrations: none | gate: offline 4145/0 · with-DB 5034/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 191568
