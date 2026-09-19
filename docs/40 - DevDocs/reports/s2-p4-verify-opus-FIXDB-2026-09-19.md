# S2-P4 FIX-DB — the three dev-DB reds (tests only)

## §0 Headline

Both reds fixed in tests only; `src/`, `configs/`, migrations and fixtures untouched.
Red 1 (2 params): `_probe`'s wall-clock `seconds` was inside a whole-dict equality → equality now on content (`schema`, `rows`, `digest`).
Red 2: `fill()` returns `FillResult`, not a list → assert on `result.transition_ids`.
Offline suite green: **1796 passed, 324 skipped, 1 xfailed, 15 warnings in 55.11s**.
ESCALATE: 0. Not committed (as instructed). Only the hub's DB run can turn these 3 skips green.

## Changes

| # | File:line | Before → after | Why the intent is preserved |
|---|---|---|---|
| 1a | `tests/cobalt/test_p4_migrations.py:257` | *(new)* `_content(probe)` helper — returns the probe dict with `seconds` dropped, every other key kept | Drops by exclusion, not by whitelist: a key added to `_probe` later is still compared, so the helper cannot silently narrow the proof. Docstring states `seconds` is a deploy-plan deliverable, not a fact of this test. |
| 1b | `test_p4_migrations.py:307` | `before = _probe(conn, "radar_membership")` → `before = _content(_probe(conn, "radar_membership"))` | `before` still carries `schema`, `rows`, `digest`; lines 320/325 read `before["digest"]` unchanged. |
| 1c | `test_p4_migrations.py:310` | `assert before["rows"] and before["rows"] > 0` → `… and before["digest"]` | Added, not loosened: proves both facts the equalities below rest on are really in the dict, so an "unchanged" assertion can never pass vacuously if `_probe` renames a key. |
| 1d | `test_p4_migrations.py:313` (second apply, idempotence) | `assert _probe(…) == before` → `assert _content(_probe(…)) == before` | Still one equality over `digest` **and** `rows` (and `schema`). The only thing no longer compared is the stopwatch reading that produced the red (`0.0012291669845581055 != 0.0017267910297960043`). |
| 1e | `test_p4_migrations.py:317` (`p4_before_p2` re-apply after P2's columns land) | same change as 1d | same |
| 2 | `tests/cobalt/test_radar_cards_db.py:223-226` | `ids = cards.fill(card_id, actor=Actor.YOU)` / `assert len(ids) == 2` → `result = cards.fill(…)` / `assert len(result.transition_ids) == 2` | Same claim, same number: a manual card filled from ARMED writes two transition rows. Count unchanged (2), only the accessor corrected to R1-5's `FillResult.transition_ids` (`src/cobalt/cards/models.py:164`). `store.fill`'s manual route from ARMED is `route[:-1]` (TRIGGERED, actor=cobalt) + FILLED = 2, matching `tests/cobalt/test_cards.py:739-741`, which already asserts 2 on the same shape. |

Lines 320 and 325 (`assert _probe(…)["digest"] == before["digest"]`, after reverse and after reapply) were already field-wise and already green — left exactly as written. Raising them to full-content equality would assert something I cannot run here, so it is not done silently; call it if you want it.

## Sweeps the brief asked for

| Sweep | Result |
|---|---|
| Whole-dict `_probe` equality elsewhere in `test_p4_migrations.py` | None. The module's only `_probe` uses are the 5 lines above. |
| Whole-dict `_probe` equality in other `requires_db` tests | None. `test_tenancy.py:537-542`, `test_migrate_proof.py:776-778 / 812-819 / 1187-1190 / 1233-1243` all compare `["rows"]`/`["digest"]` field-wise or go through `cli._verdict`. `test_migrate_proof.py:195` asserts `seconds` deliberately (`isinstance(float)`, `>= 0.0`) — correct, untouched. |
| `grep -rn "\.fill(" tests/` treating the return as a list | One only — the line fixed. `test_cards.py:716,739` already chain `.transition_ids`; `test_cards_picks.py` (10 sites) uses `result.pick_recorded` / `.pick_id` / `.transition_ids` / whole-`FillResult` equality. |

## Verification

Offline suite, verbatim final line:

```
1796 passed, 324 skipped, 1 xfailed, 15 warnings in 55.11s
```

(`uv run pytest -q tests/cobalt tests/taxonomy`, no `COBALT_ENV`, no DB env — the `requires_db` tests skip.)

Both targets collect and skip cleanly rather than erroring:

```
SKIPPED [2] tests/cobalt/test_p4_migrations.py:293: requires_db: Postgres env settings not available
SKIPPED [1] tests/cobalt/test_radar_cards_db.py:202: Postgres env settings not available
```

**What I proved:** the edited modules import, collect and run; nothing else in `tests/cobalt`/`tests/taxonomy` regressed; the accessor `result.transition_ids` exists on `FillResult` and the `== 2` count is the one `store.fill`'s ARMED→FILLED manual route produces.

**What only the hub's `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy` can confirm:** that the three skips actually go green — i.e. that `_content(_probe(…)) == before` holds on real `cobalt_dev` rows across second-apply and the `p4_before_p2` re-apply (the content claim itself was never in question; the red was only the timing key), and that `test_manual_cards_are_unaffected` reaches its fill at all after `record_stop_edit` / `transition`.

**Scope:** no `src/`, `configs/`, migration, fixture or dependency change; no assertion weakened; nothing committed; nothing launched (L36). L52 not engaged — no scoring or ranking logic is touched.
