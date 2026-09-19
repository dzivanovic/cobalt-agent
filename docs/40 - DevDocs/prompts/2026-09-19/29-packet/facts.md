# facts.md — round 2, desk's pre-computed measurements, archiver-append-0919

All commands run read-only from `/Users/cobalt/cobalt` against the already-fetched branch
`archiver/append-0919` (worktree `/Users/cobalt/cobalt-wt/archiver-append`, clean,
`git status --porcelain` empty). Nothing here was run inside the worktree.

## Commits, round 2 (`c974fbf..archiver/append-0919`)

```
fb825df docs(report): archiver append round 2 — 7 REAL findings folded, F1 blocker fixed, 1866/0/320 offline, 23 requires_db owed
9056e73 test(db-migrate): pin NULLS NOT DISTINCT on the archive_incidents partial unique index (tribunal round 1, F7)
d9ddc2a fix(archiver): the shadow artifact's night is the ET trading date, not the UTC date of the run instant (tribunal round 1, F6)
ec045bd fix(cli): QuietRefused and ArchiveLockError exit 2 on the production cobalt entry, every other exception unchanged (tribunal round 1, F5)
e5bec36 test(archiver): four quiet-window tests assert on command behaviour, not names or attributes (tribunal round 1, F4)
b9e165b test(archiver): differing-value and equal-value race tests (spec §15, tribunal round 1, F3/Q10)
806f45f fix(archiver): restate --apply writes bars on the repair's own transaction so a failed pre-commit re-check rolls them back (tribunal round 1, F1); the two named §8 boundary tests drive the command path (F2)
```

