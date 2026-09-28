# `src/cobalt/cards/health.py`

## What it does
Health pills for a FILLED radar card (S2-P2 STEP-7). The threshold table is P3's 2026-09-14 R2, copied and not re-ruled, and lives in `tunables.yaml` as eight `card.health.*` rows:

| class | warn | bad |
|---|---|---|
| participation | RVOL vs entry < 0.70 | < 0.45 |
| cost | spread vs entry ≥ 1.5× | ≥ 2.5× |
| dot | graded dot down ≥ 2 | graded dot ≤ 3 |
| structural | stop / EMA9 touched | lost on a closed working-TF bar |

## Key functions/classes
- `HealthThresholds.from_tunables(rows)` reads the eight rows and fails loud on any missing one.
- `EntrySnapshot` is RVOL, spread and the computed dot grades at entry. The S5 stage captures it on the first scan that sees the card FILLED and stores it in `aset_sizings.health` (Astra R1-12).
- `participation_pill` and `cost_pill` compute the ratio against the entry value. A missing or zero baseline, a missing current value, or no spread source gives `n/a` with a loud note, never a fabricated ratio.
- `dot_pills` covers computed dots only; judgment and desk dots are never health-scored (L11).
- `structural_pill(label, *, level, direction, intrabar, closed, t)` goes warn when a bar's extreme touches the level, and bad when a closed working bar's close loses it (long: low ≤ / close <; short mirrored).
- `card_health(...)` returns every class: participation, cost, one pill per computed dot, stop, EMA9 (last bar) and alignment (`n/a`, `DEFAULT_UNRULED`).

## Gotchas
Cobalt has no spread source in S2, so `cost` is `n/a` on every card. The snapshot is taken on the scan after the fill, not at the fill tick; `captured_at` says when. EMA9's convention lives in `radar/anatomy/indicators.ema`.

**2026-09-22 (fix round 3, F4 — R50).** `dot_pills` skips the `assumed_formation` dot (`scoring.ASSUMED_FORMATION`): it has no graded value, so a FILLED card no longer shows an extra `n/a` pill "assumed_formation has no graded value"; the card's ASSUMED mark carries it. Every other dot is unchanged, and the dot itself (on the card, refused on tap, suppressing the score) is untouched — only the health pill list changes.
