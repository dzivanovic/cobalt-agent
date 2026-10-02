JOB: ops-glob
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/ops-glob-1002
WORKTREE: ops-glob-1002
BASE: a0188b69
TIP:
REPORT: /Users/cobalt/cobalt-wt/ops-glob-1002/docs/40 - DevDocs/reports/ops-glob-build-2026-10-02.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47

## ROWS

| row | what | red first | files |
|---|---|---|---|
| G1 | Every path under `ops/desk/` is an operator script, by rule and not by list. In `src/cobalt/jobs/restarts.py`: a constant `OPS_DESK_PREFIX = "ops/desk/"` beside `OPS_TOOLS` (line 36), with one comment line saying why the folder is safe to match whole (it holds the desk's and the hubs' shell tools and a git hook; no plist executes a file in it); and the test at line 224 becomes `path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)`. `OPS_TOOLS` itself stays as it is. The rule text and the empty restart set stay `operator script; no Cobalt reader` | in `tests/cobalt/test_jobs_restarts.py`, beside `test_an_operator_script_with_no_cobalt_reader_derives_no_restart` (line 97) and in its shape: `test_every_path_under_ops_desk_is_an_operator_script` — changes `ops/desk/any-new-tool.sh` (A), `ops/desk/pre-commit` (M), `ops/desk/sub/x.py` (A) each classify `operator script; no Cobalt reader` with no restart. Negative controls in the same test: `ops/desktop.sh` (the prefix without its slash) is NOT matched by this rule, and `test_a_resident_wrapper_script_is_not_an_operator_script` (line 111) still passes. RED on `BASE`: `ops/desk/any-new-tool.sh` does not classify as an operator script | `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `docs/40 - DevDocs/cobalt/jobs/restarts.md` |

## NOT IN THIS JOB
- Any entry added to `OPS_TOOLS`; any script under `ops/`; `configs/cobalt/jobs.yaml`.
- Any other classification rule of `classify`.

## READ
- `src/cobalt/jobs/restarts.py` lines 28–36 (`OPS_TOOLS` and its comment) and lines 220–228 (the rule).
- `tests/cobalt/test_jobs_restarts.py` lines 97–122.

## CHECK ASKS
- X1 Does any plist under `ops/`, any `reads:` entry of `configs/cobalt/jobs.yaml` or any `src/` module name a file under `ops/desk/`? Write the `grep` that would show it.
- X2 Can a path that is not under the folder match the prefix test?

## RECORDS
- RESTARTS class homes: `src/cobalt/jobs/restarts.py` → static import reach (`restarts.py:210`), so `com.cobalt.radar`; `tests/cobalt/*` → test/documentation (`:239`); `docs/…` → DOCS (`:219`). (the brain, 08:20 ET)
- Why: both `ops/desk-size-guard-1001` and `ops/devdb-lock-1001` lift their scripts into `OPS_TOOLS` on the same lines and conflict at a merge; every later script card would do it again. Card `16-ops-seam-card.md` carries neither lift and stands on this job's tip.
- His order sets aside the outside house for this card (`reports/brain-direction-2026-10-02.md` row 10): the check is the fresh Opus session alone (`CHECK-HUB.md`, the NO OUTSIDE HOUSE line).
