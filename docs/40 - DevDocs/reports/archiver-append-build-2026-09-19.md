# Archiver append-only — BUILD (tribunal FINAL design), `archiver-append-0919`

DO NOT STOP until `ARCHIVER APPEND BUILT`
BUILT. 7 chunks, 7 commits (`54e98f7` … `c974fbf`), this report on top. Branch `archiver/append-0919` off main `8838dda`; OFFLINE throughout, no `.env`, no `cobalt_dev`.
Suite `1850 passed, 315 skipped, 0 failed` against BASELINE `1562 / 297 / 0` — +288 tests, +18 `requires_db` that have NEVER RUN.
`archiver.write_mode` ships **`upsert`**; `git diff main -- src/cobalt/radar/` is EMPTY (R8).
ESCALATE: 8, plus the spec's O-1…O-7 carried untouched.

## AUTHORIZATION

Verified 2026-09-19 09:44 ET, before any work.

| check | command | result |
|---|---|---|
| spec committed on main | `git -C /Users/cobalt/cobalt log --oneline -2 -- "docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md"` | `8838dda docs(design): archiver append-only FINAL design (tribunal-derived, option A per R8) + its build prompt (no new rule)` — present, not empty |
| report rows committed | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` | 8 commits, newest `e37bc12 docs(desk): 09-19 R8 'A on archiver' recorded + folded; ops-0919 launched (919e5970); archiver final design in work` |
| `cto-2026-09-18.md` §4 R1 (06:46 "Approved") | `grep -n "^| R1 "` | row present; list (2) = `02-ops-2026-09-18.md`'s launch-line allowlist as committed `5fd90e8`; "NEVER push, never `bypassPermissions`, no production write or restart, no vault write" — says what the prompt quotes |
| R14 / R15 (the nightly overwrite — the purpose of this build) | `grep -n "^| R14 \|^| R15 "` | present. R14 17:15 ET verbatim "…i want to know where the watermark is for each ticker and I want to only add the new [bars]…"; R15 17:22 ET HOLD LIFTED + directions. Says what the prompt quotes |
| R18–R21 (L67) | `grep -n "^| R18 …R21 "` | all four present; R18 17:30 ET four-house tribunal / three checkers; R19 emergency+override+law numbers; R20 rounds; R21 "Your assumption is correct." |
| `cto-2026-09-17.md` §4 R5 (unattended standard) | `grep -n "^| R5 "` | present, 06:03 ET, verbatim |
| `cto-2026-09-19.md` §4 R3 + R6 + R5 | `grep -n "^| R3 \|^| R5 \|^| R6 "` | present. R5 07:35 "Okay, I retract my approval…" (the law is followed, not re-asked); R3 07:12 three deploys; R6 07:38 no idle lane, never a skipped law step |
| `cto-2026-09-19.md` §4 **R8** (09:30 "A on archiver") | `grep -n "R8"` line 161 | verbatim: `"A on archiver"` — A = `restate --apply` / `backfill-missing` ONLY in a QUIET WINDOW (radar idle, ≥5 min after the last poll cycle completed, ≥10 min before the next session opens); the LIVE radar poller is NOT touched; covers FINAL design → build → three-house check → deploy in today's `upsert` mode → shadow nights. **NOT covered: switching the archiver to `append`.** Says exactly what the prompt quotes |

### `grep -c` of each rule string in `prompts/2026-09-18/02-ops-2026-09-18.md`

The prompt's test ("every one must count 1") does NOT pass literally on 5 of 7 strings. Every difference is
a NARROWING — the 09-19 line restricts more than the approved 09-18 line and grants nothing it did not.
The ALLOWLIST of this launch line is a STRICT SUBSET of the allowlist R1 approved as list (2). Verdict:
**not an authorization mismatch — proceed**, with the deltas recorded here and in `## ESCALATE` (item vi).
This is the same launch line `ops-0919` runs under (`16-ops-2026-09-19.md`), so the finding is shared.

| my launch line's rule string | `grep -c` in 02-ops-0918 | what 02-ops-0918 says | delta |
|---|---|---|---|
| ``never `bypassPermissions` `` | **1** | same | none |
| ``every launch resumes from the report's last `CONTINUE:` line`` | 0 | ``resumes from the report's `CONTINUE:` line`` (count 1) | reworded, same rule |
| `auto mode on; allowlist per session (L55, L61, L62)` | 0 | `auto mode on; allowlist per session (L55, L61)` (count 1) | adds the L62 citation |
| `push never in it` | 0 | absent — but R1 states "NEVER push" for all three lines, and no push rule is in either allowlist | narrowing |
| ``no production command, no `cobalt_dev`, no `.env`, no vault write, no other seat's config`` | 0 | `no production restart, no production write, no vault write, no other seat's config` (count 1) | narrowing (command ⊃ restart/write; `cobalt_dev` + `.env` added) |
| `a usage-limit message is not a failure` … | 0 | absent | a STOP protocol; grants nothing |
| `Codex = NONE; Grok = NONE` | 0 | `Codex = NONE` (count 1) | narrowing |
| `nobody sits at this session's terminal` | 0 | `nobody sits at this terminal` (count 1) | reworded, same rule |

Allowlist subset proof (this line vs R1 list (2), by rule): `uv run pytest *`, `uv run cobalt jobs restarts *`,
`git add/commit/diff/status/log/show *`, `git -C /Users/cobalt/cobalt log*`, `cd *`, `mkdir -p *`, `ls *`,
`grep *`, `tail *`, `wc *`, `date*` — all 16 appear in the committed 09-18 line. DROPPED here, as the line
says: the `.env` cp/rm, every `COBALT_ENV=dev` and `COBALT_ENV=production` command, `launchctl`, `curl`,
`chmod`, `ops/cto-desk.sh`, `shasum`, `git -C … tag --list`.

## PREFLIGHT

Run 09:44 ET, first two minutes, before any work. Every probe sits inside its own rule's pattern.

