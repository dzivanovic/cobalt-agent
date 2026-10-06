JOB: deploy-d5-1005
LADDER: S3-P3 · F14
BRANCH: deploy/deploy-d5-1005
WORKTREE: deploy-d5-1005
BASE: main
TIP: c96b5118
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-d5-1005.md
RULINGS: 2026-10-03 R326, 2026-10-05 R350, 2026-10-05 R412
TAG: deploy-2026-10-05-d5
MIGRATIONS: none
SET: s3

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `drc/d5-reconcile-1004` | `c96b5118` | `c96b5118` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-check-2026-10-04.md` | `held unfixed: 1` and `ready: NO` |  |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...drc/d5-reconcile-1004`, 15 files, 2124 insertions, 29 deletions), each with its RESTARTS class (the build report's `## RESTARTS`, `uv run cobalt jobs restarts 3e40359a..HEAD`; the check's `## Suites` gives the same 15 rows and no `UNCLASSIFIED`): `src/cobalt/aset/drc_page.py`, `src/cobalt/drc/build.py`, `src/cobalt/drc/imports.py`, `src/cobalt/drc/units.py` (each: static import reach `com.cobalt.aset,com.cobalt.radar`); `src/cobalt/drc/reconcile.py` (new, `A`: static import reach `com.cobalt.aset,com.cobalt.radar`); `ops/desk/gate-lists.md` (operator script; no Cobalt reader); `tests/cobalt/test_drc_d5.py`, `tests/cobalt/test_drc_d5_db.py`, `tests/cobalt/test_drc_d5_experiments_db.py` (each: test/documentation; no resident); `docs/40 - DevDocs/cobalt/aset/drc_page.md`, `docs/40 - DevDocs/cobalt/drc/build.md`, `docs/40 - DevDocs/cobalt/drc/imports.md`, `docs/40 - DevDocs/cobalt/drc/reconcile.md`, `docs/40 - DevDocs/cobalt/drc/units.md`, and the builder's report `docs/40 - DevDocs/reports/drc-d5-build-2026-10-04.md` (each: DOCS). RESTARTS: `com.cobalt.aset com.cobalt.radar` (the check's line). Production state: K3's deploy `07a4b8fe` started both residents, so D5's restart is a restart of two running residents. The head is the code tip: `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/d5-reconcile-1004` gives `c96b5118`, and `git -C /Users/cobalt/cobalt diff --stat c96b5118 drc/d5-reconcile-1004` prints nothing. No migration file is in the diff (`git -C /Users/cobalt/cobalt diff --stat main...drc/d5-reconcile-1004 -- src/cobalt/db_migrations` prints nothing). The row has no fix round: the check's `tip:` `c96b5118` is the code tip and the `fix report` cell is empty.

The stop-line literals are the check's own, as it ends: `held unfixed: 1` and `ready: NO` (`ops/desk/desk-launch.sh` `ships_checked` reads each backticked literal of this cell and requires the check's last non-blank line to end with it or carry it followed by a space: `case "$clast" in *"$lit"|*"$lit "*)`; it reads no other `ready` or `held unfixed` text, and a ruling row is never read against the stop line, only checked for its own shape through `RULINGS`). The line carries `held unfixed: 1 · open: 3 …` and `ready: NO · decisions: 5 …`, so both match. `ops/desk/deploy-card.sh` (lines 130–131) would refuse this card (it demands `held unfixed: 0` and `ready: YES`), so the card is written by hand in its form, as `02-deploy-s3-card.md` was.

## MARKERS
- `ls /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · before `No such file or directory` · after the path listed
- `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_d5.py` · before `No such file or directory` · after the path listed
- `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_d5_db.py` · before `No such file or directory` · after the path listed
- `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_d5_experiments_db.py` · before `No such file or directory` · after the path listed
- `grep -c -F "reconcile" /Users/cobalt/cobalt/src/cobalt/drc/units.py` · before `5` · after `8`
- `grep -c -F "refused_cards" /Users/cobalt/cobalt/src/cobalt/drc/build.py` · before `0` · after `2`
- `grep -c -F "NO_WRITER_CODE" /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · before `0` (the file is absent on main) · after `4`
- `grep -c -F "requires_db" /Users/cobalt/cobalt/tests/cobalt/test_drc_d5_db.py` · before `0` (the file is absent on main) · after `4` (the import line and the three `@requires_db` tests)

## SMOKE READS
- drc-d5 tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_drc_d5.py` · exit 0, a count of 1 or more
- drc-d5 reconcile module · `grep -c -F "NO_WRITER_CODE" /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · exit 0, a count of 1 or more

