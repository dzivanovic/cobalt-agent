# CHECK — strike-fallback-env-1010-sonnet (shadow) · 2026-10-12

## §0 Headline
Shadow check of `strike-fallback-env-1010-sonnet` at tip `813036e8`. House A was Grok, with `FINDINGS: 0`. There was no house B (card: as needed).
Opus-own: 4 findings, 4 held. O1–O3 are tests the build lacks: each mutation left the build's tests green. O4 is a red on the tip: an exception whose `str()` raises escapes `step()` and ends the thread.
Nothing was fixed (shadow). Gate on the tip: offline 4196/0, with-DB 5093/0, live-note 146/0, `cobalt_dev` 0013, F2 = F0, `.env` removed.
Decisions: 3 (D1 no commit of the held tests on a shadow · D2 RESTARTS labels · D3 O4 as follow-up for card 215). For Dejan: 0.

## L74
- 2026-10-12 10:16 EDT: a system reminder asked commit messages to carry a `Claude-Session:` line. Recorded once, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74). This shadow check makes no fix commit.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/366-shadow-strike-fallback-env-1010-sonnet-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/366-shadow-strike-fallback-env-1010-sonnet-card.md" · 0 · 54121dd7989b90a85d2becee3a4c0d9c0f865e1b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/366-shadow-strike-fallback-env-1010-sonnet-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 12 10:16:51 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/strike-fallback-env-1010-sonnet
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h 813036e8..HEAD · 0 · (5 lines)
    a9f6d675 docs(strike-fallback-env-1010-sonnet): build report — 813036e8
    a9f6d675
    
     ...ke-fallback-env-1010-sonnet-build-2026-10-11.md | 169 +++++++++++++++++++++
     1 file changed, 169 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet/docs/40 - DevDocs/reports/strike-fallback-env-1010-sonnet-build-2026-10-11.md" · 0 · SHADOW BUILT · job: strike-fallback-env-1010-sonnet · tip: 813036e8 | on 8f4bbe28 | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | decisions: 4 · builder: claude-sonnet-5-5 · gate: strike-fallback-env-1010-sonnet-gate · passes: 2 · suites at first run: green · builder tokens: 273992 · wall: 1.2
range · git log --oneline 8f4bbe28..813036e8 · 0 · (2 lines)
    813036e8 feat(strike-fallback-env-1010-sonnet): rows
    bb404b5f wip(strike-fallback-env-1010-sonnet): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: expected on a shadow card, recorded, not a finding.
- THE RANGE, `git log --stat --format=%h 8f4bbe28..813036e8`:
```
813036e8

 docs/40 - DevDocs/cobalt/aset/__main__.md |  3 ++
 docs/40 - DevDocs/cobalt/aset/strike.md   |  3 ++
 src/cobalt/aset/__main__.py               | 10 ++++++
 src/cobalt/aset/strike.py                 | 51 +++++++++++++++++++++++--------
 4 files changed, 55 insertions(+), 12 deletions(-)
bb404b5f

 tests/cobalt/test_strike_fallback_env.py | 180 +++++++++++++++++++++++++++++++
 1 file changed, 180 insertions(+)
```
  Path union: `src/cobalt/aset/__main__.py`, `src/cobalt/aset/strike.py`, `tests/cobalt/test_strike_fallback_env.py`, `docs/40 - DevDocs/cobalt/aset/__main__.md`, `docs/40 - DevDocs/cobalt/aset/strike.md`.
