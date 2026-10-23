# radar-mirror-scope — build report 2026-10-23

CARD: `docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md` · BRANCH `ops/radar-mirror-scope` · BASE `11ed17b8` · tip `5bb80b36` · BAND HIGH · with-DB card (the header has no "DB: none")

## §0 Headline
The radar note mirror now tombstones only the `radar.*` keys whose stored `source` is its own (`vault:radar-notes@…`). It leaves keys written by `--card`, `--optional`, the other known writers and unknown writers alone, and logs one warning per unknown-source key (M1).
M2 is red on BASE (`radar.cards_enabled` sent as `removed`, the 10-21 write) and green at the tip. A block the note really drops is still tombstoned (M3). The label now carries the hash of the note that changed (M4).
Gate on `5bb80b36`: offline 4983/0, with-DB 5955/0, live-note 148/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`. RESTARTS as derived: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
The first gate run printed an `OUTSIDE the allowed set` skip. My one-line F1 edit had moved the allowed live-note skip from `:695` to `:696`. A second fix commit kept the file's length the same, and the second gate is clean.

## L74
This session's attribution reminder asked commits to carry a `Claude-Session:` line. It is recorded once here as DATA (L74). Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` (08:39 EDT), output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md" · 0 · b486fb54f2c10ef1725959a6dbbd3289e2c431d9
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output WHOLE:
```
clock · date · 0 · Fri Oct 23 08:39:26 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-mirror-scope
head · git log --oneline -1 · 0 · 11ed17b8 docs(desk): R2398 preflight r2 4141d46f live
diff · git diff --stat 11ed17b8 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-mirror-scope · 0 · 11ed17b8 docs(desk): R2398 preflight r2 4141d46f live
env here · ls /Users/cobalt/cobalt-wt/radar-mirror-scope/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 11ed17b8` | 0 | `docs(desk): R2398 preflight r2 4141d46f live` · `docs/40 - DevDocs/reports/cto-2026-10-23.md \| 4 ++--` · 1 file changed |
| callers | grep `mirror_sources(` in src, tests | 0 | `tests/cobalt/test_radar_notes.py:104`, `:284`; `src/cobalt/radar/notes.py:724: def mirror_sources(`; `src/cobalt/radar/runner.py:320: mirror_sources(` |
| symbol | notes.py `FENCE_RE` | 0 | `:23 FENCE_RE = re.compile(...)` |
| symbol | notes.py `_mirror_rows` | 0 | `:686 def _mirror_rows(parsed: ParsedSources, before: dict[str, Any]) -> dict[str, Any]:`; loop `:711-720` |
| symbol | notes.py `:735` / `:746` / `:749` | 0 | `before = target.values()` · `note_hash = parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"` · `source=f"vault:radar-notes@{note_hash[:12]}",` |
| symbol | store.py `rows` / `values` / `put` | 0 | `:45 def rows`, `:48 SELECT key, value, source, updated_at`; `:54 def values`; `:60 def put`; `:90-92` unchanged skip |
| symbol | `0001_trader_settings.sql:43` | 0 | `source     TEXT NOT NULL,` |
| label | `card.py:324` | 0 | `source=f"card:{path.name}@sha256:{digest}",` |
| label | `cli.py:218`, `:280`, `:283` | 0 | `source_label = f"optional:{Path(args.optional).name}"` · `f"git:{args.from_git}"` · `f"yaml:{args.from_dir}"` |
| label | `aset/web.py:1367` | 0 | `source=f"aset.change_line@sha256:{proposal.sha256}",` |
| label | `0004_radar_pool.sql:74` | 0 | `SELECT id, 'aset.account_mode', '"live"'::jsonb, 'db_migration:0004'` |
| symbol | `runner.py:17`, `:30`, `:320` | 0 | `from loguru import logger` · `from .notes import ParsedSources, configured_sources, mirror_sources` · `mirror_sources(` (inside `try`; `except Exception` stamps a `mirror` failure, `:328-333`) |
| fakes | `test_radar_notes.py:59-70` `MirrorStore`, `:272-282` `Store` | 0 | read whole |
| fakes | `test_radar_runner.py:92-99` `Settings`, `:305-322` `CrossingSettingsStore` (`self.rows = {}` `:310`, used `:313`, `:320`) | 0 | read |
| fakes | `test_radar_evaluate.py:521-527` `_Settings` | 0 | read |
| fakes | `test_radar_price_floor.py:41` | 0 | `from test_radar_runner import ActiveClock, Poller, Settings`; loguru sink `:199-208` |
| fakes | grep `RadarRunner(` under tests | 0 | `test_radar_evaluate.py:542`, `test_radar_replay.py:285`, `:464` (`settings_store=SimpleNamespace()`), `test_radar_handicap_group.py:70` (`settings_store=None`), `test_radar_runner.py:36`, `:117`, `:362`, `test_radar_price_floor.py:138` |
| fakes | grep `settings_store=` under tests | 0 | 43 hits. Those reaching `RadarRunner` are listed above. The rest pass to `radar(...)` heartbeat checks, panels, day-open checks or `build_ladder_view`, which never call `mirror_sources` (callers grep) |
| fixture | `tests/fixtures/radar/radar-lists.example.md` | 0 | one `list: index_heavyweights` fence (`:3-71`); last fence `kind: exclude` / `tickers: [SPY]` (`:73-76`) |
| wc | `wc -l` of row files | 0 | `761 src/cobalt/radar/notes.py` · `286 tests/cobalt/test_radar_notes.py` · `663 tests/cobalt/test_radar_runner.py` · `872 tests/cobalt/test_radar_evaluate.py` · `66 docs/40 - DevDocs/cobalt/radar/notes.md` |
| READ tail | `tail -n 3` survey report | 0 | `SURVEYED · cause: prod radar vault-note mirror (notes.py:711-720) tombstoned radar.cards_enabled and radar.benchmark at 10-21 18:12:55 ET after the R2343 Radar Lists.md WBD edit · decisions: 1` |
| restarts | `uv run cobalt jobs restarts 11ed17b8..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` (empty range) |

