# worktree-salvage preflight — 2026-10-07 (card 83)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card header `:1-11` vs `CARD.md` keys | JOB, LADDER, BRANCH `ops/worktree-salvage-1007`, WORKTREE `worktree-salvage-1007`, BASE `«FILL: main HEAD at launch, 8 hex»`, TIP/CHECK REPORT/HOUSE B empty, RULINGS `2026-10-07 R613`, `DB: none` | OK |
| 2 | `grep -c "FILL"` on the card | `1` (the BASE token only) | OK |
| 3 | `ls /Users/cobalt/cobalt/.git/refs/heads/ops`; `ls /Users/cobalt/cobalt-wt` | no `worktree-salvage-1007` in either (branch and worktree are new) | OK |
| 4 | `grep -n "R613" reports/cto-2026-10-07.md` | `:8` `R613 \| 06:37 ET \| HIS RULING (words: cto-2026-10-07-words.md R613) … \| APPROVED — pending fold`; words file `:3` `## R613` holds his order | OK |
| 5 | `git log --oneline -2 -- cto-2026-10-07.md cto-2026-10-07-words.md`; `git diff --stat HEAD -- …` | `375e102c`, `f77f1bc3`; diff empty (committed, no local change) | OK |
| 6 | `git log --oneline -3 -- card, draft`; `git diff --stat HEAD -- prompts/2026-10-07 …draft` | both in `f77f1bc3`; diff empty | OK |
| 7 | `git diff --stat 2ac0e604 HEAD -- ops/desk/job-clean.sh tests/ops/test_gate_clean.py src/cobalt/jobs/restarts.py` | empty: every cite proven at `2ac0e604` still holds at HEAD | OK |
| 8 | Read `job-clean.sh` `:24` / `:24-26` / `:13` / `:11` | `[ "$#" -eq 1 ] \|\| refuse "usage: …"` / `card=$1` … / `export LC_ALL=C` / `Roots: COBALT_REPO_ROOT …` | OK |
| 9 | Read `job-clean.sh` `:41-47` | pattern `""\|.*\|*[!A-Za-z0-9._-]*` `:41-42`; `agy-trial` `:44`; symlink `:46`; `-d` `:47` | OK |
| 10 | Read `job-clean.sh` `:55` `:56` `:57` `:62-63` `:64` | merge-base `--is-ancestor`; `status --porcelain` empty; `.env` test; `RUN: … branch -d`; last line `job-clean: %s and %s removed` | OK |
| 11 | Read `job-clean.sh` `:1-11` header | 11 lines; says "(never forced)" `:9-10` | OK |
| 12 | Read `test_gate_clean.py` `:45-110`, `:63-67`, `:57`, `:253`, `:285`, `:315` | `Desk` `:45-110`; `x-job` on `ops/x-job` `:63-67`; `.gitignore` = `.env` `:57`; merge `:253`; `CONSTRUCTED_ENV` `:285`; last test ends `:315` | OK |
| 13 | Count the card's "eight existing `job-clean.sh` tests (`:251-315`)" | 7 test functions (`:251 :269 :274 :282 :290 :298 :310`); the parametrized `:290` runs 6 cases → 12 collected. Neither is 8. File has 22 `def test_` | FAIL |
| 14 | `restarts.py` grep | `:38` `OPS_DESK_PREFIX = "ops/desk/"`; `:230-232` `operator script; no Cobalt reader`; `:246` `test/documentation; no resident` | OK |
| 15 | `STANDING-LIST.md:36` | CLASS (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` — no allow change | OK |
| 16 | `cto-desk-checklist.md:59` | W8 R613 clause quoted as the card says ("card owed, no `--force`; until it ships the desk reports a broken tree and removes nothing") | OK |
| 17 | RED on BASE, W1 `salvage x-job x` | BASE `:24` prints `usage: job-clean.sh "<job card>"`; stderr lacks `job-clean.sh salvage <worktree-name>` → red for the stated reason | OK |
| 18 | RED on BASE, W2 W3 W4 W5 | every two-argument call exits 1 at `:24`, stdout empty, tree stands → each stated assertion (INSPECT lines, SALVAGED, last line, tree gone) fails | OK |
| 19 | Controls: W1 names, W3 `.env`, W5 CLEAN UNMERGED, W7 | on BASE each is refused at `:24` (exit 1, `REFUSED`, tree and branch stand, `.env` intact, no `wip/`); W7 `grep` of the five forms on BASE file → no output | OK |
| 20 | `grep -c -F "job-clean.sh salvage <worktree-name>" ops/desk/job-clean.sh` | `0` on BASE (W6 red) | OK |
| 21 | Rows W1-W7 vs R613 | inspect, report, wip branch for unsaved work, remove, never forced, nothing waits on him; no row beyond that | OK |
| 22 | `grep -n -e "--force" -e "branch -D" -e " -f" -e "reset --hard" -e "clean -"` on the card | hits only in prose that forbids them (`:15`, `:24`, `:25`, `:48`); no script text with a force form | OK |
| 23 | New commands/args vs the draft's decisions (R411, R412) | `switch -c`, `add -A`, `commit -q -m`, `merge-base`, `rev-list --count`, `rev-parse --git-path`, `check-ref-format`, `worktree remove`, `branch -d`: all named by W1-W5 and decisions 1-6; no flag or allow change | OK |
| 24 | RESTARTS homes in `## RECORDS` | card `RESTARTS` paragraph cites all three classes (script, test, report DOCS); `## RECORDS` cites the draft's RECORDS and the pre-commit hook; class homes `restarts.py:230-232`, `:245-246` proven in #14 | OK |

## ISSUES
- FAIL (#13): the card says "the eight existing `job-clean.sh` tests (`:251-315`)"; the file has 7 functions, 12 collected tests. Fix the count in W1 (and the draft's RECORDS "8 tests") before launch.
- NOTE W4: a DETACHED, CLEAN, unmerged tree (the card's own DETACHED test) takes the wip path, but `git commit` on a clean tree exits 1, which W4 turns into `REFUSED: salvage stopped`. State that the `add -A` / `commit` steps run only when `status --porcelain` is non-empty, or the DETACHED test cannot pass.
- NOTE W1: `git worktree list --porcelain` prints `locked <reason>` when a reason was given; say the match is `^locked( |$)`, not the bare line.
- NOTE W7: `clean -` is a loose substring (prose such as "clean - " in the header would trip it); the builder should keep the header free of it.
- NOTE: main HEAD moved to `375e102c`; BASE is still the desk's fill at launch.

PREFLIGHT DONE · card: worktree-salvage-83 · checks: 24 · fails: 1 · ready: NO
