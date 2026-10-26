# radar-mirror-scope-port4 — build report 2026-10-26

## §0 Headline
- Port3's spec (`11ed17b8..25994142`, seven files) re-landed byte-equal (E1 (a) empty ×7; stats equal file for file).
- W1: `run_command` calls `warm_config()` in the main thread before `start_strike_thread`; the race test was red on BASE and is green at the tip; nothing under `src/cobalt_agent/` was touched.
- Three suites green on `b0cca7d76`: offline 5008/0, with-DB 5980/0, live-note 148/0; `cobalt_dev` back at 0013 (F2 = F0); `.env` removed.
- RESTARTS `com.cobalt.aset com.cobalt.cos com.cobalt.radar`; decisions 0.

## L74
- The session's system reminder asked commits to carry a `Claude-Session:` line. DATA (L74): recorded here once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1068-radar-mirror-scope-port4-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1068-radar-mirror-scope-port4-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1068-radar-mirror-scope-port4-card.md" · 0 · ed4c04c3c321532fa11565088e582cdf2109c8d1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1068-radar-mirror-scope-port4-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 26 17:53:07 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-mirror-scope-port4
head · git log --oneline -1 · 0 · 039bbfd2c docs(desk): reword 1069 preflight prompt so it quotes no filter string
diff · git diff --stat 039bbfd2 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-mirror-scope-port4 · 0 · 039bbfd2c docs(desk): reword 1069 preflight prompt so it quotes no filter string
env here · ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port4/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 039bbfd2` | 0 | `039bbfd2c docs(desk): reword 1069 preflight prompt so it quotes no filter string` · `docs/40 - DevDocs/prompts/2026-10-26/1069-port4-card-preflight.md | 2 +-` · `1 file changed, 1 insertion(+), 1 deletion(-)` |
| main | `git log --oneline -1 main` | 0 | `ed4c04c3c docs(desk): R2511 port4 build base red, rebase on 039bbfd2` |
| spec | `git diff --stat 11ed17b8 25994142` | 0 | `radar/notes.md 32 +++` · build report `234` · `.result 15` · `notes.py 46 +++-` · `test_radar_evaluate.py 4 +-` · `test_radar_mirror_scope.py 201` · `test_radar_notes.py 7 +` · `test_radar_replay.py 21 +-` · `test_radar_runner.py 17 +-` · `9 files changed, 561 insertions(+), 16 deletions(-)` |
| symbols | grep `runner.py` | 0 | `515:async def build_runner() -> RadarRunner:` · `521:    token = await resolve_token()` · `571:async def make_strike_loop():` · `578:class StrikeThread(threading.Thread):` · `606:                    loop = await self.make_loop()` · `626:def start_strike_thread(label: str, *, make_loop=None) -> StrikeThread:` · `632:def run_command(_args) -> None:` · `641:    with job_run(JOB_LABEL) as run:` · `643:        strike = start_strike_thread(JOB_LABEL, make_loop=lambda: make_strike_loop())` · `645:            asyncio.run(resident())` · `652:def scan_command(_args) -> None:` |
| callers | `grep -rn -F "run_command(" src` | 0 | `src/cobalt/radar/runner.py:632:def run_command(_args) -> None:`; Grep `run_command` in src: `src/cobalt/radar/cli.py:25:    run.set_defaults(func=runner.run_command)` |
| callers | `grep -rn -F "start_strike_thread(" src tests` | 0 | `runner.py:626` (def), `runner.py:643` (run_command), `tests/cobalt/test_radar_runner.py:570`, `:626` |
| config.py | `git show main:src/cobalt_agent/config.py` | 0 | `Config.__new__` sets `cls._instance` then `cls._instance._config = _load_config()`; `get_instance()` returns `Config._instance` when set; `load()` returns `self._config`; `get_config()` → `Config.get_instance().load()` (as the card's records) |
| test seams | Grep `tests/cobalt/test_radar_runner.py` | 0 | `511:def _resident(monkeypatch, loop, *, cycles, block_first_s):` · `535` build_runner · `536` load_tunables · `538` should_keep_running · `539` job_run · `540` make_strike_loop · `547`, `555` `r.run_command(None)` |
| wc | `wc -l` | 0 | notes.py 761 · runner.py 735 · conftest.py 442 · test_radar_notes.py 286 · test_radar_runner.py 663 · test_radar_evaluate.py 872 · test_radar_replay.py 480 · radar/notes.md 66 · radar/runner.md 39 |
| READ tail | `tail -n 3 …/deploy-radar-mirror-scope-port3.md` | 0 | `FAILED: smoke (b) — radar Traceback 1 vs baseline 0 (strike loop 'Config' object has no attribute '_config', logs/radar.err:103098) · rollback: used — … · decisions: 2 · for Dejan: 0 · tokens: 209870` |
| restarts | `uv run cobalt jobs restarts 039bbfd2..HEAD` | 0 | `docs/40 - DevDocs/reports/radar-mirror-scope-port4-build-2026-10-26.md	A	DOCS	-` · `RESTARTS: none` (only this report, uncommitted; no code path) |

P0 (RUN), MAIN SINCE BASE — each its own call, every output empty:
- `git diff 11ed17b8..main -- src/cobalt/radar/notes.py` → (nothing)
- `git diff 11ed17b8..main -- tests/cobalt/test_radar_mirror_scope.py` → (nothing)
- `git diff 11ed17b8..main -- tests/cobalt/test_radar_notes.py` → (nothing)
- `git diff 11ed17b8..main -- tests/cobalt/test_radar_runner.py` → (nothing)
- `git diff 11ed17b8..main -- tests/cobalt/test_radar_evaluate.py` → (nothing)
- `git diff 11ed17b8..main -- tests/cobalt/test_radar_replay.py` → (nothing)
- `git diff 11ed17b8..main -- "docs/40 - DevDocs/cobalt/radar/notes.md"` → (nothing)
- `git diff 11ed17b8..main -- src/cobalt/radar/runner.py "docs/40 - DevDocs/cobalt/radar/runner.md"` → (nothing)
- also against BASE: `git diff 11ed17b8..039bbfd2 --` all nine paths → (nothing)

Card records copied: see the card's `## RECORDS` (port3 smoke cause, HOLD, drafter, THE SPEC numstat, MAIN SINCE BASE, the `config.py`/`detector.py`/`collector.py`/`finviz_api.py`/`runner.py` line reads, the test seams, the deploy port3 lines, RULINGS R1863). Re-read here: the spec stat (above, matches), MAIN SINCE BASE (P0, matches), `config.py` singleton (matches), `runner.py` lines (matches), `_resident` seams (matches), the deploy port3 stop line (matches).

PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT; the rest per the BUILD-HUB table.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (on `039bbfd2`) → `4995 passed, 878 skipped, 4 xfailed, 36 warnings in 842.32s (0:14:02)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.63s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
T1 — the five test files written to the spec bytes (Write for the new file, Edit hunk by hunk for the four fakes). Proof after the red commit: `git diff 25994142 HEAD -- tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_replay.py` → (nothing).

`uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py` on BASE's `src/` → `FF.F..F.F` · `5 failed, 4 passed in 0.19s`:
- `::test_m1_unknown_source_is_left_alone_loudly` RED: `assert 'radar.hand_typed' not in {... 'radar.hand_typed': {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...}, ...}` (the tombstone row, `status: removed`, sent for the hand-typed key).
- `::test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical` RED: `AssertionError: ('radar.cards_enabled', {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...})` (`radar.cards_enabled` in `sent` as a tombstone).
- `::test_m4_the_source_names_the_note_that_changed` RED: `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-...@7e674c8b052e'` (the label carries the Screens hash, not the edited Lists hash).
- `::test_m4_the_label_in_each_case[lists_only]` RED (same label assertion); `::test_m4_the_label_in_each_case[lists_missing]` RED: `assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-notes@missing'`.
- `::test_m3_a_block_the_note_drops_is_still_tombstoned` GREEN (third `.`), and the `first`, `screens_only`, `both` label cases GREEN.

