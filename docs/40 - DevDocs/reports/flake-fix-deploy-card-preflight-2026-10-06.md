# flake-fix deploy card — preflight (2026-10-06)

Card: `prompts/2026-10-06/11-deploy-flake-fix-card.md`. Read-only; every command run in this session.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --verify f520debb^{commit}` | `f520debb54bc4e38d0dc3fef5f25d4edc59f5b08` | OK |
| 2 | `git log --oneline -1 ops/flake-fix-1006` | `f520debb fix(flake-fix): migrated retries the open too and closes a failed attempt when rollback raises (check H2 H3)` | OK |
| 3 | `tail -n 3` of `reports/flake-fix-check-2026-10-06.md` (last non-blank line) | `CHECK DONE · job: flake-fix · pass: 2 · tip: f520debb · … · held unfixed: 0 · … · ready: YES · …` | OK |
| 4 | `git log -1 --format=%h -- <check report>` | `7f18ca5f` | OK |
| 5 | `rev-parse --verify deploy/deploy-flake-fix-1006` | `fatal: Needed a single revision` (exit 128) | OK |
| 6 | `rev-parse --verify deploy-2026-10-06-flake-fix` | `fatal: Needed a single revision` (exit 128) | OK |
| 7 | `ls /Users/cobalt/cobalt-wt/deploy-flake-fix-1006` | `No such file or directory` | OK |
| 8 | `ls <REPORT path> deploy-deploy-flake-fix-1006.md` | `No such file or directory` | OK |
| 9 | `grep -n "^\| R326 " reports/cto-2026-10-03.md` | line 332: `HIS RULING: A on all three — D5 ships at c96b5118 …` · `HIS RULING · APPROVED` | OK |
| 10 | `grep -n "^\| R412 " reports/cto-2026-10-05.md` | line 109: `HIS RULING: drop pre-merge (d2) …` · `APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a)` | OK |
| 11 | `git log -1 --format=%h --` both cto files; `git diff --stat --` both | `6ac85389` (10-03), `1f4a8598` (10-05); diff empty | OK |
| 12 | BEFORE on main: `grep -c -F` "migration retry" / "conn = None" / "def test_the_migrated_fixture" (prefix of all 5 test names) in `test_drc_store.py`; "flake-fix" in `drc/store.md` | `0` / `0` / `0` / `0` (card: before 0 for all 8 markers) | OK |
| 13 | AFTER via `git show f520debb:tests/cobalt/test_drc_store.py` and `…:store.md` (read, counted by line; `git grep` is not allowed on this seat) | "migration retry": 8 lines (1 print + 2 + 3 + 1 + 1 asserts); `conn = None`: 1; each of the 5 `def test_the_migrated_fixture_…` names: 1; store.md "flake-fix": 2 (the two dated headings). Card: 8, 1, 1×5, 2 | OK |
| 14 | smoke reads (F1, H2, H3 `def` names) | same strings as check 13: 1 each at `f520debb` (≥1, exit 0 on grep) | OK |
| 15 | `git diff --stat main...f520debb` | `store.md` 5+, `flake-fix-build-2026-10-06.md` 223+, `tests/cobalt/test_drc_store.py` 159 · `3 files changed, 383 insertions(+), 4 deletions(-)` — SHIPS row lists exactly these 3, 383/4 | OK |
| 16 | RESTARTS homes (K10) | no `src/`, `ops/desk/`, `conftest.py` or migration path in the diff; test = no resident, two docs = DOCS; check line `RESTARTS: none` | OK |
| 17 | `grep -c -F "«FILL"` on the card | `0` | OK |
| 18 | shape vs `CARD.md` §Header (l.135) and siblings `64-…d5-card.md`, `09-…next-flow-card.md` | same 11 header keys, `## SHIPS`/`## MARKERS`/`## SMOKE READS`/`## RECORDS`; no `## READ-BACK` needed (`MIGRATIONS: none`) | OK |
| 19 | `SET: none` vs `desk-launch.sh` (l.919 `need … SET`, `field()` l.645: non-empty only), `deploy-step0.sh` l.275 (non-empty), `deploy-card.sh` l.64 (`[A-Za-z0-9-]` one word), `CARD.md` l.26 (one word, stop line), `DEPLOY-HUB.md` l.180 (`set: <SET>`) | `none` is non-empty, one word, in the character set: no script rejects it. Siblings name the set (`workflow2`, `s3`); `none` reads `set: none` in the stop line | OK |
| 20 | `git diff --stat -- <card>`; `git log -1 --format=%h -- <card>` | diff empty; `04b89743` | OK |

## ISSUES

None. (Note, not a fail: siblings use a feature word for `SET`; `none` passes every script. The desk may prefer `flake-fix`.)

PREFLIGHT DONE · card: flake-fix-deploy-11 · checks: 20 · fails: 0 · ready: YES
