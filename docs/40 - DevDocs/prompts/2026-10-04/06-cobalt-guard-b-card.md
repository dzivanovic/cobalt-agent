JOB: cobalt-guard-b
LADDER: OFF-LADDER — cto-2026-10-03.md R248
BRANCH: ops/cobalt-guard-b-1004
WORKTREE: cobalt-guard-b-1004
BASE: «FILL: main after set 3 DEPLOYED, 8 hex»
TIP:
REPORT: /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
DB: none
RULINGS: «FILL: 2026-10-03 R33 and the desk row R248 (cto-2026-10-03.md), as <date> R<n> pairs»

## ROWS

| row | what | red first | files |
|---|---|---|---|
| B1 | G3 READERS: `sort`, `cut`, `uniq`, `awk` join `cat grep sed head tail less` in `ENV_READERS` (`ops/desk/bare-guard.py:74` at `a2e19ceb`; `READ_FILTERS` is line 73). Any of them with an operand that `is_env` matches → deny with G3's route (`ROUTE["G3"]`), in a single command and in a pipe segment. Backed by the check's O5 (`reports/cobalt-guard-check-2026-10-04.md` `## OWN FINDINGS` O5, `## RUNS` O5 `REJECTED`, `## OPEN`) | `test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied`, restored from the check report O5 as written (5 ids: `sort /x/wt/job/.env`, `cut -c1- /x/wt/job/.env`, `uniq /x/wt/job/.env`, `awk 1 /x/wt/job/.env`, `grep -n X f \| sort /x/wt/job/.env`; `assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)`). RED on `BASE`: each id fails `assert 0 == 2`. GREEN after. Mutation (K25 1): take the four verbs back out of `ENV_READERS` → the 5 ids red again | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |
| B2 | G1 READ-ONLY MEANS NO WRITE AND NO PROGRAM: in a pipe segment (`pipe_problems`, `bare-guard.py:389`) deny `sort` with `-o`, `--output`, `--output=*` or `--compress-program*`, and `uniq` with a second non-option operand (`uniq <in> <out>`; the first operand is the input, a second one is the output; the value of `-f`, `-s`, `-w` or their long forms is not an operand). The deny is G1's: the resend sentence (`BLOCK`, `bare-guard.py:44`) naming the problem, as `sed -i` and G11 do. Backed by the check's O4 (`cobalt-guard-check-2026-10-04.md` `## OWN FINDINGS` O4, `## RUNS` O4 `REJECTED — G1's letter`, `## OPEN`) | `test_check_guard_o4_a_filter_that_writes_or_runs_is_denied`, restored from the check report O4 as written (4 ids: `grep X f \| sort -o out`, `grep X f \| sort --output=out`, `grep X f \| sort --compress-program=sh`, `grep X f \| uniq - out`; `done.returncode == 2`). RED on `BASE`: each id fails `assert 0 == 2`. Controls, one new test `test_b2_a_read_only_sort_and_uniq_stay_allowed`: `grep X f \| sort -u` and `grep X f \| uniq -c` → `assert_allowed`; they pass on `BASE` and stay green. Mutation (K25 1): drop the `sort` check → ids 1–3 red; drop the `uniq` check → id 4 red; make the `uniq` check deny any operand → the `uniq -c` control red | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |
| B3 | THE AWK -f GAP: a pipe segment whose first word is `awk` with `-f` or `--file` (a program from a file G11 cannot read, `awk_writes`, `bare-guard.py:372`) → deny with the resend sentence naming it, as `sed -f` is (`sed_problem`: "`sed -f`, a script the guard cannot read"). Backed by the build's `## DECISIONS` 1 (`cobalt-guard-build-2026-10-04.md`) and desk row R241 (`cto-2026-10-03.md`) | `test_b3_an_awk_program_from_a_file_in_a_pipe_is_denied`: `grep X f \| awk -f p.awk` → `returncode == 2` (RED on `BASE`: `assert 0 == 2`, allowed because `awk_writes` skips the `-f` value). Control in the same file `test_b3_an_awk_program_in_the_command_stays_allowed`: `grep X f \| awk '{print $1}'` → `assert_allowed`; passes on `BASE`, stays green. Mutation (K25 1): remove the `-f` deny → the first test red | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |

## NOT IN THIS JOB
- Any hub text, launch line or allow string. The four read strings (`Bash(cut *)`, `Bash(sort *)`, `Bash(uniq *)`, `Bash(awk *)`) are his and are not put on any line by this job; they wait for this card to ship, then for the next hub-text card.
- Any file but `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py`. No rule beyond B1–B3: G1–G11 stand as built at `a2e19ceb`; the remaining reads the check recorded (`$VAR` in a `.env` path, `grep -r` of a folder holding `.env`; `cobalt-guard-check-2026-10-04.md` `## RECORDS`) stay open.
- A lone `awk -f`, `sort -o` or `uniq <in> <out>` that is ONE command (no pipe): G1 allows one command, as built; not changed here.
- A rule that needs judgment.

## READ
- `ops/desk/bare-guard.py` at `BASE` whole: `READ_FILTERS` and `ENV_READERS` (73–74), `BLOCK` (44), `awk_writes` (372), `pipe_problems` (389), `g3_bash` (543), `sed_problem` (the shape of a deny that names its option). `tests/ops/test_bare_guard.py`: `make_seat`, `run`, `call`, `assert_denied`, `assert_allowed`, `G3_ROUTE`, the G11 tests (`test_g11_…`) and the G3 tests (`test_g3_…`) as the pattern.
- `reports/cobalt-guard-check-2026-10-04.md`: O4, O5 (the tests to restore), `## DECISIONS` 1 and 2. The build report `## DECISIONS` 1.

## RECORDS
- His 2026-10-03 R33 ("allow read-only pipes") is carried in its read-only intent: B1–B3 narrow its wording, so that a pipe that writes a file, runs a program or reads a program from a file is not read-only. They sit on his veto list (desk rows R241, R247, R248, `cto-2026-10-03.md`). The desk read this line from the check report O4, O5 and the build report `## DECISIONS` 1 at 15:56 ET, 2026-10-04.
- RESTARTS class home (K10), each path as `uv run cobalt jobs restarts a8d8a848..HEAD` classified it in the check of `cobalt-guard` (`cobalt-guard-check-2026-10-04.md` `## Suites`, read 15:56 ET 2026-10-04): `ops/desk/bare-guard.py` → `M operator script; no Cobalt reader -`; `tests/ops/test_bare_guard.py` → `M test/documentation; no resident -`; the build report under `docs/` → `A DOCS -`. Expected `RESTARTS: none`; the build runs the table whole (L42) and quotes it.
- `cobalt-guard` ships at `a2e19ceb` (card 10 judged ships, desk row R248); this job's `BASE` is main after set 3 is DEPLOYED.
- The four read strings stay off every session line until this card ships (desk rows R241, R247, R248).
