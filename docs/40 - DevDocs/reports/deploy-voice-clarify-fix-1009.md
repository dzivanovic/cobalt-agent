# deploy voice-clarify-fix-1009 · SET: none · MIGRATIONS: none

## §0 Headline
- `ops/voice-clarify-fix-1009` (code tip `9feda305`, head `4465b758`) is live on `main` at `f4f0af50` and tagged `deploy-2026-10-09-voice-clarify-fix`.
- Gate green on `13698c03`: offline 4060/0 · with-DB 4947/0 · live-note 146/0. `cobalt_dev` is back at 0013 with F2 = F0, and the lock is released.
- aset and radar were restarted. Downtime was 15 s (22:42:34 → 22:42:49 EDT). No migration ran.
- Smoke GREEN: both markers read 1, all three curls returned 200, radar is cycling, and the four failure counts did not move.

## L74
- A system-reminder arriving mid-session asked that commits carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md" · 0 · 4ab4e76035069e7e205653838a13ccd691b07088
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/200-deploy-voice-clarify-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 DATE | `date` | 0 | Fri Oct  9 22:10:32 EDT 2026 |
| P2 check last line | `tail -n 3 ".../voice-clarify-fix-check-2026-10-09.md"` | 0 | `CHECK DONE · job: voice-clarify-fix-1009 · pass: 1 · tip: 9feda305 · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 161041` — carries `held unfixed: 0` and `ready: YES`; `tip: 9feda305` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/voice-clarify-fix-check-2026-10-09.md"` | 0 | c6ef303f1bb813e11641708f3ea0bc8d665c1785 |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | (nothing) |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 9feda305` | 0 | 9feda305 |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/voice-clarify-fix-1009` | 0 | 4465b758 (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 9feda305 4465b758` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 9feda305 4465b758 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-voice-clarify-fix-1009 status --short --branch` | 0 | `## deploy/voice-clarify-fix-1009` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `5fc1e9a4` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5fc1e9a4 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/voice-clarify-fix-1009` | 0 | (empty) |
| P6 marker 1 | `grep -c -F "#cv-voice .cv-row[hidden]{display:none}" /Users/cobalt/cobalt/src/cobalt/voice/web.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "\"candidates\"" /Users/cobalt/cobalt/src/cobalt/voice/turn.py` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 4465b758 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 14669` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 14679` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 4465b758` → `Merge made by the 'ort' strategy.` (14 files, 287 insertions, 2 deletions: `src/cobalt/voice/{agent,tools,turn,web}.py`, four voice tests, one fixture, docs).
- `<m1>` = `13698c03` (`git -C <GATE> rev-parse --short=8 HEAD`).
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 5fc1e9a4..deploy/voice-clarify-fix-1009` → `13698c03 Merge commit '4465b758' into deploy/voice-clarify-fix-1009` (one line, one head).
- `merge-base --is-ancestor 9feda305 deploy/voice-clarify-fix-1009` → exit 0; `merge-base --is-ancestor 4465b758 deploy/voice-clarify-fix-1009` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 5fc1e9a4 deploy/voice-clarify-fix-1009 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 5fc1e9a4 deploy/voice-clarify-fix-1009 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 1.04s`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/voice/agent.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/tools.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/turn.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/web.md	M	DOCS	-
docs/40 - DevDocs/reports/voice-clarify-fix-build-2026-10-09.md	A	DOCS	-
src/cobalt/voice/agent.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/tools.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/turn.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_voice_plan.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_tools.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_turn.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
tests/fixtures/voice/plan-replies.constructed.yaml	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (agent not in the set).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 9feda305 13698c03 -- . ":(exclude)docs"` → ` configs/cobalt/rules.yaml | 2 +-` — not empty, so the gate runs whole (`--deploy`).
- Deselects: the build report (`voice-clarify-fix-build-2026-10-09.md:125`) says `no --deselect: no with-DB test added`; none passed. TICKERS none, no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 16.27s` (0 failed; the skips are the with-DB tests, absent `.env`).

- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-voice-clarify-fix-1009 all --deploy` (launched 22:12 ET, run_in_background) → exit 0. Verdict lines whole:
```
offline 4060/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4947/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-voice-clarify-fix-1009-all-20261009-221210.log
```
- (a) offline `<p>` = 4060, 0 failed.
- (c) the seven SKIPPED lines are all in the allowed set. `test_s3_c4_experiments.py:95` is the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`).
- (c2) log `:1096` `dev forward: APPLIED 22:35:03`. The proof tables at `:1162` and `:1957` read `content UNCHANGED on every table`. `grep -n -F "CHANGED"` shows no `CHANGED` verdict.
- (c3) with-DB `<d>` = 4947, 0 failed.
- (f) log `:2018` `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `:2019–2023`, `release-devdb-lock.sh deploy-voice-clarify-fix-1009` → `lock released` → `.env` No such file. Re-checked by `ls -la <GATE>/.env` → No such file, and `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file. `.env: removed (L76 lock released, before 22:40:01 ET)`.
- (e) live-note `<l>` = 146, 0 failed. Its one skip names `COBALT_TEST_LIVE_DRC`, which is in the allowed set.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 13698c03

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 8]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M` and `??` only under `docs/40 - DevDocs/`, plus `?? .claude/settings.json.bak` (not under `src/` `tests/` `ops/` `configs/`; recorded). No staged line. |
| main since cut | `git -C /Users/cobalt/cobalt diff --stat 5fc1e9a4 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| probe tag | `tag scratch-allow-probe-voice-clarify-fix-1009` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-voice-clarify-fix-1009' (was 5fc1e9a4)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 7df81a88] scratch: …` → HEAD back at `5fc1e9a4 docs(desk): desk pane by id DEPLOYED, https and S4-P1 check reports (R795)` |
| TAG free | `rev-parse --verify --quiet refs/tags/deploy-2026-10-09-voice-clarify-fix` | 1 | — |
| rollback tag free | `rev-parse --verify --quiet refs/tags/pre-voice-clarify-fix-1009` | 1 | — |

