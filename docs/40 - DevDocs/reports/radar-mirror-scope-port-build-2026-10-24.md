# radar-mirror-scope-port — build report 2026-10-24

## §0 Headline
- Card 1020's checked diff (`11ed17b8..25994142`, seven files, 312+ 16−) re-applied on `0866400b` by Edit/Write; tip `283389ff`.
- E1: `git diff 25994142 283389ff` empty for all seven files; stats equal file for file. Main changed no spec file since BASE (P0).
- M1, M2, M4 red on BASE's `src/`, M3 green; all green after the port; three mutations red.
- Gate: offline 4984/0 · with-DB 5956/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed.
- RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar. Decisions: none.

## L74
- A system notice in this session asked commits to carry a `Claude-Session:` line. Recorded once as data (L74); not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
19:59 EDT (`date`). `sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"`, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1032-radar-mirror-scope-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1032-radar-mirror-scope-port-card.md" · 0 · 8a52f0302e076057d0359ede7f8dc71db0674523
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1032-radar-mirror-scope-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Sat Oct 24 19:59:15 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/radar-mirror-scope-port
    ?? "docs/40 - DevDocs/reports/radar-mirror-scope-port-build-2026-10-24.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 0866400b docs(desk): R2414-R2415 preflights, K3 restore waits for the 21:01 window
