# `src/cobalt/radar/cli.py`

Registers the `radar` CLI group: config check, throttle probe, resident/one-shot scans, replay building, source inspection, and HITL proposal/apply subcommands.

`radar lists propose` requires `--watchlists-yaml`; there is no working-tree default after the migration source's retirement.

`radar screens validate --pool-block FILE` is the offline prose/pool/Lists/budget/drift gate. Before Lists installation it defaults prospective input to `configs/cobalt/watchlists.yaml`; callers on a post-switch tree can supply the pinned historical file with `--watchlists-yaml`.

`radar evaluate` (S2-P2) takes exactly one of `--replay <date>` (the dry run, writes nothing) or `--candidate <date>` (the cobalt_dev persistence harness; needs `--settings-file` + `--sha256`, optional `--taps`). Either may add `--trade-def <slug>`. The body is `evaluate_cli.evaluate_command`, imported lazily.

`radar audit-export` (S2-P2 STEP-11) takes exactly one of `--run <id>` or `--replay <date>` (an argparse mutually exclusive group) and a required `--out <dir>`; `--trade-def` narrows a replay only. Arguments come from `audit_export.add_arguments`, the body is `audit_export.command`.
