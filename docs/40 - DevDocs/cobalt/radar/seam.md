# `src/cobalt/radar/seam.py`

## What it does
Closed Pydantic payloads for the two JSONB columns of `system.radar_score` (0006): `detail` (`RadarScoreDetail`) and `desk_shadow` (`DeskShadow`). The table sits on the SYSTEM side, and system never holds user data (L32, ADR-0008), so these columns are written only through these models (Astra R1-1).

## Key functions/classes
- `validate_atom(atom)` accepts a relation or qualifier word, or a bare anatomy reference that re-parses through `taxonomy.predicate` to exactly itself, with no `cfg()`, quoted string or free words anywhere inside. Anything else raises.
- `AtomOutcome` is one atom's value this run. `value_kind` names exactly one filled slot: boolean, number, symbol (one lowercase identifier) or a closed `UnavailableReason`.
- `SeamObservation` is a named number with its bar timestamp.
- `RadarScoreDetail` holds atoms, `missing_atoms`, observations, `extension_path` (`A` lands cards, `B_only` is logged, R4) and `formed_bar_ts`.
- `DeskShadowEntry` holds a grade from 1 to 10 OR a closed N/A reason (`DESK_NA`, `CHECKPOINT_MISSING`, `DEFAULT_UNRULED`), plus a WHY *code* and a formula version. `DeskShadow` holds the three desk dots.

## Gotchas
The models forbid unknown keys and are frozen. The database only checks that the columns are JSON objects; the closure lives here. WHY prose, per-trade thresholds and settings content belong to the user side (`card_dots`, `radar_score_receipt`). `test_radar_score_carries_no_trade_def_content` asserts that a valid payload cannot express them.

**2026-09-21 — X11 (setups one build STEP-3).** The closed `UnavailableReason` gains two values. `insufficient_seed` (FINAL §5 [F-14]) is used when a seeded indicator has fewer than `period` premarket buckets and a too-short RTH run. `slope_norm.bars_unset` is used when the `A-11` row is null. X11 was run on the start code: it constructed an `AtomOutcome` for every planned D1 atom × reason, and exactly these two failed validation. Each is a named reason, not free text. Every D1 atom spelling already validated as a bare atom.
