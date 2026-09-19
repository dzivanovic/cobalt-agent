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

---

# ROUND 2 — folding the three-house check (2026-09-19, `archiver-append-r2`)

## §0 Headline

The tribunal's ONE blocker is fixed: `restate --apply` wrote bars on `upsert_bars`'s OWN connection, so
§8's pre-commit re-check rolled back the incident and left the rewritten bars committed. All 7 REAL
findings are folded; `backfill-missing` never had the defect and a test now says so. Offline suite
**1866 passed / 0 failed / 320 skipped** (round-1 close 1850/0/315): +16 offline tests, +5 `requires_db`.
Radar diff empty, `write_mode` still ships `upsert`, counting identities untouched. ESCALATE: 4 new,
round 1's 8 carried verbatim.

## PREFLIGHT

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 11:30:45 EDT 2026` |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — EMPTY |
| `Bash(git status*)` | `git status` | 0 | allowed — `On branch archiver/append-0919` / `nothing to commit, working tree clean`. No rebase in progress. |
| `Bash(git log*)` | `git log --oneline -1` | 0 | allowed — `7c972ee` (first launch, as the prompt expects) |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `5f204be docs(desk): 09-19 archiver round 2 launched (f6bb98b6); ops DB run awaits 'approve env'; P4 check B timed for 11:41` |
| `Bash(ls *)` | `ls -la .env` | 1 | allowed — `ls: .env: No such file or directory` (required) |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_archiver_quiet.py tests/cobalt/test_archiver_migrations.py tests/cobalt/test_archiver_runner.py` | 0 | allowed — **142 tests collected** |

No denial. Authorization rule-proof: each of the 16 `Bash(...)` strings, `--disallowedTools
"AskUserQuestion" "EnterWorktree"`, and the three `--add-dir` values `grep -c` **1** against
`prompts/2026-09-19/17-archiver-append-build.md`. Sets identical; nothing added, altered or dropped.

## 1. F1 — `restate --apply` writes on the repair's own transaction — **FIXED** (`806f45f`)

**Read first.** `cli.py:266-267` `with store.target_transaction() as conn: written = _apply_restate(store,
conn, …)`; `_apply_restate` (`:391-399`) never used `conn` and called `store.upsert_bars(rows)`, which
`store.py:95-141` runs inside its own `with self._connect() as conn:` — a second connection that COMMITS
on exit. `guard.check_before_commit()` (`cli.py:287`) raises inside the FIRST transaction, so the
incident write rolled back and the bars did not.

**`backfill-missing` CONFIRMED safe, not assumed.** Read verbatim from `store.py:208`:

```
    def insert_new_bars(self, conn, bars: list[Bar]) -> int:
```

`conn` is its FIRST positional argument; the body has no `self._connect()`, no `commit()` and no
`close()` — it runs `with conn.cursor() as cur:` and returns the server's `rowcount`. `_cmd_backfill_missing`
(`cli.py:313-315`) calls it inside its own `target_transaction()` block, so its write already rolled back
with its re-check. **No F1-shaped fix was needed there.** A test now states it rather than leaving it to a
future reader.

**THE SHAPE TAKEN (named, as the prompt asks): a sibling connection-taking method**, not an optional
parameter on `upsert_bars`. `BarStore.upsert_bars_on(conn, bars)` holds the ONE copy of the
`ON CONFLICT … DO UPDATE` statement (L3); `upsert_bars` opens its own connection and delegates to it,
then runs `before_commit`. The nightly call site is untouched — `git diff main -- src/cobalt/archiver/runner.py`
shows `rows = store.upsert_bars(bars)` as a **context** line:

```
     total = len(targets)
     for i, (ticker, interval) in enumerate(targets, start=1):
         try:
-            bars = await fetch_bars(ticker, interval, token)
+            bars = await fetch(ticker, interval, token)
+            if settings.shadow_enabled:
+                _shadow_target(store, summary, ticker, interval, bars, settings, clock)
             rows = store.upsert_bars(bars)
```

`_apply_restate` now calls `store.upsert_bars_on(conn, rows)`; the incident write and the bar write are
both inside `_cmd_restate`'s one `target_transaction()` block and `guard.check_before_commit()` still runs
after both.

**RED (on `7c972ee`) → GREEN (on `806f45f`):**

```
E  AssertionError: a repair whose pre-commit re-check failed left a rewritten bar row behind:
E  {('TESTARCH', 'i5', datetime(2026, 9, 18, 19, 55, tzinfo=utc)): '100.00'}
E  -> {('TESTARCH', 'i5', datetime(2026, 9, 18, 19, 55, tzinfo=utc)): '105.00'}
...
3 failed, 2 passed, 37 deselected in 0.18s
```
```
5 passed, 37 deselected in 0.09s
```

The 2 that passed RED are the two this round expected to pass on the old tip: the `backfill-missing`
twin (already safe) and the quiet-window commit case.

**Tests added.** `tests/cobalt/test_archiver_quiet.py` — `test_a_failed_recheck_leaves_zero_changed_bar_rows_in_restate`,
`…_in_backfill_missing`, `test_a_quiet_restate_commits_its_rows_and_its_incident`, each driving
`archiver_cli.build_parser().parse_args(...)` → `HANDLERS[...]` with the suite's own `FakeBars`, EXTENDED
(not duplicated, L3) with `run_lock`, `target_transaction` and `upsert_bars_on`. The fake now models the
two-connection asymmetry that is the whole of F1: a write on the caller's `conn` is pending until commit
and vanishes on rollback; a write on another connection has already committed and is not undone.
`tests/cobalt/test_archiver_append_store.py` — `test_only_one_copy_of_the_upsert_statement_exists`,
`test_upsert_bars_on_takes_the_callers_connection_and_never_opens_one`, `test_upsert_bars_on_is_a_noop_on_an_empty_list`.

**One existing pin FOLLOWED, not dropped.** `test_upsert_bars_still_does_update_and_never_do_nothing`
asserted the DO UPDATE statement was inside `upsert_bars`. It now asserts the statement in
`upsert_bars_on` AND that `upsert_bars` still opens its own connection, delegates, runs `before_commit`
and holds no second copy of the clause. `test_upsert_bars_signature_is_unchanged` passes untouched.

**`requires_db` twins written, FIRST RUN OWED** (`test_archiver_append_store.py`):
`test_a_rollback_unwrites_an_upsert_made_on_the_targets_connection`,
`test_the_own_connection_upsert_survives_another_transactions_rollback`,
`test_backfill_missings_insert_rolls_back_with_its_transaction`.

## 2. F2 — the two named §8 boundary tests drive the command path — **ADDED** (in `806f45f`)

**EXTENDED, not replaced**; every existing assertion is kept byte for byte, including
`store.snapshot() == before` and `store.calls == ["upsert_bars"]` (the command drive uses a SECOND
`FakeBars`, so the original store's assertions are untouched).

- `test_gemini_close_boundary_poller_lag` gains scenario **(iv)**: on the early-close night the repair
  STARTS quiet (17:40, last cycle 17:00) and the lagging poller opens a cycle at 17:40 while the repair
  is in flight, so Q3 fails at the PRE-COMMIT re-check. That is Gemini's lag at the one boundary where
  the radar's own gate does not save us, driven through `_cmd_restate`.
- `test_astra_open_boundary_repair_crosses_open` gains the same sequence it already computed as
  verdicts — start 03:49:59 quiet, re-check 03:50:05 not — now driven through `_cmd_restate`.

Both were RED on `7c972ee` (`AssertionError: a repair that crossed the open must leave ZERO changed bar
rows`; `AssertionError: the lagging poller's cycle opened while the repair was in flight …`) and GREEN
after F1's fix.

**COMBINED COMMIT, stated as the prompt requires.** Steps 1 and 2 share one RED/GREEN boundary and one
file, so they are one commit (`806f45f`) whose message names both F1 and F2.

## 3. F3 / Q10 — the differing-value and equal-value race tests — **offline + `requires_db`** (`b9e165b`)

| test | form | why |
|---|---|---|
| `test_a_differing_value_race_the_repair_commits_last_and_its_value_survives` | **offline** | The poller commits X on its own connection between the repair's range read and its write (§15's Concurrency window); the repair's `DO UPDATE` commits after it, so the repair's Y survives. The ORDERING is deterministic Python and the fake models `DO UPDATE` / `DO NOTHING` faithfully. |
| `test_a_differing_value_race_the_poller_writes_after_the_repair_committed` | **offline** | The other order, stated so the pair is honest: a poller write AFTER the repair's commit wins and NOTHING in this build stops it — §12's Known limit 1 on a single key. The `restated` incident stays open, which is how an operator finds out. |
| `test_an_equal_value_race_rewrites_nothing` | **offline** | Traced, not assumed: `compare` normalises before deciding, so an equal key is neither `differing` nor `incoming_only`, `_apply_restate` offers an EMPTY list and `upsert_bars_on` returns 0 before sending a statement. |
| `test_an_equal_value_race_offers_no_rows_to_the_writer` | **offline** | The same property at the layer that decides it (`compare`), so a regression names the cause. |
| `test_a_committed_poller_write_is_overwritten_by_a_later_repair` | **`requires_db`** | Which value survives when two UNCOMMITTED transactions contend for one row is Postgres's row lock and commit order, not this suite's. Stretching a fake to claim it would be claiming a guarantee only a real transaction can prove (L45). |
| `test_an_equal_value_race_writes_the_same_value_and_changes_nothing` | **`requires_db`** | Same reason, plus it asserts on the real stored `NUMERIC(14,4)` rendering. |

**An honest finding, not papered over:** an equal-value race DOES open a `restated` incident, with
`rows_rewritten: 0`. Spec O-4 writes the audit row for the COMMAND the operator ran, not per rewritten
row, so that is correct behaviour and the test asserts it as such — "no incident" would have been the
wrong assertion.

All four offline tests are **GREEN on add**: they pin a gap in §15's must-exist list, they are not
regression proofs for a defect.

## 4. F4 — four tests assert on behaviour — **REWRITTEN** (`e5bec36`)

