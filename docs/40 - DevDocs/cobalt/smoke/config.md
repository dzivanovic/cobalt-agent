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
  FK — which is what lets K9.1/K9.4 run `side: user`.
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
  it is three rows: `K8.1` (`job_row`, system) owns `input_stale = 0`,
  `trade_date = {last_trading_day}` and printing `card_misses`; `K8.2`
  (`sql`, user) owns `incomplete = 0` and prints `card_rows`; `K8.3`
  (`compare`) asserts the equality that can never be a single statement —
  `card_rows = job.result card_misses` — over the two numbers those rows
  collected (each names its own through `result_number`). No cross-side
  grant was added for a smoke check, and the assertion is a machine one
  again rather than a comparison by eye (added 2026-09-19, TR-A).
- **K9 is the second worked example** (rewritten 2026-09-19, TR-B). "Does
  `movers_daily` hold every row the night's export allowed?" spans the
  same wall: the stored rows are in `system.movers_daily` (granted), the
  export's own row count is in `system.cobalt_jobs.last_result` (never
  granted). So it is six rows, three per side: `K9.1`/`K9.4` (`sql`,
  user) count ONE side's active rows and keep both of old K9's
  predicates — `top_n not_null`, `not_archived = 0` — and print `stored`;
  `K9.2`/`K9.5` (`job_row`, system) print
  `movers_by_side.<side>.expected` = `min(top_n, exported - unranked)`
  (blank-`Change` rows are unranked, S2 smoke fix F1) from the
  replay's own result, and assert `trade_date = {last_trading_day}` so
  the comparison is about the night being checked; `K9.3`/`K9.6`
  (`compare`) assert the two are equal. `side` is CHECK-constrained to
  the two values (`0008`), so the two `not_archived` predicates together
  still cover every active row of the day. What changed in verdicts: a
  side whose export really returned fewer rows than `top_n` now PASSES
  (the plan's "or fewer with export evidence"), while a side holding
  fewer rows than its export allowed FAILS — the old `full_sides eq
  true` failed both alike and deferred the difference to a hand count of
  `data/radar-cache/<date>/movers-<side>-*.csv`.

`test_no_smoke_check_reads_across_the_tenancy_wall_it_declares` keeps
this true: it derives the granted set by parsing the GRANT statements in
`src/cobalt/db_migrations/*.sql` (never a hard-coded list) and checks
every committed `sql` check in both directions;
`test_the_tenancy_wall_check_refuses_a_cross_side_query` proves it bites
on the pre-split K8 shape.

## K3 grades BOTH writers of the value pair (added 2026-09-18, chunk FY)

`rank_metric`/`rank_value` reach a membership row down two code paths, and
a check keyed on `first_seen_at` sees only one of them:

- **INSERT** — a new admitted episode. `first_seen_at >= {cutoff}` finds
  exactly these, and `radar/store.py`'s ADMIT branch always writes the pair.
- **RETAIN** — a pre-deploy episode the scan keeps. Its `first_seen_at` is
  older than the deploy, so it never enters the first set, yet the RETAIN
  branch writes `rank_metric = %s` unconditionally: a defect there was
  invisible. It is found instead through the pool's own scan id —
  `left_at IS NULL AND last_scan_id = (max scan id of pool 'primary')` —
  gated on `radar_pool.last_scan_at >= {cutoff}` so a pool that has not
  scanned since the deploy contributes nothing.

One statement, one row, five counters: `post_deploy_admitted` /
`metric_missing` / `value_null` for the first set, `rescanned_admitted` /
`rescanned_metric_missing` for the second. Both `metric_missing` counters
are graded; `known_if` needs BOTH population counts at zero, so the "no
admitted row yet → KNOWN" semantics now hold for the union rather than for
half of it.

**Only a RANKED row without a metric is graded (S2 smoke fix F3,
2026-09-23).** The 2026-09-22 smoke look read K3 red at
`post_deploy_admitted=301, metric_missing=66, value_null=66`, and every one
of the 66 was designed behaviour: an episode inserted WITH a metric and
later STICKY-RETAINed after the scan stopped ranking it gets `rank=None`
and `value_of()` → `(None, None)` (`radar/pool.py`, Transition: "None where
no ranking happened"), which `radar/store.py`'s RETAIN branch writes as
`last_rank`, `rank_metric`, `rank_value` = NULL, NULL, NULL. `last_rank` is
the column that tells that class apart from the write-path defect K3
exists for (a row the scan RANKED yet stored no metric), so both graded
counters now count `rank_metric IS NULL AND last_rank IS NOT NULL`, and a
new printed-not-graded column `unranked_retained` (`rank_metric IS NULL
AND last_rank IS NULL` over the first set) shows the designed class beside
`value_null`. This is the P4 plan's corrected K3 (`plan-s2-p4-2026-09-15.md:243`,
Astra R1-19 / R1-24: a designed NULL is not a K3 failure). The desk's
production proof before the build: `metric_missing 66 · unranked_retained
66 · ranked_without_metric 0`. The HOLD ambiguity below is unchanged — a
held row keeps its prior `last_rank`, so it is still graded.

One ambiguity is named in `expect_text` rather than hidden: a frozen HOLD
(the COALESCE branch) also stamps `last_scan_id`, so a pre-deploy episode
held because its only source was degraded carries its pre-deploy NULL into
the second set, and no column tells it apart from a RETAIN defect. It reads
as a FAIL — loud, with the counts printed — and is checked against
`radar_pool.degraded_sources` before anyone rules it known (L1: a false
loud beats a silent miss).

`test_k3_covers_the_insert_path_and_the_retain_path` holds the shape
against the SHIPPED yaml, and
`test_the_k3_coverage_check_refuses_the_first_seen_at_only_shape` proves it
bites on the pre-fix `first_seen_at`-only query. The SQL itself cannot run
offline; `test_committed_queries_run_read_only_on_cobalt_dev` (`requires_db`,
hub) is where the statement is proven to parse and run, and
`tests/cobalt/test_smoke_k3_sql.py` (added 2026-09-19, TR-A; `requires_db`,
rolled back) is where the ambiguity above stops being an argument: it
CONSTRUCTS the held pre-deploy row on `cobalt_dev` and records that the
framework grades K3 FAIL on it.

Classification for `cobalt jobs restarts` (L42): a change under
`configs/cobalt/smoke/` derives no restart. The rule is `operator command (cobalt smoke); no job reads`, in `jobs/restarts.py`. The test keeps the claim true: no plist runs `cobalt smoke`, and only `smoke/cli.py` and this file open a suite.
