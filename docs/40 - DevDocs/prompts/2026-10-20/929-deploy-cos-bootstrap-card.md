JOB: cos-bootstrap
LADDER: S5-P3 · F20
BRANCH: none
WORKTREE: none
BASE: main
TIP: none
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-bootstrap.md
RULINGS: 2026-10-11 R1112, 2026-10-18 R1854, 2026-10-20 R2232
TAG: deploy-2026-10-21-cos-bootstrap
MIGRATIONS: none
SET: cos
TICKERS: none
WAITS: cos-cutover-tooling DEPLOYED, cos-tunables DEPLOYED, agent retired, hitl.page_base_url set

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
- Any `launchctl` on `com.cobalt.agent`, any `cobalt.sh stop`: the agent's retirement is a separate desk job after this card's green stop line, on bootout strings he approves (RETIRE OWED, `DEPLOY-HUB.md:89`).
- The tunables `cos.poll_interval_s` and `hitl.request_ttl_min`: set by the K5 config card, deployed before this card.
- The R60 restart strings of a loaded cos: later restarts only.
- Any unfilled GATE RESULT placeholder: his rows; no seat fills them.

## MARKERS
- `ls /Users/cobalt/cobalt/logs/cos.err` · before `No such file or directory` · after `listed`
- `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` · before `1` · after `0`

## SMOKE READS
- cos not refused · `grep -c -F "CosRefused" /Users/cobalt/cobalt/logs/cos.err` · `0`
- cos tunables · `grep -c -F "CosConfigError" /Users/cobalt/cobalt/logs/cos.err` · `0`
- cos Mattermost poll · `grep -c -F "Traceback" /Users/cobalt/cobalt/logs/cos.err` · `0`
- cos steps · `grep -c -F "CoS step" /Users/cobalt/cobalt/logs/cos.err` · `0`
- cos turn failures · `grep -c -F "CoS turn FAILED" /Users/cobalt/cobalt/logs/cos.err` · `0`

