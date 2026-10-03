# lock-relief — check, pass 1 (2026-10-03)

## §0 Headline
- Check of `lock-relief`, pass 1, on `77d19438`. No outside house: his overrule (2026-10-02 R47). I read alone, ran every finding and fixed what held.
- 2 findings, both HELD and FIXED. O1 (X1): a test with no skip mark that called `db.connect_migration` reached `cobalt_dev` with neither half of G1 seeing it; `dev_db_tx` now guards every `psycopg.connect` after its own open (`18f03c41`, red first in `08483019`). O2 (X3): the `DB: none` path lists hid a rename's old path; both now carry `--no-renames` (`a50ec4c8`).
- W on `a50ec4c8`: offline 3737/0 · with-DB 673 + 173 = 846/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS: none. The full pass 1 without `--db-only` is green with the wider guard: 4406 passed, nothing flagged.
- The first `--db-only` pass 1 had 1 error: a Postgres deadlock in a test this job does not touch. The file passed alone, and the whole command passed when run again (DECISION 1).
- open: 0 · house B: not needed · ready: YES · decisions: 2 · for Dejan: 0.

## L74
- The session's system attribution text asked for a `Claude-Session:` line in commits; L74 and the hub: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Acted on none.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" ".../2026-10-03/01-lock-relief-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/01-lock-relief-card.md"` | 0 | `edd07fa0d3376d63c49362dbc3725aeb04c8d5b9` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (...) APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house ... | HIS RULING · APPROVED |` |
| R47 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^| R154 " ".../cto-2026-10-02.md"` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check (L68 narrowed there only); pass 1 under the lock = with-DB tests only; lands + measured 10-03; 2nd DB waits (...) | HIS RULING · APPROVED |` |
| R154 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R154 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gates | — | — | not run: `HOUSE A: none — overruled 2026-10-02 R47` (no house gate, no probe) |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 07:40:47 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/lock-relief-1003` |
| tip | `git log --oneline -1` | 0 | `1cb963f6 docs(lock-relief): build report — 77d19438` |
| docs-only above TIP | `git log --stat --format=%h 77d19438..HEAD` | 0 | `1cb963f6` · `.../reports/lock-relief-build-2026-10-03.md | 271 +++` — docs only |
| BUILT | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: lock-relief · tip: 77d19438 | on bb816d45 | migration: none | offline 3737/0 | with-DB 845/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 7 of 7 | self-check: 3 of 3 | decisions: 6 · for Dejan: 1` |
| range | `git log --oneline bb816d45..77d19438` | 0 | `77d19438 fix(lock-relief): the offline skip mark on the 68 tests G1's guard named at the W proof run (G1, P2; L68)` · `377c83b2 feat(lock-relief): offline-skip guard, --db-only pass 1, the DB: none card (G1, P1, P2, H1, H2, H3; L3, L68, L76)` · `0dcaeb12 wip(lock-relief): red — G1, P1, P2 tests on bb816d45` (3 commits) |
| range paths | `git log --stat --format=%h bb816d45..77d19438` | 0 | 77d19438: `tests/cobalt/test_aset_web.py` 28+, `test_drc_d3_fix_r2.py` 1+, `test_drc_d4_fix_r1_runs.py` 1+, `test_drc_settings.py` 8+, `test_fill_c1_offline.py` 4+, `test_modelaccess_client.py` 2+, `test_radar_panel_cards.py` 1+, `test_s3_c3_panel_offline.py` 9+, `test_s3_c4_trade_note_offline.py` 2+, `test_settings_optional.py` 1+, `test_voice_plan.py` 1+, `test_voice_web.py` 1+ · 377c83b2: `docs/40 - DevDocs/prompts/BUILD-HUB.md` 13, `CARD.md` 1, `CHECK-HUB.md` 4, `tests/cobalt/conftest.py` 84, `tests/cobalt/test_db_only_selection.py` 59 · 0dcaeb12: `tests/cobalt/test_db_only_selection.py` 583+, `tests/ops/test_pass1_db_only.py` 60+ |
| lock: own .env | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/lock-relief-1003/.env: No such file or directory` |
| lock: any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 1 | `No such file or directory` — fresh |
| houses | — | — | house A: none (overruled 2026-10-02 R47) · house B, if needed: none available (no probe run under the overrule) |

## Files copied
none — no house (overruled 2026-10-02 R47).

## OWN FINDINGS

FINDING O1
ROW: G1 (X1)
CLAIM: `db.connect_migration` opens `psycopg.connect` through `db._open` itself (`src/cobalt/db.py:269`, `:199`), past both runtime reaches (`tests/cobalt/conftest.py:241` `fake_connect`, `:289` `_open`) and past the three static doors (`tests/cobalt/test_db_only_selection.py:211`, `:231`, `:217`); an unmarked test that calls it — directly, through a support fixture or through `cobalt db migrate` in process (`src/cobalt/db_migrations/cli.py:559`) — reaches `cobalt_dev` and neither half of G1 sees it. (A static door on the name is no fix: `tests/cobalt/test_db_credentials.py:155` calls it in an offline test against a patched `psycopg.connect`.)
RUN: TEST — `tests/cobalt/test_db_only_selection.py`:
```python
@requires_db
def test_x1_an_unmarked_migration_connection_fails_with_the_guard_message(request):
    """X1 (check): `db.connect_migration` opens psycopg itself, past
    `fake_connect` and `_open`; an unmarked test that reaches it is refused
    like any other reach, before any connection opens."""
    from cobalt import db, env

    record = request.getfixturevalue("offline_skip_guard")
    item = request.node
    item.iter_markers = lambda name=None: iter(())
    opened = None
    try:
        with pytest.raises(AssertionError) as through:
            opened = db.connect_migration(env.DEV_DB_NAME)
    finally:
        del item.iter_markers
        if opened is not None:
            opened.close()
    assert str(through.value) == GUARD_MESSAGE + item.nodeid
    assert record == [GUARD_MESSAGE + item.nodeid]
    record.clear()
