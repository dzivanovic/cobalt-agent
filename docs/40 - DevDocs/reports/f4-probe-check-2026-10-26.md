# f4-probe — check report 2026-10-26

## §0 Headline
- Check of `f4-probe` at code tip `2e0d5f77`. House A Grok returned `FINDINGS: 0`. House B was not needed (`HOUSE B: as needed`).
- 7 own findings. 2 held: O1, a minute of exactly 50 passing, and O2, a 429 within the ceiling failing. These are the two halves of the `refresh_probe.py:375` pass rule. Neither was pinned: each mutant left the build's 14 tests green. Both are now pinned in tests and shown red on their mutants. No `src/` change.
- 5 not held: X1, X2, X3, X7, X8 and X9 hold. The default run is deterministic: `FAIL peak 53/min at 08:43`, 3 × 429 (radar), strike interval 30 s.
- Deploy gate on `07b507f96`: offline 9131/0 · with-DB 5967/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS: none. ready: YES.

## L74
A system reminder asked that commits carry a `Claude-Session:` line. Recorded once; not followed. Commits carry `Co-Authored-By` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1055-f4-probe-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1055-f4-probe-check-card.md" · 0 · 2a5d74ad1c2d5fbc164e7ee375b4f0c72269ef92
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1055-f4-probe-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (09:32 EDT): `grep -n "^| R17 "` → row 35 (STANDING `Bash(grok *)`); `grep -n "^| R19 "` → row 37 (four house strings pre-approved); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 26 09:32:50 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-probe
head · git log --oneline -1; git log --stat --format=%h 2e0d5f77..HEAD · 0 · (11 lines)
    1fcf33e8d docs(f4-probe): build report — 2e0d5f77 (stop line tip 8 hex)
    1fcf33e8d
     docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.md     | 5 +++--
     docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.result | 4 ++--
     2 files changed, 5 insertions(+), 4 deletions(-)
    1b25f0a1c
     .../reports/f4-probe-build-2026-10-26.md           | 133 ++++++++++++++++++++-
     .../reports/f4-probe-build-2026-10-26.result       |  15 +++
     2 files changed, 145 insertions(+), 3 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/f4-probe/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../f4-probe-build-2026-10-26.md" · 0 · BUILT · job: f4-probe · tip: 2e0d5f77 | on 596ca32f | migration: none | offline 4993/0 | with-DB 5965/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 80698
range · git log --oneline 596ca32f..2e0d5f77 · 0 · (2 lines)
    2e0d5f77b feat(f4-probe): prefill probe X15 on a virtual clock, the two X7 pins (P1, P2, X15, C1, T1, T2, D0; L1, L3, L28, L32, L45)
    5e03b1db5 wip(f4-probe): red — probe tests, the two X7 pins (P1, P2, X15, C1, T1, T2)
