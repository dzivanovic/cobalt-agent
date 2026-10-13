## §0 Headline
Row `FR1` added to `## ROWS` of `prompts/2026-10-13/446-k5-gate-card.md` (before `R2`), nothing else touched.
It removes the one `SWEEP_EXEMPT` entry `f4-refresh-build-2026-10-10.md` (`tests/ops/test_the_rule_sweep.py:55-57`).
RED/GREEN not run by this seat (no `uv`/pytest in its tool list); the failing text is the desk's, the builder runs it.
No restart: `tests/` is "test/documentation; no resident".

## DECISIONS
- ASK DESK: the RED and the whole-file pass (`uv run pytest -q tests/ops/test_the_rule_sweep.py` → `0 failed`) are unrun by this seat; default: the builder's first run quotes both, as the row says. [any time before build launch]

## RECORDS
- Entry: `grep -F "f4-refresh-build-2026-10-10.md" tests ops` → one hit, `tests/ops/test_the_rule_sweep.py:55`; `git show HEAD:tests/ops/test_the_rule_sweep.py` (HEAD `eb1da03c`) holds the same entry at `:55-57`; `git status` shows `tests/` and `ops/` clean.
- Cause read: `reports/f4-refresh-build-2026-10-10.md:276-286` now holds plain `CARRIED: O1/A3 — … — R998` and `SETTLED:` lines (the report's file name is unchanged from the entry key).
- RESTARTS class home: `tests/` → "test/documentation; no resident" (`src/cobalt/jobs/restarts.py:246`); no restart.
- BASE, TIP and other header lines of the card untouched; no placeholder token.

DRAFTED · decisions: 1