Records copied from the card's `## RECORDS` and re-read:
- Every `notes.py` line the drafter cites (`:686`, `:711-720`, `:735`, `:736-744`, `:746`, `:747`, `:749`) was re-read at BASE `11ed17b8` and matches.
- `store.py:45-52`, `:54-56` and `0001_trader_settings.sql:43` match.
- The labels at `card.py:324`, `web.py:1367`, `0004_radar_pool.sql:74` and `cli.py:218` / `:280` / `:283` match.
- The fixture's last fence is `kind: exclude`.
- The drafter's BASE `7487bb56` was reset by the desk to `11ed17b8` (preflight `head`).
- The brain record 9b07db5a, the R2389 row and the ladder line cannot be re-read with this list beyond what AUTHORIZATION printed.

PROVEN BY FIRST REAL USE:
- `sh /Users/cobalt/cobalt/ops/desk/*`: at AUTHORIZATION and PREFLIGHT.
- `uv run cobalt jobs restarts *`: above.
- `uv run pytest *` and `COBALT_LIVE_VAULT_ROOT=… uv run pytest *`: at E0.
- `git add *` and `git commit *`: at E2.
- The with-DB strings: inside `gate.sh` at W.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `11ed17b8` → `4974 passed, 878 skipped, 4 xfailed, 36 warnings in 744.60s (0:12:24)` (0 failed, 0 errors). Its skip line for the live-note proof: `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.21s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` and does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
I wrote `tests/cobalt/test_radar_mirror_scope.py` (NEW, offline, fake `_Store`, constructed seeds as the card gives them).

