# K3 deploy card draft (2026-10-05)

## §0 Headline
K3 single-feature deploy card written: `prompts/2026-10-05/51-deploy-k3-card.md`, one SHIPS row, head `3e40359a` = code tip (no code commit after it).
Merges onto main by reading: merge base `979ec797`, no file K3 touches changed on main. No migration. BRANCH, WORKTREE, TAG and REPORT are all absent today.
Main takes seven columns (`fix report` last); the cell is empty. 2 decisions for the desk.

## CARD
- JOB `deploy-k3-1005` · LADDER `S3-P3 · F14` · BRANCH `deploy/deploy-k3-1005` · WORKTREE `deploy-k3-1005` · BASE `main`
- TIP `3e40359a` · REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-k3-1005.md`
- RULINGS `2026-10-03 R326, 2026-10-03 R327, 2026-10-05 R368, 2026-10-05 R376, 2026-10-05 R390, 2026-10-05 R412`
- TAG `deploy-2026-10-05-k3` · MIGRATIONS `none` · SET `s3`
- RESTARTS `com.cobalt.aset com.cobalt.radar` (production DOWN, R327: a start)
- Markers: `store.py` `def superseded_stated_ids` 0 → 1; `build.py` `CALENDAR_INPUT` 0 → 2; `ls test_drc_k3.py` absent → present. Smoke: `def test_` count in `test_drc_k3.py` (54 on the tip).
- `«FILL` count: 0.

## DECISIONS
- ASK DESK: RULINGS carries R368 and R327 because the S3 card lists them for K3, but R368's d2 skip was "for this JOB only" (`deploy-s3-1005`). The card's G (d2) line uses the siblings' wording, not the skip. Drop R368 from RULINGS? [19:07 EDT] Default taken: kept as the S3 card lists them; G (d2) as the siblings.
- ASK DESK: `SET` is `s3`, as the S3 card has it, so the stop line names the set `s3` for a one-feature deploy. A different word (`s3-k3`)? [19:07 EDT] Default taken: `s3`.

## RECORDS
- Head: `rev-parse --short=8 drc/k3-surfaces-1004` → `3e40359a`; `git log --oneline 3e40359a..drc/k3-surfaces-1004 -- tests src configs ops` → empty.
- Merge: `merge-base main drc/k3-surfaces-1004` → `979ec79706cb62726698922ce825f01e733b3732`; `diff --stat main...drc/k3-surfaces-1004` → 20 files, 2590 insertions, 43 deletions. `diff --stat 979ec797 main` over K3's paths → empty. No overlap. Main's `src/cobalt/cli.py` and `docs/.../cobalt/cli.md` are not K3's `drc/cli.py` files.
- Absent: `rev-parse --verify` fails for `deploy/deploy-k3-1005` and `deploy-2026-10-05-k3`; `ls` fails for the worktree and the report.
- Check last line: pass 2 · tip 3e40359a · held unfixed: 0 · ready: YES · RESTARTS `com.cobalt.aset com.cobalt.radar`.
- Classes from the check's `## Suites`: six `src` files `com.cobalt.aset,com.cobalt.radar`; `drc/cli.py` `com.cobalt.radar`; seven tests no resident; six DOCS.
- Before values on main read with `grep -c -F`; after values read from `git show 3e40359a:<path>`: `store.py` 1, `build.py` 2, `test_drc_k3.py` 54 `def test_`.
- Shape: `CARD.md` and `ops/desk/deploy-card.sh:207` on main carry `fix report` as a seventh column.
- The date read at 19:07 EDT.

K3 DEPLOY CARD DRAFTED · decisions: 2