| test | was | is |
|---|---|---|
| `test_the_refusal_exit_code_is_two` | `assert QuietRefused("x").exit_code == 2` | runs `archiver_cli.main(RESTATE_ARGV)` with a window that refuses at START; asserts the code the real entry point RETURNS (2), the refusal on stderr (first line `Q1 …`, then `REFUSED — not in a quiet window.`), and that no writer was reached |
| `test_both_mutating_commands_are_refused_in_every_scanned_session` | computed `quiet_verdict` then `assert command in MUTATING_COMMANDS` | invokes each handler through `HANDLERS` for both commands across the four scanned sessions; asserts `QuietRefused` with `exit_code == 2` and a Q1 failure line, the snapshot unchanged, `committed == 0` |
| `test_previews_always_run` | monkeypatched `require_quiet`, asserted `calls == []` with nothing invoked | RUNS both previews (no `--apply`) to completion, asserts what each prints, and asserts neither `require_quiet` NOR `guarded_repair` was reached. Its observer iterator is EMPTY, so a preview that read the window raises `StopIteration` rather than merely failing an assertion |
| `test_backfill_missing_never_calls_upsert_bars` | `store.insert_new_bars(None, …)` — tested the fake | drives `_cmd_backfill_missing` through its real entry point in a QUIET window with one stored DIFFERING key and one missing key; asserts the differing key untouched, the missing one inserted, `store.calls == ["run_lock", "insert_new_bars"]`, and neither `upsert_bars` nor `upsert_bars_on` reached |

`test_backfill_missing_can_only_do_nothing`'s source scan is **kept as-is** — not one of the four, and
the hub called it weak but not wrong.

**GREEN before expected, and why (the prompt asks for this plainly).** All four are GREEN on add. F4 is
test-quality debt, not a defect — the verdict row says so. The behaviour they now assert was already
correct; what was missing was any test that looked at it. Two of them would have ERRORED on `c974fbf`
only because the suite's fake had no transaction surface until step 1 added one — a fixture shape, not a
behaviour change. **One real correction found while writing them:** §9's run-level lock is taken BEFORE
the window is read (Q4 is held for the whole command), so a refused command's call list is
`["run_lock"]`, not `[]`. The assertions say so and explain why; a lock is not a write.

## 5. F5 — exit code 2 on the production `cobalt` entry — **FIXED** (`ec045bd`)

**RED, quoted verbatim from the real process** (tip `e5bec36`, before the fix):

```
E  AssertionError: a QuietRefused must leave `cobalt` with exit status 2; got 1
E    stderr:
E    FAILED: QuietRefused: Q1 radar idle: session=rth - the radar scans in premarket, RTH and aftermarket.
E    REFUSED - not in a quiet window. session=rth - earliest allowed start: 2026-09-19 20:35:00 EDT. The preview (no --apply) is always available.
E  AssertionError: a ArchiveLockError must leave `cobalt` with exit status 2; got 1
E    stderr:
E    FAILED: ArchiveLockError: another archive/repair run holds the lock - refusing to start restate --apply TESTARCH.
E  AttributeError: type object 'ArchiveLockError' has no attribute 'exit_code'
3 failed, 2 passed, 46 deselected in 1.97s
```

GREEN after: `5 passed, 46 deselected in 1.86s`.

**The fix**, `git diff` of `src/cobalt/cli.py` in full — a NEW except-clause, no neighbour reflowed
(the file is shared with `ops/2026-09-19` at `:214-221`, untouched):

```diff
 from cobalt.archiver import cli as archiver_cli  # noqa: E402
+from cobalt.archiver.quiet import QuietRefused  # noqa: E402
+from cobalt.archiver.store import ArchiveLockError  # noqa: E402
@@
         print(f"NOT RUN — {e}")
+    except (QuietRefused, ArchiveLockError) as e:
+        # EXIT 2, the archiver's REFUSALS (append-only design §8, §9).
+        ...
+        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
+        sys.exit(e.exit_code)
     except Exception as e:
         print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
         sys.exit(1)
```

`ArchiveLockError` gained `exit_code = 2`, matching `QuietRefused` (`quiet.py:73`).

**MESSAGE SHAPE, chosen and stated:** kept as this CLI's own `FAILED: {type(e).__name__}: {e}` rather
than `archiver_cli.main`'s bare `str(refused)`. Reason: one rendering across every `cobalt` command, so
a reader never has to know which subcommand produced the line; the refusal's own multi-line body (the
three observed values and the earliest allowed start) follows it verbatim, and a separate test
(`test_the_refusal_body_survives_to_stderr`) asserts that body survives, so the exit-code mapping cannot
quietly swallow it.

**HARNESS, named as the prompt asks:** the shape of `test_migrate_proof.py`'s
`test_the_cli_turns_a_migration_error_into_failed_and_exit_1` — a REAL process running the real entry
point, with a scenario that raises before any connection is opened, so **no `cobalt_dev` is needed**.
Here the scenario is built by replacing ONE handler in the archiver's module before `cobalt.cli.main()`
builds its parser (`add_parser` reads `func` from that module's globals at build time), so the real
parser, the real dispatch and the real `try/except` all run.

**The clause did not widen:** `test_every_other_exception_keeps_its_own_exit_status` drives a real
`MigrationError` through `python -m cobalt.cli db migrate --proof-only --rollback` and asserts exit 1 and
`FAILED: MigrationError: `. `JobStopped` → `NOT RUN`/exit 0 is untouched.

## 6. F6 — the shadow artifact's night is the ET trading date — **FIXED** (`d9ddc2a`)

**RED:** a run frozen at `2026-09-19 00:30 UTC` (= `2026-09-18 20:30 EDT`, the real nightly hour) wrote

```
E  AssertionError: the artifact must be named for the ET trading night; files present: ['2026-09-19.jsonl']
...
shadow compare: 1 target(s) -> .../archiver-shadow/2026-09-19.jsonl
```

GREEN after: `46 passed in test_archiver_runner.py`.

**The fix is the one-line derivation the verdict row names, and nothing more.** `night=clock().date()`
→ `night=_trading_night(clock())`, where `_trading_night` is `SessionClock.to_et(now).date()` —
`session/clock.py:262`, the ET conversion already in the codebase, a STATIC method (no config load, no
calendar) that REFUSES a naive datetime rather than guessing a zone (ADR-0007). The artifact naming
scheme and the retention scheme are untouched. The existing schema test still asserts `2026-09-18.jsonl`
for `FETCH_AT` (20:30 UTC = 16:30 ET, same date) and passes unchanged.

## 7. F7 — `NULLS NOT DISTINCT` pinned — **PINNED** (`9056e73`)

Quoted first, as the prompt asks: the test **PASSED without the assertion** —
`1 passed, 57 deselected in 0.01s` for
`-k partial_unique_index`. That is the gap: `0011_archive_incidents.sql:92` carries the clause and its
own comment calls it load-bearing, but nothing asserted it, so a later edit could drop it without a red
test. The assertion added (no existing one removed):

```python
    assert "NULLS NOT DISTINCT" in body, (
        "the partial unique index lost NULLS NOT DISTINCT — an "
        "`empty_export` incident (range_start IS NULL) would duplicate on "
        f"every run instead of refreshing: {body}"
    )
```

GREEN on add (`48 passed, 10 skipped`) because the SQL already has it — F7 is a test-coverage finding,
not a code defect, exactly as the verdict row says.

## CLOSE (offline)

```
1866 passed, 320 skipped, 1 xfailed, 15 warnings in 44.61s
```

Round-1 close was `1850 passed, 315 skipped, 0 failed`. **Failed stays 0.**

**+16 offline tests, by step** — step 1/2 (6): `…_in_restate`, `…_in_backfill_missing`,
`test_a_quiet_restate_commits_its_rows_and_its_incident`, `test_only_one_copy_of_the_upsert_statement_exists`,
`test_upsert_bars_on_takes_the_callers_connection_and_never_opens_one`, `test_upsert_bars_on_is_a_noop_on_an_empty_list`
(the two NAMED boundary tests were extended, not added) · step 3 (4): the two differing-value orders, the
equal-value command test, the equal-value comparison test · step 4 (0 — four rewritten in place) ·
step 5 (5): `test_the_production_entry_exits_2_on_a_refusal_or_a_held_lock` ×2 params,
`test_the_refusal_body_survives_to_stderr`, `test_every_other_exception_keeps_its_own_exit_status`,
`test_the_lock_error_carries_the_same_exit_code_as_the_refusal` · step 6 (1) · step 7 (0 — one assertion
added to an existing test). 6+4+0+5+1+0 = **16**, and 1850+16 = 1866. ✓

**+5 skipped, all `requires_db`, all named** — step 1 (3):
`test_a_rollback_unwrites_an_upsert_made_on_the_targets_connection`,
`test_the_own_connection_upsert_survives_another_transactions_rollback`,
`test_backfill_missings_insert_rolls_back_with_its_transaction` · step 3 (2):
`test_a_committed_poller_write_is_overwritten_by_a_later_repair`,
`test_an_equal_value_race_writes_the_same_value_and_changes_nothing`. 315+5 = 320. ✓

**`uv run cobalt jobs restarts c974fbf..HEAD`**, verbatim:

```
path	change	rule	restart
docs/40 - DevDocs/reports/archiver-append-build-2026-09-19.md	M	DOCS	-
src/cobalt/archiver/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/archiver/runner.py	M	static import reach	-
src/cobalt/archiver/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_archiver_append_store.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_quiet.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```

**0 UNCLASSIFIED.** The only non-`src`/`tests` path is round 1's own report, which is in the range
because it was committed at `7c972ee`; it classifies `DOCS → -`. The `RESTARTS:` line is unchanged from
round 1's.

**`git diff main -- src/cobalt/radar/`** → **EMPTY** (no output). The poller is imported and driven by a
test; it is not edited.

**`git status --porcelain`** → EMPTY.

**`git diff --stat c974fbf HEAD -- src tests docs`:**

```
 .../reports/archiver-append-build-2026-09-19.md    | 249 ++++++-
 src/cobalt/archiver/cli.py                         |  16 +-
 src/cobalt/archiver/runner.py                      |  23 +-
 src/cobalt/archiver/store.py                       |  67 +-
 src/cobalt/cli.py                                  |  13 +
 tests/cobalt/test_archiver_append_store.py         | 210 +++++-
 tests/cobalt/test_archiver_migrations.py           |  12 +
 tests/cobalt/test_archiver_quiet.py                | 753 ++++++++++++++++++++-
 tests/cobalt/test_archiver_runner.py               |  34 +
 9 files changed, 1323 insertions(+), 54 deletions(-)
```

Every path is one this prompt named (`src/cobalt/archiver/*`, `src/cobalt/cli.py`, `tests/cobalt/*`,
`docs/40 - DevDocs/`). **L57: the counting identities were not touched** — no counter, no identity and
no `RunSummary` field changed this round.

**Commits, one per item (step 1+2 combined and stated):**

| commit | item |
|---|---|
| `806f45f` | F1 + F2 |
| `b9e165b` | F3/Q10 |
| `e5bec36` | F4 |
| `ec045bd` | F5 |
| `d9ddc2a` | F6 |
| `9056e73` | F7 |

## ROUND 2 ESCALATE

**Round 1's `## ESCALATE` is carried forward UNTOUCHED** — its (i) §14 OPEN table, (ii) the never-run
`requires_db` tests, (iii) the cross-branch table, (iv) the deploy-prompt list, (v) the five known
limits of §12, and its numbered findings 1–8. Nothing in this round resolves or supersedes any of them.
Two of them need a one-line amendment from this round's work, marked below.

**R2-1. Spec §5's `<YYYY-MM-DD>` is AMBIGUOUS on timezone, and this round resolved it to ET.**
The design writes `data/archiver-shadow/<YYYY-MM-DD>.jsonl` and names no zone. The verdict row (F6)
says "derive the night from the ET date (the design's `<YYYY-MM-DD>` is ambiguous — desk to rule
which)", and that is what was built. **This is a fix-per-row, not a design change; the desk or the
owner may still rule differently**, and if they rule UTC the change is one line in
`runner._trading_night` plus the test. Amends round 1's deploy-prompt item (iv)3: the first shadow
night's file is named for the **ET** trading date, so a run at 20:30 ET on 2026-09-22 writes
`2026-09-22.jsonl`, not `2026-09-23.jsonl`.