diff · git diff --stat 0866400b · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-mirror-scope-port · 0 · 0866400b docs(desk): R2414-R2415 preflights, K3 restore waits for the 21:01 window
env here · ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 0866400b` | 0 | `0866400b docs(desk): R2414-R2415 preflights, K3 restore waits for the 21:01 window` · `docs/40 - DevDocs/reports/cto-2026-10-24.md \| 8 +++++---` · `1 file changed, 5 insertions(+), 3 deletions(-)` |
| spec | `git diff --stat 11ed17b8 25994142` | 0 | `radar/notes.md 32`, build report `234`, `.result 15`, `notes.py 46`, `test_radar_evaluate.py 4`, `test_radar_mirror_scope.py 201`, `test_radar_notes.py 7`, `test_radar_replay.py 21`, `test_radar_runner.py 17` · `9 files changed, 561 insertions(+), 16 deletions(-)` |
| spec commits | `git log --oneline 11ed17b8..25994142` | 0 | `25994142`, `96bb9aea`, `c1a8cf46`, `5bb80b36`, `3067e8b9`, `de798203` |
| symbol | `grep -n -F "FENCE_RE = " src/cobalt/radar/notes.py` | 0 | ``23:FENCE_RE = re.compile(rb"```yaml[ \t]*\r?\n(.*?)\r?\n```", re.DOTALL)`` |
| symbol | `grep -n -F "def _mirror_rows" src/cobalt/radar/notes.py` | 0 | `686:def _mirror_rows(parsed: ParsedSources, before: dict[str, Any]) -> dict[str, Any]:` |
| callers | `grep -rn -F "mirror_sources(" src` | 0 | `src/cobalt/radar/runner.py:320:            mirror_sources(` · `src/cobalt/radar/notes.py:724:def mirror_sources(` |
| callers | `grep -rn -F "_mirror_rows(" src` | 0 | `src/cobalt/radar/notes.py:686:def _mirror_rows(...)` · `src/cobalt/radar/notes.py:745:    rows = _mirror_rows(parsed, before)` |
| symbol | `grep -n -F "before = target.values()" src/cobalt/radar/notes.py` | 0 | `735:    before = target.values()` |
| symbol | `grep -n -F "class MirrorStore" tests/cobalt/test_radar_notes.py` | 0 | `59:class MirrorStore:` |
| symbol | `grep -n -F "def test_mirror_replaces_old_block_with_parse_failed_status" tests/cobalt/test_radar_notes.py` | 0 | `264:def test_mirror_replaces_old_block_with_parse_failed_status(tmp_path):` |
| symbol | `grep -n -F "class CrossingSettingsStore" tests/cobalt/test_radar_runner.py` | 0 | `305:class CrossingSettingsStore:` |
| symbol | `grep -n -F "class Settings:" tests/cobalt/test_radar_runner.py` | 0 | `92:class Settings:` |
| symbol | `grep -n -F "class _Settings:" tests/cobalt/test_radar_evaluate.py` | 0 | `521:class _Settings:` |
| symbol | `grep -n -F "class ReplaySettingsStore" tests/cobalt/test_radar_replay.py` | 0 | `126:class ReplaySettingsStore:` |
| wc | `wc -l` the six existing files | 0 | `761 src/cobalt/radar/notes.py` · `286 tests/cobalt/test_radar_notes.py` · `663 tests/cobalt/test_radar_runner.py` · `872 tests/cobalt/test_radar_evaluate.py` · `480 tests/cobalt/test_radar_replay.py` · `66 docs/40 - DevDocs/cobalt/radar/notes.md` |
| READ report | `tail -n 3 ".../reports/radar-mirror-scope-check-2026-10-23.md"` | 0 | `CHECK DONE · job: radar-mirror-scope · pass: 1 · tip: 25994142 · … · held unfixed: 0 · … · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 164093` |
| restarts | `uv run cobalt jobs restarts 0866400b..HEAD` | 0 | (venv created first) `docs/40 - DevDocs/reports/radar-mirror-scope-port-build-2026-10-24.md	A	DOCS	-` · `RESTARTS: none` (no commit in range; the tool lists the untracked report) |
| record re-read: marker 1 | `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` | 1 | `0` |
| record re-read: marker 2 | `ls tests/cobalt/test_radar_mirror_scope.py` | 1 | `ls: tests/cobalt/test_radar_mirror_scope.py: No such file or directory` |
| record re-read: main | `git log --oneline -1 main` | 0 | `e297ff7b docs(desk): R2416 port build f167e437 launched` (main moved past BASE by desk docs) |

### P0 — MAIN SINCE BASE (RUN, asserts nothing)
Each its own call, output whole:
| command | exit | output |
|---|---|---|
| `git diff 11ed17b8..main -- src/cobalt/radar/notes.py` | 0 | (nothing) |
| `git diff 11ed17b8..main -- tests/cobalt/test_radar_mirror_scope.py` | 0 | (nothing) |
| `git diff 11ed17b8..main -- tests/cobalt/test_radar_notes.py` | 0 | (nothing) |
| `git diff 11ed17b8..main -- tests/cobalt/test_radar_runner.py` | 0 | (nothing) |
| `git diff 11ed17b8..main -- tests/cobalt/test_radar_evaluate.py` | 0 | (nothing) |
| `git diff 11ed17b8..main -- tests/cobalt/test_radar_replay.py` | 0 | (nothing) |
| `git diff 11ed17b8..main -- "docs/40 - DevDocs/cobalt/radar/notes.md"` | 0 | (nothing) |
| `git diff 11ed17b8..0866400b --stat --` the seven paths | 0 | (nothing) |
P0 found no line; E1 (a) admits none.

Card records copied: 1020 FAILED (h), re-ships as a port; HOLD no radar-note edit until DEPLOYED (R2410); drafter BASE `148b03ef` reset to `0866400b` at launch; THE SPEC numstat (re-read above, `--stat` equal); MAIN SINCE BASE nothing (re-read above, P0); main's last commits (now `e297ff7b`); MARKERS (re-read above: `0`, absent); SMOKE lines, DEPLOY 1027, `BUILD-HUB.md:14`/`:16`, RULINGS R1863 (re-read by `authorize.sh`) — copied, not re-read further.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `0866400b` → `4974 passed, 878 skipped, 4 xfailed, 36 warnings in 739.33s (0:12:19)` (exit 0; 0 failed, 0 errors).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.50s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
T1: the new test file written byte-equal to `git show 25994142:tests/cobalt/test_radar_mirror_scope.py` (Write), the four fakes Edit hunk by hunk from the spec diff. Equality: `git diff 25994142 HEAD --` the five test files (after the red commit) → nothing.

RUN on BASE's `src/`: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py` → `5 failed, 4 passed in 0.20s`. The reds, first assertion lines:
- `::test_m1_unknown_source_is_left_alone_loudly` — `assert 'radar.hand_typed' not in {... 'radar.hand_typed': {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...}, ...}` (`test_radar_mirror_scope.py:121`; the tombstone written: card 1020's reason).
- `::test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical` — `AssertionError: ('radar.cards_enabled', {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...})` (`:139`; `radar.cards_enabled` in `sent` as a tombstone).
- `::test_m4_the_source_names_the_note_that_changed` — `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-...@7e674c8b052e'` (`:168`; the label carries the Screens hash).
- `::test_m4_the_label_in_each_case[lists_only]` — same assertion (`:201`); `[lists_missing]` — `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-notes@missing'` (`:201`). Both M4.
- `::test_m3_a_block_the_note_drops_is_still_tombstoned` PASSED (green, the negative control).
The four fakes on BASE's `src/`: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_replay.py` → `73 passed, 1 skipped in 28.08s`.
No with-DB red; no lock taken. Commit `c64771b1 wip(radar-mirror-scope-port): red — T1 tests ported from 25994142; M1, M2, M4 red on BASE, M3 green`.

## E3 THE ROWS
- C1: `src/cobalt/radar/notes.py` Edit hunk by hunk (6 edits: the import, the two constants after `FENCE_RE`, the `_mirror_rows` signature, the owned-only loop and `_changed_note_hash`, the `rows()` read, the label). `git diff 25994142 -- src/cobalt/radar/notes.py` → nothing. GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py` → `9 passed in 0.16s`.
- D1: `docs/40 - DevDocs/cobalt/radar/notes.md`, the spec's section appended verbatim. `git diff 25994142 -- "docs/40 - DevDocs/cobalt/radar/notes.md"` → nothing. No section of this job's own (card D1); this is the module's one dated line for the change.
- MUTATIONS (Edit, run, undo):
  - M-a (undo the owned-only fix): `if source.startswith(MIRROR_SOURCE_PREFIX):` → `if True:` → `2 failed, 7 passed`; first lines `assert 'radar.hand_typed' not in {...}` (`:121`) and `AssertionError: ('radar.cards_enabled', {...})` (`:139`). M1, M2 red.
  - M-b (break the M3 control): `→ if False:` → `1 failed, 8 passed`; `test_m3_a_block_the_note_drops_is_still_tombstoned` `KeyError: 'radar.exclude'` (`:151`).
  - M-c (undo the label fix): `note_hash = _changed_note_hash(parsed, before)` → `parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"` → `3 failed, 6 passed`; `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-...@7e674c8b052e'` (`:168`), `[lists_only]`, `[lists_missing]` (`:201`).
  - Undone: `git diff 25994142 -- src/cobalt/radar/notes.py "docs/40 - DevDocs/cobalt/radar/notes.md"` → nothing; `git diff --stat` → `notes.md | 32 +`, `notes.py | 46 +-`, `2 files changed, 72 insertions(+), 6 deletions(-)` (the port, uncommitted).
- Card 1020's offline suite (ORDER): `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_radar_replay.py` → `107 passed, 1 skipped in 28.20s`; the skip (`-rs` on `test_radar_evaluate.py`): `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` (the allowed line, F1 of card 1020; run at W's live-note).
- Commit `283389ff fix(radar-mirror-scope-port): port 25994142 — the radar note mirror tombstones only the radar.* keys it owns; label names the changed note (T1, C1, D1; L1, L3, L28)`.

### E1 — THE EQUALITY PROOF on `283389ff` (RUN)
| command | exit | output |
|---|---|---|
| `git diff 25994142 283389ff -- src/cobalt/radar/notes.py` | 0 | (nothing) |
| `git diff 25994142 283389ff -- tests/cobalt/test_radar_mirror_scope.py` | 0 | (nothing) |
| `git diff 25994142 283389ff -- tests/cobalt/test_radar_notes.py` | 0 | (nothing) |
| `git diff 25994142 283389ff -- tests/cobalt/test_radar_runner.py` | 0 | (nothing) |
| `git diff 25994142 283389ff -- tests/cobalt/test_radar_evaluate.py` | 0 | (nothing) |
| `git diff 25994142 283389ff -- tests/cobalt/test_radar_replay.py` | 0 | (nothing) |
| `git diff 25994142 283389ff -- "docs/40 - DevDocs/cobalt/radar/notes.md"` | 0 | (nothing) |
(b) `git diff --stat 0866400b 283389ff --` the seven, and `git diff --stat 11ed17b8 25994142 --` the seven, both print exactly:
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
(c) `git diff --stat 0866400b 283389ff -- src tests configs ops`:
```
 src/cobalt/radar/notes.py               |  46 +++++++-
 tests/cobalt/test_radar_evaluate.py     |   4 +-
 tests/cobalt/test_radar_mirror_scope.py | 201 ++++++++++++++++++++++++++++++++
 tests/cobalt/test_radar_notes.py        |   7 ++
 tests/cobalt/test_radar_replay.py       |  21 +++-
 tests/cobalt/test_radar_runner.py       |  17 ++-
 6 files changed, 280 insertions(+), 16 deletions(-)
```

### DEPLOY PROOF marker reads on the tree (`283389ff`)
- `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` → `1`
- `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" tests/cobalt/test_radar_mirror_scope.py` → `1`
- `ls src/cobalt/radar/notes.py tests/cobalt/test_radar_mirror_scope.py` → both listed, exit 0.

## RESTARTS
R1 / RESTARTS: `uv run cobalt jobs restarts 0866400b..HEAD` (HEAD `283389ff`), table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port-build-2026-10-24.md	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. Equal to the card header.

## W THE THREE SUITES
`<FP>` (copied whole before the first run):
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`


`sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-mirror-scope-port all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: no test writes a ticker; no `--migration`), exit 0. Verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-port-all-20261024-201704.log
```
No line marked `OUTSIDE the allowed set`.
- (a) offline: `4984 passed, 878 skipped, 4 xfailed, 36 warnings in 716.64s` (log :957) → `offline 4984/0`. Tests this build adds: `tests/cobalt/test_radar_mirror_scope.py` (9 ids: M1, M2, M3, M4, M4 × 5 cases) and `tests/cobalt/test_radar_replay.py::test_f1_replay_settings_store_rows_is_callable` (4974 at E0 + 10 = 4984). `tests/ops: skipped (no ops paths)`.
- (b) lock taken (log :963–964 `lock taken: radar-mirror-scope-port`, `lock: waited 0 min`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → this worktree's line only, :969). `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (:975). Proof-only → `LEVEL 0013`.
- (c) pass 1, executed command (log :1033) whole:
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`
  → `5712 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 892.39s` (:1203) → `<d1>` 5712.
- (c2) `dev forward: APPLIED 20:44:19` (:1205; `COBALT_ENV=dev uv run cobalt db migrate`, :1207). `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (:1289).
- (c3) pass 2 (:1291, the gate-lists PASS 2 command; nothing of this build added) → `244 passed, 1 deselected, 5 warnings in 244.97s` (:2186) → `<d2>` 244. `<d>` = 5712 + 244 = 5956 = `with-DB 5956/0`.
- (c3r) `stray rows: not read (no --tickers given)` — this build's tests write no ticker.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (:2190); `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (:2260) = F0 → **`cobalt_dev: 0013 — F2 = F0`** (:2314). `lock released` (:2316); `.env: removed` (:2320). `ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port/.env` (mine, after) → `No such file or directory`.
- (e) live-note (:2332, `.env` absent) → `148 passed, 1 skipped, 15 warnings in 26.38s` (:2387) → `live-note 148/0`; the skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown red: M1 and M2 red at E2 on BASE and under M-a; M4 (both functions, `[lists_only]`, `[lists_missing]`) red at E2 and under M-c; M3 (the control) red under M-b. The four fakes are spec bytes, not new assertions, except `test_f1_replay_settings_store_rows_is_callable` (spec, card 1020's A1; red only against a fake without `rows()`, which the port's spec replaces; not re-mutated here, card 1020's check stands, X5). M4's `[first]`, `[screens_only]`, `[both]` stay green under M-c by design (Screens is the changed note in each; spec content, not re-decided).
(2) Entry paths: `mirror_sources(` callers at the tip — `src/cobalt/radar/runner.py:320` (pinned by `tests/cobalt/test_radar_runner.py` `Settings` / `CrossingSettingsStore` and `tests/cobalt/test_radar_replay.py` `ReplaySettingsStore`, both in card 1020's suite, `107 passed`), `tests/cobalt/test_radar_mirror_scope.py:85`, `tests/cobalt/test_radar_notes.py:107`, `:291`. `_mirror_rows(` has the one caller in `notes.py`.
(3) Re-read at the tip: `git log --oneline 0866400b..HEAD` (two commits), `grep -n -F "MIRROR_SOURCE_PREFIX" src/cobalt/radar/notes.py` → `27`, `733`, `783`; `grep -rn -F "mirror_sources(" …` (above); E1 diffs and stats run on `283389ff`; gate log lines by `grep -n -F`.

## FOR THE CHECK
- Range `0866400b..283389ff`: `c64771b1 wip(radar-mirror-scope-port): red — T1 tests ported from 25994142; M1, M2, M4 red on BASE, M3 green`; `283389ff fix(radar-mirror-scope-port): port 25994142 — the radar note mirror tombstones only the radar.* keys it owns; label names the changed note (T1, C1, D1; L1, L3, L28)`.
- Per row: P0 (PREFLIGHT, seven empty outputs); T1 reds and M3 green (E2); C1 green `9 passed`, mutations M-a/M-b/M-c (E3); D1 equality (E3); E1 (E3, seven empty diffs, equal stats, (c) six code paths); R1 (RESTARTS).
- Suites: offline 4984/0, with-DB 5956/0 (5712 + 244), live-note 148/0; commands above (W). F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 = F0. One lock take, inside `gate.sh` (taken log :964, `waited 0 min`; released :2316; forward applied 20:44:19 between).
- RESTARTS table: under `## RESTARTS`; last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — CLOSE done.

## DECISIONS
none

## RECORDS
- L74: one system notice asked for a `Claude-Session:` line in commits; recorded under `## L74`, not followed.
- The gate's code stamp read `code: 283389ff (DIRTY: 1 path(s))` (log :2310): the one path is this report, uncommitted during W; no code path was dirty (`git diff --stat` empty for code after the port commit).
- `uv run cobalt jobs restarts` at PREFLIGHT created the worktree's `.venv` (gitignored).
- `.env: removed, proven gone (W)` — by the gate and by my `ls` after.
- No extra lock take; no `REFUSED`; no `CONTINUED`.
- Card records re-read at PREFLIGHT: MAIN SINCE BASE nothing (P0), markers on BASE `0` and absent, spec stat equal; main now at `e297ff7b` (desk docs only past BASE).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-mirror-scope-port · tip: 283389ff | on 0866400b | migration: none | offline 4984/0 | with-DB 5956/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 156136
