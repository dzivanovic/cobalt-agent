# p2-deploy-draft — 2026-10-05

## §0 Headline
- Card written: `prompts/2026-10-05/61-deploy-p2-card.md`, one row, no `«FILL`.
- The P2 branch is STACKED on D5's build (`3c1f75b8`, not on main). `main...f15/p2-replay-1004` lists 23 files, 13 of them D5's. Shipping P2 now ships D5 code with it. DECISION 1.
- Head `6269f05e` is report-only above the code tip `437c7299`. Branch, worktree, tag and report are all absent. No file overlap with main's changes since the merge base.
- Test marks: every P2 test that reaches the database carries `requires_db`. None unmarked.

## CARD
- JOB `deploy-p2-1005` · LADDER `S3-P3 · F14` · BRANCH `deploy/deploy-p2-1005` · WORKTREE `deploy-p2-1005` · BASE `main` · TIP `6269f05e`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-p2-1005.md`
- RULINGS `2026-10-03 R326, 2026-10-05 R376, 2026-10-05 R390, 2026-10-05 R412` · TAG `deploy-2026-10-05-p2` · MIGRATIONS `none` · SET `s3`
- SHIPS: row 1, `f15/p2-replay-1004`, code tip `437c7299`, head `6269f05e`, check `f15-p2-check-2026-10-05.md` (`held unfixed: 0`, `ready: YES`), fix report empty. RESTARTS `com.cobalt.aset com.cobalt.radar`.
- MARKERS: `def corpus(` 0→1, `def replay(` 0→1 (predictions.py); `def cmd_replay` 0→1 (cards/cli.py); `ls` of `test_f15_p2_replay.py`, `tests/experiments/f15_p2/conftest.py`, `drc/reconcile.py` absent→listed. SMOKE: tests `def test_` (32 at the tip), `def cmd_replay`.

## DECISIONS
1. ASK DESK: P2 carries D5's code. `git merge-base main f15/p2-replay-1004` → `3e40359a`; `merge-base --is-ancestor 3c1f75b8 main` → exit 1 (not on main), `… f15/p2-replay-1004` and `… c96b5118` → exit 0. `diff --stat main...f15/p2-replay-1004` names `drc/reconcile.py`, `drc/build.py`, `drc/imports.py`, `drc/units.py`, `aset/drc_page.py`, three `test_drc_d5*` files and five DevDocs pages. The build report says so: STACKED, BASE = D5's BUILT tip. This breaks his R390 (one feature per deploy) and puts D5's unresolved K3/D5 seam (card `03`, R376) into the P2 gate. Default: do NOT launch this card until the brain picks. Recommended: D5 deploys first after card `03`; its head `c96b5118` holds `3c1f75b8`, so P2 then ships its own ten files (the S3 card's trial merge `c96b5118 6269f05e` was clean). The card is written for the branch as it stands. [22:40 ET]
2. ASK DESK: rulings proof. `cto-2026-10-05.md` R412 is `HIS RULING … APPROVED`; `cto-2026-10-03.md` R326 is `HIS RULING · APPROVED`. R376 and R390 are `HIS RULING` but their status cell reads `APPLIED: …`, not `APPROVED`. Default: header keeps all four as the prompt names them (R326 added from the S3 card, since it binds P2's follow-up); if the hub's K23 proof wants `APPROVED`, drop R376 and R390 (no fix round here). [22:40 ET]
3. ASK DESK: restart classes of D5's files on this stack. The check and build derive `jobs restarts 3c1f75b8..HEAD` only (P2's ten files). The card gives the K3 card's class for the four D5 files K3 already classed and none for `drc/reconcile.py` (new). The card's RESTARTS line is the check's. Default: the deploy hub derives `jobs restarts` on the merged range; no command run here (R411, R412). [22:40 ET]

## RECORDS
- Gates absent: `git rev-parse --verify deploy/deploy-p2-1005` and `deploy-2026-10-05-p2` → `fatal: Needed a single revision`; `ls /Users/cobalt/cobalt-wt/deploy-p2-1005` and the report path → `No such file or directory`.
- Head proof: `rev-parse --short=8 f15/p2-replay-1004` → `6269f05e`; `git log --oneline 437c7299..f15/p2-replay-1004 -- tests src configs ops` → empty.
- Main-side overlap: `git diff --name-only 3e40359a main` over the P2 paths names `docs/40 - DevDocs/cobalt/cli.md`, `tests/cobalt/test_drc_k3.py`, `tests/cobalt/test_validate_no_db.py`; none is in the 23 files. K3's `07a4b8fe` is an ancestor of main (exit 0); its code did not touch `drc/*.py` after `3e40359a`.
- Rulings: R412 → `cto-2026-10-05.md:109`; R376 → `:49`; R390 → `:67`; R326 → `cto-2026-10-03.md:332`; R327 → `:333`, R368 → `cto-2026-10-05.md:41` (window and the old S3 skip of (d2); not carried: job-only).
- K3-F1 mark check (read-only; `tests/cobalt/test_drc_k3.py` on main marks its with-DB tests `@requires_db`). At `437c7299`: `tests/cobalt/test_f15_p2_replay.py` (32 tests) reaches no database: every read is a `FakeReads`, and the two CLI tests monkeypatch `predictions.CardReads`. `tests/cobalt/test_f15_p2_replay_db.py` sets module `pytestmark = [requires_db, pytest.mark.integration]`, so all its tests are marked. `tests/experiments/f15_p2/test_x7_x10_x11_db.py` sets `pytestmark = [requires_db]`. No unmarked database test in P2's files. The difference from K3 is module-level `pytestmark` against per-test `@requires_db`; `conftest.py` (`offline_skip_guard`) reads a module's `pytestmark`. A RECORD, not a defect. The D5 stack tests (`test_drc_d5_db.py` marks each with-DB test `@requires_db`) were not audited past that; card `03` owns the seam.
- `sh` and git were read-only; no test, file or branch of the build changed.

P2 DEPLOY CARD DRAFTED · decisions: 3
