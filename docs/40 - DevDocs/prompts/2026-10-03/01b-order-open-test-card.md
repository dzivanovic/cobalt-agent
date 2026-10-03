JOB: order-open-test
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/order-open-test-1003
WORKTREE: order-open-test-1003
BASE: 77d19438
TIP:
REPORT: /Users/cobalt/cobalt-wt/order-open-test-1003/docs/40 - DevDocs/reports/order-open-test-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R154, 2026-10-02 R157

## ROWS

WHY: `tests/ops/test_order_open.py::test_every_block_carries_its_facts_and_nothing_changes` is red on `main` since last night's deploy put `house-probe.sh` beside `order-open.sh`: the script now probes, and the test, which expected `not probed`, reached a REAL house (`sol: OUT — …`). A test never touches a house. After card `01` every `DB: none` build runs all of `tests/ops` at W (a0), so this red would end each of them FAILED (lock-relief build DECISION 1). One row; it stacks on `01`'s tip and ships with it.

| row | what | red first | files |
|---|---|---|---|
| Q1 | The test stubs `house-probe.sh`: a tmp copy of `order-open.sh` with a stub `house-probe.sh` beside it (or on `PATH`, whichever `order-open.sh` resolves) printing canned `sol: UP` / `grok: OUT — usage` / `gemini: OUT — TIMEOUT` lines; the assertion reads those lines in the block and that nothing else changed. If `order-open.sh` resolves the probe by an absolute path, that one line becomes `$(dirname "$0")/house-probe.sh`, so the stub can stand in; no other change to the script | the test itself, run alone on `BASE`: red with the real probe's line (quote it), green with the stub. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `0 failed` at the tip | `tests/ops/test_order_open.py`; `ops/desk/order-open.sh` (one line, only if the path is fixed) |

## NOT IN THIS JOB
- Any behaviour of `order-open.sh` but how it finds the probe; `house-probe.sh`; any other `tests/ops` file.

## READ
- `reports/lock-relief-build-2026-10-03.md` `## DECISIONS` item 1; `tests/ops/test_house_probe.py` (the stub shape); `ops/desk/order-open.sh` at `BASE`.

## RECORDS
- Stacked on card `01`'s tip `77d19438` (judge, `reports/lock-relief-decisions-2026-10-03.md` item 1); ships in set 1 with `01`.
- No `DB` key: under `main`'s hub text this card takes the lock as every card does; its own proof is the `tests/ops` run in E2 / E3.
