# draft-f5-x3-values-pf-fix — 2026-10-20

## §0 Headline
- Card 958 edited in place: the two preflight FAILs (checks 18, 21) are fixed.
- DEPLOY PROOF lines 3 and 4 now end at `after `1``; the parentheticals moved to `## RECORDS`.
- T2's `>= 256` clause is dropped; T1, T2 and X2 agree. X2 now reads "no 25, no 256 spelled".
- "both 2026-09-09" became "both undated lines of `ops/logs/mainframe.log`" (one occurrence, line 29).
- Nothing run, nothing committed.

## DECISIONS
1. Check 21 — second form (drop `>= 256`). The card's rule text (WHY: "floor 256") sets the floor for the value, not for the test. The test keeps `int, multiple of 64`, and T2 says the floor is held by the value in the file. T1's "never spells 25 or 256" now holds.
2. The other DEPLOY PROOF lines follow the same rule: lines 60–63 end at `after `N``. Lines 64 and 65 carry no `· before`, so the smoke reads them by their `curl` and `ls` shapes (preflight check 20, OK).
3. NOTES 1 and 2 of the preflight are untouched, as ordered. The undated-lines fix is note 1's wording only.

## RECORDS
- 2026-10-20 21:26 EDT (`date`). Nothing run, no git write.
- Reads: prompt 961; card 958 whole; `reports/f5-x3-values-preflight-2026-10-20.md` whole (`## ISSUES`, checks 18 and 21).
- Card edits (Edit only): line 29 COLD row ("both 2026-09-09" reworded); line 28 T2 (`>= 256` clause dropped); X2 (`no 10` → `no 25`); lines 62 and 63 (trailing parenthetical removed); one new line at the top of `## RECORDS` carrying the moved parentheticals.
- Re-proved by Grep on the card after the edits: `2026-09-09`, `>= 256` and `no 10` → 0 hits; `· before … after …` → lines 60–63 end at the backticked `after` value.
- `git show main:` was not re-run: no `file:line` or count was changed or added. The marker counts (2→0, 0→2, 0→1, 0→1) are the ones preflight check 19 proved against BASE.

DRAFTED · decisions: 3
