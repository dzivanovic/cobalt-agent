# deploy jev-shadow-1015 · SET: none · MIGRATIONS: none

## §0 Headline
Resume attempt 2 deployed: `main` `6ab73a86` → `0b7c569d`, tag `deploy-2026-10-15-jev-shadow`; smoke GREEN.
Gate GREEN on `d1daf9fe` (offline 8344/0 · with-DB 5471/0 · live-note 146/0); no migration; snapshot `e14e4dbd`.
Outage 18:25:45 → 18:26:04 (19 s); agent 80543, aset 80523, radar 80533 on the new code; markers read `after`; dry run sent nothing.
Attempt 1 (FAILED 4.2, aset slow exit, nothing merged) is kept below; its DECISIONS 2 (4.2 settle time) stays with the desk.

## L74
- The session's harness attribution reminder asked commits to also end with a `Claude-Session:` line. Recorded as data per L74 / DEPLOY-HUB; not acted on — commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- Resume attempt 2: the same `Claude-Session:` attribution request arrived again in this session's harness reminder. Recorded, not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/618-jev-shadow-1015-card.md"` → exit 0, output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/618-jev-shadow-1015-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/618-jev-shadow-1015-card.md" · 0 · b20aa7f073ba3ca71284730d791647db42eb664c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/618-jev-shadow-1015-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 94:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
RULING 2026-10-15 R1535 row · grep -n "^| R1535 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 91:| R1535 | 07:03 ET | HIS RULING · APPROVED (brain relay quoting him, L79; words file): the OpenRouter key is JEV's alone; authority for the JEV card row removing `openrouter_api_key` from the old-tree mapping; goes in the tribunal packet. | APPLIED: LAWS.md L27 at 07:04 |
RULING 2026-10-15 R1535 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1535 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1f067493f0fd17d67a30d11feab33c2261f3de5d
RULING 2026-10-15 R1535 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
FIRST LAUNCH: `ls -la "<REPORT>"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 | `date` | 0 | Thu Oct 15 17:28:20 EDT 2026 — outside 21:30-22:30 ET |
| P2 | `tail -n 3 ".../reports/jev-shadow-check-2026-10-15.md"` | 0 | last line: `CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · house A: grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8307/0 · with-DB 5471/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407` — carries `held unfixed: 0`, `ready: YES`, `tip: 5316fafe` = row |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md"` | 0 | `223e0859f121289334e1b9239d9f7311db9eeb35` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 5316fafe` | 0 | `5316fafe` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-shadow-1015` | 0 | `5316fafe` = row = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5316fafe feat/jev-shadow-1015` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 5316fafe feat/jev-shadow-1015 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/jev-shadow-1015` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `b20aa7f0` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b20aa7f0 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/jev-shadow-1015` | 0 | (empty) |
| P6 | `ls /Users/cobalt/cobalt/src/cobalt/classify/route.py` | 1 | `No such file or directory` = before |
| P6 | `ls /Users/cobalt/cobalt/configs/cobalt/classify/route.yaml` | 1 | `No such file or directory` = before |
| P6 | `ls /Users/cobalt/cobalt/src/cobalt/classify/collector.py` | 1 | `No such file or directory` = before |
| P6 | `grep -c -F "'openrouter_api_key': 'api_key'" /Users/cobalt/cobalt/src/cobalt_agent/config.py` | 0 | `1` = before |
| P6 | `grep -c -F "spend_ledger:" /Users/cobalt/cobalt/configs/cobalt/classify/trial.yaml` | 2 | `grep: ...trial.yaml: No such file or directory` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 5316fafe -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 40377` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 8646` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C <GATE> merge --no-edit 5316fafe` → `Merge made by the 'ort' strategy.` (42 files changed, 7215 insertions(+), 16 deletions(-))
- `git -C <GATE> rev-parse --short=8 HEAD` → `d1daf9fe` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent b20aa7f0..deploy/jev-shadow-1015` → `d1daf9fe Merge commit '5316fafe' into deploy/jev-shadow-1015` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5316fafe deploy/jev-shadow-1015` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat b20aa7f0 deploy/jev-shadow-1015 -- src/cobalt/db_migrations` → (nothing): no migration path, MIGRATIONS: none holds
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat b20aa7f0 deploy/jev-shadow-1015 -- configs ops` →
```
 configs/cobalt/classify/route.yaml |  85 +++++++++
 configs/cobalt/classify/trial.yaml | 344 +++++++++++++++++++++++++++++++++++++
 configs/cobalt/jobs.yaml           |  17 ++
 3 files changed, 446 insertions(+)
```
- STEP-C: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" b20aa7f0 deploy/jev-shadow-1015` → exit 0, WHOLE: `STEP-C: ADMITTED 0` → `<launchd set>` empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, table WHOLE (uv lines: `Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14` · `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-jev-shadow-1015` · `Installed 254 packages in 823ms`):
```
path	change	rule	restart
configs/cobalt/classify/route.yaml	A	no resident reads (one-shot: com.cobalt.generated)	-
configs/cobalt/classify/trial.yaml	A	no resident reads (one-shot: com.cobalt.generated)	-
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
docs/30 - Design/jev-shadow-design-2026-10-14.md	M	DOCS	-
docs/40 - DevDocs/cobalt/classify/__init__.md	A	DOCS	-
docs/40 - DevDocs/cobalt/classify/cli.md	A	DOCS	-
docs/40 - DevDocs/cobalt/classify/collector.md	A	DOCS	-
docs/40 - DevDocs/cobalt/classify/config.md	A	DOCS	-
docs/40 - DevDocs/cobalt/classify/ledger.md	A	DOCS	-
docs/40 - DevDocs/cobalt/classify/models.md	A	DOCS	-
docs/40 - DevDocs/cobalt/classify/route.md	A	DOCS	-
docs/40 - DevDocs/cobalt/classify/trial.md	A	DOCS	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/reports/jev-shadow-build-2026-10-15.md	A	DOCS	-
docs/40 - DevDocs/reports/jev-shadow-build-2026-10-15.result	A	DOCS	-
docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md	A	DOCS	-
src/cobalt/classify/__init__.py	A	static import reach	com.cobalt.radar
src/cobalt/classify/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/classify/collector.py	A	static import reach	com.cobalt.radar
src/cobalt/classify/config.py	A	static import reach	com.cobalt.radar
src/cobalt/classify/ledger.py	A	static import reach	com.cobalt.radar
src/cobalt/classify/models.py	A	static import reach	com.cobalt.radar
src/cobalt/classify/route.py	A	static import reach	com.cobalt.radar
src/cobalt/classify/trial.py	A	static import reach	com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt_agent/config.py	M	static import reach	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
src/cobalt_agent/llm.py	M	static import reach	com.cobalt.agent
tests/cobalt/test_classify_config.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_discover.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_door.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_fix_r1.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_fix_r2.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_fix_r3.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_keys.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_models.py	A	test/documentation; no resident	-
tests/cobalt/test_classify_trial.py	A	test/documentation; no resident	-
tests/cobalt/test_jev_shadow_1015.py	A	test/documentation; no resident	-
tests/fixtures/classify/openrouter-model-entry.real-shape.json	A	test/documentation; no resident	-
tests/fixtures/classify/openrouter-probe-response.real-shape.json	A	test/documentation; no resident	-
tests/fixtures/classify/openrouter-probe-s1.real-shape.json	A	test/documentation; no resident	-
tests/fixtures/classify/openrouter-systemone-response.openapi-example.json	A	test/documentation; no resident	-
tests/fixtures/classify/systemone-openapi-example.json	A	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.agent com.cobalt.aset com.cobalt.radar` (= the check's). `<launchd set>` = (empty).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 5316fafe d1daf9fe -- . ":(exclude)docs"` → prints 7 files (`ops/desk/desk-done.sh`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/stop-guard.py`, `tests/ops/test_card_template_1014.py`, `tests/ops/test_close_automation_1015.py`, `tests/ops/test_desk_done.py`; 1023 insertions(+), 15 deletions(-)) — `main` moved since the check: the clause does not hold; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 18.89s` — 0 failed (with-DB tests skip: `Postgres env settings not available` / `requires_db`).
- Deselects: the build report names none added to its pass 1 (`jev-shadow-build-2026-10-15.md:179` "the 22 `--deselect`s of the list, none added"); the check's gate ran with no `--deselect` (`jev-shadow-check-2026-10-15.md:246`). TICKERS none, MIGRATIONS none → no `--tickers`, no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-jev-shadow-1015 all --deploy --deploy-gate` → exit 0, verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8344/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5471/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-jev-shadow-1015-all-20261015-173022.log
```
- (a) OFFLINE: `offline 8344/0` — log `:888 4568 passed, 806 skipped, 1 xfailed` + `:958 3776 passed, 1 xfailed` (tests/ops, deploy gate) = 8344. W line `tests/ops: run (deploy gate)`.
- (b) lock taken (`:964 lock taken: deploy-jev-shadow-1015`, waited 0 min); `:975 F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; proof-only nothing CHANGED; LEVEL 0013.
- (c) PASS 1 whole: `:1192 5266 passed, 7 skipped, 99 deselected, 3 xfailed` → `<d1>` 5266. The 7 SKIPPED lines, each inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`def` at `tests/cobalt/test_s3_c4_experiments.py:96`).
- (c2) FORWARD: `:1194 dev forward: APPLIED 18:10:17` (no migration above 0013 on this set; no `CHANGED`).
- (c3) PASS 2: `:2046 205 passed, 1 deselected` → `<d2>` 205; with-DB 5266 + 205 = 5471/0.
- (f) `:2114 F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → `cobalt_dev: 0013 — F2 = F0`.
- RELEASE: `:2167 $ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-jev-shadow-1015` → `:2168 lock released`; `.env: removed`. `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) LIVE-NOTE: `:2237 146 passed, 1 skipped` → `live-note 146/0`; its one skip `:2236` is the `test_replay_line.py:266` `COBALT_TEST_LIVE_DRC` skip (inside the set); no skip names `COBALT_LIVE_VAULT_ROOT`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `date` → Thu Oct 15 18:15:52 EDT 2026.

