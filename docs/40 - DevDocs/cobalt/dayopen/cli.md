# `src/cobalt/dayopen/cli.py`

```
cobalt day-open [--date YYYY-MM-DD] [--json]
cobalt day-open verdict "<one line>"
```

The bare command runs `runner.run()`, writes the report (never over an
existing one — a second run the same date lands as
`day-open-<date>-<HHMMSS>.md` with a `NOTE:` line; a refused write exits 1
with `FAILED:`), and prints the VERDICT table. `--json` prints the same
content as JSON and writes nothing to disk. `verdict` is
an optional subparser alongside the parent's own `--date`/`--json`
flags — argparse resolves `day-open` (no further tokens or flags only)
to `cmd_run` and `day-open verdict ...` to `cmd_verdict` without either
path's arguments leaking into the other. `verdict` always targets
TODAY's ET date; there is no `--date` override for it.
