# Card 11b — preflight 2026-10-03

Card: `prompts/2026-10-03/11b-dev-rebuild-port-card.md`. BASE `5ff16b1f`. Read-only; every output below was run in this session. `G` = `git -C /Users/cobalt/cobalt`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `G rev-parse --verify 5ff16b1f^{commit}` | `5ff16b1fcd8dc57249fad9633f2f9a53cea34f91` | OK |
| 1b | `G merge-base --is-ancestor 5ff16b1f ops/adoption-port-1003` | exit 0, no output | OK |
| 1c | `rev-parse --verify <x>^{commit}` for `6ae3f133`, `07cc965f`, `1df251b9`, `05c8b7fa` | `6ae3f13347b7…`, `07cc965f0714…`, `1df251b97f3c…`, `05c8b7faff48…` | OK |
| 1d | `merge-base --is-ancestor 6ae3f133 5ff16b1f` / `… 1df251b9 5ff16b1f` | exit 0 / exit 1: `1df251b9` is NOT an ancestor of BASE (11's tip sits on a different line) | OK (note for 3b) |
| 2a | `G rev-parse --verify ops/dev-rebuild-port-1003` | `fatal: Needed a single revision` | OK |
| 2b | `ls /Users/cobalt/cobalt-wt/` | no `dev-rebuild-port-1003` (has `dev-rebuild-1002`, `devdb-rebuild-1002`, `slot-guard-1002`) | OK |
| 3a | source `11`: `diff --name-only 6ae3f133 07cc965f` | `cli.md`, `dev_rebuild.md`, `reports/dev-rebuild-build-2026-10-02.md`, `src/cobalt/db_migrations/cli.py`, `…/dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `…/test_dev_rebuild_db.py` (7) | – |
| 3b | BASE since `11`'s base: `diff --name-only 6ae3f133 5ff16b1f` (170 paths) | includes `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/conftest.py` (full list in the diff; it has no `dev_rebuild*` path) | – |
| 3c | intersection, `11` ∩ BASE | `db_migrations/cli.md`, `db_migrations/cli.py`. P1 settles `cli.py` by Edit. `cli.md` has no hand-merge row: P1 writes "every file … from `git show 07cc965f:<path>`" and so overwrites 03d's `cli.md` change (`diff --stat 6ae3f133 5ff16b1f`: `cli.md | 3 +`). | **FAIL** (`cli.md`) |
| 3d | source `13`: `diff --name-only 1df251b9 05c8b7fa` | `cli.md`, `dev_rebuild.md`, `reports/slot-guard-build-2026-10-02.md`, `cli.py`, `dev_rebuild.py`, `tests/cobalt/conftest.py`, `test_dev_rebuild_cli.py`, `test_dev_rebuild_db.py` (8) | – |
| 3e | BASE since `13`'s true base (`1df251b9` is not an ancestor; merge-base is `6ae3f133`, so the list in 3b) | `cli.md`, `cli.py`, `tests/cobalt/conftest.py` changed by BASE (`--stat 6ae3f133 5ff16b1f`: `cli.md 3+`, `cli.py 115+/-`, `conftest.py 109+`) | – |
| 3f | intersection, `13` ∩ BASE | `cli.md`, `cli.py`, `tests/cobalt/conftest.py`. P2 settles only `test_dev_rebuild_db.py`, `dev_rebuild.md`, `dev_rebuild.py`. `conftest.py` has no row (P2 "from `git show 05c8b7fa:<path>`" would drop 03d's 109 added lines). `cli.py` and `cli.md` are written from `05c8b7fa` in P2, which would drop P1's settled `cli.py` and 03d's lines. | **FAIL** (`conftest.py`, `cli.py` in P2, `cli.md` in P2) |
| 4 | red-first tests: P1 "`11`'s with-DB tests", P2 "`13`'s guard tests"; `G grep -n -E "^def test_" 05c8b7fa -- tests/cobalt/test_dev_rebuild_db.py` | 5 tests at `:95 :127 :142 :155 :184`; file is in `11`'s and `13`'s files. No row names a test by name. | OK (rows name no test; file is in the ported set) |
| 5a | `G grep -n -F "cmd_dev_rebuild" 07cc965f -- src/cobalt/db_migrations/cli.py` | `:834 def cmd_dev_rebuild`, `:985`, `:1000` | OK |
| 5b | `G grep -n -F "FINGERPRINT" 5ff16b1f -- …/cli.py` | `:64 :375 :378 :449 :462 :463 :958` | OK |
| 5c | `G grep -n -F "LEVEL" 5ff16b1f -- src/cobalt tests/cobalt/test_migrate_level.py` | no hit in `db_migrations/cli.py`; `test_migrate_level.py:12` says "no `LEVEL` word" is printed | **FAIL** (`LEVEL` line, "03d's LEVEL/FINGERPRINT lines") |
| 5d | `G diff 5ff16b1f 07cc965f --stat -- …/cli.py` (the card's "quote `git diff <BASE> -- cli.py` showing only `11`'s lines") | `177 insertions(+), 139 deletions(-)` from a plain `07cc965f` file; the "only `11`'s lines" proof is for the build to produce | OK (not a cite) |
| 5e | O1–O5 in `reports/dev-rebuild-check-2026-10-02.md` | `:52 FINDING O1` … `:129 FINDING O5`; fix at `68dddee3`/`07cc965f` | OK |
| 6 | `ls` the five `## READ` files | all five exist (`11-dev-rebuild-card.md`, `13-slot-guard-card.md`, `13b-slot-guard-port-card.md`, `dev-rebuild-check-2026-10-02.md`, `slot-guard-check-2026-10-02.md`) | OK |
| 7a | `grep -n "^| R47 \|^| R157 " reports/cto-2026-10-02.md` | `54: \| R47 \| … HIS RULING … \| HIS RULING · APPROVED \|` | OK |
| 7b | same, R157 | `164: \| R157 \| … HIS RULING (B) … \| HIS RULING · APPROVED \|` | OK |
| 8a | `G grep -n -F "test/documentation; no resident" 5ff16b1f -- …/restarts.py` (card cites `restarts.py:239`) | `:246` | **FAIL** (`:239` does not hold; it is `:246`) |
| 8b | `G grep -n -F '"DOCS"' 5ff16b1f -- …/restarts.py` (card cites `:219`) | `:228` | **FAIL** (`:219` does not hold; it is `:228`) |
| 8c | homes: `src/cobalt/db_migrations/*.py` → `11`'s `## RESTARTS` (`RESTARTS: com.cobalt.radar`, `dev-rebuild-build-2026-10-02.md:136`, line 7 and 210 agree); `tests/cobalt/*` → test/documentation; `docs/**` → DOCS | every non-docs path has a home (`cli.py`, `dev_rebuild.py`, `tests/cobalt/*`) | OK |
| 9a | `G cat-file -e 5ff16b1f:tests/cobalt/test_dev_rebuild_db.py` and `6ae3f133:…` | both `fatal: path … does not exist`: the card ships a NEW with-DB test file (5 tests at `05c8b7fa`) that runs under the W/E2 lock take, not shown to run in pass 1 as written at 0013; `TREE STATE: unchanged` is unproven | **FAIL** (`TREE STATE`) |
| 9b | `HOUSE B` | `as needed` (filled); `HOUSE A: none — overruled 2026-10-02 R47` | OK |
| 9c | `grep -c -F "«FILL"` on the card | `0` | OK |

## ISSUES

- FAIL 3c: shared path `docs/40 - DevDocs/cobalt/db_migrations/cli.md` (11 and BASE) has no hand-merge row in P1; writing it from `07cc965f` drops 03d's change.
- FAIL 3f: shared path `tests/cobalt/conftest.py` (13 and BASE, 109 added lines at BASE) has no hand-merge row in P2.
- FAIL 3f: `cli.py` and `cli.md` are 13 paths too and are shared with BASE and P1; P2 names neither as settled, so a write from `05c8b7fa` overwrites P1's merge.
- FAIL 5c: "`03d`'s LEVEL/FINGERPRINT lines": no `LEVEL` line exists in `cli.py` at BASE (the line prints no `LEVEL` word); name the real line.
- FAIL 8a: `restarts.py:239` should be `:246` at BASE.
- FAIL 8b: `restarts.py:219` should be `:228` at BASE.
- FAIL 9a: the card ships a new with-DB test file (`tests/cobalt/test_dev_rebuild_db.py`, absent at BASE); `TREE STATE: unchanged` does not state it runs in pass 1 as written at 0013.

PREFLIGHT DONE · card: 11b · checks: 28 · fails: 7 · ready: NO