| rule | command | exit | verdict |
|---|---|---|---|
| `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 09:44:09 EDT 2026` |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **EMPTY** |
| `Bash(git status*)` | `git status` | 0 | allowed — first two lines: `On branch archiver/append-0919` / `nothing to commit, working tree clean`. Branch correct, no rebase in progress |
| `Bash(git log*)` | `git log --oneline -1` | 0 | allowed — `8838dda …` = main's tip at worktree creation (FIRST LAUNCH) |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `8838dda` (main unchanged since the worktree was cut) |
| `Bash(ls *)` | `ls -la .env` | 1 | allowed — `ls: .env: No such file or directory`. **No `.env` in this worktree: the suite cannot reach `cobalt_dev`** |
| `Bash(ls *)` | `ls "docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md"` | 0 | allowed — the spec is in this worktree |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_archiver_store.py` | 0 | allowed — `2 tests collected` (venv built on first use) |
| `Bash(uv run cobalt jobs restarts *)` | `uv run cobalt jobs restarts main..HEAD` | 0 | allowed — header + `RESTARTS: none` (empty range on a first launch) |
| `Bash(grep *)` | the 12 authorization greps above | 0 | allowed |

0 DENIED. PREFLIGHT GREEN.

## BASELINE

Taken before any edit, 09:47 ET.

| suite | command | line |
|---|---|---|
| FULL | `uv run pytest -q tests/cobalt tests/taxonomy` | **`1562 passed, 297 skipped, 1 xfailed, 15 warnings in 43.84s`** — 0 failed |
| DIFFERENTIAL (chunk 5) | `uv run pytest -q tests/cobalt/test_archiver_store.py tests/cobalt/test_radar_poller.py tests/cobalt/test_archiver_report.py` | **`10 passed, 2 skipped in 0.09s`** |

Baseline is GREEN. Every later suite line is compared with it: `failed` stays 0, `passed` grows only by
this build's tests, `skipped` only by this build's `requires_db` tests.

## Chunk S — settings and the mode flag (spec §10)

RED FIRST: `uv run pytest -q tests/cobalt/test_archiver_settings.py` before any code →
`ModuleNotFoundError: No module named 'cobalt.archiver.settings'`, `1 error in 0.10s` (collection error =
the module does not exist). Then GREEN: **`47 passed in 0.14s`**.

| what the spec asks (§10) | where it is | proven by |
|---|---|---|
| ONE model, ONE loader (L3) | `src/cobalt/archiver/settings.py`, reading `cobalt.taxonomy.loader.load_tunables()` | `test_there_is_exactly_one_yaml_reader_behind_the_settings` (no `yaml` import in the module) |
| the seven keys resolve from the SHIPPED file | `configs/cobalt/taxonomy/tunables.yaml` (new block before the S2-P2 card rows) | `test_the_seven_keys_resolve_from_the_shipped_tunables_file` |
| `write_mode` accepts EXACTLY `upsert`/`append` | `ArchiverSettings._exact_write_mode` — no `strip()`, no `lower()` | 7-case parametrize `Append`, `APPEND`, `" upsert"`, `"upsert "`, `""`, `both`, `"append\n"` + a non-string + a missing row → all refused NAMING `archiver.write_mode` |
| the shipped value is `upsert`, pinned | row `archiver.write_mode: upsert`, `status: solidified` | `test_the_shipped_write_mode_is_upsert_and_only_a_reviewed_commit_changes_it` (L7 tripwire) |
| `shadow_compare` on/off | `ShadowCompare` + `.shadow_enabled` | on/off parametrize, 5 illegal values refused, and `shadow_compare` IGNORED in `append` (§5) |
| three repair minutes are positive integers | `RepairSettings` | 3 keys × 5 bad values (`0`, `-1`, `1.5`, `"10"`, `None`) each refused naming the key; `bool` is not an integer here |
| `status: proposed` exactly where the spec says PROPOSED | 4 rows proposed, 3 solidified | `test_the_shipped_rows_carry_the_units_and_statuses_the_design_ruled` |
| `source: ruling` + citation `cto-2026-09-19.md §16 / R8` on the desk's numbers | `quiet_before_open_min`, `quiet_after_cycle_min` consumers | same test asserts the citation string |
| `cobalt validate` prints it | `validate_command_lines()`, called from `_cmd_validate` after the heartbeat block | `test_validate_prints_the_resolved_settings` — the function is unit-tested, the CLI is NOT run |

Tunables schema limit check (chunk instruction): `TunableUnit` already carries `LABEL`, `COUNT` and `MIN`
(`src/cobalt/taxonomy/tunables.py:32-53`) and `TunableRow.value` is `Any`. **No change to
`src/cobalt/taxonomy/tunables.py` was needed** — the chunk's STOP condition did not trigger.

Diff stat (chunk S): `configs/cobalt/taxonomy/tunables.yaml` +85, `src/cobalt/archiver/settings.py` +283 (new),
`src/cobalt/cli.py` +9, `tests/cobalt/test_archiver_settings.py` +280 (new),
`docs/40 - DevDocs/cobalt/archiver/settings.md` +95 (new).

SUITE: `uv run pytest -q tests/cobalt tests/taxonomy` → **`1609 passed, 297 skipped, 1 xfailed, 15 warnings
in 42.20s`**. Against BASELINE: failed 0 → 0 · passed 1562 → 1609 (+47 = this chunk's tests) · skipped
297 → 297 (this chunk adds no `requires_db` test).

## Chunk M — the two additive tables (spec §11)

RED FIRST: `uv run pytest -q tests/cobalt/test_archiver_migrations.py` before any SQL →
**`48 failed, 10 skipped`** (`FileNotFoundError: …/0010_archive_progress.sql`, and the FORWARD/REVERSE
tail assertions). The 10 `requires_db` tests SKIPPED cleanly on the red run — no collection error.
Then GREEN: **`48 passed, 10 skipped in 0.03s`**.

CONTIGUITY CHECK (the chunk's STOP condition): searched for a test asserting that the migration numbers
are contiguous — `grep -rn "FORWARD\|REVERSE" tests/` → 4 files. **No contiguity test exists.** What does
exist is four POSITION assertions (the tail of `FORWARD`, the head of `REVERSE`, and two bounded
`_rollback_paths` selections). The chunk's STOP condition did not trigger; the four were re-anchored to
assert their own property (adjacency / suffix / "nothing at or below the bound") instead of a fixed tuple
length, each with a dated comment saying why:

| test | was | now |
|---|---|---|
| `test_radar_score_migration.py::test_0006_and_0007_are_registered_forward_in_order` | `names[-2:] == [0006, 0007]` | `index(0007) == index(0006) + 1` (the system seam before the user cards that reference it) |
| `test_radar_score_migration.py::test_rollback_selects_0007_then_0006_newest_first` | `REVERSE[:2] == …` | adjacency in REVERSE + suffix of each bounded selection + "nothing ≤ the bound" |
| `test_radar_migration.py::test_rollback_selects_only_newer_files_newest_first` | fixed 4-tuple | suffix + "nothing ≤ 0003" + the full filter identity |
| `test_tenancy.py::test_down_to_0004_selects_0007_0006_then_0005_reverse` | fixed 3-tuple | suffix + "nothing ≤ 0004" |

| what the spec asks (§11) | proven by |
|---|---|
| `FORWARD` ends `…0007, 0010, 0011` | `test_forward_ends_0007_0010_0011` |
| `REVERSE` begins `0011, 0010, 0007…` | `test_reverse_begins_0011_0010_0007` |
| each new file has its rollback, both registered | `test_each_new_migration_has_its_rollback_and_both_are_registered` |
| `--down-to 0007` selects exactly the two | `test_rollback_down_to_0007_selects_exactly_the_two_new_files` |
| the 0008/0009 gap is legal | `test_the_registry_is_an_explicit_list_so_the_0008_0009_gap_is_legal` (numeric order asserted, contiguity not) |
| `side_of("archive_progress")` / `("archive_incidents")` are SYSTEM | `test_both_tables_are_declared_system_side` (also asserts `CREATED_TABLES`, so the migrate proof carries them and a rollback reads DROPPED) |
| PK `(ticker, interval)` | `test_progress_carries_its_primary_key_and_the_check` |
| `CHECK (archived_through <= export_newest)` | same test, regex on the DDL |
| the five incident kinds, and only those | `test_incidents_carries_the_five_kinds_and_nothing_else` (set equality on the CHECK's domain) |
| the partial unique index `WHERE resolved_at IS NULL` | `test_incidents_has_the_partial_unique_index_on_unresolved_rows` |
| NO grant to `cobalt_user` | `test_nothing_is_granted_to_cobalt_user` — the string does not appear in ANY of the four files |
| 0006's ownership/grant pattern | `test_each_table_is_owned_by_the_system_role` + `test_the_incident_sequence_is_granted_to_the_system_role` |
| additive, rollback = drop own table | `test_*_rollback_drops_only_its_own_table` (`count("DROP") == 1`) + `test_neither_migration_touches_bars_or_any_existing_object` |

DESIGN DECISION taken inside the spec's words, recorded: the partial unique index carries
**`NULLS NOT DISTINCT`** (Postgres 15+; this install is pg16). §11 says "ONE unresolved row per
`(kind, ticker, interval, range_start)`", and an `empty_export` incident has no span — under the DEFAULT
NULL rule a target failing empty for a month would open thirty rows for one condition.

`requires_db` WRITTEN, NEVER RUN (10 tests): forward creates both on the system side and neither
user-side · migrate twice is idempotent · `--down-to 0007` drops exactly those two, every other
`CREATED_TABLES` relation survives, forward again restores them · owner is `cobalt_system` (×2) ·
`cobalt_user` has no SELECT privilege (×2) · the `archived_through <= export_newest` CHECK refuses ·
one unresolved row per key, a second allowed after resolution · the `kind` domain is enforced by the
database.

SUITE: **`1657 passed, 307 skipped, 1 xfailed, 15 warnings in 41.88s`**. Against BASELINE: failed 0 →
0 · passed 1562 → 1657 (+95: 47 chunk S + 48 chunk M) · skipped 297 → 307 (+10, all `requires_db`).

## Chunk R — the pure core: `reconcile.py` (spec §3 V2-3, §4, §6, §7)

RED FIRST: `uv run pytest -q tests/cobalt/test_archiver_reconcile.py` before the module →
`ModuleNotFoundError: No module named 'cobalt.archiver.reconcile'`, `1 error in 0.14s`.
Then GREEN: **`66 passed in 0.11s`**.

Two of my own test-authoring defects were found on the first green run and fixed (both in the TEST, not
in the module): Grok's 100-key fixture started at 15:00 ET so 34 of its bars had not closed by the 20:30
fetch, and the purity test asserted on the module's PROSE (the docstring names `BarStore` while
explaining why `max(ts)` is the wrong watermark). The purity test now asserts on the **AST**: the module
may import only `__future__`, `datetime`, `decimal`, `enum`, `typing`, `zoneinfo`, `pydantic` and its own
`models`, and may not call `now()`, `utcnow()`, `today()`, `open()`, `read_text()` or `execute()`.

| §15 list | tests |
|---|---|
| TIME — regular close | `test_regular_close_the_1959_i1_bar_completes_at_2000_et` (ET 19:59 = UTC 23:59; closes UTC 00:00) |
| 13:00 half-day incl. the i30 12:30 bar | `test_half_day_the_i30_bar_opening_1230_completes_at_1300_et` |
| extended hours | `test_extended_hours_bars_are_ordinary_bars_to_this_module` (premarket 04:00, RTH, aftermarket 19:59) |
| Thanksgiving Thursday + Friday half-day | `test_thanksgiving_thursday_has_no_bars_and_friday_is_a_half_day` (2026: Thu 11-26, Fri 11-27) |
| weekend | `test_a_weekend_is_simply_two_dates_the_export_does_not_carry` |
| 09-07 → 09-08 holiday | `test_the_0907_holiday_is_skipped_and_0908_is_the_next_session` |
| both DST dates | `test_spring_forward_2026_03_08_…`, `test_fall_back_2026_11_01_…` — ET dates AND UTC instants asserted |
| a fetch crossing a bar close | `test_a_fetch_that_crosses_a_bar_close_excludes_that_bar` |
| unknown interval fails loud | `test_an_unknown_interval_fails_loud` (6 cases) |
| RANGE — union of (a) and (b), bootstrap = whole export | `test_bootstrap_takes_the_whole_eligible_export`, `test_steady_state_is_the_union_of_newer_than_progress_and_range_b`, `test_range_b_reaches_back_even_when_progress_is_ahead_of_it`, `test_todays_date_is_in_range_b_…` |
| the four ROUND-2 SEQUENCES, dated | `test_gemini_monday_1400_restoration_seen_on_tuesday` · `test_astra_friday_1002_late_addition_appears_after_a_weekend` · `test_grok_nvda_wednesday_1017_appears_on_thursday` · `test_the_gap_a_poller_backfill_would_have_hidden_msft_0827_to_0904` (+ `test_a_progress_row_survives_a_ticker_leaving_and_returning`, sequence #8) |
| the poller's `max(ts)` never enters a decision | `test_the_poller_maximum_never_enters_any_decision` — three different watermarks, byte-identical decisions |
| REGRESSION / ILLIQUID | THIN unchanged three sessions = SUCCESS · strict regression = FAILED with the evidence · IMCC future-dated row then valid export · half-day is not truncation |
| GAP (`export_oldest > archived_through`) | `test_a_gap_opens_when_the_export_starts_after_the_watermark` (incident BEFORE progress advances, DEGRADED, usable range still appended) + `test_no_gap_on_a_bootstrap_the_report_says_unassessed_instead` |
| COUNTERS | Grok's 100-key case · Astra's AAPL/i5 case · MSFT 19:59 new-not-late · MSFT 19:59 equal = **1 / 1 / 0** · complete withholding · a counted conflict · `late == 0` on a bootstrap · `invalid` survives as a counter |
| normalisation to `NUMERIC(14,4)` / integer volume | `test_normalisation_…`, `test_equal_after_normalisation_is_not_a_difference` |
| never an automatic repair | `test_nothing_is_ever_repaired_automatically` — a whole-export constant-factor (split-like) difference is still a withholding |

IDENTITIES IN THE OBJECT (L57, L1): `TargetCounts` carries §7's five identities in its own
`model_validator`, and `TargetPlan.counts(inserted=…, concurrent_conflicts=…)` is the ONLY way to build
one. `test_a_non_reconciling_count_cannot_be_constructed` (3 cases) and two direct-construction tests
prove a night that cannot explain itself raises rather than renders.

Diff stat (chunk R): `src/cobalt/archiver/reconcile.py` +703 (new),
`tests/cobalt/test_archiver_reconcile.py` +800 (new),
`docs/40 - DevDocs/cobalt/archiver/reconcile.md` +143 (new).

SUITE: **`1723 passed, 307 skipped, 1 xfailed, 15 warnings in 41.92s`**. Against BASELINE: failed 0 → 0 ·
passed 1562 → 1723 (+161: 47 S + 48 M + 66 R) · skipped 307, unchanged (chunk R adds no `requires_db`
test — the whole chunk is pure).

## Chunk P — store methods on ONE connection (spec §3 V2-1, §4, §9, §11)

RED FIRST: `uv run pytest -q tests/cobalt/test_archiver_append_store.py` before the code →
`ImportError: cannot import name 'incidents' from 'cobalt.archiver'`, `1 error in 0.11s`.
Then GREEN: **`32 passed, 8 skipped in 0.06s`**.

**`upsert_bars` IS BYTE-IDENTICAL TO MAIN.** Quoted verbatim:

```
$ git diff main --stat -- src/cobalt/archiver/store.py
 src/cobalt/archiver/store.py | 148 +++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 148 insertions(+)