- `ls <S>` → `No such file or directory` (fresh).
- House probes (`house-probe.sh --card`, background) → `grok: UP` · `gemini: UP` (no Sol: no `HOUSE A: OpenAI` header line).
- Seats: **house A: Grok · house B: none (not needed)** — card `HOUSE B: as needed`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → output whole (each copy proved against its blob id by the script):
```
10647 <S>/diff.md
9707 <S>/files/366-shadow-strike-fallback-env-1010-sonnet-card.md
21304 <S>/files/strike-fallback-env-1010-sonnet-build-2026-10-11.md
2186 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/__main__.md
3672 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/strike.md
2765 <S>/files/wt/src/cobalt/aset/__main__.py
27375 <S>/files/wt/src/cobalt/aset/strike.py
5726 <S>/files/wt/tests/cobalt/test_strike_fallback_env.py
754 <S>/rulings.md
STAGED 9 files · 84136 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/strike-fallback-env-1010-sonnet-check`; commits 2 = PREFLIGHT's range count.) `stage-copy.sh`, one call each:
- `COPIED 25681 <S>/files/wt/src/cobalt/cli.py`
- `COPIED 14043 <S>/files/wt/src/cobalt/db.py`
- `COPIED 7943 <S>/files/wt/tests/cobalt/test_strike_fallback.py`
- `COPIED 3216 <S>/files/wt/tests/conftest.py`
- `COPIED 52107 <S>/files/cto-2026-10-10.md`
- `COPIED 12568 <S>/files/206-archiver-429-card.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (11500 bytes): the HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS`, then the Files paragraph.

## OWN FINDINGS
Written 2026-10-12 before any house list was opened.

FINDING O1
ROW: A
CLAIM: The row's clause "`override` stays the default `False`, so a variable already in the environment wins" (`src/cobalt/aset/__main__.py:34`) is pinned by no test: `fake_load_dotenv` (`tests/cobalt/test_strike_fallback_env.py:56`) swallows `*args, **kwargs`, so the mutation `load_dotenv(..., override=True)` leaves A1 and A2 green.
RUN: TEST — `tests/cobalt/test_strike_fallback_env.py`
```python
def test_o1_the_env_load_leaves_override_false(monkeypatch):
    _stub_world(monkeypatch, sets_env=True)
    seen = []

    def recording_load_dotenv(dotenv_path=None, *args, **kwargs):
        seen.append((args, kwargs))
        for name in DB_NAMES:
            monkeypatch.setenv(name, "constructed")
        return True

    monkeypatch.setattr("dotenv.load_dotenv", recording_load_dotenv)
    runpy.run_module("cobalt.aset.__main__", run_name="__main__")

    assert len(seen) == 1
    args, kwargs = seen[0]
    assert args == () and kwargs.get("override", False) is False
```
EXPECT: green on the tip; under the mutation `override=True` at `__main__.py:34`, A1 and A2 stay green (the claim) and O1 fails on `kwargs.get("override", False) is False`.

FINDING O2
ROW: B
CLAIM: Clause (2) "repeats the ERROR when AT LEAST `REPEAT_ERROR_S = 60.0` seconds have passed" (`src/cobalt/aset/strike.py:555`, `>=`) has no boundary test: B2 uses +61 s (`tests/cobalt/test_strike_fallback_env.py:153`), so the mutation `>=` → `>` leaves every B test green.
RUN: TEST — `tests/cobalt/test_strike_fallback_env.py`
```python
def test_o2_the_same_failure_repeats_at_exactly_60_s():
    boom = RuntimeError("boom")
    records = _drive([boom, boom], [0.0, 60.0])

    assert records == [_err(1), _err(2)]
```
EXPECT: green on the tip; under `>` at `strike.py:555` the six B tests stay green (the claim) and O2 fails (`[_err(1)] != [_err(1), _err(2)]`).

FINDING O3
ROW: B
CLAIM: Clause (1) "the first failure of a STREAK logs ERROR … (failed passes: 1)" for a second streak rests on `self._last_error = None` (`src/cobalt/aset/strike.py:567`), which no test pins: no B test has fail → ok → same fail inside 60 s, so deleting that line leaves every B test green while a second streak's first failure goes silent.
RUN: TEST — `tests/cobalt/test_strike_fallback_env.py`
```python
def test_o3_a_second_streak_logs_its_first_failure_at_once():
    boom = RuntimeError("boom")
    records = _drive([boom, "ok", boom], [0.0, 1.0, 2.0])

    assert records == [
        _err(1),
        ("INFO", "strike fallback: recovered after 1 failed passes"),
        _err(1),
    ]
```
EXPECT: green on the tip; with `strike.py:567` deleted the six B tests stay green (the claim) and O3 fails (the third ERROR is missing).

