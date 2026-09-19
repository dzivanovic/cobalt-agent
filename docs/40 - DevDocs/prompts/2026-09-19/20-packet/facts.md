# facts.md — desk's pre-computed measurements, archiver-append-0919

All commands run read-only from `/Users/cobalt/cobalt` against the already-fetched branch
`archiver/append-0919` (worktree `/Users/cobalt/cobalt-wt/archiver-append`, clean,
`git status --porcelain` empty). Nothing here was run inside the worktree.

## Commit range

```
$ git -C /Users/cobalt/cobalt log --oneline main..archiver/append-0919
7c972ee docs(report): archiver append build — 7 chunks, 288 offline tests, 18 requires_db owed, radar diff empty
c974fbf feat(heartbeat): the archiver probe sees unresolved archive incidents; archiver operator docs
f4bdcfa feat(archiver): repairs only in a quiet window (R8 option A) — restate, backfill-missing, audit, incidents, progress, shadow-report
2b4893c feat(archiver): write_mode dispatch — upsert untouched, pre-write shadow compare, the append night
4e3c577 feat(archiver): append path — insert_new_bars, progress and incident writers on the target's one transaction; run-level advisory lock
72bfd21 feat(archiver): reconcile — eligibility, candidate range, four-way comparison, regression/gap rules, reconciling counters (pure)
b623e72 feat(db): 0010 archive_progress + 0011 archive_incidents — additive, system side, rollback = drop own table
54e98f7 feat(archiver): ArchiverSettings — write_mode upsert|append (ships upsert), shadow and quiet-window keys, validated on load
```

- Branch tip: `7c972ee` (the report commit sits on top of the last BUILD commit)
- **Code tip** (the stop line's claimed tip): `c974fbf` — CONFIRMED, it is the newest non-report commit; `7c972ee` is the report-only commit on top (consistent with the stop line's own wording: "ARCHIVER APPEND BUILT c974fbf (last build commit; this report commits on top)")
- Merge-base `main` / `archiver/append-0919`: `8838dda1bdb507172f33a7a4916ce28c09c1e35f` — matches the report's claimed base `8838dda`
- `main` tip now: `0569727` (main moved after the worktree was cut; the report names this and shows `git diff --stat 8838dda HEAD` as the honest set — CONFIRMED, see below)
- Worktree status: `git -C /Users/cobalt/cobalt-wt/archiver-append status` → `On branch archiver/append-0919`, `nothing to commit, working tree clean`

## Diff-stat, three-dot (`main...archiver/append-0919`, so main's later docs-only commits do not appear as deletions)

