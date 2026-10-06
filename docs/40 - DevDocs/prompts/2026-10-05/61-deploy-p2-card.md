JOB: deploy-p2-1005
LADDER: S3-P3 · F14
BRANCH: deploy/deploy-p2-1005
WORKTREE: deploy-p2-1005
BASE: main
TIP: 6269f05e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-p2-1005.md
RULINGS: 2026-10-03 R326, 2026-10-05 R376, 2026-10-05 R390, 2026-10-05 R412
TAG: deploy-2026-10-05-p2
MIGRATIONS: none
SET: s3

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `f15/p2-replay-1004` | `437c7299` | `6269f05e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md` | `held unfixed: 0` and `ready: YES` |  |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...f15/p2-replay-1004`, 23 files, 3445 insertions, 31 deletions). The branch is STACKED on D5's build: its BASE is D5's BUILT tip `3c1f75b8` (build report, `## RESTARTS`), and `merge-base main f15/p2-replay-1004` is `3e40359a` (the K3 check tip), so the diff carries D5's code too. P2's own ten files (`git -C /Users/cobalt/cobalt diff --stat 3c1f75b8 f15/p2-replay-1004`), each with its RESTARTS class from the build's `uv run cobalt jobs restarts 3c1f75b8..HEAD` (the check's `## Suites` names the line `RESTARTS: com.cobalt.aset com.cobalt.radar`): `src/cobalt/cards/predictions.py` (static import reach `com.cobalt.aset,com.cobalt.radar`); `src/cobalt/cards/cli.py` (static import reach `com.cobalt.radar`); `ops/desk/gate-lists.md` (operator script; no Cobalt reader); `tests/cobalt/test_f15_p2_replay.py`, `tests/cobalt/test_f15_p2_replay_db.py`, `tests/experiments/f15_p2/conftest.py`, `tests/experiments/f15_p2/test_x7_x10_x11_db.py` (each: test/documentation; no resident); `docs/40 - DevDocs/cobalt/cards/cli.md`, `docs/40 - DevDocs/cobalt/cards/predictions.md`, and the builder's report `docs/40 - DevDocs/reports/f15-p2-build-2026-10-04.md` (each: DOCS). The thirteen D5 files the stack adds (the same `main...f15/p2-replay-1004` listing): `src/cobalt/aset/drc_page.py`, `src/cobalt/drc/build.py`, `src/cobalt/drc/imports.py`, `src/cobalt/drc/units.py` (the K3 card's class for these paths: static import reach `com.cobalt.aset,com.cobalt.radar`; not re-derived on this range), `src/cobalt/drc/reconcile.py` (new; no class derived by any check of P2), `tests/cobalt/test_drc_d5.py`, `tests/cobalt/test_drc_d5_db.py`, `tests/cobalt/test_drc_d5_experiments_db.py` (each: test/documentation; no resident), `docs/40 - DevDocs/cobalt/aset/drc_page.md`, `docs/40 - DevDocs/cobalt/drc/build.md`, `docs/40 - DevDocs/cobalt/drc/imports.md`, `docs/40 - DevDocs/cobalt/drc/reconcile.md`, `docs/40 - DevDocs/cobalt/drc/units.md` (each: DOCS). RESTARTS: `com.cobalt.aset com.cobalt.radar` (the check's line; no `UNCLASSIFIED` in the build's derivation). Production is DOWN by his R327 and K3's deploy `07a4b8fe` started `com.cobalt.aset` and `com.cobalt.radar`, so P2's restart is a restart of two running residents. The head is a report-only commit above the code tip: `git -C /Users/cobalt/cobalt log --oneline 437c7299..f15/p2-replay-1004 -- tests src configs ops` prints nothing, and `rev-parse --short=8 f15/p2-replay-1004` gives `6269f05e`. No migration file is in the diff (`git -C /Users/cobalt/cobalt diff --stat main...f15/p2-replay-1004 -- src/cobalt/db_migrations` prints nothing). The row has no fix round: the check's `tip:` `437c7299` is the code tip and the `fix report` cell is empty.

