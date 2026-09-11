# `src/cobalt/radar/cli.py`

Registers the `radar` CLI group: config check, throttle probe, resident/one-shot scans, replay building, source inspection, and HITL proposal/apply subcommands.

`radar lists propose` requires `--watchlists-yaml`; there is no working-tree default after the migration source's retirement.
