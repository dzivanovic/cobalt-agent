JOB: launcher-1010
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R810
BRANCH: ops/launcher-1010
WORKTREE: launcher-1010
BASE: eed03ce8
TIP: b71837f2
REPORT: /Users/cobalt/cobalt-wt/launcher-1010/docs/40 - DevDocs/reports/launcher-build-2026-10-10.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-check-2026-10-10.md
HOUSE B: as needed
RULINGS: 2026-10-08 R685

## ROWS

| row | what | red first | files |
|---|---|---|---|
| A | `deploy-card.sh --fix-report` (`cto-2026-10-09.md` R810; `CARD.md` :48, K3). Today the script writes every `## SHIPS` row with an empty last cell (`ops/desk/deploy-card.sh:147`) and refuses any option it does not know (`:55`), so a fix-round row is typed by hand. Add the repeatable option `--fix-report "<job>=<fix report path>"`, `<job>` a JOB of a job card given, the path under `$REPORTS`. For that job's row the script reads the fix report, requires its last non-blank line to start `BUILT ·` and carry `tip: <hex>`, writes that tip as the row's code tip and the path, backticked, as the row's `fix report` cell. It refuses (exit 1, nothing written, the job named): a job not among the cards; a path outside `$REPORTS` or not ending `.md`; a report absent at the job's branch head (`git show <head>:<rel>`, as `desk-launch.sh:862`, never a copy on main); a last line that is not `BUILT ·` with a `tip:`; a check tip that is not an ancestor of the fix tip; a fix tip that is not an ancestor of the head; a head that adds paths outside `docs/` past the fix tip (the existing `:143-144` rule, read against the fix tip). The check report's literals (`held unfixed: 0`, `ready: YES`) are still read from the CHECK report (`:136-137`). A row with no `--fix-report` is byte-for-byte what `:147` writes today | In `tests/ops/test_deploy_card.py`, using its `Desk` fixture: `test_a_fix_report_fills_the_ships_row_cell_and_code_tip` builds a fix commit on `ops/alpha` past the check's tip, commits `alpha-fix.md` ending `BUILT · job: x · tip: <fix tip> | rows: 1 of 1` on the head, runs `desk.run("--fix-report", f"alpha={path}")`; asserts `returncode == 0`, alpha's row (`section(text, "SHIPS")`) carries `` `<fix tip>` `` as its code tip and the path in its last cell, beta's row's last cell is empty. RED on `BASE`: `returncode == 1` (`unknown option '--fix-report'`). Plus refusal tests, each RED on `BASE` for the same reason, each asserting the reason text and that `desk.out` does not exist: absent at the head; last line not `BUILT ·`; fix tip not past the check tip; unknown job. Plus `test_no_fix_report_leaves_every_cell_empty` (green on `BASE` and after: the guard that nothing else moved). Plus the round trip: the card written passes `desk-launch.sh`'s `ships_checked` (`desk-launch.sh:804-884`) in the style of `tests/ops/test_deploy_step0.py::test_o1_a_fix_round_row_the_launcher_accepts_passes_p2` | `ops/desk/deploy-card.sh`, `tests/ops/test_deploy_card.py` |
| B | RUN — asserts nothing, then a fix row only if the run finds it. Item: the deploy launcher's accept-list of held items named fixed (`areas/cobalt.md` NOW OPS line). `grep -n "named fixed\|accept" ops/desk/` finds no list in any script (the only hits are `house-probe.sh:18,67`, `bare-guard.py:1086`, `install-fixed.sh:8`, `desk-launch.sh:105`, none of them a held-item list). The only held-defect text in a script is `deploy-step0.sh:27-28` ("A held defect carried by a ruling is not read here: such a line FAILS and the hub reads it"). Run: `grep -rn "held" ops/desk/deploy-step0.sh ops/desk/desk-launch.sh ops/desk/authorize.sh` and `grep -n "held" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; quote the output; name in the report which file holds the list, its lines, and its current items. If the list is in a script under `ops/desk/`: add the row's fix and its RED test in `tests/ops/` (offline, fake files) and say so in `## DECISIONS`. If it is in `DEPLOY-HUB.md` or anywhere outside `ops/desk/` and `tests/ops/`: no edit; `## DECISIONS` item `DECISION B1` (UNPROVEN, L70) names the file and lines for the desk | — (tool output quoted in the report) | none (read only); a fix only inside `ops/desk/` and `tests/ops/` if the run finds the list there |
| C | RUN — asserts nothing, then a fix row only if the script reads the list. Item: D0 (STEP-D0, the deploy preflight) accepts `.claude/settings.json.bak` as a held item (`cto-2026-10-10.md` R828, `.bak` stays his). Today the ACCEPTED list is prose in `DEPLOY-HUB.md:113` (` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`), and `deploy-step0.sh:515-518` only records `git status --short --branch` and counts `$dirty` lines, never a gate. Run: `grep -rn "rules.yaml\|settings.json" ops/desk/` and quote it (today only `stop-guard.py:42`, a comment about a different file). If no script under `ops/desk/` reads the accepted list: no edit; `DECISION C1` (UNPROVEN, L70) says the list is `DEPLOY-HUB.md` text, a fixed file, and the one-line addition (`?? .claude/settings.json.bak`) is the desk's own install by `ops/desk/install-fixed.sh`, outside this job. If a script does read it: add `?? .claude/settings.json.bak` to it, with the RED test in `tests/ops/`: a fake repo whose status holds `?? .claude/settings.json.bak` alone passes, and one with `?? src/x.py` still fails | — (tool output quoted in the report) | none (read only); a fix only in the script the run finds, and its test in `tests/ops/` |

