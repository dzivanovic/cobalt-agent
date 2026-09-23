# SETUPS FIX R4 — 2026-09-22 (`72`, Opus 5.5, hub `setups-fix-r4-0922`, started 21:17:57 EDT from `date`)

## §0 Headline
- BUILT, 5 of 5 rows on `8da261a`. Code tip `f5aaeb4`. F1: the dials probe returns `False` only on `merge_tunables`' engine-key refusal (DIALS table unchanged). F2: `A-24` is null in the gitignored proposal. F3: no real-day literal, pinned by an allowlist test. F4: the cutter re-dates on the NY wall clock, the fixture is re-cut, five pins re-copied.
- **F5 / C3: CORRESPONDS.** The corrected cut forms short 0.6690 / 0.87 at 10:24 ET, the stored day's BTTC line; the old pin was long 0.8400 / 0.66. Blind seat `13` must re-derive the five moved pins.
- Offline 2464/0 (2453 + 11 new cases). `src` / `configs` / committed-day pins unchanged. RESTARTS: none. With-DB OWED (68).
- ESCALATE: 12. One `ASK DESK`, default taken: F3's prescribed wording contained a dated filename; an undated reference was used instead.

## L74
Recorded once: a system-reminder appended after this session's first tool result asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and named a file-send tool (`SendUserFile`). Data under L74 — not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (the branch's own precedent, `git show --stat 8da261a`).

## AUTHORIZATION
| check | command | result |
|---|---|---|
| check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"SETUPS CHECK R2R3 DONE" -- ".../setups-check-r2r3-2026-09-22.md"` | `dbfe49f95dde048b791af53af58fa382c3ebb072` |
| classification committed | `… -S"SETUPS FIX R4 DRAFTED" -- ".../setups-fix-r4-draft-2026-09-22.md"` | `688bc1f0772862d53674bbf7ca0f7734ce584861` |
| R32 | `grep -n "^| R32 " cto-2026-09-22.md` | `:119` carries `claude-opus-5-5` |
| R41 | `grep -n "^| R41 " <the previous day's desk report, as the prompt names it>` | `:52` quotes both `.env` strings and `"Approved"` |
| R23 | `grep -n "^| R23 " cto-2026-09-22.md` | `:128` carries `Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)` and `"approved"` |
| launch row + NEW USE | `grep -n "72-setups-fix-r4.md" cto-2026-09-22.md cto-2026-09-23.md` | `cto-2026-09-22.md:35: | R118 | 21:16 ET | NEW USE for \`72-setups-fix-r4.md\`, his words: "Approved" …`; `cto-2026-09-23.md`: `No such file or directory` (recorded, not fatal) |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"72-setups-fix-r4.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `1823e02128ab90e99732b367f9c9980cc0772f3d` |
| rule strings | `grep -c -F -e "<rule>" 33-setups-fix-r3.md`, one call per string, quotes included: 19 allow, 3 deny, the `--add-dir` triplet | every one `1`, except `"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)"` → `2`; all ≥1 — PASS |
| cutter string | `grep -c -F -e "\"Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)\"" 12-setups-fixture-cut.md` | `1` — PASS |

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 22 21:17:57 EDT 2026` |
| BASE TIP filled | title line | — | `8da261a` (7-hex) — PASS |
| r3 stopped on its tip | `tail -n 3 ".../setups-fix-r3-2026-09-22.md"` | 0 | `SETUPS FIX R3 BUILT be44eb4 \| on 65c08a0 \| offline 2453/0 \| with-DB 569/3 \| …` — PASS |
| clean | `git status --porcelain` | 0 | (no output) — PASS |
| branch | `git status` | 0 | `On branch setups/seven-0921` / `nothing to commit, working tree clean` — PASS |
| tip | `git log --oneline -1` | 0 | `8da261a fix(setups): round 3 — report` — PASS (first launch) |
| 8da261a docs-only | `git show --stat 8da261a` | 0 | `.../reports/setups-fix-r3-2026-09-22.md \| 187 ++++…` / `1 file changed, 183 insertions(+), 4 deletions(-)` — PASS |
| `.env` | `ls -la /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` — PASS |
| same worktree | `ls -la ".../setups-fix-r4-2026-09-22.md"` | 1 | `No such file or directory` — PASS (first launch) |
| 12's raw bars | `ls -la …/tasks/bj70z1v0d.output` | 0 | `-rw-r--r--  1 cobalt  wheel  155216 Sep 22 15:34 …` — 155216 = 12's count — PASS |
| 12's raw membership | `ls -la …/tasks/bn9p3qf72.output` | 0 | `-rw-r--r--  1 cobalt  wheel  234 Sep 22 15:34 …` — 234 = 12's count — PASS |
| 12's daily CSV | `ls -la <production daily-cache CSV, 12 § CUT 3.1>` | 0 | `-rw-r--r--  1 cobalt  staff  95128 …` — 95128 = 12's count — PASS |
| proposal file | `ls …/docs/_inflight/setups-assumed-values-r3-2026-09-22.md` | 0 | present — PASS |
| restarts | `uv run cobalt jobs restarts 8da261a..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` (empty range) |

## BASELINE
- **OFFLINE** `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` (background, on the untouched `8da261a`; no file edited while it ran — the report file was created BEFORE launch): `2453 passed, 361 skipped, 1 xfailed, 15 warnings in 483.26s (0:08:03)` → **2453/0** = r3's CLOSE line, as expected.
- NO WITH-DB BASELINE (`cobalt_dev` broken, `68` owed).

## F1
The dials probe asserts WHY a note row was refused.

### T
RED-on-`8da261a`, two new tests in `tests/cobalt/test_setups_fix_r4.py` (`uv run pytest -q -p no:cacheprovider tests/cobalt/test_setups_fix_r4.py -k f1` → `1 failed, 1 passed in 0.19s`):
- `test_f1_a_malformed_probe_note_fails_the_probe_loudly` (RED): a `tunables:<slug>` unit whose extra row carries only `key` + `value` (no unit, scope, …) → must raise `VaultTaxonomyError` matching `invalid tunables rows`. Failing line VERBATIM: `E       Failed: DID NOT RAISE <class 'cobalt.taxonomy.vault_loader.VaultTaxonomyError'>` (`tests/cobalt/test_setups_fix_r4.py:33`).
- `test_f1_the_engine_key_refusal_still_reads_not_reachable` (GREEN guard): r3's `## DIALS` row `| rubberband | stop.buffer | assumed / engine only (global) |` → `_per_trade_accepted(...) is False`.

