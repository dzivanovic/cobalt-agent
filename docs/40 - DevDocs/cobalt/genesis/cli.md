# `src/cobalt/genesis/cli.py`

Registers `cobalt genesis import <path>...` (one line per source: `<source> · <n> chunks · sha256 <12 hex>`; a bad path exits 1 through `cobalt.cli`'s `FAILED:` line with nothing written) and `cobalt genesis search <question> --limit <n>` (one line per hit: `<source>:<line_start>-<line_end> · <rank> · <first body line>`), added to `cobalt` by one `genesis_cli.add_parser(sub)` line in `src/cobalt/cli.py`.

## 2026-10-19 — f21-genesis-1013
New module (card 468 G5).

## 2026-10-19 — f21-vectors-1013
Card 469 V5: `cobalt genesis embed` (no argument) → `genesis.embed.run_embed(GenesisStore())`; DEGRADED, a dimension mismatch or a chunk left NULL exits 1 through `cobalt.cli`'s `FAILED:` line.
