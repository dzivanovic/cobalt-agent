JOB: deploy-drc-d5-o1-b2-1006
LADDER: OFF-LADDER — cto-2026-10-03.md R326
BRANCH: deploy/deploy-drc-d5-o1-b2-1006
WORKTREE: deploy-drc-d5-o1-b2-1006
BASE: main
TIP: 38e0d47e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-drc-d5-o1-b2-1006.md
RULINGS: 2026-10-03 R326, 2026-10-05 R412, 2026-10-05 R474
TAG: deploy-2026-10-06-drc-d5-o1-b2
MIGRATIONS: none
SET: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/drc-d5-o1-b2-1006` | `edd4d584` | `38e0d47e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-o1-b2-check-2026-10-06.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-o1-b2-build-2026-10-06.md` |

Card 39 (D5 O1 + B2 + O2). The check ended `held unfixed: 1 · ready: NO` (the one held item is O2, `/drc` page reads `build_day` only); row O2 of the job card widened the card to `imports.py` `_unresolved_lines` and the fix round (the fix report above, last line `BUILT · … tip: edd4d584 … rows: 4 of 4`) fixed it. Code tip `edd4d584` is the fix round's; the check's tip `9be877dc` is its ancestor; branch head `38e0d47e` adds the build report only (`git -C /Users/cobalt/cobalt diff --stat edd4d584 38e0d47e -- . ":(exclude)docs"` prints nothing).

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/drc-d5-o1-b2-1006`, 13 files, 527 insertions, 20 deletions), each with its RESTARTS class (the build's `uv run cobalt jobs restarts 4d9e451c..HEAD` at `edd4d584`, 13 rows, no `UNCLASSIFIED`):
- `src/cobalt/drc/store.py` (O1: `record_day` keeps the day's open items on its `day` row), `src/cobalt/drc/build.py` (`_unresolved` reads them; the later-day carry), `src/cobalt/drc/reconcile.py` (B2: `_status` says `then refused`), `src/cobalt/drc/units.py` (the docstring) and `src/cobalt/drc/imports.py` (O2: `_unresolved_lines` falls back to the `day` row): each class `static import reach` → `com.cobalt.aset,com.cobalt.radar`.
- `tests/cobalt/test_drc_d5.py` and `tests/cobalt/test_drc_d5_db.py` (test/documentation; no resident).
- `docs/40 - DevDocs/cobalt/drc/build.md`, `imports.md`, `reconcile.md`, `store.md`, `units.md` and `docs/40 - DevDocs/reports/drc-d5-o1-b2-build-2026-10-06.md` (DOCS).
RESTARTS: com.cobalt.aset com.cobalt.radar (the deploy restarts aset and radar, about 50 s down). No migration file, no `ops/` path in the diff.

## MARKERS
- `grep -c -F "_open_items" /Users/cobalt/cobalt/src/cobalt/drc/store.py` · before `0` · after `3`
- `grep -c -F "then refused" /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · before `0` · after `1`
- `grep -c -F "kept = derived_day" /Users/cobalt/cobalt/src/cobalt/drc/build.py` · before `0` · after `1`
- `grep -c -F "def _items(rows" /Users/cobalt/cobalt/src/cobalt/drc/imports.py` · before `0` · after `1` (O2)

## SMOKE READS
- the items kept on the day row (O1) · `grep -c -F "_open_items" /Users/cobalt/cobalt/src/cobalt/drc/store.py` · exit 0, a count of 1 or more
- the status after a write then a refusal (B2) · `grep -c -F "then refused" /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · exit 0, a count of 1 or more
- the later-day carry (check O1) · `grep -c -F "kept = derived_day" /Users/cobalt/cobalt/src/cobalt/drc/build.py` · exit 0, a count of 1 or more
- the page fallback (O2) · `grep -c -F "def _items(rows" /Users/cobalt/cobalt/src/cobalt/drc/imports.py` · exit 0, a count of 1 or more

## RECORDS
- drc-d5-o1-b2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-o1-b2-check-2026-10-06.md` last line: CHECK DONE · job: drc-d5-o1-b2 · pass: 1 · tip: 9be877dc · house A: Sol FINDINGS: 1 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · house B: Grok FINDINGS: 1 · suites: offline 3942/0 · with-DB 4826/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 20 · ready: NO · decisions: 2 · for Dejan: 2 · tokens: 198504
- drc-d5-o1-b2: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-o1-b2-build-2026-10-06.md` last line: BUILT · job: drc-d5-o1-b2 · tip: edd4d584 | on 4d9e451c | migration: none | offline 3945/0 | with-DB 4829/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 1 · tokens: 128005
- drc-d5-o1-b2: one fix round, no re-check (L75, R347, R438; desk record R545 widened the card to O2). Check tip `9be877dc` is an ancestor of the code tip `edd4d584` (`git merge-base --is-ancestor` exit 0); branch head `38e0d47e` (`rev-parse --short=8`) adds docs only past `edd4d584`. The gate on `edd4d584` (the fix round's): offline 3945/0, with-DB 4829/0, live-note 146/0, `cobalt_dev: 0013`, `.env: removed`.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut.
- FOLLOW-UP for him, NOT part of this deploy: the check's `## OPEN` A1 / B1, the D5-3 rule question. A stored copy of a carried item on a later day does not clear when its origin day's reconcile later succeeds, with or without a re-pair; whether a cleared origin clears every later stored copy is a D5-3 change, outside this card.
- AFTER values above were read from the checked-out worktree `/Users/cobalt/cobalt-wt/drc-d5-o1-b2-1006` (clean, head `38e0d47e`, `src/` identical to `edd4d584`; the `store.py` count also read from `git show edd4d584:src/cobalt/drc/store.py`), BEFORE values from main's working tree, at drafting time 2026-10-06; the deploy re-proves each with `git -C /Users/cobalt/cobalt show edd4d584:<path>`.
- Absent today: `git rev-parse --verify` of `deploy/deploy-drc-d5-o1-b2-1006` and of `deploy-2026-10-06-drc-d5-o1-b2` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-drc-d5-o1-b2-1006` and of the REPORT path both failed.
- one feature per deploy (his R390).
