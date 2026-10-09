# Desk pane by id: card draft · 2026-10-09

## §0 Headline
- Card 197 written: four rows (P1–P4), all in `prompts/CTO-DESK-WAKEUP.md` (`:14`, `:22`, `:24`); the brain's FIX 1–4.
- Red per row is a `grep -c -F`: old sentence 1 on BASE `a82d8b6f`, 0 after; `· pane <id>` 0, then 1.
- No script parses the HANDOVER line in a way the `· pane` tail breaks; no extra row.
- `BASE` is left as `«FILL»` for the desk.

## CHANGES
- Wrote `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/197-desk-pane-by-id-card.md` (header, `## ROWS`, `## NOT IN THIS JOB`, `## READ`, `## CHECK ASKS`, `## RECORDS`).
- Wrote this report. No other file touched; no git write, no launch.

## DECISIONS
1. The brain's red `grep -c 'VIEW it in the "CTO" tab'` matches the checklist, not the wake-up (0 there on BASE). The card's red uses the wake-up's own old sentences instead.
2. P1 drops "never `herdr pane list`" from the VIEW line, since the new rule tests the id against that list.
3. The `(stuck; ended by successor)` HANDOVER variant keeps its shape; the successor takes the pane id from §5 CURRENT.
4. FIX 5 (the one-time NOW re-attach) is the desk's by hand and sits in `## NOT IN THIS JOB`.
5. CHECK ASKS X1 is the brain's FOR THE CHECK line verbatim; X2 and X3 are mine.

## RECORDS
- HEAD `a82d8b6f` (`git rev-parse --short=8 HEAD`). `git diff --stat a82d8b6f -- CTO-DESK-WAKEUP.md` prints nothing, so the working file equals HEAD. I read the file with the Read tool rather than `git show`, and this diff check stands in for it.
- Grep counts on that file: P1 clause 1, P2 sentence 1, P3 sentence 1, `· pane <id>` 0.
- `grep` in `ops/desk/*`: only `desk-wake.sh:75` parses the line (`^HANDOVER: .* at HH:MM`, still matches with the tail). `gate-lists.md:30` matched "panel". `stop-guard.py` has no HANDOVER match. `~/.claude/ops` has no HANDOVER match.
- Read: `CARD.md`, `desk-tab-answer-2026-10-09.md`, `CTO-DESK-WAKEUP.md`, `topics/cto-desk-checklist.md` lines 1–20 (not edited), `areas/cobalt.md`, `topics/writing-rules.md`, `ops/desk/desk-wake.sh:70–85`.
- RESTARTS: none.

DESK PANE CARD DRAFTED · decisions: 5
