# archiver-429 — card 206 amend r2, 2026-10-09

## §0 Headline
Card 206 re-pointed on preflight r2: one class, one reading.
A retry that would pass 600 s of used waits is not taken; rule, test (4) and bound agree.
Budget lives in the runner; test (4) sums retry waits only; red reasons stated in row order.
BASE `fa968552` and RULINGS `2026-10-08 R685` kept. No `«FILL`.

## CHANGES
Card `prompts/2026-10-09/206-archiver-429-card.md`, edited in place:
1. A2 rule: a retry whose wait would take the used retry-wait total past `RETRY_429_BUDGET_SECONDS` is NOT taken, nor is one past `RETRY_429_MAX`; the 429 is recorded as a failure. Waits sum ≤ 600 s.
2. A2 rule: the budget used lives in the runner (a local or a `summary` attribute the runner sets), never in row B; B adds `record_retry`; A2's `files` unchanged.
3. A2 test (4): sums only the retry waits (15 s and up, filtered from the 1.2 s between-target sleeps); the target whose retry would pass the budget is a failure.
4. A2 and B: red-on-BASE reasons hold in row order; first red is the `ImportError` on `FinvizRateLimited`.
5. `## RECORDS`: new retry-bound line (2053 s, 2104 s, 2229 s < 2400 s). `## NOT IN THIS JOB` points at it, not at "check 14".

## DECISIONS
1. Added the bound as a `## RECORDS` line, since the card had none to reword.
2. Test (4) names the filter as "15 s and up", per the prompt; the builder may filter on the helper instead.

## RECORDS
- `git show f5010068:src/cobalt/archiver/runner.py` read whole: fetch sites, `except CollectorError`, sleeps, `run_full`, `_archive_nightly` match the card's refs.
- `grep -c -F "«FILL"` on the card → 0.
- No other file edited.

ARCHIVER 429 CARD RE-POINTED R2 · decisions: 2
