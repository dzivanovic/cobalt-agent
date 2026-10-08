JOB: dayopen-desk-check
LADDER: OFF-LADDER — reports/cto-2026-10-08.md R658
BRANCH: feat/dayopen-desk-check-1008
WORKTREE: dayopen-desk-check-1008
BASE: «FILL: main HEAD at launch, 8 hex»
TIP:
REPORT: /Users/cobalt/cobalt-wt/dayopen-desk-check-1008/docs/40 - DevDocs/reports/dayopen-desk-check-build-2026-10-08.md
CHECK REPORT:
HOUSE B:
RULINGS: 2026-10-08 R658, 2026-10-08 R660

## ROWS

WHY: on 10-08 the desk `02bc7d67` was gone, and no day-open said so. Rows K1-K2, in order. Each row has a test that is RED on BASE for the reason it names, plus negative controls.

| row | what | red first | files |
|---|---|---|---|
| K1 | C7 "cto-desk live", a new check in `src/cobalt/dayopen/checks.py` in the C1 shape (`:87-101`). `DESK_LIST_PATH = REPO_ROOT / "ops" / "desk" / "desk-list.sh"`, the repo copy, never `~/.claude/ops`. `_run_desk_list(path)` runs `subprocess.run(["sh", str(path)], capture_output=True, text=True, timeout=20)`, the `ops/desk/stop-guard.py:219-229` call. `check_c7_desk_live(*, desk_list_path: Path = DESK_LIST_PATH, run_list: Callable[[Path], subprocess.CompletedProcess] = _run_desk_list) -> CheckResult`, id `C7`, title `cto-desk live`. Rows are desk-list's stdout lines `id · name · cwd · status · state` (`ops/desk/desk-list.sh:2-3,16`). A desk row is a line split on ` · ` into 5 or more fields whose field 1 equals `cto-desk` exactly (the `ops/desk/desk-context.sh:43-46` rule). A shorter line is not a row and never raises. id-less live rows are skipped by desk-list itself and counted on its stderr (`desk-list.sh:5-6,13-18`); C7 copies that stderr into `raw` and never fails on it. VERDICTS: `OSError` or `subprocess.TimeoutExpired` from `run_list` → ERROR, `ERROR(command failed) — <e>`. Exit non-zero → ERROR, `ERROR(command failed) — sh <path> exited <n>: <stderr or (no output)>` (an unreadable list never passes, L1; desk-list exits 1 when `claude agents --json` gives no JSON). One or more desk rows → PASS, `PASS — cto-desk live: <id> (<status>, <state>)`, rows joined by `; `. None → FAIL, exactly `FAIL — desk missing — relaunch with desk-launch.sh desk`. `raw`: `command: sh <path>`, `exit: <n>`, stdout whole (or `(no rows)`), `--- stderr`, stderr whole (or `(empty)`). Add `DESK_LIST_PATH` and `check_c7_desk_live` to `__all__` (`:455-468`); the module docstring (`:1`) says seven checks, C1-C7 | `tests/cobalt/test_dayopen_checks.py`, new `# C7` section, `run_list` stubbed with `subprocess.CompletedProcess`, never the real `claude`. `test_c7_fail_when_no_cto_desk_row`: stdout `abc12345 · dayopen-desk-draft · ~/cobalt · running · busy` → FAIL, detail equals the FAIL line above. RED on BASE: `AttributeError: module 'cobalt.dayopen.checks' has no attribute 'check_c7_desk_live'`. NEGATIVE CONTROLS, green after: (a) a live `cto-desk` row among others → PASS, its id in the detail; (b) stdout empty, stderr `skipped 2 live row(s) without an id`, exit 0 → FAIL, that stderr line in `raw`; (c) the same stderr with a `cto-desk` row → PASS; (d) a 1-field line `cto-desk` and a row named `cto-desk-old` → FAIL, no raise; (e) exit 1 → ERROR, `ERROR(command failed)`; (f) `run_list` raises `subprocess.TimeoutExpired` and, parametrized, `FileNotFoundError` → ERROR; (g) `checks.DESK_LIST_PATH == checks.REPO_ROOT / "ops" / "desk" / "desk-list.sh"` and the file exists | `src/cobalt/dayopen/checks.py`, `tests/cobalt/test_dayopen_checks.py`, `docs/40 - DevDocs/cobalt/dayopen/checks.md` (one dated line) |
| K2 | THE DAY-OPEN RUNS C7 LAST. `runner.run()` (`src/cobalt/dayopen/runner.py:28-37`) appends `checks.check_c7_desk_live()` after C6. The roll-up stays `models.overall_verdict` (`src/cobalt/dayopen/models.py:49-71`): a missing desk is FAIL → OVERALL AMBER; an unreadable list is ERROR → RED. The report renders it with no change (`report.py:40-68`: section `## C7 cto-desk live`, verdict row `\| C7 \| cto-desk live \| FAIL \| desk missing — relaunch with desk-launch.sh desk \|`). The module docstring (`:1-7`) says seven checks, C1-C7 | `tests/cobalt/test_dayopen_runner.py`. NEW `test_run_is_amber_when_no_desk_is_live`: C1-C6 patched PASS (the `:45-50` way), `monkeypatch.setattr(checks, "_run_desk_list", <stub: exit 0, one non-desk row>, raising=False)`, `runner.run(report_date=date(2026, 9, 14), now=NOW)` → asserts `report.overall is Overall.AMBER`, `report.checks[-1].id == "C7"`, its detail equals the FAIL line. RED on BASE: `assert <Overall.GREEN: 'GREEN'> is <Overall.AMBER: 'AMBER'>` (BASE has no C7; the stubbed list with no `cto-desk` row leaves the day GREEN). UPDATE `test_run_calls_all_six_checks_in_order_and_rolls_up` (`:18-41`) → `…all_seven…`, C7 patched PASS, `calls` and ids end in `"C7"`; `test_run_defaults_report_date_to_todays_et_date` (`:44-55`) patches C7 PASS, so no test runs the real `desk-list.sh`. NEGATIVE CONTROL green after: the same run with a `cto-desk` row in the stub → GREEN | `src/cobalt/dayopen/runner.py`, `tests/cobalt/test_dayopen_runner.py`, `docs/40 - DevDocs/cobalt/dayopen/runner.md` (one dated line) |

