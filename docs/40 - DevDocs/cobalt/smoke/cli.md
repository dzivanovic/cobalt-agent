# `src/cobalt/smoke/cli.py`

`cobalt smoke <suite> --cutoff <ISO8601 with offset> [--date YYYY-MM-DD] [--prod] [--json]`
(S2-P4 STEP-9, R6 B). The S2 close runs `cobalt smoke s2`.

- `run(suite_name, *, cutoff, report_date=None, now=None, prod=False, deps=None)`:
  1. Loads the suite (a bad file crashes with its line).
  2. Builds the context from the registry's `day_anchor_job` spec and every tunable.
  3. Runs the suite through `default_deps(prod=)` unless fakes are given.
  4. Returns the `SmokeReport`. `run` writes nothing; `cmd_run` owns the file.
- `cmd_run`:
  - `--json` prints `render_json` and writes nothing.
  - Otherwise it writes the report, prints its path and the numbered table.
  - Exit 0 only when GREEN, 1 on AMBER or RED, so a script cannot read a red smoke as green.
- `--cutoff` is **required** and must carry an offset. It is the P4 deploy instant from the deploy report. K3 and K6 judge only rows at or after it, and a guessed default would silently widen or narrow what they judge (L1).
- `--prod` has `cobalt db query`'s meaning: without it, the production database is refused.
- `add_parser(sub)` is mounted by `cobalt.cli`. `build_parser()` is a standalone parser for tests.

The committed suite is `configs/cobalt/smoke/s2.yaml`: K1–K18, split into
sub-rows (K4.1–K4.4, K5.1–5.2, K10.1–10.2, K11.1–11.3, K12.1–12.2,
K16.1–16.2) so each row carries one exact command.
