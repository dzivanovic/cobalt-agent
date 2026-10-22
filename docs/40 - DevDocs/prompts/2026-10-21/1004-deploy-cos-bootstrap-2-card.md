JOB: cos-bootstrap-2
LADDER: S5-P3 · F20
BRANCH: none
WORKTREE: none
BASE: main
TIP: none
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-bootstrap-2.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-cos-bootstrap-2
MIGRATIONS: none
SET: cos
TICKERS: none
RESTARTS: none — nothing merges; STEP-R has no card value (K10 smoke (a) acts on an empty set)
WAITS: cos-env-load DEPLOYED ea7f7727

## LAUNCHD
com.cobalt.cos · add · prompts/2026-10-18/730-f20-card.md:C4a · dry run: none

## GATE RESULTS
GATE RESULT: com.cobalt.cos · D14 · his — row R2232 (2026-10-20 ~20:30 ET): Mattermost listener MOVED to com.cobalt.cos; scheduler/morning briefing RETIRED (unused); Scribe RETIRED (redevelop later); memory layer RETIRED (redevelop on F21); he said "Yes replace the old agent" (words: reports/cto-2026-10-20-words.md R2232)
GATE RESULT: com.cobalt.cos · agent stopped · YES — his row R2232 (retire yes); cobalt.sh stop 2026-10-21 16:00 ET, bootout gui/501/com.cobalt.agent and rm of the installed ~/Library/LaunchAgents/com.cobalt.agent.plist typed by him ~16:1x ET; reads: cobalt.sh status OFFLINE, launchctl print "Could not find service", plist ls "No such file" (desk, 17:10 ET); ops/desk/retired-labels holds com.cobalt.agent (brain 9b07db5a)
GATE RESULT: com.cobalt.cos · X1 · OK (shell, not under a LaunchAgent) — the LaunchAgent login is proven by this run's smoke (s)
GATE RESULT: com.cobalt.cos · X13 · PASS — answer line OK; the settings warning recorded (brain, R2197)
GATE RESULT: com.cobalt.cos · X2 · OK — no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)
GATE RESULT: com.cobalt.cos · X10 · OK — no process, file, contents or tool call (0 allowlisted tool calls; turn ok=True)
GATE RESULT: com.cobalt.cos · X3 · OK — cap: turn stopped at max turns; kill: the session died; timeout: timeout after 10s, the CLI was killed
GATE RESULT: com.cobalt.cos · X14 · OK — ok 20/20 · max num_turns 6 · max seconds 7.4 (caps: max_turns 30, timeout 900s)
GATE RESULT: com.cobalt.cos · X11 · OK — init tools 7, all mcp__cobalt__* allowlisted (planted server started: no)
GATE RESULT: com.cobalt.cos · X12 · OK — neither dummy in the child
GATE RESULT: com.cobalt.cos · X15 · DEFERRED by his word ("Ok so we can try after it deploys", 2026-10-21, brain relay) — his four legs run after the 994 port deploys; a lost k only refuses approvals (fails safe, F20-FINAL :43); brain 9b07db5a R2322
GATE RESULT: com.cobalt.cos · X17 · OK — sonnet ok 20/20 · opus ok 20/20
GATE RESULT: com.cobalt.cos · X18 · OK — median 28.5 s; the max, 641 s, was F5's migration deploy (0029, card 909)
GATE RESULT: com.cobalt.cos · X20 · OK — 1 passed

## NOT IN THIS JOB
- A merge, an outage, a restart of `com.cobalt.aset`, `com.cobalt.radar` or `com.cobalt.agent`.
- Any `launchctl` on `com.cobalt.agent`, any `cobalt.sh stop`: the agent stays retired (`ops/desk/retired-labels`; DESK RECORD R2340).
- Deleting, moving or truncating `logs/cos.err` or `logs/cos.log`: no seat deletes logs.
- The tunables `cos.poll_interval_s` and `hitl.request_ttl_min`: set by the K5 config card, deployed before card 929.
- The R60 restart strings of a loaded cos: later restarts only.
- Any `src/`, `ops/` or `configs/` change: the `.env` load landed with cos-env-load (`src/cobalt/cos/run.py:141`).

## MARKERS
- `ls /Users/cobalt/cobalt/data/cos/scratch` · before `No such file or directory` · after listed
- `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` · before `1` · after `0`

## SMOKE READS
- cos not refused · `grep -c -F "CosRefused" /Users/cobalt/cobalt/logs/cos.err` · `0`
- cos tunables · `grep -c -F "CosConfigError" /Users/cobalt/cobalt/logs/cos.err` · `0`
- cos Postgres settings · `grep -c -F "DbConfigError: Missing Postgres settings" /Users/cobalt/cobalt/logs/cos.err` · `2`
- cos Mattermost poll · `grep -c -F "Traceback" /Users/cobalt/cobalt/logs/cos.err` · `2`
- cos steps · `grep -c -F "CoS step" /Users/cobalt/cobalt/logs/cos.err` · `0`
- cos turn failures · `grep -c -F "CoS turn FAILED" /Users/cobalt/cobalt/logs/cos.err` · `0`

## CHECK ASKS
- X1 Cos bootstrap-only card: 4.6L-BO loads `com.cobalt.cos` alone, no other deploy in between.
- X2 Smoke (s) reads six counts on `logs/cos.err`, which holds card 929's two tracebacks. `Traceback` = 2 and `DbConfigError: Missing Postgres settings` = 2 mean no new line since 929; a count above 2 is a new failure → bootout cos, `FAILED: smoke (s)`. LaunchAgent auth is UNPROVEN until his one DM turn, confirmed by the desk. `CoS turn FAILED` > 0 → bootout cos, `FAILED: smoke (s)`; the agent is not brought back (a rollback is his).
- X3 D14, agent stopped and X15 are his rows.
- X4 Marker 1 reads the scratch dir the start makes (`src/cobalt/cos/run.py:106`), absent since 929 died at the old `run.py:149`; no marker reads the old log files.

