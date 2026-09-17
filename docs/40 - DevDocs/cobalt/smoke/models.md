# `src/cobalt/smoke/models.py`

The Pydantic shapes `cobalt smoke` loads and renders (L10: one schema per
config family, validated on load).

## Verdicts
`Verdict`, `Overall` and `overall_verdict` are re-exported from
`cobalt.dayopen.models`, so there is one roll-up (L3):
- RED if any check is ERROR.
- AMBER if any check is FAIL.
- GREEN otherwise. KNOWN never lowers it.
- An empty list raises, because nothing was checked.

## Variables
- `VARIABLES`: `now`, `report_date`, `session`, `cutoff`, `last_trading_day`, `last_summary_slot`, `last_summary_date`.
- `{tunable:<key>}` is the one parameterised form.
- `VAR_RE` finds them. `variables_in(text)` raises on an unknown name, so a typo fails at load with its line, never at 21:50 on the close evening.

## `Predicate`
- One comparison over a column of the check's single row: `column`, `op` (`Op`: eq/ne/lt/le/gt/ge/in/not_in/is_null/not_null), `value`, `known`.
- `value` may be a literal or a `{variable}`. The validator enforces the shape: null ops take no value, `in`/`not_in` take a list, and every other op needs one.
- `known` lists actual values that turn a FAILING predicate into KNOWN. Every committed list starts empty and gains an entry only by ruling.

## Check kinds (discriminated on `kind`)
Every kind carries `id` (`K<n>` or `K<n>.<m>`), `title` and `expect_text`. `expect_text` is the exact expected output that Astra R1-24 requires beside each command.

| Kind | Fields | Read-only by construction |
|---|---|---|
| `LaunchctlCheck` | `mode` `running` (needs `label`) or `registry_match` (no label) | `launchctl print` / `launchctl list` |
| `SqlCheck` | `side`, `query`, `expect`, `known_if` + `known_text` (together or neither), `requires_relation` | `query` must pass `db_query.guard_select` at load |
| `HttpCheck` | `url`, `status`, `contains` | GET |
| `LogGrepCheck` | `path` (repo-relative, no `..`), `block_start`, `pattern` (compiled at load), `present` | file read |
| `JobRowCheck` | `label`, `state`, `exit_code`, `not_missed`, `max_age_min`, `result_keys`, `result_equals` (dotted path → value, variables allowed in both), `result_positive`; must expect something | one `cobalt_jobs` row through the read path |
| `VaultUnitCheck` | `note` (`drc`), `day`, `section`, `unit` | text read + `find_section` |
| `CliCheck` | `argv`, `exit_code` | `argv` must start with a prefix in `READ_ONLY_CLI` |

`READ_ONLY_CLI` is `(("cobalt", "validate"),)`. Each exclusion was checked in the code:
- `cobalt jobs check` and `cobalt heartbeat show` both sweep and stamp job rows.
- `cobalt cards picks` runs `ensure_schema`.

## `SmokeSuite`
`suite`, `title`, `day_anchor_job` (the one-shot whose finished occurrence
defines `{last_trading_day}`) and `checks` (at least one, ids unique).

## `SmokeContext`
- Holds the run's variables plus `prod` and `tunables`.
- `now` and `cutoff` must be timezone-aware.
- `printable()` is the block at the top of every report, so each rendered command can be replayed from the file (L57).

## `CheckOutcome` / `SmokeReport`
- `CheckOutcome`: `id`, `title`, `kind`, `verdict`, `detail`, `command`, `expected`, `raw` (verbatim evidence).
- `SmokeReport`: `suite`, `title`, `context`, `generated_at`, `checks`, `overall`.
