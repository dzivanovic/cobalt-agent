# devfix-sizings preflight — card 99 (read-only)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card 99 header | JOB, LADDER, BRANCH, WORKTREE, BASE, REPORT, RULINGS, TABLE, PROOF TEST all present | OK |
| 2 | TABLE vs `desk-launch.sh:1005-1013` | `user.aset_sizings`: `user.` prefix, name `aset_sizings` is `[a-z0-9_]` | OK |
| 3 | PROOF TEST vs `:1014-1030` | `tests/cobalt/test_dev_rebuild_db.py::test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings`: file `.py`, name chars in `[A-Za-z0-9_:.]` | OK |
| 4 | `grep -n` in the test file | `237:def test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings(conn):` · body `:243-249` calls `slot_report(conn)`, selects `("user", "aset_sizings")`, compares to `SL` (`:229-233`, reads `"user".aset_sizings`) | OK |
| 5 | REPORT vs `:1031-1039` · `ls` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-aset-sizings-2026-10-07.md` matches `$REPORTS/devfix-<…>.md`; `ls` → No such file | OK |
| 6 | `git merge-base --is-ancestor 73cbf7a1 main` | exit 0; `73cbf7a1` is 8 hex | OK |
| 7 | BRANCH `ops/devfix-aset-sizings-1007`, WORKTREE `devfix-aset-sizings-1007` vs `:721-722` | chars in `[A-Za-z0-9._/-]`, no leading `-`, no `..` | OK |
| 8 | `ls /Users/cobalt/cobalt-wt/devfix-aset-sizings-1007` | No such file or directory | OK |
| 9 | `grep -n -E "«FIL[L]\|## ROWS"` on the card | no match | OK |
| 10 | `grep -n "^\| R625 "` in `reports/cto-2026-10-07.md` | `19:\| R625 \| 10:15 ET \| HIS RULING (words: … R625): a radar card's header row and title are green for long, red for short; … \| HIS RULING · APPROVED \|` | OK |
| 11 | `git status --short` on card, draft report, `cto-2026-10-07.md`; `git log --oneline -1` on card and draft | status empty (committed, unchanged); both last commit `58db5b54` | OK |
| 12 | card `## RECORDS` vs `deploy-radar-direction-color-1007.md` | 1538 of 1600 ↔ `:5`, `:86`, `:124`; 1534 before, 1534 → 1538 ↔ `:93-95`, `:124` | OK |
| 13 | `grep dev-rebuild` in `src/cobalt/` | subcommand `"dev-rebuild"` at `db_migrations/cli.py:1110`, `set_defaults(func=cmd_dev_rebuild)` at `:1128`; `dev_rebuild.py:815` prints `fix: cobalt db dev-rebuild {s}.{t} (dev only)` | OK |
| 14 | dev-only: `cli.py:1002-1006` | `if mode != env.DEV: _refuse("… dev-rebuild runs on cobalt_dev only — nothing opened.")` | OK |
| 15 | `DEVFIX-HUB.md` steps | S1 takes the lock (`:36`), S3 `dev-rebuild <TABLE> --dry-run` (`:47`), S4 same without `--dry-run` (`:48`), S6 runs `<PROOF TEST>` (`:50`), S8 releases the lock (`:52`) | OK |

## ISSUES
- NOTE: card `BASE 73cbf7a1` is behind `main` (`58db5b54`). It is an ancestor, so `desk-launch.sh` accepts it. The card and draft commits sit above BASE; the hub's PREFLIGHT `git log --oneline -1` → `<BASE>` is read in the new worktree, which is cut from BASE.
- NOTE: the draft's decision 1 is the desk's kept default; not failed (per prompt).

PREFLIGHT DONE · card: devfix-aset-sizings-99 · checks: 15 · fails: 0 · ready: YES
