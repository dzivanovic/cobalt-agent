## §0 Headline
Card 392 re-pointed to `ops/prodwrite-seat-1012b`, worktree `prodwrite-seat-1012b`, REPORT under that worktree.
Row S kept as is; row S2 added (re-apply `86b9daa5..b96737bf`, 17 paths, tests named).
BASE, TIP, JOB, CHECK REPORT untouched; no placeholder token.

## DECISIONS
- ASK DESK: fill BASE for the new worktree (the card keeps `86b9daa5`; the brain's point is that the new branch is cut from current main, which holds `ba37c2a9`) [12 Oct] — default: the desk sets BASE to main HEAD at launch.

## RECORDS
- `git -C /Users/cobalt/cobalt diff 86b9daa5 b96737bf --stat` → 17 files, 1316 insertions, 37 deletions; the 17 paths are listed in row S2.
- `git -C /Users/cobalt/cobalt rev-parse b96737bf 86b9daa5 ba37c2a9 1966c239` → all four resolve.
- Edited only `prompts/2026-10-12/392-prodwrite-seat-card.md`: header lines 5, 6, 9; row S2 after row S; four `## RECORDS` lines.

DRAFTED · decisions: 1
