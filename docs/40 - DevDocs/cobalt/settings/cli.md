# `src/cobalt/settings/cli.py`

## What it does
`cobalt settings load --from <dir> | --from-git <commit>
--dry-run|--apply` and `cobalt settings show`.

## Key behaviour
- Exactly one of `--from` / `--from-git`, and exactly one of
  `--dry-run` / `--apply`. No defaults: one of them changes what every
  card is sized on.
- Prints a per-setting diff (db value vs file value) before doing
  anything.
- `--apply` is market_reset gated (`assert_writable`) — re-typing a sheet
  dollar is a trading-logic change. `--dry-run` is not: seeing what WOULD
  change during the window is exactly when you want to.
- After applying it RE-READS the rows and asserts
  `from_db() == the seed` before claiming success.

## `--from-git`, and why it exists
`configs/cobalt/aset.yaml` and `daymode.yaml` left the repo in the same
sprint. A LIVE seed therefore reads them at a revision:
`cobalt settings load --from-git <deletion commit>^ --apply`. Same
recovery pattern the taxonomy migration uses for its own deleted inputs.

## Gotchas
`cobalt settings show` prints every row with its `source` and date, then
the RESOLVED objects — a row that parses but does not resolve is worth
seeing as both.
