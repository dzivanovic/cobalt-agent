# `src/cobalt/dayopen/cli.py`

```
cobalt day-open [--date YYYY-MM-DD] [--json]
cobalt day-open verdict "<one line>"
```

The bare command runs `runner.run()`, writes the report, and prints the
VERDICT table (or the same content as JSON with `--json`). `verdict` is
an optional subparser alongside the parent's own `--date`/`--json`
flags — argparse resolves `day-open` (no further tokens or flags only)
to `cmd_run` and `day-open verdict ...` to `cmd_verdict` without either
path's arguments leaking into the other. `verdict` always targets
TODAY's ET date; there is no `--date` override for it.
