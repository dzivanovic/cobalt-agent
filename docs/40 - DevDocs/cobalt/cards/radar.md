# `src/cobalt/cards/radar.py`

## What it does
The radar card's creation spec, the owner badge of every card field, and the ladder order (S2-P2 STEP-4/6; Astra R1-7, R1-15). Pure.

## Key functions/classes
- `RadarCardSpec` is everything the one radar creation path (`CardStore.create_radar_card`) writes for a new unsized WATCH card: formation evidence, deadline, WHY, seam id, hashes, the first score values, dots and genesis evidence.
  - Refuses a stop on the wrong side of the trigger, a deadline at or before formation, and naive timestamps.
  - `entry`/`stop` start equal to `trigger_price`/`structural_stop`.
- `FIELD_OWNERS` gives every column of `"user".radar_cards_v` one badge from `OWNER_BADGES`:
  - `COBALT`: the engine wrote it;
  - `YOU`: his tap or edit decides it (`stop`, `tapped_grade`, `conviction`, `promoted_at`, `account_mode`);
  - `LEDGER`: `state`/`state_at`, owned by the actor of the last transition.
  `test_every_card_field_is_badge_owned` parses the view SQL against this map.
- `ladder_order(entries)` returns `LadderOrder` (`active`, `terminal`), each position carrying a rank chip, pinned flag and promoted flag:
  - pinned (ARMED/TRIGGERED/FILLED) first, by pool position (nulls last), score desc (nulls last), ticker, id;
  - WATCH by card_score desc NULLS LAST, pool position, ticker, id; the rank chip is the place in this order;
  - at most one promoted WATCH card moves to #2, or just below two or more pinned cards, and is never moved down; its rank chip is unchanged;
  - release restores the natural order.

2026-09-16 (chunk C): the view gained `last_price` and `pool_position` (the membership's `last_rank`) for the panel; both are `COBALT`. The panel's `RadarCardRow` refuses to import if its columns and `FIELD_OWNERS` disagree.

## Gotchas
Two price representations, named (R1-7): `trigger_price`/`structural_stop` are immutable formation evidence, read by replay and audit. `entry`/`stop` are the live sizing inputs, read by key taps, proximity and stop-touched expiry.