### STEP-D1 (baseline, 22:40:28 EDT)
- `<hb0>` (`heartbeat show` 22:40:29): `HEARTBEAT RED — 2 job(s) and 1 probe(s)`. The REDs are `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (1.8 h ago), rows written 3308843, exit 1`, `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` and `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. None is on the aset, sheet or radar probe: they are named here and do not stop the run. `OK sheet HTTP … -> 200` · `OK radar idle (overnight)` · `OK com.cobalt.aset running loaded, pid 14669` · `OK com.cobalt.radar running running 254 min, heartbeat fresh` · `OK com.cobalt.agent running pid 22243 alive`.
- `<val0>` (`validate`): exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.6 h old` (ssd local ARMED).
- aset `state = running`, `<aset pid>` = 14669 · radar `state = running`, `<radar pid>` = 14679 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → `radar cycle: idle:overnight scan_id=None` every ~100 s, last at `2026-10-09 22:40:12.375`; no traceback.
- Log baselines: `<a0>` 54 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: marker 1 → `0`, marker 2 → `0` (the before values).
- MIGRATIONS: none, so there is no `<RB>`, no census and no D1-M.

### STEP-D2
- D2.0: `git -C /Users/cobalt/cobalt add` + `commit … -- "<REPORT>"` → `[main 86ee64d4] docs(report): deploy voice-clarify-fix-1009 — gate green on 13698c03`. `show --stat HEAD` lists the one file (143 insertions). `<pre-merge>` = `86ee64d4`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2: `<stack-final>` = `f4f0af50`; `rev-parse --short=8 f4f0af50^2` → `86ee64d4` = `<pre-merge>`; `merge-base --is-ancestor 13698c03 f4f0af50` → exit 0.
- D2.3: `git -C /Users/cobalt/cobalt diff --stat 13698c03 f4f0af50 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4: `backup status` before → `newest snapshot: 0.6 h old` · `backup run` (22:41:17–22:42:01) → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6694.4 MB` · `ssd: snapshot 401fc6d1 — 0 new / 2 changed, 27.5 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5: `date` 22:42:19 · `heartbeat show` 22:42:21 (112 s after D1's 22:40:29). Same three REDs as `<hb0>` (archiver ×2, replay); no new RED. aset pid 14669, radar `heartbeat fresh`.
- D2.6: `date` → `Fri Oct  9 22:42:25 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-voice-clarify-fix-1009` at `86ee64d4`.

### STEP-4 (the outage)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = Fri Oct  9 22:42:34 EDT 2026 |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print …` | (no output) · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print …` | (no output) · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `86ee64d4` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/voice-clarify-fix-1009` | `Updating 86ee64d4..f4f0af50` / `Fast-forward` (14 files, 287+/2−) |
| 4.4 | — | `migrations applied: none` (MIGRATIONS: none; no uv sync line) |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | (no output) · print → `state = running`, pid 55969 (≠ 14669) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | (no output) · print → `state = running`, pid 55984 (≠ 14679) |
| 4.6 | `date` | `<t up>` = Fri Oct  9 22:42:49 EDT 2026 · downtime 15 s |

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
- (a) `date` 22:43:02 · aset `state = running`, pid 55969 (new, ≠ 14669) · radar `state = running`, pid 55984 (new, ≠ 14679) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent outside the set: same pid). GREEN.
- (b) `grep -c "Started server process" aset.err` → 55 (`<a0>` 54; > 54, ≤ 56). `tail -n 30 aset.err` → `INFO:     Started server process [55975]` · `voice: scratch dir … locked by this process; start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`. The tail also shows the old process shutting down: `Finished server process [14675]` and a `resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown` UserWarning, which is not a traceback. Tracebacks: aset 2 = `<ta0>` · radar 0 = `<tr0>` · TaxonomyConfigError 0 = `<tc0>`.
- (c) run between the 22:43:02 and 22:43:15 `date` calls; (b) and (c) were not each preceded by their own `date` (recorded under `## RECORDS`) · `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `grep -c -F "#cv-voice .cv-row[hidden]{display:none}" …/voice/web.py` → `1` (after `1`) · `grep -c -F "\"candidates\"" …/voice/turn.py` → `1` (after `1`). GREEN.
- (f) `date` 22:43:15 · `COBALT_ENV=production uv run cobalt jobs restarts 86ee64d4..f4f0af50` → exit 0, same 14 rows as STEP-R, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.aset com.cobalt.radar` = `<restart set>` · `validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`, `Placement (docs/PLACEMENT.md): tree clean.` GREEN.
- (g) no migration: not run.
- (s) SMOKE READS: the hidden-row rule `grep -c -F "#cv-voice .cv-row[hidden]{display:none}" /Users/cobalt/cobalt/src/cobalt/voice/web.py` → exit 0, `1` (green: 1 or more) · the plan clarify candidates `grep -c -F "\"candidates\"" /Users/cobalt/cobalt/src/cobalt/voice/turn.py` → exit 0, `1` (green: 1 or more). The tests behind them ran in the gate (with-DB 4947/0, offline 4060/0).
- (e) read 1: `date` 22:43:21 · `heartbeat show` 22:43:22 → the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`), nothing new · `OK com.cobalt.aset running loaded, pid 55969` · `OK com.cobalt.radar running running 1 min, heartbeat fresh` · `OK sheet HTTP … -> 200`.

- (b) THE SPACED TAILS: `date` 22:44:19 (`<t up>` + 90 s) · `tail -n 12 radar.err` → `F17: com.cobalt.radar RUNNING (timeout 300s, heartbeat every 100s)` at 22:42:48.171, then `radar cycle: idle:overnight scan_id=None` at 22:42:48.285. That cycle line is one second before `<t up>`, so it does not settle (b). `date` 22:45:49 (`<t up>` + 180 s) · `tail -n 12 radar.err` → `2026-10-09 22:44:28.306 | INFO | cobalt.radar.runner:resident:576 - radar cycle: idle:overnight scan_id=None`: a cycle after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback. Settled GREEN at the second tail, so the third was not needed. `grep -c "Traceback" radar.err` → 0.
- (e) read 2: `date` 22:45:12 · `heartbeat show` 22:45:14, 112 s after read 1 → the same three REDs as `<hb0>`, nothing new · `OK com.cobalt.radar running running 2 min, heartbeat fresh` · `OK com.cobalt.aset running loaded, pid 55969`. GREEN.
- (h) REVERT-READBACK at 22:45:49 (`<t up>` + 180 s, after (b) settled): `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39, the same as `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `curl … /radar` → `200` · no `census` reads on this card. GREEN.

THE CHAIN:
- P2: the check is committed (`c6ef303f`) with `held unfixed: 0 · ready: YES` at `tip: 9feda305`.
- P3: the tips re-read as `9feda305` and `4465b758`.
- T: one clean merge, giving `<m1>` `13698c03`.
- R: RESTARTS derived as `com.cobalt.aset com.cobalt.radar`.
- G: three suites green on `13698c03`.
- D2.3: `<stack-final>` `f4f0af50` = `<m1>` plus docs.
- 4.3: the code landed by fast-forward `86ee64d4..f4f0af50`.
- (d): both markers moved 0 → 1.
- (g): no migration.
- (a): the residents are up on new pids after the merge.
- (b), (e): radar is cycling with a fresh heartbeat.
- (s): both reads are 1.
- (h): no new failure.
- The voice widget surface is not readable here; the desk confirms it with him (L70).

### STEP-7 close
- `<pre-merge>` `86ee64d4` → `<stack-final>` `f4f0af50` (main tip `f4f0af50`).
- Tags: `pre-voice-clarify-fix-1009` at `86ee64d4`; `deploy-2026-10-09-voice-clarify-fix` at `f4f0af50`, set after the green smoke.
- `<t down>` 22:42:34 · `<t up>` 22:42:49 · 15 s.
- The uv sync line: the production tree needed none. The gate's first `uv run` created its `.venv` (`Installed 253 packages in 1.04s`).
- No proof cost: no migration.
- `migrations applied: none`; no `<RB>` before or after.
- Snapshot `401fc6d1` (ssd).
- `RESTARTS done: com.cobalt.aset com.cobalt.radar`.
- THE ROLLBACK STRING:
  1. CODE: boot out com.cobalt.aset and com.cobalt.radar, then `git -C /Users/cobalt/cobalt revert --no-edit -m 2 f4f0af50`, then bootstrap both.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK:
  1. Every smoke row is quoted with its `date`. (b) and (c) shared (a)'s 22:43:02 `date` (see RECORDS).
  2. Code tip `9feda305` and head `4465b758` were re-read at P3, and `merge-base --is-ancestor` of each against `f4f0af50` exited 0.
  3. REVERT-READBACK (h) is shown above, and every count, sha and `file:line` in this report was read from this run's tool output.
  4. STEP-T ran clean (`Merge made by the 'ort' strategy.`), so no conflict marker exists.
- THE RELEASE: the lock was released by `gate.sh` (log `:2020` `lock released`). `ls -la <GATE>/.env` → No such file, and `/Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.

