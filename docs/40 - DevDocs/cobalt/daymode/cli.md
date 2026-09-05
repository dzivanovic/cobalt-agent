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
- `attest` refuses an `.htk` filename not declared in
  `configs/cobalt/daymode.yaml`, and says plainly that the file is
  attested, not read.
