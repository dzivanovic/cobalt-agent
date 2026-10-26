JOB: prefill-refresh-bootstrap
LADDER: S5-P2 · F4
BRANCH: none
WORKTREE: none
BASE: main
TIP: none
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-prefill-refresh-bootstrap.md
RULINGS: 2026-10-18 R1833, 2026-10-18 R1863
TAG: deploy-2026-10-27-prefill-refresh-bootstrap
MIGRATIONS: none
SET: prefill-refresh
TICKERS: none
WAITS: f4-probe DEPLOYED, 1045 SECOND PASS (X7 offline tests, X15 probe), his X7 render read, his X9 Sync read

## LAUNCHD
com.cobalt.prefill-refresh · add · prompts/2026-10-18/726-f4-304-recut-card.md:C2 · dry run: none

## GATE RESULTS
GATE RESULT: com.cobalt.prefill-refresh · X10 · OK — the attempt2 deploy gate, reports/deploy-f4-refresh-attempt2.md:263 (offline 8539/0 · with-DB 5552/0 · live-note 146/0 on db62c4b5); no fresh gate (brain R2463)
GATE RESULT: com.cobalt.prefill-refresh · X8 · RULED post-load watch, not a load gate (FINAL :214 R3; brain R2463) — offline leg from reports/f4-gate-run-2026-10-26.md

## NOT IN THIS JOB
- A merge, an outage, a restart of `com.cobalt.aset`, `com.cobalt.radar` or any other label.
- A kickstart of `com.cobalt.prefill-refresh`: `RunAtLoad` is false (`ops/com.cobalt.prefill-refresh.plist:149-150`); its first firing is the next weekday entry.
- Any edit of `prefill.refresh_interval_min`, `prefill.refresh_window` or the plist: X8's watch result is its own card.
- The X7, X9 and X15 `GATE RESULT` lines: the desk writes each from its source (`## RECORDS` HIS INPUTS) only when it reads `OK`; no seat fills a placeholder.

## MARKERS
- `grep -c -F "com.cobalt.prefill-refresh" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` · before `1` · after `0`

## SMOKE READS
- the refresh plist on main · `grep -c -F "<string>com.cobalt.prefill-refresh</string>" /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` · prints 1 or more
- the refresh subcommand registered · `grep -c -F "REFRESH_JOB = \"com.cobalt.prefill-refresh\"" /Users/cobalt/cobalt/src/cobalt/prefill/cli.py` · prints 1

## CHECK ASKS
- X1 4.6L-BO loads `com.cobalt.prefill-refresh` alone, outside its window (before 05:45 or after 15:45 ET on a weekday, or a weekend), no other deploy in between.
- X2 `deploy-step-c.sh --bootstrap-only` refuses while any of X7, X9, X15 has no line (`ops/desk/deploy-step-c.sh:182-186`); that refusal is the load rule holding.
- X3 The X8 watch and the X9 launchd watch are desk jobs after the green stop line, not smoke.

## RECORDS
- F4 gate 1045 — X10 OK from the attempt2 deploy gate; X8 post-load watch (FINAL :214 R3); X15 load gate by probe card f4-probe (+X7 two offline tests); X7 render and X9 Sync legs his; X9 firings post-load — brain 9b07db5a 2026-10-26
- LOAD RULE (brain R2463): X10 OK; X15 OK by the f4-probe probe; X7 the offline tests OK plus his render leg; X9 the hub legs OK plus his Sync leg. X8 does not gate the load.
- HIS INPUTS AND SOURCES: X7 = 1045's X7 line (both offline legs passed, pass 1 and pass 2) plus his render read; X9 = 1045's X9 line (derive `RESTARTS: com.cobalt.aset com.cobalt.radar`, no `ESCALATE:`; bounce 28 s) plus his Sync read; X15 = 1045's X15 line, `PROBE X15 OK …`. Each line is written `OK — <its sources>` by the desk, or not at all.
- X8 WATCH (R2463): on the first loaded weekday, count per-minute Finviz requests and 429s per consumer from the logs, first read 10:00 ET. A peak over 50 or a 429 on radar → raise `prefill.refresh_interval_min` and regenerate the plist in one change, as its own card.
- X9 WATCH (R2463): the launchd firings and sleep/wake, read post-load under the window rule (`prefill.refresh_window` 05:45–15:45 ET).
- ORDER: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --bootstrap-only "<card>" com.cobalt.prefill-refresh` → `ADMITTED: com.cobalt.prefill-refresh · bootstrap-only` → 4.6L `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist`, `launchctl print gui/501/com.cobalt.prefill-refresh` (found, `path = ` that plist) → smoke → `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --owed-clear "<card>" com.cobalt.prefill-refresh` → `OWED CLEARED: com.cobalt.prefill-refresh` (`DEPLOY-HUB.md:146`).
- FILES AND OBJECTS IT TOUCHES: launchd label `com.cobalt.prefill-refresh` (loaded); `/Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` (its entry removed); at its first firing (not this run): `/Users/cobalt/cobalt/logs/prefill-refresh.log`, `.err` (`ops/com.cobalt.prefill-refresh.plist:151-154`), his real daily note's `trading` and `market_calendar` units (`COBALT_VAULT_PATH`, `:14-15`), the production `vault_writes` and job rows.
- ROLLBACK (returns the old state): `launchctl bootout gui/501/com.cobalt.prefill-refresh`, then `launchctl print gui/501/com.cobalt.prefill-refresh` → `Could not find service` (STEP-5 (1L)). With `--owed-clear` run last, a red smoke leaves the owed entry in place. No revert: nothing merged.
- The `## LAUNCHD` line is card 778's (`prompts/2026-10-18/778-deploy-f4-refresh-card.md:21`) with `deferred` → `add` and no gate field (`CARD.md:69`; `deploy-step-c.sh:176`).
- HUB STEPS WITH NO CARD VALUE (no code tip): as card 929 `## RECORDS` (P2, P3, P5, P7, STEP-T, STEP-R, STEP-G, D2.0–D2.3, D2.6's tag at a merge, STEP-4 4.1–4.6, smoke (f)'s restarts, the revert).
- TAG: dated 2026-10-27, the earliest launch after the WAITS; the desk re-dates it at launch if later.
- written by hand by drafter `draft-f4-gate-run` (prompt 1043, R2463) on 2026-10-26 (`date`), as 929 was (R236); `ops/desk/deploy-card.sh` cannot cut a card with no code branch.