## CONTINUE
done: deployed and smoke GREEN; nothing further for this session after the STEP-7 commit. The outage ran from 22:42:34 to 22:42:49 EDT, and the residents are up.

## DECISIONS
none

## RECORDS
- Downtime 15 s, under 300 s.
- `cobalt_dev: 0013 (F2 = F0)` (gate log `:2018`).
- No `RETIRE OWED`: STEP-C diff of `configs ops` was empty.
- Carried RED as read: no radar-family RED; radar was `idle (overnight)` with a fresh heartbeat throughout. Three standing REDs outside the aset/sheet/radar probes were present from `<hb0>` to smoke (e) and are unchanged. They are:
  - the `archiver` probe;
  - `com.cobalt.archiver` (`RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests'`);
  - `com.cobalt.replay` (`ReplayError: archiver not done: state 'failed'`).
  
  They belong to the desk, not this deploy.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-voice-clarify-fix-1009` and branch `deploy/voice-clarify-fix-1009`; the set's branch `ops/voice-clarify-fix-1009` and its worktree, if any. Push is his (L55): `main` is ahead of `origin/main`, and the two new tags are local.
- Not a refusal, my own cwd slip at 22:12: one `COBALT_ENV=production uv run cobalt heartbeat show` ran while the cwd was still `<GATE>` (no `.env`). It failed with `DbConfigError: Missing Postgres settings for the APP credential …`. I then ran `cd /Users/cobalt/cobalt`, and `ls -la /Users/cobalt/cobalt/.env` listed the file. Nothing was written.
- Smoke (b) and (c) did not each get their own `date` call; they ran between the 22:43:02 and 22:43:15 `date` calls.
- `git status --porcelain` at D0 also listed `?? .claude/settings.json.bak`. It is not in the accepted list and not in a refused prefix (`src/` `tests/` `ops/` `configs/`), so it was recorded and not refused.
- The equal-tree clause did not hold (`configs/cobalt/rules.yaml` differs between `9feda305` and `13698c03`), so the gate ran whole.
- Card `## RECORDS`, copied:
  - voice-clarify-fix-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-clarify-fix-check-2026-10-09.md` last line: CHECK DONE · job: voice-clarify-fix-1009 · pass: 1 · tip: 9feda305 · house A: Sol FINDINGS: 1 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 1 · suites: offline 4060/0 · with-DB 4947/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 161041
  - voice-clarify-fix-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/voice-clarify-fix-1009` → `4465b758`; code tip `9feda305`
  - written by deploy-card.sh at 2026-10-09 20:40 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one system-reminder asked for a `Claude-Session:` line in commits. It was recorded under `## L74` and not acted on.

DEPLOYED deploy-2026-10-09-voice-clarify-fix f4f0af50 | set: none | migrations: none | gate: offline 4060/0 · with-DB 4947/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 204552
