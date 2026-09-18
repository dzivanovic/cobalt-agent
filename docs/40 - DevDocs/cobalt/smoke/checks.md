# `src/cobalt/smoke/checks.py`

One evaluator per check kind, the run's variables, and the exact hand command each check prints.

## `SmokeDeps`
- One field per collector: `read_rows`, `launchctl_print`, `launchctl_loaded`, `http_get`, `read_text`, `run_cli`, `job_specs`, `drc_note_path`, `missed_grace`.
- Tests pass fakes. `default_deps(prod=)` is the only place the real collectors are named:
  - `read_rows` is `db_query.read_rows`, the `cobalt db query` read path.
  - `launchctl_print` is day-open's; `launchctl_loaded` is `jobs.watchdog.launchctl_status(label).loaded`.
  - `http_get` is a urllib GET; a 4xx/5xx comes back as an answer, not an error.
  - `run_cli` is `uv run <argv>` in the repo root.
  - `load_job_specs()` reads the registry.
  - `drc_note_path` = resolved vault / `prefill.yaml` `review_dir` / `drc_filename_pattern`, the same two values prefill-drc and the replay line use.
  - `missed_grace` reads the `jobs.missed_grace_min` tunable.

## Context
- `last_trading_day(now, anchor_spec, calendar)`: the latest NYSE trading day whose anchor-job occurrence (`schedule.at` ET) plus that job's `timeout_s` has passed by `now`. It walks back at most 14 days.
  - With `com.cobalt.replay` (21:10 ET, 1800 s): 21:50 gives today, 21:20 gives the previous trading day, and holidays are skipped.
- `build_context(now=, report_date=, cutoff=, prod=, anchor_spec=, tunables=)` returns a `SmokeContext`:
  - `session` comes from the session clock.
  - `last_summary_slot`/`last_summary_date` is the latest `heartbeat.summary_at` slot at or before now, or yesterday's last slot before the first one. It uses `heartbeat.runner.summary_at` (the same parser the heartbeat uses).

## Rendering
Variables render as **SQL literals** (`sql_literal`), not bind parameters. The printed hand command must be byte-for-byte the statement that ran, and `cobalt db query` takes no parameters.
- `DATE '…'`, `TIMESTAMPTZ '…'`, numbers bare, `true`/`false`, `NULL`.
- Strings are single-quoted with `'` doubled.
- Every value is typed context, never free input.

The rendering helpers:
- `render_sql` renders SQL.
- `render_text` renders URLs, paths, argv and dotted result paths.
- `_resolve` turns a whole-string `{variable}` predicate value into its typed value.

## Comparison
- `same(actual, expected)`:
  - Numbers compare by value (`Decimal`).
  - A bool matches only a bool.
  - Dates compare as their ISO text, so a JSONB `"2026-09-22"` equals `{last_trading_day}`.
  - Everything else compares as text.
- `holds(pred, row, ctx)` applies one `Predicate`; a column the query did not return raises, which surfaces as ERROR.

## Commands (`command_for`) — the hand fallback, R6 A / Astra R1-24
| Kind | Command |
|---|---|
| sql | `uv run cobalt db query --side <side> [--prod] --format json '<rendered SQL>'` (prefixed by the `to_regclass` probe when `requires_relation` is set) |
| job_row | the same, `--side system`, `SELECT label, state, exit_code, started_at, finished_at, updated_at, registered_at, last_result FROM cobalt_jobs WHERE label = '<label>'` |
| launchctl | `launchctl print gui/$(id -u)/<label>`, or `launchctl list \| grep com.cobalt.` for `registry_match` |
| http | `curl -s -o /dev/null -w '%{http_code}' <url>` (+ `curl -s <url> \| grep -F <needle>`) |
| log_grep | `tail -r <path> \| sed -E '/<block_start>/q' \| grep -E <pattern>` (newest block), else `grep -E <pattern> <path>` |
| vault_unit | `grep -n -F -e '<!-- cobalt:section S -->' -e '<!-- cobalt:unit U -->' <note path>` |
| cli | `uv run <argv>` |

## Evaluation
`evaluate(check, ctx, deps)` never raises. Any exception becomes ERROR with its class and message: a broken probe is not a finding. `run_suite` evaluates every check in file order.

- **launchctl**
  - `running`: PASS when `state = running` with a pid.
  - `registry_match`: FAIL names every enabled label that is not loaded and every `enabled: false` label that is loaded.
- **sql**
  - `side` is a Postgres role: `read_rows` SET ROLEs to it and asserts `current_user`, so a relation the role was never granted is a permission-denied ERROR, not a FAIL. A cross-side read is therefore split into one check per side (K8.1/K8.2), never granted across — see `config.md`'s tenancy-wall section.
  - The `requires_relation` probe runs first; an absent relation is FAIL naming it (K5.1: P2 not deployed = FAIL), and the main query never runs.
  - More than one row is ERROR; no row is FAIL.
  - When every `known_if` predicate holds, the check is KNOWN with `known_text`. Otherwise the `expect` predicates grade it:
    - Any failing predicate whose value is not in its `known` list makes the check FAIL.
    - Otherwise, a failing predicate whose value is listed makes it KNOWN.
    - PASS only when every predicate holds.
- **job_row**
  - No row is FAIL. Otherwise it checks `state`, `exit_code` and `updated_at` age.
  - `not_missed` uses `jobs.watchdog.is_missed(spec, row, now_et, grace)`, the same arithmetic as the heartbeat archiver probe. So K13 is cadence-aware with no flat 30 h cutoff (Astra R1-24).
  - `result_keys`, `result_equals` (dotted path into `last_result`) and `result_positive` (> 0) check the run's result.
- **http:** status and every `contains` needle.
- **log_grep**
  - With `block_start`, only the text from the last matching line on is searched. No such line is ERROR.
  - PASS when "a match exists" equals `present`.
- **vault_unit**
  - The note path comes from the check's `day` variable.
  - Absent note is FAIL, and nothing is created.
  - A `MarkerError` is ERROR; a missing section or unit is FAIL.
  - `raw` is the section text.
- **cli:** the exit code against `exit_code`; `raw` is the last 40 output lines.
