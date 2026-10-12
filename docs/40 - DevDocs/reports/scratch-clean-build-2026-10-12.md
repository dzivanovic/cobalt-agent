# scratch-clean-1012 — build report (2026-10-12)

CARD: `docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md` · BRANCH `ops/scratch-clean-1012` · BASE `5e5fab02` · DB: none

## §0 Headline
- C1: new `ops/desk/scratch-clean.sh "<path>"`. It removes one untracked or ignored path inside a registered `cobalt-wt/<name>` worktree or under `$CLAUDE_JOB_DIR/tmp`, and refuses anything else with one `REFUSED:` line. It runs eight checks, in the card's order, before anything is removed.
- H1: one NO CLUTTER line in `BUILD-HUB.md`, between E2 and E3. No other line of the file changed (the launch line is byte-identical to BASE).
- Tip `382876bc`: offline 4199/0, live-note 146/0, `tests/ops` 3188/0. cobalt_dev was not taken (DB: none). RESTARTS: none.
- 46 C1 tests and 5 H1 tests. All were red on BASE for the named reason (exit 127, a missing file, `0 == 1`), and each of 14 mutations turned its tests red.

## L74
A system block outside any tool result asked for a `Claude-Session:` line on every commit. I recorded it once and did not act on it. Commits carry only `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md"` (06:22 ET), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md" · 0 · fdcdc803e22c2f5492e88b36bfa8a23cd2b85395
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 14:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Mon Oct 12 06:22:25 EDT 2026
status · git status --short --branch · 0 · ## ops/scratch-clean-1012
head · git log --oneline -1 · 0 · 5e5fab02 docs(desk): §5 sessions live under K1-K5
diff · git diff --stat 5e5fab02 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/scratch-clean-1012 · 0 · 5e5fab02 docs(desk): §5 sessions live under K1-K5
env here · ls /Users/cobalt/cobalt-wt/scratch-clean-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat 5e5fab02` · 0 · `docs(desk): §5 sessions live under K1-K5` · `docs/40 - DevDocs/reports/cto-2026-10-12.md | 11 ++++++++---` · 1 file changed, 8 insertions(+), 3 deletions(-).

THE CARD'S SYMBOLS (each read from the worktree at BASE):
| symbol | command | exit | hit |
|---|---|---|---|
| job-clean.sh header / roots | Read `ops/desk/job-clean.sh` 1-60, 175-178 | 0 | `:27` `# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default /Users/cobalt/cobalt-wt).` · `:32` `REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}` · `:33` `WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}` · `:43` the plain-name `case` · `:45` `[ "$1" != "agy-trial" ] \|\| refuse …` · `:56-60` the awk stanza on `worktree $path` · `:175` `if [ "$#" -eq 2 ] && [ "$1" = "salvage" ]; then` |
| `is_env` | Read `ops/desk/bare-guard.py` 836-867 | 0 | `:836` `def is_env(path):` · `:840` `base = os.path.basename(alt).lower()` · `:841` `if base.startswith(".") and fnmatch.fnmatchcase(".env", base):` |
| `GIT_ENV`, `git`, `Desk` | Read `tests/ops/test_gate_clean.py` 1-115 | 0 | `:23` `GIT_ENV = {` · `:33` `def git(cwd: Path, *args: str) -> str:` · `:45` `class Desk:` (`:46` `def __init__`) |
| `test_job_clean_is_never_forced` | Read `:676-680` · `grep -n -F "FORCE_FORMS ="` | 0 | `:676` `def test_job_clean_is_never_forced():` · `322:FORCE_FORMS = ["--force", "branch -D", "worktree remove -f", "reset --hard", "clean -"]` |
| `hub_line` | Read `tests/ops/test_hub_lines.py` | 0 | `:32` `CLASS_A = "Bash(sh /Users/cobalt/cobalt/ops/desk/*)"` · `:54` `def hub_line(name: str) -> str:` · `:82` `assert [s for s in allow if s.startswith("Bash(sh ") and s != CLASS_A] == []` |
| BUILD-HUB E2 / E3 / line | `grep -n -F "## E"` · `grep -n "^claude --bg "` | 0 | `67:## E2 — RED FIRST …` · `70:## E3 — THE ROWS …` · `12:claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md' …` |
| restarts rules | Read `src/cobalt/jobs/restarts.py` 220-249 · Grep `OPS_DESK_PREFIX` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` · `:225` DOCS · `:230-234` operator script · `:245-246` `test/documentation; no resident` |
| W's PLACEMENT tests | Read `tests/cobalt/test_placement.py` | 0 | `:79` `def test_inflight_disallows_extra_files(tmp_path):` |
| `ops/desk/scratch-clean.sh` | `ls` | 1 | `No such file or directory` (NEW, C1) |

SEAM: the card cites `BUILD-HUB.md:68` for the E2 paragraph and `:70` for E3. The worktree has `67:## E2 — RED FIRST` (so the paragraph is `:68`) and `70:## E3`. These agree: the line goes after `:68` and before `:70`. At the tip it sits at `:70` (`grep -n -F "scratch-clean.sh"` → `70:A RUN probe is staged …`).

