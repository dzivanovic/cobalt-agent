# `src/cobalt/daymode/cli.py`

## What it does
`cobalt daymode` — F6's command surface, mounted by `cobalt.cli`.

| Command | Purpose |
|---|---|
| `show [--date]` | the ladder, the row, and the mode **in force** |
| `propose [--date] [--at] [--dry-run]` | what `com.cobalt.daymode-propose` runs at 09:00 ET |
| `decide --mode M [--reason]` | approve, or overrule (reason required) |
| `attest --file half.htk [--date]` | state which `.htk` is loaded |

## Notes
- `propose` gathers its four inputs via `drc.prior_day_inputs()`, reads
  the band from tunables, and writes **one** row — or reports
  `NOT A TRADING DAY` and writes nothing.
- A **missing** `daymode.trade_count_band.*` tunables row is a config
  error and exits (F16: no built-in default). A **null value** is "not
  ruled yet" and is an adverse signal, not a crash.
- `_band()` then hands both values to `propose.validate_band` — the ONE
  validator, shared with `cobalt validate` (L3). A band that is SET but
  cannot be a band (inverted `min > max`, or a value that is not a whole
  non-negative count — a string, a fraction, a negative, a bool) becomes
  a `BandError`, which `_band()` re-raises as `SystemExit` with the same
  message. In practice the deploy's `cobalt validate` refuses it first,
  which is the point: the refusal happens at deploy time with both keys
  and both values named, not at 09:00 inside
  `com.cobalt.daymode-propose` (L10). A **half-set** band (exactly one
  null) is still accepted and still "not ruled yet" — see `propose.md`.
- `attest` refuses an `.htk` filename not declared in
  `configs/cobalt/daymode.yaml`, and says plainly that the file is
  attested, not read.