## CHECK ASKS
- X1 Cos bootstrap-only card, brain 2026-10-20: 4.6L-BO loads `com.cobalt.cos` alone, after the market (16:30+ ET), no other deploy in between.
- X2 Smoke (s) reads the five absence counts; `Traceback` = 0 proves the poll; LaunchAgent auth is UNPROVEN until his one DM turn, confirmed by the desk. `CoS turn FAILED` > 0 → bootout cos, `FAILED: smoke (s)`, agent not brought back (a rollback is his).
- X3 Agent retirement is a separate desk job on his strings, after green.
- X4 D14, agent stopped and X15 are his rows.
- X5 The tunables card (K5: `cos.poll_interval_s`, `hitl.request_ttl_min`; the brain's defaults to him 10 and 30) deploys first: cos raises on null (`src/cobalt/cos/session.py:76-85`, `src/cobalt/hitl/actions.py:62-71`).
- X6 RECORDS: cos bootstrap 929 — no listener overlap (F-14 kept, run.py:44-57); agent retired first after F5 checkpoints cleared, X2 green and his D14; cos-cutover-tooling (K5, HIGH) T1 RESIDENTS/P8/D1/final read accept a retired agent, T2 desk-launch.sh deploy admits a bootstrap-only card; tunables card sets jobs.yaml:214 enabled: true; smoke (s) auth UNPROVEN until his one DM turn; MIGRATIONS none (additive CREATE IF NOT EXISTS) — brain 9b07db5a 2026-10-20

## RECORDS
- MIGRATIONS: none; the first start CREATEs cobalt_cos_sessions, cobalt_cos_turns, cobalt_hitl_requests IF NOT EXISTS plus the jobs row (run.py:105, :109, :150, :155): additive, the rollback leaves them.
- PREREQUISITE: the K5 config card sets `cos.poll_interval_s` (`configs/cobalt/taxonomy/tunables.yaml:1008-1009`, `value: null`) and `hitl.request_ttl_min` (`:1026-1027`, `value: null`) with his values and is DEPLOYED before this card. `tunable_int` raises `CosConfigError` on a null (`src/cobalt/cos/session.py:76-85`), called at the start (`src/cobalt/cos/run.py:99`); `request_ttl_min` raises on a null (`src/cobalt/hitl/actions.py:62-71`).
- HIS INPUTS: GATE RESULT D14 and agent stopped = his ruling's R row (retire yes/no); X15 = his phone result row. Each stays an unfilled GATE RESULT placeholder until the desk writes it from his row.
- ORDER: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --bootstrap-only "<card>" com.cobalt.cos` → `ADMITTED: com.cobalt.cos · bootstrap-only` → 4.6L `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist`, `launchctl print gui/501/com.cobalt.cos` (found, `path = ` that plist) → smoke (s) → `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --owed-clear "<card>" com.cobalt.cos` → `OWED CLEARED: com.cobalt.cos`. `com.cobalt.agent` is not touched.
- FILES AND OBJECTS IT TOUCHES: launchd label `com.cobalt.cos` (loaded); `/Users/cobalt/cobalt/logs/cos.log`, `/Users/cobalt/cobalt/logs/cos.err` (new, `ops/com.cobalt.cos.plist:33`, `:35`); `/Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` (the cos entry removed); `/Users/cobalt/cobalt/data/cos/scratch/` (emptied and made, `src/cobalt/cos/run.py:103`); production DB at cos's first start: the jobs row of `com.cobalt.cos` (`run.py:150`, `:155`), `cobalt_cos_sessions`, `cobalt_cos_turns` (`src/cobalt/cos/migrations/0001_cobalt_cos.sql:14`, `:28`) and `cobalt_hitl_requests` (`src/cobalt/hitl/migrations/0001_cobalt_hitl.sql:20`), each `CREATE … IF NOT EXISTS` (`run.py:105`, `:109`).
- ROLLBACK (returns the old state): `launchctl bootout gui/501/com.cobalt.cos`, then `launchctl print gui/501/com.cobalt.cos` → `Could not find service` (STEP-5 (1L); an `add` label stays out, (2L)). With `--owed-clear` run last, a red smoke (s) leaves the owed entry in place. No revert: nothing merged. The log files, the scratch dir and the `IF NOT EXISTS` tables stay.
- HUB STEPS WITH NO CARD VALUE (no code tip): P2 and P3 (no `## SHIPS` row), P5 (no gate worktree), P7, STEP-T, STEP-R, STEP-G, D2.0's `deploy-shipped.sh --moved`, D2.1–D2.3, D2.6's `pre-<JOB>` tag at a merge, STEP-4 4.1–4.6, smoke (f)'s `jobs restarts <pre-merge>..<stack-final>`, and the ROLLBACK STRING's revert.
- gate report `reports/cos-gate-run-2026-10-20.md` at `7de50210`: `GATES DONE · ok: 10 · fail: 1 · not run: 3`; X13 ruled PASS by the brain (row R2197 of `reports/cto-2026-10-20.md`): 11 OK. Brief: row R2198 of `reports/cto-2026-10-20.md`.
- SMOKE READS row 5 (`cos turn failures`): `Traceback` = 0 proves the poll; LaunchAgent auth stays UNPROVEN (L70) until one DM turn of his after the hub's green, asked by day in one sentence and confirmed by the desk; `CoS turn FAILED` > 0 → bootout cos, record `FAILED: smoke (s)`; the agent is not brought back by this step, a rollback is his.
- tunables 933 — P1 probes cos/hitl unknown-green while com.cobalt.cos is in bootstrap-owed.json (mirrors watchdog.py:441-449), BAND MID; hitl.page_base_url his value, owed before 929 (WAITS) — brain 9b07db5a 2026-10-20
- written by hand by drafter `draft-cos-bootstrap` at 2026-10-20 17:38 ET (`date`); `ops/desk/deploy-card.sh` cannot cut a card with no code branch.
