# Card 11b — preflight r2 (2026-10-03)

Card: `prompts/2026-10-03/11b-dev-rebuild-port-card.md` · BASE `5ff16b1f` · read-only; every command was run by this seat.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --verify 5ff16b1f^{commit}` | `5ff16b1fcd8dc57249fad9633f2f9a53cea34f91` | OK |
| 1 | `git merge-base --is-ancestor 5ff16b1f ops/adoption-port-1003` | exit 0, no output. The branch tip is `bd19a0b3 docs(adoption-port): build report — 5ff16b1f`, one docs commit past BASE (`log 5ff16b1f..ops/adoption-port-1003`). | OK |
| 1 | `rev-parse --verify` of `6ae3f133`, `07cc965f`, `1df251b9`, `05c8b7fa` | `6ae3f13347b7…`, `07cc965f0714…`, `1df251b97f3c…`, `05c8b7faff48…`. All resolve. | OK |
| 1 | `merge-base --is-ancestor 1df251b9 05c8b7fa` (card: `13` built on `11`'s tip) | exit 0. `log 1df251b9..05c8b7fa` is 7 commits, `dd60df2b` … `05c8b7fa`. | OK |
| 1 | `merge-base 1df251b9 5ff16b1f` | `6ae3f133…`, the same base as `11`'s. | OK |
| 2 | `rev-parse --verify ops/dev-rebuild-port-1003` | `fatal: Needed a single revision` (exit 128), so the branch does not exist | OK |
| 2 | `ls /Users/cobalt/cobalt-wt/` | 83 entries; no `dev-rebuild-port-1003`. Only `dev-rebuild-1002`, `devdb-rebuild-1002` and `slot-guard-1002` are near it. | OK |
| 3 | `diff --name-only 6ae3f133 07cc965f` (source `11`) | `cli.md`, `dev_rebuild.md`, `reports/dev-rebuild-build-2026-10-02.md`, `src/cobalt/db_migrations/cli.py`, `dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `test_dev_rebuild_db.py` | — |
| 3 | `diff --name-only 6ae3f133 5ff16b1f` (BASE since `11`'s base), the files that matter | `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/conftest.py`, plus about 250 other docs, ops, configs and tests paths that no source touches | — |
| 3 | `11` ∩ BASE | `cli.md`, `cli.py`. Both have a hand-merge in P1. | OK |
| 3 | `diff --name-only 1df251b9 05c8b7fa` (source `13`) | `cli.md`, `dev_rebuild.md`, `reports/slot-guard-build-2026-10-02.md`, `cli.py`, `dev_rebuild.py`, `tests/cobalt/conftest.py`, `test_dev_rebuild_cli.py`, `test_dev_rebuild_db.py` | — |
| 3 | `diff --name-only 07cc965f 1df251b9` (`11`'s check fix) | `dev_rebuild.md`, `reports/dev-rebuild-build-2026-10-02.md`, `dev_rebuild.py`, `test_dev_rebuild_db.py` | — |
| 3 | `13` ∩ BASE (truly BASE's: the `6ae3f133..5ff16b1f` set) | `cli.md`, `cli.py`, `conftest.py`. All three are hand-merged in P2. | OK |
| 3 | `13` ∩ `11`'s check fix | `dev_rebuild.md`, `dev_rebuild.py`, `test_dev_rebuild_db.py`. All three are hand-merged in P2. | OK |
| 3 | literal `13` ∩ `diff 1df251b9 5ff16b1f` also lists `tests/cobalt/test_dev_rebuild_cli.py` | The path shows up only because `1df251b9` is not an ancestor of BASE, so that diff replays `11`'s own files. `diff --name-only 6ae3f133 5ff16b1f -- tests/cobalt/test_dev_rebuild_cli.py` is empty and `diff 07cc965f 1df251b9 -- …` is empty, so neither BASE nor `11`'s fix touches it. P2's "hash-proven where neither `11`'s fix nor BASE touched it" covers it, and the file is not settled by P1. | OK (note) |
| 4 | red-first tests: P1 "`11`'s with-DB tests" | `test_dev_rebuild_db.py` at `07cc965f`: `test_d1_*` ×3, `test_d3_*`, `test_check_o1`…`o4`, each with `@requires_db`. The file is in `11`'s files. | OK |
| 4 | red-first tests: P2 "`13`'s guard tests" | `test_s1_slot_report_…` is in `test_dev_rebuild_db.py` at `05c8b7fa` with `@requires_db`. The S2 guard is in `conftest.py` (`pytest_sessionstart`). Both are in `13`'s files. BASE has no `test_dev_rebuild_db.py`. Test count after the merge is 8 + 5 − 4 shared = 9. | OK |
| 5 | cite: "BASE's `cmd_migrate`" and "the TABLES / FINGERPRINT lines" | At BASE `cli.py`: `684:def cmd_migrate`; `378:FINGERPRINT_SQL`, `463:return f"FINGERPRINT cols …`; `437`/`439:return "TABLES none"` / `f"TABLES {some[-1]}"`. The `TABLES` lines are not in `07cc965f`'s `cli.py`. | OK |
| 5 | cite: `11`'s `cmd_dev_rebuild`; `13`'s `SLOT_WARN_AT` | `07cc965f:cli.py:834 def cmd_dev_rebuild`. `05c8b7fa:cli.py:148 SLOT_WARN_AT = 1200` and `866 def cmd_dev_rebuild`. | OK |
| 5 | cite: BASE's `01` guard lines in `conftest.py`; `13`'s slot-guard lines | BASE `conftest.py` has `require_offline_skip`, `offline_skip_guard`, `_guarded_reach` (lock-relief G1/P1). `05c8b7fa` has `pytest_sessionstart`, `_SLOTS_WARN`, `pytest_terminal_summary`. Both sides are present. | OK |
| 5 | cite: `11`'s O1–O5 | `test_check_o1`…`o4` are in `07cc965f`; `07cc965f`'s commit message names O1 O2 O3 O4 O5. | OK |
| 5 | cite: ruled sentence copied from a decisions file | None. The card quotes no ruled sentence. | OK |
| 6 | `ls` of the five `## READ` files | `11-dev-rebuild-card.md`, `13-slot-guard-card.md`, `13b-slot-guard-port-card.md`, `dev-rebuild-check-2026-10-02.md`, `slot-guard-check-2026-10-02.md` all exist. `grep -n "^## "`: `dev-rebuild-check` has `190:## FIXES`; `slot-guard-check` has `3:## §0 Headline`. | OK |
| 7 | `grep -n "^\| R(47\|157) " reports/cto-2026-10-02.md` | `54:\| R47 \| 07:57 ET \| HIS RULING (… script program by Anthropic seats only, no outside house …) \| HIS RULING · APPROVED \|`; `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included … \| HIS RULING · APPROVED \|` | OK |
| 8 | `grep -n` on `restarts.py` (identical at `bd19a0b3` and BASE; `diff --stat` is empty) | `228: output.append(Classification(path, item.change, "DOCS", ()))`; `246: rule = "test/documentation; no resident"`. Both cites hold. | OK |
| 8 | the card's non-docs paths and their homes | `src/cobalt/db_migrations/cli.py` and `dev_rebuild.py` → the `com.cobalt.radar` class. `dev-rebuild-build-2026-10-02.md` `## RESTARTS` at `07cc965f`: `132:src/cobalt/db_migrations/cli.py M static import reach com.cobalt.radar`, `133:…dev_rebuild.py A static import reach com.cobalt.radar`, `136:RESTARTS: com.cobalt.radar`. `tests/cobalt/*` (including `conftest.py`) → `:246`. `docs/**` → `:228`. Every shipped non-docs path has a home. | OK |
| 9 | ships a new with-DB test or migration? | Yes: `tests/cobalt/test_dev_rebuild_db.py`, which BASE does not have, so it is a new with-DB test file. No migration. Its tests carry `requires_db` (skipif), so BASE's `--db-only` pass 1 keeps them. D3 reads `aset_sizings` at `0013`, so they run in pass 1 as written at 0013 and `TREE STATE: unchanged` holds. The card has no `DB:` line, which is correct because it ships under `src/` and `tests/cobalt/`. | OK |
| 9 | `HOUSE B` filled; `grep -c -F "«FILL"` on the card | `HOUSE B: as needed`; count `0` | OK |

## ISSUES

None. One note, not a fail: the literal `13` ∩ `diff 1df251b9 5ff16b1f` set includes `test_dev_rebuild_cli.py`, but that is an artifact of `1df251b9` not being an ancestor of BASE. The file is touched by neither BASE nor `11`'s fix, and P2 hash-proves it from `05c8b7fa`.

PREFLIGHT DONE · card: 11b · checks: 9 · fails: 0 · ready: YES
