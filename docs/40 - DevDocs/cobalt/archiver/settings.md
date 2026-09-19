# `src/cobalt/archiver/settings.py`

New 2026-09-19 with the append-only redesign (chunk S). Spec:
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §10.

## What it does
Resolves the Bar Archiver's seven engine tunables into ONE validated
Pydantic model, `ArchiverSettings`. The rows live in
`configs/cobalt/taxonomy/tunables.yaml` — the same registry that already
carries `radar.scan_interval` and `radar.poll_overlap_bars` — and are
read through `cobalt.taxonomy.loader.load_tunables()`. There is no
second YAML reader in this module and a test asserts there never is
(L3).

The one that matters is `archiver.write_mode`. It selects the nightly
write path: `upsert` is today's behaviour byte for byte (the whole
export through `ON CONFLICT DO UPDATE`), `append` is the design's night
(only bars that do not exist are inserted; no stored row is rewritten).
**The repo ships `upsert`.** Switching is the owner's ruling on the
shadow numbers (L7), taken as a reviewed commit to that row — a test
pins the shipped value so the flip cannot happen by drift.

## Key functions/classes
- `WriteMode` — `upsert` | `append`. A `str` enum, but the model's
  validator does the accepting, not the enum: `Append`, `APPEND`,
  `" upsert"`, `""`, `both` and a non-string are all REFUSED with a
  message naming `archiver.write_mode`. No `strip()`, no `lower()`.
- `ShadowCompare` — `on` | `off`, same strictness.
- `ARCHIVER_TUNABLE_UNITS` — the seven keys and the `TunableUnit` each
  must carry. The unit check is load-bearing: a `min` row read as a
  `count` turns a ten-minute quiet window into ten of something else.
- `RepairSettings` — `quiet_before_open_min`, `quiet_after_cycle_min`,
  `cycle_max_min`; each a positive integer (`bool` is not an integer
  here and `"10"` is not a number — a quoted YAML value is a hand edit,
  and coercing it hides that).
- `ArchiverSettings` — the five fields above plus the two shadow counts.
  `extra="forbid"`, `frozen=True`.
  - `.shadow_enabled` — whether tonight writes a shadow artifact:
    `write_mode is upsert AND shadow_compare is on`. In `append` the
    comparison IS the gate (§5), so the key is ignored there rather than
    doubling the read.
- `load_archiver_settings(registry=None)` — the loader. `registry` is a
  TEST seam (the `by_key` mapping); production passes nothing.
- `validate_command_lines()` — the lines `cobalt validate` prints for
  this family (L10). A list of strings rather than `print` calls, so
  the gate is testable without running the whole F16 sweep (which reads
  the vault). `cobalt validate` calls it after the heartbeat block.

## Data flow in/out
**In:** `configs/cobalt/taxonomy/tunables.yaml`, via the taxonomy
loader.
**Out:** one frozen `ArchiverSettings`, or `ArchiverSettingsError`.
Consumers: `cobalt.archiver.runner` (dispatch on `write_mode`),
`cobalt.archiver.shadow`, `cobalt.archiver.quiet`, `cobalt validate`.

## Config it reads
The seven `archiver.*` rows of `tunables.yaml`:

| key | unit | ships | status |
|---|---|---|---|
| `archiver.write_mode` | label | `upsert` | solidified by the FINAL design |
| `archiver.shadow_compare` | label | `on` | proposed |
| `archiver.shadow_statement_timeout_s` | count | 10 | proposed |
| `archiver.shadow_retention_nights` | count | 30 | proposed |
| `archiver.repair.quiet_before_open_min` | min | 10 | the desk's number (`cto-2026-09-19.md §16 / R8`) |
| `archiver.repair.quiet_after_cycle_min` | min | 5 | the desk's number (same citation) |
| `archiver.repair.cycle_max_min` | min | 30 | proposed (spec O-2) |

## Gotchas
- **Every refusal names the TUNABLES key, not the model field.** Pydantic
  reports `write_mode`; an operator needs `archiver.write_mode`.
  `_name_the_keys()` does that mapping in one place rather than through
  validation aliases, so the nested `repair.*` rows read the same way as
  the top-level ones.
- **A missing row is a crash, never a default** (L1, L10). A defaulted
  write mode is the single failure this design exists to make
  impossible.
- **`cycle_max_min` is an ESTIMATE, and a recorded dissent.** The radar
  stamps a cycle's START into `system.radar_pool.last_scan_at` and
  persists its completion nowhere, so the quiet window derives "the
  cycle has finished" from start + this bound. Gemini and Astra both
  dissented on exactly that (spec §13); spec O-2 carries the
  alternative (the radar stamping a completion instant), which touches
  the live radar's write path and is NOT in this build.
- `shadow_compare` is read but ignored in `append` mode. Read
  `.shadow_enabled`, never the raw field, when deciding whether to run
  the comparison.