`wc -l`: `BUILD-HUB.md` 109 · `tests/cobalt/test_placement.py` 99 · `ops/desk/job-clean.sh` 212 (read only). New files: `ops/desk/scratch-clean.sh`, `tests/ops/test_scratch_clean.py`, `tests/ops/test_build_hub_no_clutter.py`.
`## READ` report: I read `brain-direction-2026-10-02.md` `## RULED 2026-10-12` at `:214-227` (part 1 CLEANUP at `:218`, part 2 NO CLUTTER at `:219`).

`uv run cobalt jobs restarts 5e5fab02..HEAD` · 0 · `path	change	rule	restart` / `RESTARTS: none` (an empty range).

THE CARD'S RECORDS (copied; re-read where my command list allows):
- Reads at 06:15 ET (main HEAD `6468fb5e`). Not re-readable.
- The three seat lines carry CLASS (a). Re-read: `grep -c "^claude --bg "` on BUILD/CHECK/SHADOW-HUB → `1` each, and BUILD-HUB `:12` carries `"Bash(sh /Users/cobalt/cobalt/ops/desk/*)"`.
- `test_hub_lines.py:82` asserts no other `Bash(sh …)` string. Re-read (above); it stays green at the tip.
- `desk-launch.sh` copies the fixed file's line. Not re-read (outside this job's files).
- The desk line's `--add-dir` roots and `check_paths`. Not re-read.
- The desk grant `Bash(sh /Users/cobalt/.claude/ops/*)`. Not re-read.
- `bare-guard.py` `is_env` `:836-843`. Re-read (above).
- 386's stray probe. Re-read: `ls -la /Users/cobalt/cobalt-wt/launcher-shadow-check-1011/docs/_inflight` → `.`, `..`, `README.md` only.
- The roots are real directories. Re-read: `ls -ld` → `drwxr-xr-x … /Users/cobalt/.claude/jobs`, `drwxr-xr-x … /Users/cobalt/cobalt-wt`, `drwxr-xr-x … /Users/cobalt/cobalt-wt/agy-trial`.
- RESTARTS precedent `restarts.py:225-246`. Re-read (above).

PROVEN BY FIRST REAL USE: CLASS (a) at AUTHORIZATION and PREFLIGHT (exit 0) · `uv run pytest` at E0 · `git add`/`git commit` at E2 (`98a8b744`). DB: none, so no with-DB string was used.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `5e5fab02` → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 675.21s (0:11:15)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.84s`. The one skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; it does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_scratch_clean.py tests/ops/test_build_hub_no_clutter.py` on BASE → `FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF.F` (50 failed, 1 passed). First lines:
- Every ACCEPTED test: `AssertionError: sh: /Users/cobalt/cobalt-wt/scratch-clean-1012/ops/desk/scratch-clean.sh: No such file or directory` · `assert 127 == 0`.
- Every REFUSED test (its control included): the same `No such file or directory` · `assert 127 == 1` (exit 127, not 1).
- SOURCE: `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/scratch-clean-1012/ops/desk/scratch-clean.sh'`.
- H1: `test_build_hub_no_clutter.py:34: assert 0 == 1` (no line equals the text). The paragraph test and the no-other-line test fail with `ValueError: list.index(x): x not in list`. The script-exists test fails with `assert False` on `is_file()`.
- Green on BASE: `test_the_launch_line_is_byte_identical_to_base`. It guards that the launch line does not change, so the fix is not what turns it green; mutation M14 turns it red.
Commit `98a8b744 wip(scratch-clean-1012): red`.