```

**0 deletions** — additions only, as the chunk requires. (The new `Interval` import is on its own line
for exactly this reason; extending the existing `from .models import Bar` line would have shown as a
deletion.) Two tests pin the method beyond the diff: `DO UPDATE SET` present and `DO NOTHING` absent in
its CODE, `return len(rows)`, and the signature `(self, bars, *, before_commit)` unchanged.

| what the spec asks | proven by |
|---|---|
| `insert_new_bars` sends `ON CONFLICT (ticker, interval, ts) DO NOTHING` | `test_insert_new_bars_uses_do_nothing_on_the_primary_key` (and `DO UPDATE` absent) |
| counts ACTUAL inserts, never `len(rows)` | `test_insert_new_bars_counts_actual_inserts_not_rows_sent` — 3 bars sent, driver says 1, method returns **1** |
| a row count the driver cannot give FAILS | `test_insert_new_bars_refuses_a_row_count_the_driver_did_not_give` (L1) |
| never opens or commits a connection | `test_insert_new_bars_never_opens_or_commits_a_connection` + the `no_connections` fixture, which makes `BarStore._connect` itself an assertion failure for EVERY offline test in the file |
| one statement for the whole batch | `test_insert_new_bars_sends_one_statement_for_the_whole_batch` |
| the range read takes `conn`, is ONE private method (O-5) | `test_the_range_read_is_one_private_method_that_takes_a_connection`, `test_there_is_exactly_one_range_read_on_the_store` (asserts the store has exactly `["_bars_in_range"]`), `test_the_range_read_is_parameterised_never_interpolated` |
| progress upsert uses `GREATEST`, takes `conn`, only on an accepted outcome | `test_progress_is_written_with_greatest_and_takes_the_connection`, `test_progress_refuses_to_write_for_a_target_that_was_not_accepted` (the writer RAISES and sends no statement), `test_progress_sends_the_bar_timestamp_never_a_clock_time` |
| a progress row is never deleted | `test_progress_rows_are_never_deleted_by_this_module` (over the CODE, docstrings stripped) |
| incident open-or-refresh takes `conn`, never duplicates | `test_an_incident_is_opened_or_refreshed_never_duplicated` — asserts `ON CONFLICT (kind, ticker, interval, range_start) WHERE resolved_at IS NULL` |
| a refresh moves `last_seen_at`, never `first_seen_at` | `test_a_refresh_moves_last_seen_at_and_never_first_seen_at` (splits on `DO UPDATE SET`) |
| every kind the pure core can raise is writable | parametrized over all 5 of `IncidentKind` |
| read-only commands mutate nothing | `test_listing_unresolved_incidents_writes_nothing` |
| resolution is explicit and audited | `test_resolving_an_incident_is_explicit_and_audited`, `test_resolve_refuses_an_empty_who` |
| the lock: ONE constant key, SESSION level | `test_the_lock_key_is_one_constant`, `test_the_lock_is_session_level_not_transaction_level` (no `pg_try_advisory_xact_lock`), `test_acquiring_the_lock_asks_the_server_once` |
| a second holder refuses loudly | `test_a_second_holder_is_refused_loudly` — "another archive/repair run holds the lock" |

Four assertions failed on the first green run because they searched the raw SOURCE and found the module's
own PROSE (`upsert_bars`'s docstring explains why it is `DO UPDATE` **rather than** `DO NOTHING`; the lock
helper's docstring names `pg_try_advisory_xact_lock` to say why it is not used). A `code_of()` helper now
strips docstrings and comments via `ast.unparse`, so those four assert on CODE. No production behaviour
changed.

`requires_db` WRITTEN, NEVER RUN (8 tests): the append path never modifies an existing row · a
poller-style insert between the range read and the insert is a counted conflict, not an error · a crash
after the inserts leaves neither bars nor progress · the retry is idempotent · a second holder of the
advisory lock refuses and the lock is re-takeable after release · progress and an incident commit with
the bars or not at all · progress is monotonic across accepted runs (`GREATEST` refuses to move it back)
· a recurring incident refreshes rather than duplicating (`first_seen_at` held, `last_seen_at` moved).

SPEC vs CODE (this chunk): `reconcile.TargetPlan` gained `fetch_started_at`. The spec's §11 column list
requires it on the progress row and §2's read of the code does not carry it on the plan — a pure
addition, no decision changed.

SUITE: **`1755 passed, 315 skipped, 1 xfailed, 15 warnings in 41.83s`**. Against BASELINE: failed 0 → 0 ·
passed 1562 → 1755 (+193: 47 S + 48 M + 66 R + 32 P) · skipped 297 → 315 (+18 `requires_db`: 10 M + 8 P).

## Chunk N — the runner: mode isolation, the shadow compare, the append night (spec §5, §6, §7, §9)

RED FIRST: `uv run pytest -q tests/cobalt/test_archiver_runner.py` (a NEW file — there was no runner test
in this repo) → `ImportError: cannot import name 'shadow' from 'cobalt.archiver'`, `1 error in 0.19s`.
Then GREEN: **`45 passed in 0.15s`**.

### Mode isolation, differential against today's behaviour

| §5 / §15 requirement | test |
|---|---|
| night 1 AND night 2 send the WHOLE export to `upsert_bars` | `test_upsert_sends_the_whole_export_on_every_night` (parametrized 1, 2) — asserts `sent == export`, unfiltered |
| the incomplete latest bar is kept | `test_upsert_keeps_the_incomplete_latest_bar` |
| no progress, no incident, no `insert_new_bars` | `test_upsert_writes_no_progress_and_no_incident` |
| today's failure on an empty export | `test_upsert_keeps_todays_failure_on_an_empty_export` — and NO incident is opened in upsert mode |
| the submitted-row count | `test_upsert_keeps_the_submitted_row_count` |
| the run-report row byte for byte | `test_upsert_keeps_the_run_report_row_byte_for_byte` — 8 columns (9 pipes), and `APPEND_COLUMNS` must NOT appear |
| **the COMPLETE list of additions, pinned** | `test_the_complete_list_of_upsert_mode_additions_is_pinned` — asserts the fake store's recorded call sequence EXACTLY with the shadow off (`run_lock, ensure_schema, upsert_bars`) and on (`+ target_transaction, conn.execute(set_config), _bars_in_range`), plus `job_result()`'s key set. **A fourth addition fails it.** |
| `_run_targets(mode=…)` still means the report scope | `test_run_targets_mode_still_means_the_report_scope` |
| the lock in BOTH modes, a second run refuses | `test_the_run_level_lock_is_taken_in_both_write_modes`, `test_a_second_run_refuses_on_the_lock` (and writes nothing) |

### The shadow compare

Runs after the fetch and BEFORE the write (`test_the_shadow_runs_after_the_fetch_and_before_the_write`
asserts the index of `_bars_in_range` < that of `upsert_bars`), labelled `pre-write`, and:

- an exception and a timeout each leave the target's upsert and the summary IDENTICAL to a shadow-off
  night (`test_a_shadow_failure_leaves_the_target_and_the_summary_identical`, parametrized), with
  `shadow_errors == 1`; a slow read is the same path (`test_a_slow_shadow_read_does_not_slow_the_write_path`);
- it calls NO write method of the store (`test_the_shadow_writes_nothing_to_the_database`);
- both scopes are reported (`test_the_shadow_reports_both_scopes`: bootstrap 4 candidates, steady-state 3);
- field-level differences after normalisation, and an equal RENDERING is not a difference
  (`test_the_shadow_records_field_level_differences_after_normalisation`, `test_an_equal_rendering_is_not_recorded_as_a_difference`);
- artifact schema (`test_the_artifact_is_json_lines_with_the_recorded_schema` — every §5 field asserted by name);
- retention (`test_retention_deletes_only_nights_older_than_the_window` — by FILENAME date, not mtime);
- `shadow-report`'s persisted / vanished / appeared across nights (`test_shadow_report_says_which_differences_persisted_vanished_and_appeared`);
- `shadow_compare: off` skips it entirely, and no `shadow` key reaches the job result;
- the aggregate reaches `job.result["shadow"]` with by-interval, poller-writable vs archiver-only,
  volume-only vs any-OHLC, late and new.

### The append night

bootstrap · steady state · a withheld target (no insert, progress frozen, target FAILED, **incident
persisted in a SECOND transaction opened after the first was rolled back** — asserted by index) · a gap
(**incident written BEFORE progress advances** — asserted by index; DEGRADED; the usable range still
appended) · a regression · `inserted = 0` = SUCCESS · an empty export → FAILED + `empty_export` incident ·
two failed nights then a success · the run continues after a failed target · FAILED **and** DEGRADED →
`healthy is False`, while an `upsert` night stays healthy (`degraded` is an append-mode verdict) ·
`Rows Written` = `inserted` · a concurrent conflict is counted and the identity closes · the append report
row has 14 columns, its schema break is written ONCE, and a return to `upsert` opens its own table again.

### Two defects found by the tests and fixed in the CODE

1. **`report._current_header` used a substring search.** `COLUMNS` is a PREFIX of `APPEND_COLUMNS`, so
   `find` reported both at the same offset, every append night read as an upsert file, and a fresh schema
   break was written above EVERY row (3 of them in a 3-row test). Now it scans whole LINES backwards.
2. **`test_finviz_consumers.py::test_every_finviz_consumer_is_in_the_total_demand_inventory` went red.**
   The `fetch=` test seam replaced the literal `fetch_bars(...)` call with `fetch_fn(...)`, so L53's
   total-demand inventory scan stopped seeing `archiver/runner.py` as a Finviz consumer — while the module
   went on sending exactly as many requests. Fixed by making the default an explicit named wrapper
   `_default_fetch` that calls `fetch_bars(...)`. **The guard was not weakened**; the module was made
   honest to it.

SPEC vs CODE (this chunk): §5 asks the shadow record to carry "poller member yes/no". The archiver's night
does not query the radar's tables, so the field is `poller_writable`, decided from the INTERVAL — the
poller writes i1 and only i1 (`radar/poller.py:88`). It answers "could the poller write this target at
all", not "was this ticker a pool member tonight". ESCALATE 5.

SUITE: **`1800 passed, 315 skipped, 1 xfailed, 15 warnings in 42.21s`**. Against BASELINE: failed 0 → 0 ·
passed 1562 → 1800 (+238: 47 S + 48 M + 66 R + 32 P + 45 N) · skipped 315, unchanged (chunk N adds no
`requires_db` test — the whole chunk runs on fakes).

## Chunk Q — the quiet window and the commands (spec §8, §6, §3 V3-7)

RED FIRST: `uv run pytest -q tests/cobalt/test_archiver_quiet.py` before the code →
`ImportError: cannot import name 'cli' from 'cobalt.archiver'`, `1 error in 0.11s`.
Then GREEN: **`39 passed in 0.13s`**.

**`git diff main -- src/cobalt/radar/` → EMPTY (no output).** R8's core condition holds: the live poller
and every other radar file are untouched by this branch. A second test asserts it from inside the suite —
`test_the_poller_module_is_imported_never_edited` — by checking the poller's source knows nothing of
`archive_progress`, `archive_incidents`, `quiet` or `ARCHIVE_RUN_LOCK_KEY`.

| §8 / §15 requirement | test |
|---|---|
| Q1 refuses alone, in every scanned session | `test_q1_every_non_overnight_session_refuses_alone` (4 sessions) |
| `MARKET_RESET` is NOT quiet | `test_market_reset_is_not_quiet` — "the radar is PAUSED there, not idle" |
| Q2 refuses alone; exact boundary allowed | `test_q2_refuses_alone_when_the_next_scanning_open_is_too_close`, `test_q2_allows_exactly_the_configured_distance` |
| Q3 refuses alone; exact derived bound allowed | `test_q3_refuses_alone_when_the_derived_cycle_finish_is_too_recent` (34 min), `test_q3_allows_exactly_the_derived_bound` (35 min) |
| a missing pool row / NULL `last_scan_at` REFUSES | `test_a_missing_pool_row_refuses_because_quiet_cannot_be_PROVEN`, `test_a_null_last_scan_at_refuses_the_same_way` — both carry "cannot prove the radar is quiet" |
| the refusal text carries every observed value | `test_the_refusal_names_every_observed_value_and_the_earliest_start` — session, last scan start + age + need, next scanning open + distance + need, earliest allowed start, and the preview line; one line per FAILED rule above the summary |
| earliest allowed start | `test_the_earliest_allowed_start_is_the_later_of_the_two_constraints` |
| exit code 2 | `test_the_refusal_exit_code_is_two` |
| **NO `--force`** | `test_there_is_no_force_flag_anywhere` — the parser rejects it on BOTH repairs, and the string is absent from `cli.py`'s and `quiet.py`'s CODE (docstrings stripped: both files say in prose that there is none) |
| **`test_gemini_close_boundary_poller_lag`** | named exactly as §8 titles it. (i) normal 20:00 → refused by Q1 (`market_reset`); (ii) early-close 17:00 → OVERNIGHT, so Q3 is the whole protection and the repair is refused with "1 min ago"; (iii) the literal 16:00 → RTH, refused by Q1. **Asserts NO bar row changed.** |
| **`test_astra_open_boundary_repair_crosses_open`** | 03:59:50 refused at START by Q2; 03:49:59 PASSES the start check and the same repair at its 03:50:05 commit does not. **Asserts NO bar row changed.** |
| the PRE-COMMIT re-check rolls back | `test_the_pre_commit_recheck_rolls_the_repair_back` — a two-instant clock, a transaction with real rollback semantics, and the row restored |
| both repairs refused in every scanned session | `test_both_mutating_commands_are_refused_in_every_scanned_session` (2 × 4) |
| previews always run | `test_previews_always_run`, `test_the_read_only_commands_are_the_ones_the_design_names` |
| `backfill-missing` can only DO NOTHING | `test_backfill_missing_can_only_do_nothing` (`upsert_bars` absent from its handler) + `test_backfill_missing_never_calls_upsert_bars` (a differing key is left exactly as it is) |
| `restate --apply` needs `--reason`, audit on an incident row | `test_restate_apply_requires_a_reason`, `test_restate_without_apply_is_a_preview`; the handler opens a `restated` incident carrying the reason (spec O-4) |
| every read-only command calls no write method | `test_every_read_only_command_calls_no_write_method` — over all four handlers' source |
| `incidents resolve` is explicit and audited | `test_incidents_resolve_is_explicit_and_audited` (`--by` and `--note` both required) |
| `audit --from`, `shadow-report --nights` | `test_audit_is_read_only_and_takes_a_from_date`, `test_shadow_report_takes_a_night_count` |
| **Known limit 1, DEMONSTRATED** | `test_known_limit_1_the_poller_keeps_writing_while_a_restated_incident_is_open` — IMPORTS `cobalt.radar.poller`, drives a real `BarPoller`, and shows a new-basis i1 bar landing beside old-basis history. It does not edit the poller. |

`src/cobalt/cli.py` gains ONE new block — `archiver_cli.add_parser(sub)` at the END of the subparser
group, plus one import line. No neighbour's lines were reflowed (`ops-0919` edits `:214-221`, a different
region).

**A THIRD L53 FINDING, handled not papered over.** `test_finviz_consumers.py` went red: `archiver/cli.py`
is a NEW Finviz consumer (`restate` / `backfill-missing` re-fetch one target to compare it against
storage). The test is L53's total-demand inventory and it did exactly its job. The module is now
registered with an honest description — "CLI, by hand, one target, no bucket" — and the strict-xfail
`test_no_finviz_request_bypasses_the_shared_gate` still fails as expected. **This is a real demand change
and goes to the deploy prompt** (ESCALATE 4).

SUITE: **`1839 passed, 315 skipped, 1 xfailed, 15 warnings in 42.32s`**. Against BASELINE: failed 0 → 0 ·
passed 1562 → 1839 (+277: 47 S + 48 M + 66 R + 32 P + 45 N + 39 Q) · skipped 315, unchanged.

## Chunk H — heartbeat and docs (spec §11, O-7)

RED FIRST: `uv run pytest -q tests/cobalt/test_heartbeat_archiver_incidents.py` before the probe change →
**`11 failed in 0.15s`** (`TypeError: archiver_freshness() got an unexpected keyword argument 'incidents'`
×10, plus the source assertion). Then GREEN: **`64 passed in 6.55s`** for
`test_heartbeat_archiver_incidents.py` + `test_heartbeat.py` + `test_heartbeat_runner.py` together.

| requirement | test |
|---|---|
| not green while an unresolved incident exists | `test_one_unresolved_incident_is_not_green` |
| the detail names the count and the oldest kind | `test_the_detail_names_the_count_and_the_oldest_kind` — 3 incidents, "oldest restated", the target, the date, and the tally `gap=2, restated=1`; the run's own line survives |
| it points at the command that lists them | `test_the_detail_points_at_the_command_that_lists_them` |
| zero incidents → **exactly** today's result | `test_zero_incidents_is_exactly_todays_result` — asserted by **IDENTITY** (`_with_archive_incidents(base, reader) is base`), not equality |
| a red run keeps its own reason | `test_a_red_run_stays_red_with_its_own_reason` |
| a missing table → LOUD, naming the migration | `test_an_unreadable_incident_table_is_a_loud_probe_failure` (2 error shapes) — names `archive_incidents`, `0011_archive_incidents.sql` and `cobalt db migrate` |
| never green | same test (`ok is False`) |
| never a crash of the heartbeat run | `test_an_unreadable_incident_table_does_not_crash_the_heartbeat_run` — it returns a red Probe, it does not raise |
| the run detail survives the failure | `test_the_run_detail_survives_an_unreadable_incident_table` |
| the production reader is the archiver's own read-only query | `test_the_default_reader_is_the_archivers_own_unresolved_query` — and reaches no writer |

`heartbeat/probes.py` changed in ONE probe only. `archiver_freshness` splits into
`_archiver_run_probe` (today's verdict on the last RUN, unchanged) and `_with_archive_incidents` (the
fold), with `_read_archive_incidents` as the production reader and `incidents=` as the test seam.

ONE PRE-EXISTING FILE TOUCHED: `tests/cobalt/test_heartbeat.py` gains an autouse fixture pinning
`_read_archive_incidents` to "no incidents". That file is about RUN FRESHNESS and has never had a
database; without the pin the probe correctly refuses to call anything green when its own alarm is
unreadable, and 5 of its tests would have gone red for a reason that is not theirs. **No test of its was
changed or weakened** — the incident behaviour, including the unreadable case, lives in the new file.

DevDocs: `heartbeat/probes.md` (the 09-19 section) and **`archiver/__init__.md` gains the operator's
page** — the two modes, what a shadow night writes, how to read `shadow-report` (persisted / vanished /
appeared, and why a post-write audit cannot produce them), the quiet window in plain words, the command
table, and **the five known limits of spec §12 VERBATIM**.

SUITE: **`1850 passed, 315 skipped, 1 xfailed, 15 warnings in 43.02s`**. Against BASELINE: failed 0 → 0 ·
passed 1562 → 1850 (+288: 47 S + 48 M + 66 R + 32 P + 45 N + 39 Q + 11 H) · skipped 315, unchanged.

## Close (offline)

### Suite against BASELINE

| | BASELINE | CLOSE |
|---|---|---|
| passed | 1562 | **1850** (+288) |
| skipped | 297 | **315** (+18, every one a `requires_db` test written here) |
| failed | 0 | **0** |
| xfailed | 1 | 1 (unchanged — `test_no_finviz_request_bypasses_the_shared_gate`, strict) |

This build's tests, by file (306 collected = 288 passed + 18 skipped):

| chunk | file | tests |
|---|---|---|
| S | `tests/cobalt/test_archiver_settings.py` | 47 |
| M | `tests/cobalt/test_archiver_migrations.py` | 48 + **10 `requires_db`** |
| R | `tests/cobalt/test_archiver_reconcile.py` | 66 |
| P | `tests/cobalt/test_archiver_append_store.py` | 32 + **8 `requires_db`** |
| N | `tests/cobalt/test_archiver_runner.py` | 45 |
| Q | `tests/cobalt/test_archiver_quiet.py` | 39 |
| H | `tests/cobalt/test_heartbeat_archiver_incidents.py` | 11 |

The 18 `requires_db` tests, by name — **none has ever run**:

`test_archiver_migrations.py`: `test_forward_creates_both_tables_on_the_system_side` ·
`test_migrate_twice_is_idempotent_for_the_two_new_tables` ·
`test_rollback_down_to_0007_drops_exactly_those_two_and_nothing_else` ·
`test_owner_is_the_system_role[archive_progress]` · `[archive_incidents]` ·
`test_the_user_role_has_no_grant_on_either_table[archive_progress]` · `[archive_incidents]` ·
`test_the_check_refuses_progress_past_its_own_export` ·
`test_one_unresolved_incident_per_key_then_a_second_after_resolution` ·
`test_the_kind_domain_is_enforced_by_the_database`

`test_archiver_append_store.py`: `test_the_append_path_never_modifies_an_existing_row` ·
`test_a_poller_style_insert_between_the_read_and_the_insert_is_a_counted_conflict` ·
`test_a_crash_after_the_inserts_leaves_neither_bars_nor_progress` ·
`test_the_retry_after_a_crash_is_idempotent` ·
`test_a_second_holder_of_the_advisory_lock_refuses` ·
`test_progress_and_an_incident_commit_with_the_bars_or_not_at_all` ·
`test_progress_is_monotonic_across_accepted_runs` ·
`test_a_recurring_incident_refreshes_rather_than_duplicating`

### The two gates named by the close step

- **L45 leak scan**: `tests/cobalt/test_radar_notes.py::test_screen_filter_values_live_only_in_approved_radar_fixtures`
  → `1 passed in 0.11s`. It covers `docs/40 - DevDocs`, `src/cobalt`, `configs/cobalt`, `tests/cobalt`
  and `ops`, i.e. every tree this build wrote to.
- **DevDocs symbol check**: **IT DOES NOT EXIST IN THIS REPO.** Searched `src/cobalt`, `dev_utils` and
  `tests/` for `symbol check` / `symbol-check` / `symbol_check` (0 hits outside prompt files) and for
  `symbol` (13 files, every hit a ticker symbol or the predicate grammar's "symbol" atom). This is the
  same finding `reports/alerts-transition-2026-09-14.md:90` recorded: "A DevDocs symbol-check gate was
  searched for in `src/`, `dev_utils/` and `tests/` and was not found, so it did not run." ESCALATE 2.

### RESTARTS (L42)

`uv run cobalt jobs restarts main..HEAD` — 53 rows, **0 UNCLASSIFIED**. Every `docs/` path classified
`DOCS → -`; every test path `test/documentation; no resident → -`; the four `.sql` files
`non-Python src asset → -`.

```
RESTARTS: com.cobalt.aset com.cobalt.radar
```

Derived, not judged: `configs/cobalt/taxonomy/tunables.yaml` M → `resident reads` →
`com.cobalt.aset,com.cobalt.radar`, and the new-core Python files → `static import reach` →
`com.cobalt.radar` (+ `com.cobalt.aset` for `reconcile.py` and `store.py`).

NOTE on the table's extra rows: `main` moved while this run was building (from `8838dda` when the
worktree was cut to `0569727` now — desk doc commits). `main..HEAD` therefore also lists six
`prompts/2026-09-19/18-*` paths and `reports/cto-2026-09-19.md` as deletions. **Those are main's own
later commits, not this branch's changes**, they are all `DOCS → -`, and the `RESTARTS:` line is
unaffected.

### Commits (one per chunk + the report's own updates folded into each)

```
c974fbf feat(heartbeat): the archiver probe sees unresolved archive incidents; archiver operator docs
f4bdcfa feat(archiver): repairs only in a quiet window (R8 option A) — restate, backfill-missing, audit, incidents, progress, shadow-report
2b4893c feat(archiver): write_mode dispatch — upsert untouched, pre-write shadow compare, the append night
4e3c577 feat(archiver): append path — insert_new_bars, progress and incident writers on the target's one transaction; run-level advisory lock
72bfd21 feat(archiver): reconcile — eligibility, candidate range, four-way comparison, regression/gap rules, reconciling counters (pure)
b623e72 feat(db): 0010 archive_progress + 0011 archive_incidents — additive, system side, rollback = drop own table
54e98f7 feat(archiver): ArchiverSettings — write_mode upsert|append (ships upsert), shadow and quiet-window keys, validated on load
```

The report file is committed with each chunk rather than once at the end (L48: evidence in the report
file in the SAME turn as the work), plus a final `docs(report):` commit for these closing sections.

### Paths

`git diff --stat 8838dda HEAD` (this branch's BASE — the honest set of what this build changed):
**46 files, 9100 insertions, 38 deletions.** Every path is under

- `configs/cobalt/taxonomy/tunables.yaml` (1)
- `docs/40 - DevDocs/` (16)
- `src/cobalt/archiver/` (10)
- `src/cobalt/db_migrations/` (6)
- `src/cobalt/heartbeat/probes.py` (1)
- `src/cobalt/cli.py` (1)
- `tests/cobalt/` (11)

**No path under `src/cobalt/radar/`.** The 38 deletions are the four pre-existing migration position
assertions being re-anchored (chunk M) and the lines `report.py` / `runner.py` / `probes.py` rewrote
inside their own functions.

```
$ git diff main -- src/cobalt/radar/
(no output)
```

**EMPTY.** R8's core condition holds.

## SPEC vs CODE

Where this build's reading of the code differs from the spec's §2, or where the spec left a shape to
the builder, THE CODE WON and the difference is here.

| # | spec says | the code / this build |
|---|---|---|
| 1 | §11 names the progress columns, and §2's read of the code does not carry the fetch instant on the decision object | `reconcile.TargetPlan` gained `fetch_started_at`. A pure addition; no decision changed. |
| 2 | §5: the shadow record carries "poller member yes/no" | The archiver's night does not query the radar's tables, so the field is `poller_writable`, decided from the INTERVAL — the poller writes i1 and only i1 (`radar/poller.py:88`). It answers "could the poller write this target at all", not "was this ticker a pool member tonight". |
| 3 | §7: an EMPTY export is already a `CollectorError` today; in append mode ADDITIONALLY an `empty_export` incident | The collector raises the SAME `CollectorError` class for an empty response (`collector.py:133`), a header-only response (`:143`), an unparseable row (`:146-170`) AND a transport failure (`:201`). Without changing `collector.py` — outside this chunk's scope and a behaviour the spec keeps — a transport failure in append mode also opens an `empty_export` incident, carrying the collector's scrubbed message in `detail`. ESCALATE 6. |
| 4 | §11: ONE unresolved row per `(kind, ticker, interval, range_start)` | An `empty_export` incident has no span, so `range_start` is NULL, and the DEFAULT NULL rule would make every night's row distinct. The index carries **`NULLS NOT DISTINCT`** (Postgres 15+; this install is pg16). |
| 5 | §8: `cycle_max_min` derives the cycle's completion | Confirmed against the code: `radar/runner.py:171` stamps the cycle's START into `last_scan_at` and the COMPLETION instant is persisted nowhere. The derivation stands, and so does the dissent (§13, O-2). |
| 6 | §7: `inserted = 0` is SUCCESS | CHECKED against `heartbeat.probes.archiver_freshness`, which calls a run with `rows_written == 0` RED. No conflict: §7's rule is PER TARGET, the probe's is per RUN. A night where every target legitimately inserted nothing across ~1,000 targets would be a real anomaly; a night where every target was WITHHELD is already red through `failures`. |
| 7 | §2: "no `cobalt archiver` subcommand exists" | Still true on main; this build adds the group as ONE new block at the end of `cli.py`'s subparser list. The `archiver` script entry point in `pyproject.toml` is untouched and still runs the nightly job. |

## ESCALATE

**(i) The spec's §14 OPEN items, carried untouched, with what was BUILT as the safe default.**

| # | item | who decides | built as |
|---|---|---|---|
| O-1 | N, the number of shadow nights before the switch ruling (PROPOSED 5 trading nights) | the OWNER | nothing switches without his ruling; `archiver.write_mode` ships `upsert` and a test pins it |
| O-2 | `archiver.repair.cycle_max_min` (PROPOSED 30) — a cycle's COMPLETION is not persisted, so Q3 derives it from start + an upper bound | the DESK (value now); Sunday's design (any radar change) | **30**, `status: proposed`, and a REFUSAL when the pool row cannot be read. The alternative (the radar stamping a completion instant) touches the live radar's write path and is NOT in this build. |
| O-3 | the three deliberate additions to an `upsert` night — the advisory lock means a manual `--backfill` during the nightly run now REFUSES instead of interleaving | the DESK | as listed, and **pinned by a test that fails if a fourth appears** |
| O-4 | where a repair's audit trail lives when no incident exists | the DESK | `restate --apply` opens-and-carries a `restated` incident holding the operator's `--reason`; `--reason` is MANDATORY with `--apply` and the parser enforces it |
| O-5 | cross-branch L3: `sprint-2/p4` adds `BarStore.bars_between()` (own connection); this build needs a range read ON THE TARGET'S CONNECTION | the DESK at integration | this branch adds exactly **ONE** private read, `_bars_in_range(conn, …)`, and a test asserts the store has no other. **The second lander folds the two into one method taking an optional connection.** |
| O-6 | whether the shadow's whole-export read every night is acceptable to the owner for N nights | the OWNER, with O-1 | `archiver.shadow_compare: on`, `status: proposed`; the key turns it off **without a deploy of code** |
| O-7 | heartbeat wording and colour for DEGRADED vs FAILED nights | the DESK | not green = the probe's existing FAIL form; the detail names the count, the oldest kind with its target and first-seen date, the tally by kind, and `cobalt archiver incidents` |

**(ii) THE `requires_db` TESTS HAVE NEVER RUN.** 18 of them, written and skipping cleanly offline
(a collection error would have been a failure; none occurred). **Their first run on `cobalt_dev` is OWED
before this branch may deploy** — `p4-verify-0919` holds that lane today.

**(iii) Cross-branch.** Files this branch shares with unmerged work:

| file | also changed by | this branch's edit |
|---|---|---|
| `src/cobalt/db_migrations/__init__.py` | `sprint-2/p4` (0008/0009) | new tuple entries only |
| `src/cobalt/db_migrations/placement.py` | `sprint-2/p4` | two new dict rows at the END of the radar/archiver group |
| `configs/cobalt/taxonomy/tunables.yaml` | `sprint-2/p4` | a new block before the S2-P2 card rows |
| `src/cobalt/cli.py` | `sprint-2/p4`, `ops/2026-09-19` (`:214-221`) | ONE import line + ONE `add_parser` line at the END of the group |
| `src/cobalt/archiver/runner.py` | `sprint-2/p4` (`_check_demand(targets, mode)` at the top of `_run_targets`) | `_run_targets` is REWRITTEN here (mode dispatch). **P4's `_check_demand` call must be re-applied at the top of the new `_run_targets`, before the lock.** |
| `src/cobalt/archiver/store.py` | `sprint-2/p4` (`bars_between`) | additions only; see O-5 |
| `src/cobalt/db_migrations/cli.py` | `ops/2026-09-19` | **not touched here** |

Migration numbers: **0010/0011 here, 0008/0009 on `sprint-2/p4`.** The gap is legal (explicit tuple, no
contiguity test — searched). **The branch that lands SECOND rebases and keeps BOTH sets in numeric
order, and the integrated suite on the combined tree is the gate.** Four pre-existing position
assertions were re-anchored here (chunk M); P4 will meet the re-anchored versions, which are the ones
that survive a growing registry.

**(iv) For the DEPLOY PROMPT.**

1. **TWO migrations ship** — `0010_archive_progress.sql` and `0011_archive_incidents.sql`.
   `cobalt db migrate --allow-prod` runs INSIDE the 20:00–21:00 market_reset pause with the residents
   down (L66, L43), and **the proof budget applies**: `_probe_all` now digests two more tables. Both are
   EMPTY on the first run, so the added cost is negligible — but the BEFORE/AFTER proof on
   `system.bars` (8.4 M rows, ≈46 s each) is unchanged and still dominates. Take the `--proof-only`
   preflight before the window, as `db_migrations/cli.py`'s own doc says.
2. `archiver.write_mode` ships **`upsert`**. Nothing about tonight's write path changes.
3. The shadow's FIRST NIGHT is the first nightly run after the deploy. Artifact path:
   **`data/archiver-shadow/<YYYY-MM-DD>.jsonl`**. `data/` is gitignored; **the directory must exist or
   be created by the run** — `write_records` does `mkdir(parents=True, exist_ok=True)`, so no manual
   step is needed, but the deploy should confirm the file appeared the next morning.
4. **RESTARTS: `com.cobalt.aset com.cobalt.radar`** — both read `configs/cobalt/taxonomy/tunables.yaml`,
   which this branch changes. Per L42/L28 the config change and those restarts are ONE action, and per
   L43 `com.cobalt.radar` restarts only inside the pause or in overnight idle.
5. `cobalt validate` now prints the archiver block; run it after the merge as part of the smoke test.
6. **A NEW FINVIZ CONSUMER** — see ESCALATE 4 below. The total-demand plan grows by one by-hand CLI.

**(v) THE FIVE KNOWN LIMITS OF SPEC §12 GO TO THE OWNER *WITH* THE SWITCH RULING.** They are reproduced
verbatim in `docs/40 - DevDocs/cobalt/archiver/__init__.md`'s operator page. Limits 1 and 2 are the
recorded DISSENTS (Astra: the unchanged poller mixes old- and new-basis prices past a withholding;
Gemini + Astra: option A's closing-side protection is a bound, not an exclusion). **Limit 1 is now
EXECUTABLE**: `test_archiver_quiet.py::test_known_limit_1_the_poller_keeps_writing_while_a_restated_incident_is_open`
imports the real `BarPoller` and shows it happening.

---

Found by this build, beyond the spec's own list:

**1. AUTHORIZATION — the launch line's literal `grep -c` test does not pass, and the run proceeded.**
5 of 7 rule strings count 0 in `prompts/2026-09-18/02-ops-2026-09-18.md`. **Every difference is a
NARROWING** and the allowlist is a STRICT SUBSET of what R1 approved as list (2) — the full table is in
`## AUTHORIZATION` above. Verdict taken: not an authorization mismatch. **The desk should either reword
the launch line to quote the committed strings, or reword the test.** The same line is running
`ops-0919`, so the finding is shared.

