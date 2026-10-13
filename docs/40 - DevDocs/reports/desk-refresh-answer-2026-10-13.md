# Desk refresh at 300k — HIS RULING and the card, 2026-10-13

His words (brain session, 10-13), on survey row 5: "I need desk to MUST restart and hand off as soon as it's next number red above 300K and it MUST read it's size on every turn to know if it is over" · "I don't want to add another block to desk, it will just stop and say I am blocked waiting for Dejan, or it will just idle" · "Yes, and we have to ensure that old desk must write it's handover so no work is lost".

The desk records it as HIS RULING · APPROVED, writes memory now (10-05 ROW C) and launches the drafter (Opus).

## §0 Headline
- Survey row 5 is KEPT: the 300k launch refusal stays. The desk becomes unable to stay past 300k, with no new block.
- Three parts: a per-turn size line, a REFRESH order at 300k, and a forced refresh if the desk does not act.
- No work is lost: the desk's state is written every turn, the handover is written before any stop, and the successor reconciles live sessions against it.

## THE CARD (one card, K5; the drafter writes it; its header names the ONE install line)
| row | what |
|---|---|
| R1 MEASURE EVERY TURN | A hook on the desk session runs `desk-context.sh <desk id> 300000` after every desk turn and prints `DESK SIZE <n> / 300,000` into the desk's context. The desk never measures by hand. |
| R2 STATE EVERY TURN | The same hook checks that `## §5 CURRENT` of the day's desk report carries a `STATE AT <hh:mm>` stamp from this turn's hour. If it is stale, it prints `UPDATE §5 CURRENT NOW` first. The §5 table (live sessions, watches, OWED rows) is the handover's body at every moment. |
| R3 THE ORDER AT 300k | At ≥300,000 the hook prints, instead of the size: `REFRESH NOW: (1) write the HANDOVER line and §5 CURRENT, (2) run <the successor launch command>, (3) stop.` These are exact commands, not a block: every other tool still works. |
| R4 FORCED REFRESH | If the desk is still live one turn or 10 minutes after the order, the refresh script sends the desk one final message, `WRITE HANDOVER NOW`, and waits up to 5 minutes for a new `HANDOVER:` line in the report. Then, either way, it launches the successor desk on the day's report and stops the old desk. If no line came, it writes `HANDOVER: FORCED — no line from <old id>; successor reconciles` itself. It never waits for Dejan. |
| R5 SUCCESSOR RECONCILES | Every new desk's first act lists the live sessions (ListAgents / herdr tabs) against §5's table, re-arms every watch, and records each difference as a row. Nothing running is lost even when the handover is thin. |
| R6 INSTALL | The hook entries live in settings.json, which no seat can edit. The card's header gives the ONE line he pastes once, by day, with why. After that it runs for every desk. |

## ALSO FROM THIS REVIEW
- Survey row 5: KEPT (his reason: the old "REFRESH OWED" printing led to a 700k desk).
- Still waiting on his word: survey rows 11 (L62) and 17 (L66/L61), and the desk's hand-edit line for `bare-guard.py` in settings. Recommended: yes, yes, and drop the line.

## FOR THE CHECK
`desk refresh 2026-10-13 HIS RULING: size measured by hook every turn; REFRESH order at 300k; forced refresh after 1 turn or 10 min, handover written or FORCED line; successor reconciles live sessions; one install line by day; survey row 5 KEPT`