The first run showed `test_m4_the_label_in_each_case[lists_missing]` red for the wrong reason: `FileNotFoundError`, because the expected-label dict hashed the absent file eagerly. I rewrote it to compute the expected value only for its own case. The second run, `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_mirror_scope.py`, gave `5 failed, 4 passed in 0.15s`:
- M1 `test_m1_unknown_source_is_left_alone_loudly`: `AssertionError: {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...}` / `assert 'radar.hand_typed' not in {… 'radar.hand_typed': {'block': None, …` (`:121`). The key is tombstoned: the row's red.
- M2 `test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical`: `AssertionError: ('radar.cards_enabled', {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...})` (`:139`). `radar.cards_enabled` is in `sent` as the tombstone: the 10-21 write.
- M4 `test_m4_the_source_names_the_note_that_changed`: `AssertionError: assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-...@7e674c8b052e'` (`:168`). The label carries the Screens fixture's hash on a Lists edit.
- M4 cases `[lists_only]`: the same Screens-hash red (`:201`). `[lists_missing]`: `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-notes@missing'` (`:201`).
- GREEN on BASE: M3 `test_m3_a_block_the_note_drops_is_still_tombstoned`, and the M4 cases `[first]`, `[screens_only]` and `[both]` (BASE already gives the Screens hash there).

No with-DB red, so no lock was taken at E2. Commit `de798203 wip(radar-mirror-scope): red — M1, M2, M4 red on BASE, M3 green`.

## E3 THE ROWS
- **M1** (`src/cobalt/radar/notes.py`):
  - `mirror_sources` reads `stored = target.rows()` once (`:767`), then builds `before` (`{key: value}`) and `owners` (`{key: source}`) and passes both to `_mirror_rows`.
  - Constants beside `FENCE_RE`: `MIRROR_SOURCE_PREFIX = "vault:radar-notes@"` (`:27`, the one assignment) and `FOREIGN_SOURCE_PREFIXES` (six labels, each with its `file:line` comment).
  - The loop now tombstones a `radar.*` key absent from the notes only when `owners[key].startswith(MIRROR_SOURCE_PREFIX)` (`:733`). Any other key stays out of `rows`. A source with neither prefix gets `logger.warning("radar mirror left {} alone: source {} is not this mirror's", key, source)` (`:742`). The note and block rows are unchanged.
  - The label is `source=f"{MIRROR_SOURCE_PREFIX}{note_hash[:12]}"` (`:783`).
  - `docs/…/radar/notes.md` line 3 says "mirrors status through `TraderSettingsStore.put`". It does not state the tombstone rule, so it does not misstate it, and I left it as it was.
- **M2, M3**: tests only. M3's existing companion is `test_radar_notes.py` `Store`, which gains `rows()` returning `radar.screen.old` with source `"vault:radar-notes@" + "0" * 12`, so it still asserts `removed`.
- **M4**: `_changed_note_hash(parsed, before)` returns the hash of the first note, Screens then Lists, whose `note_sha256` is not `None` and differs from the stored `radar.note.<kind>` row's `note_sha256`; otherwise `"missing"`. The format `vault:radar-notes@<hash12>` is unchanged.
- **F1**: every fake that reaches `mirror_sources`, by the `mirror_sources(`, `settings_store=` and `RadarRunner(` greps:
  - `test_radar_notes.py` `MirrorStore` gains `rows()` (returns `[]`), and `Store` gains `rows()` (row M3).
  - `test_radar_runner.py` `Settings` gains `rows()` (returns `[]`). `test_radar_price_floor.py:41` imports this class.
  - `test_radar_runner.py` `CrossingSettingsStore`: the attribute `self.rows` is renamed `self.stored`. It gains `rows()`, and `put` now takes `source` and keeps it (`self.source`) for `rows()`.
  - `test_radar_evaluate.py` `_Settings` gains `rows()`.
  - `test_radar_replay.py:285`, `:464` (`SimpleNamespace()`) and `test_radar_handicap_group.py:70` (`None`) are unchanged. Their suites are green in W, and their runners do not reach the mirror there.
