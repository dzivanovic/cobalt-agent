# S2-P4 build — Chunk C (STEP-9, STEP-8) — Opus 5 headless — 2026-09-17

## §0 Headline
- Chunk C is **built in the working tree and not committed**. It adds:
  - **`cobalt smoke s2`**, read-only. It runs K1–K18 from `configs/cobalt/smoke/s2.yaml` through a Pydantic schema; a bad file crashes with its line number.
  - **Verdicts:** PASS/FAIL/KNOWN/ERROR, and OVERALL (RED on any ERROR, AMBER on any FAIL, KNOWN never lowers) using day-open's own roll-up.
  - **Report:** the numbered verdict table, and every row's exact command and expected output (R1-24).
  - **STEP-8 docs:** DevDocs complete across A+B+C, ADR-0010, the BACKLOG row.
- Suite `uv run pytest -q tests/cobalt tests/taxonomy`: **1326 passed, 263 skipped** (chunk B: 1310 / 262). The one new skip is `requires_db`, and nothing errors.
- The replay job row and plist from chunk B match R1-22/R2-6 and needed no change. `ops/README.md` gained the replay row and its explicit bootstrap action.
- **ESCALATE: 0 new.** Chunk B's E1–E3 still stand, E1 (the L53 ceiling) blocks deploy (§5).

## §1 Files changed

| File | Change |
|---|---|
| `src/cobalt/smoke/__init__.py` | new: package map |
| `src/cobalt/smoke/models.py` | new: `SmokeSuite`, seven check kinds discriminated on `kind`, `Predicate` (per-value `known`), `SmokeContext`, `CheckOutcome`, `SmokeReport`, `READ_ONLY_CLI`, `variables_in`; re-exports day-open `Verdict`/`Overall`/`overall_verdict` |
| `src/cobalt/smoke/config.py` | new: `load_suite` (YAML node marks → `SmokeConfigError.line`), `SUITES_DIR`, `suite_path` |
| `src/cobalt/smoke/checks.py` | new: `SmokeDeps`/`default_deps`, `last_trading_day`, `build_context`, `render_sql` (typed literals), `same`/`holds`, `command_for` (hand fallback), one evaluator per kind, `evaluate` (never raises), `run_suite` |
| `src/cobalt/smoke/report.py` | new: `build_report`, `render_table`, `render_markdown`, `render_json`, `write_report` (never overwrites; `…-HHMMSS.md` beside) |
| `src/cobalt/smoke/cli.py` | new: `cobalt smoke <suite> --cutoff ISO8601 [--date] [--prod] [--json]`; exit 1 unless GREEN |
| `configs/cobalt/smoke/s2.yaml` | new: the K1–K18 checklist, split into sub-rows so each carries one command (K4.1–4, K5.1–2, K10.1–2, K11.1–3, K12.1–2, K16.1–2) |
| `src/cobalt/db_query.py` | `read_rows` (the one read path, now shared), `QueryRows`, `hand_command`; `command` behaviour unchanged |
| `src/cobalt/dayopen/models.py` | `Verdict.KNOWN`; `overall_verdict` takes any `.verdict` sequence; empty list raises |
| `src/cobalt/jobs/restarts.py` | `configs/cobalt/smoke/*` → `operator command (cobalt smoke); no job reads`, no restart (plan §5, Astra R2-6) |
| `src/cobalt/cli.py` | mounts `cobalt smoke`; docstring lists `replay` and `smoke` |
| `tests/cobalt/test_smoke.py` | new |
| `tests/cobalt/test_jobs_restarts.py` | + 1 test |
| `docs/10 - Decisions/ADR-0010-missed-corpus-counterfactual-r-picks.md` | new: picks, the cf-R formula, horizon rule, gate order, movers benchmark, receipts/versioning, job + line |
| `docs/00 - Project/BACKLOG.md` | S2-P4 row under NOW |
| `ops/README.md` | `com.cobalt.replay.plist` row (bootstrap once at D1 step 4, no restart); label count 14 → 16 (it was stale before replay too) |
| `docs/40 - DevDocs/cobalt/smoke/{__init__,models,config,checks,report,cli}.md` | new pages |
| `docs/40 - DevDocs/cobalt/{db_query,dayopen/models,cli,jobs/restarts}.md` | dated `2026-09-17 — S2-P4` sections |

## §2 Tests added (names)

**§4 Smoke sentences (STEP-9)** — all in `tests/cobalt/test_smoke.py`

