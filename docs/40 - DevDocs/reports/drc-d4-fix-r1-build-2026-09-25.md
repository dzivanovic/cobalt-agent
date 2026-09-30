# DRC D4 FIX R1 BUILD — 2026-09-25

## §0 Headline
DRC D4 fix r1 BUILT on `5d4f8201` → tip `e96f0be7`: the card apply now writes through `apply_settings` (F-1, L3). The settings log line carries no digest (F-8, L32). Pins F-2…F-6 each have a negative control. F-7 lines are below.
Red `36331949` hit exactly the 3 named tests; the fix `807c13ec` is green. Offline 2520/0 · with-DB 2980/0 (+ probe short by 4) · live-note 142/0 · `.env` removed.
RUNS: RUN-1 GREEN (the store joins the rollback). RUN-2 GREEN (0 log messages on a refused change). RUN-3: 1 committed docs file carries the old literal (ESCALATE 4).
ESCALATE: 15.

## L74
ONE block arrived, appended to the Read tool result of this prompt file (`21-drc-d4-fix-r1-build.md`, first page): a `system-reminder` asking every commit message to end with a `Claude-Session: https://claude.ai/code/session_…` line and naming a file-send tool (`SendUserFile`). Recorded as DATA; NOT followed — every commit of this run carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and nothing else; no file was sent.

## AUTHORIZATION
Started `date` → `Fri Sep 25 07:23:39 EDT 2026` (`<D>` = 2026-09-25).

