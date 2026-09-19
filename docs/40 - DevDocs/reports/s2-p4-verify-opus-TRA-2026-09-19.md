# S2-P4 TR-A — smoke `compare` kind + the K3 SQL test file (2026-09-19)

## §0 Headline
- BUILT, both items. K8 `counts_agree` is a MACHINE assertion again: new `kind: compare` (`K8.3`, `left: K8.1`, `right: K8.2`, `op: eq`), Pydantic-validated at load; the "compare by eye" wording is gone from both halves.
- `tests/cobalt/test_smoke_k3_sql.py` added: `requires_db`, skips clean offline, constructs build2 ESCALATE 6's HOLD row inside the rolled-back dev transaction and asserts the framework grades K3 FAIL.
- Offline suite `1788 passed, 324 skipped, 1 xfailed, 15 warnings in 54.74s` (0 failed).
- The STOP sentence did NOT trigger: the kind is additive and the field is optional, and a test proves the shipped suite with both stripped out loads and runs byte-identically. No other smoke file's loading or running is touched. ESCALATE: 0.
- NOT DONE HERE (no DB, L41 interim): both `requires_db` tests are SKIPPED — their red/green is the hub's dev-DB run. `cobalt validate` not run (no `.env`; I launch nothing).

## Files changed
| file | change |
|---|---|
| `src/cobalt/smoke/models.py` | `CompareOp` (one member: `eq`), `CompareCheck`, `RESULT_NUMBER`, optional `result_number` on `SqlCheck`/`JobRowCheck`, `SmokeSuite._compare_operands` load-time validator, `CheckOutcome.number` |
| `src/cobalt/smoke/checks.py` | `COMPARE_OPS`, `_compare()`, `command_for` compare branch, number capture in `_sql`/`_job_row`, `evaluate(..., results=None)`, `run_suite` threads outcomes by id |
| `src/cobalt/smoke/report.py` | `render_json` carries `number` as text (a `Decimal` prints exactly; a float would not — L57) |
| `configs/cobalt/smoke/s2.yaml` | `result_number` on K8.1/K8.2, new K8.3 compare row, both `expect_text`s rewritten (no hand comparison), K8 header comment + file header rewritten |
| `tests/cobalt/test_smoke.py` | 5 new tests; `test_the_k8_split_keeps_every_assertion_on_its_own_side` updated to assert K8.3 instead of the eye comparison |
| `tests/cobalt/test_smoke_k3_sql.py` | NEW — 2 `requires_db` tests |
| `docs/40 - DevDocs/cobalt/smoke/{models,checks,report,config}.md` | DevDocs for every changed `.py`, plus `config.md`'s K8 and K3 paragraphs, which described the now-removed hand comparison |

`git diff --stat`: 9 files changed, 522 insertions(+), 58 deletions(-), plus the one new test file. Nothing outside the bound: no `replay/**`, no `radar/**`, no migration, no other config file, K9 untouched, no dependency, no commit.

## Tests added (names)
| file | test |
|---|---|
| `test_smoke.py` | `test_compare_refuses_an_unknown_id_a_self_reference_and_an_operand_with_no_number` |
| `test_smoke.py` | `test_compare_grades_equal_pass_unequal_fail_and_errors_on_a_bad_operand` |
| `test_smoke.py` | `test_the_shipped_k8_3_asserts_the_two_counters_agree` |
| `test_smoke.py` | `test_the_report_renders_the_compare_row` |
| `test_smoke.py` | `test_a_suite_with_no_compare_row_loads_and_runs_exactly_as_before` |
| `test_smoke.py` (changed) | `test_the_k8_split_keeps_every_assertion_on_its_own_side` |
| `test_smoke_k3_sql.py` (new file, `requires_db`) | `test_k3_statement_parses_and_returns_its_five_counters_on_cobalt_dev` |
| `test_smoke_k3_sql.py` (new file, `requires_db`) | `test_k3_hold_row_reads_red_documented_ambiguity` |

Coverage against the ruling, row by row: unknown id · self-reference (both `id == left/right` and `left == right`) · an operand BELOW the compare row · an operand that declares no `result_number` · an operand kind with no number at all (`launchctl`) · an op that is not `eq` · non-numeric operand · operand ERROR · equal PASS · unequal FAIL · the shipped `s2.yaml` validating at load · the report rendering the compare row (table, markdown section, JSON) · an old compare-free smoke file loading and running unchanged.

## Red before, green after
Tests were written first and run against the unchanged framework. All six red (`6 failed, 21 deselected in 0.34s`):