No test opens a DB, runs `claude`, or reads `/Users/cobalt/.claude`. The mutations (BUILD-HUB E3): K1, the desk-row test accepts any 5-field row → (a)-negative pair goes red; field-count guard removed → (d) raises `IndexError`; non-zero exit read as rows → (e) goes red. K2, the C7 line removed from `runner.run` → the new runner test goes red.

RESTARTS (K10): `uv run cobalt jobs restarts <BASE>..HEAD`, quote the table whole. Classes by `src/cobalt/jobs/restarts.py:178-264`: the two `src/cobalt/dayopen/` files → `static import reach` (`:215-220`), the residents named by the table; the two tests → `test/documentation; no resident` (`:245-246`); the two DevDocs pages → `DOCS` (`:225-229`). `RESTARTS:` is the table's last line, never predicted.

## NOT IN THIS JOB
- Any file outside the ROWS' `files` cells (and the build report). Not `ops/desk/desk-list.sh`, `prompts/DAY-OPEN-QWEN.md`, `~/.qwen/settings.json`, any allow file, `~/.claude/ops/*`.
- `src/cobalt/dayopen/models.py`, `report.py`, `cli.py`, `__init__.py`, `config.py`: no change. Their "six" / "C1-C6" docstrings stay (`__init__.py:3,6`, `models.py:1,4`, `cli.py:6`).
- No calendar guard on C7: the check runs the same on every date.
- No new command: C7 runs the existing `ops/desk/desk-list.sh`; the Qwen seat still runs only `cobalt day-open` (`DAY-OPEN-QWEN.md:8-9`).
- No DB in any new test.

## READ
- `reports/cto-2026-10-08.md` R658, R660; `reports/desk-ops-fixes-draft-2026-10-08.md` `## DECISIONS` D2.
- `src/cobalt/dayopen/checks.py` whole (468 lines); `runner.py` whole (47); `models.py:16-82`; `report.py:40-68`.
- `tests/cobalt/test_dayopen_checks.py:1-111`; `tests/cobalt/test_dayopen_runner.py` whole (55).
- `ops/desk/desk-list.sh` whole (19); `ops/desk/stop-guard.py:219-229`; `ops/desk/desk-context.sh:40-50`.
- `reports/day-open-2026-10-07.md:164-176` (the VERDICT shape).

## RECORDS
- Citations proven at main HEAD `c364bc43` by Read / Grep (drafter, 2026-10-08 07:43 EDT); see `reports/dayopen-desk-check-draft-2026-10-08.md` `## RECORDS`.
- `grep runner.run`: the one caller is `src/cobalt/dayopen/cli.py:42`; `tests/cobalt/test_dayopen_cli.py:56,85` patch `runner.run`, so the CLI tests do not reach C7.

## PRE-STOP SELF-CHECK
`BUILD-HUB.md` `## PRE-STOP SELF-CHECK` (K25), with the evidence for this card:
(1) The RED of each new test is quoted from BASE: K1 the `AttributeError` line, K2 `GREEN is AMBER`. Each negative control (K1 a-g, K2 the GREEN run) is quoted green at the tip, and each mutation above is quoted red.
(2) Entry paths: `check_c7_desk_live` is called only by `runner.run` (grep), which is called only by `dayopen/cli.py:42` (grep). Each verdict path (PASS, FAIL, ERROR by exit, ERROR by raise) and each row shape (id-less stderr, short line, near-name) is pinned by a named test.
(3) Every `file:line` and count in the report is re-read at the tip with `git show <tip>:<path>` / `grep -n`.
