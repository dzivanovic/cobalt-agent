JOB: sweep-pin-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1406, R1412
CLASS: K5
INSTALL: none
BRANCH: ops/sweep-pin-1013
WORKTREE: sweep-pin-1013
BASE: 03d8ebbe
TIP:
REPORT: /Users/cobalt/cobalt-wt/sweep-pin-1013/docs/40 - DevDocs/reports/sweep-pin-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/sweep-pin-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: brain L79, R1406, R1412 and FR1-3. `tests/ops/test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches` fails on main with `AssertionError: ['f4-refresh-build-2026-10-10.md']`, so main's offline suite is red and every deploy gate fails. URGENT: this card deploys before every other card. One devfix row, the same feature as card 446 (`## RECORDS`).

| row | what | red first | files |
|---|---|---|---|
| FR1 | THE STALE EXEMPTION GOES (a fix round; main's offline suite is red and every deploy gate fails). Remove ONE entry from `SWEEP_EXEMPT` in `tests/ops/test_the_rule_sweep.py`: the key `"f4-refresh-build-2026-10-10.md":` and its two-line reason string (`:55`-`:57`, proved by `git show HEAD:tests/ops/test_the_rule_sweep.py`; no other file holds the name, `grep -n -F "f4-refresh-build-2026-10-10.md" tests ops` → that one hit). Cause: card 304's rows CR and CR2 gave that build report plain `CARRIED:` and `SETTLED:` lines (`reports/f4-refresh-build-2026-10-10.md:276-286`), so it no longer mismatches and `test_every_exempt_entry_still_mismatches` (`:134`) rejects the entry, exactly as that pin intends. Nothing else is changed: the other six entries, `CHECKS_SWEPT`, `BUILDS_SWEPT` and the report are untouched | `uv run pytest -q tests/ops/test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches`: RED before the removal, `AssertionError: ['f4-refresh-build-2026-10-10.md']`; GREEN after. Pins, GREEN before and after, whole file: `uv run pytest -q tests/ops/test_the_rule_sweep.py` → `0 failed` (`test_the_sweep_has_no_mismatch`, `test_the_exempt_reasons_name_their_shape`, `test_the_304_check_reads_o1_and_a3`, `test_the_sweep_swept_what_it_pins` among them) | `tests/ops/test_the_rule_sweep.py` (RESTARTS class home: `tests/` → "test/documentation; no resident", `src/cobalt/jobs/restarts.py:246`; no restart) |
| R2 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line. Expected none: `ops/desk/` → "operator script; no Cobalt reader" (`src/cobalt/jobs/restarts.py:38`, `:230-232`), `tests/` → "test/documentation; no resident" (`:246`), `docs/` → `DOCS` (`:225-228`) | — (output quoted) | none |

## NOT IN THIS JOB
- Any other line of `tests/ops/test_the_rule_sweep.py`: the other six `SWEEP_EXEMPT` entries, `CHECKS_SWEPT`, `BUILDS_SWEPT` and the tests stand.
- Any check or build report (R1157: "this report is never edited to pass a gate"); `ops/desk/deploy-card.sh`, `desk-launch.sh`, `deploy-step0.sh`; any other test file; card 304, its branch and its fix report.
- A new command, option, script or seat (R411, R412); any `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` lines 40-70 (`SWEEP_EXEMPT`) and 128-135 (`test_every_exempt_entry_still_mismatches`).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md` lines 276-286 (the plain `CARRIED:` and `SETTLED:` lines).
- Precedent: `prompts/2026-10-13/446-k5-gate-card.md` row FR1.

## CHECK ASKS
- X1 Is exactly the one `SWEEP_EXEMPT` entry `f4-refresh-build-2026-10-10.md` (key and reason, `:55`-`:57` at `BASE`) removed and nothing else changed in the file?
- X2 Does `uv run pytest -q tests/ops/test_the_rule_sweep.py` read `0 failed`, and does `grep -c -F "f4-refresh-build-2026-10-10.md" tests/ops/test_the_rule_sweep.py` print `0`?
FOR THE CHECK: sweep pin 2026-10-13 brain: FR1-3 KEEP

## DEPLOY PROOF
- `grep -c -F "f4-refresh-build-2026-10-10.md" /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` · before `1` · after `0`

## RECORDS
- Reads by the drafter `draft-sweep-pin-card`, 2026-10-13, at `main` HEAD `80563111` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`); `git -C /Users/cobalt/cobalt status --short -- tests ops` printed nothing, so `tests/` and `ops/` read as HEAD's.
- `git -C /Users/cobalt/cobalt show HEAD:tests/ops/test_the_rule_sweep.py` read whole: the entry key `"f4-refresh-build-2026-10-10.md":` is at line 55, its reason at lines 56-57 (`grep -n` of the same file: line 55 is the only hit); `test_every_exempt_entry_still_mismatches` is at line 131 of the file at HEAD (the row text's `:134` is card 446's older count; the row text stands unchanged).
- `grep -c -F "f4-refresh-build-2026-10-10.md" /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` printed `1`.
- RESTARTS class home: `src/cobalt/jobs/restarts.py:245-246` (`grep -n`): `if not rule and path.startswith("tests/")` → `rule = "test/documentation; no resident"`; the one changed path `tests/ops/test_the_rule_sweep.py` → no restart. `OPS_DESK_PREFIX = "ops/desk/"` at `:38`.
- The same feature as card 446 (`446-k5-gate-card.md`, row FR1, which this card carries unchanged); the sweep file is on main, so the fix is a plain one-row devfix of the red test.
- `BASE` is the desk's: `main` at the launch (the desk rewrites it if `main` has moved); `TIP` starts empty. Tests only: house A is Grok, `HOUSE B: as needed`, never OpenAI (R920).
