# `src/cobalt/settings/card.py`

## What it does
The trader's radar-card settings: five `"user".trader_settings` keys with typed schemas (S2-P2 R7/R9, Astra R1-5).

| key | schema |
|---|---|
| `radar.cards_enabled` | bool, required: the dark-ship switch |
| `card.proposed_key` | `ProposedKeyBands` `{a_plus_min, a_min, b_min, c_min}`, conviction 0–1, strictly descending |
| `card.curves` | `{factor: Curve}`, anchors `[[x, grade], …]`, ≥2, strictly increasing x, grade 1–10 |
| `card.alignment_default` | `AlignmentDefault` `{with_grade, flat_grade, against_grade, flat_pct}` |
| `card.shadow_promotion_bar` | `ShadowPromotionBar` `{sessions, pairs, median_max, within2_min}` |

## The write path
`cobalt settings load --card <file> --sha256 <hash> --dry-run|--apply`

1. The sha256 is taken over the file's bytes and verified before anything parses. `--apply` requires it.
2. The file must have the shape `card_settings: {<key>: <value>, …}` and is the WHOLE card-settings set: a key it omits is deleted.
3. A per-key diff is printed.
4. One `TraderSettingsStore.put(rows, delete=…)`, a single transaction.
5. A round-trip read (`CardSettings.from_rows(db) == file`) runs before success is printed.

A trader-run apply is exempt from the HITL token (L28 amended 2026-09-15).

## Key functions/classes
- `CardSettings.from_rows(rows)` is the runtime reader. It refuses a missing `radar.cards_enabled` rather than defaulting, and refuses `cards_enabled: true` without `card.proposed_key` and `card.curves`. Errors name the ROW key.
- `CardSettings.rows()`, `.snapshot()` and `.sha256()` give the canonical row values and hash (the run's `settings_sha256`).
- `CardSettingsReader.current()` reads the store on every call. The S5 stage and the tap routes use it per cycle/request, so an apply needs no restart.
- `load_card_file(path, *, expected_sha256)` refuses:
  - `card.dot.*` / `card.health.*`: engine tunables (L53);
  - the seven sheet/day-mode keys: they have their own `--from` path;
  - any unknown key.
- `cmd_load_card(args)` is the CLI body, dispatched from `settings/cli.py`.
