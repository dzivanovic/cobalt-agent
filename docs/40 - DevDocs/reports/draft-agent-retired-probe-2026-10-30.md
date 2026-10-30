## §0 Headline
Card 1099 written: `prompts/2026-10-30/1099-agent-retired-probe-card.md`, BAND MID, 3 rows (T1 tests, W1 watchdog, K1 smoke K18).
Two job checks read "not loaded" as RED: `src/cobalt/jobs/watchdog.py:448` (heartbeat, `cobalt jobs check`) and `src/cobalt/smoke/checks.py:428` (K18). Both get the record.
The RED did not first show on 10-29: it has been on every close since 10-21 22:51 ET (see DECISIONS 1).
Nothing run, nothing committed, no existing file edited.

## DECISIONS
1. FACT, not an ask: the RED is not new on 10-29. `com.cobalt.agent` was retired 10-21 (`ops/desk/retired-labels` committed `5dfea1164`, 17:10 ET) and stayed registered (`configs/cobalt/jobs.yaml:127`, enabled by default). `watchdog.py` last changed 2026-10-13 (`01fb72978`) and never reads the record, so the RED began at the first beat after the bootout: `close-2026-10-21-now.md:3` (22:51 ET) already lists "com.cobalt.agent not loaded (retired by design)". It sat beside `com.cobalt.replay` failed (10-21 to 10-26), so the header read 2 to 3 jobs and the line was read as one of them; `day-open-2026-10-23.md:91` RED 2 jobs, `close-2026-10-27-now.md:3` is the first close where it is the only one ("1 job"). 10-29 is the day the desk put it to the brain (`cto-2026-10-30.md:6`), not the day it appeared. No code or record change on 10-28 or 10-29 explains a start then.
2. ASK DESK: should "retired but running" also read the pidfile (`logs/cobalt.pid`, a hand-started agent with no launchd label)? The card says no: "running" is "loaded in launchd", the probe both checks already make; the pidfile case is under `## NOT IN THIS JOB`. Default: as the card. [07:13 ET]
3. ASK DESK: RESTARTS is `com.cobalt.cos` by reading (`src/cobalt/cos/run.py:50` imports `jobs.watchdog`), not by `uv run cobalt jobs restarts`, which I did not run (no `uv`). Confirm with the derivation before the deploy plan. Default: the card's `RESTARTS: com.cobalt.cos`, replaced by the derivation's output if it differs. [07:13 ET]
4. FACT: no `CLASS` line. CARD.md's header table lists `CLASS` for no build card (only the prodwrite card names it), and the K1–K5 classes in `LAWS.md` are permission classes (K5 = harness upkeep, not `src/`). The 10-29 precedent card carries `CLASS: K5` for an ops-script-only job; this one edits `src/`.
5. FACT: `BASE` is left `«FILL: …»` (the desk's value, per CARD.md); `TIP`, `CHECK REPORT`, `HOUSE B` are empty. `desk-launch.sh` refuses the card until the desk fills `BASE`.
6. FACT: the `com.cobalt.agent` entry in `configs/cobalt/jobs.yaml` stays (card `## NOT IN THIS JOB`): `tests/cobalt/test_jobs.py:133` reads it and `cobalt validate` holds registry = `ops/` = plists. Dropping it would also end the RED but is a separate item.

## RECORDS
- 07:09 ET `date`; 07:12 ET `date` (card written 07:1x).
- Read `prompts/2026-10-30/1098-draft-agent-retired-probe.md`, `prompts/CARD.md` (whole), `prompts/2026-10-29/1085-launcher-tip-prefix-card.md` (precedent), `Vault/.../topics/writing-rules.md`.
- `git -C /Users/cobalt/cobalt show main:ops/desk/retired-labels` → one line, `com.cobalt.agent`. `git log -- ops/desk/retired-labels` → `5dfea1164 2026-10-21 17:10:52 -0400`.
- `git log -- src/cobalt/jobs/watchdog.py` newest `01fb72978 2026-10-13`; `-- src/cobalt/smoke/checks.py` newest `01fb72978 2026-10-13`; `-- configs/cobalt/jobs.yaml` last touch of the agent entry `0b1def13d 2026-10-18`.
- `git grep main` anchors: `watchdog.py:44,55,63,421,441,448`; `checks.py:426,428,436`; `test_jobs.py:952,955`; `test_smoke.py:1583,1586,1591`; `deploy-step0.sh:77`; `deploy-outage.sh:93`; `cos/run.py:50`.
- Reports read for the first-RED answer: `close-2026-10-21-now.md:3`, `close-2026-10-21.md:35`, `close-2026-10-22…10-27/29-now.md:3`, `day-open-2026-10-20/23/27/29.md:91`, `cto-2026-10-30.md:6,17`.
- Not read: `ops/desk/restarts` derivation output, any test run (none executed).
- Not touched: the working tree's modified files in `git status` (not mine).

DRAFTED · decisions: 2
