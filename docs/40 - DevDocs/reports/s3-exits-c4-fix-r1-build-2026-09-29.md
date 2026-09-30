# S3 EXITS C4 FIX R1 BUILD — 2026-09-29

Prompt: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-29/24-s3-exits-c4-fix-r1-build.md` · seat `s3-exits-c4-fix-r1-build` · Opus 5.5 · relaunch `CONTINUE: PREFLIGHT` (R109) · started 17:09:50 EDT (`date`). The first run's report (`3e2f557b`, FAILED PREFLIGHT on the dev-vault dialog) is replaced by this file; its record stays in git.

## §0 Headline
- **F1 BUILT** at `01d0fbb9`, tests and DevDocs only. The autouse guard `trade_note_path_guard` fails any test that resolves a trade-note path outside `tmp_path`. `panel_world` builds the `tmp_path` vault once and `note_world` reuses it. Red at E2: the 14 panel tests that post a fill failed on the dev-vault path.
- **Three suites green on `01d0fbb9`:** offline 3320/0 · with-DB 3728 + 107 = 3835/0 · live-note 146/0. `cobalt_dev` back at `0013` (F2 = F0), `.env` removed, RESTARTS: none.
- **U1 run:** `/fill` with `NaN` or `-1` → 200, no row written, card stays TRIGGERED. No ESCALATE.
- **U2 run:** his `exit_price: 5.10` becomes `exit_price: "5.1"` after a later write → ESCALATE U2 for round 2.
- Two lock takes. No command ran on the dev vault. No file under `src/` changed.

## L74
A system block attached to this session's context asks for a `Claude-Session: https://claude.ai/code/session_…` line in every commit message and PR body and names a file-send tool. Recorded once here (L74); not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`<D>` = `2026-09-29` (`date` → `Tue Sep 29 17:09:50 EDT 2026`).
| gate | command | result |
|---|---|---|
| placeholder `R__` | `grep -n -E "R_[_]" "…/prompts/2026-09-29/24-s3-exits-c4-fix-r1-build.md"` | no output — PASS |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" "…/24-s3-exits-c4-fix-r1-build.md"` | one hit, `42:` = this gate's own line — PASS |
| classification | `grep -n -F "S3 EXITS C4 FIX R1 DRAFTED" "…/reports/s3-exits-c4-fix-r1-draft-2026-09-29.md"` | `69:S3 EXITS C4 FIX R1 DRAFTED · FIX: 2 · NOT REAL: 12 · UNPROVEN: 2 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 7` — last non-blank line, `OWNER ITEM: 0` — PASS |
| launch row | `grep -n -F "24-s3-exits-c4-fix-r1-build.md" "…/reports/cto-2026-09-29.md"` | `109:` R101 (the draft launch), `113:` R105 (`<base>` = `cfd9f091`, `no with-DB run in flight`), **`117:| R109 | 17:09 ET | — RELAUNCH ROW (R105, R108, L60; …): … \`<base>\` = \`3e2f557b\` … prefix \`CONTINUE: PREFLIGHT\`; no \`.env\` in any worktree, no with-DB run in flight. DESK DEV-VAULT LISTING 17:09: …`**, `123:` the session row — R109 carries `<base>` `3e2f557b` and the literal — PASS |
| row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"24-s3-exits-c4-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-29.md"` | `bbfd688b203be404f4c5ff353cc4e7f567669e02` — NON-EMPTY, PASS |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 29 17:09:50 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## s3/exits-c4` |
| base | `git log --oneline -1` | 0 | `3e2f557b docs(s3-c4): S3 exits C4 fix r1 build report — FAILED PREFLIGHT (dev-vault listing outside --add-dir)` = `<base>` |
| no code past `<code base>` | `git -C /Users/cobalt/cobalt log --oneline d05ae72d..s3/exits-c4 -- src tests configs` | 0 | empty |
| no `.env` here | `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/s3-exits-c4/.env: No such file or directory` |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| `panel_world` | `grep -n "def panel_world" tests/cobalt/test_s3_c3_panel_db.py` | 0 | `44:def panel_world(world, monkeypatch):  # noqa: F811` |
| `note_world` | `grep -n "def note_world" tests/cobalt/test_s3_c4_trade_note_db.py` | 0 | `41:def note_world(panel_world, monkeypatch, tmp_path):  # noqa: F811` |
| `make_vault` | `grep -n "def make_vault" tests/cobalt/trade_note_support.py` | 0 | `65:def make_vault(monkeypatch, tmp_path: Path) -> Path:` |
| `dev_env` | `grep -n "def dev_env" tests/cobalt/conftest.py` | 0 | `67:def dev_env(monkeypatch):` |
| `resolve_target` uses | `grep -n "resolve_target" src/cobalt/prefill/trade_note.py` | 0 | `51:from .vault_writer import VaultWriteError, read_if_exists, resolve_target` · `256:    path = resolve_target(prefill_paths.trades_dir, filename)` · `422:    path = resolve_target(str(rel.parent), rel.name)` |
| `resolve_target` def | `grep -n "def resolve_target" src/cobalt/prefill/vault_writer.py` | 0 | `26:def resolve_target(vault_relative_dir: str, filename: str) -> Path:` |
| dev vault (the desk's listing, R109; no command run by me) | — | — | `-rw------- 767 Sep 29 09:35 …/2 - Trades/Trade-2026-09-03 10-00-00 -TEST.md` · `-rw------- 665 Sep 29 09:35 …/2 - Trades/Trade-2026-09-03 10-00-00 -ZZPB.md` (DESK DEV-VAULT LISTING 17:09) |
| restarts, empty range | `uv run cobalt jobs restarts 3e2f557b..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |

## E0 BASELINE
On `<base>` `3e2f557b` (src = `d05ae72d`), no `.env`, no test file written while the offline run was in flight.
- offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, from 17:10) → **`3318 passed, 478 skipped, 1 xfailed, 20 warnings in 558.60s (0:09:18)`**, exit 0 (= EXPECTED `3318 passed`, 0 failed).
- live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 27.38s`** (= EXPECTED). The one skip: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — none names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Written (tests only, `panel_world` / `note_world` unchanged):
- `tests/cobalt/conftest.py` — autouse `trade_note_path_guard(monkeypatch, tmp_path_factory)`: wraps `cobalt.prefill.trade_note.resolve_target`; the original resolves, then a path not inside `tmp_path_factory.getbasetemp()` is recorded and `AssertionError("L28: a trade-note path resolved outside tmp_path in a test: <path>. Nothing read or written — point the test at a tmp_path vault (trade_note_support.make_vault).")` is raised before any read or write; teardown → `pytest.fail` with the same text per recorded path. Yields the record.
- `test_s3_c3_panel_db.py::test_a_panel_fill_writes_its_note_in_the_tmp_path_vault` (with-DB).
- `test_s3_c4_trade_note_offline.py::test_a_trade_note_path_outside_tmp_path_fails_loud` (offline) and `::test_run_u2_a_typed_exit_price_after_a_later_write` (RUN U2).
- `test_s3_c4_trade_note_db.py::test_run_u1_a_nan_or_negative_price_posted_to_the_manual_fill` (RUN U1).

**RUN U2** (offline, on `d05ae72d` src): `uv run pytest -q -rP -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_trade_note_offline.py -k test_run_u2` → WHOLE:
```
.                                                                        [100%]
==================================== PASSES ====================================
______________ test_run_u2_a_typed_exit_price_after_a_later_write ______________
----------------------------- Captured stdout call -----------------------------

RUN U2 · close write updated (one confirmed exit leg @ 5.6000)
U2 exit_price before: 'exit_price: 5.10'
U2 exit_price after:  'exit_price: "5.1"'
U2 entry_time after:  'entry_time: "2026-09-03 10:00"'
U2 exit_time after:   'exit_time: "2026-09-03 10:31"'
1 passed, 16 deselected in 0.10s
```
The line changed → `ESCALATE U2` (under `## ESCALATE`). Not fixed here.

**Offline** (background, 17:20 → 17:29, no `.env`): `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → **`3320 passed, 480 skipped, 1 xfailed, 20 warnings in 556.66s (0:09:16)`**, exit 0 = E0's 3318 + the 2 new offline tests (the guard test PASSED, U2 ran); skipped = 478 + the 2 new with-DB tests. `grep -c "outside tmp_path"` on the output → `0`: **no offline test trips the guard** (offline, the fill routes fail at `card_for_note` before the resolver). Nothing joins F1's fixture list from offline.

**With-DB — LOCK TAKE 1** (on `d05ae72d` src + the red tests):
- Lock (a): `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`.
- Lock (b): `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 29 17:30 /Users/cobalt/cobalt-wt/s3-exits-c4/.env`. **L76 lock taken 17:30** (`date` 17:30:10). Every `COBALT_ENV=dev` call was directly preceded by `ls -la /Users/cobalt/cobalt-wt/s3-exits-c4/.env` (LISTED).
- `<FP>` (the query under `## W THE THREE SUITES`) → `664	35	272c95bbb12241e3611e4b36326ccf87` → **F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** (= C4's F0).
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `legs user - - -`, `voice_turns user - - -` → **`0013`**; `aset_sizings 1 0824685c…`, `card_stop_edits 1`, `card_transitions 4 f181e76b…`, `cobalt_redactions 198 a092c46e…` (system, outside this build), `vault_overrides 6`, `vault_writes 187 2c8181e1…`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `code: 3e2f557b (DIRTY: 5 path(s))`. No forward.
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py` → exit 1, progress `...E.E...E.E.E.E.E.E.E..E.E.E.E.EFE....................`; the tool output was truncated past 30 k characters, so the same three files ran again for the summary: `COBALT_ENV=dev uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=no --show-capture=no <same three files>` → **`1 failed, 39 passed, 15 errors in 8.82s`**:
```
(line 1, quoted: `FAILED tests/cobalt/test_s3_c3_panel_db.py::test_a_panel_fill_writes_its_note_in_the_tmp_path_vault`)
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_fill_from_the_untouched_prefill_is_an_estimated_last_poll_entry_leg
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_fill_with_an_edited_price_is_a_typed_confirmed_entry_leg
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_half_from_the_rendered_page_then_the_same_half_again_is_refused
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_an_untouched_flat_is_estimated_closes_the_card_and_is_listed_for_correction
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_flat_with_the_check_and_a_typed_price_is_confirmed_and_closes
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_holding_50_is_the_entry_correction_and_running_is_50
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_correction_of_an_estimated_leg_is_confirmed
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_stop_edit_shows_yours_and_the_delta_and_the_reset_gives_it_back
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_p_missing_renders_the_re_read_stop_line
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_market_reset_refuses_every_post_and_writes_nothing
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_get_radar_and_the_in_trade_render_write_nothing
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_correction_posted_on_one_card_never_writes_another_cards_leg
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_sheet_flat_without_the_check_closes_and_is_listed_for_correction
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_run_r1_a_nan_or_negative_price_posted_to_the_taps
ERROR tests/cobalt/test_s3_c3_panel_db.py::test_a_panel_fill_writes_its_note_in_the_tmp_path_vault
```
  - Every ERROR is the guard at teardown, all in `test_s3_c3_panel_db.py` (the 14 tests that post `/radar/card/<id>/fill` or `/fill`, plus the new F1 test). The first path (the first run, `--tb=line`): `ERROR at teardown of test_a_fill_from_the_untouched_prefill_is_an_estimated_last_poll_entry_leg` → `E   Failed: L28: a trade-note path resolved outside tmp_path in a test: /Users/cobalt/dev-vault-cobalt/1 - Trading/2 - Trades/Trade-2026-09-03 10-00-00 -ZZPB.md. Nothing read or written — point the test at a tmp_path vault (trade_note_support.make_vault).`; the captured stderr shows the web helper swallowing it: `cobalt.aset.web:_fill_note:1552 - card 13076: trade note NOT written after the fill: L28: …` — the fixture's teardown is what makes it loud. The manual `/fill` test names the `-TEST.md` path: `ERROR at teardown of test_a_sheet_flat_without_the_check_closes_and_is_listed_for_correction` → `… /Users/cobalt/dev-vault-cobalt/1 - Trading/2 - Trades/Trade-2026-09-03 10-00-00 -TEST.md …` (from a third, `-k`-narrowed run of three ids with `--tb=line`: `1 failed, 2 passed, 18 deselected, 3 errors in 1.28s`).
  - The new F1 with-DB test FAILS: `tests/cobalt/test_s3_c3_panel_db.py:509: KeyError: 'vault'` (and errors at teardown on the ZZPB path).
  - Every `test_s3_c4_trade_note_db.py` test PASSED (its `note_world` patches the vault first), `test_prefill_trade_note.py` PASSED. No red for any other reason.
- **RUN U1**: `COBALT_ENV=dev uv run pytest -q -rP -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_trade_note_db.py -k test_run_u1` → WHOLE:
```
.                                                                        [100%]
==================================== PASSES ====================================
________ test_run_u1_a_nan_or_negative_price_posted_to_the_manual_fill _________
----------------------------- Captured stdout call -----------------------------

RUN U1 · POST /fill on a fresh manual card per input
U1 /fill card 13160 actual_fill='NaN' → 200 · body[:200]='<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Cobalt · ASET Sheet</title>\n<style>\n body{font-family:system-ui'
U1   counts before {'aset_sizings': 2, 'legs': 0, 'card_transitions': 7, 'card_stop_edits': 1, 'picks': 0} · after {'aset_sizings': 2, 'legs': 0, 'card_transitions': 7, 'card_stop_edits': 1, 'picks': 0} · legs 0 → 0
U1   card row: state='TRIGGERED' actual_fill=None trade_note_path=None
U1 /fill card 13161 actual_fill='-1' → 200 · body[:200]='<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Cobalt · ASET Sheet</title>\n<style>\n body{font-family:system-ui'
U1   counts before {'aset_sizings': 3, 'legs': 0, 'card_transitions': 10, 'card_stop_edits': 1, 'picks': 0} · after {'aset_sizings': 3, 'legs': 0, 'card_transitions': 10, 'card_stop_edits': 1, 'picks': 0} · legs 0 → 0
U1   card row: state='TRIGGERED' actual_fill=None trade_note_path=None
1 passed, 15 deselected in 0.55s
```
  No 500 and no row written for either input (counts unchanged, the card stays TRIGGERED, `actual_fill` NULL) → **no `ESCALATE U1` line**. Recorded for the round-2 classifier: both inputs return 200 with the sheet page (the refusal text, if any, is past the first 200 characters, not printed).
- `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` = F0 (unchanged). Nothing left behind: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN ('TEST', 'ZZPB') GROUP BY ticker"` → `ticker	count` (no rows).
- Lock (d): `rm /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` → `ls: /Users/cobalt/cobalt-wt/s3-exits-c4/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` → **`.env: removed, proven gone (E2) — L76 lock released 17:31:16`** (held 17:30:10 → 17:31:16). No migration applied.

Red committed **`b493c09c`** `wip(s3-c4-fix-r1): red` (conftest, the three test files, this report).

## E3 THE ROW
Fix commit **`01d0fbb9`** `fix(s3-c4): fix r1 — every trade-note test write in a tmp_path vault; a test that resolves one outside fails loud (L28, L75)` (3 files, 12 insertions, 3 deletions). No file under `src/`.
| row | built | where |
|---|---|---|
| **F1 (a)** the guard | autouse `trade_note_path_guard` (committed with the red, `b493c09c`) | `tests/cobalt/conftest.py` (end of file) |
| **F1 (b)** the fixtures | `panel_world(world, monkeypatch, tmp_path)` calls `make_vault(monkeypatch, tmp_path)` once → `world["vault"]`; `note_world(panel_world, monkeypatch)` no longer calls `make_vault` (reuses `panel_world["vault"]`; `make_vault` stays imported for `test_x3_human_wins_once_on_the_real_store`, which has its own `tmp_path`) | `tests/cobalt/test_s3_c3_panel_db.py:44`, `tests/cobalt/test_s3_c4_trade_note_db.py:41` |
| DevDocs | `## 2026-09-29 — S3 exits C4 fix r1` (the guard and where it lives) | `docs/40 - DevDocs/cobalt/prefill/trade_note.md` |
- Tripped fixtures beyond `panel_world`: none (E2 named no offline trip; every with-DB trip was a `panel_world` test). `grep -rln "panel_world" tests/cobalt` → only `test_s3_c3_panel_db.py`, `test_s3_c4_trade_note_db.py`.
- Offline re-run: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_trade_note_offline.py tests/cobalt/test_s3_c3_panel_offline.py` → **`59 passed in 1.10s`**, 0 failed.
- The with-DB green is W's (c) / (c3).

## W THE THREE SUITES
`<tip>` = `01d0fbb9`. `<FP>` = the fingerprint query EXACTLY as the C4 report `## W THE THREE SUITES` quotes it:
```
COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"
```

- **(a) offline** (background, 17:32 → 17:41, no `.env`): `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → **`3320 passed, 480 skipped, 1 xfailed, 20 warnings in 554.51s (0:09:14)`**, exit 0, 0 failed, 0 errors → **`<p>` = 3320**.
- **(b) LOCK TAKE 2:**
  - Lock (a): `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`.
  - Lock (b): `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 29 17:41 /Users/cobalt/cobalt-wt/s3-exits-c4/.env`. **L76 lock taken 17:41:48** (`date`). Every `COBALT_ENV=dev` call was preceded by the listed `ls -la /Users/cobalt/cobalt-wt/s3-exits-c4/.env`.
  - `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` → **F0**.
  - `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → WHOLE table as at E2 (`legs user - - -`, `voice_turns user - - -`; `aset_sizings 1 0824685c130da3c7cb7f0e76191a6819`, `card_stop_edits 1 7599f9ab…`, `card_transitions 4 f181e76b…`, `cobalt_redactions 198 a092c46e…`, `day_modes 2`, `session_blocks 6`, `traders 1`, `vault_overrides 6 6a8b0520…`, `vault_writes 187 2c8181e1…`, every other table 0 rows or unchanged; `bars 1043443 2769919a…`), `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `code: 01d0fbb9 (DIRTY: 1 path(s))` (this report) → **`0013`**.
- **(c) PASS 1 at `0013`** (background, 17:42 → 17:53) — the C4 report `## RELAUNCH` (c) command BYTE FOR BYTE (fourteen `--deselect`, no C4 deselect):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk
```
  → **`3728 passed, 7 skipped, 65 deselected, 1 xfailed, 20 warnings in 660.67s (0:11:00)`**, exit 0 → **`<d1>` = 3728** (C4's 3724 + the 4 new tests). `grep -c "outside tmp_path"` on the output → `0` (no guard text). The 7 skips are C4's.
- **(c2) FORWARD:** `COBALT_ENV=dev uv run cobalt db migrate` (foreground). Output: `-- applying` lines for `0001_schemas.sql` … `0013_tunables_slug_nullable.sql`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0017_voice_turns.sql`, `0021_legs.sql`, in that order. `legs … - -> user … CREATED` and `voice_turns … CREATED`; every other table `OK`; `content UNCHANGED on every table.`; no `CHANGED`; `code: 01d0fbb9 (DIRTY: 1 path(s))`. **`dev forward: APPLIED 17:53`** (`date` right after → `17:53:39`). `<FP>` → `773	38	126f2d6983fa59f9d0eaaff7da7dd29c` → **F1** (= C4's F1).
- **(c3) PASS 2 at `0021`** (foreground) — the C4 report `## RELAUNCH` (c3) command BYTE FOR BYTE:
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py
```
  → **`107 passed, 5 warnings in 147.58s (0:02:27)`**, exit 0 → **`<d2>` = 107** (C4's 105 + F1's with-DB test + U1). The `-rA` line: `PASSED tests/cobalt/test_s3_c3_panel_db.py::test_a_panel_fill_writes_its_note_in_the_tmp_path_vault`. `grep -c "outside tmp_path"` → `0`. The three `FAILED` strings in the output are captured log/print text, not results: `cobalt.aset.web:radar:885 - radar panel FAILED: FAILED: radar pool 'primary' is missing` (×2) and `R2 GET /radar → 200 · page carries FAILED: True`. These are C3's RUN R2 prints. **`<d>` = 3728 + 107 = 3835.**
- **(c3r) nothing left behind:** `ls -la /Users/cobalt/cobalt-wt/s3-exits-c4/.env` (listed), then `COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN ('X7CT', 'X21LK', 'X1RF', 'TEST', 'ZZPB') GROUP BY ticker"` → `ticker	count` (no rows).
- **(f) ROLLBACK:** `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0021_legs.rollback.sql`, `0017_voice_turns.rollback.sql`, `0015_shadow_agreement_stale.rollback.sql`, `0014_radar_handicap.rollback.sql`, in that order. `legs … DROPPED`, `voice_turns … DROPPED`; every other table `OK`; `content UNCHANGED on every table.` `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` → **F2 = F0 field for field → `cobalt_dev: 0013 — F2 = F0`**.
- Lock (d): `rm /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` → `ls: /Users/cobalt/cobalt-wt/s3-exits-c4/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` → **`.env: removed, proven gone (W) — L76 lock released 17:56:57`**. Held 17:41:48 → 17:56:57; `0021` was applied from 17:53 and rolled back before 17:56:57.
- **(e) live-note** (no `.env`): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 25.54s`**. The one skip is `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC … not set`; none names `COBALT_LIVE_VAULT_ROOT` → **`<l>` = 146**.
- X22 not repeated (no migration). No guard trip at W → no second fix commit, no third lock take.

## RESTARTS
`uv run cobalt jobs restarts 3e2f557b..01d0fbb9`, exit 0 — the table WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/prefill/trade_note.md	M	DOCS	-
docs/40 - DevDocs/reports/s3-exits-c4-fix-r1-build-2026-09-29.md	M	DOCS	-
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_db.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c4_trade_note_db.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c4_trade_note_offline.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row (= EXPECTED).

## FOR THE CHECK
- Range **`3e2f557b..01d0fbb9`** (`git log --oneline 3e2f557b..HEAD`):
  - `b493c09c` `wip(s3-c4-fix-r1): red`
  - `01d0fbb9` `fix(s3-c4): fix r1 — every trade-note test write in a tmp_path vault; a test that resolves one outside fails loud (L28, L75)`
  - then this report's commit.
- F1 reds (on `d05ae72d` src, the `b493c09c` tests, lock take 1), quoted under `## E2 RED`:
  - 14 `test_s3_c3_panel_db.py` tests ERROR at teardown with the guard's text. The radar fill names `/Users/cobalt/dev-vault-cobalt/1 - Trading/2 - Trades/Trade-2026-09-03 10-00-00 -ZZPB.md`; the manual `/fill` names `…-TEST.md`.
  - The new with-DB test FAILED: `KeyError: 'vault'`.
- F1 greens:
  - pass 2 `PASSED tests/cobalt/test_s3_c3_panel_db.py::test_a_panel_fill_writes_its_note_in_the_tmp_path_vault`;
  - the offline guard test PASSED from E2 on;
  - no guard text in pass 1, pass 2 or offline.
- Every test the guard tripped, by id (all in `tests/cobalt/test_s3_c3_panel_db.py`, all fixed by `panel_world`):
  - `test_a_fill_from_the_untouched_prefill_is_an_estimated_last_poll_entry_leg`
  - `test_a_fill_with_an_edited_price_is_a_typed_confirmed_entry_leg`
  - `test_a_half_from_the_rendered_page_then_the_same_half_again_is_refused`
  - `test_an_untouched_flat_is_estimated_closes_the_card_and_is_listed_for_correction`
  - `test_a_flat_with_the_check_and_a_typed_price_is_confirmed_and_closes`
  - `test_holding_50_is_the_entry_correction_and_running_is_50`
  - `test_a_correction_of_an_estimated_leg_is_confirmed`
  - `test_a_stop_edit_shows_yours_and_the_delta_and_the_reset_gives_it_back`
  - `test_p_missing_renders_the_re_read_stop_line`
  - `test_market_reset_refuses_every_post_and_writes_nothing`
  - `test_get_radar_and_the_in_trade_render_write_nothing`
  - `test_a_correction_posted_on_one_card_never_writes_another_cards_leg`
  - `test_a_sheet_flat_without_the_check_closes_and_is_listed_for_correction`
  - `test_run_r1_a_nan_or_negative_price_posted_to_the_taps`
  - `test_a_panel_fill_writes_its_note_in_the_tmp_path_vault` (new).
  - No offline trip.
- U1 and U2 outputs: WHOLE under `## E2 RED`.
- Suites:
  - E0: offline `3318 passed` · live-note `146 passed, 1 skipped`.
  - E2 offline: `3320 passed`.
  - W on `01d0fbb9`: offline `3320` · with-DB `3728` + `107` = **3835** · live-note `146`.
- F per take:
  - take 1 (E2): F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, end = F0, no forward;
  - take 2 (W): F0 same, F1 `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 = F0.
- Lock times: take 1 17:30:10 → 17:31:16 · take 2 17:41:48 → 17:56:57.
- The desk's dev-vault listing from R109: `-rw------- 767 Sep 29 09:35 …/2 - Trades/Trade-2026-09-03 10-00-00 -TEST.md` · `-rw------- 665 Sep 29 09:35 …/2 - Trades/Trade-2026-09-03 10-00-00 -ZZPB.md`. I ran no command on the dev vault. The guard wraps the resolver: every E2 trip raised after the original resolved the path and before any read or write.
- Worth a checker's eye:
  - The guard's original resolver still `stat`s the target DIRECTORY (`path.parent.is_dir()`, `vault_writer.py:32`) before the guard checks the path. That is a directory existence check, not a file read or write.
  - At E2, lock take 1 ran the with-DB red files THREE times: the `-rA` run, whose output was truncated; the `-rfE --tb=no` summary; and a `-k`-narrowed `--tb=line` run of three ids. All ran inside the one take, and each ended inside the suite's rolled-back transaction (F0 unchanged, no TEST / ZZPB rows after).
  - U1's printed body is the sheet's first 200 characters. Whether the page carries a refusal banner is not printed (the RUN asserts nothing).
- Stop line: the last line of this file.

## CONTINUE
done — every step ran: AUTHORIZATION, PREFLIGHT, E0, E2 `b493c09c`, E3 `01d0fbb9`, W, RESTARTS, CLOSE. `cobalt_dev` is at `0013` (F2 = F0); no `.env` in any worktree.

## ESCALATE
1. **ESCALATE U2: `exit_price: 5.10` → `exit_price: "5.1"`.** The file's typed `5.10` (the test's hand edit) is re-rendered by the next frontmatter merge: YAML reads it as a float, and the renderer quotes it and drops the trailing zero. `entry_time` / `exit_time` render quoted (`"2026-09-03 10:00"` / `"2026-09-03 10:31"`). The value is kept (not replaced by Cobalt's `5.6000`), but its bytes change. This is for the round-2 classifier; nothing was fixed here (`vaultwrite/frontmatter.py`, NOT IN THIS FIX). `design-changing: no` (a run, not a build).
2. U1 needs no ESCALATE line. Both `NaN` and `-1` on the manual `/fill` returned 200 with no row written (counts unchanged, `state='TRIGGERED'`, `actual_fill=None`, `trade_note_path=None`). Recorded for the classifier.
3. L74: recorded once under `## L74`.

**"C4 fix r1 is checked by `25-s3-exits-c4-fix-r1-check.md` (round 2 of ≤3: Opus 5.5 · Sol · Grok, L67). X3 (human wins once) is OUT OF SCOPE here and routed by the desk. With C4 checked, C1–C4 are the S3 exits set for ONE deploy (L43), gated on the combined tree (L68). The builder decided nothing."**

S3 EXITS C4 FIX R1 BUILT 01d0fbb9 | on d05ae72d | migration none (0021 rolled back) | offline 3320/0 | with-DB 3835/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | FIX: 1 | RUNS: 2 | ESCALATE: 1