GATE GREEN on d1daf9fe

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 173]`. `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (not under `src/`, `tests/`, `ops/`, `configs/`; no staged line).
- `git -C /Users/cobalt/cobalt diff --stat b20aa7f0 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- ALLOWLIST PROBE: `tag scratch-allow-probe-jev-shadow-1015` → ok; `tag -d` → `Deleted tag 'scratch-allow-probe-jev-shadow-1015' (was b20aa7f0)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 73bb51e0] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `b20aa7f0 docs(desk): card 618 RULINGS in the launcher's form` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-15-jev-shadow` → exit 1; `refs/tags/pre-jev-shadow-1015` → exit 1.

### STEP-D1 (baseline)
- `date` → Thu Oct 15 18:16:26 EDT 2026. `<hb0>` = `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:16:27 EDT)`; one `AMB com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) [launchd probe]; runs outside launchd by declared interim` (not RED); `OK radar scanning (aftermarket), members 50`; `OK com.cobalt.radar running running 2645 min, heartbeat fresh`. No RED — no carried radar RED.
- `<val0>`: `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` / `registry <-> ops/: 15 label(s), exact match.`
- `backup status` → `newest snapshot: 2.2 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` 40377; `…/com.cobalt.radar` → `state = running`, `<radar pid>` 8646; `cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).`; `ps -p 14763` → `14763 ??  0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last cycle `2026-10-15 18:14:29.708 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792102379083`, then price-floor lines at 18:16:21; no traceback.
- LOG BASELINES: `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again: route.py / route.yaml / collector.py `No such file or directory`; openrouter grep `1`; trial.yaml grep `No such file or directory` — each its `before`.
- LAUNCHD SET: empty — nothing. MIGRATION: none — no `<RB>`, no proof-only.

### STEP-D2
- D2.0: `add` + `commit -m "docs(report): deploy jev-shadow-1015 — gate green on d1daf9fe"` → `[main 8685057a] … 1 file changed, 186 insertions(+)`; `show --stat HEAD` → that one file. `<pre-merge>` = `8685057a`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2: `<stack-final>` = `ccb86121`; `rev-parse --short=8 ccb86121^2` → `8685057a` = `<pre-merge>`; `merge-base --is-ancestor d1daf9fe ccb86121` → exit 0.
- D2.3: `diff --stat d1daf9fe ccb86121 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- D2.4: `backup status` → `newest snapshot: 2.2 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 8356.3 MB` · `ssd: snapshot a844c1b9 — 0 new / 2 changed, 114.0 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`. Snapshot id `a844c1b9`.
- D2.5: `date` 18:18:12 → heartbeat 18:18:12 (105 s after D1's 18:16:27, under 110 s); again `date` 18:18:16 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:18:18 EDT)` (111 s); no RED.
- D2.6: `date` → Thu Oct 15 18:18:21 EDT 2026; `git -C /Users/cobalt/cobalt tag pre-jev-shadow-1015` → `rev-parse --short=8 pre-jev-shadow-1015` → `8685057a`.

### STEP-4 — the outage (ended at 4.2)
- 4.1 `date` → `<t down>` = Thu Oct 15 18:18:33 EDT 2026.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → (no output, exit 0). `launchctl print gui/501/com.cobalt.aset` → still loaded: `state = SIGTERMed`, `pid = 40377`. One `date` → 18:18:37; print again → still `state = SIGTERMed`, `pid = 40377`. Still loaded after the one retry → STEP-5 (nothing merged), per 4.2. radar not yet booted out; agent not yet stopped; orphan-clean not reached; 4.3 (merge) NOT run.
- Cause as read (not proven, L70): `tail -n 30 aset.err` after the restore shows the old process's `INFO: Shutting down` / `INFO: Waiting for connections to close. (CTRL+C to force quit)` — uvicorn was waiting on open connections past the second print (~4 s after bootout; plist `exit timeout = 5`). By STEP-5 (1) at 18:18:45 (12 s after bootout) the service was gone.

### STEP-5 — rollback (nothing merged)
- (0) `date` → Thu Oct 15 18:18:45 EDT 2026.
- (1) `launchctl print gui/501/com.cobalt.aset` → exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` (gone, no second bootout needed). radar still loaded → `launchctl bootout gui/501/com.cobalt.radar` → exit 0; `print` → exit 113 `Could not find service "com.cobalt.radar"`. Agent: `cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` → `cobalt.sh stop` → `Sending graceful shutdown signal to Cobalt (PID: 14763)...` / `Cobalt stopped safely.`; `ps -p 14763` → header only. Counts: `<rp5>` 18 · `<rpr5>` 60 · `<re5>` 43 · `<lc5>` 39 (= D1 baselines).
- (1L) `<launchd set>` empty — nothing.
- (2) 4.3 did not merge: `git -C /Users/cobalt/cobalt log --oneline -1` → `8685057a docs(report): deploy jev-shadow-1015 — gate green on d1daf9fe` = `<pre-merge>`, not `<stack-final>`. NO revert. `main` carries no code of the set.
- (2L) none. (2a)/(2b) MIGRATIONS none — `migrations applied: none`.
- (3) `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` (dry run) → `orphan-clean: aset · none found`. `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → exit 0; `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → exit 0; `launchctl kickstart gui/501/com.cobalt.agent` → exit 0. `launchctl print` aset → `state = running`, `pid = 77670` (≠ 40377); radar → `state = running`, `pid = 77683` (≠ 8646). `date` → `<t up>` = Thu Oct 15 18:19:05 EDT 2026. Downtime: aset 18:18:33 → 18:19:05 = 32 s; radar 18:18:4x → 18:19:05 (~20 s); agent stopped ~18:18:5x → 18:19:05.

## Smoke
STEP-5 (4) — re-run on the OLD tree (nothing merged), `<t up>` 18:19:05:
- (a) aset `state = running` pid 77670 (≠ 40377); radar `state = running` pid 77683 (≠ 8646); `cobalt.sh status` → `Cobalt is ONLINE (PID: 77694).` (≠ 14763). GREEN.
- (b) `grep -c "Started server process" aset.err` → 280 (`<a0>` 279; +1, within +2). `tail -n 30 aset.err` → `INFO:     Started server process [77670]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)`. Traceback aset 217 = `<ta0>`; radar 0 = `<tr0>`; TaxonomyConfigError 0 = `<tc0>`. Radar tail at `date` 18:20:35 (`<t up>` + 90 s): `2026-10-15 18:20:32.837 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792102742817`, the lines above it `cards.expire: falling back to the session close` INFO only; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN on the first tail.
- (c) `curl … /` → `200`; `/radar` → `200`; `/radar\?frame=phone` → `200`. GREEN.
- (e) heartbeat #1 `date` 18:19:26 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:19:26 EDT)`, `com.cobalt.radar running running 0 min, heartbeat fresh`.
- (f) `validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`. `jobs restarts 8685057a..ccb86121` (from `/Users/cobalt/cobalt`, old code) → exit 1 `FAILED: RestartError: one or more changed paths were unclassified` — `configs/cobalt/classify/route.yaml A UNCLASSIFIED CONFIG …` / `ESCALATE: unclassified path configs/cobalt/classify/route.yaml`, the same for `trial.yaml`; `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. The old tree's classifier lacks the set's `jobs.yaml` rule (see `## DECISIONS` 3). STEP-5 is not entered twice.
- (g) no migration — `migrations applied: none`.
- (e) heartbeat #2 `date` 18:21:15 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:21:17 EDT)` (111 s after #1), `com.cobalt.radar running running 2 min, heartbeat fresh`; no RED (only `AMB com.cobalt.herdr`, as in `<hb0>`). GREEN.
- REVERT-READBACK (after the settled tail): `radar panel FAILED` 18 = `<rp5>` · `radar pool refresh FAILED` 60 = `<rpr5>` · `radar S5 evaluate FAILED` 43 = `<re5>` · `lifecycle card read failed` 39 = `<lc5>`. No count grew.