PREFLIGHT OK
```
THE RANGE typed: `git log --stat --format=%h 596ca32f..2e0d5f77` → 2e0d5f77b: `cli.md` 22+, `daily.md` 3+, `src/cobalt/prefill/cli.py` 12+, `src/cobalt/prefill/refresh_probe.py` 458+, `tests/cobalt/test_refresh_probe.py` 2+; 5e03b1db5: build report 89+, `tests/cobalt/test_prefill_refresh.py` 46+, `tests/cobalt/test_refresh_probe.py` 238+. Path union: 7 paths.
`ls <S>` → No such file or directory (fresh).
House probes (`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"`, exit 0): `grok: UP` · `gemini: UP`.
SEAT ORDER, no header line, `HOUSE B: as needed` → **house A: Grok (grok-4.7) · house B: none (not needed)**.
DB card (no `DB: none` line): with-DB strings proven at first use (gate.sh, `## 6`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
28 <S>/STAGED-CARD
32245 <S>/diff.md
16835 <S>/files/1055-f4-probe-check-card.md
23721 <S>/files/f4-probe-build-2026-10-26.md
3511 <S>/files/wt/docs/40 - DevDocs/cobalt/prefill/cli.md
11626 <S>/files/wt/docs/40 - DevDocs/cobalt/prefill/daily.md
7455 <S>/files/wt/docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.md
4626 <S>/files/wt/src/cobalt/prefill/cli.py
16995 <S>/files/wt/src/cobalt/prefill/refresh_probe.py
59388 <S>/files/wt/tests/cobalt/test_prefill_refresh.py
9003 <S>/files/wt/tests/cobalt/test_refresh_probe.py
386 <S>/rulings.md
STAGED 12 files · 185819 bytes · commits 2
```
`stage-copy.sh` (each `COPIED <bytes> <dest>`): 14813 `files/1047-f4-probe-card.md` · 78381 `files/wt/docs/30 - Design/F4-FINAL-2026-10-10.md` · 54690 `files/wt/src/cobalt/prefill/daily.py` · 15532 `files/wt/src/cobalt/strike/detector.py` · 10495 `files/wt/src/cobalt/archiver/collector.py` · 11570 `files/wt/src/cobalt/radar/collector.py` · 18467 `files/wt/src/cobalt/prefill/checkpoint_probe.py` · 3825 `files/wt/src/cobalt/env.py` · 10287 `files/wt/src/cobalt/daymode/note.py` · 3642 `files/wt/src/cobalt/prefill/market.py` · 3611 `files/wt/src/cobalt/prefill/calendar.py` · 8125 `files/wt/tests/cobalt/test_finviz_consumers.py` · 10603 `files/wt/tests/cobalt/test_daymode_note.py`.
`<S>/HOUSE-INSTRUCTIONS.md` written (18334 bytes). Grok started 09:34:42 EDT (`run_in_background`, timeout 2700000); `cd <WT>`; `git status --short --branch` → `## ops/f4-probe`.

## OWN FINDINGS
Written before any house list was opened. Tests go in `tests/cobalt/test_refresh_probe.py` (fixtures `probe`, helpers `x15`, `records` of that file) unless named otherwise.

FINDING O1
ROW: X4 (X15)
CLAIM: No test pins that a minute of exactly 50 passes: `src/cobalt/prefill/refresh_probe.py:375` `if peak > ceiling or throttled:` can become `peak >= ceiling` and every test of the file stays green (the default run's 08:43 is 53, `small()` peaks far under 50).
RUN: TEST
```python
def test_check_o1_a_minute_of_exactly_the_ceiling_passes(probe):
    hits = [probe.Hit("08:41", "radar", "/p", 200)] * 50
    verdict, clause = probe._clause(hits, probe._Ledger(), 50)
    assert verdict == "OK", clause
```
EXPECT: green on the tip; with `:375` mutated to `>=` this test fails `assert 'FAIL' == 'OK'` while the file's 15 tests stay `passed`.

FINDING O2
ROW: X4 (X15)
CLAIM: No test pins the `or throttled` half of `refresh_probe.py:375`: deleting it leaves every test green, because the mock answers 429 only past the ceiling (`:184`), so a 429 always rides with `peak > ceiling`.
RUN: TEST
```python
def test_check_o2_a_429_within_the_ceiling_fails(probe):
    hits = [probe.Hit("08:41", "radar", "/p", 200)] * 10 + [probe.Hit("08:41", "strike", "/p", 429)]
    verdict, clause = probe._clause(hits, probe._Ledger(), 50)
    assert verdict == "FAIL", clause
    assert "429 1 (strike=1)" in clause and probe.CONSEQUENCE in clause
```
EXPECT: green on the tip; with `or throttled` removed from `:375` it fails `assert 'OK' == 'FAIL'` while the file's 15 tests stay `passed`.

FINDING O3
ROW: X3, X8, X9
CLAIM: The default run (`refresh_probe.py:83` `SETUP`) is not the same line across three runs, labels a request outside radar/strike/refresh, or records a minute past 08:45 (`VirtualClock.run` `:143` stops at `RUN_S` `:59`); X9's shape `peak 53/min at 08:43`, `429 3 (radar=3)`, `strike interval 30 s` is re-derived from `strike/detector.py:108` (ceil(5×60/10) = 30 s → 10 rpm; 40 + 10 + 3 = 53).
RUN: TEST
```python
def test_check_o3_the_default_run_is_deterministic_and_stops_at_0846(monkeypatch, capsys, probe):
    lines = []
    for _ in range(3):
        probe.built.clear()
        code, line, _ = x15(monkeypatch, capsys, probe)
        lines.append(line)
        seen = records(probe)
        assert {r.consumer for r in seen} == {"radar", "strike", "refresh"}
        assert (min(r.minute for r in seen), max(r.minute for r in seen)) == ("08:40", "08:45")
        assert code == 1
    assert len(set(lines)) == 1, lines
    assert lines[0].startswith("PROBE X15 FAIL peak 53/min at 08:43 "), lines[0]
    assert "429 3 (radar=3)" in lines[0] and "strike interval 30 s" in lines[0]
```
EXPECT (claim true): one of the assertions fails.

FINDING O4
ROW: P2 (a), X2
CLAIM: An unknown `COBALT_ENV` value is not pinned (`test_refresh_probe.py:94` tests `production` and unset only); `_dev_only` (`refresh_probe.py:426-432`) may build a transport before refusing it.
RUN: TEST
```python
def test_check_o4_an_unknown_env_is_refused_before_any_request(monkeypatch, capsys, probe):
    monkeypatch.setenv("COBALT_ENV", "staging")
    code, line, _ = x15(monkeypatch, capsys, probe)
    assert (code, line) == (1, "PROBE X15 FAIL refused: COBALT_ENV is 'staging' — set it to one of production, dev.")
    assert probe.built == []
```
EXPECT (claim true): the tuple or `probe.built == []` assertion fails.

FINDING O5
ROW: P2 (c), X1
CLAIM: `test_no_write_no_db_no_token_no_launchctl` (`test_refresh_probe.py:106`) blocks named stores only, not the one `psycopg.connect` (`src/cobalt/db.py:199`); some path of the default run (`strike.config.check`, `load_tunables`, `load_job_registry`, `_gated_fetch`) may open a database.
RUN: TEST
```python
def test_check_o5_the_default_run_opens_no_database(monkeypatch, capsys, probe):
    import psycopg

    def boom(*a, **kw):
        raise AssertionError("the probe opened a database")

    monkeypatch.setattr(psycopg, "connect", boom)
    code, line, _ = x15(monkeypatch, capsys, probe)
    assert "error" not in line, line
    assert records(probe)
```
EXPECT (claim true): `assert "error" not in line` fails on `PROBE X15 FAIL error AssertionError`.

FINDING O6
ROW: X7 (T1, T2)
CLAIM: The code T1 and T2 exercise differs between BASE and the tip, so green on the tip does not show green on BASE.
RUN: COMMAND `git diff --stat 596ca32f 2e0d5f77 -- src/cobalt/prefill/daily.py src/cobalt/daymode src/cobalt/taxonomy src/cobalt/radar`
EXPECT (claim true): a non-empty stat.

FINDING O7
ROW: T2, X7
CLAIM: T2's first-line assertion (`tests/cobalt/test_prefill_refresh.py:531`) already holds before the daymode write (`:529`), so T2 stays green if the write does nothing.
RUN: TEST — `tests/cobalt/test_prefill_refresh.py`, class `TestStamp`
```python
    def test_check_o7_t2_holds_without_the_daymode_write(self, vault, finviz):
        store = MemoryStore()
        refresh(at(5, 15), store)
        body = unit_body(vault, "daymode", "sheet_mode").split("\n")
        assert re.match(r"^as of \d\d:\d\d ET$", body[0]), body[0]
```
EXPECT (claim true): passes.

## Findings
House A Grok: notice at 09:51:20 EDT; `<S>/house-a.md` (12 bytes, written by Grok) reads whole `FINDINGS: 0`. Its stdout: "The pass rule, the mock boundary, and the two pins hold on the copied tip. No break I can hand over as a failing run." House B: none (not needed, `HOUSE B: as needed`).
No house finding to keep.

## Dropped
none (Grok wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_refresh_probe.py::test_check_o1_…` on the tip; then `refresh_probe.py:375` → `peak >= ceiling` by Edit, `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_refresh_probe.py --deselect …::test_check_o3_…`, undone by Edit | tip: passed (in `4 passed` with O2, O4, O5). Mutant: `1 failed, 17 passed, 1 deselected in 94.35s` — only O1 red: `assert 'FAIL' == 'OK'` (`peak 50/min at 08:41 … → strike/refresh residual cannot ship as named …`); the build's 14 probe tests stayed green under the mutant | HELD — the boundary of `:375` had no pin (a test gap; the code is right) |
| O2 | opus-own | same, with `:375` → `if peak > ceiling:` (the `or throttled` half removed), undone by Edit | tip: passed. Mutant: `1 failed, 17 passed, 1 deselected in 94.57s` — only O2 red: `assert 'OK' == 'FAIL'` (`peak 11/min at 08:41 · … · 429 1 (strike=1) …`); the build's 14 stayed green | HELD — the `or throttled` half had no pin (a test gap; the code is right) |
| O3 | opus-own | `uv run pytest … ::test_check_o3_the_default_run_is_deterministic_and_stops_at_0846` (run again on the clean tree because the first run overlapped the O1 mutant edit) | `1 passed in 4.15s` (the first run: `1 passed in 4.26s`) | NOT HELD — three runs give the same line; consumers are radar, strike and refresh only; minutes run 08:40–08:45; the line starts `PROBE X15 FAIL peak 53/min at 08:43 ` with `429 3 (radar=3)` and `strike interval 30 s`. Removed. |
| O4 | opus-own | `uv run pytest … ::test_check_o4_…` | passed | NOT HELD — `COBALT_ENV=staging` → `PROBE X15 FAIL refused: COBALT_ENV is 'staging' — set it to one of production, dev.`, exit 1, no transport built. Removed. |
| O5 | opus-own | `uv run pytest … ::test_check_o5_…` | passed | NOT HELD — `psycopg.connect` set to raise; the default run's line has no `error` and requests reached the mock. Removed. |
| O6 | opus-own | `git diff --stat 596ca32f 2e0d5f77 -- src/cobalt/prefill/daily.py src/cobalt/daymode src/cobalt/taxonomy src/cobalt/radar` | empty. `git diff --stat 596ca32f 2e0d5f77 -- src` → `cli.py | 12 +`, `refresh_probe.py | 458 +` only | NOT HELD — the code T1 and T2 exercise is the same on BASE and the tip |
| O7 | opus-own | `uv run pytest … tests/cobalt/test_prefill_refresh.py::TestStamp::test_check_o7_…` | `1 failed`: `AssertionError: **Day mode: REDUCED** (fixture)` | NOT HELD — before the write, the unit is the fixture line, so T2's `as of` assertion needs the write. Removed. |

The two mutant runs and their undo: Edit → run → Edit; `git status --short --branch` afterwards → `## ops/f4-probe` plus ` M tests/cobalt/test_prefill_refresh.py` and ` M tests/cobalt/test_refresh_probe.py` (the check tests not yet removed); `refresh_probe.py` is clean.
CHECK ASKS answered: X1 — none of `from httpx import`, `aiohttp`, `requests`, `urllib`, `httpx.Client(` sits in `archiver/collector.py`, `prefill/market.py`, `prefill/calendar.py` or `strike/detector.py` (Grep over `src/cobalt`: the hits are `notify/mattermost.py`, `classify/*`, `heartbeat/probes.py`, `smoke/checks.py`, `modelaccess/adapters.py`, `db.py`, `radar/propose.py`, none on the probe path); O5 covers the database. X2 — O4 plus the build's `:94`. X3 — O3 (labels); `_x15` awaits `detector.tick()` (`:338`) and `daily._gated_fetch` (`:348`). X4 — O1, O2 (held, pinned); the 429 counts into the peak (`:191` appends every status; `test_x15_a_minute_above_50…:180` `len(minute) >= 51`). X5 — `test_x15_clause_holds_no_query_or_token` green (the card suite below). X6 — RESTARTS below: `cli.py` and `refresh_probe.py` `static import reach`, `-`; `refresh_probe` imports only `httpx`, `loguru` and `cobalt.env` at module level (`:45-48`), which `daily` already imports; the module-level `assert` (`:423`) is a constant. X7 — O6, O7. X8 — O3. X9 — `poll_interval(5, 10, floor)` = max(floor, ceil(300/10)) = 30 s → 10 rpm; 40 + 10 = 50 a minute; +3 at 08:43 = 53; the mock 429s requests 51–53 of that minute, all radar (O3's line).

## FIXES
- O1, O2: no `src/` change: the code is right and `src/` is fenced. The fix is the pins themselves, `tests/cobalt/test_refresh_probe.py::test_check_o1_a_minute_of_exactly_the_ceiling_passes` (`:243`) and `::test_check_o2_a_429_within_the_ceiling_fails` (`:249`), each red under its mutant (RUNS). `150296da0 wip(f4-probe): check red — O1, O2 …`; DevDocs line in `docs/40 - DevDocs/cobalt/prefill/cli.md`, `07b507f96 fix(f4-probe): the X15 pass rule's two halves pinned, DevDocs line (check O1, O2)`.
- The card's offline suite after both commits: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_refresh_probe.py tests/cobalt/test_prefill_refresh.py tests/cobalt/test_finviz_consumers.py` → `67 passed, 28 skipped, 4 xfailed in 97.06s` (the build's 65 + O1 + O2).

## Suites
RESTARTS: `uv run cobalt jobs restarts 596ca32f..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/prefill/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.md	A	DOCS	-
docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.result	A	DOCS	-
src/cobalt/prefill/cli.py	M	static import reach	-
src/cobalt/prefill/refresh_probe.py	A	static import reach	-
tests/cobalt/test_prefill_refresh.py	M	test/documentation; no resident	-
tests/cobalt/test_refresh_probe.py	A	test/documentation; no resident	-
RESTARTS: none
```
Gate: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-probe all --deploy --deploy-gate` (`run_in_background`) on HEAD `07b507f96` → exit 0, the verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9131/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5967/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-probe-all-20261026-095741.log
```
No SKIPPED line is marked `OUTSIDE the allowed set`. with-DB 5967 = the build's 5965 + O1 + O2 (pass 1 runs the offline tests again, on purpose). `offline 9131` includes `tests/ops` (`--deploy-gate`). `ls /Users/cobalt/cobalt-wt/f4-probe/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union (7): `docs/40 - DevDocs/cobalt/prefill/cli.md`, `…/prefill/daily.md`, the build report, `src/cobalt/prefill/cli.py`, `src/cobalt/prefill/refresh_probe.py`, `tests/cobalt/test_prefill_refresh.py`, `tests/cobalt/test_refresh_probe.py`: all in rows' `files`, plus the build report. My commits: `tests/cobalt/test_refresh_probe.py` (rows P1/P2/X15/C1) and `docs/40 - DevDocs/cobalt/prefill/cli.md` (row D0). No `src/` edit committed.

## Checked against the branch
- (i) `git log --oneline 2e0d5f77..HEAD -- . ":(exclude)docs"` → `150296da0 wip(f4-probe): check red — O1, O2 (…)`. `<tip now>` = `150296da`.
- (ii) `git log --stat --format=%h 2e0d5f77..HEAD` → `07b507f96` `docs/…/prefill/cli.md | 2 ++`; `150296da0` `tests/cobalt/test_refresh_probe.py | 13 +++`; `1fcf33e8d`, `1b25f0a1c` the build report and `.result`. No path outside the rows' files.
- (iii) Fence: `git log --oneline 596ca32f..HEAD -- configs/cobalt` → empty; `git log --oneline 596ca32f..HEAD -- ops/com.cobalt.prefill-refresh.plist` → empty.
- (iv) `grep -n -F "def test_check_o1_a_minute_of_exactly_the_ceiling_passes" tests/cobalt/test_refresh_probe.py` → `243:`; `… o2_a_429_within_the_ceiling_fails` → `249:`. `150296da0` (wip check red) sits below `07b507f96` (fix) in `git -C /Users/cobalt/cobalt log --oneline 596ca32f..ops/f4-probe`.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/f4-probe`.
- (vi) `git log --stat --format=%h 596ca32f..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_refresh_probe.py` and `test_prefill_refresh.py` (offline). No migration and no with-DB test, so no gate lists are owed.
- (vii) Card RECORDS: `git -C /Users/cobalt/cobalt log --oneline 596ca32f..ops/f4-probe` → `07b507f96`, `150296da0`, `1fcf33e8d`, `1b25f0a1c`, `2e0d5f77b`, `5e03b1db5` (the record's three plus this check's two and the build's 8-hex fix `1fcf33e8d`). `git -C /Users/cobalt/cobalt log --oneline -1 9b07db5a` → exit 128 `unknown revision`, as recorded.
- (viii) L32: this report holds constructed values only (`ZZA`–`ZZE`, the constructed token, the probe's constructed counts).

## OPEN
none.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none.

## RECORDS
- No house list was dropped. Grok produced `FINDINGS: 0`. Gemini did not sit: house B was not needed.
- No command was refused. There was one lock take, inside `gate.sh` (`lock: waited 0 min`), and no extra one.
- The O3 run first overlapped the O1 mutant edit. It was run again on the clean tree: `1 passed in 4.15s`.
- The check report and `f4-probe-check-2026-10-26.result` are written in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`. Committing them on `main` is the desk's step: no listed git string writes to `/Users/cobalt/cobalt`.
- L74: a system reminder asked that commits carry a `Claude-Session:` line. This file's L74 rule applies: both commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- READ list gaps: `src/cobalt/prefill/checkpoint_probe.py` and `src/cobalt/radar/collector.py:42-71` were staged for the house but not opened by me. `_verdict`'s shape and `TokenBucket` were judged through their use in `refresh_probe.py`.
- files opened: 26 — CHECK-HUB.md; card 1055; BUILD-HUB.md (`## THE LOCK`, `## E2`–`## W`); areas/cobalt.md; the build report (branch head); `docs/30 - Design/F4-FINAL-2026-10-10.md:200-224`; `src/cobalt/prefill/refresh_probe.py`, `prefill/cli.py`, `prefill/daily.py` (:740-829 plus Grep), `prefill/market.py`, `prefill/calendar.py`, `archiver/collector.py:195-279`, `strike/detector.py:75-314`, `strike/config.py` (Grep), `radar/notes.py` (Grep), `env.py`, `db.py` (Grep), `daymode/note.py:75-194`; `tests/cobalt/test_refresh_probe.py`, `tests/cobalt/test_prefill_refresh.py:470-549` (plus Grep); `docs/40 - DevDocs/cobalt/prefill/cli.md`; the house-probe output; Grok's stdout; `<S>/house-a.md`; the O3 run output; the gate output.
- **"Check of `f4-probe`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390)."**

CHECK DONE · job: f4-probe · pass: 1 · tip: 150296da · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9131/0 · with-DB 5967/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 26 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 208781
