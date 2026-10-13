# draft-f21-amend · 2026-10-13

## §0 Headline
- Card 468 G1 (c) now carries the card 448 M1 rule (`grep -rn "0024" tests`, move every pin) and the sixteen files (seven plus the preflight's nine), each `file:line` proven by grep at HEAD `a6c6335c`.
- The `files` column of G1 points at the (c) grep's files. `## RECORDS` gained the BASE re-proof line (each pin to 0026) and the read line.
- Card 469 is unchanged: V4 already says "card 468 G1 (c)".
- `BASE`, `«FILL` cells, TIP and headers untouched; no F5 or 0025 text added.

## DECISIONS

## RECORDS
- `grep -rnE "0024|strike_alerts" tests` (Grep, `*.py`): the seven listed files match their cited lines, and the nine added files match the preflight check 12 lines. Strike test files that name 0024 only to apply it are not tail pins and are not added.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `a6c6335c`; `git -C /Users/cobalt/cobalt status --short -- src tests ops/desk/gate-lists.md` → empty, so the working tree equals HEAD on those paths.
- Card 448 M1 read (`448-dml-roles-card.md:18`): its rule is "re-run `grep -rn "0024" tests`".
- `grep -n "G1 (c)" 469-f21-vectors-card.md` → line 22 (V4), unchanged.

DRAFTED · decisions: 0