## CONTINUE
next: STEP-D0 (gate green at 18:15:52) — D0, D1, D2 done
OUTAGE STARTING 18:18:21 — residents of com.cobalt.agent com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED 18:19:05 — STEP-5 (3) restored all three on the old code; nothing merged. next: the desk's (recut, or a new session at `CONTINUE: STEP-D0`).
RESUME attempt 2 (18:22:24): resume checks TRUE; STEP-0, D0, D1, D2 done.
OUTAGE STARTING 18:25:32 — residents of com.cobalt.agent com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
OUTAGE ENDED 18:26:04 — merged 6ab73a86..0b7c569d; all three residents up on the new code.
SMOKE GREEN 18:29:04; tag set; report closed (STEP-7).

## DECISIONS
1. FOR THE DESK — the run FAILED at 4.2 on aset's slow exit (`state = SIGTERMed` at the one retry), not on the set's code: the gate is green on `d1daf9fe` and nothing merged. This hub has no RECUT path for a `rollback: used` ending with nothing merged; the RECUT clause covers `rollback: not used` only. Safe default taken: residents restored on the OLD code, `main` at `8685057a` (docs only), rollback tag `pre-jev-shadow-1015` left at `8685057a`, gate worktree and branch left as they are. The desk decides between a recut and a relaunch (`CONTINUE: STEP-D0`, whose (a) the `FAILED:` last line satisfies). Not his: no scope, money or schema touched.
2. FOR THE DESK — 4.2's single `date` between two prints gave aset ~4 s to exit against the plist's `exit timeout = 5` and a uvicorn that waits on open connections (`Waiting for connections to close`); at 12 s it was gone. Whether 4.2 should allow a longer settle for aset is a hub change, the desk's (L67: the hub is read by another house at each change). Safe default: none — the hub was followed as written.
3. FOR THE DESK — STEP-5 (4)'s `jobs restarts 8685057a..ccb86121`, run from `/Users/cobalt/cobalt` (old code), exits 1 with `UNCLASSIFIED CONFIG` on `configs/cobalt/classify/route.yaml` and `trial.yaml`: the classification rule arrives with the set's own `configs/cobalt/jobs.yaml` (+17), which `main` does not carry because nothing merged. On the gate tree (STEP-R) the same paths read `no resident reads (one-shot: com.cobalt.generated)`. Read as a property of the un-merged tree, not a production fault (L70: not proven either way beyond these two reads). Safe default: recorded, not a DECISION 0.