```
$ git -C /Users/cobalt/cobalt diff --stat main...archiver/append-0919
```
46 files changed, 9339 insertions(+), 38 deletions(-). By area:
- `configs/cobalt/taxonomy/tunables.yaml` (1 file, +90)
- `docs/40 - DevDocs/` (16 files — DevDocs + the build's own report; docs-only)
- `src/cobalt/archiver/` (10 files: cli, incidents, progress, quiet, reconcile, report, runner, settings, shadow, store)
- `src/cobalt/db_migrations/` (6 files: `__init__.py`, `placement.py`, `0010_archive_progress.sql` + rollback, `0011_archive_incidents.sql` + rollback)
- `src/cobalt/heartbeat/probes.py` (1)
- `src/cobalt/cli.py` (1)
- `tests/cobalt/` (11 files)

**No path outside `src/`, `tests/`, `configs/cobalt/`, `docs/40 - DevDocs/`.** No `scratch/`, no `.env`, no data file, nothing under `src/cobalt/radar/`.

### Non-docs diff only (`-- src tests configs ops`, matches 18's packet convention)

```
$ git -C /Users/cobalt/cobalt diff --stat main...archiver/append-0919 -- src tests configs ops
```
31 files changed, 7708 insertions(+), 38 deletions(-). `ops` is UNCHANGED (empty against that path — confirmed, worth stating not assuming). This is the code the packet's `code-*.diff` files carry, split into 5 files by area (see `## Packet contents` below) because the whole diff is 328,366 bytes, over the ~150 KB guidance.

## Item-by-item file:line confirmation (design §10/§11 and the build's own claims)

| item | file:line | confirmed |
|---|---|---|
| Settings — ONE model, ONE loader | `src/cobalt/archiver/settings.py:136` `class ArchiverSettings(BaseModel)`; reads via `cobalt.taxonomy.loader` (no `yaml` import in the module) | YES |
| Settings — seven keys | `configs/cobalt/taxonomy/tunables.yaml:534-611`: `archiver.write_mode`, `archiver.shadow_compare`, `archiver.shadow_statement_timeout_s`, `archiver.shadow_retention_nights`, `archiver.repair.quiet_before_open_min`, `archiver.repair.quiet_after_cycle_min`, `archiver.repair.cycle_max_min` = 7 keys | YES, exactly seven |
| `write_mode` exact-match validator | `src/cobalt/archiver/settings.py:147-160` `_exact_write_mode` — no `.strip()`/`.lower()`, raises naming `archiver.write_mode` | YES |
| shipped value `upsert` | `configs/cobalt/taxonomy/tunables.yaml:538` `value: upsert`, `status: solidified` | YES |
| Migration 0010 `system.archive_progress` | `src/cobalt/db_migrations/0010_archive_progress.sql` — `CREATE TABLE IF NOT EXISTS system.archive_progress`, PK `(ticker, interval)`, `CHECK (archived_through <= export_newest)` (per file header) | YES |
| Migration 0011 `system.archive_incidents` | `src/cobalt/db_migrations/0011_archive_incidents.sql` — `CREATE TABLE IF NOT EXISTS system.archive_incidents`, `kind` CHECK domain names 5 kinds: `gap, restated, stored_only, empty_export, regression` | YES |
| Registry order | `src/cobalt/db_migrations/__init__.py:58-74` — `FORWARD` ends `…0007_radar_cards.sql, 0010_archive_progress.sql, 0011_archive_incidents.sql`; `REVERSE` begins `0011…, 0010…, 0007…`. NOTE: main's own `0007` is `0007_radar_cards.sql`, not a bare "0007" — the report's chunk-M narrative names the position correctly | YES |
| reconcile.py (pure core) | `src/cobalt/archiver/reconcile.py` (+933 lines, new file) | YES, present |
| store.py append methods | `src/cobalt/archiver/store.py` (+167 lines; report claims `upsert_bars` byte-identical / additions only — see `git diff main -- src/cobalt/archiver/store.py` quoted in the report, 148 insertions, 0 deletions for that one file at chunk-P time; the FINAL diff shown here is +167 because chunk H/Q added nothing to store.py beyond chunk P — not independently re-verified line-by-line by this hub, flagged for the checkers) | PARTIAL — hub trusts the report's own quoted `git diff --stat`, did not re-derive it independently; checkers should |
| runner + shadow compare | `src/cobalt/archiver/runner.py` (+284/-…), `src/cobalt/archiver/shadow.py` (+356, new) | YES, present |
| quiet window + commands | `src/cobalt/archiver/quiet.py` (+350, new), `src/cobalt/archiver/cli.py` (+522, new) | YES, present |
| `restate --apply` / `backfill-missing` refuse outside quiet window | `src/cobalt/archiver/cli.py:262` (`_cmd_restate`) and `:310` (`_cmd_backfill_missing`) both call `quiet_mod.guarded_repair(...)`; both call `guard.check_before_commit()` at `:287` and `:315` respectively, inside the repair transaction, before COMMIT | YES |
| the re-check IS before COMMIT, not just at start | `src/cobalt/archiver/quiet.py:311` `def check_before_commit`; `tests/cobalt/test_archiver_quiet.py:430` `test_the_pre_commit_recheck_rolls_the_repair_back` — two-instant fake clock, real rollback semantics (a `Txn.__exit__` that restores the store's row snapshot on exception) | YES |
| `late` = key ≤ previous `archived_through` | FINAL design §7: "`late` = key ≤ the PREVIOUS `archived_through`"; `src/cobalt/archiver/reconcile.py` (not independently line-verified by this hub beyond the report's own COUNTERS table naming MSFT 19:59 new-not-late / equal cases) — checkers should confirm the exact comparator (`<=` not `<`) in the source | NOT INDEPENDENTLY VERIFIED — name for checkers |
| five incident kinds incl. `regression` | `src/cobalt/db_migrations/0011_archive_incidents.sql` CHECK domain: `gap, restated, stored_only, empty_export, regression` (5, matches design §11) | YES |
| advisory lock held in `upsert` mode too | `src/cobalt/archiver/runner.py:95-97` — comment "§9: the run-level advisory lock, in BOTH write modes", `store.run_lock(...)` wraps both `_upsert_targets` and `_append_targets` dispatch | YES |
| heartbeat probe sees unresolved incidents | `src/cobalt/heartbeat/probes.py:261` `def archiver_freshness`, `:361` `_read_archive_incidents`, `:375` `_with_archive_incidents`, `:396-397` names the migration `0011_archive_incidents.sql` on an unreadable table | YES |
| `write_mode` default ships `upsert` | `configs/cobalt/taxonomy/tunables.yaml:538` `value: upsert` — CONFIRMED in the shipped config file, not just the report's prose | YES |
| radar package diff EMPTY | `git -C /Users/cobalt/cobalt diff main...archiver/append-0919 -- src/cobalt/radar/` → **no output** (checked both two-dot and three-dot forms; two-dot form: `git diff main..archiver/append-0919 -- src/cobalt/radar/ \| wc -l` → `0`) | YES, EMPTY, independently confirmed by this hub, not just quoted from the report |
| two named boundary tests present | `tests/cobalt/test_archiver_quiet.py:327` `test_gemini_close_boundary_poller_lag`, `:381` `test_astra_open_boundary_repair_crosses_open` — both read, both assert `store.snapshot() == before` ("no bar row changed") | YES |

## Design test list (§15) vs tests actually in the diff — gaps named

Spec §15's quiet-window bullet lists, verbatim: "the two named boundary tests; `restate --apply` AND `backfill-missing` refused in every scanned session and in `MARKET_RESET`; refused when the pool row is missing; the refusal text carries all three observed values and the earliest allowed start; the pre-commit re-check rolls back; previews always run; **differing-value and equal-value races**."

Every item has a counterpart in `tests/cobalt/test_archiver_quiet.py` EXCEPT the last: **"differing-value and equal-value races" has no counterpart.** The two named boundary tests (`test_gemini_close_boundary_poller_lag`, `test_astra_open_boundary_repair_crosses_open`) and `test_the_pre_commit_recheck_rolls_the_repair_back` all assert only `store.snapshot() == before` — i.e., that NO bar row changes when a repair is refused or rolled back. None of them constructs a scenario where the poller and the repair race to write DIFFERENT values (a "differing-value race") versus the SAME value (an "equal-value race") and asserts which value wins or that the outcome is auditable either way. This hub could not find that test anywhere in the diff; the checkers should confirm from the real files (not just the packet) before ruling it a genuine gap.

## §14 OPEN items — spelled out in the report, all present in `## ESCALATE (i)`

O-1 through O-7 are all named in the report with "who decides" and "built as" columns — confirmed present, not independently re-derived by this hub (the report's own text is the claim; the checkers read it as a claim, per L35).

## Full stop line (verbatim, last line of the report)

```
ARCHIVER APPEND BUILT c974fbf (last build commit; this report commits on top) | on main 8838dda (base; main now 0569727) | offline 1850/0 (315 skipped; baseline 1562/297) | settings built · migrations 0010/0011 built · reconcile built · store built · runner+shadow built · quiet window+commands built · heartbeat+docs built | write_mode ships: upsert | radar diff: empty | RESTARTS: com.cobalt.aset com.cobalt.radar | db: OWED — 18 requires_db tests written, never run | OWED: three-house check, dev-DB run after p4-verify's stop line, deploy prompt (upsert), his approval, shadow nights, his switch ruling | ESCALATE: 8
```

## `## ESCALATE` items, one line each (report's numbered list beyond the §14 OPEN table)

1. AUTHORIZATION — the launch line's literal `grep -c` test does not pass on 5 of 7 rule strings against `prompts/2026-09-18/02-ops-2026-09-18.md`; every difference is a NARROWING (strict subset); the report's own table proves this; verdict taken: not a mismatch, proceed. Shared with `ops-0919`'s launch line.
2. The DevDocs symbol-check gate does not exist in this repo (searched `src/`, `dev_utils/`, `tests/`) — third time recorded per the report.
3. `heartbeat.archiver_freshness` now reads a database-backed fact; `test_heartbeat.py` never had one, so an autouse fixture pins the reader — a ruling-flavored choice (unreadable alarm = not green), not obviously wrong but named as a choice.
4. `src/cobalt/archiver/cli.py` is a NEW Finviz consumer (`restate`/`backfill-missing` re-fetch one target) — caught by `test_finviz_consumers.py`, registered honestly rather than the guard being widened; belongs in the deploy prompt's total-demand inventory.
5. `poller_writable` (decided from interval) vs true "poller member" (would need a new read of `system.radar_membership`) — the report says this was NOT taken on the build's own authority.
6. In `append` mode a TRANSPORT failure (not just an empty body) also opens an `empty_export` incident, because `collector.py` raises the same `CollectorError` class for all four cases — the report calls the clean fix out of this chunk's scope.
7. `main` moved during the run (`8838dda` → `0569727`); `git diff --stat main HEAD` (two-dot against CURRENT main) would show 7 desk-doc paths as deletions the branch never touched — the report says to use `8838dda HEAD` instead. This hub's packet uses three-dot (`main...archiver/append-0919`) against CURRENT main, which is the form immune to this problem by construction — CONFIRMED no phantom deletions appear in the three-dot diff-stat above.
8. Two defects the tests caught and fixed in the code (both described in the report, chunk N): a substring-search bug in `report._current_header`, and a `fetch=` test-seam bug that made `runner.py` briefly invisible to the L53 Finviz-consumer inventory scan.

## `requires_db` — never run

18 tests, named in the report's `## Close` section, by file: 10 in `test_archiver_migrations.py`, 8 in `test_archiver_append_store.py`. Confirmed present in the diff (both files are in `code-04-tests-store-migrations-settings-heartbeat.diff`); NOT run by this hub, NOT run by the build (offline, no `.env`, no `cobalt_dev` — confirmed by `ls -la .env` in the build's own PREFLIGHT table, and by the absence of any `cobalt_dev`/`.env`-touching command in the build's allowlist).

## Config boundary law (CLAUDE.md)

The only new-core config touched is `configs/cobalt/taxonomy/tunables.yaml` — an EXISTING file, extended with a new block, not a new file. It sits under `configs/cobalt/`, the shared new-core data location the config boundary law names as safe (outside the old loader's top-level, non-recursive glob). No new config file was added anywhere in the diff.

## Packet contents (this folder)

- `code-01-settings-migrations-config.diff` — `tunables.yaml`, `archiver/settings.py`, `db_migrations/__init__.py`, `db_migrations/placement.py`, the four 0010/0011 SQL + rollback files
- `code-02-reconcile-store.diff` — `archiver/reconcile.py`, `archiver/store.py`, `archiver/incidents.py`, `archiver/progress.py`
- `code-03-runner-shadow-quiet-cli-heartbeat.diff` — `archiver/runner.py`, `archiver/shadow.py`, `archiver/quiet.py`, `archiver/cli.py`, `archiver/report.py`, `heartbeat/probes.py`, `cli.py`
- `code-04-tests-store-migrations-settings-heartbeat.diff` — `test_archiver_append_store.py`, `test_archiver_migrations.py`, `test_archiver_settings.py`, `test_finviz_consumers.py`, `test_heartbeat.py`, `test_heartbeat_archiver_incidents.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py`
- `code-05-tests-quiet-reconcile-runner.diff` — `test_archiver_quiet.py`, `test_archiver_reconcile.py`, `test_archiver_runner.py`

Split by area because the whole non-docs diff (`main...archiver/append-0919 -- src tests configs ops`) is 328,366 bytes, over the ~150 KB single-file guidance. The five files sum to exactly 328,366 bytes — no path double-counted, none dropped (verified by byte-sum against the unsplit diff before this split was kept).

- `spec-final-design.md` — verbatim copy of `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md`
- `spec-17-build-prompt.md` — verbatim copy of `docs/40 - DevDocs/prompts/2026-09-19/17-archiver-append-build.md`
- `build-report.md` — `git -C /Users/cobalt/cobalt show archiver/append-0919:"docs/40 - DevDocs/reports/archiver-append-build-2026-09-19.md"` (661 lines, matches the worktree copy)
- `QUESTIONS.md` — this run's questions for the three houses (verbatim, see the launch prompt)