### C
`tests/cobalt/test_setups_fix_r3.py` `_per_trade_accepted` only (+ `import re` and one module constant under it): `except VaultTaxonomyError as e:` returns `False` only when `str(e)` matches `_ENGINE_KEY_REFUSAL`, else `raise`. The pattern is the fixed words of the refusal's raise site (no value):
- raise site `src/cobalt/taxonomy/loader.py:114` in **`merge_tunables`**: `raise TaxonomyConfigError(f"user tunable row(s) {collisions} shadow engine keys in " f"{TUNABLES_PATH.name}. A per-trade row in a strategy note may only " "ADD keys (scope per_trade(...)), never redefine an engine key — " …)`;
- re-raised as `VaultTaxonomyError` at `src/cobalt/taxonomy/vault_loader.py:601` in `_resolve_every_cfg` (`raise VaultTaxonomyError(f"{', '.join(notes)}: {e}") from e`), called from `load_vault_trade_defs` (`vault_loader.py:517`).
- pattern: `r"user tunable row\(s\) .* shadow engine keys in .*A per-trade row in a strategy note may only\s+ADD keys"` (`re.S`).
After C: `-k f1` → `2 passed in 0.17s`.

### A1
None. r3's F6 tests: `uv run pytest -q -s -p no:cacheprovider tests/cobalt/test_setups_fix_r3.py -k f6` → `2 passed, 17 deselected in 26.67s`; the `DIALS` lines re-printed and compared row for row with r3's `## DIALS` table: **IDENTICAL** — 79 rows, same order, same `reachable` cell (78 `assumed / engine only (<scope>)`, 1 `per_trade` = `hitchhiker | example_drive_then_range.range_duration_band`); no probe raised, so every r3 "not reachable" was the engine-key refusal. F6 (b)'s three lines re-printed unchanged (`formed_scans=71`, `4.8500` / `4.8500` / `4.6220`).