## RECORDS
- drc-d5: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-check-2026-10-04.md` last line: CHECK DONE · job: drc-d5 · pass: 2 · tip: c96b5118 · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · suites: offline 3898/0 · with-DB 867/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 18 · ready: NO · decisions: 5 · for Dejan: 3
- drc-d5: head `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/d5-reconcile-1004` → `c96b5118`; code tip `c96b5118`. The held item, quoted from the check (`## DECISIONS` 3): "O1 HELD, NOT FIXED (a carried held defect; confirmed again by house B, B3). An unresolved item stored on a date that a later statement re-pairs is lost (`store.py:935`). Its red is pinned as `test_check_o1_…` (strict xfail). Fixing it needs a build: a card row naming `src/cobalt/drc/store.py`, or a store for the items (a migration). Default: ships as a known gap, pinned."
- THE O1 CARRY (his ruling): R326 (`cto-2026-10-03.md`, 10-05 06:19 ET, `HIS RULING · APPROVED`, committed `b1337431`): "A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording)". R350 (`cto-2026-10-05.md`, 10-05 06:47 ET, `HIS RULING · APPROVED`, committed `e89ef63a`) restates it: "10-02 R4 already let D5 ship with O1 pinned on 10-04; the brain's A/B was its error; the 10-05 standing row restates it." D5 ships with O1 pinned as a strict `xfail` (`tests/cobalt/test_drc_d5.py`, `test_check_o1_a_re_paired_date_keeps_its_stored_unresolved_item`; the gate counts it among `2 xfailed`). The O1 store and the B2 wording are owed rows on card `03` (R381), NOT part of this deploy. 10-02 R4 is a `LAUNCHED` row, not a ruling row, so it is not cited.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- K3/D5 seam: K3-6 tests reaching the DB offline when D5 is stacked is fixed on main by K3-F1 `0ebdf95e`, inside `07a4b8fe` (K3 DEPLOYED). D5 never touches `tests/cobalt/test_drc_k3.py`: `git -C /Users/cobalt/cobalt diff --stat 3e40359a..c96b5118 -- tests/cobalt/test_drc_k3.py` prints nothing.
- If the gate reds on a D5 test that reaches the database without `requires_db`, that is K3's pattern: a fix row on card `03` on the fix-round path, no check (the brain's ruling). Read at `c96b5118`: none found. The four with-DB tests (`test_drc_d5_db.py` ×3, `test_drc_d5_experiments_db.py` ×1) each carry `@requires_db`; `test_drc_d5.py` holds no `requires_db`, `migrated` or `psycopg` use and is offline.
- Merges onto main by reading: `git -C /Users/cobalt/cobalt merge-base main drc/d5-reconcile-1004` → `3e40359ac99508105d7bed5dc849ca336f3bd1b3` (K3's check tip; main `d664b926` holds `07a4b8fe`, `git merge-base --is-ancestor 07a4b8fe main` exit 0). `git diff --stat main...drc/d5-reconcile-1004` lists D5's 15 files and no P2 file. `git -C /Users/cobalt/cobalt diff --name-only 3e40359a main` names no one of the 15 (main's `docs/40 - DevDocs/cobalt/cli.md` and `src/cobalt/cli.py` are not `drc/` files; `ops/desk/gate-lists.md` is not in main's list; `tests/cobalt/test_drc_k3.py` is K3's, D5 does not touch it). No overlap by name. The trial merge at the old main `57c7502c` (`02-deploy-s3-card.md` `## RECORDS`): `main c96b5118` → clean `08de26af`; not repeated at the current main.
- Gate history of the check: gates 1 and 2 of pass 1 and gate 1 of pass 2 were red on a `cobalt_dev` migration-0002 DDL `DeadlockDetected` in files this job does not touch; gate 3 (pass 1, `55e43a17`) and gate 2 (pass 2, `c96b5118`) were green: `offline 3898/0 · with-DB 867/0 · live-note 146/0`, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`.
- Open items carried by the check, not part of this deploy: A3 (the event day's reconcile corrects an entry price through `record_correction`, which rewrites the card's fill cache; check `## DECISIONS` 4, default as built, R314 KEEP) and B2 (the status wording after a partial write then a refusal; owed on card `03` by R326). The P2 stack: P2's branch carries D5's build `3c1f75b8` only; after this deploy the trial merge `c96b5118 6269f05e` → clean `c02eeec7` (`02-deploy-s3-card.md`).
- one feature per deploy (his R390): S3 on resume = K3 (DEPLOYED `07a4b8fe`), D5 now (the brain's ruling 10-05 ~23:20 ET: D5 as it stands), then P2 alone.
- written by the drafter `d5-deploy-draft` on 2026-10-05, 22:4x EDT (`date`), by hand from `02-deploy-s3-card.md`'s D5 row, `03-drc-d5-card.md` and the check report, in the form main's `CARD.md` and `ops/desk/deploy-card.sh` take (seven columns); `deploy-card.sh` refuses `held unfixed: 1`.
