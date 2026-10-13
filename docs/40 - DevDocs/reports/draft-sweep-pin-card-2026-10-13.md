## §0 Headline
- Card `516-sweep-pin-card.md` written: one row FR1 (copied from card 446) plus RUN row R2.
- BASE `80563111`; FR1 removes `SWEEP_EXEMPT` entry `f4-refresh-build-2026-10-10.md` (`tests/ops/test_the_rule_sweep.py:55-57`).
- `tests/` → no restart (`src/cobalt/jobs/restarts.py:246`).
- Nothing was run but allowed reads.

## DECISIONS
- ASK DESK: FR1 copied byte for byte holds the words "a fix round" and `:134` (the test is at `:131` at HEAD), against the brief's "no fix-round wording". Default: byte copy kept; the card's WHY and RECORDS say plain devfix, same feature as 446. [10-13]

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `80563111` (BASE).
- `git -C /Users/cobalt/cobalt show HEAD:tests/ops/test_the_rule_sweep.py`: entry key line 55, reason 56-57; `test_every_exempt_entry_still_mismatches` at line 131.
- `grep -c -F "f4-refresh-build-2026-10-10.md" /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` → `1`.
- `grep -n` of `src/cobalt/jobs/restarts.py`: `:38` `OPS_DESK_PREFIX = "ops/desk/"`; `:245-246` `tests/` → "test/documentation; no resident".
- `git status --short -- tests ops` → nothing (HEAD's lines).

DRAFTED · decisions: 1