- **D0**: one section `## 2026-10-23 — radar-mirror-scope` appended after the last section of `docs/40 - DevDocs/cobalt/radar/notes.md`. It covers the 10-21 cause, OWNERSHIP, `MIRROR_SOURCE_PREFIX`, the unknown-source warning and the M4 label.

Greens after the fix:
- `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_mirror_scope.py` → `9 passed in 0.16s`.
- The card's offline suite, `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_drc_d4_fix_r1.py` → `101 passed, 1 skipped in 27.86s`. The skip is `tests/cobalt/test_radar_evaluate.py:696: COBALT_LIVE_VAULT_ROOT not set` before the second fix and `:695` after it.

THE MUTATIONS. Each was made with Edit, run alone, then undone with Edit. `git status --short --branch` at the end → `## ops/radar-mirror-scope` plus only the untracked report.
1. Ownership check → `if True:` (tombstone every absent key). `2 failed, 7 passed`: M1 `assert 'radar.hand_typed' not in {…}` (`:121`), M2 `AssertionError: ('radar.cards_enabled', {…})` (`:139`).
2. Never tombstone → `if False:`. Scope and notes tests: `2 failed, 23 passed`: M3 `KeyError: 'radar.exclude'` (`:151`), `test_radar_notes.py::test_mirror_replaces_old_block_with_parse_failed_status` `KeyError: 'radar.screen.old'` (`:293`).
3. Warning removed (`pass`). `1 failed, 8 passed`: M1 `assert 0 == 1` (`:124`).
4. Warning for every non-owned key (`else:`), which breaks "known writers silently". `1 failed, 8 passed`: M1 `assert not ["radar mirror left radar.benchmark alone: source optional:optional-settings.yaml is not this mirror's", …]` (`:127`).
5. Label back to `parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"`. `3 failed, 6 passed`: M4 named (`:168`), `[lists_only]` and `[lists_missing]` (`:201`).
6. Note order Lists then Screens. `2 failed, 7 passed`: `[first]` (`:183`), `[both]` (`:201`).
7. Only Lists read, at PRE-STOP SELF-CHECK. `3 failed, 6 passed`: `[first]`, `[screens_only]` (`assert 'vault:radar-notes@missing' == 'vault:radar-...@2e5777e04990'`), `[both]`.
8. F1: `test_radar_runner.py` `Settings.rows` removed. `2 failed, 18 passed`: `test_stage_order_is_membership_pool_mirror_then_bars` and `test_mirror_failure_is_stamped_and_bars_continue`, `At index 2 diff: 'failure' != 'mirror'`. A fake without `rows()` turns the mirror into a stamped failure.

Commit `3067e8b9 fix(radar-mirror-scope): the radar note mirror tombstones only the radar.* keys it owns; label names the changed note (M1, M2, M3, M4, F1, D0; L1, L32, L69)`.

The second fix (a red at W that E2 / E3 did not show): the first gate printed `OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_radar_evaluate.py:696: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`. `ops/desk/gate-lists.md:54` `## ALLOWED SKIPS` names `tests/cobalt/test_radar_evaluate.py:695`, and the F1 line `def rows(self): return []` in `_Settings` had moved the test down one line. `gate-lists.md` is not in any row's `files`, so the fix stays inside `test_radar_evaluate.py`: `_Settings.put`'s body became one line, `return before_commit() or {}`, so the file's line count above the test is the same as BASE. Then `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py` → `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: …` / `31 passed, 1 skipped in 7.67s`. Commit `5bb80b36 fix(radar-mirror-scope): keep the live-note skip at test_radar_evaluate.py:695, the allowed-skip line (F1, L68)`.

## RESTARTS
`uv run cobalt jobs restarts 11ed17b8..HEAD` at `5bb80b36`, WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-build-2026-10-23.md	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. The same table was printed at `3067e8b9`.