## MARKERS
- `grep -c -F "def corpus(" /Users/cobalt/cobalt/src/cobalt/cards/predictions.py` · before `0` · after `1`
- `grep -c -F "def replay(" /Users/cobalt/cobalt/src/cobalt/cards/predictions.py` · before `0` · after `1`
- `grep -c -F "def cmd_replay" /Users/cobalt/cobalt/src/cobalt/cards/cli.py` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/cobalt/test_f15_p2_replay.py` · before `No such file or directory` · after the path listed
- `ls /Users/cobalt/cobalt/tests/experiments/f15_p2/conftest.py` · before `No such file or directory` · after the path listed
- `ls /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · before `No such file or directory` · after the path listed (D5's file, carried by the stack)

## SMOKE READS
- f15-p2 replay tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_f15_p2_replay.py` · exit 0, a count of 1 or more
- f15-p2 corpus command · `grep -c -F "def cmd_replay" /Users/cobalt/cobalt/src/cobalt/cards/cli.py` · exit 0, a count of 1 or more

## RECORDS
- f15-p2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md` last line: CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · house A: Grok FINDINGS: 0 (Sol METER) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0
- f15-p2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 f15/p2-replay-1004` → `6269f05e`; code tip `437c7299`. The build report's last line: `BUILT · job: f15-p2 · tip: 437c7299 | on 3c1f75b8 | migration: none | offline 3926/0 | with-DB 878/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 5 · for Dejan: 0`.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- Merges onto main by reading: `git -C /Users/cobalt/cobalt merge-base main f15/p2-replay-1004` → `3e40359ac99508105d7bed5dc849ca336f3bd1b3` (K3's check tip; main holds `07a4b8fe`, `git merge-base --is-ancestor 07a4b8fe main` exit 0). `git -C /Users/cobalt/cobalt diff --name-only 3e40359a main` over the P2 paths (`docs/40 - DevDocs/cobalt`, `src/cobalt/aset`, `src/cobalt/drc`, `src/cobalt/cards`, `tests/cobalt`, `tests/experiments`, `ops/desk/gate-lists.md`) names `docs/40 - DevDocs/cobalt/cli.md`, `tests/cobalt/test_drc_k3.py`, `tests/cobalt/test_validate_no_db.py`; none is one of the 23 files above (main's `cli.md` is not `cards/cli.md`). No overlap by name. The trial merge at the old main `57c7502c` (`02-deploy-s3-card.md` `## RECORDS`): `main 6269f05e` → clean `022d9f19`; `c96b5118 6269f05e` → clean `c02eeec7`; not repeated at the current main.
- P2 stack: D5's BUILT tip `3c1f75b8` is an ancestor of `f15/p2-replay-1004` and of D5's head `c96b5118` (`merge-base --is-ancestor`, exit 0 both) and NOT of main (exit 1). D5's own fixes since (`3c1f75b8..c96b5118`, five commits) are not in P2's branch; the P2 branch carries D5's build only.
- Production state: DOWN by his R327 until S3 resumes; K3 (`07a4b8fe`) started `com.cobalt.aset` and `com.cobalt.radar`. They are running now.
- S3 smoke reads this deploy needs: the f15-p2 replay-tests line above (the P2 line of the S3 card's `## SMOKE READS`); the other two S3 lines (drc-k3, cobalt-guard-b) belong to their own deploys.
- S3 card preconditions for P2, as `02-deploy-s3-card.md` words them: MARKERS read on the main checkout before and in the job tree after (`predictions.py` `1`, tests `32` in `f15-p2-1004`; `git log -S` adds the string at `735d0344`); MIGRATIONS `none` (`diff --stat main...6269f05e -- src/cobalt/db_migrations` prints nothing). Window: a feature deploys when READY at any hour (LAWS L43; his R389, R390).
- FOLLOW-UP OWED, NOT PART OF THIS DEPLOY (R326, S3 card `02` `## RECORDS` item 2): F15 P2 X11, the `no_trigger` row: a card that EXPIRES with its entry never traded through gets no `missed` row (`replay_card` → `no_trigger`, `replay/runner.py:431-432`) and reads `awaiting nightly replay` for good (`reports/f15-p2-build-2026-10-04.md` DECISION 3).
- one feature per deploy (his R390): S3 on resume = K3 (DEPLOYED `07a4b8fe`), then P2, then D5 after card `03`.
- written by the drafter `p2-deploy-draft` on 2026-10-05, 22:40 EDT (`date`), from `02-deploy-s3-card.md` row 2 and the P2 check report, in the form main's `CARD.md` and `ops/desk/deploy-card.sh` take (seven columns). The stack and the open decisions are in `reports/p2-deploy-draft-2026-10-05.md` `## DECISIONS`.
