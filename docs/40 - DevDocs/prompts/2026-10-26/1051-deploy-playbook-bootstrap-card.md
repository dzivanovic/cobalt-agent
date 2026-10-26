JOB: playbook-bootstrap
LADDER: S5-P2 · F23
BRANCH: none
WORKTREE: none
BASE: main
TIP: none
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-playbook-bootstrap.md
RULINGS: 2026-10-18 R1863, 2026-10-26 R2465
TAG: deploy-2026-10-27-playbook-bootstrap
MIGRATIONS: none
SET: playbook
TICKERS: none
WAITS: 1046 (F23 gate run) GATES DONE, 1050 (render seat) RENDER DONE and its SECOND PASS, his E1 viewer read and E2 clip read

## LAUNCHD
com.cobalt.playbook · add · prompts/2026-10-13/503-f23-card.md:P6 · dry run: none

## GATE RESULTS
GATE RESULT: com.cobalt.playbook · E5 · RULED MOOT — gated the code deploy, DEPLOYED 7398d4a7 2026-10-18 (uv sync at 4.5); this bootstrap restarts nothing (brain R2465)
GATE RESULT: com.cobalt.playbook · E6 · RULED post-load watch, not a load gate — the proof is a weekday `cobalt jobs check` after load (brain R2465); offline leg from reports/f23-gate-run-2026-10-26.md

## NOT IN THIS JOB
- A merge, an outage, or a restart of any label.
- A kickstart or manual render of `com.cobalt.playbook`. `RunAtLoad` is false (`ops/com.cobalt.playbook.plist:44`), and its first firing is Sunday 17:30 ET.
- `cobalt jobs register`: the deploy hub's line bars it (`DEPLOY-HUB.md:3`, "NO `jobs register`"). No string is added (brain R2465).
- The E1, E2 and E4 `GATE RESULT` lines. The desk writes each from its source (`## RECORDS` HIS INPUTS), and only when it reads `OK`. No seat fills a placeholder.

## MARKERS
- `grep -c -F "com.cobalt.playbook" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` · before `1` · after `0`

## SMOKE READS
- the playbook plist on main · `grep -c -F "<string>com.cobalt.playbook</string>" /Users/cobalt/cobalt/ops/com.cobalt.playbook.plist` · prints 1
- the playbook subcommand mounted · `grep -c -F "playbook_cli.add_parser(sub)" /Users/cobalt/cobalt/src/cobalt/cli.py` · prints 1

## CHECK ASKS
- X1 4.6L-BO loads `com.cobalt.playbook` alone, with no other deploy in between, and not on a Sunday between 17:00 and 17:45 ET.
- X2 `deploy-step-c.sh --bootstrap-only` refuses while any of E1, E2 or E4 has no line (`ops/desk/deploy-step-c.sh:182-186`). That refusal is the load rule holding.
- X3 EXPECTED, NOT A RED SMOKE: the first heartbeat sweep after the load reads `RED com.cobalt.playbook unregistered — no jobs row existed — registered now; nothing has run yet`, once (`src/cobalt/jobs/watchdog.py:451-456`). The sweep registers the row itself, and the next beat reads `never run yet (registered, not yet due)` until Sunday (`:336`). Any other red line on the label, or this one a second time, is a red smoke.
- X4 The E6 weekday check and the first-Sunday firing watch are desk jobs after the green stop line, not smoke.

## RECORDS
- F4 reservation card drafted in parallel, launched only on the X15 FAIL; F23 E1/E2 dev render by a K2 seat plus his open legs; E4 settled offline (+ first-Sunday watch); E5 moot; register only if already on the line; E6 post-load weekday check — brain 9b07db5a 2026-10-26
- LOAD RULE (brain R2465): E4 `OK` from 1046 (parity tests plus `date +%Z`, settled offline); E1 = 1050's kill leg OK + his viewer read; E2 = 1050's decks + his clip read; E5 moot; E6 post-load. E6 does not gate the load.
- HIS INPUTS AND SOURCES: E1 = 1046's E1 offline leg, 1050's `E1 kill leg` line and its SECOND PASS line, plus his app read. E2 = 1046's E2 offline leg plus his clip read on 1050's two synthetic decks. E4 = 1046's E4 line. The desk writes each line as `OK — <its sources>`, or not at all.
- THE UNREGISTERED BEAT (brain R2465 item 4): `cobalt jobs register` is not on the deploy hub's line, so no string is added. The one `unregistered` RED beat after the load is expected and is recorded here and in CHECK ASKS X3.
- E6 WATCH (R2465): on the first weekday after the load, `COBALT_ENV=production uv run cobalt jobs check` (the desk's own read) prints the label's line. A red or `(MISSED)` line before the first Sunday → FINAL `:161`'s consequence applies: one manual render, as its own card.
- E4 WATCH (R2465): the first Sunday 17:30 ET firing. Read `logs/playbook.log` and the label's job row. A firing at other than 17:30 ET wall-clock → FINAL `:159`'s consequence applies: the plist shape changes, as its own card. System TZ: `/etc/localtime -> …/America/New_York`.
- ORDER: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --bootstrap-only "<card>" com.cobalt.playbook` → `ADMITTED: com.cobalt.playbook · bootstrap-only` → 4.6L `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.playbook.plist`, `launchctl print gui/501/com.cobalt.playbook` (found, `path = ` that plist) → smoke → `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh --owed-clear "<card>" com.cobalt.playbook` → `OWED CLEARED: com.cobalt.playbook` (`DEPLOY-HUB.md:146`).
- FILES AND OBJECTS IT TOUCHES: launchd label `com.cobalt.playbook` (loaded); `/Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` (its entry removed); the production `jobs` row for the label (registered by the first sweep). At its first firing (not this run): `/Users/cobalt/cobalt/data/playbook/<date>/`, `/Users/cobalt/cobalt/logs/playbook.log` and `.err` (`ops/com.cobalt.playbook.plist:46-49`), and a read of his live vault's strategy notes (`:20`, no write, L28).
- ROLLBACK (returns the old state): `launchctl bootout gui/501/com.cobalt.playbook`, then `launchctl print gui/501/com.cobalt.playbook` → `Could not find service` (STEP-5 (1L)). With `--owed-clear` run last, a red smoke leaves the owed entry in place. No revert: nothing merged. The registered `jobs` row stays; it is harmless while the label is unloaded and listed as owed (`watchdog.py:441`).
- The `## LAUNCHD` line is card 779's (`prompts/2026-10-18/779-deploy-f23-playbook-card.md:21`), with `deferred` → `add` and no gate field (`CARD.md:69`; `deploy-step-c.sh:176`).
- HUB STEPS WITH NO CARD VALUE (no code tip): as card 929 `## RECORDS` (P2, P3, P5, P7, STEP-T, STEP-R, STEP-G, D2.0–D2.3, D2.6's tag at a merge, STEP-4 4.1–4.6, smoke (f)'s restarts, the revert).
- TAG: dated 2026-10-27, the earliest launch after the WAITS. The desk re-dates it at launch if later.
- Written by hand by drafter `draft-f23-gate-run` (prompt 1044, revision R2465) on 2026-10-26 (`date`), as 1048 was. `ops/desk/deploy-card.sh` cannot cut a card with no code branch.
