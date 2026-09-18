# S2-P4 CHUNK FX — build report (Opus 5, headless builder) — 2026-09-18

## §0 Headline
- (a) DONE: smoke `K8` split into `K8.1` (system, `job_row`) + `K8.2` (user, `sql`) per the desk ruling — no migration touched, no cross-side grant added; every original expectation still asserted except `counts_agree`, which is now a named hand comparison (ESCALATE 2).
- (a) DONE: 3 new offline tests in `tests/cobalt/test_smoke.py`, 2 of them failing before the edit, all passing after; the granted set is parsed from the shipped migrations, never hard-coded.
- (c) DONE: `jobs/wrapper.py` docstring + `jobs/wrapper.md` now state the real rule (`timeout_s / jobs.heartbeat_fraction`) with one worked example from the shipped numbers (2400 / 3 = 800 s). Docs only, no behaviour change, no test — stated as the brief allows.
- NOT touched: `replay/movers.py` (stopped by the hub), any migration, any config number.
- `uv run pytest -q tests/cobalt tests/taxonomy`: **`1707 passed, 306 skipped, 2 xfailed, 15 warnings in 51.61s`** — 0 failed. ESCALATE: 4.

## Files changed
| File | Change |
|---|---|
| `configs/cobalt/smoke/s2.yaml` | `K8` → `K8.1` + `K8.2`; header comment on the split and why no grant was added |
| `tests/cobalt/test_smoke.py` | +3 tests, +`granted_relations()` / `cross_side_reads()` helpers, `import re` |
| `docs/40 - DevDocs/cobalt/smoke/config.md` | new "The tenancy wall in a suite file (L32)" section (suite-file = the config family's page) |
| `docs/40 - DevDocs/cobalt/smoke/checks.md` | `sql` evaluator: `side` is a role, cross-side reads split not granted |
| `src/cobalt/jobs/wrapper.py` | docstring item 3 rewritten (rule + shipped worked example) |
| `docs/40 - DevDocs/cobalt/jobs/wrapper.md` | same rewrite, both config paths named |

## (a) What is compared where — K8's assertions after the split
| Original K8 expectation | Now owned by | How |
|---|---|---|
| `job.result trade_date = last trading day` | **K8.1** (`job_row`, system) | `result_equals: {trade_date: "{last_trading_day}"}` — machine-asserted (K7 asserts the same value; the old K8 also duplicated it, and it is what makes the hand comparison valid) |
| `job.result input_stale = 0` (R1-12) | **K8.1** | `result_equals: {input_stale: 0}` — machine-asserted; an ABSENT key now FAILs (the old SQL would have compared NULL) |
| `incomplete = 0` (every `kind='card'` row has `cf_r` + `inputs_sha256`) | **K8.2** (`sql`, user) | `expect: [{column: incomplete, op: eq, value: 0}]` — machine-asserted, unchanged query fragment |
| `counts_agree` (`card_rows` = `job.result card_misses`) | **K8.1 + K8.2, by hand** | K8.1 `result_keys: [card_misses]` makes the number present and prints the whole job row; K8.2 prints `card_rows`; both `expect_text`s name the comparison, so the R6 A hand fallback still performs it. **No longer machine-asserted** — see ESCALATE 2 |

Framework check first, as the brief required: `run_suite` maps `evaluate` over checks independently; a `Predicate` value and a `result_equals` value resolve only from `SmokeContext` (fixed run variables) or a literal. There is **no** mechanism to carry a value from one check into another or to compare two checks, so the equality could not stay machine-asserted without building a new check kind (L3: not a second copy of the read path — a new kind, out of this chunk's scope).

`K8.1` uses the `job_row` kind rather than a `side: system` `sql` check on purpose: `job_row` is the one path that reads `cobalt_jobs` (it hard-codes `side="system"`), and every other job assertion in the suite already goes through it.

IDs: `K8.1`/`K8.2` keep the `K8` family, so `test_smoke_checks_load_through_schema_bad_file_crashes_with_line`'s `{K1…K18}` family assertion is unchanged and no renumbering reached any other id. Nothing else in the tree names `K8` as a *check id*: the report renderer has no per-id expectations; `plan-s2-p4-2026-09-15.md:229` and `ADR-0010:120` name the **family** `K8` exactly as they name `K4`/`K5`/`K10`–`K12`/`K16` families that are already split into `.1`/`.2` rows — not an id I changed, so both dated records are left as written.

## New tests — failing before, passing after
Evidence captured by restoring the committed `s2.yaml` (`git show HEAD:…`) with the new tests in place, then restoring the split file.

| Test | Failing assertion BEFORE | After |
|---|---|---|
| `test_no_smoke_check_reads_across_the_tenancy_wall_it_declares` | `AssertionError: a smoke check would hit `permission denied` on a real connection (L32: `cobalt db query` SET ROLEs to the side's role and asserts it).` → `K8 (side: user) reads system.cobalt_jobs, which no migration GRANTs to cobalt_user` … `assert ['K8 (side: u... cobalt_user'] == []` | PASS |
| `test_the_k8_split_keeps_every_assertion_on_its_own_side` | `AssertionError: assert 'K8' not in {'K1': LaunchctlCheck(id='K1', title='co…` | PASS |
| `test_the_tenancy_wall_check_refuses_a_cross_side_query` | **Passed before and after, by construction** — it feeds the helper a doctored copy of the pre-split K8 (and a doctored reverse-direction check) rather than the shipped file, so it cannot depend on the config edit. It is the bite proof the brief asked for; before this change it did not exist at all. Stated plainly rather than manufactured. | PASS |

How the granted set is derived (no hard-coded list): `granted_relations()` strips `--` comments from every `src/cobalt/db_migrations/*.sql` and parses `GRANT <privs> ON [TABLE|SEQUENCE] <schema>.<relation> TO <roles>;`, bounded to one statement. Only **per-relation** grants count, deliberately: `0001`'s `GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user` ran while `system` was empty, and its `ALTER DEFAULT PRIVILEGES` reaches only relations *created* later by the named roles — neither reaches a relation `0002` **moved** in with `ALTER TABLE … SET SCHEMA`, which keeps its `public` ACL. `system.cobalt_jobs` is exactly such a moved relation, and the test asserts both facts directly (`system.movers_daily in granted["cobalt_user"]`, `system.cobalt_jobs not in`). The failure message names `system.movers_daily` (`0008_radar_value_movers.sql:42-44`, granted for `missed.mover_id`'s FK, used by K9) as the one documented, migration-backed exception. Direction (2) is covered by the same helper (`cobalt_system` has no grant into `"user"`; `0001` REVOKEs the schema) and is bite-proved in the second test.

## (c) wrapper docstring + DevDoc
Shipped numbers read, not guessed: `configs/cobalt/jobs.yaml:197` `com.cobalt.archiver timeout_s: 2400`; `configs/cobalt/taxonomy/tunables.yaml:626-627` `jobs.heartbeat_fraction: 3` → **800 s**. Both files now state the rule first and the worked example second, and name both config paths (DevDoc). No code changed, so no test — the claim under test would be `wrapper.py:169` `every_s = spec.timeout_s / heartbeat_fraction()`, which is already the shipped behaviour the docs were misdescribing.

## Suite
`uv run pytest -q tests/cobalt tests/taxonomy`, offline (no `.env`, no DB), final line verbatim:

```
1707 passed, 306 skipped, 2 xfailed, 15 warnings in 51.61s
```

## ESCALATE
1. **Desk wording vs implementation (desk to confirm).** The desk's wording was "no `side: user` smoke query names a `system.` relation". Read literally that also forbids K9's `system.movers_daily` read, which `0008` grants on purpose for `missed.mover_id`. Implemented as the **granted-set** reading: a user-side check may name a `system.` relation exactly where a migration GRANTs it to `cobalt_user`. If the desk meant the literal rule, K9 must be split too and the grant in `0008` reconsidered.
2. **`counts_agree` is no longer machine-asserted.** It is a hand comparison of two printed numbers (K8.1's `last_result.card_misses` vs K8.2's `card_rows`), named in both `expect_text`s. This is the one honest cost of the split: no role can read both tables and the framework carries no value between checks. Restoring a machine assertion needs a new suite check kind (e.g. `compare`, two queries + one predicate over both rows) — a framework build, ruled before it is written.
3. **Same defect class, wider than K8 (no migration touched, per the brief).** `0001`'s schema-wide grant ran before `0002` moved the tables in, so `cobalt_user` has SELECT on **none** of the moved system tables — `bars`, `cobalt_jobs`, `cobalt_kill_switch`, `cobalt_redactions`, `cobalt_email_sends`, `session_blocks` — even though `0001`'s own comment says "a user-side job reads bars and radar membership" (`radar_membership` is fine: explicitly granted by `0004`). No smoke check names any of them today and the new test catches any future one, but a user-side *reader* of `system.bars` would fail in production the same way K8 would have. Migration-level fix, needs a ruling.
4. **K8.1 repeats K7's `trade_date` assertion.** Deliberate, and the pre-split K8 did the same: without it, K8.2's `card_rows` (counted for `{last_trading_day}`) could be compared by hand against a job row from another day. Not L3 duplication (one assertion in two checks, not two implementations), but recorded so it is not mistaken for drift.

## Not done
- `src/cobalt/replay/movers.py` `REQUIRED_HEADERS` / `Asset Type` — out of chunk, stopped by the hub.
- No commit (the hub commits). Worktree left dirty with exactly the six files above; `scratch/` untouched apart from a temp copy that was removed.