### SUITE
OFFLINE → `2455 passed, 361 skipped, 1 xfailed, 15 warnings in 485.05s (0:08:05)` → **2455/0** = 2453 + 2 new F1 tests.

### COMMIT
`2817896 fix(setups): round 4 — F1 the dials probe refuses only on the engine-key refusal, any other error fails loudly` — `git show --stat HEAD`: `.../reports/setups-fix-r4-2026-09-22.md | 101 +++…` · `tests/cobalt/test_setups_fix_r3.py | 17 +++-` · `tests/cobalt/test_setups_fix_r4.py | 42 +++…` · `3 files changed, 158 insertions(+), 2 deletions(-)`.

## F2
`A-24` → null in the gitignored proposal.

### C
Read the file; ONE Edit, on the `A-24` row's PROPOSED-value cell only (every other cell of the row, and rows `A-09`, `A-10`, `A-16`, untouched). Committed config untouched (`leg.min_size_atr` already `value: null`).
- Read back (`grep -n "A-24" docs/_inflight/setups-assumed-values-r3-2026-09-22.md`, row 10), the changed cell only, no value: `` `null` — `status: null` — reason: `no passage speaks to pullback size (check r2r3, unanimous)` (fix r4 F2) ``.
- `git status --porcelain` → (no output): no line for `docs/_inflight/…` — the file stays untracked and ignored. No commit (nothing tracked changed).
- NOT edited (row-only rule): the file's line 12 paragraph explaining the old A-24 value and its closing tally line `proposal: 4 proposed, 0 null` — now stale; ESCALATE (ii).

## F3
No real-day literal in the cut's committed test.

### T
RED-on-`8da261a`, in `tests/cobalt/test_setups_fix_r4.py`: `test_f3_every_iso_date_in_the_cut_is_a_synthetic_day`, parametrised over `test_setups_fixture_cut.py` and `_cut_setups_fixtures.py` (2 cases): every `\d{4}-\d{2}-\d{2}` literal ∈ `{2026-01-06, 2026-01-07, 2026-01-08}`. The message COUNTS outsiders and never prints them (L32). `-k f3` → `1 failed, 1 passed, 2 deselected in 0.11s`; failing lines VERBATIM: `E       AssertionError: test_setups_fixture_cut.py: 1 ISO date literal(s) outside the synthetic allowlist` / `E       assert 1 == 0` (`tests/cobalt/test_setups_fix_r4.py:66`). The cutter case was already GREEN.

