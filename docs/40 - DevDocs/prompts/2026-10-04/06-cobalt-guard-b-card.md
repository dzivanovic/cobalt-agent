JOB: cobalt-guard-b
LADDER: OFF-LADDER — cto-2026-10-03.md R248
BRANCH: ops/cobalt-guard-b-1004
WORKTREE: cobalt-guard-b-1004
BASE: 979ec797
TIP: 8e68decd
REPORT: /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/cobalt-guard-b-check-2026-10-04-r2.md
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-03 R33

## ROWS

| row | what | red first | files |
|---|---|---|---|
| B1 | G3 READERS: `sort`, `cut`, `uniq`, `awk` join `cat grep sed head tail less` in `ENV_READERS` (`ops/desk/bare-guard.py:74` at `a2e19ceb`; `READ_FILTERS` is line 73). Any of them with an operand that `is_env` matches → deny with G3's route (`ROUTE["G3"]`), in a single command and in a pipe segment. Backed by the check's O5 (`reports/cobalt-guard-check-2026-10-04.md` `## OWN FINDINGS` O5, `## RUNS` O5 `REJECTED`, `## OPEN`) | `test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied`, restored from the check report O5 as written (5 ids: `sort /x/wt/job/.env`, `cut -c1- /x/wt/job/.env`, `uniq /x/wt/job/.env`, `awk 1 /x/wt/job/.env`, `grep -n X f \| sort /x/wt/job/.env`; `assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)`). RED on `BASE`: each id fails `assert 0 == 2`. GREEN after. Mutation (K25 1): take the four verbs back out of `ENV_READERS` → the 5 ids red again | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |
| B2 | G1 read-only means no write and no program. A `sort` command is denied when (a) any short-option word (one leading `-`, not `--`) contains the letter `o`, which covers `-o out`, `-oout` and `-uo out` (sort's key modifiers hold no `o`; an over-deny such as `-t o` is resent as plain, which is acceptable), or (b) any long-option name (the text after `--`, up to `=`) is a prefix of `output`, or begins `com` and is a prefix of `compress-program`. A `uniq` command is denied when it carries a second non-option operand (an operand is a word that is not an option and not the value of an option: the word after `-f`, `-s` or `-w`, and the digits attached in `-f1`, `-s2` or `-w3`, are values, so `uniq -f 1 f` holds one operand and is allowed). Route: the resend sentence | red: `check_guard_o4`'s 4 ids plus `sort -uo out`, `sort -oout`, `sort --out=x`, `sort --compress=sh` each allowed on BASE; controls `grep X f \| sort -u`, `sort -k2,2n f`, `sort --unique f` and `grep X f \| uniq -c` stay allowed | both files |
| B3 | THE AWK -f GAP: a pipe segment whose first word is `awk` with `-f` or `--file` (a program from a file G11 cannot read, `awk_writes`, `bare-guard.py:372`) → deny with the resend sentence naming it, as `sed -f` is (`sed_problem`: "`sed -f`, a script the guard cannot read"). Backed by the build's `## DECISIONS` 1 (`cobalt-guard-build-2026-10-04.md`) and desk row R241 (`cto-2026-10-03.md`) | `test_b3_an_awk_program_from_a_file_in_a_pipe_is_denied`: `grep X f \| awk -f p.awk` → `returncode == 2` (RED on `BASE`: `assert 0 == 2`, allowed because `awk_writes` skips the `-f` value). Control in the same file `test_b3_an_awk_program_in_the_command_stays_allowed`: `grep X f \| awk '{print $1}'` → `assert_allowed`; passes on `BASE`, stays green. Mutation (K25 1): remove the `-f` deny → the first test red | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |
| B4 | B2, B3 and card 10's awk write checks (G11: `system(`, `>`, `\|` in the program) apply to a lone `sort`, `uniq` or `awk` command exactly as to a pipe segment | red: lone `sort -o out f`, `uniq f out`, `awk -f p.awk f` and `awk '{print > "x"}' f` each allowed on BASE; controls lone `sort f` and `awk '{print $1}' f` stay allowed | both files |
| B7 | O2: B2(b)'s long-option test becomes: a long-option name (the text after `--`, up to `=`) is denied when it is a non-empty prefix of `output`, or a prefix of `compress-program` at least two letters long (`--co`, `--com`, …; `--c` alone is ambiguous with `--check` and is refused by sort itself) | red: `sort --co=sh f`, `sort --co sh f` and `sort --compress=sh f` each allowed on 1f2c19a9; controls `sort --check f` and `sort -c f` stay allowed | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |
| B8 | O3: G3's `.env` test also reads option values, for every command in `ENV_READERS`: the text after the first `=` of a `--name=value` word, and the word after `--files0-from` given without `=`, are each tested by `is_env` like an operand; a match → deny with G3's route | red: `sort --files0-from=.env`, `sort --files0-from .env` and `sort --files0-from=/x/wt/job/.env` each allowed on 1f2c19a9; controls `sort --key=2 f` and `grep -n --include=*.py X .` stay allowed | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |

## NOT IN THIS JOB
- Any hub text, launch line or allow string. The four read strings (`Bash(cut *)`, `Bash(sort *)`, `Bash(uniq *)`, `Bash(awk *)`) are his and are not put on any line by this job; they wait for this card to ship, then for the next hub-text card.
- Any file but `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py`. No rule beyond B1–B4: G1–G11 stand as built at `a2e19ceb`; the remaining reads the check recorded (`$VAR` in a `.env` path, `grep -r` of a folder holding `.env`; `cobalt-guard-check-2026-10-04.md` `## RECORDS`) stay open.
- A rule that needs judgment.

## READ
- `ops/desk/bare-guard.py` at `BASE` whole: `READ_FILTERS` and `ENV_READERS` (73–74), `BLOCK` (44), `awk_writes` (372), `pipe_problems` (389), `g3_bash` (543), `sed_problem` (the shape of a deny that names its option). `tests/ops/test_bare_guard.py`: `make_seat`, `run`, `call`, `assert_denied`, `assert_allowed`, `G3_ROUTE`, the G11 tests (`test_g11_…`) and the G3 tests (`test_g3_…`) as the pattern.
- `reports/cobalt-guard-check-2026-10-04.md`: O4, O5 (the tests to restore), `## DECISIONS` 1 and 2. The build report `## DECISIONS` 1.

## RECORDS
- His 2026-10-03 R33 ("allow read-only pipes") is carried in its read-only intent: B1–B4 narrow its wording, so that a pipe that writes a file, runs a program or reads a program from a file is not read-only. They sit on his veto list (desk rows R241, R247, R248, `cto-2026-10-03.md`). The desk read this line from the check report O4, O5 and the build report `## DECISIONS` 1 at 15:56 ET, 2026-10-04.
- RESTARTS class home (K10), each path as `uv run cobalt jobs restarts a8d8a848..HEAD` classified it in the check of `cobalt-guard` (`cobalt-guard-check-2026-10-04.md` `## Suites`, read 15:56 ET 2026-10-04): `ops/desk/bare-guard.py` → `M operator script; no Cobalt reader -`; `tests/ops/test_bare_guard.py` → `M test/documentation; no resident -`; the build report under `docs/` → `A DOCS -`. Expected `RESTARTS: none`; the build runs the table whole (L42) and quotes it.
- `cobalt-guard` ships at `a2e19ceb` (card 10 judged ships, desk row R248); this job's `BASE` is main after set 3 is DEPLOYED.
- The four read strings stay off every session line until this card ships (desk rows R241, R247, R248).
- judge 2026-10-04: D1 CHANGE (B2 by form), D2 CHANGE (B4), D3 KEEP — desk row R254; B2 and B4 narrow R33 to its read-only intent and sit on his veto list.
- judge 2026-10-04 19:27: check O2 CHANGE (B7), O3 CHANGE (B8), not his; row text pasted as the brain wrote it — desk row R273. B7 and B8 narrow R33 to read-only and secrets-safe; both go on his veto list. FOR THE CHECK: the B7 and B8 reds are green, and every earlier guard-b and card 10 test stays green. B5 and B6 are unused numbers.
