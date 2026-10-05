## §0 Headline
The S3 card `02-deploy-s3-card.md` no longer ships D5 (`c96b5118`): TIP is `3e40359a 6269f05e 47ec01c5`, SHIPS has three rows (K3, P2, guard-b).
D5's MARKER, SMOKE READ, check/head lines, THE CARRY and FOLLOW-UP (1) are gone; the drop record is added.
K3's two markers/reads hold at `3e40359a` (checked). Two RECORDS lines still name D5 and are left as written (DECISIONS 1).

## CARD
- `TIP: 3e40359a 6269f05e 47ec01c5`
- `## SHIPS`: row 2 `drc/d5-reconcile-1004` dropped; P2 is now 2, guard-b 3.
- `## MARKERS`: dropped the `reconcile.py` `ls` line.
- `## SMOKE READS`: dropped the `test_drc_d5.py` line.
- `## RECORDS`: dropped the two drc-d5 lines (check, head), THE CARRY (P2), and FOLLOW-UP item (1); item (2) kept as written, still numbered `(2)`.
- `## RECORDS` added last: `D5 (c96b5118) dropped by the desk's R378 (L43): G (c) red, K3-6 on the K3/D5 seam, deploy-s3-1005-attempt2.md; D5's seam fix is a build on card 03 (R376).`
- Untouched: `BRANCH`, `WORKTREE`, `TAG`, `REPORT`, `RULINGS`, `JOB`, the (d2) line, every K3, P2 and guard-b line.

## DECISIONS
1. ASK DESK: two kept RECORDS lines still mention D5 — the trial-merge line (`main c96b5118`, `c96b5118 6269f05e` clauses) and the MARKERS/SMOKE desk-answer line (`reconcile.py`, `drc-d5-1004`, test count `27`). Left unchanged because they mix K3/P2/guard-b facts. Default: leave as history; the recut's STEP-T merge is binding. [07:46 EDT]
2. ASK DESK: FOLLOW-UP item numbering stays `(2)` (P2 X11 line unchanged, per "keep every P2 line"). Default: keep. [07:46 EDT]
3. K3 markers, checked without D5: `def superseded_stated_ids` is in `src/cobalt/drc/store.py` at `3e40359a` (count 1); `tests/cobalt/test_drc_k3.py` exists there with `def test_` lines. No K3 marker was dropped. P2 and guard-b markers are untouched (card: no other head touches those files).

## RECORDS
- Edited by the Edit tool only; no git write, no launch.
- `reconcile.py` is absent at `3e40359a` (`git show` → path does not exist), which confirms it is D5's alone.
- Time of drafting: 2026-10-05 07:46 EDT (`date`).

S3 CARD REDRAFTED · ships: K3, P2, guard-b · decisions: 3