W1 — NEW `tests/cobalt/test_radar_config_warmup.py`. `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_config_warmup.py` on BASE's `src/` → `.FF` · `2 failed, 1 passed in 0.79s`:
- `::test_w1_a_cold_singleton_hands_a_second_thread_no_config` GREEN (the control: the fake reproduces `radar.err:103098`).
- `::test_w1_warm_config_builds_the_singleton_once_in_the_calling_thread` RED: `E       AttributeError: module 'cobalt.radar.runner' has no attribute 'warm_config'. Did you mean: 'load_config'?`
- `::test_w1_run_command_warms_config_before_the_strike_thread` RED: `E         Left contains one more item: ('MainThread', AttributeError("'Config' object has no attribute '_config'"))` (callers `['strike', 'MainThread']`).
- The test was revised once before this run, still in E2: the fake `cycle()` waits up to 2 s on an event the fake strike `make_strike_loop` sets, so the one resident cycle cannot end before the strike thread reads the config (no timing luck either way).

Commit `cb2554205 wip(radar-mirror-scope-port4): red — T1 spec tests ported, W1 warm-up tests` (6 files, test files only).

## E3 THE ROWS
Rows in card order: P0 (PREFLIGHT, above), T1 (E2), C1, D1, W1, E1, R1.

- C1: six Edit hunks bring `src/cobalt/radar/notes.py` to the spec (`from loguru import logger`; `MIRROR_SOURCE_PREFIX`, `FOREIGN_SOURCE_PREFIXES`; `_mirror_rows(parsed, before, owners)` with the owned-only tombstone and the unknown-source warning; `_changed_note_hash`; `stored = target.rows()`; the label). `git diff 25994142 -- src/cobalt/radar/notes.py` → (nothing). `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py` → `25 passed in 0.40s`.
- D1: the spec's section `## 2026-10-23 — radar-mirror-scope` appended to `docs/40 - DevDocs/cobalt/radar/notes.md`. `git diff 25994142 -- "docs/40 - DevDocs/cobalt/radar/notes.md"` → (nothing). No section of this job's own.
- W1: `src/cobalt/radar/runner.py` gains `def warm_config() -> None` (`:632`) and the call `warm_config()` (`:650`), on the line before `strike = start_strike_thread(...)`; `tests/cobalt/conftest.py` gains the autouse fixture `radar_warm_config_noop` (no-op outside `test_radar_config_warmup.py`); `docs/40 - DevDocs/cobalt/radar/runner.md` gains `## 2026-10-26 — radar-mirror-scope-port4`. Nothing under `src/cobalt_agent/` was needed. `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_config_warmup.py tests/cobalt/test_radar_runner.py` → `23 passed in 20.93s`.
- ORDER suite: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_radar_replay.py tests/cobalt/test_radar_config_warmup.py` → `110 passed, 1 skipped in 29.30s`; `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` (run at W (e)).

THE MUTATIONS (each made with Edit, run alone, undone with Edit):
| row | mutation | run | result |
|---|---|---|---|
| C1 ownership | `notes.py` `if source.startswith(MIRROR_SOURCE_PREFIX):` → `if True:` | `--tb=line tests/cobalt/test_radar_mirror_scope.py` | `2 failed, 7 passed`: `FAILED ::test_m1_unknown_source_is_left_alone_loudly`, `FAILED ::test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical`; first line `E   AssertionError: {'block': None, 'block_sha256': None, 'error': None, 'note_sha256': None, ...}` |
| C1 label | `note_hash = _changed_note_hash(parsed, before)` → `parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"` | same | `3 failed, 6 passed`: `FAILED ::test_m4_the_source_names_the_note_that_changed`, `::test_m4_the_label_in_each_case[lists_only]`, `[lists_missing]`; first line `E   AssertionError: assert 'vault:radar-...@33a77dc6c179' == 'vault:radar-...@7e674c8b052e'` |
| W1 call | `warm_config()` line removed from `run_command` | `--tb=line tests/cobalt/test_radar_config_warmup.py` | `1 failed, 2 passed`: `FAILED ::test_w1_run_command_warms_config_before_the_strike_thread`; `E   assert [('MainThread... '_config'"))] == []` |
| W1 control (negative) | the fake `__new__` sets `_config` before `_instance` | same | `1 failed, 2 passed`: `FAILED ::test_w1_a_cold_singleton_hands_a_second_thread_no_config`; `E   assert (0 == 1)` |
| W1 seam | conftest name check `"test_radar_config_warmup.py"` → `"test_radar_config_warmup.MUTATED"` (W1's own file gets the no-op) | same | `2 failed, 1 passed`: `FAILED ::test_w1_warm_config_builds_the_singleton_once_in_the_calling_thread` (`E   AssertionError: assert [] == ['MainThread']`), `FAILED ::test_w1_run_command_warms_config_before_the_strike_thread` |
After the undo: `git diff --stat` → the five fix files only (`notes.md 32`, `runner.md 3`, `notes.py 46`, `runner.py 8`, `conftest.py 20`), and `git diff 25994142 --` the seven spec paths → (nothing).

Commit `b0cca7d76 fix(radar-mirror-scope-port4): re-land the mirror scope; warm Config before the strike thread (T1, C1, D1, W1; L1, L3, L72)`.

E1 (RUN), on `<tip>` = `b0cca7d76`:
- (a) `git diff 25994142 b0cca7d76 -- <path>`, one call each, for `src/cobalt/radar/notes.py`, `tests/cobalt/test_radar_mirror_scope.py`, `tests/cobalt/test_radar_notes.py`, `tests/cobalt/test_radar_runner.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_replay.py`, `docs/40 - DevDocs/cobalt/radar/notes.md` → (nothing) ×7. P0 found no main line, so none is admitted.
- (b) `git diff --stat 039bbfd2 b0cca7d76 --` the seven → `radar/notes.md 32` · `notes.py 46` · `test_radar_evaluate.py 4` · `test_radar_mirror_scope.py 201` · `test_radar_notes.py 7` · `test_radar_replay.py 21` · `test_radar_runner.py 17` · `7 files changed, 312 insertions(+), 16 deletions(-)`; `git diff --stat 11ed17b8 25994142 --` the seven → the same seven lines, `7 files changed, 312 insertions(+), 16 deletions(-)`. Equal file for file.
- (c) `git diff --stat 039bbfd2 b0cca7d76 -- src tests configs ops` → `src/cobalt/radar/notes.py 46` · `src/cobalt/radar/runner.py 8` · `tests/cobalt/conftest.py 20` · `tests/cobalt/test_radar_config_warmup.py 145` · `tests/cobalt/test_radar_evaluate.py 4` · `tests/cobalt/test_radar_mirror_scope.py 201` · `tests/cobalt/test_radar_notes.py 7` · `tests/cobalt/test_radar_replay.py 21` · `tests/cobalt/test_radar_runner.py 17` · `9 files changed, 453 insertions(+), 16 deletions(-)`: `notes.py`, the five test files and W1's three.
- (d) `git diff 039bbfd2 b0cca7d76 -- src/cobalt/radar/runner.py tests/cobalt/conftest.py "docs/40 - DevDocs/cobalt/radar/runner.md"` → only `+def warm_config() -> None:` (docstring, `from cobalt_agent.config import Config`, `Config.get_instance()`), `+        warm_config()` before `strike = start_strike_thread(...)`, the fixture `radar_warm_config_noop`, and the section `## 2026-10-26 — radar-mirror-scope-port4` (the whole diff is in `## FOR THE CHECK`).
- (e) `git diff --stat 039bbfd2 b0cca7d76 -- src/cobalt_agent` → (nothing).

DEPLOY PROOF marker reads on the tree (worktree paths): `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` → `1`; `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" tests/cobalt/test_radar_mirror_scope.py` → `1`; `grep -c -F "def warm_config" src/cobalt/radar/runner.py` → `1`; `ls src/cobalt/radar/notes.py tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_config_warmup.py` → all three listed, exit 0.

## RESTARTS
R1 (RUN) `uv run cobalt jobs restarts 039bbfd2..HEAD` (HEAD = `b0cca7d76`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-port4-build-2026-10-26.md	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_config_warmup.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. The last line equals the card header's `RESTARTS`.

## W THE THREE SUITES
`<tip>` = `b0cca7d76`. `<FP>` (copied whole): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

`sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-mirror-scope-port4 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`; no `--migration`) → exit 0. Verdict lines, whole:
```
tests/ops: skipped (no ops paths)
offline 5008/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5980/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-port4-all-20261026-181324.log
```
- (a) offline: log `:957` `5008 passed, 878 skipped, 4 xfailed, 36 warnings in 819.75s (0:13:39)` → `offline 5008/0`. Tests this build adds: `tests/cobalt/test_radar_mirror_scope.py` (9), `tests/cobalt/test_radar_config_warmup.py` (3), `tests/cobalt/test_radar_replay.py::test_f1_replay_settings_store_rows_is_callable` (1). `tests/ops: skipped (no ops paths)`.
- (b) log `:963-964` `lock taken: radar-mirror-scope-port4`, `:969` the one `.env` line (this worktree's); `:975` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `LEVEL 0013`. `grep -n -F "OUTSIDE"` on the log → no line.
- (c) pass 1, log `:1033`: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py` → `:1203` `5736 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 993.99s (0:16:33)` → `<d1>` = 5736.
- (c2) `:1205` **`dev forward: APPLIED 18:44:04`** (the standing gate-list migrations above `0013`; none of this build); `:1289` `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2 → `:2186` `244 passed, 1 deselected, 5 warnings in 246.73s (0:04:06)` → `<d2>` = 244; `<d>` = 5736 + 244 = 5980 = `with-DB 5980/0`. This build adds no with-DB test id.
- (c3r) `stray rows: not read (no --tickers given)`: this build's tests write no ticker.
- (f) `:2260` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`**; `:2315-2316` `release-devdb-lock.sh radar-mirror-scope-port4` → `lock released`; `.env: removed`. `ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port4/.env` → `No such file or directory`. Record: `.env: removed, proven gone (W)`.
- (e) `:2387` `148 passed, 1 skipped, 15 warnings in 26.46s` → `live-note 148/0`; its skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED: M1, M2, M4 (+ the `lists_only`, `lists_missing` label cases) RED on BASE's `src/` (E2) and RED again under the C1 ownership / label mutations (E3); M3 GREEN on BASE (the named control). W1: `::test_w1_warm_config_builds…` RED on BASE (`AttributeError … 'warm_config'`) and under the seam mutation; `::test_w1_run_command_warms…` RED on BASE (`('MainThread', AttributeError("'Config' object has no attribute '_config'"))`) and under the call-removal mutation; the control `::test_w1_a_cold_singleton…` GREEN on BASE and RED under the `__new__`-order mutation (`assert (0 == 1)`). The four fakes and `test_f1_replay_settings_store_rows_is_callable` are spec bytes (T1), not new behaviour of this job; their reds stand in cards 1020/1032. No test stayed green under its mutation.
(2) Entry paths: `run_command` is reached from `src/cobalt/radar/cli.py:25` (`run.set_defaults(func=runner.run_command)`) only (Grep `run_command` in `src`); `::test_w1_run_command_warms…` calls `r.run_command(None)`, the same function. `warm_config` has one call (`grep -n -F "warm_config()" src/cobalt/radar/runner.py` → `:632` def, `:650` call). `start_strike_thread` callers: `runner.py:643` (now `:651`, after `warm_config()`), and the tests `test_radar_runner.py:570`, `:626` (direct, no `run_command`: they need no warm-up). `scan_command` and replay start no strike thread and call no `warm_config` (E1 (d), the whole runner diff). `mirror_sources` callers are card 1020's, not re-opened (X6).
(3) Re-read at the tip: `git log --oneline 039bbfd2..HEAD` → the two commits; `grep -n -F "MIRROR_SOURCE_PREFIX" src/cobalt/radar/notes.py` → `:27`, `:733`, `:783`; `grep -n -F "def radar_warm_config_noop" tests/cobalt/conftest.py` → `:414`; `grep -n -F "warm_config()" src/cobalt/radar/runner.py` → `:632`, `:650`; E1 (a)–(e) run on `b0cca7d76`; the gate log lines quoted with `grep -n -F`.

## FOR THE CHECK
- Range `039bbfd2..b0cca7d76`: `cb2554205 wip(radar-mirror-scope-port4): red — T1 spec tests ported, W1 warm-up tests` · `b0cca7d76 fix(radar-mirror-scope-port4): re-land the mirror scope; warm Config before the strike thread (T1, C1, D1, W1; L1, L3, L72)`.
- Per row: reds in `## E2 RED`; mutations and greens in `## E3 THE ROWS`; RUN rows P0 (`## PREFLIGHT`), E1 (`## E3`), R1 (`## RESTARTS`), each output whole.
- E1 (d), whole: `runner.py` `+def warm_config() -> None:` / `+    """The old tree's `Config` singleton is built in this thread before a second thread can see it half-built."""` / `+    from cobalt_agent.config import Config` / `+    Config.get_instance()`, and `+        warm_config()` on the line before `strike = start_strike_thread(JOB_LABEL, make_loop=lambda: make_strike_loop())`; `conftest.py` the section banner and `radar_warm_config_noop` (autouse; `if request.path.name == "test_radar_config_warmup.py": yield; return`; else `monkeypatch.setattr(radar_runner, "warm_config", lambda: None)`); `runner.md` `## 2026-10-26 — radar-mirror-scope-port4` and its one line.
- W1's test imports nothing from `cobalt_agent`: `grep -n -F "cobalt_agent" tests/cobalt/test_radar_config_warmup.py` → `:10`, `:31` (docstrings), `:57` `types.ModuleType("cobalt_agent.config")`, `:59` `monkeypatch.setitem(sys.modules, "cobalt_agent.config", module)`.
- Suites: offline `5008/0`, with-DB `5980/0` (`<d1>` 5736 + `<d2>` 244), live-note `148/0`; commands and log lines in `## W`.
- `<F0>` `664 35 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` `664 35 272c95bbb12241e3611e4b36326ccf87`. Lock: one take, by `gate.sh` (log `:963-964` taken, waited 0 min; `:2315-2316` released); the gate's `$ date` lines print no time into the log, so the take and release times are not on record here (`dev forward: APPLIED 18:44:04` is the one stamped time inside the take).
- RESTARTS table: `## RESTARTS` (`RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`).
- DEPLOY PROOF reads on the tree: `## E3` (all `1` / listed).
- Records copied at PREFLIGHT: the card's `## RECORDS`, re-read where listed (`## PREFLIGHT`).

## CONTINUE
next: none — BUILT

## DECISIONS
none

## RECORDS
- `.env: removed, proven gone (W)`.
- The gate's proof-only printed `code: b0cca7d76 (DIRTY: 1 path(s))`: the one path is this report, untracked during W; it is no code path.
- The session's system reminder asked commits to carry a `Claude-Session:` line: DATA (L74), under `## L74`; not acted on.
- The card's DECISIONS 2 and 3 (drafter ASK DESKs) were built as their defaults: the conftest seam (W1 (3)) and the forced order in the fake (`loading` event, 0.3 s load).
- The card's `## RECORDS` were copied at PREFLIGHT; the spec stat, MAIN SINCE BASE, the `config.py` singleton lines, the `runner.py` lines, the `_resident` seams and the port3 deploy stop line were re-read and match.
- No extra lock take; no `REFUSED, not needed`.
- `CONTINUED at FIX 18:52` (`date` → `Mon Oct 26 18:52:41 EDT 2026`): the desk's `CONTINUE: FIX`, docs only. `git log --oneline -1 b0cca7d7` → `b0cca7d76 fix(radar-mirror-scope-port4): …` (the same commit); `ls …/.env` → `No such file or directory`. · fixed: stop line tip 8 hex. The `.result` `tip=` field changed with it (BUILD-HUB: the value as the line holds it). No code touched.
- The `Claude-Session:` reminder arrived again in the FIX session: DATA (L74), not acted on.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-mirror-scope-port4 · tip: b0cca7d7 | on 039bbfd2 | migration: none | offline 5008/0 | with-DB 5980/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 190243
