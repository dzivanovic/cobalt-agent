JOB: deploy-k3-1005
LADDER: S3-P3 · F14
BRANCH: deploy/deploy-k3-1005
WORKTREE: deploy-k3-1005
BASE: main
TIP: 44e8de82
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-k3-1005.md
RULINGS: 2026-10-05 R412
TAG: deploy-2026-10-05-k3
MIGRATIONS: none
SET: s3

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `drc/k3-surfaces-1004` | `0ebdf95e` | `44e8de82` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-fixround-2026-10-05.md` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...0ebdf95e`, 20 files, plus the build report as the head `44e8de82` carries it), each with its RESTARTS class (check report `## Suites`, `jobs restarts 979ec797..HEAD` at `3e40359a`; the K3-F1 build report gives the same `RESTARTS` line at `0ebdf95e`): `src/cobalt/aset/drc_page.py`, `src/cobalt/aset/web.py`, `src/cobalt/drc/build.py`, `src/cobalt/drc/imports.py`, `src/cobalt/drc/store.py`, `src/cobalt/drc/units.py` (each: static import reach `com.cobalt.aset,com.cobalt.radar`); `src/cobalt/drc/cli.py` (static import reach `com.cobalt.radar`); `tests/cobalt/test_drc_imports.py`, `tests/cobalt/test_drc_k3.py`, `tests/cobalt/test_drc_k3_db.py`, `tests/cobalt/test_drc_k3_experiments.py`, `tests/cobalt/test_drc_web_seam.py`, `tests/cobalt/test_radar_panel_cards.py`, `tests/cobalt/test_s3_c3_panel_offline.py` (each: test/documentation; no resident); `docs/40 - DevDocs/cobalt/drc/build.md`, `docs/40 - DevDocs/cobalt/drc/cli.md`, `docs/40 - DevDocs/cobalt/drc/imports.md`, `docs/40 - DevDocs/cobalt/drc/store.md`, `docs/40 - DevDocs/cobalt/drc/units.md`, and the builder's report `docs/40 - DevDocs/reports/drc-k3-build-2026-10-04.md` (each: DOCS). RESTARTS: `com.cobalt.aset com.cobalt.radar` (the check's line; no `UNCLASSIFIED`). Production is DOWN by his R327, so the restart is a start. The head adds the build report only: `git -C /Users/cobalt/cobalt diff --stat 0ebdf95e..44e8de82` lists `docs/40 - DevDocs/reports/drc-k3-build-2026-10-04.md` alone, and `rev-parse --short=8 drc/k3-surfaces-1004` gives `44e8de82`. No migration file is in the diff (`git -C /Users/cobalt/cobalt diff --stat main...0ebdf95e -- src/cobalt/db_migrations` prints nothing). The row has a fix round (K3-F1, `tests/cobalt/test_drc_k3.py` only): the check's `tip:` is `3e40359a`, an ancestor of the code tip `0ebdf95e`, and the `fix report` cell is the committed file whose last line is `BUILT · … tip: 0ebdf95e …`.

## MARKERS
- `grep -c -F "def superseded_stated_ids" /Users/cobalt/cobalt/src/cobalt/drc/store.py` · before `0` · after `1`
- `grep -c -F "CALENDAR_INPUT" /Users/cobalt/cobalt/src/cobalt/drc/build.py` · before `0` · after `2`
- `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` · before `No such file or directory` · after the path listed
- `grep -c -F "requires_db" /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` · before `0` (the file is absent on main) · after `3`

## SMOKE READS
- drc-k3 tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` · exit 0, a count of 1 or more

## RECORDS
- drc-k3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md` last line: CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0
- drc-k3: head `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/k3-surfaces-1004` → `44e8de82`; code tip `0ebdf95e` (K3-F1). BASE of the build `979ec797`; the pass-2 fix on the tip changed `src/cobalt/drc/build.py` (`CALENDAR_INPUT`, the stale read), `tests/cobalt/test_drc_k3_experiments.py`, `tests/cobalt/test_drc_k3.py` and one DevDocs page (`git -C /Users/cobalt/cobalt diff --stat c7e65590 3e40359a`).
- Merges onto main by reading: `git -C /Users/cobalt/cobalt merge-base main drc/k3-surfaces-1004` → `979ec79706cb62726698922ce825f01e733b3732` (the build's BASE). Main changed 183 files since it; none is a path K3 touches (`git -C /Users/cobalt/cobalt diff --stat 979ec797 main -- "docs/40 - DevDocs/cobalt/drc" src/cobalt/aset src/cobalt/drc` and the seven K3 test files and the K3 build report prints nothing). The near names are different files: main's `src/cobalt/cli.py` and `docs/40 - DevDocs/cobalt/cli.md` against K3's `src/cobalt/drc/cli.py` and `docs/40 - DevDocs/cobalt/drc/cli.md`.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- The first attempt (`deploy-deploy-k3-1005.md`) failed at the gate on the two K3-6 tests. K3-F1 fixed them: the tests were with-DB tests without the `requires_db` mark, and the `statements` fixture now patches the module `imports` calls. The deploy rides the fix-round path: the check's `3e40359a` is an ancestor of `0ebdf95e`, and the fix report (`reports/drc-k3-fixround-2026-10-05.md`) ends `BUILT · … tip: 0ebdf95e`. The fix report must be committed on main and unmodified before the launch. D5 is NOT in this deploy.
- Open item carried by the check, not part of this deploy: S3 (a flat restatement from the page) stays REJECTED by row K3-6 and goes to follow-up; the flat restatement stays CLI-only.
- S3 card preconditions for K3, as `02-deploy-s3-card.md` words them: MARKERS read on the main checkout before and in the job tree after; the trial merge `main 3e40359a` → clean `6fdc7001` (git objects only, at main `57c7502c`; taken at the old tip, not repeated at `0ebdf95e`). Window: a feature deploys when READY at any hour (LAWS L43; his R389, the NOW line). Production has been down since R327; K3's restart of `com.cobalt.aset` and `com.cobalt.radar` is a start. Residents are down before the merge (L66), as the S3 card words it. Every check of K3 derives RESTARTS `com.cobalt.aset com.cobalt.radar`.
- S3 smoke reads this deploy needs: the drc-k3 tests line above (the only K3 line of the S3 card's `## SMOKE READS`); the other two S3 lines (f15-p2, cobalt-guard-b) belong to their own deploys.
- one feature per deploy (his R390): S3 on resume = K3 first, then P2, then D5 after card `03`. Production is DOWN by his R327 until S3 resumes.
- written by the drafter `k3-deploy-draft` on 2026-10-05, 19:07 EDT (`date`), from `02-deploy-s3-card.md` row 1 and the K3 check report, in the form main's `CARD.md` and `ops/desk/deploy-card.sh` take (seven columns); re-pointed on 2026-10-05 by the drafter `k3-deploy-fixround` onto the fix-round path (code tip `0ebdf95e`, head `44e8de82`, `fix report` filled).
