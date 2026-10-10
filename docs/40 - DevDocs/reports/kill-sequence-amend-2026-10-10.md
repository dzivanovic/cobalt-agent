## §0 Headline
- Both DEPLOY-HUB orphan places (4.2 `:137`, STEP-5 (3) `:162`) and the STANDING-LIST row (`:149`) now state the brain's five-step `--kill` sequence (R927) and both stop rules.
- Old "same call again, then STEP-5" wording: 0 left. No new command, no `sleep`.
- Not committed; awaiting his yes.

## DECISIONS
- ASK DESK: `git diff --stat` lists 9 files, not 2. The other 7 (`.claude/settings.json`, five reports, `seat-usage.md`) were already modified in the tree at session start (see the opening git status); I touched none of them. [15:00] Default: left as is; commit only the two prompt files.

## RECORDS
- Sequence, `DEPLOY-HUB.md:137` (4.2): "(1) `…orphan-clean.sh aset` (dry run) → … `none found` … `verified 0` = clean, no kill, go on to 4.3; … `verified <n>` with n ≥ 1 … = a verified orphan; (2) `date`, then the SAME dry run → the SAME pid, still ppid 1 and `-m cobalt.aset`; (3) `…orphan-clean.sh --kill com.cobalt.aset` once; (4) the dry run again → `none found` or `verified 0`; (5) go on to 4.3. Any difference at (2), or any orphan at (4) → no second kill, STEP-5 (nothing merged), each pid into `## DECISIONS` FOR DEJAN."
- Sequence, `DEPLOY-HUB.md:162` (STEP-5 (3)): same steps (1)–(4); "(5) continue with the bootstrap. Any difference at (2), any orphan at (4), or exit 1 = no second kill, residents stay down (aset no bootstrap), `DECISION 0: aset orphan … — FOR DEJAN`."
- Row, `STANDING-LIST.md:149`: "ONLY in this sequence: (1)…(5); any difference at (2) or any orphan at (4) → no second kill: at 4.2 STEP-5 ending FOR DEJAN, inside STEP-5 (3) residents stay down, FOR DEJAN; a first dry run that finds nothing → no kill, the run continues."
- `grep -c -F "same call again"` on both files: 0.
- `git diff --stat`: `DEPLOY-HUB.md | 4 +-`, `STANDING-LIST.md | 1 +` among 9 files (7 pre-existing, see DECISIONS).
- Only these two files edited, plus this report. The 4.2 existing exit-1 rule (`REFUSED:` / `UNVERIFIED:` → STEP-5) is kept.

KILL SEQUENCE AMENDED · files: 2 · decisions: 1
