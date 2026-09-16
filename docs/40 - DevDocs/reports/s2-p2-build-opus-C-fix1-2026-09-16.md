# S2-P2 chunk C — fix 1: slug fallback scoped to catalyst-review edits (Opus 5, headless)

## §0 Headline
- Fixed the second-review finding (agy) in `EvaluateStage._evaluate`: an open card whose formation md5 is gone now takes its slug's current def ONLY when every formation field matches the def it formed under. The fields allowed to differ are `quality_factors`, `preferred_windows`, `preferred_windows_ref`, `aliases`, `name` and `reference_stats`.
- The original def is read from the formation day's receipts (`definitions_snapshot`, sha256-checked). No new storage.
- If a formation field changed, a snapshot fails its hash check, or the def is missing, the card gets the existing loud `no longer loaded — not refreshed` refusal plus the reason. It is never refreshed from the new def.
- Suite green: `1534 passed, 282 skipped`. Not committed. ESCALATE: 0.

## Files changed
| File | Change |
|---|---|
| `src/cobalt/radar/evaluate.py` | New `CATALYST_REVIEW_FIELDS` and `formation_changes(original, current)`. New `EvaluateStage._formation_definition(card, pool_key)`, which reads the def from `card_store.receipts_for_day` by the card's formation ET date, checks the hash, and keeps found defs in `_formation_defs`. The refresh loop's slug fallback is gated on this. Both new names added to `__all__`. |
| `tests/cobalt/radar_p2_support.py` | `FakeCardStore.receipts_for_day`, a copy of the real `CardStore.receipts_for_day` (`src/cobalt/cards/store.py:1028`). The fallback now calls it, so the in-memory store must have it. This is test support, not a hub-cut fixture. It is the only file changed beyond the one the brief named. |
| `tests/cobalt/test_radar_catalyst_dot.py` | Two new tests (below) and `import pytest`. The existing tests are unchanged. |
| `docs/40 - DevDocs/cobalt/radar/evaluate.md` | One dated paragraph on this fix. |

## Tests added
| Test | Proves |
|---|---|
| `test_a_catalyst_only_edit_refreshes_from_the_formation_def_stored_in_the_receipt` | Safe case: the stored-def memo is cleared first, so the original def must come from the receipt. A catalyst-only edit still refreshes card 1 with no refusals. |
| `test_a_formation_field_edit_under_the_same_slug_is_refused_never_adopted[preconditions]` | Unsafe case: `refreshed == []`. A refusal names card 1, contains `no longer loaded` and `preconditions changed since formation`. The card's dots are untouched and no catalyst dot was added. |
| `…[trigger]` | Same checks, with `trigger changed since formation`. |
| `…[stop]` | Same checks with `stop changed since formation` (the stop's placement ref was edited). |

The existing R2-4 tests (`test_radar_catalyst_dot.py`, 4 tests) and the card-refresh tests in `test_radar_evaluate.py` all pass.

## Suite result (verbatim tail)
```
uv run pytest -q tests/cobalt tests/taxonomy
1534 passed, 282 skipped, 15 warnings in 36.69s
```

## Could not do / notes
- **Red run not executed.** I wanted to swap `HEAD`'s `evaluate.py` back in and run the new tests against it, but the command needed approval and I did not get it. On `HEAD` the fallback takes any def under the slug, so the card would refresh (`refreshed == [1]`) and all three unsafe tests would fail their `refreshed == []` check. That is reasoned from the code, not observed. The one red run I did observe was the existing R2-4 tests failing on the missing `FakeCardStore.receipts_for_day` before I added it. The hub should run the red proof if it needs one (L35).
- **Behaviour change, as the brief intended:** a formation def stored in no receipt of its formation day is now refused instead of silently adopted. That happens when the run that formed the card failed before writing its receipt and no later receipt that day held the md5.
- The DB-backed `CardStore.receipts_for_day` was not exercised here: no DB (L41 interim). The requires_db tests skip offline.
- `id` (the slug) is compared as a formation field. It always matches, because the lookup is by slug.
