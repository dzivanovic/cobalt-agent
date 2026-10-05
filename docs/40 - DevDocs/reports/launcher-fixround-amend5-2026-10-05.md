## §0 Headline
- Card 21 (`prompts/2026-10-02/21-launcher-checks-card.md`) amended: the literals wording corrected in F2 (line 29, incl. its RULE sentence), F3 (line 30), F4 (line 31).
- Now says: on a fix-round row, `tip:` of the check is an ancestor of the code tip; `held unfixed: 0` and `ready: YES` are read from the CHECK report's last line; `tip: <code tip>` from the fix report's `BUILT ·` stop line; no-fix-report rows unchanged.
- Edit tool on the card only; nothing else touched. No git write.

## CARD
Replaced in each of lines 29, 30, 31 the clause "the literals and (the) `tip: <code tip>` are read from the fix report's `BUILT ·` stop line" with "the literals `held unfixed: 0` and `ready: YES` are read from the CHECK report's last line, and `tip: <code tip>` is read from the fix report's `BUILT ·` stop line" (F4 keeps its following "; the literals column stays…").

## DECISIONS
None.

## RECORDS
- Read before, line 29 (F2 RULE sentence): old clause present once.
- Read before, line 30 (F3): old clause present once.
- Read before, line 31 (F4): old clause present once.
- Read after: grep `CHECK report's last line` → 3 occurrences (lines 29-31); grep of the old clause → 0.
- The "header sentence near line 29" is the F2 RULE sentence; no other occurrence of the old wording exists in the file (grep count of "read from" was 3 before).

LAUNCHER FIXROUND AMENDED 5 · decisions: 0
