JOB: deploy-p2-1005
LADDER: S3-P3 · F14
BRANCH: deploy/deploy-p2-1005-attempt2
WORKTREE: deploy-p2-1005-attempt2
BASE: main
TIP: 6269f05e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-p2-1005-attempt2.md
RULINGS: 2026-10-03 R326, 2026-10-05 R412
TAG: deploy-2026-10-05-p2-attempt2
MIGRATIONS: none
SET: s3

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `f15/p2-replay-1004` | `437c7299` | `6269f05e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md` | `held unfixed: 0` and `ready: YES` |  |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...f15/p2-replay-1004`, 10 files, 1822 insertions, 4 deletions; every file is P2's own, none is D5's or K3's). D5 is on main (`c8503415`), so `merge-base main f15/p2-replay-1004` is now `3c1f75b8` (D5's BUILT tip, P2's BASE). Each file with its RESTARTS class from the build's `uv run cobalt jobs restarts 3c1f75b8..HEAD` (the check's `## Suites` names the line `RESTARTS: com.cobalt.aset com.cobalt.radar`): `src/cobalt/cards/predictions.py` (static import reach `com.cobalt.aset,com.cobalt.radar`); `src/cobalt/cards/cli.py` (static import reach `com.cobalt.radar`); `ops/desk/gate-lists.md` (operator script; no Cobalt reader); `tests/cobalt/test_f15_p2_replay.py`, `tests/cobalt/test_f15_p2_replay_db.py`, `tests/experiments/f15_p2/conftest.py`, `tests/experiments/f15_p2/test_x7_x10_x11_db.py` (each: test/documentation; no resident); `docs/40 - DevDocs/cobalt/cards/cli.md`, `docs/40 - DevDocs/cobalt/cards/predictions.md`, and the builder's report `docs/40 - DevDocs/reports/f15-p2-build-2026-10-04.md` (each: DOCS). RESTARTS: `com.cobalt.aset com.cobalt.radar` (the check's line; no `UNCLASSIFIED` in the build's derivation). Production is DOWN by his R327 and K3's deploy `07a4b8fe` started `com.cobalt.aset` and `com.cobalt.radar`, so P2's restart is a restart of two running residents. The head is a report-only commit above the code tip: `git -C /Users/cobalt/cobalt log --oneline 437c7299..f15/p2-replay-1004 -- tests src configs ops` prints nothing, and `rev-parse --short=8 f15/p2-replay-1004` gives `6269f05e`. No migration file is in the diff (`git -C /Users/cobalt/cobalt diff --stat main...f15/p2-replay-1004 -- src/cobalt/db_migrations` prints nothing). The row has no fix round: the check's `tip:` `437c7299` is the code tip and the `fix report` cell is empty.

## MARKERS
- `grep -c -F "def corpus(" /Users/cobalt/cobalt/src/cobalt/cards/predictions.py` · before `0` · after `1`
- `grep -c -F "def replay(" /Users/cobalt/cobalt/src/cobalt/cards/predictions.py` · before `0` · after `1`
- `grep -c -F "def cmd_replay" /Users/cobalt/cobalt/src/cobalt/cards/cli.py` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/cobalt/test_f15_p2_replay.py` · before `No such file or directory` · after the path listed
- `ls /Users/cobalt/cobalt/tests/experiments/f15_p2/conftest.py` · before `No such file or directory` · after the path listed

## SMOKE READS
- f15-p2 replay tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_f15_p2_replay.py` · exit 0, a count of 1 or more
- f15-p2 corpus command · `grep -c -F "def cmd_replay" /Users/cobalt/cobalt/src/cobalt/cards/cli.py` · exit 0, a count of 1 or more

## RECORDS
- f15-p2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md` last line: CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · house A: Grok FINDINGS: 0 (Sol METER) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0
- f15-p2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 f15/p2-replay-1004` → `6269f05e`; code tip `437c7299`. The build report's last line: `BUILT · job: f15-p2 · tip: 437c7299 | on 3c1f75b8 | migration: none | offline 3926/0 | with-DB 878/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 5 · for Dejan: 0`.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- Merges onto main by reading: `git -C /Users/cobalt/cobalt merge-base main f15/p2-replay-1004` → `3c1f75b8307ba355667fef64d8a38b8702b1b3f9` (D5's BUILT tip, an ancestor of main). `git -C /Users/cobalt/cobalt diff --name-only 3c1f75b8 main` over the ten files above prints nothing: main changed none of P2's files since the merge base (K3 `07a4b8fe` and D5 `c8503415` included; main's `cobalt/cli.md` is not `cards/cli.md`). No overlap. The earlier trial merges (at the old main `57c7502c`, `02-deploy-s3-card.md` `## RECORDS`) are not repeated at the current main.
- P2 ships alone: D5 DEPLOYED `c8503415`, K3 `07a4b8fe`. `git -C /Users/cobalt/cobalt merge-base --is-ancestor c96b5118 main`, `… 3c1f75b8 main`, `… 07a4b8fe main`, `… c8503415 main` → exit 0 each. The branch's diff against main holds P2's ten files only (the stack note of the earlier draft is gone; the brain's ruling 10-05 under his R474).
- Production state: DOWN by his R327 until S3 resumes; K3 (`07a4b8fe`) started `com.cobalt.aset` and `com.cobalt.radar`. They are running now.
- Markers dropped: `drc/reconcile.py` (`ls` exit 0 on main now: D5's file, no longer a P2 marker).
- K3-F1 mark record (read-only, from the earlier report): at `437c7299`, `tests/cobalt/test_f15_p2_replay.py` (32 tests) reaches no database (every read a `FakeReads`; the two CLI tests monkeypatch `predictions.CardReads`); `tests/cobalt/test_f15_p2_replay_db.py` sets module `pytestmark = [requires_db, pytest.mark.integration]`; `tests/experiments/f15_p2/test_x7_x10_x11_db.py` sets `pytestmark = [requires_db]`. Module-level `requires_db` in P2's test files; no unmarked database test.
- S3 smoke reads this deploy needs: the f15-p2 replay-tests line above (the P2 line of the S3 card's `## SMOKE READS`); the other two S3 lines (drc-k3, cobalt-guard-b) belong to their own deploys.
- S3 card preconditions for P2, as `02-deploy-s3-card.md` words them: MARKERS read on the main checkout before and in the job tree after (`predictions.py` `1`, tests `32` in `f15-p2-1004`; `git log -S` adds the string at `735d0344`); MIGRATIONS `none` (`diff --stat main...6269f05e -- src/cobalt/db_migrations` prints nothing). Window: a feature deploys when READY at any hour (LAWS L43).
- FOLLOW-UP OWED, NOT PART OF THIS DEPLOY (R326, S3 card `02` `## RECORDS` item 2): F15 P2 X11, the `no_trigger` row: a card that EXPIRES with its entry never traded through gets no `missed` row (`replay_card` → `no_trigger`, `replay/runner.py:431-432`) and reads `awaiting nightly replay` for good (`reports/f15-p2-build-2026-10-04.md` DECISION 3).
- written by the drafter `p2-deploy-draft` on 2026-10-05, 22:40 EDT, from `02-deploy-s3-card.md` row 2 and the P2 check report, in the form main's `CARD.md` and `ops/desk/deploy-card.sh` take (seven columns); re-pointed by the drafter `p2-repoint` on 2026-10-05, 23:31 EDT (`date`), now that D5 is on main (`reports/p2-repoint-draft-2026-10-05.md`).