```
FAILED tests/cobalt/test_smoke.py::test_the_k8_split_keeps_every_assertion_on_its_own_side - KeyError: 'K8.3'
FAILED tests/cobalt/test_smoke.py::test_compare_refuses_an_unknown_id_a_self_reference_and_an_operand_with_no_number - cobalt.smoke.config.SmokeConfigError: …
FAILED tests/cobalt/test_smoke.py::test_compare_grades_equal_pass_unequal_fail_and_errors_on_a_bad_operand - cobalt.smoke.config.SmokeConfigError: …
FAILED tests/cobalt/test_smoke.py::test_the_shipped_k8_3_asserts_the_two_counters_agree - KeyError: 'K8.3'
FAILED tests/cobalt/test_smoke.py::test_the_report_renders_the_compare_row - KeyError: 'K8.3'
FAILED tests/cobalt/test_smoke.py::test_a_suite_with_no_compare_row_loads_and_runs_exactly_as_before - AssertionError: nothing was stripped
```

The two `SmokeConfigError` reds in full — the schema refusing everything the kind needs:

```
E  pydantic_core._pydantic_core.ValidationError: 3 validation errors for SmokeSuite
E  checks.0.sql.result_number
E    Extra inputs are not permitted [type=extra_forbidden, input_value='card_rows', input_type=str]
E  checks.1.job_row.result_number
E    Extra inputs are not permitted [type=extra_forbidden, input_value='card_misses', input_type=str]
E  checks.2
E    Input tag 'compare' found using 'kind' does not match any of the expected tags:
E    'launchctl', 'sql', 'http', 'log_grep', 'job_row', 'vault_unit', 'cli' [type=union_tag_invalid, …]
E  cobalt.smoke.config.SmokeConfigError: …/s9.yaml:10: checks → 0 → sql → result_number: Extra inputs are not permitted (+2 more)
```

After the edit, the same six:

```
tests/cobalt/test_smoke.py::test_the_k8_split_keeps_every_assertion_on_its_own_side PASSED
tests/cobalt/test_smoke.py::test_compare_refuses_an_unknown_id_a_self_reference_and_an_operand_with_no_number PASSED
tests/cobalt/test_smoke.py::test_compare_grades_equal_pass_unequal_fail_and_errors_on_a_bad_operand PASSED
tests/cobalt/test_smoke.py::test_the_shipped_k8_3_asserts_the_two_counters_agree PASSED
tests/cobalt/test_smoke.py::test_the_report_renders_the_compare_row PASSED
tests/cobalt/test_smoke.py::test_a_suite_with_no_compare_row_loads_and_runs_exactly_as_before PASSED
```

`test_smoke_k3_sql.py` is exempt from red-first by the brief (it is a DB test). Offline, verbatim:

```
SKIPPED [1] tests/cobalt/test_smoke_k3_sql.py:86: requires_db: Postgres env settings not available
SKIPPED [1] tests/cobalt/test_smoke_k3_sql.py:97: requires_db: Postgres env settings not available
```

## The design choice: how a check names its numeric result
**`result_number`: one optional additive string field on `sql` and `job_row`.** For `sql` it is a COLUMN of the single returned row; for `job_row` a dotted `last_result` path. `CheckOutcome` gains `number: Optional[Decimal]`, filled by those two evaluators; `run_suite` keeps outcomes by id as it goes and hands that map to the next `evaluate`, so a `compare` row grades numbers that have already been collected — one pass, no source read twice, nothing new opened.

Why this shape and not the alternatives:

| alternative | why not |
|---|---|
| the compare row names the column itself (`left: {check: K8.1, key: card_misses}`) | the same fact would then live in two rows and could drift; the check that produces a number is the one that knows which of its columns IS the number |
| the compare re-runs both operands' probes | two reads of the same source in one run, two chances to disagree with the numbers printed above, and the tenancy wall would be crossed twice for nothing |
| a `number:` field on every kind | `launchctl`/`http`/`vault_unit`/`cli` have no number; an optional field they would never set is dead surface. A compare over one of them is refused AT LOAD, naming the id and the kind |

Two deliberate consequences, both documented in the DevDocs:
- `result_number` grades NOTHING on its own check. K8.1's verdict still comes from `result_keys`/`result_equals` alone, so a job that failed to write `card_misses` stays a FAIL (AMBER), and it is K8.3 that goes ERROR (RED) because it had nothing to compare. A missing/absent/non-numeric value leaves `number = None` rather than raising — the loudness belongs on the row that wanted the number.
- `CompareOp` has exactly one member. An operator nothing asserts is an untested branch; adding one is adding its test (`COMPARE_OPS` is the one place to add it).