**2. THE DevDocs SYMBOL-CHECK GATE DOES NOT EXIST.** The close step names it as a suite member; it is not
in `src/`, `dev_utils/` or `tests/`. Third time recorded (`alerts-transition-2026-09-14.md:90`).
Either build it or stop naming it in prompts.

**3. `heartbeat.archiver_freshness` reads TWO facts now, and one of them needs a database offline.**
`tests/cobalt/test_heartbeat.py` has never had one, so an autouse fixture pins the reader there. If a
house prefers the probe to stay green when its own alarm is unreadable, that is a ruling — this build
took L1's reading: unreadable alarm = not green, loud, naming the migration, never a crash.

**4. L53 — `src/cobalt/archiver/cli.py` IS A NEW FINVIZ CONSUMER.** `restate` and `backfill-missing`
re-fetch one target to compare it against storage. `test_finviz_consumers.py` caught it and the module
is now registered with an honest description rather than the guard being widened. By hand, one ticker at
a time, and both `--apply` forms only run OVERNIGHT (the quiet window), when no other consumer is
requesting — but it is a real addition to the total-demand inventory and belongs in the deploy prompt.

**5. `poller_writable` vs "poller member".** See SPEC vs CODE 2. If the houses want true pool
membership on the shadow record, the archiver would have to read `system.radar_membership` during the
nightly run — a new read of the radar's tables, which this build did not take on its own authority.