## W THE THREE SUITES
Gate run 2 (the record) on `5bb80b36`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-mirror-scope all --deploy` (no `--deselect`, no `--tickers`: this build adds no with-DB test and writes no ticker; no `--migration`). Exit 0. Verdict lines WHOLE:
```
tests/ops: skipped (no ops paths)
offline 4983/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5955/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-all-20261023-093133.log
```
- (a) offline 4983/0; the W line is `tests/ops: skipped (no ops paths)`. The tests this build adds are `test_radar_mirror_scope.py::test_m1_unknown_source_is_left_alone_loudly`, `::test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical`, `::test_m3_a_block_the_note_drops_is_still_tombstoned`, `::test_m4_the_source_names_the_note_that_changed` and `::test_m4_the_label_in_each_case[first|screens_only|lists_only|both|lists_missing]` (9 ids).
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:975`), `LEVEL 0013`, lock `waited 0 min` (log `:963-967`).
- (c) pass 1 (log `:1031` `pass 1: whole (deploy)`), the executed command, log `:1033`:
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`
  Every SKIPPED line the gate prints is quoted above, and none is marked `OUTSIDE the allowed set`.
- (c2) / (c3) forward and pass 2: the pass 2 command is at log `:1290`. `with-DB 5955/0` = pass 1 + pass 2. This build adds no with-DB id.
- (c3r) `stray rows: not read (no --tickers given)`: this build's tests use a fake store and write no row.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2258`), `cobalt_dev: 0013 — F2 = F0` (log `:2312`), `lock released` (log `:2313-2314`), `.env: removed`. Then `ls /Users/cobalt/cobalt-wt/radar-mirror-scope/.env` → `No such file or directory`.
- (e) live-note 148/0, with no skip naming `COBALT_LIVE_VAULT_ROOT` in that pass.

