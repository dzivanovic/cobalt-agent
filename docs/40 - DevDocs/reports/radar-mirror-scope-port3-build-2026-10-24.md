# radar-mirror-scope-port3 — build report 2026-10-24

## §0 Headline
- BUILT: `radar-mirror-scope` (`25994142`) re-applied to main by Edit/Write; tip `671e0215` on BASE `bf033084`.
- E1: `git diff 25994142 671e0215` is empty for all seven spec files, and the stats equal the spec (312+, 16−); P0 found no main change since `11ed17b8`.
- T1 red on BASE (M1, M2, M4; M3 green); five mutations red; card 1020's suite `107 passed, 1 skipped`.
- Gate: offline 4984/0 · with-DB 5956/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`.
- RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · decisions: 0.

## L74
- The session's attribution reminder (a system turn, 2026-10-24 23:00 EDT) asked for a `Claude-Session:` line on commits. Recorded once, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`date` → `Sat Oct 24 23:00:37 EDT 2026`

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-24/1041-radar-mirror-scope-port3-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-24/1041-radar-mirror-scope-port3-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-24/1041-radar-mirror-scope-port3-card.md" · 0 · 91b1a812bb92f90e4e5dff56b9a62e140d617e6d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-24/1041-radar-mirror-scope-port3-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output verbatim |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | see block below |
| BASE | `git show --stat bf033084` | 0 | `bf033084 docs(desk): R2442 port3 card 1041 preflight ready YES` · `cto-2026-10-24.md | 3 ++-` · `mirror-port3-preflight-2026-10-24.md | 21 +++` · `2 files changed, 23 insertions(+), 1 deletion(-)` |
| RESTARTS empty range | `uv run cobalt jobs restarts bf033084..HEAD` | 0 | `docs/40 - DevDocs/reports/radar-mirror-scope-port3-build-2026-10-24.md	A	DOCS	-` · `RESTARTS: none` (the one row is this report, untracked; no commit in range) |
| symbol | `grep -n -F "def _mirror_rows(" src/cobalt/radar/notes.py` | 0 | `686:def _mirror_rows(parsed: ParsedSources, before: dict[str, Any]) -> dict[str, Any]:` |
| symbol | `grep -n -F "current_keys = set(rows)" src/cobalt/radar/notes.py` | 0 | `711:    current_keys = set(rows)` |
| symbol | `grep -n -F "before = target.values()" src/cobalt/radar/notes.py` | 0 | `735:    before = target.values()` |
| symbol | `grep -n -F "vault:radar-notes@" src/cobalt/radar/notes.py` | 0 | `749:        source=f"vault:radar-notes@{note_hash[:12]}",` |
| callers | `grep -rn -F "_mirror_rows(" src` | 0 | `src/cobalt/radar/notes.py:686:def _mirror_rows(…)` · `src/cobalt/radar/notes.py:745:    rows = _mirror_rows(parsed, before)` |
| callers | `grep -rn -F "mirror_sources(" src` | 0 | `src/cobalt/radar/runner.py:320:            mirror_sources(` · `src/cobalt/radar/notes.py:724:def mirror_sources(` |
| wc | `wc -l` the six existing files | 0 | `761 notes.py` · `286 test_radar_notes.py` · `663 test_radar_runner.py` · `872 test_radar_evaluate.py` · `480 test_radar_replay.py` · `66 radar/notes.md` |
| READ tail | `tail -n 3 reports/radar-mirror-scope-check-2026-10-23.md` | 0 | `CHECK DONE · job: radar-mirror-scope · pass: 1 · tip: 25994142 · … held unfixed: 0 · … RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 164093` |
| main head | `git -C /Users/cobalt/cobalt log --oneline -1 main` | 0 | `a16584df docs(desk): R2443 port3 build 0c76f94e launched` |
| spec stat | `git diff --stat 11ed17b8 25994142` | 0 | `radar/notes.md 32 +++` · build report `234` · `.result 15` · `notes.py 46 +++-` · `test_radar_evaluate.py 4 +-` · `test_radar_mirror_scope.py 201` · `test_radar_notes.py 7 +` · `test_radar_replay.py 21 +-` · `test_radar_runner.py 17 +-` · `9 files changed, 561 insertions(+), 16 deletions(-)` |

```
clock · date · 0 · Sat Oct 24 23:00:53 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/radar-mirror-scope-port3
    ?? "docs/40 - DevDocs/reports/radar-mirror-scope-port3-build-2026-10-24.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · bf033084 docs(desk): R2442 port3 card 1041 preflight ready YES
diff · git diff --stat bf033084 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-mirror-scope-port3 · 0 · bf033084 docs(desk): R2442 port3 card 1041 preflight ready YES
env here · ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port3/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

### P0 — MAIN SINCE BASE (RUN, asserts nothing)
| path | command | exit | output |
|---|---|---|---|
| `src/cobalt/radar/notes.py` | `git diff 11ed17b8..main -- <path>` | 0 | nothing |
| `tests/cobalt/test_radar_mirror_scope.py` | same | 0 | nothing |
| `tests/cobalt/test_radar_notes.py` | same | 0 | nothing |
| `tests/cobalt/test_radar_runner.py` | same | 0 | nothing |
| `tests/cobalt/test_radar_evaluate.py` | same | 0 | nothing |
| `tests/cobalt/test_radar_replay.py` | same | 0 | nothing |
| `docs/40 - DevDocs/cobalt/radar/notes.md` | same | 0 | nothing |
P0: no line of any spec file changed on main since `11ed17b8`; E1 (a) admits no line.

### Card records, copied and re-read
- Records 1–14 of the card's `## RECORDS` copied by reference (card `1041`, committed `91b1a812`). Re-read here: MAIN SINCE BASE (P0 above; `git diff --stat 11ed17b8 bf033084 -- src tests configs ops` → `configs/cobalt/rules.yaml | 2 +-` only); THE PRECEDENT (`git diff --stat 25994142 283389ff --` the seven paths → nothing); ANCHORS (`:686`, `:711`, `:713`, `:735`, `:746`, `:749` read with the Read tool, as the card states); CHECK 1020 stop line (tail above). Not re-readable by this list: the survey, deploy 1036, smoke-script line numbers (no step needs them).

## E0 BASELINE
- Offline, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (exit 0) → `4974 passed, 878 skipped, 4 xfailed, 36 warnings in 735.59s (0:12:15)`; 0 failed, 0 errors (the skips are Postgres env / `reaches cobalt_dev` / `COBALT_LIVE_VAULT_ROOT not set`, offline as expected).
- Live-note, `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (exit 0) → `146 passed, 1 skipped, 15 warnings in 28.68s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
T1 ported first: `tests/cobalt/test_radar_mirror_scope.py` written with the Write tool from `git show 25994142:tests/cobalt/test_radar_mirror_scope.py`; the four fakes brought to the spec hunk by hunk with Edit (found by content: `MirrorStore`, the inner `Store` of `test_mirror_replaces_old_block_with_parse_failed_status`, `Settings`, `CrossingSettingsStore`, `_Settings`, `ReplaySettingsStore` and `test_f1_replay_settings_store_rows_is_callable`).
- Equality before the commit: `git diff 25994142 -- <the four modified test files>` → nothing; after `git add`, `git diff --cached 25994142 --stat -- <the five test files>` → nothing.
- RED on BASE's `src/`: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py` (exit 1) → `5 failed, 4 passed in 0.19s`:
  - `FAILED …::test_m1_unknown_source_is_left_alone_loudly` — `assert 'radar.hand_typed' not in {… 'radar.hand_typed': {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...}, ...}` (`:121`): the hand-typed key is sent as a tombstone (card 1020's reason).
  - `FAILED …::test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical` — `AssertionError: ('radar.cards_enabled', {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...})` (`:139`): `radar.cards_enabled` in `sent` as a tombstone.
  - `FAILED …::test_m4_the_source_names_the_note_that_changed` — `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-...@7e674c8b052e'` (`:168`): the label carries the Screens hash (`33a77dc6c179` = the `first` case's Screens label, which passed).
  - `FAILED …::test_m4_the_label_in_each_case[lists_only]` — the same assertion (`:201`); `FAILED …[lists_missing]` — `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-notes@missing'` (`:201`).
  - GREEN: `test_m3_a_block_the_note_drops_is_still_tombstoned`, `test_m4_the_label_in_each_case[first]`, `[screens_only]`, `[both]`.
- No with-DB red: no lock taken at E2.
- Commit `07dd7d7c wip(radar-mirror-scope-port3): red — T1 tests ported from 25994142` (`5 files changed, 240 insertions(+), 10 deletions(-)`).

## E3 THE ROWS
- C1: `src/cobalt/radar/notes.py` brought to `25994142` by six Edits, each quoting the spec hunk (`from loguru import logger`; `MIRROR_SOURCE_PREFIX` / `FOREIGN_SOURCE_PREFIXES` after `FENCE_RE`; the `_mirror_rows(parsed, before, owners)` signature; the owned-only tombstone loop with the unknown-source warning plus `_changed_note_hash`; `stored = target.rows()` / `before` / `owners`; the `_changed_note_hash` call and `f"{MIRROR_SOURCE_PREFIX}{note_hash[:12]}"`).
- D1: `docs/40 - DevDocs/cobalt/radar/notes.md` section `## 2026-10-23 — radar-mirror-scope` added by Edit, verbatim from the spec. Per the card, this job adds no section of its own.
- `git diff 25994142 -- src/cobalt/radar/notes.py "docs/40 - DevDocs/cobalt/radar/notes.md"` → nothing.
- GREEN, card 1020's offline suite with the A1 file: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_radar_replay.py` → `107 passed, 1 skipped in 28.22s`; skip `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` (the live-note suite runs it: W (e)).

THE MUTATIONS (each made with Edit, run, then undone with Edit):
| mutation | run | result | first failing line |
|---|---|---|---|
| A: `if source.startswith(MIRROR_SOURCE_PREFIX):` → `if True:` (undoes ownership) | `test_radar_mirror_scope.py` | `2 failed, 7 passed` (M1, M2) | `:121 AssertionError: {'block': None, …}` · `:139 AssertionError: ('radar.cards_enabled', …)` |
| C (M3 negative control): same line → `if False:` (no tombstone) | `test_radar_mirror_scope.py test_radar_notes.py` | `2 failed, 23 passed` | `test_radar_mirror_scope.py:151: KeyError: 'radar.exclude'` · `test_radar_notes.py:293: KeyError: 'radar.screen.old'` |
| B: `note_hash = _changed_note_hash(parsed, before)` → the old `parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"` | `test_radar_mirror_scope.py` | `3 failed, 6 passed` (M4, `[lists_only]`, `[lists_missing]`) | `:168: AssertionError: assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-...@7e674c8b052e'` |
| W: `elif not source.startswith(FOREIGN_SOURCE_PREFIXES):` → `elif False:` (no warning) | `test_radar_mirror_scope.py` | `1 failed, 8 passed` (M1) | `:124: AssertionError: [] assert 0 == 1` |
| F1: `ReplaySettingsStore.rows` removed | `test_radar_replay.py` | `1 failed, 5 passed` | `:143: AttributeError: 'ReplaySettingsStore' object has no attribute 'rows'` |
After undoing them: `git diff 25994142 --stat --` the seven paths → nothing; the 1020 suite again → `107 passed, 1 skipped in 28.22s`.
- Commit `671e0215 fix(radar-mirror-scope-port3): port radar-mirror-scope 25994142 onto main by Edit/Write (T1, C1, D1; L3, L79)` (`2 files changed, 72 insertions(+), 6 deletions(-)`).

### E1 — THE EQUALITY PROOF (RUN) on tip `671e0215`
(a) `git diff 25994142 671e0215 -- <path>`, one call each (exit 0):
| path | output |
|---|---|
| `src/cobalt/radar/notes.py` | nothing |
| `tests/cobalt/test_radar_mirror_scope.py` | nothing |
| `tests/cobalt/test_radar_notes.py` | nothing |
| `tests/cobalt/test_radar_runner.py` | nothing |
| `tests/cobalt/test_radar_evaluate.py` | nothing |
| `tests/cobalt/test_radar_replay.py` | nothing |
| `docs/40 - DevDocs/cobalt/radar/notes.md` | nothing |
(b) `git diff --stat bf033084 671e0215 --` the seven paths, and `git diff --stat 11ed17b8 25994142 --` the seven paths, are identical:
```
 docs/40 - DevDocs/cobalt/radar/notes.md |  32 +++++
 src/cobalt/radar/notes.py               |  46 +++++++-
 tests/cobalt/test_radar_evaluate.py     |   4 +-
 tests/cobalt/test_radar_mirror_scope.py | 201 ++++++++++++++++++++++++++++++++
 tests/cobalt/test_radar_notes.py        |   7 ++
 tests/cobalt/test_radar_replay.py       |  21 +++-
 tests/cobalt/test_radar_runner.py       |  17 ++-
 7 files changed, 312 insertions(+), 16 deletions(-)
```
(c) `git diff --stat bf033084 671e0215 -- src tests configs ops`:
```
 src/cobalt/radar/notes.py               |  46 +++++++-
 tests/cobalt/test_radar_evaluate.py     |   4 +-
 tests/cobalt/test_radar_mirror_scope.py | 201 ++++++++++++++++++++++++++++++++
 tests/cobalt/test_radar_notes.py        |   7 ++
 tests/cobalt/test_radar_replay.py       |  21 +++-
 tests/cobalt/test_radar_runner.py       |  17 ++-
 6 files changed, 280 insertions(+), 16 deletions(-)
```
E1: all three hold.

### DEPLOY PROOF markers, read on the worktree tree at `671e0215`
- `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` → `1`
- `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" tests/cobalt/test_radar_mirror_scope.py` → `1`
- `ls src/cobalt/radar/notes.py tests/cobalt/test_radar_mirror_scope.py` → both listed, exit 0

## RESTARTS
R1 `uv run cobalt jobs restarts bf033084..HEAD` (HEAD = `671e0215`; the report is untracked here):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port3-build-2026-10-24.md	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. It matches the card header.

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-mirror-scope-port3 all --deploy` (exit 0; no `--deselect`: this build adds no with-DB test; no `--tickers`: no with-DB test writes a ticker; no `--migration`). Verdict lines, whole:
```
tests/ops: skipped (no ops paths)
offline 4984/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5956/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-port3-all-20261024-231737.log
```
No skip marked `OUTSIDE the allowed set`.
- (a) offline: log `:957` `4984 passed, 878 skipped, 4 xfailed, 36 warnings in 717.02s (0:11:57)` → `4984`; this build adds `tests/cobalt/test_radar_mirror_scope.py` (9 tests) and `test_radar_replay.py::test_f1_replay_settings_store_rows_is_callable` (E0 4974 + 10 = 4984).
- (b) lock: log `:963-964` `sh …/take-devdb-lock.sh radar-mirror-scope-port3 90` → `lock taken: radar-mirror-scope-port3`; `:968-969` `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly this worktree's; `:975` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `LEVEL 0013`.
- (c) pass 1, the executed command (log `:1033`), whole:
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`
  → log `:1203` `5712 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 895.08s (0:14:55)` → `<d1>` = 5712.
- (c2) forward: log `:1205` **`dev forward: APPLIED 23:44:56`**; `:1289` `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2: log `:2186` `244 passed, 1 deselected, 5 warnings in 245.21s (0:04:05)` → `<d2>` = 244; 5712 + 244 = 5956 = `with-DB 5956/0`. This build adds no with-DB test id.
- (c3r) `stray rows: not read (no --tickers given)`: no with-DB test of this build writes a ticker.
- (f) rollback: log `:2260` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`**; `:2315-2316` `release-devdb-lock.sh radar-mirror-scope-port3` → `lock released`; `:2318-2320` `No such file or directory` / `.env: removed`. My own call `ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port3/.env` → `No such file or directory` (exit 1).
- (e) live-note: log `:2387` `148 passed, 1 skipped, 15 warnings in 26.43s` → `live-note 148/0`; the skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), which does not name `COBALT_LIVE_VAULT_ROOT`.
- The proof table's `code: 671e0215 (DIRTY: 1 path(s))` (log `:2310`): the one path is this untracked report.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED: M1, M2, M4 (`[lists_only]`, `[lists_missing]`) at E2 on BASE's `src/`; M1 again under mutations A and W; M2 under A; M3 and `test_mirror_replaces_old_block_with_parse_failed_status` (the changed inner `Store.rows`) under C; M4 cases under B; `test_f1_replay_settings_store_rows_is_callable` under F1 (all quoted in E2 / E3). Tests that stay green under every single-line mutation: `[first]`, `[screens_only]`, `[both]` (their expected label equals the Screens hash on both the old and the new code by construction; they are spec tests, kept byte-equal under X5). The `rows()` of `MirrorStore`, `Settings`, `CrossingSettingsStore`, `_Settings`: once C1 lands they are needed by every test that drives `mirror_sources` through them (a fake without `rows()` raises `AttributeError` at `stored = target.rows()`, the same failure F1 shows). Nothing was rewritten: the card fences the spec bytes.
(2) Entry paths: `_mirror_rows` has one caller (`notes.py:779`, from `mirror_sources`), and `mirror_sources` has one `src` caller (`runner.py:320`). They are pinned by `test_radar_mirror_scope.py` (direct, five label cases and the owned / foreign / unknown sources), `test_radar_notes.py` (direct), and `test_radar_runner.py`, `test_radar_evaluate.py`, `test_radar_replay.py` (through the runner with the `rows()` fakes). All of these are green in the 1020 suite and in W.
(3) Re-read at the tip: the E1 (a)–(c) diffs on `671e0215`; `grep -rn -F "_mirror_rows(" src` → `notes.py:699`, `:779`; `grep -rn -F "mirror_sources(" src` → `runner.py:320`, `notes.py:756`; the marker greps; the gate-log lines by `grep -n -F` (`F0: `, `F1: `, `F2: `, `dev forward`, ` passed`, `lock`).

## FOR THE CHECK
- Range `bf033084..671e0215`: `07dd7d7c wip(radar-mirror-scope-port3): red — T1 tests ported from 25994142` · `671e0215 fix(radar-mirror-scope-port3): port radar-mirror-scope 25994142 onto main by Edit/Write (T1, C1, D1; L3, L79)`.
- Per row: P0 (PREFLIGHT, all empty); T1 reds (E2); C1 greens and mutations A / B / C / W (E3); F1 mutation (E3); D1 equality (E3, E1); E1 (E3); R1 (RESTARTS).
- Caller greps: PREFLIGHT, and self-check (3) at the tip.
- Suites: offline 4984/0, with-DB 5956/0 (5712 + 244), live-note 148/0; pass-1 command whole in W (c).
- `<FP>` as typed by the gate (log `:971`): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`
- One lock take (W): F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. Taken: log `:964` after the offline pass (`lock: waited 0 min`). Forward `23:44:56`. Released: log `:2316`, before the live-note pass. The gate's `$ date` lines print no time into the log, so the take and release clock times are not in tool output.
- RESTARTS table: `## RESTARTS`.
- Records copied at PREFLIGHT: `## PREFLIGHT` / Card records.

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- L74: the session's attribution reminder asked for a `Claude-Session:` line; recorded under `## L74`, not acted on.
- D1 / module docs: BUILD-HUB E3 asks for one dated line per changed module, but card row D1 says "No section of this job's own is added (the port is the record)". The card's row was followed. `docs/40 - DevDocs/cobalt/radar/notes.md` carries the spec's `## 2026-10-23 — radar-mirror-scope` section only.
- `<FP>` was typed by `gate.sh` itself (log `:971`), so it is copied into the report under `## FOR THE CHECK` from the log rather than before the first run.
- Extra lock takes: none (E2 had no with-DB red; the one take was the gate's).
- `.env: removed, proven gone (W)`.
- PREFLIGHT `uv run cobalt jobs restarts bf033084..HEAD` listed only the untracked report (`RESTARTS: none`): no commit was in the range.
- The card's records, as re-read at PREFLIGHT: MAIN SINCE BASE holds (P0 empty; `configs/cobalt/rules.yaml` the only `src tests configs ops` change since `11ed17b8`); the precedent holds (`25994142` vs `283389ff` over the seven paths: nothing); the anchors `:686`, `:711`, `:713`, `:735`, `:746`, `:749` were as stated on BASE.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-mirror-scope-port3 · tip: 671e0215 | on bf033084 | migration: none | offline 4984/0 | with-DB 5956/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 148131