```
EXPECT: with the database, on the tip: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O2
ROW: H1, H2 (X3)
CLAIM: (a0) (`docs/40 - DevDocs/prompts/BUILD-HUB.md:85`, `git diff --name-only <BASE>`) and the check's DB: none PREFLIGHT line (`docs/40 - DevDocs/prompts/CHECK-HUB.md:66`, `git diff --name-only <BASE>..<TIP>`) list a renamed file by its NEW path only (git's default rename detection), so a diff that moves `src/<file>` to `docs/<file>` prints only `docs/<file>` and passes the three-prefix test with a `src/` path gone.
RUN: COMMAND — `git diff --name-only 53a85f27^..53a85f27` (a rename on this branch's history, `R073 …/04-draft-x5-fix-card.md → …/04-draft-x5-fix.md`), against `git diff --name-only --no-renames 53a85f27^..53a85f27`.
EXPECT: the first prints ONE path, `docs/40 - DevDocs/prompts/2026-10-02/04-draft-x5-fix.md`; the second prints both, the old path included.

NO FINDING (each ask read, nothing runnable to hand over):
- X2: the only runtime `pytest.skip` that depends on the database is in a fixture (`tests/cobalt/radar_migrated_support.py:77`, `migrated_radar`), behind the `migrated_*` static door; the other runtime skips (`test_cards_picks.py:388`, `:401`, `test_env.py:90`, `test_heartbeat_runner.py:712`, `test_voice_transcribe.py:43`) do not depend on `POSTGRES_*`, so they behave the same offline and in pass 1. No plugin adds marks at collection (`grep` for `collection_modifyitems|add_marker|applymarker` over `tests` → only `tests/cobalt/conftest.py:103`). The build's counts agree: 4405 + 7 + 3 full-pass items = 672 + 7 + 2 kept + 3734 unmarked; offline 3737 passed + 1 xfailed = 3734 + 4 marked items that do not skip offline.
- X4: beyond the build's DECISION 6 (`CHECK-HUB.md:129`, answered: none holds), no sentence of either hub demands a lock, a fingerprint or a with-DB number from a `DB: none` job: `BUILD-HUB.md:42`, `:56`, `:85`, `:108`, `:115` and `CHECK-HUB.md:66`, `:112` carry the exceptions.
- X5: no reader on `main` parses those fields (`grep -rn -F "cobalt_dev:" /Users/cobalt/cobalt/ops/desk` → `gate.sh:39`, `:448` write them, `desk-launch.sh:23` a comment; DEPLOY-HUB's `with-DB` hits are its own gate, line 185 its own stop line). `gate.sh` reads (c) with `after("c")` (`ops/desk/gate.sh:139`–`:153`), matching `- (c) `, which the new label keeps.
- Observed, not a defect: under `--db-only` the runtime half of G1 runs only in a full pass 1, which after this job is the deploy gate (STEP-G), where seam (1) keeps it. A new unmarked reach that swallows its error is caught there, at deploy, not at build.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | lock take 07:47:38 EDT (`lock taken: lock-relief-1003`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → this worktree's alone); `<F0>` `664	35	272c95bbb12241e3611e4b36326ccf87`; `--proof-only` → 36 tables, 0014+ `-`, `NOTHING WAS APPLIED` → `0013`; `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_db_only_selection.py::test_x1_an_unmarked_migration_connection_fails_with_the_guard_message` | `E           Failed: DID NOT RAISE <class 'AssertionError'>` · `tests/cobalt/test_db_only_selection.py:655: Failed` · `1 failed in 0.09s` | HELD — red for its stated reason: the unmarked `connect_migration` opened |
| O2 | own | `git diff --name-only 53a85f27^..53a85f27` · `git diff --name-only --no-renames 53a85f27^..53a85f27` | first → `docs/40 - DevDocs/prompts/2026-10-02/04-draft-x5-fix.md` (one path); second → `.../04-draft-x5-fix-card.md` and `.../04-draft-x5-fix.md` | HELD — the old path of a rename is not listed |

Red commit: `08483019 wip(lock-relief): check red — O1` (the test file only). O2's red is a command on git history; it has no test file to commit.

## FIXES
| id | commit | change | green |
|---|---|---|---|
| O1 | `18f03c41 fix(lock-relief): G1 guards every psycopg.connect after the suite's own open, so db.connect_migration is a reach (check O1)` | `tests/cobalt/conftest.py`: `dev_db_tx` (with the database only) also patches `db.psycopg.connect` with a guarded wrapper; the fixture's own open runs under `_opening_the_suite_connection` and is not a reach (an inner pytester run's `dev_db_tx` opens under the outer test's wrapper). A test that patches `psycopg.connect` itself (`test_db_credentials.py:65`, `captured`) replaces the wrapper and is unaffected. | first attempt (wrapper with no exemption): `3 failed, 91 passed, 2 errors` — the two pytester tests of the build tripped on the inner `dev_db_tx` open (`conftest.py:239 in dev_db_tx … AssertionError: with-DB test without an offline skip mark: …test_a_reach_a_store_swallowed_still_fails_the_test_at_teardown`), and `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` (`assert 28 == 36`; a pass-1 deselect, it needs 0014+, not run by any gate at 0013 — my run of the whole file, not a defect). With the exemption, same take: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_db_only_selection.py tests/cobalt/test_db_credentials.py` → `33 passed, 12 warnings in 1.90s`. `<F>` after = `664	35	272c95bbb12241e3611e4b36326ccf87` = `<F0>`; released 07:50:01 EDT `lock released`; `.env` → `No such file or directory`. |
| O2 | `a50ec4c8 fix(lock-relief): the DB: none path lists carry --no-renames, so a rename shows its old path (check O2)` | `BUILD-HUB.md` (a0) `git diff --name-only --no-renames <BASE>`; `CHECK-HUB.md` PREFLIGHT THE LOCK `git diff --name-only --no-renames <BASE>..<TIP>`. `git diff *` is on both lines; no new string. | `git diff --name-only --no-renames 53a85f27^..53a85f27` → both paths (above) |

No DevDocs module line: `tests/cobalt/conftest.py` has no page under `docs/40 - DevDocs/cobalt/` (`Glob docs/40 - DevDocs/cobalt/*test*` → none; the build wrote none either).

## Suites
W on `<tip now>` = `a50ec4c8` (main's `BUILD-HUB.md` `## W`, with (c) the command row P2 wrote, as the card's TREE STATE says).
- RESTARTS: `uv run cobalt jobs restarts bb816d45..HEAD` → every path `DOCS` or `test/documentation; no resident	-` (the build's 19 rows, `tests/cobalt/conftest.py` and `tests/cobalt/test_db_only_selection.py` among them) → `RESTARTS: none`.
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 587.79s (0:09:47)` → `<p>` = 3737 (the build's 744 skips + the new X1 test, which skips offline). Test this check adds: `tests/cobalt/test_db_only_selection.py::test_x1_an_unmarked_migration_connection_fails_with_the_guard_message` (with-DB).
- (e) LIVE-NOTE (`ls <WT>/.env` → `No such file or directory`) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.36s` → `<l>` = 146; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (none names `COBALT_LIVE_VAULT_ROOT`).
- (b) take 08:01:22 EDT `lock taken: lock-relief-1003`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  3 08:01 /Users/cobalt/cobalt-wt/lock-relief-1003/.env` alone. `<F0>` = `664	35	272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → 36 tables, the 0014+ tables `-`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `code: a50ec4c8 (clean)` → `0013`.
- THE PROOF for O1's wider guard (as row P2's proof, before (c)): `main`'s pass-1 command byte for byte, no `--db-only` (`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip … --deselect tests/cobalt/test_x5_tap_refresh_db.py`, the 15 deselects of `main`'s line) → `4406 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 702.52s (0:11:42)`. Nothing failed and nothing errored, so the guarded `psycopg.connect` flags no test (the build's PROOF: 4405 passed; +1 is the X1 test). The 7 SKIPPED: `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`; `test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`; `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`; `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`; `test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`; `test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c) PASS 1, the command row P2 wrote (`BUILD-HUB.md:89` on this branch), executed WHOLE with no deselect added (the X1 test needs no migration above 0013): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py`
  - run 1 → `672 passed, 7 skipped, 3801 deselected, 2 xfailed, 11 warnings, 1 error in 110.70s (0:01:50)`. The error: `ERROR at setup of test_run4_the_real_cards_read_inside_get_drc_writes_nothing` (`tests/cobalt/test_drc_d2_fix_r1_runs.py`). Its `migrated` fixture (`tests/cobalt/test_drc_store.py:237` `_apply(conn, FORWARD)`), while applying `0002_move_tables.sql`, raised `psycopg.errors.DeadlockDetected: deadlock detected` · `Process 1776692 waits for AccessExclusiveLock on relation 165692 of database 165601; blocked by process 1776678.` · `Process 1776678 waits for ShareLock on transaction 3410367; blocked by process 1776692.` · `CONTEXT:  SQL statement "ALTER TABLE "user".vault_writes OWNER TO cobalt_user"`. The guard is not involved (it adds a Python check and opens nothing), and the file is not in this job's diff. The same test passed in the PROOF above, on the same tree. → DECISION 1.
  - the file alone, same take: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_drc_d2_fix_r1_runs.py` → `4 passed, 2 xfailed, 6 warnings in 1.33s`.
  - run 2, the same command whole → `673 passed, 7 skipped, 3801 deselected, 2 xfailed, 12 warnings in 109.92s (0:01:49)` → `<d1>` = 673; nothing failed, nothing errored. The 7 SKIPPED are the same 7 as the PROOF.
- THE COUNTS: `--db-only` passed 673 + offline passed 3737 = 4410 ≥ full pass-1 passed 4406 → no shortfall. Seconds: full pass 1 702.52 s → `--db-only` 109.92 s.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001` … `0013`, `0014_radar_handicap.sql` … `0022_prediction_records.sql` applied in order; every pre-existing table `OK`, the nine 0014+ tables `CREATED`, `content UNCHANGED on every table`, no `CHANGED`. **dev forward: APPLIED 08:19:07 EDT.** `<F1>` = `893	44	126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, `BUILD-HUB.md` W (c3) byte for byte (nothing deselected for this check) → `173 passed, 1 deselected, 5 warnings in 219.12s (0:03:39)` → `<d2>` = 173; `<d>` = 673 + 173 = 846. (Its `ERROR` lines are the app's loguru output of refusals the tests provoke, such as `REFUSED (cards.transition.FILLED): … inside MARKET RESET`, not test errors.)
- (c3r) not run: the X1 test writes no row and no ticker (the guard refuses before any connection opens).
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` `.rollback.sql`, newest first; the nine tables `DROPPED`, every other `OK`, `content UNCHANGED on every table`. `<F2>` = `664	35	272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **cobalt_dev: 0013 — F2 = F0.** Release 08:23:35 EDT `lock released`; `ls /Users/cobalt/cobalt-wt/lock-relief-1003/.env` → `No such file or directory`. `.env: removed, proven gone (W)`.
- (c4) not run: no migration added.
- `tests/ops/test_pass1_db_only.py` after O2's hub edit: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_pass1_db_only.py` → `3 passed, 15 warnings in 0.99s`.
- Beside the card's baseline (check `17`: offline 595.72 s / pass 1 709.60 s / pass 2 220.14 s): this check's offline 587.79 s / pass 1 109.92 s / pass 2 219.12 s.

## Scope
- The build's paths (PREFLIGHT): `docs/40 - DevDocs/prompts/BUILD-HUB.md` (P2, H1), `CHECK-HUB.md` (H2), `CARD.md` (H3), `tests/cobalt/conftest.py` and `tests/cobalt/test_db_only_selection.py` (G1, P1), `tests/ops/test_pass1_db_only.py` (P2), and the mark line of 12 `tests/cobalt/` files G1's guard named (G1's files). Each is in a row's `files`. The 12 files gained decorator lines only (`git diff -U0 377c83b2 77d19438 -- tests/cobalt/test_aset_web.py tests/cobalt/test_drc_settings.py tests/cobalt/test_s3_c3_panel_offline.py` → only `+@pytest.mark.skipif(... reason="reaches cobalt_dev (lock-relief G1)")` lines).
- My commits: `tests/cobalt/test_db_only_selection.py`, `tests/cobalt/conftest.py` (G1's files), and `BUILD-HUB.md` / `CHECK-HUB.md` (H1's and H2's files). None is outside the rows.
- No path reaches a score, rank, grade or size: the job changes test fixtures and hub text only, and `src/` is untouched ((iii) below).

## Checked against the branch
- (i) `git log --oneline 77d19438..HEAD -- . ":(exclude)docs"` → `18f03c41 fix(lock-relief): G1 guards every psycopg.connect after the suite's own open, so db.connect_migration is a reach (check O1)` · `08483019 wip(lock-relief): check red — O1`. `<tip now>` = `a50ec4c8`, the tree W ran on. The newest non-docs commit is `18f03c41`; `a50ec4c8` above it is O2's fix to two hub files that are rows' `files` (H1, H2), so the branch is to be taken at `a50ec4c8` (a record below).
- (ii) `git log --stat --format=%h 77d19438..HEAD` → `a50ec4c8` `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `CHECK-HUB.md` · `18f03c41` `tests/cobalt/conftest.py` · `08483019` `tests/cobalt/test_db_only_selection.py` · `1cb963f6` the build report. Every non-docs path is a row's file or a test file: no WIDENED.
- (iii) `git log --oneline bb816d45..HEAD -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md" ops/desk src` → (nothing). No commit touches `env.py`, the lock scripts or the pass-2 command (`git log --stat` above).
- (iv) `grep -n -F "def test_x1_an_unmarked_migration_connection_fails_with_the_guard_message" tests/cobalt/test_db_only_selection.py` → `644:def test_x1_an_unmarked_migration_connection_fails_with_the_guard_message(request):` (one line); `08483019` (check red) sits below `18f03c41` (fix) in (i). O2 has no test (a command on git history); its fix is `a50ec4c8`.
- (v) `ls /Users/cobalt/cobalt-wt/lock-relief-1003/.env` → `No such file or directory`; `git status --short --branch` → `## ops/lock-relief-1003`.
- (vi) TREE STATE `row P2`: `git log --stat --format=%h bb816d45..HEAD -- src/cobalt/db_migrations tests/cobalt` → no migration file. The with-DB tests added sit in `tests/cobalt/test_db_only_selection.py`, which pass 1 collects (`--db-only` keeps them). `git log --oneline bb816d45..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `a50ec4c8 …`, `377c83b2 …` (NON-EMPTY). The pass-1 command W executed at (c) is the line row P2 wrote (`BUILD-HUB.md:89`); pass 2 is the unchanged (c3) line. DEPLOY-HUB's pass 1 has no `--db-only`, by seam (1).
- (vii) The card's records naming a command: `grep -rn -E "POSTGRES_HOST" tests/taxonomy` → (nothing), so `tests/taxonomy` carries no Postgres skip, as recorded. `grep -rl -F "POSTGRES_HOST" tests/cobalt` → the `.py` list in this session's output, which includes `__pycache__` hits, so I did not recount it against the record's 57.
- (viii) L32: this report holds constructed values and tool output only. The tickers and dates quoted are the test fixtures' constructed ones, inside quoted output.

COUNTS: findings 2 (O1, O2; no house) · dropped 0 · held 2 · fixed 2 · held unfixed 0 · open 0.

## OPEN
none.
- OUT OF SCOPE (the card's `## RECORDS`, decisions 1–6 answered): `CHECK-HUB.md:129`'s stop-line shape for a `DB: none` check (build DECISION 6); `tests/ops/test_order_open.py` red on BASE (card 01b's); `db.connect_migration` as a static door (build DECISION 4; now covered at run time by O1).

## CONTINUE
next: none — the check is closed; the desk verifies the artifact.

## DECISIONS
1. A pass-1 red that comes and goes, outside this job's rows: `tests/cobalt/test_drc_d2_fix_r1_runs.py::test_run4_the_real_cards_read_inside_get_drc_writes_nothing` errored once at setup with `psycopg.errors.DeadlockDetected` (`ALTER TABLE "user".vault_writes OWNER TO cobalt_user` inside its `migrated` fixture's FORWARD, against a second backend of the same run; `## Suites` (c) run 1). It passed in the full pass 1, alone, and in (c) run 2, all on the same tree. Under `--db-only` the with-DB tests now run back to back, so a gate may catch this race more often. It can fail any build or deploy gate at random. Safe default taken: not fixed and not marked (the file is not in this job's diff; the fence forbids changing what an existing test asserts); (c) was run again whole, and that green run is the one counted. The desk may card the race (the fixture's migration connection against the suite's open transaction).
2. O2's fix changes the card's literal text in two sentences (H1 (2), H2 (1)): `git diff --name-only <BASE>` and `git diff --name-only <BASE>..<TIP>` now read `git diff --name-only --no-renames …`. The allow string (`git diff *`) is unchanged, and so is every other word. If the desk wants the card's text byte for byte, reverting `a50ec4c8` undoes it, and the rename gap stays open (`## RUNS` O2). Safe default taken: committed, as a held finding inside the rows' files.

## RECORDS
- Files opened (14): `CHECK-HUB.md` (main); the card; the build report (sections `## E2 RED` to the last line, as `## RUNS` cites); `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `tests/cobalt/conftest.py`; `tests/cobalt/test_db_only_selection.py`; `tests/cobalt/radar_migrated_support.py`; `tests/cobalt/stale_db_support.py`; `tests/cobalt/test_db_credentials.py` (lines 130–169); `src/cobalt/db.py` (lines 180–289); the branch's `BUILD-HUB.md` (lines 70–117); the branch's `CHECK-HUB.md` (line 66); `ops/desk/gate.sh` (lines 120–179); the saved `git diff bb816d45..77d19438 -- tests/cobalt/conftest.py tests/ops docs` output. `main`'s `BUILD-HUB.md` `## THE LOCK`, `## E2`, `## RESTARTS`, `## W` were read through that diff and the branch file: the two differ only in the lines the diff shows. Not opened: `tests/cobalt/test_radar_panel.py`, `test_session.py`, `reports/devdb-parallel-answer-2026-10-02.md` (card `## READ`); my findings did not need them.
- Lock takes: 2. ONE for O1's with-DB red and its green (07:47:38 → 07:50:01 EDT, `<F>` = `664	35	272c95bbb12241e3611e4b36326ccf87` before and after, no forward), and W's (08:01:22 → 08:23:35 EDT). The first take is the extra one. `.env` was proven gone after each.
- Inside W's take, (c) ran twice (DECISION 1) and the full pass-1 PROOF ran once before (c). Neither changes the schema; both ran at `0013` before (c2).
- `cobalt_redactions` 246 → 249 across this check's pass-1 runs (`--proof-only` at 07:47 and 08:01 → 246; FORWARD at 08:19 → 249). This is the leak the build's DECISION 3 names (answered). Nothing deleted.
- `<tip now>` `a50ec4c8` is a docs-path commit above the newest non-docs commit `18f03c41`; it holds O2's fix to rows' files and is the tree W ran on, so the stop line names it.
- Not run: `## 1` and `## 3` (house A none, overruled 2026-10-02 R47); no house gate, no probe, nothing staged under `<S>` but `opus-1.md`.
- No REFUSED call, no CONTINUE message, no L74 block in a tool result.
- Check of `lock-relief`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: lock-relief · pass: 1 · tip: a50ec4c8 · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB 846/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0
