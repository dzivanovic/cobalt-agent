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
- `render_text` renders paths, argv and dotted result paths.
- `render_url` (S2 smoke fix F2, 2026-09-23) renders a `kind: http` URL, for BOTH the probe and the printed hand-fallback `curl`: each substituted variable's text is percent-encoded with `urllib.parse.quote(…, safe="")`, the template's own text is left alone. It exists because K4.4 now passes the deploy cutoff as `/api/radar/pool?since={cutoff}` — the endpoint requires `since` (P3 plan R2-1: missing, malformed, naive or future values are rejected, never defaulted), and an unencoded ISO instant's `+00:00` would reach the server as a space and be rejected again. A URL with no variable renders byte for byte as before.
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
| compare | `# compare <left> <op> <right> — run both rows above; their two printed numbers must be <op>` |

The compare line is the one entry that is not a command, because that row runs no probe. It is still the hand fallback: it names the two ids and the operator, and the two rows it names print the numbers themselves.

## Evaluation
`evaluate(check, ctx, deps, results=None)` never raises. Any exception becomes ERROR with its class and message: a broken probe is not a finding. `run_suite` evaluates every check in file order, keeping each outcome by id as it goes and passing that map into the next `evaluate` — which is what a `compare` row reads. One pass, no source read twice.

- **launchctl**
  - `running`: PASS when `state = running` with a pid.
  - `registry_match`: FAIL names every enabled label that is not loaded and every `enabled: false` label that is loaded.
- **sql**
  - `side` is a Postgres role: `read_rows` SET ROLEs to it and asserts `current_user`, so a relation the role was never granted is a permission-denied ERROR, not a FAIL. A cross-side read is therefore split into one check per side (K8.1/K8.2), never granted across — see `config.md`'s tenancy-wall section.
  - The `requires_relation` probe runs first; an absent relation is FAIL naming it (K5.1: P2 not deployed = FAIL), and the main query never runs.
  - More than one row is ERROR; no row is FAIL.
  - `result_number`, when the check declares one, is read off the returned row and carried on the outcome for a `compare` row. It never changes this check's own verdict — a column that is absent or not a number simply leaves `number` as `None`, and the compare that wanted it is the row that goes loud.
  - When every `known_if` predicate holds, the check is KNOWN with `known_text`. Otherwise the `expect` predicates grade it:
    - Any failing predicate whose value is not in its `known` list makes the check FAIL.
    - Otherwise, a failing predicate whose value is listed makes it KNOWN.
    - PASS only when every predicate holds.
- **job_row**
  - No row is FAIL. Otherwise it checks `state`, `exit_code` and `updated_at` age.
  - `not_missed` uses `jobs.watchdog.is_missed(spec, row, now_et, grace)`, the same arithmetic as the heartbeat archiver probe. So K13 is cadence-aware with no flat 30 h cutoff (Astra R1-24).
  - `result_keys`, `result_equals` (dotted path into `last_result`) and `result_positive` (> 0) check the run's result.
  - `result_number` is the dotted `last_result` path that IS this check's number, read the same way and with the same rule: it grades nothing here (K8.1's missing `card_misses` stays a FAIL through `result_keys`, not an ERROR).
- **compare**
  - Reads no source. It looks up the outcomes of `left` and `right` in the map `run_suite` threads through, and grades their `number`s with `COMPARE_OPS[op]` (`eq` today).
  - Equal → PASS. Unequal → FAIL. An operand that ERRORed → ERROR naming it, never a quiet PASS: nothing ran, so nothing was compared. An operand with no number (the key was absent, or the value was text) → ERROR naming it and its kind.
  - Both operands are printed in `detail` and in `raw` whatever the verdict, so the comparison replays from the report alone (L57).
  - Evaluating one outside `run_suite` — no results map — raises, and so reports ERROR. The schema already forbids the file-level version of that mistake.
- **http:** status and every `contains` needle.
- **log_grep**
  - With `block_start`, only the text from the last matching line on is searched. No such line is ERROR.
  - PASS when "a match exists" equals `present`.
- **vault_unit**
  - The note path comes from the check's `day` variable.
  - Absent note is FAIL, and nothing is created.
  - A `MarkerError` is ERROR; a missing section or unit is FAIL.
  - `raw` is the section text.
  - **The DRC note (`note: drc`, DRC D3-6, 2026-09-29, `[F-25]` / R103 O18).** The day's DRC event decides first, read-only on the USER side (`DRC_EVENT_SQL`: the event of the day's CURRENT trading-log import, else of its current `no_trade` statement — `DrcStore.event_for`'s rule). No event → KNOWN `pending — no DRC event for <day>` (no DRC is his lawful choice, R66). `failed`, or a build left `pending` / `running` → FAIL naming the state and its error. `done` → the note and the unit's markers as above. Nothing requires the note at 15:41. No new check kind: the conditional lives in this evaluator. K10.2 (a `sql` row in `s2.yaml`) carries the same event read with `known_if: event_state is_null`.
  - **An absent DRC relation is FAIL, never ERROR (DRC D3-9, 2026-09-29, R32 / R33).** `requires_relation` is checked by ONE helper, `_relation_absent`, that both `_sql` (on `check.side`) and `_vault_unit` (FIRST in its DRC branch, on `"user"` — the side `_drc_event` reads) call: `to_regclass` answers not-present → FAIL `relation <name> does not exist`, and nothing else is read (no main / event query, no note). K10.1 and K10.2 declare `requires_relation: user.drc_events` — `0019`'s table, whose foreign keys name `drc_imports` and `drc_stated_books`, so its presence proves all three K10 reads. Before the DRC deploy's migrate step (and on `cobalt_dev`, where the DRC migrations are never left applied — L76) K10.1 / K10.2 are FAIL naming the relation, not ERROR. `command_for`'s `vault_unit` branch prefixes the relation's hand command with ` && `, as the `sql` branch does (R6 A). Any new smoke row that reads a `drc_` relation declares the same guard (`test_every_committed_drc_read_declares_the_drc_events_guard`).
- **cli:** the exit code against `exit_code`; `raw` is the last 40 output lines.

**2026-09-29 — DRC D3 fix r1 (F-2): K10.2 keys on the day's note.** K10.2's `writes` counts the `drc-misses` / `miss_line` rows of `vault_writes` whose `note` EQUALS the stored `note_path` of the same event row that `event_state` selects. There is no `ts` predicate. The old count was of any note's rows whose `ts` fell on the day (ET). The build stamps its writes at clock time, so a miss line written for day D after midnight ET FAILed D. Another note's miss line stamped on D PASSed D. Both paths name the note the same way: `vault_writes.note` is `str(path)`, and `drc_events.note_path` is `str(note)` of the build's return. The 21:10 writer and the build compose that path from the same `load_prefill_paths()` under the resolved vault. `expect_text` now ends `writes >= 1 for the day's DRC note (any clock time)`.