| §4 sentence | Test |
|---|---|
| checks load through schema, bad file crashes with line | `test_smoke_checks_load_through_schema_bad_file_crashes_with_line`. Covers: the committed suite loads with K1–K18; bad op → line 12; missing `side` → line of the check; YAML syntax error; `DELETE` refused at load; argv off the allowlist; unknown variable; duplicate ids; absent file. |
| RED on error, AMBER on fail, KNOWN never lowers | `test_verdict_red_on_error_amber_on_fail_known_never_lowers` (also: an empty list raises) |
| imports no writer, calls no write (sentinels) | `test_smoke_imports_no_writer_and_calls_no_write`. **Static:** AST scan of `src/cobalt/smoke/*.py` for writer modules and names. **Runtime:** the committed suite runs through `cli.run` while `VaultWriter`, `VaultWriteStore`, `JobStore`, `TraderSettingsStore` write methods, `db.connect`, `db.connect_migration`, `subprocess.run` and `Popen` are armed to raise. A renamed write method fails the test rather than un-arming it. |
| writes report file with table | `test_smoke_writes_report_file_with_table` (table rows, OVERALL, variables block, one `command:` and one `expected:` per check, second run lands beside) |
| one test per K-check kind on fakes | `test_kind_launchctl_running_and_registry_match`, `test_kind_sql_renders_literals_through_the_read_path_and_grades_rows`, `test_kind_http_status_and_body`, `test_kind_log_grep_reads_only_the_newest_block`, `test_kind_job_row_state_cadence_age_and_result`, `test_kind_vault_unit_reads_markers_and_never_creates`, `test_kind_cli_exit_code_through_the_allowlist` |

**Amendments and support**