**6. In append mode a TRANSPORT failure opens an `empty_export` incident.** See SPEC vs CODE 3. The
clean fix is a `CollectorError` subclass raised at `collector.py:133` and `:143` only; it is
behaviour-preserving for every existing catcher but is outside this chunk's named files, so it was not
taken.

**7. `main` moved during this run** (`8838dda` → `0569727`). `git diff --stat main HEAD` therefore lists
seven desk-doc paths as deletions that this branch never touched; `git diff --stat 8838dda HEAD` is the
honest set. All of them are `DOCS → -` and the `RESTARTS:` line is unaffected. A rebase onto current
main before the deploy is routine.

**8. Two defects the tests caught in the code, both fixed here** (detail in the chunk sections):
`report._current_header`'s substring search (COLUMNS is a PREFIX of APPEND_COLUMNS), and the `fetch=`
seam making `archiver/runner.py` invisible to L53's inventory scan.

**MEMORY:** none proposed — this build changed no law and no standing practice.
**RULING:** none required to finish the build. The rulings the OWNER still owes are O-1 (N shadow
nights), O-6 (the shadow read's cost), the switch to `append`, and his acceptance or refusal of the five
known limits of §12 in words.

ARCHIVER APPEND BUILT c974fbf (last build commit; this report commits on top) | on main 8838dda (base; main now 0569727) | offline 1850/0 (315 skipped; baseline 1562/297) | settings built · migrations 0010/0011 built · reconcile built · store built · runner+shadow built · quiet window+commands built · heartbeat+docs built | write_mode ships: upsert | radar diff: empty | RESTARTS: com.cobalt.aset com.cobalt.radar | db: OWED — 18 requires_db tests written, never run | OWED: three-house check, dev-DB run after p4-verify's stop line, deploy prompt (upsert), his approval, shadow nights, his switch ruling | ESCALATE: 8