- Branch tip: `fb825df` (the round-2 report commit sits on top of the last round-2 CODE commit)
- **Round-2 code tip** (the round-2 stop line's claimed tip): `9056e73` — CONFIRMED, it is the newest non-report commit; `fb825df` is the report-only commit on top
- Round-1 code tip (this round's base): `c974fbf` — CONFIRMED, matches round-2 prompt's stated starting point
- Worktree: `git -C /Users/cobalt/cobalt-wt/archiver-append status` → `On branch archiver/append-0919`, `nothing to commit, working tree clean`
- Radar diff re-run, both forms: `git -C /Users/cobalt/cobalt diff main...archiver/append-0919 -- src/cobalt/radar/` and `main..archiver/append-0919 -- src/cobalt/radar/` → **0 bytes, both forms** — CONFIRMED EMPTY, independently re-run this round, not just quoted from the report

## Diff-stat, `c974fbf..archiver/append-0919` (round 2's own change only)

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

**No path outside `src/cobalt/archiver/`, `src/cobalt/cli.py`, `tests/cobalt/`, `docs/40 - DevDocs/`.**
No `scratch/`, no `.env`, no data file, nothing under `src/cobalt/radar/` or `configs/`. `configs/` is
untouched this round (round 2 added no config key).

## F1–F7 — verified at file:line by this hub, independent of the round-2 report's own claims (L35)

| finding | fix claimed | file:line, confirmed | matches verdict row's "fix in one line"? |
|---|---|---|---|
| F1 BLOCKER | `restate --apply` writes bars on the SAME connection/transaction as the pre-commit re-check | `archiver/store.py:127` new `def upsert_bars_on(self, conn, bars)` (connection-taking sibling, no internal connect/commit); `archiver/cli.py:391` `_apply_restate(store, conn, ticker, interval)` now takes `conn` and calls `store.upsert_bars_on(conn, rows)` (was `store.upsert_bars(rows)`, which opened its own connection); `cli.py:267` `_apply_restate` is called INSIDE `with store.target_transaction() as conn:`, and `guard.check_before_commit()` (`cli.py:287`) runs AFTER both the bar write and the incident write, inside the same block | YES — matches "pass the re-check into the write … or do the overwrite on `conn`"; the build chose the `conn`-taking sibling method, keeping ONE copy of the `ON CONFLICT DO UPDATE` SQL (L3) |
| F1 sibling check | `backfill-missing` already safe | `archiver/cli.py:313-315` region: `_cmd_backfill_missing` already calls `store.insert_new_bars(conn, …)` inside `target_transaction()` — CONFIRMED by reading `insert_new_bars`'s signature (`store.py:239`, takes `conn` first, no internal connect/commit) | YES — the report's "already-safe" claim holds on direct read, not just cited |
| nightly `upsert` path unaffected | `store.upsert_bars` itself untouched in shape; nightly call site (`runner.py:130`-region) unaffected apart from the F6 line | `git diff c974fbf..archiver/append-0919 -- src/cobalt/archiver/runner.py` shows exactly TWO changes: a new `_trading_night()` helper function, and the `night=` argument at the shadow-write call changing from `clock().date()` to `_trading_night(clock())`. The `store.upsert_bars(bars)` call itself (the nightly `upsert`-mode write) is NOT in this diff at all — CONFIRMED unchanged. `store.py`'s `upsert_bars` (not `_on`) still opens its own connection (`self._connect()`, store.py ~line 105-121) and still takes `before_commit` — same signature as round 1 | YES |
| F2 MAJOR | the two named §8 boundary tests drive the command path, not only `quiet_verdict` | `test_archiver_quiet.py:614` `test_gemini_close_boundary_poller_lag(monkeypatch)`, `:701` `test_astra_open_boundary_repair_crosses_open(monkeypatch)` — both NOW take `monkeypatch` (round 1's versions took no args); `:527` `archiver_cli.HANDLERS[args.command](args)` appears in a helper used by both tests; comment at `:752` says "This drives `_cmd_restate` itself" | YES |
| F3/Q10 MAJOR | differing-value and equal-value race tests exist | `test_archiver_quiet.py:1105-1107` section header "§15's named races (tribunal round 1, F3 = the desk's Q10)"; `:1129` `test_a_differing_value_race_the_repair_commits_last_and_its_value_survives`, `:1168` `test_a_differing_value_race_the_poller_writes_after_the_repair_committed`, `:1196` `test_an_equal_value_race_rewrites_nothing`, `:1227` `test_an_equal_value_race_offers_no_rows_to_the_writer` — 4 tests, 2 differing-value orderings + 2 equal-value angles, matching the report's claim of "the two differing-value orders, the equal-value command test, the equal-value comparison test" | YES — this closes the gap this hub itself flagged in round 1's `facts.md` |
| F4 MAJOR | four tests rewritten to assert on command behaviour | `:249` `test_the_refusal_exit_code_is_two(monkeypatch, capsys)` (was a bare class-attribute assert), `:836` `test_both_mutating_commands_are_refused_in_every_scanned_session` (now with fixture args, not just `quiet_verdict`), `:877` `test_previews_always_run(monkeypatch, capsys)`, `:953` `test_backfill_missing_never_calls_upsert_bars(monkeypatch)` — all four now take `monkeypatch`/`capsys`, consistent with driving a real call rather than asserting a class attribute | YES |
| F5 MAJOR | `QuietRefused`/`ArchiveLockError` exit 2 on the production `cobalt` entry | `src/cobalt/cli.py`: a new `except (QuietRefused, ArchiveLockError) as e:` clause, placed BEFORE the generic `except Exception as e:` clause, calling `sys.exit(e.exit_code)`; `archiver/store.py:39` `class ArchiveLockError(RuntimeError):` now carries `exit_code = 2` (`:50`) alongside `quiet.py`'s existing `QuietRefused.exit_code = 2` (`:73`, round 1) | YES |
| F6 MINOR | shadow artifact night = ET trading date | `archiver/runner.py`: new `def _trading_night(now)` helper, docstring names the bug plainly ("this was `now.date()` on a UTC instant … every artifact was named for the day after the trading night it recorded"), body is `from cobalt.session.clock import SessionClock; return SessionClock.to_et(now).date()`; the shadow-write call site now passes `night=_trading_night(clock())` | YES |
| F7 MINOR | `NULLS NOT DISTINCT` pinned in the migration test | `test_archiver_migrations.py:208-211`: `assert "NULLS NOT DISTINCT" in body, (...)` added to the existing `test_incidents_has_the_partial_unique_index_on_unresolved_rows`; the SQL clause itself (`0011_archive_incidents.sql:92`, unchanged since round 1) was already present — this is a test-coverage fix, not a code change, exactly as the round-2 report states | YES |

## `late` comparator (Q4 from round 1's review, spot-checked by Grok, re-confirmed here)

`reconcile.py:818` (unchanged this round): `late = 0 if plan.bootstrap else sum(1 for k in incoming if before is not None and k <= before)` — comparator is `<=`, matching design §7's "`late` = key ≤ the PREVIOUS `archived_through`". Round 1's Grok review already quoted this line; this round's diff does not touch `reconcile.py` at all (confirmed: `reconcile.py` does not appear in `git diff --stat c974fbf..archiver/append-0919`).

## Pure-data-fixture check (P4 lesson — exclude pure DATA fixtures from the packet, list them here with bytes)

Searched every file in the whole-build diff (`main...archiver/append-0919 -- src tests configs`) for large embedded literal data blocks (raw CSV/vendor-export blobs, base64, or similar) that would inflate a packet file without being logic a reviewer needs to read line by line. **None found.** Every test file's size is accounted for by ordinary Python test code (fixtures built as small in-line dicts/dataclasses, not pasted vendor exports) and docstrings. **0 bytes excluded from the packet on this basis** — the four `build-*.diff` files in this packet are the complete, unfiltered non-docs three-dot diff.

## Whole-build diff, split into 4 area buckets for Gemini (and offered whole to Astra)

Total non-docs three-dot diff (`main...archiver/append-0919 -- src tests configs ops`; `ops` and the rest of `configs` are unchanged beyond the one `tunables.yaml` block, confirmed empty against those two paths beyond that one file): **374,210 bytes**, 31 files, 8,755 insertions / 55 deletions.

| bucket | files | bytes | design sections that bind it |
|---|---|---|---|
| `build-A-settings-heartbeat-store.diff` | `tunables.yaml`, `archiver/settings.py`, `heartbeat/probes.py`, `test_heartbeat.py`, `test_heartbeat_archiver_incidents.py`, `test_archiver_settings.py`, `archiver/store.py`, `archiver/incidents.py`, `archiver/progress.py`, `test_archiver_append_store.py` | 97,907 | §4 (archive progress), §9 (lock, failure semantics), §10 (config keys), §11 (the two tables) — `spec-excerpt-A-settings-heartbeat-store.md` |
| `build-B-migrations-reconcile.diff` | the four 0010/0011 SQL+rollback files, `db_migrations/__init__.py`, `placement.py`, `test_archiver_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py`, `archiver/reconcile.py`, `test_archiver_reconcile.py` | 111,567 | §3 (closed 3-0 items), §4 (candidate range), §6 (comparison), §7 (gaps/regression/counters), §11 (tables), §15 (migrations bullet) — `spec-excerpt-B-migrations-reconcile.md` |
| `build-C-runner-shadow-report.diff` | `archiver/runner.py`, `archiver/shadow.py`, `archiver/report.py`, `test_archiver_runner.py`, `src/cobalt/cli.py`, `test_finviz_consumers.py` | 76,100 | §5 (mode isolation, shadow compare), §9 (lock in both modes) — `spec-excerpt-C-runner-shadow-report.md` |
| `build-D-quiet-cli.diff` | `archiver/quiet.py`, `archiver/cli.py`, `test_archiver_quiet.py` | 88,636 | §6 (comparison/restate), §8 (quiet window, option A), §3 V3-7 (range=horizon), §15 (quiet-window + concurrency bullets) — `spec-excerpt-D-quiet-cli.md` |

Sum of the four buckets = 374,210 bytes = the whole diff, byte for byte (no path double-counted, none dropped — verified before staging).

## Full stop line (verbatim, last line of the report after round 2)

```
ARCHIVER APPEND R2 9056e73 | on archiver/append-0919 (round 1 c974fbf) | offline 1866/0 (320 skipped; round-1 close 1850/0/315) | F1 restate fixed · backfill-missing shape already-safe | F2 command-path tests added | F3/Q10 race tests offline+requires_db | F4 four tests rewritten fixed | F5 exit code 2 on cobalt fixed | F6 shadow night = ET date fixed | F7 NULLS NOT DISTINCT pinned fixed | radar diff: empty yes | write_mode ships: upsert (unchanged) | RESTARTS: com.cobalt.aset com.cobalt.radar | CARRIED: 23 requires_db tests never run (now includes this round's 5) | ESCALATE: 4
```

## `## ROUND 2 ESCALATE` — four items, one line each (verbatim from the report)

1. **R2-1 (timezone ruling owed):** spec §5's `<YYYY-MM-DD>` names no timezone; this round resolved it to the ET trading date (a fix-per-verdict-row, not a design change) — the desk/owner may still rule UTC, which would be a one-line change to `_trading_night` plus its test.
2. **R2-2 (no new finding):** `backfill-missing` needed no F1-shaped fix — confirmed by reading the code, not assumed, and now pinned by a new test so a future change that breaks this shape is caught.
3. **R2-3 (carried, unchanged in kind):** the `requires_db` first run is still OWED; the count moved from 18 to 23 (round 2 added 5, named in the report's CLOSE section) — none has ever run.
4. **R2-4 (disclosed refactor):** `test_upsert_bars_still_does_update_and_never_do_nothing` was REWRITTEN (not dropped) to match the new `upsert_bars`/`upsert_bars_on` split — the `ON CONFLICT … DO UPDATE` assertion moved to the sibling method, plus a new `test_only_one_copy_of_the_upsert_statement_exists` (L3). Also recorded, not an escalation: the run-level lock is taken BEFORE the quiet-window read, so a refused repair's call list starts `["run_lock"]` — correct per §8 Q4, now documented in tests.

Round 1's `## ESCALATE` (i)–(v) and its 8 numbered findings are carried forward UNTOUCHED — nothing in round 2 resolves or supersedes them.

## Packet contents (this folder)

- `fold.diff` — `git diff c974fbf..archiver/append-0919 -- src tests configs` (56,795 bytes) — for GROK only
- `build-A-settings-heartbeat-store.diff` (97,907 B), `build-B-migrations-reconcile.diff` (111,567 B), `build-C-runner-shadow-report.diff` (76,100 B), `build-D-quiet-cli.diff` (88,636 B) — the WHOLE updated build, non-docs, three-dot, split by area — for GEMINI (as separate calls) and ASTRA (whole)
- `spec-excerpt-A/B/C/D-*.md` — the design-section excerpts binding each bucket, for Gemini's per-call reads
- `spec-final-design.md` — the full FINAL design, verbatim — for Astra's whole-build read and for reference
- `verdicts-r1.md` — round 1's verdict table verbatim (what was found REAL and what fix each finding was owed) — the SPEC for what "fixed" means this round
- `facts.md` — this file
- `build-report.md` — the branch's current report (round 1 + round 2 sections), verbatim, as committed on `archiver/append-0919`
- `QUESTIONS-fold.md` — Grok's questions (fold-only)
- `QUESTIONS-whole.md` — Gemini's and Astra's questions (whole-build)