## RECORDS
- 929 FAILED smoke (s), cos lacked the .env load under launchd; cos-env-load DEPLOYED ea7f7727; cos-bootstrap-2 re-issues the bootstrap — brain 9b07db5a 2026-10-21
- MIGRATIONS: none; the first start CREATEs cobalt_cos_sessions, cobalt_cos_turns, cobalt_hitl_requests IF NOT EXISTS plus the jobs row (`src/cobalt/cos/run.py:108`, `:112`, `:159`, `:160`): additive, the rollback leaves them.
- THE START ON MAIN: `load_dotenv(ENV_FILE)` at `src/cobalt/cos/run.py:141` (`ENV_FILE` `:40`), before `refuse_if_agent_alive()` `:157`, `store.ensure_schema()` `:159`, `store.register` `:160`, `mark_running` `:165`; `_build` reads `tunable_int(POLL_KEY)` `:102`, then empties and makes `SCRATCH_DIR` (`:105`, `:106`).
- RESTARTS: the bootstrap itself loads `com.cobalt.cos` (4.6L-BO); no resident restarts. cos-env-load's tool line was `RESTARTS: com.cobalt.cos com.cobalt.radar`; cos was not loaded, so its `<restart set>` was `com.cobalt.radar` (L42), done at `ea7f7727` (`reports/deploy-cos-env-load.md` `## RESTARTS`).
- SMOKE READS: `grep -c -F` rows only. No curl row: `deploy-smoke.sh` maps curl to `http://127.0.0.1:5010/` only and the launch line admits `https://cobalt.taild24291.ts.net/*` only (L80).
- ORDER: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --bootstrap-only "<card>" com.cobalt.cos` → `ADMITTED: com.cobalt.cos · bootstrap-only` → 4.6L `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `launchctl print gui/501/com.cobalt.cos` (found, `path = ` that plist) → smoke (s) → `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --owed-clear "<card>" com.cobalt.cos` → `OWED CLEARED: com.cobalt.cos` → marker 2 read as smoke (d). `com.cobalt.agent` is not touched (929 hub DECISIONS 2, kept per R2335).
- FILES AND OBJECTS IT TOUCHES: launchd label `com.cobalt.cos` (loaded); `/Users/cobalt/cobalt/logs/cos.log`, `/Users/cobalt/cobalt/logs/cos.err` (appended, `ops/com.cobalt.cos.plist:33`, `:35`); `/Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` (the cos entry removed); `/Users/cobalt/cobalt/data/cos/scratch/` (made, `src/cobalt/cos/run.py:106`); production DB at cos's first start: the jobs row of `com.cobalt.cos` (`run.py:159`, `:160`), `cobalt_cos_sessions`, `cobalt_cos_turns` (`src/cobalt/cos/migrations/0001_cobalt_cos.sql:14`, `:28`) and `cobalt_hitl_requests` (`src/cobalt/hitl/migrations/0001_cobalt_hitl.sql:20`), each `CREATE … IF NOT EXISTS`.
- ROLLBACK (returns the old state): `launchctl bootout gui/501/com.cobalt.cos`, then `launchctl print gui/501/com.cobalt.cos` → `Could not find service` (STEP-5 (1L); an `add` label stays out, (2L)). With `--owed-clear` run after smoke (s), a red smoke (s) leaves the owed entry in place. No revert: nothing merged. The log files, the scratch dir and the `IF NOT EXISTS` tables stay.
- HUB STEPS WITH NO CARD VALUE (no code tip): P2 and P3 (no `## SHIPS` row), P5 (no gate worktree), P7, STEP-T, STEP-R, STEP-G, D2.0's `deploy-shipped.sh --moved`, D2.1–D2.3, D2.6's `pre-<JOB>` tag at a merge, STEP-4 4.1–4.6, smoke (f)'s `jobs restarts <pre-merge>..<stack-final>`, and the ROLLBACK STRING's revert.
- gate report `reports/cos-gate-run-2026-10-20.md` at `7de50210`: `GATES DONE · ok: 10 · fail: 1 · not run: 3`; X13 ruled PASS by the brain (row R2197 of `reports/cto-2026-10-20.md`): 11 OK.
- SMOKE READS row 6 (`cos turn failures`): LaunchAgent auth stays UNPROVEN (L70) until one DM turn of his after the hub's green, asked by day in one sentence and confirmed by the desk.
- READS at drafting (drafter `draft-cos-bootstrap-2`, 2026-10-21 20:18 ET, `date`): `ls -la` → `logs/cos.err` 3040 bytes 17:23, `logs/cos.log` 0 bytes, `data/cos` and `data/cos/scratch` `No such file or directory`; `grep -c -F` on `logs/cos.err` → `Traceback` 2, `DbConfigError: Missing Postgres settings` 2, `CosRefused` 0, `CosConfigError` 0, `CoS step` 0, `CoS turn FAILED` 0; `grep -n -F "com.cobalt.cos" data/deploy/bootstrap-owed.json` → line 4, gate items D14, agent stopped, X1, X13, X2, X10, X3, X14, X11, X12, X15, X17, X18, X20 (one GATE RESULT line each above).
- written by hand by drafter `draft-cos-bootstrap-2` at 2026-10-21 20:20 ET (`date`); `ops/desk/deploy-card.sh` cannot cut a card with no code branch.
