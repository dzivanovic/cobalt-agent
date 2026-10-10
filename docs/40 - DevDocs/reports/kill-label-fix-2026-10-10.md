## §0 Headline
- `--kill com.cobalt.aset` → `--kill aset` in DEPLOY-HUB.md (4.2 (3), STEP-5 (3) (3)) and the STANDING-LIST.md row.
- "SAME pid" → "the same pid set" in those three sequences; "DRAFT" and "awaiting his yes" removed from the row.
- Uncommitted, working tree only.

## DECISIONS
- DEPLOY-HUB.md:145 "the SAME pid" (restart-set check, not the kill sequence) left unchanged.
- Remaining `com.cobalt.aset` hits name the launchd job; left unchanged.

## RECORDS
- `grep -n -F -e "--kill com.cobalt.aset"` in both files → no hit.
- `grep -n -F -e "--kill aset"` → DEPLOY-HUB.md:137, DEPLOY-HUB.md:162, STANDING-LIST.md:149.
- `git diff --stat`: my files are DEPLOY-HUB.md and STANDING-LIST.md; the other modified files were already dirty before this run.

KILL LABEL FIXED · places: 3 · decisions: 2