Gate run 1 on `3067e8b9` (superseded): exit 0, `offline 4983/0`, `with-DB 5955/0`, `live-note 148/0`, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`, log `/Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-all-20261023-085738.log`. It printed one red: `OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_radar_evaluate.py:696: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`. The second fix above clears it.

## PRE-STOP SELF-CHECK
1. Every added or changed test was shown RED for its named reason, against a mutation or a negative control:
   - M1: E2 red, and mutations 1, 3 and 4.
   - M2: E2 red and mutation 1.
   - M3: mutation 2 (green on BASE by design).
   - `test_mirror_replaces_old_block_with_parse_failed_status`: mutation 2.
   - M4 named test: E2 red and mutation 5.
   - M4 cases: `[lists_only]` and `[lists_missing]` by E2 and mutation 5; `[first]` and `[both]` by mutation 6; `[screens_only]` by mutation 7.
   - F1 fakes: mutation 8.
   - One test was rewritten (`[lists_missing]`, a wrong-reason red at E2).
2. Every entry path is pinned. The callers grep gives `mirror_sources(` at `runner.py:320`, pinned through the F1 runner fakes (mutation 8), and at `test_radar_notes.py:104` / `:284` (the notes suite, mutation 2). The ownership branches are pinned: mirror-owned (M3), known foreign (M2, and M1's silence check, mutation 4) and unknown (M1, mutation 3). So are the label states X4 names: first mirror, Screens only, Lists only, both, and a note missing (M4 cases).
3. Lines re-read at the tip `5bb80b36`:
   - `grep -n -F "MIRROR_SOURCE_PREFIX" src/cobalt/radar/notes.py` → `27`, `733`, `783`.
   - `grep -n -F "radar mirror left" …` → `742`.
   - `grep -n -F "stored = target.rows()" …` → `767`.
   - `grep -n -F "def rows(self)"` over the four test files → `test_radar_notes.py:63`, `:278`; `test_radar_runner.py:94`, `:314`; `test_radar_evaluate.py:522`; `test_radar_mirror_scope.py:48`.
   - `git diff --stat 11ed17b8 5bb80b36` → 6 files, `291 insertions(+), 12 deletions(-)`.
   - DEPLOY PROOF on the worktree tree: `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` → `1`; `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" tests/cobalt/test_radar_mirror_scope.py` → `1`.

## FOR THE CHECK
- Range `11ed17b8..5bb80b36`:
  - `de798203 wip(radar-mirror-scope): red — M1, M2, M4 red on BASE, M3 green`
  - `3067e8b9 fix(radar-mirror-scope): the radar note mirror tombstones only the radar.* keys it owns; label names the changed note (M1, M2, M3, M4, F1, D0; L1, L32, L69)`
  - `5bb80b36 fix(radar-mirror-scope): keep the live-note skip at test_radar_evaluate.py:695, the allowed-skip line (F1, L68)`
- Per row, the reds, mutations and greens are under E2 and E3 (quoted).
- Caller greps are under PREFLIGHT.
- R1 RUN output WHOLE is under RESTARTS.
- The suites are under W (gate run 2 is the record). F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87` in one lock take, inside `gate.sh`: taken with `lock: waited 0 min`, released `lock released`. F1 / forward lines are in the log (no migration of this build).
- X5: `grep '"removed"' src` → only `src/cobalt/radar/notes.py:738` (the writer). A wider grep (`'removed'|== "removed"|status.*removed`) adds only `src/cobalt/voice/scratch.py:133`, a log string about a partial file. No reader in `src` matches on a tombstone status.
- X6: the tool derives `com.cobalt.aset,com.cobalt.cos,com.cobalt.radar` for `src/cobalt/radar/notes.py` (`static import reach`), which is wider than the card header's `com.cobalt.radar`. The importers of `cobalt.radar.notes` in `src` are `radar/replay.py:125`, `radar/sources.py:16`, `drc/build.py:171`, `strike/measure.py:135`, `:157`, `strike/detector.py:51`, `:113`, `:315`, `archiver/config.py:12`, `prefill/daily.py:91`, `archiver/runner.py:62`, `:84`, `:116`, `radar/propose.py:564`, `:628`, `prefill/checkpoints.py:83`, `radar/handicap_dry_run.py:51`, `:492`, `radar/runner.py:30`, `:356`, `replay/cli.py:104`, `replay/movers.py:84` and `replay/runner.py:56`.
- M4's literal rule, for X4: the label takes the first CHANGED note that has a hash. When only the Lists note changed and it is missing (hash `None`), the label is `vault:radar-notes@missing` even though Screens has a hash, because Screens did not change. That is what the card's rule says ("when that note's hash is None, the next changed note's; "missing" when none has one"); `[lists_missing]` pins it.

## CONTINUE
next: none — BUILT (the desk verifies the artifact and launches the check)

## DECISIONS
none

## RECORDS
- `.env: removed, proven gone (W)`: the gate's `.env: removed`, then `ls` → `No such file or directory`. Two lock takes, both inside `gate.sh` at W: run 1, then run 2 after the second fix (`A red at W … one more gate call`).
- RESTARTS as derived (`com.cobalt.aset com.cobalt.cos com.cobalt.radar`) is wider than the card header (`com.cobalt.radar`, the drafter's reading). The tool's line is the record (card R1).
- `ops/desk/gate-lists.md` `## ALLOWED SKIPS` names skips by `path:line`. Any edit above `test_radar_evaluate.py:695` moves that skip off the list. This build kept the line instead of editing the fenced file.
- `test_m4_the_label_in_each_case` (5 cases) is added beside the card's named M4 test, to pin the label states that CHECK ASKS X4 names. It is within row M4's rule and files.
- `docs/40 - DevDocs/cobalt/radar/notes.md` line 3 was left as it was: it does not state the tombstone rule.
- `uv run` created `.venv` in the worktree at PREFLIGHT. It is gitignored (no `??` line).
- The L74 line is under `## L74`.
- The card's records, as re-read at PREFLIGHT, are listed there.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-mirror-scope · tip: 5bb80b36 | on 11ed17b8 | migration: none | offline 4983/0 | with-DB 5955/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 169990