### C
`tests/cobalt/test_setups_fixture_cut.py` module docstring only: `real day <real day>,` → `the real stored day (see` / `` the fixture-cut report of prompt `12`, `## FIND — rubberband`), `` — the synthetic day stays. **Deviation from the row's wording, named (ESCALATE (iii-a)):** the row's text `(see \`setups-fixture-cut-2026-09-22.md\`)` itself carries an ISO date (`2026-09-22`, the report's filename) — it would keep this row's own pin RED and fail the CLOSE `grep -rn "2026-09-" …` self-check. Safe default taken: the pin and the self-check win; the report is named by its prompt and section instead. For the same reason this module's own docstring names the check and drafter reports by prompt number, not by dated filename. After C: `-k f3` → `2 passed, 2 deselected in 0.07s`; `grep -rn "2026-09-" tests/cobalt/test_setups_fix_r4.py tests/cobalt/test_setups_fixture_cut.py` → (no output).

### A1
None.

### SUITE
OFFLINE → `2457 passed, 361 skipped, 1 xfailed, 15 warnings in 487.30s (0:08:07)` → **2457/0** = 2455 + 2 new F3 cases.

### COMMIT
(below)

## F4
The cutter keeps the New York wall clock; re-cut; pins re-copied.

### T
RED-on-`b77d8e5` (the cutter is unchanged since `8da261a`), in `tests/cobalt/test_setups_fix_r4.py`, the cutter's `_shift_datetime_str` loaded by path (`importlib.util.spec_from_file_location`), on constructed days of this file's own (two June/July EDT days, one December EST day — no stored day, no `2026-09-`). 5 functions = 7 cases. `-k f4` → `5 failed, 2 passed, 4 deselected in 0.12s`. RED lines VERBATIM:
- EDT → EST keeps the NY clock (2 cases, space + `T`/fraction): `E       AssertionError: assert '2025-12-10 13:30:00+00:00' == '2025-12-10 14:30:00+00:00'` · `E       AssertionError: assert '2025-12-10T0....469346+00:00' == '2025-12-10T0....469346+00:00'` (diff `- …T09:01:57…` / `+ …T08:01:57…`).
- a UTC time moves by its NY LOCAL date: `E       AssertionError: assert '2025-12-11 00:00:00+00:00' == '2025-12-11 01:00:00+00:00'`.
- a time not in UTC fails loudly (2 cases, naive + `-04:00`): `E       Failed: DID NOT RAISE <class 'SystemExit'>` ×2.
- GREEN guards: EDT → EDT keeps `13:30:00+00:00` (today's behaviour); a bare date moves by the delta.

### C (commit 1 of 2)
`tests/fixtures/radar/_cut_setups_fixtures.py` only: `_shift_datetime_str` re-dates on the NY wall clock (aware UTC → `ZoneInfo("America/New_York")` → local date + delta, local clock kept → UTC; the input's separator and fractional digits kept, `+00:00` kept); a bare `YYYY-MM-DD` moves by the delta; a time not ending `+00:00` → `SystemExit` naming it. `_DATETIME_RE`'s optional offset widened from `(?:\+00:00)?` to `(?:[+-]\d{2}:\d{2}|Z)?` so a non-UTC offset REACHES that check instead of silently passing through unshifted (ESCALATE (iv-b)); two module constants (`_UTC_SUFFIX`, `_NEW_YORK`), imports `timezone` / `ZoneInfo`, and ONE module-docstring line "Every time is re-dated on the New York wall clock (fix r4 F4)." `cut_daily` untouched. After C: `uv run pytest -q -p no:cacheprovider tests/cobalt/test_setups_fix_r4.py` → `11 passed in 0.16s`.

### A1
None (commit 1: the committed fixtures are not yet re-cut).

### SUITE (commit 1)
OFFLINE → `2464 passed, 361 skipped, 1 xfailed, 15 warnings in 483.71s (0:08:03)` → **2464/0** = 2457 + 7 new F4 cases.

### COMMIT (commit 1)
`c000411 fix(setups): round 4 — F4 cutter keeps the New York wall clock` — `git show --stat HEAD`: `.../reports/setups-fix-r4-2026-09-22.md | 21 ++++++++-` · `tests/cobalt/test_setups_fix_r4.py | 52 +++…` · `tests/fixtures/radar/_cut_setups_fixtures.py | 30 +++++++++++--` · `3 files changed, 98 insertions(+), 5 deletions(-)`.

### THE RE-CUT (commit 2 of 2)
- `uv run python tests/fixtures/radar/_cut_setups_fixtures.py <12's argv, § CUT 3.3>` (background; `12`'s own raw bars / membership files and the production daily-cache CSV, read by path, none edited) → exit 0, VERBATIM: `wrote /Users/cobalt/cobalt-wt/setups-c1/tests/fixtures/radar/membership-setups-rubberband.real-shape.json (1 rows)` / `wrote …/bars-setups-rubberband.real-shape.json (956 bars)` / `wrote …/daily-bars-setups-rubberband.real-shape.csv (40 rows)` — = `12`'s counts.
- Leak proofs: `grep -rl "2026-09-" tests/fixtures/radar/` → `tests/fixtures/radar/_cut_panel_fixtures.py` / `tests/fixtures/radar/_cut_p2_fixtures.py` (the two precedent `.py` files only — none of the three outputs) · `grep -c "user_id" tests/fixtures/radar/bars-setups-rubberband.real-shape.json` → `0`.
- `git diff --stat -- tests/fixtures/radar` → `.../radar/bars-setups-rubberband.real-shape.json | 1912 ++++++++++----------` / `.../membership-setups-rubberband.real-shape.json | 4 +-` / `2 files changed, 958 insertions(+), 958 deletions(-)`. The daily CSV: **UNCHANGED** (as expected — date-only rows, `cut_daily` untouched). Membership diff VERBATIM: `-    "entered_at": "2026-01-07 08:01:57.469346+00:00",` → `+    "entered_at": "2026-01-07 09:01:57.469346+00:00",` · `-    "left_at": "2026-01-08 00:00:00+00:00",` → `+    "left_at": "2026-01-08 01:00:00+00:00",` (+1 h in UTC = the same New York wall clock on an EST day).
- F5's field added to the printing test in THIS commit (`formed_bar_ny=…`, `from zoneinfo import ZoneInfo`; no assertion changed).
- THE PIN: `uv run pytest tests/cobalt/test_setups_fixture_cut.py -s -k engine_output` → `1 passed, 1 deselected in 4.50s`, line VERBATIM:
  `CUT ENGINE OUTPUT side=short formed_bar_ts=2026-01-07T15:24:00+00:00 trigger.price=0.6690 stop.price=0.87 anchor=Anchor(object='Extension', direction='up', bar_ts=datetime.datetime(2026, 1, 7, 15, 24, tzinfo=datetime.timezone.utc)) scan_instant=2026-01-07T15:26:40+00:00 formed_bar_ny=2026-01-07T10:24:00-05:00`
- The five constants re-copied from that line VERBATIM under the `DEF_WRITTEN_*` RULE, each comment `# engine on the corrected cut day at R4-F4 on 8da261a; a blind house re-derives it (13, [F-16] (1))` → `## PINS MOVED`. The geometry guard holds by the test (short → stop above trigger).

### A1 (commit 2)
| test | old | new | row |
|---|---|---|---|
| `test_setups_fixture_cut.py::test_rubberband_forms_on_the_cut_day` (the five `DEF_WRITTEN_RUBBERBAND_CUT_*` it asserts) | the mis-timed cut's values | the corrected cut's values (`## PINS MOVED`), same five assertions + the geometry guard, same strength | F4 (by design) |

`uv run pytest tests/cobalt/test_setups_fixture_cut.py tests/cobalt/test_setups_lego.py -q` → `14 passed in 131.42s (0:02:11)`; `grep -n "AWAITING_A_DAY" tests/cobalt/test_setups_lego.py` → `43:AWAITING_A_DAY: frozenset[str] = frozenset({"hitchhiker"})` (unchanged; gate 2's `CUT_DAY_CHECKS` passes on the re-cut).

### SUITE (commit 2)
OFFLINE → `2464 passed, 361 skipped, 1 xfailed, 15 warnings in 478.66s (0:07:58)` → **2464/0** (no new test in commit 2).

### COMMIT (commit 2)
`f5aaeb4 fix(setups): round 4 — F4 re-cut on the New York wall clock, pins re-copied (13 re-derives)` — `git show --stat HEAD`: `.../reports/setups-fix-r4-2026-09-22.md | 49 +-` · `tests/cobalt/test_setups_fixture_cut.py | 26 +-` · `.../radar/bars-setups-rubberband.real-shape.json | 1912 ++++++++++----------` · `.../membership-setups-rubberband.real-shape.json | 4 +-` · `4 files changed, 1017 insertions(+), 974 deletions(-)`. The cutter is not in it (the re-cut did not change it).

## F5
C3: the correspondence, in New York local time.

### C
T: the printing test `test_rubberband_cut_day_engine_output` gained ONE field, `formed_bar_ny=<formed_bar_ts in America/New_York, isoformat>` — added in F4's commit 2 (said so there); no assertion changed. C: `## C3` below. Every time in it is printed output (the stored day's from `12`'s `## FIND — rubberband` lines; the pin's from the new field) — none is my arithmetic (L35).

## C3
| source | line VERBATIM | formed bar, New York local |
|---|---|---|
| stored day, `12` `## FIND — rubberband` (the replay of the PRODUCTION-synced definition on `<real day>`), the cut ticker's FORMED line | `10:26:40 ET BTTC rubberband FORMED short trigger 0.6690 stop 0.87 (formation bar 10:24 ET)` | `10:24 ET` |
| corrected cut pin (the NEUTRAL test shape `setups_shapes.SHAPES["rubberband"]` on the re-cut fixture, F4 commit 2) | `CUT ENGINE OUTPUT side=short formed_bar_ts=2026-01-07T15:24:00+00:00 trigger.price=0.6690 stop.price=0.87 … formed_bar_ny=2026-01-07T10:24:00-05:00` | `10:24:00-05:00` |
| (for the record) the OLD, mis-timed cut pin, `12` `## PIN` 4.1 | `CUT ENGINE OUTPUT side=long formed_bar_ts=2026-01-07T15:34:00+00:00 trigger.price=0.8400 stop.price=0.66 …` | not printed then (no NY field) |

**Verdict: `CORRESPONDS — the stored day's BTTC line (short · trigger 0.6690 · stop 0.87 · formation bar 10:24 ET)`.** Side, trigger, stop and the New York formation-bar time all match the stored day's first BTTC line. The hour shift (cause (1) of the check) is REMOVED by F4 (`test_f4_an_edt_time_re_dated_onto_an_est_day_keeps_its_new_york_clock`, `test_f4_a_time_moves_by_its_new_york_local_date`). The definition difference (cause (2): the production-synced note vs the neutral shape, `12` ESCALATE (i)) is NOT RUN here (his note, L32; no production command in this line) — on this day it does not change the first formation. That is a reading of two printed lines, not proof the two definitions agree in general → UNPROVEN beyond that reading.

## PINS MOVED
F4 only; `tests/cobalt/test_setups_fixture_cut.py`. Blind seat that must re-derive them: **`13`** (on the re-cut fixture, AFTER this round).

| constant | old | new |
|---|---|---|
| `DEF_WRITTEN_RUBBERBAND_CUT_SIDE` | `"long"` | `"short"` |
| `DEF_WRITTEN_RUBBERBAND_CUT_FORMED_BAR` | `datetime.fromisoformat("2026-01-07T15:34:00+00:00")` | `datetime.fromisoformat("2026-01-07T15:24:00+00:00")` |
| `DEF_WRITTEN_RUBBERBAND_CUT_TRIGGER` | `"0.8400"` | `"0.6690"` |
| `DEF_WRITTEN_RUBBERBAND_CUT_STOP` | `"0.66"` | `"0.87"` |
| `DEF_WRITTEN_RUBBERBAND_CUT_ANCHOR` | `"Anchor(object='Extension', direction='down', bar_ts=datetime.datetime(2026, 1, 7, 15, 34, tzinfo=datetime.timezone.utc))"` | `"Anchor(object='Extension', direction='up', bar_ts=datetime.datetime(2026, 1, 7, 15, 24, tzinfo=datetime.timezone.utc))"` |

No other `DEF_WRITTEN_*` moved (the four committed-day pin files: CLOSE `git diff` EMPTY).

## CLOSE
- **OFFLINE** (the BASELINE command, on `f5aaeb4`) → `2464 passed, 361 skipped, 1 xfailed, 15 warnings in 480.40s (0:08:00)` → **2464/0**. Counted: base 2453 + 11 new cases in `tests/cobalt/test_setups_fix_r4.py` (8 `def test_` functions: F1 2 · F3 1 parametrised ×2 · F4 5, two of them parametrised ×2 → 2 + 2 + 7 = 11); skipped unchanged at 361.
- `git diff --stat 8da261a` → `.../reports/setups-fix-r4-2026-09-22.md | 182 ++` · `tests/cobalt/test_setups_fix_r3.py | 17 +-` · `tests/cobalt/test_setups_fix_r4.py | 118 ++` · `tests/cobalt/test_setups_fixture_cut.py | 30 +-` · `tests/fixtures/radar/_cut_setups_fixtures.py | 30 +-` · `.../radar/bars-setups-rubberband.real-shape.json | 1912 ++++++++++----------` · `.../membership-setups-rubberband.real-shape.json | 4 +-` · `7 files changed, 1315 insertions(+), 978 deletions(-)` — ONLY the listed paths; the daily CSV is not among them (unchanged).
- EMPTY, each its own call, each "no output": `git diff 8da261a -- src` · `git diff 8da261a -- configs` · `git diff 8da261a -- tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_nine_ema.py tests/cobalt/test_setups_vwap_cont.py tests/cobalt/test_setups_second_chance.py` · `git diff 8da261a -- tests/fixtures/radar/_cut_p2_fixtures.py` · `git diff 8da261a -- tests/cobalt/test_setups_lego.py`.
- **L32 SELF-CHECK:** `git status --porcelain` → no output (no line for `docs/_inflight/…`). The proposal file still carries values for `A-09`, `A-10`, `A-16` (read with the Read tool; A-09 and A-10 share one value): `grep -rn -F "<value>" tests/cobalt/test_setups_fix_r4.py`, one call each → proposal value 1 (A-09 / A-10): no hits · proposal value 2 (A-16): no hits. `grep -rn "2026-09-" tests/cobalt/test_setups_fix_r4.py tests/cobalt/test_setups_fixture_cut.py` → no output.
- `uv run cobalt jobs restarts 8da261a..HEAD` → VERBATIM:
```
path	change	rule	restart
docs/40 - DevDocs/reports/setups-fix-r4-2026-09-22.md	A	DOCS	-
tests/cobalt/test_setups_fix_r3.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_fix_r4.py	A	test/documentation; no resident	-
tests/cobalt/test_setups_fixture_cut.py	M	test/documentation; no resident	-
tests/fixtures/radar/_cut_setups_fixtures.py	M	test/documentation; no resident	-
tests/fixtures/radar/bars-setups-rubberband.real-shape.json	M	test/documentation; no resident	-
tests/fixtures/radar/membership-setups-rubberband.real-shape.json	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED`.
- `git log --oneline 8da261a..HEAD` (before the report commit): `f5aaeb4` F4 re-cut + pins · `c000411` F4 cutter · `b77d8e5` F3 · `2817896` F1. (F2: gitignored, no commit.)
- **L68** (`git -C /Users/cobalt/cobalt log --oneline 8da261a..<branch> -- <the 7 changed paths>`, one call per branch):

| branch | shared path | commits |
|---|---|---|
| `cards/stale-score-0922` | — | not cut (`fatal: bad revision '8da261a..cards/stale-score-0922'`) |
| `radar/handicap-h1-0922` | none | (no output) |

## WITH-DB OWED
"Every with-DB claim of rounds 2, 3 and 4 is UNPROVEN (L70) until `68-devdb-repair.md` lands. Owed on `<tip>` after `68`: `33`'s CLOSE with-DB set + `tests/cobalt/test_setups_fix_r3.py` + `tests/cobalt/test_setups_fix_r4.py`, inside the R41 `.env` pair, by a seat the desk names. Rows proven OFFLINE here: F1, F3, F4, F5 (tests), F2 (a gitignored file, no test). Rows that could NOT be proven offline: none — but `tests/cobalt/test_setups_lego.py` sits in the with-DB set and is re-run there."
`<tip>` = `f5aaeb4`.

## NOTE FOR THE DESK
"Check round 3 of 3 (the LAST, L39) = `prompts/2026-09-22/70-setups-check-r2r3.md`'s shape RE-POINTED (L19, a full re-issue) to this round's range `8da261a..<tip>` — its PREFLIGHT built line (`SETUPS FIX R4 BUILT … | on 8da261a |`), its range, its boundary (this round's CLOSE list), its packet (this round's diff; the re-cut bars file excerpted, never staged whole; this report's `## F1`–`## F5`, `## C3`, `## PINS MOVED`, `## ESCALATE`), its questions (F1–F5 of this round only, tagged `[R4]`). `13` (the blind re-derivation of the five `DEF_WRITTEN_RUBBERBAND_CUT_*` pins) runs AFTER this round, on the re-cut fixture — its pins' line numbers and the base named in `13` must be re-pointed; it is never pointed at the check's packet folder. Pins this round moved: <list> → `13`."
`<tip>` = `f5aaeb4`. `<list>` = `DEF_WRITTEN_RUBBERBAND_CUT_SIDE`, `_FORMED_BAR`, `_TRIGGER`, `_STOP`, `_ANCHOR` (`tests/cobalt/test_setups_fixture_cut.py`, now at L101 / L103 / L105 / L107 / L109-112 by `grep -n "^DEF_WRITTEN_RUBBERBAND_CUT_"` — +2 against `12`'s `## FOR 13`, from F5's import and printed field; `13` re-reads them by symbol).

## ESCALATE
(i) **F1 raise site:** the engine-key refusal is raised in **`merge_tunables`** (`src/cobalt/taxonomy/loader.py:114`, `TaxonomyConfigError`) and re-raised as `VaultTaxonomyError` by `_resolve_every_cfg` (`src/cobalt/taxonomy/vault_loader.py:601`), which `load_vault_trade_defs` calls (`:517`). So the how-to / r3 report's attribution to `merge_tunables` MATCHES the originating raise; the probe sees it through `load_vault_trade_defs`. Both readings of the check's NOT CHECKABLE row are true at different layers. The how-to is NOT edited (UNPROVEN row, L70).
(ii) **F2:** `A-24` → `null` / `status: null` in the gitignored proposal; `A-09`, `A-10`, `A-16` untouched (owner item Q3 is his). Left as they were (row-only rule): the file's line 12 paragraph that explains the old `A-24` value, and its closing tally `proposal: 4 proposed, 0 null` — both are now stale (the true tally is 3 proposed, 1 null). The desk may correct them; nothing of that file entered a commit.
(iii) **F3:** the CUT commit `65c08a0`'s message still carries the real day — history not rewritten (OUT OF SCOPE). (iii-a) **Wording deviation:** the row's prescribed docstring text `(see \`setups-fixture-cut-2026-09-22.md\`)` contains an ISO date (the filename's) that would keep F3's own allowlist pin RED and fail the CLOSE `2026-09-` grep. Safe default taken: the docstring names the report as "the fixture-cut report of prompt `12`, `## FIND — rubberband`". `ASK DESK: accept the undated reference, or re-issue F3's wording? [Tue Sep 22 22:06:48 EDT 2026]` — the default stands (the stamp is the time it was written here, from `date`; the deviation itself was made at F3, committed `b77d8e5` 21:45:26 EDT per `git show`).
(iv) **F4:** five pins moved (`## PINS MOVED`), old → new, blind seat **`13`**; the daily CSV diff: NONE (unchanged, as expected). (iv-b) `_DATETIME_RE`'s optional offset group was widened (`(?:\+00:00)?` → `(?:[+-]\d{2}:\d{2}|Z)?`) so a non-UTC offset reaches the new `SystemExit` rather than passing through unshifted and unreported — part of `_shift_datetime_str`'s own matcher, named because the row said "nothing else in the cutter changes". The re-cut's raw inputs are all `+00:00` (space separator); the output counts equal `12`'s.
(v) **F5:** `CORRESPONDS — the stored day's BTTC line (short · trigger 0.6690 · stop 0.87 · formation bar 10:24 ET)`. With the hour shift removed, the neutral shape's first formation on the cut is the stored day's first BTTC line. Cause (2), the definition difference, is not run here and stays UNPROVEN beyond this one reading.
(vi) `_cut_p2_fixtures.py` NOT touched: `git diff 8da261a -- tests/fixtures/radar/_cut_p2_fixtures.py` → (no output). The drafter's ESCALATE names a possible same-shape hour shift there. It is not a finding of this round. This round's C3 result (the shift moved a formation by one hour and flipped its side) makes that question worth the desk's look.
(vii) `WITH-DB: OWED (68)`.
(viii) `ASK DESK`: one — (iii-a), safe default taken.
(ix) `MEMORY:` / `RULING:` lines: none.
(x) **Slip, stated plainly (L35):** this session's FIRST command read the prompt file with `cat`, before the prompt (and its no-`cat` rule) had been read — the harness then saved the output and it was read with the Read tool. No other unlisted command was run; no call was denied.
(xi) Pins' line numbers in `test_setups_fixture_cut.py` shifted by +2 (the `ZoneInfo` import, the printing test's extra line): now L101–L112. `12`'s `## FOR 13` line numbers are stale; `13` must re-locate them by symbol (NOTE FOR THE DESK).
(xii) L74 recorded once above (`## L74`).

## CONTINUE
next: none — F1–F5 and CLOSE done (F1 `2817896`, F2 gitignored, F3 `b77d8e5`, F4 `c000411` + `f5aaeb4`, F5 in `f5aaeb4` + this report). `.env` never copied. A relaunch has nothing to build; the desk's next steps: check round 3 of 3 (`70` re-pointed), `13`, the with-DB set after `68`.

SETUPS FIX R4 BUILT f5aaeb4 | on 8da261a | offline 2464/0 | with-DB: OWED (68) | tests added: 11 (8 functions; three parametrised functions counted as their cases) | ESCALATE: 12