Verdict semantics as ruled: equal PASS · unequal FAIL · an operand that ERRORed → ERROR naming it (never a silent PASS) · a non-numeric operand → ERROR naming it and its kind. Both operands are printed in `detail` and `raw` whatever the verdict (L57).

Rendered row (from `test_the_report_renders_the_compare_row`'s fixture, `card_misses=2` vs `card_rows=3`):

```
| K8.3 | missed — the corpus and the job agree on the card count | FAIL | K8.1 = 2, K8.2 = 3 (op eq) — they disagree |

## K8.3 missed — the corpus and the job agree on the card count — FAIL
- kind: compare
- command: `# compare K8.1 eq K8.2 — run both rows above; their two printed numbers must be eq`
- expected: K8.1's last_result.card_misses = K8.2's card_rows, both printed on their own rows above. …
- verdict detail: K8.1 = 2, K8.2 = 3 (op eq) — they disagree
```
```
K8.1	PASS	2
K8.2	PASS	3
```

R6 A for this row is a hand INSTRUCTION, not a command, because the row runs no probe: it names the two ids and the operator, and the rows it names print their own commands and numbers. That is the one place the report's "every row prints the exact command it ran" reads differently, and the file header and the K8 comment both say so.

## The K3 SQL test file
`tests/cobalt/test_smoke_k3_sql.py`, `requires_db` exactly as `tests/cobalt/test_radar_store.py` declares it, inside the autouse `dev_db_tx` transaction (`tests/cobalt/conftest.py`) that is always rolled back.

- It loads `configs/cobalt/smoke/s2.yaml` through `load_suite`, renders K3 with `checks.render_sql` and a real `SmokeContext` (fixed cutoff `2026-09-18T20:05-04:00`), and executes through `checks.default_deps(prod=False).read_rows` — the framework's own loader, renderer and read path, no second copy (L3).
- Test 1: the statement parses and executes, returns exactly one row, and its columns are exactly `post_deploy_admitted, metric_missing, value_null, rescanned_admitted, rescanned_metric_missing`.
- Test 2 constructs build2 ESCALATE 6's scenario in the same transaction: the `primary` `radar_pool` row is UPSERTed to `last_scan_id = max+1`, `last_scan_at = cutoff + 1h` (an existing dev row is CHANGED, never duplicated — `ON CONFLICT (pool_key) DO UPDATE`), and one `radar_membership` episode is inserted with `first_seen_at = cutoff − 1 day`, `entered_at` set, `left_at NULL`, `last_scan_id` = that scan and `rank_metric`/`rank_value` NULL — what `radar/store.py:100-110`'s HOLD branch leaves behind. NOT NULL columns taken from `0004_radar_pool.sql` (+ `0008`'s two added columns).
- It then asserts `rescanned_admitted >= 1` and `rescanned_metric_missing >= 1` on the returned row, and calls the framework's grader (`checks.evaluate`) on it: **FAIL**, with `rescanned_metric_missing` named in the detail.
- No fix is built for the ambiguity; the disposition is Dejan's (ESCALATE 6 already states the three options). The file's docstring says exactly that.

## What I could not do
1. **Neither `requires_db` test has been RUN.** No database and no credentials in this worktree (L41 interim). Both skip cleanly here; the hub's `COBALT_ENV=dev` run is their first real execution, and is the only thing that can confirm the constructed SQL against the live dev DDL. If the hub's run goes red, the likely spots are the `radar_membership` NOT NULL column list and `read_rows`' `BEGIN READ ONLY` inside the fixture's open transaction (a Postgres WARNING, not an error — the same thing `test_committed_queries_run_read_only_on_cobalt_dev` already does, which has also never run).
2. **`cobalt validate` not run** — no `.env` here and I launch nothing (L36).
3. **One imprecise line number.** A check-level mistake (self-reference, `left == right`, a bad `op`) crashes with the offending row's own line. The suite-level ones — an unknown operand id, an operand below the compare row, an operand with no `result_number` — report the line of the `checks:` key, because they are validated on the whole list. Every message names the ids involved, so the row is still findable; making the line exact would need per-index error locations from the suite validator. Noted, not built.
4. **`op` is `eq` only.** The ruling allows more with tests; nothing in S2 needs one, so none was added.
5. `config.md`'s K8 and K3 paragraphs were updated although `config.py` itself did not change — they described the hand comparison that no longer exists. Flagging it as a docs edit outside the "changed .py" rule.