**R2-2. `backfill-missing` needed NO F1-shaped fix — stated either way, as the prompt requires.**
Confirmed by reading the signature and body of `insert_new_bars` (`store.py:208`), not assumed: it takes
`conn` first, never connects, never commits, never closes. `_cmd_backfill_missing` already called it
inside its own `target_transaction()`. This is now an assertion
(`test_a_failed_recheck_leaves_zero_changed_bar_rows_in_backfill_missing`, plus a `requires_db` twin), so
if the command ever grows F1's shape a test says so. **No new finding here.**

**R2-3. The `requires_db` first run is still OWED, and the count is now 23.** Round 1 wrote 18; this
round adds 5 (named under CLOSE). None has ever run. **Their first run on `cobalt_dev` remains a gate
before this branch may deploy** — unchanged from round 1's ESCALATE (ii), only the number moves.

**R2-4. One existing test was rewritten to follow F1's refactor, not dropped — flagged so the next
check sees it deliberately.** `test_upsert_bars_still_does_update_and_never_do_nothing` pinned the
`ON CONFLICT … DO UPDATE` statement *inside* `upsert_bars`; the statement now lives in the sibling
`upsert_bars_on`. The test asserts it there AND asserts `upsert_bars` still opens its own connection,
delegates to that sibling, runs `before_commit`, and holds no second copy of the clause — plus a new
`test_only_one_copy_of_the_upsert_statement_exists` for L3. The §5 mode-isolation property is unchanged;
only the file location of the assertion moved. `test_upsert_bars_signature_is_unchanged` passes as it
was.

**Also recorded, not an escalation:** §9's run-level lock is taken BEFORE the quiet window is read, so a
refused repair's recorded call list is `["run_lock"]`. Correct by §8's Q4 (the lock is held for the
whole command) and now documented in the tests rather than being a surprise to the next reader.

**MEMORY:** none proposed — this round changed no law and no standing practice.
**RULING:** one is owed by the desk/owner: **R2-1**, the shadow artifact's timezone. Everything else
this round fixed was already ruled by the FINAL design.

