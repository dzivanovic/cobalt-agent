# Archiver append-only — BUILD (tribunal FINAL design), `archiver-append-0919`

DO NOT STOP until `ARCHIVER APPEND BUILT`
Seat `archiver-append-0919`, Opus 5, OFFLINE, worktree `/Users/cobalt/cobalt-wt/archiver-append`, branch `archiver/append-0919` off main `8838dda`.
Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` (committed on main `8838dda`).
Status: PREFLIGHT green (9/9 allowed, 0 denied). BASELINE running.
ESCALATE: pending.

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

CONTINUE: step 4
