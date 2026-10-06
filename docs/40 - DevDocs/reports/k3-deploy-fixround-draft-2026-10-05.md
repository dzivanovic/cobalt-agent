# k3-deploy-fixround draft — 2026-10-05

## §0 Headline
Card `51-deploy-k3-card.md` is re-pointed on the fix-round path: TIP `44e8de82`, code tip `0ebdf95e`, check report unchanged, `fix report` = the new `reports/drc-k3-fixround-2026-10-05.md`.
The new file's last line is the branch report's stop line, byte for byte (proved: `git grep -c -F` of the typed line at `44e8de82` → 1).
`3e40359a` is an ancestor of `0ebdf95e`; the head adds the build report only; the shipped files are the same 20.
Owed before the launch: the desk commits the new fix report on main (the launcher needs it committed and unmodified).

## DECISIONS
1. ASK DESK: commit `reports/drc-k3-fixround-2026-10-05.md` on main (no git write in this seat). Default: commit it alone, then `desk-launch.sh recut`. [before the recut]
2. ASK DESK: the trial merge `main 3e40359a` → `6fdc7001` in RECORDS is from the old tip and not repeated (`git merge-tree` is not on this seat's allow line). Default: the card now says so; the deploy's own gate merges the real tree. [before the launch]

## RECORDS
- Facts proved with git: `log --oneline 3e40359a..drc/k3-surfaces-1004` → `44e8de82`, `0ebdf95e`; `diff --stat 0ebdf95e..44e8de82` → the build report only; `diff --stat main...0ebdf95e` → 20 files, the same set as at `3e40359a`; `merge-base --is-ancestor 3e40359a 0ebdf95e` → exit 0; check report last line `tip: 3e40359a`, `held unfixed: 0`, `ready: YES`.
- Gate numbers quoted from the branch report `## K3-F1`: offline 3869/0 · with-DB 4730/0 · live-note 146/0.
- MARKERS AFTER at `0ebdf95e` (`git grep -c -F`): `def superseded_stated_ids` 1, `CALENDAR_INPUT` 2, `requires_db` in `test_drc_k3.py` 3. BEFORE on main: 0, 0 and (file absent) 0; the `ls` marker is unchanged. New marker added for K3-F1.
- Edited the card in place: header TIP, SHIPS row, files line, MARKERS, RECORDS (head line, the K3/D5 seam line replaced, trial-merge note, written-by line). Kept: RULINGS `R412`, L43/R389 wording, G (d2) wording. `grep -c -F "«FILL"` → 0. No rename done.
- Shell note: pipes with `git` were refused by the bare-command hook; the counts were taken with `git grep -c -F <rev> -- <path>` instead.
- Files written: the fix report and this report. Only the card was edited.

K3 DEPLOY CARD RE-POINTED · decisions: 2