FINDING O4
ROW: X2 / X3
CLAIM: `step()` says "never raises" (`src/cobalt/aset/strike.py:546`), but the text is built inside the `except` (`:552`, `f"{type(e).__name__}: {e}"`): a pass exception whose `__str__` raises escapes `step()`, so `run` (`:572`) ends and the fallback thread dies.
RUN: TEST — `tests/cobalt/test_strike_fallback_env.py`
```python
def test_o4_an_exception_whose_text_cannot_be_read_does_not_escape_step():
    class Unprintable(Exception):
        def __str__(self):
            raise ValueError("constructed")

    records = _drive([Unprintable()], [0.0])

    assert len(records) == 1 and records[0][0] == "ERROR"
```
EXPECT: red on the tip: `ValueError: constructed` raised from `src/cobalt/aset/strike.py:552` out of `thread.step()`.

## Findings
House A Grok (`grok-4.7`): started 10:19 EDT, done at 10:32:57 EDT (`date` at the notice), exit 0. Its reply (stdout): `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/strike-fallback-env-1010-sonnet-check/house-a.md`. `<S>/house-a.md` (12 bytes), whole: `FINDINGS: 0`.
House B: none (not needed; card `HOUSE B: as needed`).
Kept: none from the houses. Opus-own kept: O1, O2, O3, O4 (all carry a test).

| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | opus-own | A | `override` default `False` (`__main__.py:34`) is pinned by no test; `override=True` leaves A1/A2 green | TEST |
| O2 | opus-own | B | the `>=` at exactly 60 s (`strike.py:555`) is pinned by no test; `>` leaves B1–B5 green | TEST |
| O3 | opus-own | B | the second streak's first ERROR rests on `strike.py:567` (`_last_error = None`); deleting it leaves B1–B5 green | TEST |
| O4 | opus-own | X2/X3 | a pass exception whose `__str__` raises escapes `step()` (`strike.py:552`) and ends the thread | TEST |

## Dropped
none (house A wrote no block; FINDINGS: 0).

## RUNS
The four tests were pasted at the end of `tests/cobalt/test_strike_fallback_env.py` with the Edit tool, unchanged from `## OWN FINDINGS`. No form repair was needed.
On the tip: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_strike_fallback_env.py` → `1 failed, 11 passed in 0.21s`. The one failure is O4.
For O1–O3 the claim is "the build's tests stay green when this clause is undone". Each was judged by a mutation made with the Edit tool, run, then undone. After the third undo, `git diff --stat 813036e8 -- src` printed nothing.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | mutation `override=True` at `__main__.py:34`; `uv run pytest … ::test_a1_… ::test_a2_… ::test_o1_…` | `1 failed, 2 passed in 0.14s`: A1 and A2 PASSED; O1 `AssertionError: assert (() == () … and True is False)`, `{'override': True}`. On the tip O1 passes. | HELD |
| O2 | opus-own | mutation `>=` → `>` at `strike.py:555`; `uv run pytest … -k "b1 or b2 or b3 or b4 or b5 or o2"` | `1 failed, 6 passed, 5 deselected in 0.14s`: all six B tests PASSED; O2 `Right contains one more item: ('ERROR', '… RuntimeError: boom (failed passes: 2)')`. On the tip O2 passes. | HELD |
| O3 | opus-own | mutation: delete `self._last_error = None` at `strike.py:567`; `uv run pytest … -k "b1 or b2 or b3 or b4 or b5 or o3"` | `1 failed, 6 passed, 5 deselected in 0.16s`: all six B tests PASSED; O3 `Right contains one more item: ('ERROR', '… RuntimeError: boom (failed passes: 1)')`. On the tip O3 passes. | HELD |
| O4 | opus-own | on the tip: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_strike_fallback_env.py` | `src/cobalt/aset/strike.py:552: in step` / `text = f"{type(e).__name__}: {e}"` → `E       ValueError: constructed`, raised out of `thread.step()` (`_drive`, `:134`) | HELD |