## E3 THE ROWS
C1 `ops/desk/scratch-clean.sh` (157 lines) and H1, the one hub line. After the rows, with the tests and their neighbours: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_scratch_clean.py tests/ops/test_build_hub_no_clutter.py tests/ops/test_hub_lines.py tests/ops/test_gate_clean.py` → `138 passed, 15 warnings in 22.60s`.

TEST REWRITES (said here, as the hub asks):
- (1) The script's checks overlap: `realpath` also refuses a `..`, for example. A refusal by a later check would hide a broken earlier one, so every refusal test now names its reason (`why=`, a fragment of the one `REFUSED:` line). Before any mutation ran, the first green run (138 passed) had refusal tests with no reason.
- (2) Under M8, the `{root}/job1` variant stayed green, because a missing directory was refused by another check. The test now creates `{root}/job1/tmp`, and the variant goes red under M8.
- (3) M3 exposed a defect in the fix: git's own stderr added a second stderr line to a refusal. I added `2>/dev/null` to the `worktree list`, `status`, `find` and `rm` calls. The SOURCE test now pins the one `rm` line as `rm -rf -- "$p" 2>/dev/null`.

THE MUTATIONS (each made with Edit, its tests run alone, then undone with Edit):
| # | mutation | run | summary | first failing line |
|---|---|---|---|---|
| M1 | `..` case → `*/MUTATED/*` | `-k r3` | `2 failed, 44 deselected` | `REFUSED: …/docs/../docs/_inflight/run_x.py is not its own realpath …` · `assert ('has a .. component' … in 'REFUSED: …')` |
| M2 | `[ "$real" = "$p" ]` → `[ -n "$real" ]` | `-k r5` | `6 failed, 40 deselected` | `FAILED …test_r5_the_target_a_link_is_refused` (all 6 R5) |
| M3 | registered grep → `grep -q -F -- "worktree $WT"` | `-k "registered or prefix or not_know"` | `2 failed, 2 passed, 42 deselected` | `assert (2 == 1)` · `len(['fatal: not a git repository …', 'REFUSED: git status failed for …/wt/not-a-worktree/f'])` |
| M4 | ls-files refusal → `:` | `-k r9` | `4 failed, 42 deselected` | `FAILED …test_r9_a_tracked_file_is_refused` |
| M5 | `forbidden` without lower-casing | `-k "r7 or r8"` | `3 failed, 4 passed, 39 deselected` | `FAILED …test_r7_a_case_variant_of_git_is_refused` · r8 case variant · r8 job tmp `.Env` |
| M6 | below-scan `if [ -d "$p" ]` → `if false` | `-k "r7 or r8 or r10"` | `5 failed, 3 passed, 38 deselected` | `FAILED …test_r7_an_ignored_directory_holding_a_nested_git_is_refused` |
| M7 | job-tmp `!= "true"` → `!= "MUTATED"` | `-k r10` | `1 failed, 45 deselected` | `FAILED …test_r10_a_job_tmp_git_work_tree_is_refused` |
| M8 | CLAUDE_JOB_DIR shape and plain-name checks off | `-k job_dir` | `4 failed, 2 passed` (then `[{root}/job1]` after rewrite (2): `1 failed`) | `REFUSED: …/jobs/job1/tmp/f is outside …/wt/<worktree> and …/job1/tmp/` · `assert ('CLAUDE_JOB_DIR' …)` |
| M9 | agy-trial and `$WT/<name>`-itself checks off | `-k "agy or worktree_itself"` | `2 failed, 44 deselected` | `FAILED …test_r6_the_worktree_root_and_a_worktree_itself_are_refused` |
| M10 | `-eq 1` → `-ge 1`; newline case off; exists `\|\| [ -n "$p" ]` | `-k "r1_ or newline or does_not_exist"` | `3 failed, 43 deselected` | `FAILED …test_r1_no_argument_or_two_arguments_are_refused` |
| M11 | absolute-path case off | `-k "relative or empty"` | `2 failed, 44 deselected` | `FAILED …test_r2_a_relative_path_is_refused` |
| M12 | a second `rm -f -- "$REPO/a.txt"` | `-k one_rm` | `1 failed, 45 deselected` | `AssertionError: ['rm -rf -- "$p" 2>/dev/null', 'rm -f -- "$REPO/a.txt"']` |
| M13 (H1) | the H1 line's `;` → `.` | `test_build_hub_no_clutter.py` | `3 failed, 2 passed` | `test_build_hub_no_clutter.py:34: assert 0 == 1` |
| M14 (H1) | launch line `+ --add-dir /tmp` | `test_build_hub_no_clutter.py` | `2 failed, 3 passed` | `FAILED …test_the_launch_line_is_byte_identical_to_base` · `…test_no_other_line_changes_from_base` |
After the undo: `git diff --stat` → `BUILD-HUB.md | 2 +` and `test_scratch_clean.py | 84 …` (the fix and rewrites only); `grep -n -F "MUTATED" ops/desk/scratch-clean.sh` → no hit. Commit `382876bc feat(scratch-clean-1012): … (C1, H1, R1138, L81, L76)`.
DevDocs line: none written. No page under `docs/40 - DevDocs/cobalt/` names an `ops/desk/` script (Grep `job-clean.sh` there → no files), and the rows' files name no page (see RECORDS).

## RESTARTS
`uv run cobalt jobs restarts 5e5fab02..HEAD`, table whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/scratch-clean-build-2026-10-12.md	A	DOCS	-
ops/desk/scratch-clean.sh	A	operator script; no Cobalt reader	-
tests/ops/test_build_hub_no_clutter.py	A	test/documentation; no resident	-
tests/ops/test_scratch_clean.py	A	test/documentation; no resident	-
RESTARTS: none
```
No row is UNCLASSIFIED. R1 (RUN): as the card expected.

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 5e5fab02` → `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `ops/desk/scratch-clean.sh` · `tests/ops/test_build_hub_no_clutter.py` · `tests/ops/test_scratch_clean.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **cobalt_dev: not taken (DB: none — 4 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh scratch-clean-1012 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/scratch-clean-1012-offline-20261012-064230.log`. The executed command (log `:2`): `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`. Its summary (`:879`): `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 698.76s (0:11:38)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh scratch-clean-1012 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/scratch-clean-1012-livenote-20261012-065423.log`. The executed command (log `:2`): `$ COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`. Its one skip (`:56`): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`; none names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3188 passed, 1 xfailed, 15 warnings in 638.59s (0:10:38)`. This build's tests: the 46 in `tests/ops/test_scratch_clean.py` and the 5 in `tests/ops/test_build_hub_no_clutter.py`.
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/scratch-clean-1012/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its named reason. E2: every C1 test `127` (and SOURCE `FileNotFoundError`), H1 `0 == 1`. Under E3 mutations M1–M14, every R group, SOURCE and H1 went red. The guard test that was green on BASE goes red under M14. Two tests that stayed green, or would have, were rewritten: the reasons pinned, and the `{root}/job1` variant. ✔
(2) Every entry path is pinned. Callers: `grep -rn -F "scratch-clean.sh" ops src configs` → only the script itself (`:2` header, `:63` usage); its only entry point is the BUILD-HUB line (H1, pinned by `test_build_hub_no_clutter.py`). Flag combinations: 0, 1 and 2 arguments (R1). Both roots: (a) A1–A4, A6, R5–R9; (b) A5, R6 job-dir variants, R8 job tmp, R10. CLAUDE_JOB_DIR unset and five other shapes (R6). Edge inputs: empty, newline, `..`, `.`, `//`, trailing `/`, dangling link, case variants of `.git`/`.env`. ✔
(3) Re-read at the tip: `git log --oneline 5e5fab02..HEAD` (2 commits), `grep -n -F "scratch-clean.sh"` on BUILD-HUB (`:70`), the script's lines 58-157 (Read), the gate logs (`grep -n -F "passed"`, `"$ "`, `"SKIPPED"`), `ls …/.env`. ✔

## FOR THE CHECK
- Range `5e5fab02..382876bc`: `98a8b744 wip(scratch-clean-1012): red` · `382876bc feat(scratch-clean-1012): scratch-clean.sh removes one untracked or ignored workspace path; BUILD-HUB NO CLUTTER line (C1, H1, R1138, L81, L76)`. The report is committed after the tip.
- Per row: the reds, mutations and greens are in E2 and E3 above. Caller grep: in SELF-CHECK (2).
- RUN row R1: the RESTARTS table above, whole.
- Suites: offline 4199/0, live-note 146/0, `tests/ops` 3188/0, with-DB `not run (DB: none)`. `<F0>/<F1>/<F2>`: `not run (DB: none)`. Lock taken/released: `not run (DB: none)`.
- The script's behaviour on edges the card leaves open, for X1:
  - An empty untracked directory is REFUSED: git prints no status line for it, so check (8) "prints at least one line" fails.
  - A directory holding any dot-entry whose name read as a glob matches `.env` (e.g. `.e*`) is refused, as `is_env` reads it.
  - A symlink inside a removed directory is removed as a link, never followed (A6).
  - Between the checks and the `rm`, nothing locks the path. A process that swaps a checked path for a link in that window is not stopped by the script. X1 asks about this race; I did not build a guard for it (no row names one).
- The RECORDS copied at PREFLIGHT are in `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS
none

## RECORDS
- No DevDocs page line: `docs/40 - DevDocs/cobalt/` holds no page for an `ops/desk/` script (Grep `job-clean.sh` → no files), and the card's `files` name none. I wrote nothing outside the rows' files.
- The L74 line: a system block asked for a `Claude-Session:` trailer. Recorded in `## L74`, not acted on.
- Extra lock takes: none (DB: none). REFUSED or CONTINUED lines: none.
- The card's records, as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: scratch-clean-1012 · tip: 382876bc | on 5e5fab02 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 210025