| Item | Test |
|---|---|
| R1-24 exact command + expected per K row | `test_every_committed_check_renders_an_exact_command_and_expected_output` |
| K6 "no fill yet" KNOWN; K3 KNOWN on no post-deploy admission; K5 P2 absent = FAIL | in `test_kind_sql_…` (known_if, `requires_relation`), plus the suite assertions |
| K13 cadence-aware, not a flat 30 h cutoff | in `test_kind_job_row_…` (`not_missed` via `jobs.watchdog.is_missed`; yesterday's finish tonight → MISSED; `result_positive`) |
| `{last_trading_day}` definition | `test_context_last_trading_day_waits_for_the_anchor_job_and_skips_holidays` |
| `--json` writes nothing; `--cutoff` required with offset | `test_json_flag_prints_and_writes_nothing`, `test_cutoff_is_required_and_must_carry_an_offset` |
| L42 classification of `s2.yaml` | `test_a_smoke_suite_file_derives_no_restart_and_no_job_runs_the_smoke` (test_jobs_restarts) |
| hub, cobalt_dev | `test_committed_queries_run_read_only_on_cobalt_dev` (**requires_db**): every committed sql/job_row check through the real read path must not be ERROR |

**Failing test first (recorded):**
- `test_smoke.py` first ran red at collection: `ImportError: cannot import name 'QueryRows' from 'cobalt.db_query'`.
- The restarts test first ran red: `rule='UNCLASSIFIED CONFIG' … escalate=True`.
- Its first draft then failed on a wrong claim. It asserted that no resident import-reaches `cobalt.smoke`, but `com.cobalt.radar` enters through `cobalt.cli`. The assertion now checks who opens a suite file (§4.3).

## §3 Suite result (verbatim)

`uv run pytest -q -p no:cacheprovider --color=no tests/cobalt tests/taxonomy`:
```
1326 passed, 263 skipped, 15 warnings in 26.90s
```
- The 15 warnings are the existing litellm `asyncio.iscoroutinefunction` DeprecationWarning, as in chunks A and B.
- New files alone: `tests/cobalt/test_smoke.py tests/cobalt/test_db_query.py tests/cobalt/test_dayopen_models.py -rs` → `28 passed, 1 skipped`, where the skip reads `requires_db: Postgres env settings not available`. `test_jobs_restarts.py` → `8 passed`.

## §4 What I could not do, and why

1. **`cobalt validate` was not run.** Without an environment, the bare command failed: `FAILED: EnvConfigError: COBALT_ENV is unset`. `COBALT_ENV=dev uv run cobalt validate` needed an approval this headless session could not get. The hub runs it.
   - Chunk B's `test_registry_and_ops_carry_the_replay_job_with_matching_schedule` covers the registry ↔ plist mirror.
   - `uv run cobalt smoke --help` did run and shows the mounted parser.
2. **The `requires_db` test was not run** (no DB, L41 interim). The hub runs it with `COBALT_ENV=dev` on cobalt_dev **after 0008/0009 are applied**, otherwise K3/K8/K9 hit a missing relation and ERROR. With P2 not merged, K5.1 is expected to be FAIL (relation absent), which the test allows. An empty dev corpus gives FAIL/KNOWN, never ERROR.
3. **Design choices the hub/reviewer should check:**
   - **`--cutoff` is a required argument, not derived.** No migration ledger records when 0009 was applied, and a guessed cutoff would silently change K3/K6. The deploy report's D1 merge instant is the value.
   - **K3 uses `first_seen_at >= cutoff`, not "re-scanned after deploy".** `radar_membership` has no per-row scan time, and a HOLD row carries forward a pre-deploy NULL, so a re-scan filter cannot tell a HOLD from a write defect. Rows first inserted after the deploy always go through the INSERT path, which writes `rank_metric`, so a NULL there is a genuine write-path defect (R1-19). `rank_value` NULL is reported as evidence only.
   - **K6 is SQL over every FILLED transition since the cutoff**, not one `cobalt cards picks --date` call. That CLI covers one day, and its `_store()` runs `ensure_schema`, which is not read-only, so it is off the `cli` allowlist. Its per-day command is quoted in K6's `expect_text`.
   - **K11 and K13 do not call `cobalt heartbeat show` or `cobalt jobs check`.** Both reach `watchdog.sweep`, which runs `ensure_schema` and `mark_probe`, so neither is read-only.
     - K11 is split in two: the heartbeat row age, and a `log_grep` for `OK database` / `OK sheet HTTP` in the newest block of `logs/heartbeat.log`.
     - K13 is a `job_row` check with `not_missed`. It uses the same `is_missed` arithmetic as the heartbeat archiver probe, plus `rows_written > 0`.
   - **K15 reads `cobalt_jobs.last_result.summary_sent[<last slot>]`.** The heartbeat records a slot only after the DM send succeeded, so this is the persisted form of "summary sent". There is no separate notify send-log to grep since the 2026-09-14 retirement.
   - **K18 has a gap.** It compares every registry label's enabled flag to `launchctl list`, loaded or not, through `watchdog.launchctl_status`, the existing parser. A `com.cobalt.*` job loaded in launchd with no registry row is not detected here; `cobalt validate` covers registry ↔ `ops/` (K17).
   - **K9 FAILs when a side has fewer than `top_n` rows.** The plan's "or fewer with export evidence" is left to the hub, who compares the cached export's row count. The check cannot read the CSV without a new kind.
   - **Hand commands are shell-quoted, so SQL with `'` renders as `'"'"'`.** This is correct shell, and `shlex.split(cmd)[-1]` is byte-identical to the executed statement (tested), but it is not pretty.
   - **Radar picks up the new code.** `cobalt.cli` imports `cobalt.smoke`, so `com.cobalt.radar` (entry `cobalt.cli`) derives a restart for `src/cobalt/smoke/*`. That restart is already in the P4 deploy.
4. **Not verified by me:**
   - `git check-ignore` on the new paths needed approval. `git status` lists every new file as untracked (not ignored), and the D6 carve-outs `!docs/10 - Decisions/**` and `!docs/40 - DevDocs/**` cover the docs.
   - `cobalt jobs restarts main..HEAD` was not run. Expected additions from chunk C:
     - `src/cobalt/smoke/*`, `db_query.py`, `dayopen/models.py` and `cli.py` → by static import reach (radar via `cobalt.cli`);
     - `jobs/restarts.py` → its importers;
     - `configs/cobalt/smoke/s2.yaml` → no restart;
     - `ops/README.md` → operations documentation;
     - `docs/*` → DOCS.
5. **STEP-8 DevDocs completeness** was checked by listing every `src/**/*.py` changed vs `main` plus untracked files. That is 37 `.py` files; `.sql` files are excluded. Every one has a page:
   - Chunk C added the 6 `smoke/` pages and sections to 4 existing pages.
   - `replay/models.md` and `replay/cli.md` are chunk B's new pages. They do not contain the string "S2-P4", but they are wholly P4 pages.

## §5 ESCALATE

0 new. Carried from chunk B, not resolved here:
- **E1:** the L53 gate refuses the archiver and replay under the unchanged ceiling. This is a deploy gate needing Dejan's ruling.
- **E2:** P2's formation contract is unbound.
- **E3:** the dev end-to-end needs a day whose bars carry real offsets.

On the S2 close evening, E1 shows as K7/K8/K9/K10 FAIL (AMBER) until it is ruled.

RESTARTS (expected; the hub derives it): chunk C adds no plist and no resident `reads:` file. `configs/cobalt/smoke/s2.yaml` → no restart. `src/` changes → `com.cobalt.radar` (via `cobalt.cli`), already in the P4 set.