## NOT IN THIS JOB
- Any text of `DEPLOY-HUB.md` or any other fixed file (`CARD.md`, `BUILD-HUB.md`, `CHECK-HUB.md`); a hub edit is the desk's `install-fixed.sh`, by his approved row.
- The pgrep row of `DEPLOY-HUB.md` (needs his word); `ops/desk/orphan-clean.sh`; the `ops-hand` seat; the R685 orphan-cause card.
- A new command or option for any seat other than `deploy-card.sh --fix-report` (R411, R412); `desk-launch.sh`'s `ships_checked` and `deploy-step0.sh`'s P2 are read, not changed (the round trip test only runs them).
- Touching `.claude/settings.json` or `.claude/settings.json.bak`: the `.bak` stays his.
- Any `src/` or `configs/` file; any with-DB test.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-09.md` row R810; `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md` row R828.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md` `## SHIPS` and its :48 paragraph (the fix-round row).
- `ops/desk/deploy-card.sh` whole (the options `:43-58`, the per-card read `:106-164`, the row `:147`, the card text `:199-222`).
- `ops/desk/desk-launch.sh:804-884` (`ships_checked`, `fixed_ok` `:856-869`, the `frep` cell `:820`).
- `ops/desk/deploy-step0.sh:24-31` (P2, P3) and its fix-round branch (~:385-403).
- `tests/ops/test_deploy_card.py` (the `Desk` fixture `:47-130`, `section`, `header`); `tests/ops/test_deploy_step0.py:546-620`.
- `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:113` (STEP-D0 MAIN), read only.

## CHECK ASKS
- X1 Does a row with no `--fix-report` come out byte-for-byte as before (the `:147` row and the card text)?
- X2 Does every refusal of row A leave `--out` unwritten and the repo state (status, refs, index) unchanged, as the existing tests assert?
- X3 Does the card written for a fix round pass `ships_checked` in `desk-launch.sh` (the code tip is the fix report's `tip:`, the check's tip an ancestor of it)?
- X4 Rows B and C: did the builder quote the `grep` outputs, and does each decision name the file and lines of the list it found? Is any edit outside `ops/desk/` and `tests/ops/`?

## RECORDS
- RESTARTS: none. `ops/desk/` derives `operator script; no Cobalt reader` and no restart (`src/cobalt/jobs/restarts.py:230-232`, `OPS_DESK_PREFIX = "ops/desk/"` at `:38`); `tests/` derives `test/documentation; no resident` (`:245-246`). The builder runs `uv run cobalt jobs restarts <BASE>..HEAD` and quotes `RESTARTS: none`.
- Row A's current behaviour read from `deploy-card.sh` at `d0a5fbb8` (the files are identical on HEAD): no `--fix-report` (`:46-58` options; `:55` refuses unknown); the row `:147` ends `| |`; the tip is the check's `tip:` (`:138`).
- Rows B and C: the accepted list is `DEPLOY-HUB.md:113`; no `ops/desk/` script reads it (`deploy-step0.sh:515-518` records only). Both rows stay diagnose-first (L70).
- Tests in `tests/ops/` run offline on fake repos and files (`Desk` fixture, `COBALT_REPO_ROOT`, `COBALT_WT_ROOT`); class of `tests/`: `test/documentation; no resident`.