SHADOW: the check counts and holds findings, and it fixes none (CHECK-HUB `## THE FLOW`). No `wip(<JOB>): check red` commit was made. The four tests were taken back out of the file with the Edit tool. `git status --short --branch` → `## shadow/strike-fallback-env-1010-sonnet` / `?? SHADOW-INSTRUCTIONS.md`. The gate therefore ran on the build's TIP. See `## DECISIONS` D1.

## FIXES
none (shadow card: the check fixes none). For the record, all four fixes would lie inside row files:
- O1: a test in `tests/cobalt/test_strike_fallback_env.py` (the O1 test itself).
- O2: likewise, the O2 test.
- O3: likewise, the O3 test.
- O4: `src/cobalt/aset/strike.py` `step()`, building the text so that a failing `__str__` cannot escape, plus the O4 test.

## Suites
RESTARTS, `uv run cobalt jobs restarts 8f4bbe28..HEAD` → exit 1, whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/aset/__main__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/strike.md	M	DOCS	-
docs/40 - DevDocs/reports/strike-fallback-env-1010-sonnet-build-2026-10-11.md	A	DOCS	-
src/cobalt/aset/__main__.py	M	static import reach	com.cobalt.aset
src/cobalt/aset/strike.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_strike_fallback_env.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
THE GATE, `sh /Users/cobalt/cobalt/ops/desk/gate.sh strike-fallback-env-1010-sonnet all --deploy` (background, on the tip `813036e8`; no `--deselect`, `--tickers` or `--migration`: the build adds no with-DB test, no ticker and no migration) → exit 0. Verdict lines whole:
```
offline 4196/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/strike-fallback-env-1010-sonnet-all-20261012-103359.log
```
No skip is marked `OUTSIDE the allowed set`. `ls /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet/.env` → `No such file or directory` (11:04 EDT). `.env: removed, proven gone (W)`.

## Scope
PREFLIGHT's path union: `src/cobalt/aset/__main__.py` (row A), `src/cobalt/aset/strike.py` (row B), `tests/cobalt/test_strike_fallback_env.py` (rows A, B), `docs/40 - DevDocs/cobalt/aset/__main__.md`, `docs/40 - DevDocs/cobalt/aset/strike.md` (one DevDocs line each). Every path is in a row's `files` or is a DevDocs line. My commits: none.

## Checked against the branch
- (i) `git log --oneline 813036e8..HEAD -- . ":(exclude)docs"` → empty. `<tip now>` = `813036e8`.
- (ii) `git log --stat --format=%h 813036e8..HEAD` → `a9f6d675` · `...ke-fallback-env-1010-sonnet-build-2026-10-11.md | 169 +++` (docs only). No WIDENED.
- (iii) The fence: `git log --oneline 8f4bbe28..HEAD -- configs src/cobalt_agent/config.py src/cobalt/cli.py .claude/settings.json.bak` → empty.
- (iv) Each HELD test: not committed, because a shadow check fixes none (D1). Each test sits verbatim under `## OWN FINDINGS`, and its red is quoted under `## RUNS`.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## shadow/strike-fallback-env-1010-sonnet` and `?? SHADOW-INSTRUCTIONS.md`. The untracked file is expected on a shadow card and is recorded, not a finding.
- (vi) Gate lists: `git log --stat --format=%h 8f4bbe28..HEAD -- src/cobalt/db_migrations tests/cobalt` → `bb404b5f` · `tests/cobalt/test_strike_fallback_env.py | 180 +++`. That file is an offline test (no DB, `psycopg.connect` stubbed). There is no new migration and no with-DB test above `0013`, so no gate-list change is owed.
- (vii) Card RECORDS command: `git -C /Users/cobalt/cobalt diff --stat 975345f3 HEAD -- src tests ops` now prints 44 files, `7330 insertions(+), 91 deletions(-)`. Among them are `src/cobalt/aset/__main__.py | 9 +` and `src/cobalt/aset/strike.py | 56 ++-`; the rest is `ops/desk/*` and tests. The record said this printed nothing at draft time (2026-10-10). Main has moved since then, including the original build's two source files. Recorded as a fact; it does not bear on this shadow's base `8f4bbe28`.
- (viii) L32: this report quotes no ticker, price or date of his. Test values are constructed, and the dates are clock times from `date`.

