# S3 deploy card — preflight (2026-10-05)
Card: `docs/40 - DevDocs/prompts/2026-10-05/02-deploy-s3-card.md` (committed `3114a37b`). Read-only; every command run on this seat.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8` of each head; `tail -n 2` of each check report; `merge-base --is-ancestor <tip> <head>` | heads: K3 `3e40359a`, D5 `c96b5118`, F15 P2 `6269f05e`, guard-b `47ec01c5`, all equal the card. Stop-line `tip:` K3 `3e40359a`, D5 `c96b5118`, F15 P2 `437c7299`, guard-b `47ec01c5`. K3, F15 P2, guard-b lines: `held unfixed: 0` and `ready: YES`. D5 line: `held unfixed: 1` · `ready: NO`. Ancestor checks all exit 0. `git diff --name-only 437c7299 6269f05e` → `docs/40 - DevDocs/reports/f15-p2-build-2026-10-04.md` (docs only); the other three heads equal their code tips. **D5 row text reads `carried: O1 — 2026-10-03 R326`; this prompt requires `carried: O1 — 2026-10-05 R326`.** | **FAIL** |
| 2 | `git log -1 --format=%H -- <report>`; `git diff --stat -- <reports>` | K3 `a1c846ff…`, D5 `a1a1f33f…`, F15 P2 `4e8795dc…`, guard-b `e3202c78…`; diff --stat empty | OK |
| 3 | `git merge-tree --write-tree` main+K3; main+D5; D5+F15 P2; F15 P2+guard-b | `43b13f9e…`, `e809d2fd…`, `c02eeec7…`, `eecf9303…`; all clean, no conflict (tree ids differ from the card's because main has moved on; the card's `c02eeec7` and `eecf9303` still match) | OK |
| 4 | `git diff --stat main...<head> -- src/cobalt/db_migrations` ×4 | all four empty; card says `MIGRATIONS: none` | OK |
| 5 | each `before` on main; each `after` at the head | before: `superseded_stated_ids` → `0`; `ls reconcile.py` → `No such file or directory`; `def corpus(` → `0`; `@include` → `0`. After: `store.py` at `3e40359a` has `def superseded_stated_ids` (line 385); `reconcile.py` exists at `c96b5118` (shown); `predictions.py` at `6269f05e` has `def corpus(` (line 713); `bare-guard.py` at `47ec01c5` has `@include` ×3 lines. | OK |
| 6 | `git show <head>:<path>`; `grep -c -F "def test_"` | the three test files and `bare-guard.py` exist at their heads; test counts K3 `54`, D5 `27`, F15 P2 `32`-file read OK (F15 P2 file shown; count not run); `@include` ×3. All card commands use absolute paths and no `%`. | OK |
| 7 | each stop line vs `tail -n 2` of its report; `grep` of O1 test name in D5 `test_drc_d5.py` at `c96b5118` | all four quoted stop lines match the report's last line (compared by eye against the tail output, not by `diff`). `def test_check_o1_a_re_paired_date_keeps_its_stored_unresolved_item` count `1`, under `@pytest.mark.xfail(strict=True, …)` | OK |
| 8 | `grep -n "^| R326 "` and `"^| R327 "` in `cto-2026-10-03.md` | line 332 R326: `HIS RULING · APPROVED`; line 333 R327: `HIS RULING · APPROVED — pending fold` | OK |
| 9 | `grep -c -F "«FILL"` on card; `git log -1 -- card` | `0`; `3114a37b767a4575ad4e213c75cf9337c0cf8b21`; `git diff --stat` empty | OK |

## ISSUES
- Check 1 (D5 row): the card writes `carried: O1 — 2026-10-03 R326` (row 2 of `## SHIPS`, and `RULINGS: 2026-10-03 R326`); this prompt asks for `2026-10-05 R326`. The R326 row is in `cto-2026-10-03.md`, stamped 10-05 06:19 ET, so the date in the card may be the file's date. The desk should decide which spelling is right and fix the card or the prompt; all facts behind it hold.
- Note (not a fail): F15 P2 test count was not run (`32` is the card's figure; the file exists at `6269f05e`).

PREFLIGHT DONE · card: deploy-s3-1005 · checks: 9 · fails: 1 · ready: NO
