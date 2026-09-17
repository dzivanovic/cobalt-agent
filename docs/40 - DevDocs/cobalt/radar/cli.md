# `src/cobalt/radar/cli.py`

Registers the `radar` CLI group: config check, throttle probe, resident/one-shot scans, replay building, source inspection, and HITL proposal/apply subcommands.

`radar lists propose` requires `--watchlists-yaml`; there is no working-tree default after the migration source's retirement.

`radar screens validate --pool-block FILE` is the offline prose/pool/Lists/budget/drift gate. Before Lists installation it defaults prospective input to `configs/cobalt/watchlists.yaml`; callers on a post-switch tree can supply the pinned historical file with `--watchlists-yaml`.