| gate | command | result |
|---|---|---|
| placeholder R__ | `grep -n -E "R_[_]" …/21-drc-d4-fix-r1-build.md` | no output (exit 1) — PASS |
| placeholder FILL AT LAUNCH | `grep -n -F "FILL AT LAUNCH" …/21-drc-d4-fix-r1-build.md` | hits on line 1 (desk prose) and line 28 (the gate's own line) ONLY — PASS |
| `06` stop | `tail -n 3 …/drc-d4-check-2026-09-25.md` | last non-blank `DRC D4 CHECK DONE · round: 1 · … · defects that HOLD: 12 · ready for D2: NO · ESCALATE: 12` — PASS |
| `06` committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/drc-d4-check-2026-09-25.md` | `a1f0c2b58c28bb92b088082a3506f38c10ae38d0` — PASS |
| classification | `tail -n 3 …/drc-d4-fix-r1-draft-2026-09-25.md` | last non-blank `DRC D4 FIX R1 DRAFTED · FIX: 10 · NOT REAL: 10 · UNPROVEN: 3 · OUT OF SCOPE: 5 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 6` — PASS |
| classification committed | `git -C … log -1 --format=%H -- …/drc-d4-fix-r1-draft-2026-09-25.md` | `5c1eaed8cee28c27bdf37ebe07ea65b18fd6d6b7` — PASS |
| `.env` pair his | `grep -n -F "Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)" …/cto-2026-09-24.md` | `:40` `\| R22 \| 07:56 ET \| His words: "approved. A for now. …` — PASS |
| R22 committed | `git -C … log -1 --format=%H -S"approved. A for now" -- …/cto-2026-09-24.md` | `813a4dfa27ace0faede64584d45932169345db9e` — PASS |
| launch row | `grep -n "21-drc-d4-fix-r1-build.md" …/cto-2026-09-25.md` | `:39` `\| R31 \|` (not counted) and `:46` `\| R38 \| 07:22 ET \| … DESK LAUNCH ROW for prompts/2026-09-25/21-drc-d4-fix-r1-build.md …` — PASS |
| launch row committed | `git -C … log -1 --format=%H -S"21-drc-d4-fix-r1-build.md" -- "…/cto-2026-09-2*.md"` | `9f8d458f32b7b7ec68ea8f46258826f0b5d053f6` — PASS |

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| date | `date` | 0 | `Fri Sep 25 07:23:39 EDT 2026` |
| clean tree | `git status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git log --oneline -3` | 0 | `8b6518a8 docs(drc-d4): DRC D4 build report — 5d4f8201` · `facdfc93 wip(drc-d4): DRC D4 build report — FAILED at E7 (E3 fixture), fix 5d4f8201 unproven` · `5d4f8201 wip(drc-d4): E3 fixture writes a coherent constructed sheet + day-mode set (E7 red cause; with-DB unproven)` |
| code unmoved | `git diff --stat 5d4f8201 8b6518a8 -- . ':(exclude)docs'` | 0 | (empty) — `<base>` = `5d4f8201` |
| no .env | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |
| lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live strategies | `ls ".../1 - Trading/4 - Strategies"` | 0 | listed, 22 notes |
| requires_vault | `grep -rln "requires_vault" tests` | 0 | `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_replay_line.py`, `tests/taxonomy/test_predicate.py`, `tests/taxonomy/test_catalyst.py` — the expected set |
| card put | `grep -n -F "store.put(" src/cobalt/settings/card.py` | 0 | `323:    outcome = store.put(new_rows, source=f"card:{path.name}@sha256:{digest}", delete=deletes)` |
| card gate | `grep -n -F "assert_writable(" src/cobalt/settings/card.py` | 0 | `322:    assert_writable("settings.load.card", target='"user".trader_settings')` |
| cli docstring | `grep -n "Every apply goes through" src/cobalt/settings/cli.py` | 0 | `10:Every apply goes through \`apply_settings\` — the one write function the` |
| cli log | `grep -n "settings applied: keys" src/cobalt/settings/cli.py` | 0 | `107:        "settings applied: keys {} · deleted {} · sha256 {} · source {} · at {}",` |
| cli digest | `grep -n "digest = payload_sha256(rows)" src/cobalt/settings/cli.py` | 0 | `95:    digest = payload_sha256(rows)` |
| web docstring | `grep -n "the one log line (keys + hash + time" src/cobalt/aset/web.py` | 0 | `1268:    the one log line (keys + hash + time, never values)."""` — LINE MOVED (expected 1270) |
| card test patches | `grep -n -F "monkeypatch.setattr(card_mod, " tests/cobalt/test_card_settings.py` | 0 | `160`, `171`, `172` (assert_writable), `187`, `188` (assert_writable) |
| X12 test | `grep -n "def test_x12_size_still_sizes_without_drc_keys" …db.py` | 0 | `74:` |
| E3 test | `grep -n "def test_e3_a_two_key_apply_with_one_bad_key_writes_neither" …db.py` | 0 | `251:` |
| F-5 test | `grep -n "def test_each_drc_key_validates_a_good_constructed_value" …` | 0 | `153:` |
| F-4 test | `grep -n "def test_one_reader_of_the_daily_stop_and_the_grade_dollars" …` | 0 | `241:` |
| F-6 test | `grep -n "def test_saved_only_after_the_read_back_equals_the_payload" …` | 0 | `464:` |
| F-8 test | `grep -n "def test_no_log_line_carries_a_value" …` | 0 | `472:` |
| dev_db_tx | `grep -n "def dev_db_tx" tests/cobalt/conftest.py` | 0 | `134:` |
| _failed | `grep -n "def _failed" src/cobalt/aset/web.py` | 0 | `745:` |
| restarts | `uv run cobalt jobs restarts 5d4f8201..HEAD` | 0 | `docs/40 - DevDocs/reports/drc-d4-build-2026-09-25.md	M	DOCS	-` · `RESTARTS: none` |

## F1 BASELINE
On `8b6518a8` (= `5d4f8201`'s code).

| leg | command | summary verbatim |
|---|---|---|
| offline | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` | `2516 passed, 467 skipped, 1 xfailed, 15 warnings in 69.49s (0:01:09)` → `<bp>` = 2516, `<bf>` = 0 |
| live-note | `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` | `142 passed, 1 skipped, 15 warnings in 9.84s` → `<blp>` = 142, `<blf>` = 0 |

Live-note SKIPPED lines: ONLY `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (the known one); NONE naming `COBALT_LIVE_VAULT_ROOT`. The with-DB baseline is `05`'s E7 record `2973/0`.

## F2 RED (offline)
New `tests/cobalt/test_drc_d4_fix_r1.py` (F-1: 2 tests; harness by import from `test_card_settings.py`). Named edits in `tests/cobalt/test_drc_settings.py`: F-4 (`_second_readers` helper + NEW negative control `test_the_one_reader_walk_flags_a_second_reader`; `:258`/`:259` count assertions kept byte for byte), F-5 (third `typed` column; accessor `DrcKey.validate` `src/cobalt/settings/models.py:199`; `DrcKey.from_rows(...).row()` models.py:212 — `_DrcLeaf` has no `__eq__`, so the round trip is asserted as `from_rows({key: row}).row() == row` and `validate(row) == typed`), F-6 (two assertions after `:469`), F-8 (`_leaks` helper; grade figure `"61"` → `"7061"` (constructed, L69), stop `"31337"` kept; THE NAMED REVERSAL `assert sha in` → `assert sha not in`; the per-message `"31337" not in m` loop now runs through `_leaks(m, (stop, grade)) == []`, which includes the stop figure; the two figures are held in local names `stop` / `grade`).

Run: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_drc_settings.py tests/cobalt/test_card_settings.py` → `3 failed, 68 passed, 1 skipped in 0.38s`. The three failures, EXACTLY the named rows:
- `test_the_card_apply_writes_through_the_one_apply_function` — `AssertionError: the card apply bypassed apply_settings: []` / `assert 0 == 1` (`test_drc_d4_fix_r1.py:46`)
- `test_the_settings_package_has_one_caller_of_put` — `AssertionError: a second caller of .put( in settings/: ['card.py']` / `assert {'card.py', 'cli.py'} == {'cli.py'}` (`:68`)
- `test_no_log_line_carries_a_value` — `AssertionError: assert '2538de05a8b...6cda5399524b' not in 'settings ap...6:28+00:00\n'` (`test_drc_settings.py:560`; the reversal; the `_leaks` negative controls above it passed)

PINS GREEN on the base (in the 68 passed): F-4 `test_one_reader_of_the_daily_stop_and_the_grade_dollars` and its negative control `test_the_one_reader_walk_flags_a_second_reader`; F-5 the 12 `test_each_drc_key_validates_a_good_constructed_value` rows; F-6 `test_saved_only_after_the_read_back_equals_the_payload`. The 1 skip = `test_card_settings.py`'s with-DB test.
Commit `<red>` = `36331949` `wip(d4-fix-r1): DRC D4 fix r1 red tests, offline — …`.

## F3 PINS (with-DB)
Named edits of `tests/cobalt/test_drc_settings_db.py`: the ONE helper `_write_constructed_set(store, *, b_full="60")` (the coherent sheet + day-mode set `change_page` wrote inline; `change_page` now calls it with the default — same order: store, `_clear_drc_rows()`, cfg, the put); F-2 (X12: `load_sheet_modes_config` patch REMOVED; `_write_constructed_set(TraderSettingsStore(), b_full="73")` then `_clear_drc_rows()`; before the POST, UNPATCHED `web_module.load_sheet_modes_config()` → `full.B == Decimal("73")` AND `!= _offline_sheet_modes_config().sheets["full"].B` (offline full.B = 2, `test_aset_web.py:44`) — the negative control; `_daymode_state` stays patched — the day's attestation row is not X12's input; POST + `:125`–`:127` assertions byte for byte; docstring sentence added); F-3 NEW `test_e3_a_failure_inside_the_one_put_writes_neither_key` (valid two-key change: stop `31337`, full.B `67`; `TraderSettingsStore.put` wrapped to pass a raising `before_commit` while a flag is set → FAILED + `constructed failure`, `store.rows() == before`; NEGATIVE CONTROL flag cleared, same post → `Settings saved`, both constructed keys read back); `test_e3_a_two_key_apply_with_one_bad_key_writes_neither` body byte for byte + the one docstring sentence (as dictated; NOTE: at `drc.py:258` stands `if errors:`, the raise is `:259`).

THE LOCK, first take: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`; (b) `cp …` → exit 0; `ls -la …` → ONE line `-rw-------  1 cobalt  staff  2186 Sep 25 07:27 /Users/cobalt/cobalt-wt/drc-d1/.env`; (c) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_settings_db.py` → `7 passed in 0.43s` — every test PASSED, none SKIPPED (the 7: `test_e10_a_new_drc_key_lands_without_a_migration`, `test_x12_size_still_sizes_without_drc_keys` (F-2 PIN + negative control), `test_x12_every_drc_field_is_none_without_rows`, `test_e3_a_good_apply_writes_through_the_store_and_reads_back`, `test_e3_an_apply_inside_market_reset_writes_nothing`, `test_e3_a_two_key_apply_with_one_bad_key_writes_neither`, `test_e3_a_failure_inside_the_one_put_writes_neither_key` (F-3 PIN + negative control)); (d) `rm …` exit 0; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. `.env: removed, proven gone (F3)`.
Commit `d523bba5` `wip(d4-fix-r1): DRC D4 fix r1 with-DB pins — …`.

## F4 THE EDITS
- **F-1** `src/cobalt/settings/card.py` `cmd_load_card`: `assert_writable(...)` + `store.put(...)` REPLACED by `settings_cli.apply_settings(new_rows, source=f"card:{path.name}@sha256:{digest}", actor="settings.load.card", store=store, delete=deletes)` with `from . import cli as settings_cli` inside the function. The `applied:` print and the `CardSettings.from_rows(store.values()) != incoming` round trip STAY byte for byte. `grep -n "assert_writable" src/cobalt/settings/card.py` after the call edit → ONLY `58:from cobalt.session import assert_writable` (the import) → import REMOVED. `src/cobalt/settings/cli.py` module docstring `:10`–`:11` → the dictated sentence; ALSO `apply_settings`' first docstring line (`:79`–`:81` at base, the other half of HOLD 1's cite `cli.py:79–:81`) now names "every `cobalt settings load --apply` form (--card included, D4 fix r1 F-1)".
- **F-8** `cli.py` `apply_settings`: `digest = payload_sha256(rows)` REMOVED; the log call is `"settings applied: keys {} · deleted {} · source {} · at {}", sorted(rows), delete, source.split("@sha256:", 1)[0], datetime.now(timezone.utc).isoformat(timespec="seconds")`; docstring trace sentences = AMENDED D4-4 TRACE's words. `grep -n "digest" src/cobalt/settings/cli.py` BEFORE: `68` (hexdigest in `payload_sha256`), `95` (`digest = payload_sha256(rows)`), `108` (the log args), `160`/`165`/`167`/`170` (`load_optional_file`'s own file-bytes digest); AFTER: `73` (hexdigest), `94` (docstring "never a digest of one"), `167`/`172`/`174`/`177` (`load_optional_file`) — nothing in `apply_settings` reads a digest. `src/cobalt/aset/web.py` `settings_daily_apply` docstring `:1268` → `the one log line (keys, source kind and time — never a value or a digest of one)`. Nothing else in `web.py`.
- **THE ONE NAMED SETUP CHANGE (F-1; NOT an assertion change):** `tests/cobalt/test_card_settings.py:172`, `:188` retargeted `card_mod` → `settings_cli` for `assert_writable`; `from cobalt.settings import cli as settings_cli` added to the imports. Every assertion of both tests byte for byte.
- **DevDocs:** `docs/40 - DevDocs/cobalt/settings/card.md` (write-path step 4 → `apply_settings`, F-1), `docs/40 - DevDocs/cobalt/settings/cli.md` (the log line's shape, F-8; the caller list incl. `cmd_load_card` + the radar mirror, F-1). `grep -n "hash" "docs/40 - DevDocs/cobalt/aset/web.md"` → `:252` (the review page's Apply form posts the hash), `:257` (the row `source`) — neither says the LOG carries a hash → `web.md` NOT edited.

Proofs:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_drc_settings.py tests/cobalt/test_card_settings.py tests/cobalt/test_settings_optional.py tests/cobalt/test_trader_settings.py tests/cobalt/test_aset_web.py` → `119 passed, 17 skipped in 0.56s` — **0 failed**; every named file exists.
- `git diff --stat 5d4f8201` → `docs/40 - DevDocs/cobalt/settings/card.md`, `docs/40 - DevDocs/cobalt/settings/cli.md`, `docs/40 - DevDocs/reports/drc-d4-build-2026-09-25.md` (the D4 report, `facdfc93`/`8b6518a8`, not mine), `src/cobalt/aset/web.py` (2 ±, docstring), `src/cobalt/settings/card.py`, `src/cobalt/settings/cli.py`, `tests/cobalt/test_card_settings.py`, `tests/cobalt/test_drc_d4_fix_r1.py`, `tests/cobalt/test_drc_settings.py`, `tests/cobalt/test_drc_settings_db.py` — `10 files changed, 336 insertions(+), 76 deletions(-)`; no other path.
- `git diff 5d4f8201 -- src` → quoted in the F4 box below.
- `git diff 5d4f8201 -- src/cobalt/db_migrations configs src/cobalt/cli.py src/cobalt/drc src/cobalt/aset/engine.py src/cobalt/settings/store.py src/cobalt/settings/models.py src/cobalt/settings/drc.py src/cobalt/prefill src/cobalt/radar src/cobalt/cards` → EMPTY.
- `grep -n -F "store.put(" src/cobalt/settings/card.py` → EMPTY. `grep -rn -F ".put(" src/cobalt/settings` → ONE hit `src/cobalt/settings/cli.py:104:    outcome = store.put(rows, source=source, **extra)` (inside `apply_settings`). `grep -n "sha256 {}" src/cobalt/settings/cli.py` → EMPTY. `grep -rn "VaultWriter" src/cobalt/settings` → EMPTY.
- Commit `<fix>` = `807c13ec` `fix(drc): D4 fix r1 — the card apply through the one apply, no digest in the settings log line (L3 / L32, L75, 09-25)`.

`git diff 5d4f8201 -- src` (whole):
```
diff --git a/src/cobalt/aset/web.py b/src/cobalt/aset/web.py
@@ -1265,7 +1265,7 @@ async def settings_daily_apply(request: Request) -> str:
-    the one log line (keys + hash + time, never values)."""
+    the one log line (keys, source kind and time — never a value or a digest of one)."""
diff --git a/src/cobalt/settings/card.py b/src/cobalt/settings/card.py
@@ -55,8 +55,6 @@
-from cobalt.session import assert_writable
-
@@ -319,8 +317,15 @@ def cmd_load_card(args: argparse.Namespace) -> None:
-    assert_writable("settings.load.card", target='"user".trader_settings')
-    outcome = store.put(new_rows, source=f"card:{path.name}@sha256:{digest}", delete=deletes)
+    from . import cli as settings_cli
+
+    outcome = settings_cli.apply_settings(
+        new_rows,
+        source=f"card:{path.name}@sha256:{digest}",
+        actor="settings.load.card",
+        store=store,
+        delete=deletes,
+    )
diff --git a/src/cobalt/settings/cli.py b/src/cobalt/settings/cli.py
@@ -7,8 +7,13 @@
-Every apply goes through `apply_settings` — the one write function the
-ASET change line (DRC D4-4) calls too.
+Every apply of `cobalt settings load` (--from, --from-git, --optional,
+--card) and the ASET change line (DRC D4-4) goes through `apply_settings`
+— the one write function for his settings (L3; D4 fix r1 F-1 routed
+--card through it). The radar's vault-note mirror (`radar/notes.py`
+`mirror_sources`, the `radar.note.*` keys) is the one other writer of
+`trader_settings` rows: a machine mirror with its own market-reset
+refusal, not a settings load.
@@ -76,23 +81,25 @@ def apply_settings(
-    """THE ONE APPLY (L3 / L40, DRC D4-4). `cobalt settings load --apply`
-    and the ASET change line both write `"user".trader_settings` through
-    this function and nothing else.
+    """THE ONE APPLY (L3 / L40, DRC D4-4). Every `cobalt settings load
+    --apply` form (--card included, D4 fix r1 F-1) and the ASET change line
+    write `"user".trader_settings` through this function and nothing else.
-    database returns equals the payload; one log line naming the keys,
-    the payload hash and the time. NEVER the values: they are his user
-    data (L32). The store's own trace is each row's `source` and
+    database returns equals the payload; ONE log line naming the keys,
+    the deleted keys, the source KIND (the source label up to `@sha256:`)
+    and the time — never a value and never a digest of one (a digest of a
+    small-value payload is the value, L32; D4 fix r1 F-8). The store's
+    own trace is each written row's `source` (the reviewed payload hash
+    for the change line, the loader's own label for the CLI) and its
     `updated_at`.
-    digest = payload_sha256(rows)
-        "settings applied: keys {} · deleted {} · sha256 {} · source {} · at {}",
-        sorted(rows), delete, digest, source,
+        "settings applied: keys {} · deleted {} · source {} · at {}",
+        sorted(rows), delete, source.split("@sha256:", 1)[0],
```
(context lines trimmed to the changed hunks; the tool output is the full diff, 3 files.)

## F5 THE RUNS
New `tests/cobalt/test_drc_d4_fix_r1_runs.py` (harness by import: `FakeStore`, `_form`, `page`, `world` from `test_drc_settings.py`). No test was red → NO `xfail` mark added.
- **RUN-1** (`06` `:179`): `test_run1_a_a_store_write_lands_inside_its_test` then `test_run1_b_nothing_of_the_previous_test_survives` — defined in that order; pytest runs a file's tests in definition order. THE LOCK, second take: (a) `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`; (b) cp exit 0, `ls -la` → ONE line `-rw-------  1 cobalt  staff  2186 Sep 25 07:30 /Users/cobalt/cobalt-wt/drc-d1/.env`; (c) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_d4_fix_r1_runs.py` → `3 passed in 0.24s` (none skipped: RUN-1 a PASSED, RUN-1 b PASSED, RUN-2 PASSED); (d) rm exit 0, `ls …/.env` → `No such file or directory`. `.env: removed, proven gone (F5)`. **RUN-1 GREEN: the with-DB `TraderSettingsStore()` joins the `dev_db_tx` rollback** — the row written in (a) is read back in (a) and absent in (b).
- **RUN-2** (`06` `:179`): offline `uv run pytest -q -rsP -p no:cacheprovider tests/cobalt/test_drc_d4_fix_r1_runs.py` (`-rsP` to show the passed test's stdout; the one change from the dictated flags, recorded) → `1 passed, 2 skipped in 0.18s`, captured stdout `RUN-2 captured messages: 0`; with-DB run above: PASSED. **RUN-2 GREEN**: a POST of a refused change (daily stop = a constructed 5-digit figure + `aset.sheet_modes.half.A = "x"`) to `/settings/daily` AND `/settings/daily/apply` renders FAILED on both, `world.puts == []`, and the loguru sink (all levels) captured **0** messages on the whole request path — so no log line carries the typed figure. (NOTE for `22`: 0 captured means the refusal path logs nothing at all; the assertion holds trivially on this path — it would go red the day that path starts logging the form.)
- **RUN-3** (`06` `:179`; R95): the old daily-stop line READ once from `git show 00262e45:configs/cobalt/templates/daily.md.j2` (the line under `Daily HARD Stop`), tool result only. There is NO Grep TOOL in this session's tool set → Bash `grep -rlF --exclude-dir=.git --exclude-dir=.venv --exclude-dir=data --exclude-dir=node_modules -e '<the line, single-quoted, fixed string>' /Users/cobalt/cobalt-wt/drc-d1` (and a second call with the dollar figure alone, a superset). **old literal outside configs/src/tests: 1 hits** — `docs/00 - Project/INCIDENT-2026-09-03-notes.md` (TRACKED: `git log -1 --format=%h -- …` → `b0fd2e41`); the figure-alone search names the SAME one path. A RESULT → ESCALATE (the desk's redaction, L45 companion ruling); not edited here.
Commit `<tip>` = `e96f0be7` `test(drc): D4 fix r1 RUNS — the store joins the suite rollback, a refused field logs no typed value (L70)`.

## F6 LIVE-NOTE
On `<tip>` `e96f0be7`, F1's live-note command byte for byte → `142 passed, 1 skipped, 15 warnings in 10.02s` → `<lp>` = 142, `<lf>` = 0; 0 errors. SKIPPED lines: 1 (`grep -c "SKIPPED"` → 1) — `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (known); NONE naming `COBALT_LIVE_VAULT_ROOT`. Same as F1. GATE GREEN.

## F7 OFFLINE
On `<tip>` `e96f0be7`. `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory`. F1's offline command byte for byte → **`2520 passed, 470 skipped, 1 xfailed, 15 warnings in 70.27s (0:01:10)`** → `<p>` = 2520, `<f>` = 0; 0 errors. GATE GREEN.
Counts (from the tool results): 2520 = `<bp>` 2516 + 4 new offline tests (F-1's 2 in `test_drc_d4_fix_r1.py`, F-4's negative control `test_the_one_reader_walk_flags_a_second_reader`, RUN-2) ✓. Skipped 467 → 470 = +3 new with-DB tests (F-3's `test_e3_a_failure_inside_the_one_put_writes_neither_key`, RUN-1's two) ✓. The F-5 / F-6 / F-8 / F-2 edits change no test count.

## F8 WITH-DB
On `<tip>` `e96f0be7`, 07:32–07:35 ET. The four deselected ids, one grep each: `test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips` (`697:    def test_twice_is_idempotent_and_the_rollback_round_trips(self):`), `test_tenancy.py::TestMigrationRoundTrip::test_the_proof_table_names_every_ruled_table` (`710:    def test_the_proof_table_names_every_ruled_table(self):`), `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default` (`263:    def test_every_user_table_carries_user_id_not_null_with_the_guc_default(`), `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` (`306:def test_rows_reach_the_probe_through_a_named_cursor_in_batches():`) — all at the expected lines.
- THE LOCK, third take: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`; (b) cp exit 0; `ls -la` → ONE line `-rw-------  1 cobalt  staff  2186 Sep 25 07:32 /Users/cobalt/cobalt-wt/drc-d1/.env`.
- (c) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → **`2980 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 149.25s (0:02:29)`** → `<dp>` = 2980, `<df>` = 0; 0 errors; deselected 4 (EXPECTED 4). GATE GREEN. `<dp>` = `05`'s 2973 + 7 new tests (F2: 3 (F-1 ×2, F-4's negative control); F3: 1 (F-3); F5: 3 (RUN-1 ×2, RUN-2)) = 2980 ✓. The 6 SKIPPED lines name ONLY `test_cards_picks.py:383`, `test_cards_picks.py:396`, `test_radar_evaluate.py:691`, `test_replay_line.py:256`, `test_catalyst.py:365`, `test_predicate.py:262` — the same six as `05`'s E7 — so `test_drc_settings_db.py`, `test_drc_d4_fix_r1_runs.py`, `test_card_settings.py`, `test_drc_store.py`, `test_drc_k1_store.py`, `test_drc_k2_store.py`, `test_drc_k2_fix_r1_store.py` are NOT skipped.
- (c2) absence probe: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → `1 failed in 5.65s`, `E       assert 28 == 32` — SHORT BY EXACTLY 4, THE KNOWN SHAPE (`05`'s E7 (c2)). **0016 + 0018: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 4).** No `db migrate` of any spelling was typed.
- (d) `rm /Users/cobalt/cobalt-wt/drc-d1/.env` exit 0; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory`. **`.env: removed, proven gone (F8)`.**

## RESTARTS
`uv run cobalt jobs restarts 5d4f8201..e96f0be7` → exit 0:

| path | change | rule | restart |
|---|---|---|---|
| `docs/40 - DevDocs/cobalt/settings/card.md` | M | DOCS | - |
| `docs/40 - DevDocs/cobalt/settings/cli.md` | M | DOCS | - |
| `docs/40 - DevDocs/reports/drc-d4-build-2026-09-25.md` | M | DOCS | - |
| `src/cobalt/aset/web.py` | M | static import reach | com.cobalt.aset |
| `src/cobalt/settings/card.py` | M | static import reach | com.cobalt.aset,com.cobalt.radar |
| `src/cobalt/settings/cli.py` | M | static import reach | com.cobalt.aset,com.cobalt.radar |
| `tests/cobalt/test_card_settings.py` | M | test/documentation; no resident | - |
| `tests/cobalt/test_drc_d4_fix_r1.py` | A | test/documentation; no resident | - |
| `tests/cobalt/test_drc_d4_fix_r1_runs.py` | A | test/documentation; no resident | - |
| `tests/cobalt/test_drc_settings.py` | M | test/documentation; no resident | - |
| `tests/cobalt/test_drc_settings_db.py` | M | test/documentation; no resident | - |

**`RESTARTS: com.cobalt.aset com.cobalt.radar`** — as expected; NO `UNCLASSIFIED`. (Run before F8 — the range `5d4f8201..e96f0be7` is the code range; F8 adds no commit, the report commit at CLOSE is docs.)

## CORRECTIONS TO THE D4 BUILD REPORT
F-7 (HOLDs 6–7, `06` `:127`–`:128`), REPORT-ONLY; `drc-d4-build-2026-09-25.md` stays as committed — these lines are the correction of record.
1. **HOLD 6 — the E2 D4-4 count.** `drc-d4-build-2026-09-25.md:85` reads `| D4-4 (11) | …`. Re-counted from `tests/cobalt/test_drc_settings.py` at `5d4f8201` (Read before any edit of this round): the D4-4 section holds `test_the_page_shows_the_change_line_with_the_attestation_form` `:366` (1), `test_review_shows_the_per_key_diff_and_the_payload_sha` `:375` (1), `test_apply_with_a_wrong_sha_is_refused_and_writes_nothing` `:391` (1), `test_apply_inside_market_reset_is_refused_with_the_reason` `:398` (1), `test_a_bad_field_is_refused_naming_it_and_nothing_is_written` `:419` (5 parametrized rows, `:409`–`:417`), `test_a_good_apply_writes_through_the_one_apply_function_then_reads_back` `:428` (1), `test_saved_only_after_the_read_back_equals_the_payload` `:464` (1), `test_no_log_line_carries_a_value` `:472` (1) = **12 test items**. The E2 table then sums 26 + 3 + 3 + 4 + **12** + 1 = **49** = the `49 passed` it reports (`:130`).
2. **HOLD 7 — ESCALATE 7 / 9 (iii) stale.** `drc-d4-build-2026-09-25.md:217` (ESCALATE 7: "X12 reader half … NOT yet run with-DB") and `:219` (ESCALATE 9 (iii): "RESTARTS not run") were written at the E6 stop and are SUPERSEDED by the same report's E7 and `## RESTARTS`: `:166` "The E1 / X12 tests: `test_e10_…`, `test_x12_size_…`, `test_x12_every_drc_field_is_none_without_rows` PASSED in this run (only the three E3 tests failed) — the X12 reader half is proven after the code." and `:153` "… **`2973 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 149.80s`** …" (the FINAL E7, every with-DB test incl. X12's); `:172` "05:58 ET: `uv run cobalt jobs restarts 00262e45..5d4f8201` → exit 1, `FAILED: RestartError: one or more changed paths were unclassified`" with `:185` "**`RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`**".

## SEAM FOR D2
"`src/cobalt/aset/web.py` holds TWO new route blocks and they share nothing. D4's settings change-line block (`POST /settings/daily`, `POST /settings/daily/apply`, and any helper they alone use) sits DIRECTLY AFTER the `/attest` route (`@app.post("/attest")`, `web.py:1138` at `4626a1f2`) and BEFORE the next existing route. D2's `/drc` block (`GET /drc`, `POST /drc/import`, `POST /drc/no-trade`, `POST /drc/scan`, and any helper they alone use) sits at the END of the file, after every existing route. Neither block calls, imports or edits a helper of the other; the only shared names are the file's EXISTING helpers (`_render`, `_failed`, `app`, the existing imports), which neither block changes. D2 adds the seam test (`tests/cobalt/test_drc_web_seam.py`): both blocks exist in that order, and no name defined inside one block is referenced inside the other. D3 and every later reader of the daily stop or the dollars per grade call `cobalt.settings.drc.daily_risk_values(conn)` (D4-2) and `cobalt.settings.drc.load_drc_settings(conn)` (D4-1) — never a second reader (L3)."

On `<tip>` `e96f0be7` (read from this tree):
- `/attest`: `src/cobalt/aset/web.py:1141` (`@app.post("/attest", response_class=HTMLResponse)`).
- D4's block: FIRST line `web.py:1184` (the `# ----` banner; `:1185` `# DRC D4-4: the settings CHANGE LINE (R96 / R102). THE SEAM WITH D2 (L72):`), LAST line `web.py:1295` (the closing `)` of `settings_daily_apply`'s return). `@app.post("/settings/daily")` `:1243`, `@app.post("/settings/daily/apply")` `:1258`; next existing route `@app.post("/card/{card_id}/move")` `:1298`; the file's last route `@app.post("/radar/card/{card_id}/release")` `:1507`. **The block's line numbers did NOT move**: F-8's one docstring edit (`:1268`) replaced one line with one line.
- Imports D4 added (used only by D4's block): `web.py:70` `from cobalt.settings import cli as settings_cli`, `:71` `from cobalt.settings import drc as settings_drc` (unchanged).
- Signatures (unchanged; `git diff 5d4f8201 -- src/cobalt/settings/drc.py` EMPTY): `load_drc_settings(conn: Optional[SettingsSource] = None) -> DrcSettings` — `src/cobalt/settings/drc.py:82`; `daily_risk_values(conn: Optional[SettingsSource] = None) -> DailyRisk` — `src/cobalt/settings/drc.py:114`.
- **The one apply: `apply_settings(rows, *, source, actor="settings.load", store=None, delete=())` — `src/cobalt/settings/cli.py:76`; callers: `cmd_load_optional` (`cli.py:237`) and `cmd_load` (`cli.py:317`) (same file), `cmd_load_card` (`src/cobalt/settings/card.py:279`, its call `:322`, D4 fix r1 F-1) and `settings_daily_apply` (`web.py:1258`, its call `:1280`); its log line names keys, deleted keys, source kind and time — no value, no digest (F-8).**

D2 reads no settings key; D2 edits nothing in D4's block.

## FOR D3
- `daily_risk_values(conn)` (`src/cobalt/settings/drc.py:114`) is the ONE reader D3's `drc-risk/facts` unit calls for the distance to the daily stop; `DailyRisk.daily_stop` is per sheet (`{"full": …, "half": …}`) — D3 picks the sheet the day used (the day mode's ruling), and a `None` renders `not given` (never a default).
- `load_drc_settings(conn)` (`src/cobalt/settings/drc.py:82`) is the reader of `limits.card_match_window_minutes` (D3's card match: `None` → every trade `card: not matched (window not given)`), of `windows.*` (B27: `premarket_end`, `first_window_minutes`, `prime`, `dead`, `second`) and of `goal.*` (`primary`, `metric`, `target_pct`, `switch_threshold_pct`).
- `cobalt drc build --dry-run` is D3's (it joins K1's `drc` group, `[F-17]` seam (6)); X12's second half (v2 `:118`: "`cobalt drc build` fails naming the missing key") is D3's to prove, and D3's row renders `not given` rather than failing — the conflict is carried to D3's `## ESCALATE`.
- His daily-stop VALUE must be loaded by HIM before the first deploy (his change line or `cobalt settings load --optional`) — until then the daily note and D3's risk unit say `not given` (a production-visible change the deploy prompt names).
- D4 fix r1 changes no reader: daily_risk_values / load_drc_settings are untouched (git diff 5d4f8201 -- src/cobalt/settings/drc.py EMPTY).

(Re-read on this tree: `drc.py:114` and `:82` as above. The v2 `:118` cite is carried byte for byte from the D4 report; the real X12 line is v2 `:204` per `06` ESCALATE 3.)

## CONTINUE
DONE. F0 → F1 → F2 (`36331949`) → F3 (`d523bba5`) → F4 (`807c13ec`) → F5 (`e96f0be7`) → F6 → F7 → F8 → RESTARTS → CLOSE. `.env` removed and proven gone after each of the three lock takes (F3, F5, F8).

## ESCALATE
1. LINE MOVED: `grep -n "the one log line (keys + hash + time" src/cobalt/aset/web.py` — expected 1270, read 1268.
2. R22 scope: read as the drc-d1 pair for this worktree (desk reading, R61 / R65 (1) / 09-25 R9).
3. L74: one `Claude-Session:` / `SendUserFile` block inside a tool result (the prompt file's Read) — recorded under `## L74`, not followed.
4. **RUN-3 RESULT: old literal outside configs/src/tests: 1 hits** — `docs/00 - Project/INCIDENT-2026-09-03-notes.md` (tracked, last commit `b0fd2e41`). A committed docs file carrying his old daily-stop value: the DESK's redaction (L45 companion ruling: redact the report, never narrow the test). Not edited here.
5. TOOL GAP (RUN-3): this session has NO Grep tool (the prompt's "GREP TOOL"). Taken instead: Bash `grep -rlF --exclude-dir=.git --exclude-dir=.venv --exclude-dir=data --exclude-dir=node_modules -e '<literal>' /Users/cobalt/cobalt-wt/drc-d1` — a listed prefix, the literal SINGLE-quoted as a fixed string (no `$` in a double-quoted argument), `-l` so only paths print. It walks gitignored folders too (it does not honour `.gitignore`); the one hit is tracked. No dialog.
6. RULE SLIP, self-reported (L35): two early read-only greps (before F2) used a `\|` alternation in a double-quoted pattern (`grep -rn "daily_stop_\|…" src/cobalt --include=*.py`, which zsh refused with `no matches found: --include=*.py`, and one `grep -n "put\|apply_settings\|…"` on the card DevDoc). Both are listed `grep *` prefixes; NO dialog was raised and nothing was written; every later grep was one fixed string per call.
7. RUN-2: the dictated flags `-rs` hide a passing test's stdout; the count was read from ONE extra offline run with `-rsP` (listed `uv run pytest *` prefix). Captured messages = **0**: the refusal path logs nothing at all, so RUN-2's "no figure in any log line" holds trivially today and goes red the day that path logs the form (NOTE for `22`).
8. F-5 shape: `OPTIONAL_SETTING_MODELS[key]` is a `DrcKey` adapter whose `from_rows` returns a `_DrcLeaf` with no `__eq__` (`models.py:178`–`:185`), so "`from_rows(model.row()) == model`" is asserted as `adapter.from_rows({key: row}).row() == row` plus `adapter.validate(row) == typed`; the typed accessor is `DrcKey.validate` (`models.py:199`), type-checked (`type(got) is type(typed)`, element types for tuples). No input value changed. All 12 rows GREEN on the base.
9. F-8 shape: the two constructed figures are held in local names (`stop = "31337"`, `grade = "7061"`; the grade was `"61"`); the per-message `"31337" not in m` loop became `_leaks(m, (stop, grade)) == []` (stricter: stop + grade + any 64-hex run). The negative controls sit at the top of the test.
10. F-1 scope note: beside the dictated module-docstring sentence (`cli.py:10`–`:11`), `apply_settings`' own first docstring sentence (`cli.py:79`–`:81` at base — the other half of HOLD 1's cite "`cli.py:10`–`:11`, `:79`–`:81`") was amended to name "every `cobalt settings load --apply` form (--card included)". Docstring only.
11. Cite drift in a DICTATED sentence: the `test_e3_a_two_key_apply_with_one_bad_key_writes_neither` docstring says `drc.py:258` (as dictated); `drc.py:258` is `if errors:` and the `raise DailyChangeInvalid(errors)` is `:259`.
12. Not edited, for `22`: `settings/card.py`'s module docstring (`:10`–`:16`) still describes the apply as "ONE `put` … its trace is the command, hash and time" — still true in effect through `apply_settings` (one `put`; the hash stays in the row `source`), but it does not name `apply_settings`; not a named F-1 line, left as built (L75).
13. NOTE for `22`: `settings/card.py` and `tests/cobalt/test_card_settings.py` are F-1's own files listed under D4-4 (the R16 / R17 shape); `radar/notes.py:747` (`mirror_sources`, `return target.put(`) is named in F-1's walk docstring and in `cli.py`'s module docstring as the one other writer of `trader_settings` rows, outside D4 — NOT changed (`git diff 5d4f8201 -- src/cobalt/radar` EMPTY).
14. PINS red on the base: NONE (F-2, F-3, F-4, F-5, F-6 all green on the base, each with its negative control). RUNS red: NONE (RUN-1, RUN-2 green; RUN-3 = item 4).
15. Standing line: **"The FIX rows moved on file evidence only (`06` `## Checked against the branch` rows 1–3, 5–10 HOLD and `06` ESCALATE 4; row 4 NOT REAL — the D4-4 trace TEXT is AMENDED D4-4 TRACE, no code; rows 11–12 the desk's R17 / R16 readings, NOT REAL). The red: F2 offline on `36331949` (F-1, F-8), with PINS for F-2 … F-6 each carrying a negative control; green on `807c13ec`. The seam moves in ONE bullet (the one apply's caller list, F-1); `## FOR D3` stands. The check is `22` (round 2 of ≤3; Opus 5.5 + Grok, with Sol from Sep 26th, 2026 6:47 AM), and its packet carries this report's executed output of all three suites and RUN-1…RUN-3 (L68). Astra's read of the D4 NEW BUILD is owed from its meter return (`06` ESCALATE 10, the desk's seat). The deploy's L68 gate re-proves the three suites on the tree that ships."**

DRC D4 FIX R1 BUILT e96f0be7 | on 5d4f8201 | red 36331949 | offline 2520/0 | with-DB 2980/0 | live-note 142/0 | .env: removed | 0018: rolled back | FIX: 8 | RUNS: 3 | ESCALATE: 15