ARCHIVER APPEND R2 9056e73 | on archiver/append-0919 (round 1 c974fbf) | offline 1866/0 (320 skipped; round-1 close 1850/0/315) | F1 restate fixed · backfill-missing shape already-safe | F2 command-path tests added | F3/Q10 race tests offline+requires_db | F4 four tests rewritten fixed | F5 exit code 2 on cobalt fixed | F6 shadow night = ET date fixed | F7 NULLS NOT DISTINCT pinned fixed | radar diff: empty yes | write_mode ships: upsert (unchanged) | RESTARTS: com.cobalt.aset com.cobalt.radar | CARRIED: 23 requires_db tests never run (now includes this round's 5) | ESCALATE: 4

---

# DB RUN

Seat `archiver-db-0919`, worktree `/Users/cobalt/cobalt-wt/archiver-append`, prompt
`docs/40 - DevDocs/prompts/2026-09-19/35-archiver-db-run.md`. Started 2026-09-19 12:38:15 EDT (`date`).
This section APPENDS to the report above; `## ROUND 2` and `## ESCALATE` are untouched.

## §0 Headline

**The branch's DB debt is CLOSED, and closing it found three real reds.** 0010/0011 applied AND reversed on
real `cobalt_dev` — both tables created system-side, every pre-existing digest unchanged, `--rollback
--down-to 0009` dropped exactly those two and the closing proof is byte-identical to the baseline.
All 23 owed `requires_db` tests ran for the first time: **20 pass, 3 red** — `cobalt_user` CAN read both new
tables (§11's grant sentence contradicts the 0006 pattern it also mandates, DB-1 ×2, a ruling), and one
`upsert_bars` commit test is unobservable under the suite's autouse single-transaction fixture (DB-2, a
ruling). One test-side defect FIXED (the advisory-lock test needed two sessions, not two savepoint proxies).
Offline **1866/0/320**, unchanged. All three REVIEW.md UNVERIFIABLE items settled. `cobalt_dev` left at
0001–0009 unchanged, `.env` removed and proven gone. **ESCALATE: 4.**

## DB RUN PREFLIGHT

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 12:38:15 EDT 2026` |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **EMPTY** |
| `Bash(git status*)` | `git status` | 0 | allowed — first two lines verbatim: `On branch archiver/append-0919` / `nothing to commit, working tree clean`. Branch correct; no rebase in progress. |
| `Bash(git log*)` | `git log --oneline -1` | 0 | allowed — `fb825df docs(report): archiver append round 2 — 7 REAL findings folded, F1 blocker fixed, 1866/0/320 offline, 23 requires_db owed` (first launch, the expected tip) |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `d5ea92d docs(desk): 09-19 archiver DB run prompt (35) — 25's line + R18's two archiver env strings; rolls cobalt_dev back to 0009` (recorded, no equality required) |
| `Bash(ls *)` | `ls -la .env` | 1 | allowed — `ls: /Users/cobalt/cobalt-wt/archiver-append/.env: No such file or directory` ✅ nothing inherited |
| `Bash(ls *)` | `ls -la /Users/cobalt/cobalt-wt/ops-2026-09-19/.env` | 1 | allowed — `No such file or directory` ✅ `ops-0919-db` released the lane |
| `Bash(grep *)` | `grep -rln "cobalt_dev" "…/reports/"` | 0 | allowed — see the lane check below |
| `Bash(git -C … diff*)` | `git -C /Users/cobalt/cobalt-wt/archiver-append diff --stat c974fbf..HEAD -- src tests docs` | 0 | allowed — quoted below |
| `Bash(uv run pytest *)` | `uv run pytest --co -q <the three files>` | 0 | allowed — `157 tests collected in 0.11s`, no collection error |

**`ops-0919-db`'s stop line, read with the Read tool from `~/cobalt-wt/ops-2026-09-19/docs/40 - DevDocs/reports/ops-2026-09-19.md:1816`, quoted verbatim:**

> `OPS 0919 DB be00506 (code tip; one docs-only commit fills this sha in) | code d860bf7 | offline 1608/0 (302 skipped vs round-2 298; +4 named) | db 61/0 (tests/cobalt/test_migrate_proof.py only) | R1/R11 SET LOCAL does NOT take the snapshot — moved ahead of the BEFORE probe, coverage test added | F1 nested | F3 disposition recorded — ACCEPTED AS DISCLOSED, no edit | F4 marked | F5 marked | cobalt_dev: 0001–0009, unchanged (every row count and digest identical to the step-0 proof) | .env: removed, proven gone | RESTARTS: com.cobalt.radar (d860bf7..HEAD, 0 UNCLASSIFIED; branch 4c14712..HEAD com.cobalt.aset com.cobalt.radar) | OWED: three-house check on this diff, next deploy prompt | ESCALATE: 12`

**Lane check — nobody claimed `cobalt_dev` after `ops-0919-db` closed.** `grep -rln "cobalt_dev"` over
`~/cobalt/docs/40 - DevDocs/reports/` returns 37 files; only three carry a 2026-09-19 date:
`harness-round2-2026-09-19.md`, `prod-proof-only-3-2026-09-19.md` and the desk's own `cto-2026-09-19.md`.
Dated by their commits (`git -C /Users/cobalt/cobalt log --format=…`), the first two landed **07:11–07:55 ET** —
hours BEFORE `ops-0919-db` launched at 12:0x (`cto-2026-09-19.md` §41) and closed. `cto-2026-09-19.md` is the
desk's record of that launch, not a second claim on the lane. `ops-2026-09-19.md` itself is not in `~/cobalt`
(its worktree is unmerged), so it cannot appear in this grep. **No later session claims `.env` or `cobalt_dev`.**

**UNVERIFIABLE item 1 of 3, SETTLED HERE — `git diff --stat c974fbf..HEAD -- src tests docs`, verbatim:**

```
 .../reports/archiver-append-build-2026-09-19.md    | 634 ++++++++++++++++-
 src/cobalt/archiver/cli.py                         |  16 +-
 src/cobalt/archiver/runner.py                      |  23 +-
 src/cobalt/archiver/store.py                       |  67 +-
 src/cobalt/cli.py                                  |  13 +
 tests/cobalt/test_archiver_append_store.py         | 210 +++++-
 tests/cobalt/test_archiver_migrations.py           |  12 +
 tests/cobalt/test_archiver_quiet.py                | 753 ++++++++++++++++++++-
 tests/cobalt/test_archiver_runner.py               |  34 +
 9 files changed, 1708 insertions(+), 54 deletions(-)
```

Nine paths, every one named by round 2's own CLOSE section (`:972`) — five `src`/`tests` files the seven
findings touched, three more test files, and this report. **No surprise path.** Matches round 2's own
`git diff --stat c974fbf HEAD` line for line.

**Collection and the `requires_db` count — the report's figure of 23 is CORRECT, its LOCATION is not.**
157 tests collected across the three files, no error. Counted from the collected node ids:

| file | `requires_db` items |
|---|---|
| `tests/cobalt/test_archiver_migrations.py` | **10** (`…forward_creates_both_tables…`, `…migrate_twice_is_idempotent…`, `…rollback_down_to_0007_drops_exactly…`, `…owner_is_the_system_role` ×2, `…user_role_has_no_grant…` ×2, `…check_refuses_progress_past_its_own_export`, `…one_unresolved_incident_per_key…`, `…kind_domain_is_enforced_by_the_database`) |
| `tests/cobalt/test_archiver_append_store.py` | **13** (`test_the_append_path_never_modifies_an_existing_row` … `test_an_equal_value_race_writes_the_same_value_and_changes_nothing`) |
| `tests/cobalt/test_archiver_quiet.py` | **0** |
| **total** | **23** ✅ matches `ROUND 2`'s carried count exactly |

**Two DRIFTS in the prompt's own index card, named as the prompt asks (neither blocks):**
1. The prompt says `test_archiver_quiet.py` holds "one `requires_db` test (the F3/Q10 race twin)". It holds
   **none**. `test_archiver_quiet.py:1123-1125` says so in a comment: the twin lives in
   `test_archiver_append_store.py` (`test_a_committed_poller_write_is_overwritten_by_a_later_repair` and
   `test_an_equal_value_race_writes_the_same_value_and_changes_nothing`). The file is still run in step 2 —
   it contributes 0 skipped-to-real, not 1.
2. The prompt says the 0010/0011 `requires_db` half is "≈17 tests". It is **10**. The three test names it
   quotes all exist and are among them.

## DB RUN AUTHORIZATION

**R18 VERIFIED MYSELF, not taken from the prompt.** `grep -n "R18" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-19.md"` → line 31, `## §4 Rulings`, row **R18**, 11:33 ET, "approve env". Its text matches
the prompt's quotation word for word, including all four rule strings, the two REUSED `COBALT_ENV=dev` lines,
the NEVER block, and `Covers: 25-ops-db-run.md (launch when cobalt_dev is free) and the archiver's DB run
after its round 2.` **APPLIED marker present**, verbatim: `APPLIED: this row committed before either launch`.
The row is committed in `~/cobalt` on main (`git -C /Users/cobalt/cobalt log --oneline -1` → `d5ea92d`, above
it in history). The two rules new to THIS worktree —
`Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/archiver-append/.env)` and
`Bash(rm /Users/cobalt/cobalt-wt/archiver-append/.env)` — are two of R18's four strings, by name.
**No authorization mismatch.** Laws read in full this run: `LAWS.md` (L4, L29, L41, L45, L46, L48, L54, L57,
L60, L67 bind directly), `UNATTENDED-LAUNCH.md` §2 + §6, memory `INDEX.md` → `areas/cobalt.md ## NOW`.

## DB RUN — MIGRATIONS 0010/0011

### Step 0 — STATE PROBE (12:42 ET): the allowlist rules and what `cobalt_dev` held before this run

`cp … .env` → allowed. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → allowed, exit 0, FULL output:

```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  -        -            -                                  0.01
archive_progress     system  -        -            -                                  0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.01
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.40
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   126          5c891af77292421e9595daef739c3941   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.00
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     184          4a965c69340f112d12e6ca21a8a0602c   0.01
------------------------------------------------------------------------------------------
25 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 5.3 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

Then `rm … .env` → allowed; `ls -la .env` → `No such file or directory` ✅.

Read against `placement.py`: **25 tables in this branch's view** (the 23 `ops-0919-db` probed, plus this
branch's two). 0001–0007's 23 objects all present with a schema, a row count and a digest. The two new ones,
`archive_progress` and `archive_incidents`, read **`-` / `-` / `-` — ABSENT**, exactly as expected: this
branch has never applied 0010/0011 against `cobalt_dev`. Nothing read `CHANGED`; no error. P4's 0008/0009 are
not in this branch's `FORWARD`, so its harness has no opinion on them and none appears in the table.

**Two small drifts in the prompt's step-0 wording, named (neither blocks):** (a) `--proof-only` has no
`OK`/`CHANGED` verdict column at all — verdicts are a property of the BEFORE→AFTER proof the FORWARD and
ROLLBACK runs print (`cli.py:541-551` takes one probe and calls `_print_probe`; `:553-591` takes two and
calls `_print_proof`). "Present and OK" for step 0 therefore means *present with a row count and a digest*.
(b) There is no trailing `code:` line; the trailing line is `NOTHING WAS APPLIED: --proof-only ran in a READ
ONLY transaction.`

> **`cobalt_dev` holds (this branch's view, before this run): 0001–0007 objects OK, 1,043,443 rows in
> `system.bars` (digest `2769919a57144c7bf8720110061dbf72`); 0010/0011 objects: absent (expected — never
> applied on this `cobalt_dev`).**

### Step 1 — FORWARD (12:43 ET): `.env` re-copied, `cobalt db migrate`, FULL output

```
cobalt db migrate — FORWARD on cobalt_dev
-- applying 0001_schemas.sql
-- applying 0002_move_tables.sql
-- applying 0003_heartbeat_vault_outcome.sql
-- applying 0004_radar_pool.sql
-- applying 0005_heartbeat_note_absent.sql
-- applying 0006_radar_score.sql
-- applying 0007_radar_cards.sql
-- applying 0010_archive_progress.sql
-- applying 0011_archive_incidents.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  - -> system                - -> 0          0.01 -> 0.00    - -> d41d8cd9         CREATED
archive_progress     system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
aset_sizings         user    user -> user               1 -> 1          0.01 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.24 -> 5.31    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           126 -> 126      0.00 -> 0.00    5c891af7 -> 5c891af7  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               184 -> 184      0.01 -> 0.01    4a965c69 -> 4a965c69  OK
----------------------------------------------------------------------------------------------------------------------
25 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.3 s + AFTER 5.3 s = total 10.6 s; slowest table bars (5.2 s before).
```

0001–0007 replayed as **idempotent no-ops** (every digest identical before→after), 0010 and 0011 **CREATED**,
both empty, both on the **system** side. `content UNCHANGED on every table` — the run committed. **L45
satisfied: this is real Postgres, not the SQL text.**

### Step 1 — `--proof-only` with both tables applied

Every one of the 25 tables now reads with a schema, a row count and a digest — `archive_incidents` and
`archive_progress` at `system` / `0` / `d41d8cd98f00b204e9800998ecf8427e`; every 0001–0007 digest **identical
to step 0's baseline, byte for byte** (`bars` 1043443 / `2769919a…`, `vault_writes` 184 / `4a965c69…`,
`cobalt_redactions` 126 / `5c891af7…`, and so on down the table). Nothing `CHANGED`. Trailing line:
`25 table(s) probed on cobalt_dev; … Proof cost: total 5.2 s` / `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`

### Step 1 — ROLLBACK `--down-to 0009`, FULL output

```
cobalt db migrate — ROLLBACK on cobalt_dev
-- applying 0011_archive_incidents.rollback.sql
-- applying 0010_archive_progress.rollback.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  system -> -                0 -> -          0.01 -> 0.00    d41d8cd9 -> -         DROPPED
archive_progress     system  system -> -                0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
aset_sizings         user    user -> user               1 -> 1          0.00 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.05 -> 5.18    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           126 -> 126      0.00 -> 0.00    5c891af7 -> 5c891af7  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               184 -> 184      0.01 -> 0.01    4a965c69 -> 4a965c69  OK
----------------------------------------------------------------------------------------------------------------------
25 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.1 s + AFTER 5.2 s = total 10.3 s; slowest table bars (5.1 s before).
```

**`_rollback_paths("0009")` selected exactly two files, in the right order** — `0011_…rollback.sql` then
`0010_…rollback.sql`, and stopped. 0001–0009 were NOT touched: every other row reads `OK` with an unchanged
digest, and `0007_radar_cards.rollback.sql` (the next in `REVERSE`) never ran. This is the live confirmation
of the offline `test_rollback_down_to_0007_selects_exactly_the_two_new_files` and of the module docstring's
numeric-prefix claim.

### Step 1 — `--proof-only` after the rollback: back at 0001–0009

Byte-identical to step 0's baseline table, including the two `-` rows. `bars` 1043443 / `2769919a…`;
every 0001–0007 digest unchanged; `archive_progress` and `archive_incidents` ABSENT again.

**`.env` STATE AT THIS BOUNDARY, stated explicitly rather than left silent:** `.env` **remains in place** at
the end of step 1 — step 2 (the with-DB suite) needs it, which is the same convention `25-ops-db-run.md`'s
own step 1 used. It is removed and proven gone at the end of step 2.

> **migrations 0010/0011: applied (both tables created on the system side, `--proof-only` shows all 25
> objects present and every pre-existing digest unchanged) and reversed (`--rollback --down-to 0009` dropped
> exactly those two, `--proof-only` shows `cobalt_dev` back at 0001–0009, byte-identical to the step-0
> baseline).**

No code changed in step 1 — the proof surfaced no defect, so this step's commit is report-only.

## DB RUN — WITH-DB SUITE

Scope, exactly as the prompt narrows it: `tests/cobalt/test_archiver_migrations.py`,
`tests/cobalt/test_archiver_append_store.py`, `tests/cobalt/test_archiver_quiet.py`. Repo-wide
`requires_db` tests this branch merely touched in passing (`test_radar_score_migration.py`,
`test_tenancy.py`) were NOT run and are not verified by this run. The whole `tests/cobalt` tree was never
run with `.env` present.

### Run 1 (12:45 ET) — the prompt's own ordering, run first so the finding is PROVEN, not asserted (L70)

```
12 failed, 145 passed in 4.38s
```

**THE PROMPT'S STEP ORDER IS WRONG, and this is the evidence.** Step 1 ends with `cobalt_dev` at 0001–0009 —
`archive_progress` and `archive_incidents` DROPPED. Step 2's own note assumes "every test that writes cleans
up; the migration-harness tests … are self-contained round trips". That is true of only 3 of the 23
(`…forward_creates_both_tables…`, `…migrate_twice_is_idempotent…`, `…rollback_down_to_0007_drops_exactly…`,
which call `_apply`/`_rollback_paths` on their own connection and roll back). **The other 20 need the two
tables to already EXIST**: seven via the `real_connect` fixture (which conftest documents as a REAL
`db.connect` that applies no migrations, `conftest.py:196-223`) and thirteen via `BarStore().ensure_schema()`,
which executes the bars module DDL only (`archiver/store.py:100-103`) and creates neither new table. Ten went
red on `relation … does not exist` / `… missing — run cobalt db migrate`:

| test | assertion, verbatim |
|---|---|
| `test_owner_is_the_system_role[archive_progress]` | `AssertionError: archive_progress missing — run \`cobalt db migrate\`` |
| `test_owner_is_the_system_role[archive_incidents]` | `AssertionError: archive_incidents missing — run \`cobalt db migrate\`` |
| `test_the_user_role_has_no_grant_on_either_table[archive_progress]` | `psycopg.errors.UndefinedTable: relation "system.archive_progress" does not exist` |
| `test_the_user_role_has_no_grant_on_either_table[archive_incidents]` | `psycopg.errors.UndefinedTable: relation "system.archive_incidents" does not exist` |
| `test_the_check_refuses_progress_past_its_own_export` | `assert ('archived_through' in 'relation "archive_progress" does not exist…')` |
| `test_one_unresolved_incident_per_key_then_a_second_after_resolution` | `psycopg.errors.UndefinedTable: relation "archive_incidents" does not exist` |
| `test_a_crash_after_the_inserts_leaves_neither_bars_nor_progress` | `psycopg.errors.UndefinedTable: relation "archive_progress" does not exist` |
| `test_progress_and_an_incident_commit_with_the_bars_or_not_at_all` | `psycopg.errors.UndefinedTable: relation "archive_progress" does not exist` |
| `test_progress_is_monotonic_across_accepted_runs` | `psycopg.errors.UndefinedTable: relation "archive_progress" does not exist` |
| `test_a_recurring_incident_refreshes_rather_than_duplicating` | `psycopg.errors.UndefinedTable: relation "archive_incidents" does not exist` |

**ASK DESK: should `35`'s step order be swapped (suite BEFORE the rollback) in the next prompt of this
shape, or is the re-apply the desk wants? [12:45 ET]** Safe default taken, and it is the only one that
delivers BOTH of step 1's and step 2's stated outcomes: re-apply `COBALT_ENV=dev uv run cobalt db migrate`
(an allowlisted command this run had already used twice), run the suite for real, then roll back to 0009
again so `cobalt_dev` is left exactly as step 2's own terminal line requires. Nothing outside the allowlist
was typed and no step was skipped — step 1's applied-and-reversed proof stands on its own, above.

### Run 2 (12:46 ET) — migrations re-applied, the suite's FIRST REAL RUN

`COBALT_ENV=dev uv run cobalt db migrate` → both tables `CREATED` again, every other table `OK`,
`content UNCHANGED on every table`. Then:

```
4 failed, 153 passed in 4.67s
```

Ten of run 1's twelve went green the moment the tables existed. **Four reds survived — none of them
caused by the ordering, all four never seen before, because these tests had never run.**

### Run 3 (12:47 ET) — after the one test-side fix

```
3 failed, 154 passed in 3.22s
```

> **`cobalt_dev` holds (after this step): 0001–0009, unchanged | db 154/3 (the 23 archiver `requires_db`
> tests, scoped as above — 20 of the 23 pass, 3 red, all three ESCALATED below)**

**`cobalt_dev` IS unchanged in content, and it is proven, not assumed.** The BEFORE probe of the closing
`--rollback --down-to 0009` was taken AFTER the whole with-DB suite had run, and every digest in it is
identical to step 0's baseline — `bars` 1043443 / `2769919a…`, `vault_writes` 184 / `4a965c69…`,
`cobalt_redactions` 126 / `5c891af7…`, `cobalt_jobs` 13 / `8d9b0861…`, down the table. The mechanism is
`conftest.dev_db_tx` (autouse): every `db.connect` in the suite returns a `_SavepointConnection` over one
`cobalt_dev` transaction that is rolled back. The suite committed nothing. The closing `--proof-only` is
byte-identical to step 0's, including the two `-` rows.

`rm …/.env` → `ls -la .env` → `No such file or directory` ✅.

### The four reds, one row each

**F-DB1 / F-DB2 — `cobalt_user` CAN read both new tables. GENUINE FINDING, ESCALATED, not "fixed".**
`AssertionError: cobalt_user can read system.archive_progress` (and `…archive_incidents`).
`has_table_privilege('cobalt_user', 'system.archive_progress', 'SELECT')` returns **true** on real
`cobalt_dev`. Cause, read from the SQL and not guessed: `0001_schemas.sql:124`
`GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user;` — which 0001 replays on every migrate, after
0010/0011 have created their tables — and `:150-152`
`ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, <login> IN SCHEMA system GRANT SELECT ON TABLES TO cobalt_user`,
a standing default privilege on every future system table. **The spec contradicts itself** (§11): it asks
for "`cobalt_user` is granted nothing on them" AND for "Ownership and grants follow `0006_radar_score.sql`'s
pattern for a system table — the builder reads it, never invents one" — and `0006_radar_score.sql:198-200`
does the opposite, granting `cobalt_user` SELECT on its own system tables explicitly. **The branch's code is
consistent with every other system table; the spec sentence is the thing that is not achievable** without an
explicit `REVOKE SELECT … FROM cobalt_user` that nobody wrote. Per the index card the CODE wins and the
difference is an ESCALATE line — so it is one, and the test stays RED for the desk to rule. This is exactly
the L45/L70 class: the offline twin `test_nothing_is_granted_to_cobalt_user` PASSES because it only greps
the migration TEXT for the string `cobalt_user`; the database says otherwise. **Not fixed here — I do not
rule a tenancy question, and I do not change real grants.**

**F-DB3 — the advisory-lock test could not observe its own property. TEST-SIDE, FIXED, tests-first.**
`assert try_acquire_run_lock(second) is False` → `assert True is False`, `where True = try_acquire_run_lock(<conftest._SavepointConnection object …>)`.
§9's lock is SESSION level (`store.py:53-66`, `pg_try_advisory_lock`, deliberately not `…_xact_lock`), and
`pg_try_advisory_lock` is re-entrant within one session. The test opened `BarStore()._connect()` twice —
both of which go through the autouse `dev_db_tx` fixture and come back as savepoint proxies over **one**
session — so the "second holder" was the first holder. The code is correct; the test could not see it.
Fixed by taking the two connections from the `real_connect` fixture, which conftest documents for exactly
this ("a savepoint proxy over one shared connection cannot show that a SYSTEM role is refused a `"user"`
table, because both proxies are the same session"). It writes no rows, so RULING 7 is untouched. RED before
(`assert True is False`) → GREEN after (`1 passed`). Own commit.

**F-DB4 — `test_the_own_connection_upsert_survives_another_transactions_rollback`. GENUINE, ESCALATED, left RED.**
`AssertionError: \`upsert_bars\` is expected to commit on its OWN connection; if this now rolls back, the
nightly night's write semantics changed`. Same root cause as F-DB3 — under `dev_db_tx` the "own connection"
`upsert_bars` opens is a savepoint of the SAME transaction as the enclosing `target_transaction()`, so the
outer rollback takes the inner write with it and the close reads `100.0000` instead of `999.0000`. **But
unlike F-DB3 there is no fix that does not either narrow the test or break a standing ruling:** the property
under test is that `upsert_bars` **COMMITS**, and a committing test is what conftest's RULING 7 exists to
forbid ("Before RULING 7 the test suite wrote REAL rows into the same `cobalt_dev` tables the PRODUCTION
ASET sheet and both prefill jobs wrote to"). Rewriting it to prove anything weaker is narrowing, which L45's
companion ruling refuses. **This is a ruling for the desk, not for me** — two options, named: (a) delete the
`requires_db` twin and rely on the offline pins that already assert `upsert_bars` opens its own connection
and holds the only `DO UPDATE` (`test_upsert_bars_still_does_update_and_never_do_nothing`,
`test_upsert_bars_on_takes_the_callers_connection_and_never_opens_one`,
`test_only_one_copy_of_the_upsert_statement_exists`); or (b) give the suite a sanctioned committing lane
with mandatory cleanup, which amends RULING 7. I took neither.

**Companion note, not a finding:** F-DB4's sibling `test_a_rollback_unwrites_an_upsert_made_on_the_targets_connection`
PASSES — but under one shared transaction it would pass whether or not the property held, since everything
rolls back. Its verdict should be read as UNPROVEN until F-DB4's ruling lands, not as evidence for F1.

## DB RUN — OFFLINE SUITE + RESTARTS + UNVERIFIABLE SETTLED

`ls -la .env` → `No such file or directory` re-confirmed before this step. `uv run pytest -q tests/cobalt tests/taxonomy`:

```
1866 passed, 320 skipped, 1 xfailed, 15 warnings in 44.43s
```

**UNVERIFIABLE item 2 of 3, SETTLED: the `1866/0/320` count is REAL.** `passed` 1866 = round 2's close,
exactly. `failed` **0**. This step touched no offline test, and the one test this run did change (F-DB3) is
`requires_db`, so it skips offline and moves no count.

**The arithmetic on `skipped`, named rather than waved off — and the prompt's expectation here is wrong.**
`skipped` is **320**, unchanged, and it MUST be. The prompt expects it to "drop by however many of the 23
`requires_db` tests ran for real in step 2". It cannot: `requires_db` is
`pytest.mark.skipif(not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")))`, and step 3 runs with
`.env` REMOVED, so those two variables are unset and all 23 skip again — exactly as they did at round 2's
close. The 23 ran in step 2's own separate run, with `.env` present and `COBALT_ENV=dev`. Two runs, two
environments; the offline number is not supposed to move. `320 - 320 = 0` is the correct arithmetic, not a
mismatch. (1 xfailed is pre-existing and appears in round 2's close the same way.)

**UNVERIFIABLE item 3 of 3, SETTLED: `uv run cobalt jobs restarts 8838dda..HEAD`, table VERBATIM:**

```
path	change	rule	restart
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
docs/40 - DevDocs/cobalt/archiver/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/cli.md	A	DOCS	-
docs/40 - DevDocs/cobalt/archiver/incidents.md	A	DOCS	-
docs/40 - DevDocs/cobalt/archiver/progress.md	A	DOCS	-
docs/40 - DevDocs/cobalt/archiver/quiet.md	A	DOCS	-
docs/40 - DevDocs/cobalt/archiver/reconcile.md	A	DOCS	-
docs/40 - DevDocs/cobalt/archiver/report.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/settings.md	A	DOCS	-
docs/40 - DevDocs/cobalt/archiver/shadow.md	A	DOCS	-
docs/40 - DevDocs/cobalt/archiver/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/placement.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/reports/archiver-append-build-2026-09-19.md	M	DOCS	-
src/cobalt/archiver/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/archiver/incidents.py	A	static import reach	com.cobalt.radar
src/cobalt/archiver/progress.py	A	static import reach	com.cobalt.radar
src/cobalt/archiver/quiet.py	A	static import reach	com.cobalt.radar
src/cobalt/archiver/reconcile.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/archiver/report.py	M	static import reach	-
src/cobalt/archiver/runner.py	M	static import reach	-
src/cobalt/archiver/settings.py	A	static import reach	com.cobalt.radar
src/cobalt/archiver/shadow.py	A	static import reach	com.cobalt.radar
src/cobalt/archiver/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/0010_archive_progress.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0010_archive_progress.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0011_archive_incidents.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0011_archive_incidents.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_archiver_append_store.py	A	test/documentation; no resident	-
tests/cobalt/test_archiver_migrations.py	A	test/documentation; no resident	-
tests/cobalt/test_archiver_quiet.py	A	test/documentation; no resident	-
tests/cobalt/test_archiver_reconcile.py	A	test/documentation; no resident	-
tests/cobalt/test_archiver_runner.py	A	test/documentation; no resident	-
tests/cobalt/test_archiver_settings.py	A	test/documentation; no resident	-
tests/cobalt/test_finviz_consumers.py	M	test/documentation; no resident	-
tests/cobalt/test_heartbeat.py	M	test/documentation; no resident	-
tests/cobalt/test_heartbeat_archiver_incidents.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```

**0 UNCLASSIFIED — every one of the 46 rows carries a rule.** `RESTARTS: com.cobalt.aset com.cobalt.radar`
is CORRECT, and now derived rather than asserted. The `aset` half comes from exactly three paths
(`configs/cobalt/taxonomy/tunables.yaml` by `resident reads`, `archiver/reconcile.py` and `archiver/store.py`
by `static import reach`); everything else that restarts anything restarts `com.cobalt.radar` alone; the 15
DevDocs paths derive `-` under L42's 09-13 documentation amendment. Note the two new SQL files classify as
`non-Python src asset` → `-`: correct, since a migration file is read by the `db migrate` CLI, not by a
resident — but the deploy still runs `cobalt db migrate --allow-prod` as its own named step (round 1's
ESCALATE (iv)1), and that is not a restart.

**UNVERIFIABLE item 1 of 3** was run in PREFLIGHT and is restated here rather than rerun: the fresh
`git diff --stat c974fbf..HEAD -- src tests docs` shows the same nine paths round 2's own close listed, no
surprise path.

`git status --porcelain` → one line, this report, uncommitted at the moment of writing and committed by the
close commit below. `git diff --stat 8838dda HEAD -- src tests docs` → 45 files, 10955 insertions, 55
deletions: 14 DevDocs files + this report, 18 `src/cobalt/...` paths (10 archiver modules, `cli.py`, the four
0010/0011 SQL files, `db_migrations/__init__.py`, `placement.py`, `heartbeat/probes.py`) and 12 test files.
Every path is one this prompt or the branch's own prior commits named.

## DB RUN ESCALATE

**CARRIED FORWARD UNTOUCHED — round 1's `## ESCALATE` in full:** (i) the spec §14 OPEN table O-1…O-7 with
what was built as the safe default; (ii) the never-run `requires_db` tests — **CLOSED by this run, see
below**; (iii) the cross-branch table (`sprint-2/p4` shares `db_migrations/__init__.py`, `placement.py`,
`tunables.yaml`, `cli.py`, `archiver/runner.py`, `archiver/store.py`; P4's `_check_demand` call must be
re-applied at the top of the rewritten `_run_targets`); (iv) the deploy-prompt list 1–6; (v) the five known
limits of §12; and its numbered findings 1–8. **And round 2's `## ROUND 2 ESCALATE` in full:** R2-1 (the
shadow artifact's timezone, ET — a ruling still OWED from the desk or the owner), R2-2 (`backfill-missing`
needed no F1-shaped fix), **R2-3 (the `requires_db` first run) — now CLOSED**, R2-4 (one test rewritten to
follow F1's refactor). Nothing in this run resolves or supersedes any of the rest.

**NEW THIS RUN — 4 items.**

**DB-1. `cobalt_user` CAN read both new tables; §11's grant sentence is not achievable as written. TWO TESTS RED.**
Detail and cause above (`0001_schemas.sql:124` + `:150-152`, vs `0006_radar_score.sql:198-200` which §11 told
the builder to copy). **The desk or the tribunal rules one of two ways:** (a) add an explicit
`REVOKE SELECT ON system.archive_progress, system.archive_incidents FROM cobalt_user;` to 0010/0011, making
the spec sentence true and making these two tables the ONLY system tables the user role cannot read — a real
tenancy decision, not a typo fix; or (b) amend §11 to match 0006's pattern and relax the two tests to assert
no WRITE grant. **This is the first thing this branch's DB run found that reads clean from the SQL text and
false from the database — precisely the L45/L70 class, and precisely why the run was owed.**

**DB-2. `test_the_own_connection_upsert_survives_another_transactions_rollback` is unobservable under
conftest's autouse single-transaction fixture. ONE TEST RED.** Detail and the two options above. Neither
was taken: (a) narrows the test (L45 companion ruling forbids), (b) amends RULING 7 (not mine).

**DB-3. `35`'s step order is wrong and the next prompt of this shape should not repeat it.** Step 1's
rollback removes the two tables that 20 of the 23 `requires_db` tests need. Proven, not asserted: run 1 went
`12 failed, 145 passed` with the ten missing-table reds listed above. The safe default taken (re-apply, run,
roll back again) delivered both steps' stated outcomes. **ASK DESK line raised in the suite section, 12:45 ET.**

**DB-4. Two index-card drifts, named in PREFLIGHT** — `test_archiver_quiet.py` holds ZERO `requires_db`
tests (the F3/Q10 twin is in `test_archiver_append_store.py`), and the 0010/0011 `requires_db` half is 10
tests, not ≈17. The total of 23 is correct.

**IS THE BRANCH'S DB DEBT CLOSED? YES — the debt itself, not every question it opened.** Round 1's ESCALATE
(ii) and round 2's R2-3 were both "23 `requires_db` tests written, NEVER RUN". **All 23 have now run on real
`cobalt_dev`: 20 pass, 3 are red and every one of the three is named, explained and escalated above.** The
migrations are proven applied AND reversed on real Postgres. What the branch now carries in place of the
debt is two rulings (DB-1, DB-2) and three red tests — which is a shipping gate the house check and Dejan
decide on, not an unknown.

**The three REVIEW.md UNVERIFIABLE items, by name, with how each was settled:**

| # | item | settled how |
|---|---|---|
| 1 | a fresh `git diff` of `c974fbf..archiver/append-0919` | PREFLIGHT ran it: nine paths, identical to round 2's own close listing, no surprise path |
| 2 | the `1866/0/320` suite pass and the 23 `requires_db` tests | step 3's offline run: **1866 passed / 0 failed / 320 skipped**, exact match; step 2 ran the 23 for real: **20 pass, 3 red** (DB-1 ×2, DB-2) |
| 3 | the `RESTARTS: com.cobalt.aset com.cobalt.radar` line | `uv run cobalt jobs restarts 8838dda..HEAD` printed above: **0 UNCLASSIFIED**, the line is derived and correct |

**MEMORY:** none proposed — this run changed no law and no standing practice.
**RULING:** two are owed by the desk or the tribunal — **DB-1** (the `cobalt_user` grant on the two archiver
tables: REVOKE, or amend §11) and **DB-2** (whether a `requires_db` test may commit, or the twin retires).
R2-1 (the shadow artifact's timezone) remains owed from round 2 and is untouched by this run.

ARCHIVER DB d2099e1 (code tip; report 2e4ca6f, and this line's own docs-only commit on top) | offline 1866/0 (320 skipped vs round-2 320 — unchanged, and correct: step 3 runs with `.env` removed so all 23 `requires_db` skip again) | db 154/3 (the 23 archiver requires_db tests: 20 pass, 3 red — DB-1 ×2 cobalt_user grant, DB-2 unobservable commit) | migrations 0010/0011: applied on real cobalt_dev (both CREATED system-side, every pre-existing digest unchanged) and reversed (`--rollback --down-to 0009` dropped exactly those two, proof-only byte-identical to the step-0 baseline) | UNVERIFIABLE settled: (1) fresh c974fbf..HEAD diff = round 2's nine paths, no surprise; (2) 1866/0/320 real + the 23 ran for the first time; (3) RESTARTS derived, 0 UNCLASSIFIED | cobalt_dev: 0001–0009, unchanged (every row count and digest identical to this run's step-0 proof) | .env: removed, proven gone | RESTARTS: com.cobalt.aset com.cobalt.radar | OWED: whole-build house check close (Astra), rulings DB-1 + DB-2 + R2-1, next deploy prompt (deploy 3, after P4) | ESCALATE: 4

---

# ROUND 3 — REVOKE cobalt_user off the two archiver tables (cto-2026-09-19 R25 "B", DB-1)

Seat `archiver-round3-0919` (Opus 5), worktree `~/cobalt-wt/archiver-append`, branch `archiver/append-0919`,
OFFLINE by design — `.env` absent, `cobalt_dev` untouched. Prompt: `prompts/2026-09-19/40-archiver-round3.md`.

## §0 Headline

DB-1 is CLOSED IN THE SQL: `0010` and `0011` now carry an explicit `REVOKE ALL … FROM cobalt_user`, and
`0011` revokes `archive_incidents_id_seq` with its table. Five new offline tests, all RED first, now GREEN.
Offline suite **1871 passed / 0 failed / 320 skipped** (baseline 1866/0/320 — +5, exactly the new tests).
The two `requires_db` grant tests still SKIP and are OWED to the DB re-run, together with the
apply-twice idempotency fact. §11 NOT edited; one sentence in it escalated instead. ESCALATE: 6 new.

## Step 1 — the cause, quoted from the file

`src/cobalt/db_migrations/0001_schemas.sql`, verbatim:

```
124:GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user;
125:GRANT SELECT ON ALL SEQUENCES IN SCHEMA system TO cobalt_user;
```

and inside the `DO $$ … $$` block of section 5:

```
149:    EXECUTE format(
150:        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
151:        'GRANT SELECT ON TABLES TO cobalt_user', current_user);
152:    EXECUTE format(
153:        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
154:        'GRANT SELECT ON SEQUENCES TO cobalt_user', current_user);
```

`:124` fires once, at 0001's own run, over the tables that exist then; `:149-151` is what reaches a table
created LATER — 0010's and 0011's. `:125`/`:152-154` are the same pair for SEQUENCES.

**Only two routes, confirmed from the files and not from the prompt.** `grep -rn cobalt_user
src/cobalt/db_migrations/` returns every mention: 0001 (the two routes above, plus the role's `CREATE ROLE
… NOLOGIN` at `:78-79` and the login role's `GRANT cobalt_system, cobalt_user, cobalt_backup TO %I` at
`:95`), and explicit per-table grants in `0004:59-60`, `0006:198-200`, `0007:204-206` — each naming its own
tables, none naming an archive table. `cobalt_user` is NOLOGIN and is a member of no role (only the login
role is granted membership INTO it, `:95`), and `:132` `REVOKE ALL ON SCHEMA "user", system FROM PUBLIC;`
closes the PUBLIC route at schema level (PUBLIC holds no default table privilege in Postgres regardless).
**No third route. Nothing folded in silently.**

**THE SEQUENCE — decided, option (i), revoke it too.** `0011_archive_incidents.sql:49` is
`id            BIGSERIAL   PRIMARY KEY,` — read from the file, not assumed: the sequence
`archive_incidents_id_seq` is created as part of the `CREATE TABLE`, so an order test anchored on
`CREATE TABLE system.archive_incidents` is sufficient. By `:152-154` it inherits the same default SELECT
the table does. 0011's own comment at `:99-100` says *"NOTHING is granted to `cobalt_user`"* — aspirational
for the sequence exactly as it was for the table. Option (ii) would have narrowed a true-intent comment to
"nothing except the identity counter", which is a readable row-count proxy for the incident log the tenancy
answer excludes. **Taken: revoke, in the same commit, so the comment is true of both objects.** This is one
OBJECT beyond R25's literal words ("these two are the only system tables"); it is authorized by step 1 of
the prompt, which put both options in front of this seat and required one to be taken. Named in ESCALATE.

## Step 2 — 0006 is a contrast, not a template

`0006_radar_score.sql:198-200` is `GRANT SELECT, REFERENCES ON system.radar_score TO cobalt_user;` /
`… system.radar_score_run …` / `GRANT SELECT ON system.radar_board_v TO cobalt_user;` — those tables are
MEANT to be read user-side (radar scores feed ASET sizing). **0010/0011 diverging from that pattern is
deliberate (R25), not an inconsistency to fix toward 0006: the two sets of tables have opposite tenancy
answers (L32), and both migrations now say so in their own comments so the next reader cannot mistake it.**

## Step 3 — tests first (RED), then the SQL (GREEN)

Parametrized over `(path, table)` pairs, the way the existing `test_each_table_is_owned_by_the_system_role`
is — **five new OFFLINE tests, no `requires_db` marker**, all through the file's own `_code()` helper so a
REVOKE living only in a `--` comment cannot pass them:

| test | pins |
|---|---|
| `test_each_table_revokes_everything_from_cobalt_user[path0-archive_progress]` | `REVOKE ALL ON system.archive_progress FROM cobalt_user;` present in `0010` |
| `…[path1-archive_incidents]` | the same statement for `archive_incidents` in `0011` |
| `test_the_revoke_comes_after_the_table_exists[path0-archive_progress]` | `.index()` of the `CREATE TABLE IF NOT EXISTS` < `.index()` of the REVOKE |
| `…[path1-archive_incidents]` | the same ORDER for `0011` |
| `test_the_incident_sequence_is_also_revoked_from_cobalt_user` | `REVOKE ALL ON SEQUENCE system.archive_incidents_id_seq FROM cobalt_user;`, ordered after the `CREATE TABLE` |

**SPELLING — `REVOKE ALL`, stated rather than silently picked.** §11's word is "nothing", not "no SELECT
specifically". `REVOKE ALL` is the spelling that matches it; it costs nothing today (SELECT is the only
privilege the role holds on these objects, per step 1) and stays correct if a later migration ever adds a
different default grant to `cobalt_user` in schema `system` that this design never intended for these two.

**RED, before any SQL change** — `uv run pytest -q tests/cobalt/test_archiver_migrations.py -k revoke`:

```
FAILED …::test_each_table_revokes_everything_from_cobalt_user[path0-archive_progress] - AssertionError: assert 'REVOKE ALL ON system.archive_progress FROM cobalt_u...
FAILED …::test_each_table_revokes_everything_from_cobalt_user[path1-archive_incidents] - AssertionError: assert 'REVOKE ALL ON system.archive_incidents FROM cobalt_...
FAILED …::test_the_revoke_comes_after_the_table_exists[path0-archive_progress] - ValueError: substring not found
FAILED …::test_the_revoke_comes_after_the_table_exists[path1-archive_incidents] - ValueError: substring not found
FAILED …::test_the_incident_sequence_is_also_revoked_from_cobalt_user - AssertionError: assert 'REVOKE ALL ON SEQUENCE system.archive_incidents_id_...
5 failed, 58 deselected in 0.08s
```

**THE SQL.** `0010_archive_progress.sql` — one statement after `ALTER TABLE … OWNER TO cobalt_system;`,
with the cause and the 0006 divergence in its comment:

```
REVOKE ALL ON system.archive_progress FROM cobalt_user;
```

`0011_archive_incidents.sql` — in the existing grants section, beside the sequence grant already there:

```
REVOKE ALL ON system.archive_incidents FROM cobalt_user;
REVOKE ALL ON SEQUENCE system.archive_incidents_id_seq FROM cobalt_user;
```

**GREEN** — `uv run pytest -q tests/cobalt/test_archiver_migrations.py`: **`53 passed, 10 skipped in 0.03s`**
(63 collected = 58 before + 5 new; the 10 skips are the file's `requires_db` half, the two named ones
included).

**ONE EXISTING OFFLINE TEST HAD TO CHANGE, and it is named here rather than buried.**
`test_nothing_is_granted_to_cobalt_user` asserted `"cobalt_user" not in _code(path)` — the ROLE NAME's
absence. A REVOKE has to name the role, so R25's ruling makes that assertion false by construction. Its
INTENT is untouched and is what R25 affirms; only its mechanism moved: it now asserts `"TO cobalt_user"
not in code` (the direction — no grant), and still asserts the bare name is absent from both
`.rollback.sql` files, where nothing names it. **This is not one of the two `requires_db` tests the prompt
froze** (`test_the_user_role_has_no_grant_on_either_table[archive_progress|archive_incidents]`,
`:391-398` before this edit) — those are byte-for-byte unchanged and still SKIP.

**IDEMPOTENCY — a Postgres fact, NOT tested here.** `REVOKE` on a privilege the grantee does not currently
hold succeeds as a no-op rather than erroring, so re-running 0010/0011 against a database where the REVOKE
already applied is safe, exactly as idempotent as the files' existing `CREATE TABLE IF NOT EXISTS`. **Only a
live `cobalt db migrate` run twice proves it. It is OWED to the DB re-run, alongside the two `requires_db`
tests, and is not claimed as tested by this chunk.** The existing offline
`test_both_migrations_are_idempotent` scans `CREATE …` statements only and says nothing about a REVOKE.

**NEITHER `.rollback.sql` CHANGED.** `DROP TABLE IF EXISTS system.archive_progress;` /
`… system.archive_incidents;` remove the table and every privilege recorded on it, the REVOKE included —
there is nothing for a rollback to undo. `0011`'s rollback already notes its sequence goes with the table.

**COMMIT `193a2ca`** — `fix(db-migrate): REVOKE cobalt_user off system.archive_progress and
system.archive_incidents (cto-2026-09-19 R25 "B", DB-1)`. `git show --stat HEAD`: exactly
`src/cobalt/db_migrations/0010_archive_progress.sql`, `src/cobalt/db_migrations/0011_archive_incidents.sql`,
`tests/cobalt/test_archiver_migrations.py` — 3 files, 101 insertions, 3 deletions. No other path.

## Step 4 — §11 confirmed, NOT edited

The sentence R25 names, quoted from
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §11, first paragraph:

> Both SYSTEM side (L32: market-data bookkeeping, nothing of one trader's choice; `placement.py` gains both;
> `cobalt_user` is granted nothing on them).

**It was correct as written and stays untouched** — this chunk makes it true in the SQL, and true in the
database once the DB re-run proves it. §15's "Migrations" bullet (`… `cobalt_user` has no grant`) is
likewise correct and stays: the test it demands exists and is currently skipping, not missing.

**`docs/30 - Design/` was NOT touched.** One sentence in §11 nevertheless reads wrong to this seat, and it
is escalated rather than edited — see R3-1. The reason for escalating instead of editing: R25 ruled the
substance and explicitly said §11 "stands as written"; editing a tribunal-derived FINAL design (L67) on a
sentence the ruling did not name would extend R25, which this chunk is told not to do.

## CLOSE — offline numbers

| check | result |
|---|---|
| `uv run pytest -q tests/cobalt/test_archiver_migrations.py` | `53 passed, 10 skipped in 0.03s` — the two `requires_db` grant tests SKIP (not run, not xfail) |
| `uv run pytest -q tests/cobalt tests/taxonomy` | **`1871 passed, 320 skipped, 1 xfailed, 15 warnings in 44.43s`** — 0 failed |
| vs the DB run's offline close (1866 passed / 0 failed / 320 skipped) | failed **0**, unchanged · passed **+5**, exactly the five new tests named in step 3 · skipped **320**, unchanged (this chunk added no `requires_db` test) |
| `uv run cobalt jobs restarts c14e6f9..HEAD` | verbatim below — 3 paths, **0 UNCLASSIFIED** |
| `git diff c14e6f9 HEAD -- src/cobalt/archiver/ src/cobalt/radar/` | **EMPTY** (the prompt's `main`-based form cannot be empty on this branch — see R3-5) |
| `git status --porcelain` | empty |
| `git diff --stat c14e6f9 HEAD -- src tests docs` | the 3 paths above, +101/−3; this report's own path joins it with the closing docs commit |

```
path	change	rule	restart
src/cobalt/db_migrations/0010_archive_progress.sql	M	non-Python src asset	-
src/cobalt/db_migrations/0011_archive_incidents.sql	M	non-Python src asset	-
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
RESTARTS: none
```

**RESTARTS: none** for THIS CHUNK. The branch's own deploy line is unchanged and still
`com.cobalt.aset com.cobalt.radar` (round 1's ESCALATE (iv) item 4, driven by `tunables.yaml`, which this
chunk does not touch). A migration file derives no restart of its own; it ships through
`cobalt db migrate --allow-prod` inside the pause (L66/L43), as round 1's deploy list already says.

## ROUND 3 ESCALATE

**CARRIED FORWARD UNTOUCHED, nothing re-litigated, nothing resolved here:** round 1's `## ESCALATE` in
full — (i) the §14 OPEN table O-1…O-7 with what was built as the safe default, (ii) the never-run
`requires_db` tests **(CLOSED by the DB run)**, (iii) the cross-branch table (`sprint-2/p4` shares
`db_migrations/__init__.py`, `placement.py`, `tunables.yaml`, `cli.py`, `archiver/runner.py`,
`archiver/store.py`; P4's `_check_demand` call must be re-applied at the top of the rewritten
`_run_targets`), (iv) the deploy-prompt list 1–6, (v) §12's five known limits, and its numbered findings
1–8 · round 2's **R2-1** (the shadow artifact's timezone, ET — a ruling still OWED from the desk or the
owner), **R2-2**, **R2-4** · the DB run's **DB-2**
(`test_the_own_connection_upsert_survives_another_transactions_rollback` unobservable under conftest's
autouse single-transaction fixture — **NOT ruled, NOT touched here, status unchanged: ruling owed**),
**DB-3** (the step-order lesson, settled for future prompts) and **DB-4** (the two index-card drifts,
settled). **Nothing in this run supersedes any of them.**

**NEW THIS RUN — 6 items.**

**R3-1. §11 carries a second sentence that this chunk makes visibly wrong, and it was NOT edited.** Quoted
from §11's "Migrations" bullet:

> Ownership and grants follow `0006_radar_score.sql`'s pattern for a system table — the builder reads it,
> never invents one.

After R25 the grants deliberately do NOT follow 0006's pattern: 0006 GRANTS `cobalt_user` read, 0010/0011
REVOKE it. Read narrowly the sentence means "state grants explicitly rather than relying on default
privileges", which the REVOKE also satisfies — but read plainly it would send the next builder to copy
`0006:198-200` and re-open exactly the hole DB-1 found. **This seat did not edit it** (see step 4).
**Proposed wording for the desk or the tribunal, one clause added:** "Ownership and the SYSTEM-role grants
follow `0006_radar_score.sql`'s pattern; the user-side grant is its OPPOSITE — `cobalt_user` is revoked,
not granted (`cto-2026-09-19` R25)." **DECIDES: the desk or the tribunal that derived the FINAL design.**

**R3-2. The sequence REVOKE is one object beyond R25's literal wording.** R25 says "these two are the only
system TABLES that role cannot read"; `archive_incidents_id_seq` is a sequence. The prompt's step 1 put
option (i) revoke / (ii) narrow-the-comment in front of this seat and required a choice; (i) was taken and
is reasoned above. **If the desk wants the sequence readable after all, the single line to drop is
`0011_archive_incidents.sql`'s `REVOKE ALL ON SEQUENCE …` plus
`test_the_incident_sequence_is_also_revoked_from_cobalt_user`.** Flagged for visibility, not as a doubt.

**R3-3. STILL OWED TO THE DB RE-RUN — three things, none provable offline.** (a)
`test_the_user_role_has_no_grant_on_either_table[archive_progress]` and `[archive_incidents]` — red on
`cobalt_dev` in the DB run, expected GREEN after this chunk, **not yet proven**; (b) the apply-twice
IDEMPOTENCY of the new REVOKE statements on real Postgres (stated as a Postgres fact above, never as a
test result); (c) nothing here proves the REVOKE actually bites against the default-privilege grant — only
`has_table_privilege('cobalt_user', …)` on a migrated database does. **The re-run's order matters: apply →
suite → roll back (DB-3), not the DB run's original order.**

**R3-4. An existing offline test's MECHANISM changed, by necessity, and is recorded here.**
`test_nothing_is_granted_to_cobalt_user` moved from "the role name never appears" to "no grant in the
role's direction", because R25's REVOKE must name the role. Intent unchanged; the rollback files still
assert full absence. Named so no reviewer finds it as a surprise diff. **No other pre-existing test in the
file was altered, and the two frozen `requires_db` tests are byte-identical.**

**R3-5. The prompt's close check `git diff main -- src/cobalt/archiver/ src/cobalt/radar/` CANNOT be empty
on this branch, and was not.** It returns ~140 KB — the branch's OWN archiver build from rounds 1/2:
`git diff --stat main -- …` = `cli.py`, `incidents.py`, `progress.py`, `quiet.py`, `reconcile.py`,
`report.py`, `runner.py`, `settings.py`, `shadow.py`, `store.py`, 10 files, +3477/−44, and ZERO
`src/cobalt/radar/` files. The check as written asks this chunk to prove the branch has no archiver build,
which is its entire purpose. **The check that carries the intended meaning — did THIS chunk touch archiver
or radar source — is `git diff c14e6f9 HEAD -- src/cobalt/archiver/ src/cobalt/radar/`, and it is EMPTY.**
Reported rather than silently substituted; the next prompt of this shape should anchor the check on the
chunk's branch point, not on `main`.

**R3-6. Citation drift in DB-1's own text, named for the record.** DB-1 cites the default-privilege grant as
`0001_schemas.sql:150-152`; the statement actually spans `:149-151` (`:152` opens the SEQUENCES twin). The
prompt's `:149-151` is correct. Quoted from the file above; no consequence beyond the citation.

**MEMORY:** none proposed — this run changed no law and no standing practice; R25 is already recorded in
`cto-2026-09-19.md` §4 and is owed a `areas/cobalt-product-definition.md` line at the desk's fold.
**RULING:** R3-1 (the §11 "follows 0006's pattern" sentence) is the one new item owed a decision. DB-2 and
R2-1 remain owed, untouched.

## Round 3 PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 13:15:44 EDT 2026` |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — EMPTY |
| `Bash(git status*)` | `git status` | 0 | allowed — `On branch archiver/append-0919` / `nothing to commit, working tree clean`; no rebase in progress |
| `Bash(git log*)` | `git log --oneline -1` | 0 | allowed — `c14e6f9 docs(report): archiver db run — fill the stop line's sha (code tip d2099e1, report 2e4ca6f)` = the expected first-launch tip |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `1dfc8cb docs(desk): 09-19 R25 (DB-1 = B, explicit REVOKE); archiver round-3 chunk prompt (40)` (recorded, no equality required) |
| `Bash(ls *)` | `ls -la .env` | 1 | allowed — `No such file or directory`, as required: this run never sees the dev database |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_archiver_migrations.py` | 0 | allowed — **58 tests collected**, both frozen `requires_db` grant tests present and unchanged |
| `Bash(grep *)` | the 21 authorization `grep -c` calls | 0 | allowed — see below |

**AUTHORIZATION — verified, HOLDS.** All 16 `Bash(...)` rule strings, `--disallowedTools "AskUserQuestion"
"EnterWorktree"` and the three `--add-dir` values counted ≥1 in
`prompts/2026-09-19/26-archiver-round2.md`. Four counted **2** rather than 1 — `Bash(uv run pytest *)`,
`Bash(uv run cobalt jobs restarts *)`, the deny pair and `--add-dir /Users/cobalt/cobalt-wt`. Located, not
assumed: the second hit is 26's OWN PROSE (its line 1 "NO NEW RULE" sentence and its line 18 AUTHORIZATION
paragraph), never a differing rule; 26's committed launch line (line 5) carries every string exactly once.
**No rule in this run's line is absent from 26's, none is altered, none added.** The WORK ITEM is
authorized by `cto-2026-09-19.md` §4 R25 (13:10 ET, "B" — read in full, quoted in step 3's commit),
DB-1 in this report's `# DB RUN` section, and §11/§15 of the FINAL design.

ARCHIVER R3 193a2ca (code tip; report cedf3dc, and this line's own docs-only commit on top) | offline 1871/0 (320 skipped, unchanged — `.env` absent so all 23 `requires_db` skip; passed +5 = the five new offline pins) | DB-1: REVOKE in 0010 + 0011 (offline pin green; the sequence `archive_incidents_id_seq` revoked with its table, R3-2; 2 requires_db OWED to the DB re-run, with apply-twice idempotency, R3-3) | DB-2: not touched — ruling owed | §11: confirmed, NOT edited; its "follows 0006's pattern" sentence escalated as R3-1 | RESTARTS: none | ESCALATE: 6 | cobalt_dev: untouched
