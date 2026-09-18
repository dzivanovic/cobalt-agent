# `src/cobalt/smoke/config.py`

Loads a suite file. L10 requires that a bad file crash with its line number.

- `SUITES_DIR` = `configs/cobalt/smoke/`; `suite_path(name)` → `<name>.yaml`. The new-core config boundary holds: the file is under `configs/cobalt/`, outside the old loader's top-level glob.
- `SmokeConfigError(path, line, message)`: its text is `path:line: message`, and `.line` is 1-based, or None when the file is unreadable.
- `load_suite(path)`:
  - Reads the text once and parses it twice: `yaml.compose` keeps the node tree with its start marks, and `yaml.safe_load` feeds `SmokeSuite`.
  - A YAML syntax error reports the parser's `problem_mark` line.
  - A Pydantic error walks its location (`checks → 3 → sql → expect → 0 → op`) down the node tree:
    - The union tag (`sql`) is skipped, as is any key the file never wrote.
    - The line reported is that of the deepest node found. A missing required field therefore points at the check's own mapping.
  - The message names the first error and counts the rest.
  - A file that is not a mapping crashes at line 1.

## The tenancy wall in a suite file (L32)

A `sql` check's `side` is a real Postgres role: `read_rows` SET ROLEs to
it and asserts `current_user`, so a query that names a relation the role
was never granted does not fail an assertion — it ERRORs on permission
denied, and OVERALL goes RED.

- A check reads its own side freely. It may name the OTHER side's
  relation only where a migration GRANTs that relation to its role.
  Today the one such crossing is `system.movers_daily`, granted to
  `cobalt_user` by `0008_radar_value_movers.sql` for `missed.mover_id`'s
  FK — which is what lets K9 run `side: user`.
- `system.cobalt_jobs` is NOT in that set: it is system-side by
  declaration (`0003`) and was MOVED into `system` by `0002`'s
  `ALTER TABLE … SET SCHEMA`, so it kept its `public` ACL — neither
  `0001`'s schema-wide grant (the schema was empty when it ran) nor its
  default privileges (which reach only relations created later) apply.
  The one path that reads that table is the `job_row` kind, which is
  always `side: system`.
- `cobalt_system` has no reach into `"user"` at all (`0001` REVOKEs the
  schema), so the reverse crossing is never legal either.
- **K8 is the worked example.** The corpus question spans both sides, so
  it is two checks: `K8.1` (`job_row`, system) owns `input_stale = 0`,
  `trade_date = {last_trading_day}` and printing `card_misses`; `K8.2`
  (`sql`, user) owns `incomplete = 0` and prints `card_rows`. The one
  assertion that needed both in a single statement — `card_rows =
  job.result card_misses` — is now a hand comparison of the two printed
  numbers, named in both `expect_text`s (R6 A). No cross-side grant was
  added for a smoke check.

`test_no_smoke_check_reads_across_the_tenancy_wall_it_declares` keeps
this true: it derives the granted set by parsing the GRANT statements in
`src/cobalt/db_migrations/*.sql` (never a hard-coded list) and checks
every committed `sql` check in both directions;
`test_the_tenancy_wall_check_refuses_a_cross_side_query` proves it bites
on the pre-split K8 shape.

Classification for `cobalt jobs restarts` (L42): a change under
`configs/cobalt/smoke/` derives no restart. The rule is `operator command (cobalt smoke); no job reads`, in `jobs/restarts.py`. The test keeps the claim true: no plist runs `cobalt smoke`, and only `smoke/cli.py` and this file open a suite.