## RECORDS
- Downtime (under 300 s, recorded for the file): aset down 18:18:33 → up 18:19:05 (32 s); radar booted out at STEP-5 (1) after 18:18:45 → up 18:19:05; agent stopped after 18:18:45 → ONLINE by 18:19:05 (pid 77694). The radar and agent stops were STEP-5 (1)'s, on the old code, with nothing merged.
- No code of the set reached production: `main` at `8685057a` (the D2.0 report commit, docs only); `ccb86121` (`<stack-final>`) is on `deploy/jev-shadow-1015` only. MARKERS still read `before`.
- Tag `pre-jev-shadow-1015` at `8685057a` left in place; `deploy-2026-10-15-jev-shadow` NOT set.
- Snapshot `a844c1b9` (ssd) taken at D2.4.
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both; lock released (`lock released`, log `:2168`).
- No `RETIRE OWED`, no `BOOTSTRAP OWED` (STEP-C `ADMITTED 0`).
- Carried RED: none — `<hb0>` had no RED; `herdr` AMBER (declared interim) throughout.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-jev-shadow-1015` and branch `deploy/jev-shadow-1015` (at `ccb86121`, carrying `d1daf9fe` and the main-into-gate merge) — the desk's, with its recut or relaunch; set branch `feat/jev-shadow-1015` and its worktree stay until the set deploys.
- L74: the harness's `Claude-Session:` attribution line recorded under `## L74`, not acted on.
- From the card's `## RECORDS`: jev-shadow-1015: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md` last line: CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · house A: grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8307/0 · with-DB 5471/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407
- From the card's `## RECORDS`: jev-shadow-1015: head `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-shadow-1015` → `5316fafe`; code tip `5316fafe`
- From the card's `## RECORDS`: written by deploy-card.sh at 2026-10-15 17:27 ET (`date`); trial merge of the heads onto main in order: clean
- PRE-STOP SELF-CHECK: (1) every smoke row quoted with its `date` (`## Smoke`). (2) P3 re-read `5316fafe` (tip = head); `merge-base --is-ancestor d1daf9fe ccb86121` → exit 0 and `5316fafe` ⊂ `deploy/jev-shadow-1015` (STEP-T) — but `<stack-final>` never landed on `main`. (3) REVERT-READBACK shown under `## Smoke` (STEP-5 (4)): 18/60/43/39 = `<rp5>`/`<rpr5>`/`<re5>`/`<lc5>`; every count and sha re-read from tool output this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); no conflict marker.
- ROLLBACK STRING (attempt 1): not written — nothing merged (THE ROLLBACK STRING applies to an ending that merged).
- RELEASE: the lock was released by `gate.sh` at STEP-G; `<GATE>/.env` and the lock dir absent (STEP-G reads).
- Attempt 2: DECISIONS 1 resolved by the relaunch (`CONTINUE: STEP-D0`); DECISIONS 3 resolved on the merged tree (smoke (f) `jobs restarts 6ab73a86..0b7c569d` exit 0, the two classify configs classified); DECISIONS 2 stands for the desk — in attempt 2 aset was gone at the FIRST print after bootout (exit 113).
- Attempt 2 downtime: 18:25:45 → 18:26:04 = 19 s (under 300 s).
- Attempt 2 tags: `pre-jev-shadow-1015` deleted at `8685057a` (attempt 1's) and set again at `6ab73a86`.
- Attempt 2 smoke (s): `uv run cobalt classify route … --dry-run` (the card's smoke read) is not a string of the hub's launch line; it ran without a refusal, exit 0. Recorded for the desk's list review; no action taken.
- Cleanup owed (L46), attempt 2: gate worktree `/Users/cobalt/cobalt-wt/deploy-jev-shadow-1015` and branch `deploy/jev-shadow-1015` (at `0b7c569d`, now on `main`); set branch `feat/jev-shadow-1015` and its worktree — the set has deployed.
- Snapshot `e14e4dbd` (ssd) taken at attempt 2's D2.4.

# RELAUNCH
Launch message: `CONTINUE: STEP-D0` (THE ONE RESUME, attempt 2). `date` → Thu Oct 15 18:22:24 EDT 2026. The report's last non-blank line before this launch, quoted:
> `FAILED: 4.2 — com.cobalt.aset still loaded (state = SIGTERMed) after bootout and one retry · rollback: used — migrations applied: none — aset: UP — radar: UP — launchd: none · decisions: 3 · for Dejan: 0 · tokens: 198005`

Resume checks, each its own call, (e) first:
- (e) `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 77670`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`; `…/com.cobalt.radar` → `state = running`, `pid = 77683`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 77694).` TRUE — no restore needed.
- GATE `.env`: `ls -la /Users/cobalt/cobalt-wt/deploy-jev-shadow-1015/.env` → `No such file or directory` — no G (f), no release by hand.
- (a) the old last line begins `FAILED:` (quoted above). TRUE.
- (b) `## L68 GATE` carries `GATE GREEN on d1daf9fe`; `## RESTARTS` carries `<restart set>` = `com.cobalt.agent com.cobalt.aset com.cobalt.radar`. TRUE.
- (c) `git -C <GATE> status --short --branch` → `## deploy/jev-shadow-1015` alone; `rev-parse --short=8 HEAD` → `ccb86121` (the earlier attempt's main-into-gate merge, above `<m1>`); `merge-base --is-ancestor d1daf9fe ccb86121` → exit 0; `diff --stat d1daf9fe deploy/jev-shadow-1015 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing). TRUE.
- (d) `merge-base --is-ancestor d1daf9fe main` → exit 1 (nothing merged). TRUE.

## RESUME (attempt 2)
### STEP-0 (fresh rows)
| rule | command | exit | result |
|---|---|---|---|
| P0 | `sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "<card>"` | 0 | WHOLE as in `## AUTHORIZATION` with these row-number changes: `R1532 row … 98:| R1532 |…` and `R1535 row … 95:| R1535 |…` (same text, same commits `1ddcdc64…`, `1f067493…`); card commit `b20aa7f0…`, CARD UNCHANGED nothing; last line `AUTHORIZED` |
| P1 | `date` | 0 | Thu Oct 15 18:22:48 EDT 2026 — outside 21:30-22:30 ET |
| P2 | `tail -n 3 ".../jev-shadow-check-2026-10-15.md"` | 0 | last line unchanged (`… tip: 5316fafe … held unfixed: 0 … ready: YES …`) |
| P2 | `log -1 --format=%H -- "<check report>"` | 0 | `223e0859f121289334e1b9239d9f7311db9eeb35` |
| P2 | `diff --stat -- "<check report>"` | 0 | (nothing) |
| P3 | `rev-parse --short=8 5316fafe` · `… feat/jev-shadow-1015` | 0 · 0 | `5316fafe` · `5316fafe` = row = TIP |
| P3 | `merge-base --is-ancestor 5316fafe feat/jev-shadow-1015` · `diff --stat 5316fafe feat/jev-shadow-1015 -- . ':(exclude)docs'` | 0 · 0 | — · (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `status --short --branch` · `rev-parse --short=8 HEAD` (GATE) | 0 · 0 | `## deploy/jev-shadow-1015` · `ccb86121` (as (c) found); `<m0>` = `b20aa7f0` (the report's); `merge-base --is-ancestor b20aa7f0 main` → exit 0; EMPTY check not run (resume) |
| P6 | the five `## MARKERS` | 1·1·1·0·2 | `No such file or directory` ×3 · `1` · `grep: …trial.yaml: No such file or directory` — each `before` |
| P7 | `diff --stat main 5316fafe -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 | `launchctl print` aset / radar (at (e)) · `ls …/ops/com.cobalt.aset.plist` · `cobalt.sh status` | 0·0·0·0 | aset `running` pid 77670, path = the ops plist · radar `running` pid 77683, path = the LaunchAgents plist · listed · `Cobalt is ONLINE (PID: 77694).` |

### STEP-D0
- `status --short --branch` → `## main...origin/main [ahead 176]`. `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, `?? .claude/settings.json.bak`; no staged line; no `src/`, `tests/`, `ops/`, other `configs/` path.
- `diff --stat b20aa7f0 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- ALLOWLIST PROBE: `tag scratch-allow-probe-jev-shadow-1015` → ok; `tag -d` → `Deleted tag 'scratch-allow-probe-jev-shadow-1015' (was 255dab0e)`; `commit --allow-empty …` → `[main 910e96c8] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `255dab0e docs(desk): R1621-R1623 JEV deploy FAILED 4.2 (nothing merged), 546 port check DONE ready YES` (HEAD back).
- TAG NAMES: `refs/tags/deploy-2026-10-15-jev-shadow` → exit 1. `refs/tags/pre-jev-shadow-1015` → exit 0 `8685057aba6204bdee7261a197e35452b80fd056` (attempt 1's) → `tag -d pre-jev-shadow-1015` → `Deleted tag 'pre-jev-shadow-1015' (was 8685057a)`.

### STEP-D1 (fresh baseline)
- `date` → Thu Oct 15 18:23:17 EDT 2026. `<hb0>` = `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:23:18 EDT)`; `AMB com.cobalt.herdr unmanaged AMBER …declared interim` (not RED); `OK radar scanning (aftermarket), members 50`; `OK com.cobalt.radar running running 4 min, heartbeat fresh`. No RED.
- `<val0>`: `validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` / `registry <-> ops/: 15 label(s), exact match.`
- `backup status` → `newest snapshot: 0.1 h old` (ssd local ARMED).
- aset `state = running` `<aset pid>` 77670; radar `state = running` `<radar pid>` 77683; `cobalt.sh status` → `Cobalt is ONLINE (PID: 77694).`; `ps -p 77694` → `77694 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last cycle `2026-10-15 18:20:32.837 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792102742817`, then price-floor INFO lines at 18:22:25; no traceback.
- LOG BASELINES: `<a0>` 280 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again → each `before` (route.py / route.yaml / collector.py `No such file or directory`; openrouter `1`; trial.yaml `No such file or directory`).
- LAUNCHD SET: empty. MIGRATION: none — no `<RB>`, no proof-only.

### STEP-D2
- D2.0: `add` + `commit -m "docs(report): deploy jev-shadow-1015 — gate green on d1daf9fe"` → `[main 6ab73a86] … 1 file changed, 48 insertions(+), 1 deletion(-)`; `show --stat HEAD` → that one file. `<pre-merge>` = `6ab73a86`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (4 files, all `docs/40 - DevDocs/reports/`).
- D2.2: `<stack-final>` = `0b7c569d`; `rev-parse --short=8 0b7c569d^2` → `6ab73a86` = `<pre-merge>`; `0b7c569d^1` → `ccb86121` (attempt 1's main-into-gate merge, above `<m1>`); `merge-base --is-ancestor d1daf9fe 0b7c569d` → exit 0.
- D2.3: `diff --stat d1daf9fe 0b7c569d -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- D2.4: `backup status` → `newest snapshot: 0.1 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 8375.8 MB` · `ssd: snapshot e14e4dbd — 0 new / 1 changed, 70.0 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`. Snapshot id `e14e4dbd`.
- D2.5: `date` 18:25:27 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:25:28 EDT)` (130 s after D1's 18:23:18); no RED.
- D2.6: `date` → Thu Oct 15 18:25:32 EDT 2026; `tag pre-jev-shadow-1015` → `rev-parse --short=8 pre-jev-shadow-1015` → `6ab73a86`.

### STEP-4 — the outage (attempt 2)
- 4.1 `date` → `<t down>` = Thu Oct 15 18:25:45 EDT 2026.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → exit 0; `print` → exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` (first print). `launchctl bootout gui/501/com.cobalt.radar` → exit 0; `print` → exit 113 `Could not find service "com.cobalt.radar"`. ORPHAN-CLEAN (1) `sh …/orphan-clean.sh aset` → `orphan-clean: aset · none found` (no kill). `cobalt.sh stop` → `Sending graceful shutdown signal to Cobalt (PID: 77694)...` / `Cobalt stopped safely.`; `ps -p 77694` → header only.
- 4.3 `rev-parse --short=8 HEAD` → `6ab73a86` = `<pre-merge>`. `merge --ff-only deploy/jev-shadow-1015` → `Updating 6ab73a86..0b7c569d` / `Fast-forward` (42 files changed, 7215 insertions(+), 16 deletions(-)).
- 4.4 MIGRATIONS none → `migrations applied: none`.
- 4.5 `validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` / `registry <-> ops/: 15 label(s), exact match.` = `<jobs0>`. No uv sync lines.
- 4.6 `bootstrap … com.cobalt.aset.plist` → exit 0; `bootstrap … com.cobalt.radar.plist` → exit 0; `kickstart gui/501/com.cobalt.agent` → exit 0. `print` aset → `state = running`, `pid = 80523` (≠ 77670); radar → `state = running`, `pid = 80533` (≠ 77683); `cobalt.sh status` → `Cobalt is ONLINE (PID: 80543).` `date` → `<t up>` = Thu Oct 15 18:26:04 EDT 2026. Downtime 19 s.
- 4.6L `<launchd set>` empty — nothing.

### STEP-4.7 — SMOKE (attempt 2), `<t up>` 18:26:04
- FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39.
- (a) `date` 18:26:21 — aset `state = running` pid 80523 (≠ 77670); radar `state = running` pid 80533 (≠ 77683); `cobalt.sh status` → `Cobalt is ONLINE (PID: 80543).` (≠ 77694). GREEN.
- (b) `grep -c "Started server process" aset.err` → 281 (`<a0>` 280; +1). `tail -n 30 aset.err` → `INFO:     Started server process [80523]` … `INFO:     Application startup complete.` / `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` (the old 77670 `Finished server process` above it). Traceback aset 217 = `<ta0>`; radar 0 = `<tr0>`; TaxonomyConfigError 0 = `<tc0>`.
- (c) `curl … /` → `200`; `/radar` → `200`; `/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `ls …/classify/route.py` → `/Users/cobalt/cobalt/src/cobalt/classify/route.py`; `ls …/classify/route.yaml` → `/Users/cobalt/cobalt/configs/cobalt/classify/route.yaml`; `ls …/classify/collector.py` → `/Users/cobalt/cobalt/src/cobalt/classify/collector.py`; openrouter grep → `0`; `spend_ledger:` grep → `1`. Each its `after`. GREEN.
- (e) heartbeat #1 `date` 18:26:33 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:26:34 EDT)`; `com.cobalt.radar running running 1 min, heartbeat fresh`; only `AMB com.cobalt.herdr` (as `<hb0>`).
- (f) `validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`. `jobs restarts 6ab73a86..0b7c569d` → exit 0, no `UNCLASSIFIED`; `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar` = STEP-R's `<restart set>`; `configs/cobalt/classify/route.yaml` / `trial.yaml` now `no resident reads (one-shot: com.cobalt.generated)` (attempt 1's DECISIONS 3 read resolved on the merged tree). GREEN.
- (g) no migration.
- (s) SMOKE READS: `ls /Users/cobalt/.cobalt/classify` → exit 1 `No such file or directory` (green as the card calls it; read again after the dry run: still `No such file or directory`). `tests/cobalt/test_jev_shadow_1015.py` — quoted from the gate (no test runs in production): it ran in pass 1 offline and with-DB (log `:123`, `:1179` `tests/cobalt/test_jev_shadow_1015.py: 15 warnings`) inside `offline 8344/0` and `with-DB 5471/0`, 0 failed; its `test_j1_dry_run_sends_nothing` (`tests/cobalt/test_jev_shadow_1015.py:447`) asserts the dry run's two lines. `uv run cobalt classify route --card "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" --dry-run` → exit 0: `ROUTE DRY card=docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md launch=1bd425f59159b95f29d90a14763098699dbf2301 bytes=35773 tokens_est=8944 projected_usd=0.00037565 guard=ok` / `ROUTE DRY TOTAL cards=1 calls=1 projected_usd=0.00037565 (nothing sent)` — one `ROUTE DRY` card line, `cards=1 calls=1`, nothing sent. GREEN.
- (b) radar tail #1 at `date` 18:27:35 (`<t up>` + 91 s): `2026-10-15 18:27:31.896 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792103162506`, above it `cards.expire: falling back to the session close` INFO only; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN. Tail again at 18:29:04: the same cycle line last, nothing new after it.
- (e) heartbeat #2 `date` 18:28:25 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 18:28:26 EDT)` (112 s after #1); `com.cobalt.radar running running 2 min, heartbeat fresh`; only `AMB com.cobalt.herdr` (as `<hb0>`). GREEN.
- (h) REVERT-READBACK `date` 18:29:04 (`<t up>` + 180 s): `radar panel FAILED` 18 = `<rp_up>` · `radar pool refresh FAILED` 60 = `<rpr_up>` · `radar S5 evaluate FAILED` 43 = `<re_up>` · `lifecycle card read failed` 39 = `<lc_up>` — no count grew; `curl … /radar` → `200`; no `census` read on the card. GREEN.
- THE CHAIN: every check committed (P2: `223e0859`) → the tips re-read (P3: `5316fafe` = head) → the merged tree (T: `d1daf9fe`) → RESTARTS derived (R: agent, aset, radar) → three suites green on `d1daf9fe` (G: offline 8344/0 · with-DB 5471/0 · live-note 146/0) → `<stack-final>` `0b7c569d` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `6ab73a86..0b7c569d` fast-forward) → markers `after` (d) → no migration (g) → residents up on new pids after the merge (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

### Deploy table (attempt 2)
| item | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `6ab73a86` → `0b7c569d` (`main` now `0b7c569d`) |
| tags | `pre-jev-shadow-1015` at `6ab73a86` · `deploy-2026-10-15-jev-shadow` at `0b7c569d` |
| `<t down>` / `<t up>` / seconds | 18:25:45 / 18:26:04 / 19 |
| uv sync line | none at 4.5 |
| proof cost | none (no migration) |
| migrations applied | none |
| `<RB>` before / after | none / none |
| snapshot id | `e14e4dbd` (ssd) |
| RESTARTS done | `com.cobalt.agent com.cobalt.aset com.cobalt.radar` |
| LAUNCHD done | none · BOOTSTRAP OWED: none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 0b7c569d` — residents agent, aset, radar down first, up after. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

PRE-STOP SELF-CHECK (attempt 2): (1) every smoke row above carries its verbatim evidence and its `date`. (2) P3 re-read `5316fafe` = head; `merge-base --is-ancestor 5316fafe 0b7c569d` → exit 0; `merge-base --is-ancestor d1daf9fe 0b7c569d` → exit 0. (3) REVERT-READBACK (h) shown: 18/60/43/39 = `<rp_up>`/`<rpr_up>`/`<re_up>`/`<lc_up>`; every count and sha re-read from tool output this run. (4) STEP-T ran clean in attempt 1 (`Merge made by the 'ort' strategy.`); D2.1 clean; no conflict marker.
RELEASE: `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file (the lock was released by `gate.sh` in attempt 1; this run never took it).

DEPLOYED deploy-2026-10-15-jev-shadow 0b7c569d | set: none | migrations: none | gate: offline 8344/0 · with-DB 5471/0 · live-note 146/0 | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 3 · for Dejan: 0 · tokens: 201162
