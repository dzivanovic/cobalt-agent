# The desk stops with unblocked work: brain answer · 2026-10-09
Source: his report in the brain session, 10-09 ~11:30 ET ("This is still happening. Desk just stops and waits"), with the desk transcript after R721. A defect he reports: surveyed, fixed, deployed, "please check", no A/B (R685, L78).

## §0 Cause
The stop-guard (card 66, LIVE) blocks a desk stop only on the `OWED:` lines under `## §5 CURRENT` (`ops/desk/stop-guard.py:22`, `:92`, `:270`). At R721 the block held two lines, and BOTH read as settled:
- `OWED: DISARM one-tap card 134 … | live: aa94b309`: the brain's id, which counts as live because it is a session not named `cto-desk`. The desk's own work hid behind another seat's id.
- `OWED: S4-P1 72 / S4-P2 73 … ; D2 then D1 guard cards now unblocked (R707) | waiting on Dejan`: two items on one line. The S4 builds do wait on his Finviz-rate D2, but the guard cards D2 and D1 are the desk's (R707), and they were settled by HIS marker. The Finviz question had not even been put to him ("I haven't opened that question yet"), so the marker was false.
- The four startable cards (HTTPS-only, guard D2→D1, `/radar` 51 names, ARM on unsized) sat only as `QUEUE` rows in the session TABLE, which the guard does not read.
So the guard passed and the turn ended with a menu. Cost, his word: over an hour of idle time after the smoke (R721, 10:40 ET), until he pushed the desk. The behaviour broke the rule (L78), and the bookkeeping let the guard miss it.

## RULE NOW (the desk records it as a DESK RECORD row and keeps it from this turn on)
1. Every piece of work the desk can start is its OWN `OWED:` line with no marker until it is launched; then `| live: <that worker's id>` or `| live: watch <path>`. No `QUEUE` row in the table for work that has no live session.
2. `| live: <id>` names the session doing THAT item. The brain's id settles only an item the brain is answering right now.
3. `| waiting on Dejan` only on a line that holds ONE question already put to him, citing its row: `OWED: <question> (asked R<n>) | waiting on Dejan`. A question not yet asked is put to him in the same turn, as one line with the recommended answer, before the line is written.
4. A turn never ends with "tell me which" or "or I'll take them in order". The desk takes the order and launches.

## CARD ROW (same feature, card 66, small fix by L75; the desk's drafter writes it on card 66 from this text)
G7 · WHAT THE GUARD READS. (a) In `## §5 CURRENT`, a session-table row whose first cell starts with `QUEUE` → unsettled, `start it: <its prompt cell>`. (b) A `waiting on Dejan` item is settled only when its `<what>` holds `R<digits>`; without one → `start it: ask him: <what>`. (c) A `live: <id>` that matches the row of the BRAIN seat (name `brain`) settles only an item whose `<what>` contains `brain`; else unsettled. Reds, each exit 0 on BASE and exit 2 after: a §5 table row `| QUEUE | — | x card | …` with `owed: none`; `OWED: build 72 | waiting on Dejan` with no `R<n>`; `OWED: launch https card | live: <brain id>` with a fake `desk-list.sh` row named `brain`. Negative controls, exit 0 before and after: `OWED: Finviz rate D2 (asked R722) | waiting on Dejan`; `OWED: brain checks card 134 draft | live: <brain id>`. Files: `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`. Touched tests plus the deploy gate; no re-check (L75, R376).

## FACTS THE DESK HAD WRONG IN THE SAME TRANSCRIPT
- The guard D2/D1 brief is NOT only in a message: it is `reports/guard-d1-d2-answer-2026-10-09.md`. The drafter reads that file.
- There are two D2s: the guard card D2 (`G3 by path`, the desk's) and the S4 Finviz-rate D2 (his). Keep them apart in every row.
- The card 134 check: `aa94b309` is closed. The new brain judges the 134 draft's DECISIONS when the desk sends them.