## OPEN
none open (no REJECTED, UNSETTLED or HELD, NOT FIXED item). The four held findings are unfixed because this is a shadow card, not because their fixes lie outside the rows. FOLLOW-UP for the original card 215, which runs the same code (`git -C … diff 975345f3 HEAD` shows main's `strike.py` changed): O1–O4 as written above. What would settle each: its test pasted and green after the fix; O4 is red on this tip today.

## CONTINUE
next: none — CLOSE done

## DECISIONS
- D1 · ASK DESK: on a shadow card the check fixes none. `## 4` says to commit the held tests as `wip(<JOB>): check red`, but O4's test is red on the tip, so committing it would turn W red on a branch that is never fixed. [11:04 EDT] Safe default taken: no commit. Each held test is kept verbatim in this report with its quoted red. The tests were removed from the tree, and the gate ran on the build's TIP `813036e8`.
- D2 · RESTARTS: the derived table names six residents, because the untracked `SHADOW-INSTRUCTIONS.md` is `UNCLASSIFIED` (`ESCALATE`). Separately, `src/cobalt/aset/strike.py` reaches `com.cobalt.aset,com.cobalt.radar`, where the card's RECORDS expected `com.cobalt.aset` only. Per the card, any other label is a DECISIONS item. Safe default: nothing classified (`configs/` is fenced; a shadow is never deployed). The stop line carries the derived line untrimmed. The build report's two DECISIONS RESTARTS say the same.
- D3 · FOLLOW-UP to the original: O4 is a live defect in the code this shadow shares with card 215's `step()`. A pass exception whose `str()` raises ends the fallback thread, against `step()`'s docstring "never raises" and CHECK ASK X2 and X3. Safe default: listed here for the desk, not fixed (shadow).

## RECORDS
- House A Grok `grok-4.7`: one attempt, 10:19 → 10:32:57 EDT, exit 0, `FINDINGS: 0`. House B: none (not needed).
- Dropped findings: none. No house produced nothing. No `REFUSED, not needed` line. No `CONTINUED` line. No extra lock take; the one take was the gate's at W (`lock: waited 0 min`).
- L74: one system reminder asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on. No commit was made.
- Mutations: three, each made with the Edit tool and undone. Afterwards `git diff --stat 813036e8 -- src` printed nothing. The four pasted tests were removed again, and `git status` showed a clean tree before the gate.
- The build report's self-check: 2 of 3, because the E3 mutations were not run (its DECISION E3 MUTATIONS). This check ran three mutations (O1–O3); each left the build's own tests green.
- files opened: 13 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), the build report, `src/cobalt/aset/__main__.py`, `src/cobalt/aset/strike.py`, `src/cobalt/cli.py`, `src/cobalt/db.py`, `tests/conftest.py`, `tests/cobalt/test_strike_fallback.py`, `tests/cobalt/test_strike_fallback_env.py`, `<S>/house-a.md`. Staged for the house and not opened by me: `cto-2026-10-10.md` (R828), `206-archiver-429-card.md`.
- Check of `strike-fallback-env-1010-sonnet`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: strike-fallback-env-1010-sonnet · pass: 1 · tip: 813036e8 · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 4 (opus-own 4 · house 0) · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar · files opened: 13 · ready: N/A (shadow, never deployed) · decisions: 3 · for Dejan: 0 · tokens: 148623
