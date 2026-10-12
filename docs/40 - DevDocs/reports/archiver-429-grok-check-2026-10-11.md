# archiver-429-grok — check report (2026-10-11 card, run 2026-10-12)

## §0 Headline

This is a shadow check of Grok's build `archiver-429-grok` at tip `3e60d5f6`. House A, Grok, returned `FINDINGS: 0`; no house B sat (not needed). I wrote 8 findings and ran each one: **1 held** (O1: `Retry-After: 7.5` gives `retry_after == 7.5`, but delta-seconds is digits only) and 7 did not. Following the shadow rule, nothing was fixed and no commit of mine is on the branch.
The deploy gate on the tip is green: offline 4139/0, with-DB 5028/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed.
X1–X4 were all answered "no defect" by run (O4–O7). `held: 1 (opus-own 1 · house 0)`. `ready: N/A (shadow, never deployed)`.
3 decisions, none for Dejan: O1's test was kept out of the tree, the log was not staged, and RESTARTS flags the untracked harness file.

## L74

A system reminder in this session asked that commits end with a `Claude-Session:` line. It is recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/378-shadow-archiver-429-grok-card.md"` · exit 0 · whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/378-shadow-archiver-429-grok-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/378-shadow-archiver-429-grok-card.md" · 0 · df562ef73d7d3275922f19e3f44c620a794c9857
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/378-shadow-archiver-429-grok-card.md" · 0 · nothing
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

House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · 0 · one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (STANDING: `Bash(grok *)` pre-approved).
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · 0 · one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (STANDING: the four house strings pre-approved).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT

- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · whole:
```
clock · date · 0 · Mon Oct 12 14:32:10 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/archiver-429-grok
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h 3e60d5f6..HEAD · 0 · (5 lines)
    41614bd8 docs(archiver-429-grok): build report — 3e60d5f6
    41614bd8
    
     .../reports/archiver-429-grok-build-2026-10-11.md  | 197 +++++++++++++++++++++
     1 file changed, 197 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/archiver-429-grok/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/archiver-429-grok/docs/40 - DevDocs/reports/archiver-429-grok-build-2026-10-11.md" · 0 · SHADOW BUILT · job: archiver-429-grok · tip: 3e60d5f6 | on fa968552 | offline 4139/0 | with-DB 5028/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | decisions: 2 · builder: grok-4.7 · gate: archiver-429-grok-gate · passes: 2 · suites at first run: green · builder tokens: UNKNOWN · wall: 12.2
range · git log --oneline fa968552..3e60d5f6 · 0 · (2 lines)
    3e60d5f6 feat(archiver-429-grok): rows
    d78f4669 wip(archiver-429-grok): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md` at the worktree root: expected on a shadow card, recorded here, not a finding.
- THE RANGE · `git log --stat --format=%h fa968552..3e60d5f6` · 0 ·
```
3e60d5f6

 docs/40 - DevDocs/cobalt/archiver/collector.md |  4 ++
 docs/40 - DevDocs/cobalt/archiver/report.md    |  4 ++
 docs/40 - DevDocs/cobalt/archiver/runner.md    |  4 ++
 src/cobalt/archiver/collector.py               | 39 +++++++++-
 src/cobalt/archiver/report.py                  | 34 +++++++++
 src/cobalt/archiver/runner.py                  | 99 +++++++++++++++++++++++---
 6 files changed, 175 insertions(+), 9 deletions(-)
d78f4669

 tests/cobalt/test_archiver_collector.py |  59 ++++++++
 tests/cobalt/test_archiver_report.py    |  22 +++
 tests/cobalt/test_archiver_runner.py    | 248 ++++++++++++++++++++++++++++++++
 3 files changed, 329 insertions(+)
```
  The paths changed in the range: the three DevDocs pages, `src/cobalt/archiver/{collector,report,runner}.py`, and `tests/cobalt/test_archiver_{collector,report,runner}.py`.
- The card does not say "DB: none", so the DB-none diff row does not apply.
- `ls <S>` · 1 · `No such file or directory`, so this is a fresh check.
- THE HOUSE PROBES · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) · 0 · whole:
```
grok: UP
gemini: UP
```
- Seats: **house A: Grok · house B: none (not needed)**. The card reads `HOUSE B: as needed` and has no `HOUSE A:` header line.
- Self-check: on a shadow card the build line carries no self-check field. The build report's PRE-STOP SELF-CHECK reads "2 of 3" because the mutations were not run. This goes to the house as a fact.

## Files copied

`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · whole (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/archiver-429-grok-check`):
```
26255 <S>/diff.md
12693 <S>/files/378-shadow-archiver-429-grok-card.md
21713 <S>/files/archiver-429-grok-build-2026-10-11.md
3082 <S>/files/wt/docs/40 - DevDocs/cobalt/archiver/collector.md
5802 <S>/files/wt/docs/40 - DevDocs/cobalt/archiver/report.md
11961 <S>/files/wt/docs/40 - DevDocs/cobalt/archiver/runner.md
10294 <S>/files/wt/src/cobalt/archiver/collector.py
12433 <S>/files/wt/src/cobalt/archiver/report.py
25474 <S>/files/wt/src/cobalt/archiver/runner.py
9660 <S>/files/wt/tests/cobalt/test_archiver_collector.py
5153 <S>/files/wt/tests/cobalt/test_archiver_report.py
47393 <S>/files/wt/tests/cobalt/test_archiver_runner.py
754 <S>/rulings.md
STAGED 13 files · 192667 bytes · commits 2
```
The commit count, 2, matches PREFLIGHT's range. The `## READ` files the script cannot derive were copied with `stage-copy.sh`:
- `COPIED 30852 <S>/files/wt/src/cobalt/radar/notes.py`
- `COPIED 19699 <S>/files/wt/configs/cobalt/jobs.yaml`
- `logs/archiver.err` was not copied. It holds his real tickers and times (L32), and the card's `## RECORDS` quote the lines it relies on. This is under `## DECISIONS` (ASK DESK).

`<S>/HOUSE-INSTRUCTIONS.md` was written: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS`, and the Files paragraph.

House A, Grok, was started at 14:34 (`date` → `Mon Oct 12 14:34:00 EDT 2026`, the gates R17 and R19 re-grepped, one row each), from `<AGY>`, in the background. There is no house B.

## OWN FINDINGS

I wrote these after reading the card, the diff `fa968552..3e60d5f6`, the touched files at the tip and the build report sections, and before opening anything a house wrote. Correction made at close: `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down) was NOT read before these findings. I read it at `## 8`, and nothing in it changes a finding: the change touches no platform, trade, secret or sizing. Each test uses only helpers its file already has at the tip: `_mock_finviz_status` in the collector file, and `wired`, `run`, `settings`, `scripted_fetcher`, `_rate_limited`, `_record_sleep`, `bar`, `ts`, `NIGHT_1` and `FakeStore` in the runner file.

FINDING O1
ROW: A1
CLAIM: `_retry_after_seconds` (`src/cobalt/archiver/collector.py:185–198`, the match at `:193`) accepts a decimal such as `7.5` through `_DELTA_SECONDS = r"\d+(?:\.\d+)?"` (`:52`). Delta-seconds is digits only (RFC 9110 §10.2.3, `1*DIGIT`), and the row says anything that is not delta-seconds → `None`.
RUN: TEST `tests/cobalt/test_archiver_collector.py`
```python
def test_check_retry_after_decimal_is_not_delta_seconds(monkeypatch):
    from cobalt.archiver.collector import FinvizRateLimited, fetch_bars

    _mock_finviz_status(monkeypatch, 429, {"Retry-After": "7.5"})
    with pytest.raises(FinvizRateLimited) as caught:
        asyncio.run(fetch_bars("TESTARCH", Interval.I5, "synthetic-token"))
    assert caught.value.retry_after is None
```
EXPECT: `assert 7.5 is None`.

FINDING O2
ROW: A1
CLAIM: No test pins the row's clause "an HTTP-date or unparseable → `None`". Only an absent header is pinned (`tests/cobalt/test_archiver_collector.py:230`). A negative, an HTTP-date, a word or an empty value could reach the runner as a number.
RUN: TEST `tests/cobalt/test_archiver_collector.py`
```python
@pytest.mark.parametrize(
    "header", ["Wed, 21 Oct 2026 07:28:00 GMT", "-5", "soon", ""]
)
def test_check_retry_after_not_delta_seconds_is_none(monkeypatch, header):
    from cobalt.archiver.collector import FinvizRateLimited, fetch_bars

    _mock_finviz_status(monkeypatch, 429, {"Retry-After": header})
    with pytest.raises(FinvizRateLimited) as caught:
        asyncio.run(fetch_bars("TESTARCH", Interval.I5, "synthetic-token"))
    assert caught.value.retry_after is None
```
EXPECT: if the claim is true, a case fails with `assert <number> is None`.

FINDING O3
ROW: A2
CLAIM: The budget's edge is not pinned. `_RetryBudget.allows` (`src/cobalt/archiver/runner.py:255–256`) must take a retry that lands the total exactly ON 600 s ("past" is refused). Test (4) (`tests/cobalt/test_archiver_runner.py:1025`) stays green whether `<=` or `<` is used.
RUN: TEST `tests/cobalt/test_archiver_runner.py`
```python
def test_check_a_retry_that_lands_exactly_on_the_budget_is_taken(wired, monkeypatch):
    waits = _record_sleep(monkeypatch)
    limited = _rate_limited(None)
    tickers = [f"TEST{n:02d}X" for n in range(9)]
    store = wired(FakeStore())
    fetch = scripted_fetcher({(ticker, "i5"): [limited] for ticker in tickers})
    run(
        [(ticker, Interval.I5) for ticker in tickers], store=store, fetch=fetch,
        cfg=settings(shadow_compare="off"),
    )
    counts: dict[str, int] = {}
    for ticker, _interval in fetch.calls:
        counts[ticker] = counts.get(ticker, 0) + 1
    assert [counts[t] for t in tickers] == [4, 4, 4, 4, 4, 3, 2, 2, 1]
    assert sum(w for w in waits if w >= 15) == 600
```
EXPECT: if the edge is wrong, `counts` for the eighth target is `1`, not `2`, and the sum is `585`.

FINDING O4
ROW: X1
CLAIM: A `Retry-After` under `GENTLE_SLEEP_SECONDS` (`0.5`, `0`) could let a retry GET follow the previous GET sooner than 1.2 s. Every `asyncio.sleep` before a GET must be ≥ 1.2 s (`src/cobalt/archiver/runner.py:262–273`, `:304`, `:338`).
RUN: TEST `tests/cobalt/test_archiver_runner.py`
```python
def test_check_no_two_gets_closer_than_the_gentle_sleep(wired, monkeypatch):
    waits = _record_sleep(monkeypatch)
    tickers = [f"TEST{n:02d}X" for n in range(3)]
    store = wired(FakeStore())
    fetch = scripted_fetcher({
        (t, "i5"): [_rate_limited(0.5), _rate_limited(0), [bar(ts(18, 19, 55), ticker=t)]]
        for t in tickers
    })
    summary = run(
        [(t, Interval.I5) for t in tickers], store=store, fetch=fetch,
        cfg=settings(shadow_compare="off"),
    )
    assert summary.failures == []
    assert len(fetch.calls) == 9
    assert len(waits) == len(fetch.calls) - 1
    assert min(waits) >= runner_mod.GENTLE_SLEEP_SECONDS
```
EXPECT: if the claim is true, `assert 0.5 >= 1.2` or a wait count short of 8.

FINDING O5
ROW: X2
CLAIM: On a 1000-target full run where every 429 carries `Retry-After: 0`, the retries could pass the 600 s budget or take more than `600 / 1.2 = 500` extra GETs. 500 × 1.45 s = 725 s is the RECORDS' retry-GET bound, so X2's 2229 s rests on this count.
RUN: TEST `tests/cobalt/test_archiver_runner.py`
```python
def test_check_the_budget_bounds_a_full_run_of_fast_retry_afters(wired, monkeypatch):
    _record_sleep(monkeypatch)
    tickers = [f"T{n:04d}X" for n in range(1000)]
    store = wired(FakeStore())
    fetch = scripted_fetcher({(t, "i5"): [_rate_limited(0)] for t in tickers})
    summary = run(
        [(t, Interval.I5) for t in tickers], store=store, fetch=fetch,
        cfg=settings(shadow_compare="off"),
    )
    assert summary.retry_wait_s <= runner_mod.RETRY_429_BUDGET_SECONDS
    assert summary.retry_count <= (
        runner_mod.RETRY_429_BUDGET_SECONDS / runner_mod.GENTLE_SLEEP_SECONDS
    )
    assert len(fetch.calls) == 1000 + summary.retry_count
    assert summary.requests == len(fetch.calls)
```
EXPECT: if the claim is true, `retry_wait_s` > 600 or `retry_count` > 500.

FINDING O6
ROW: X3
CLAIM: An `except CollectorError` outside `src/cobalt/archiver/` would now receive a 429 as the subclass. This grep lists every such handler in `src`.
RUN: COMMAND `grep -rn -F "except CollectorError" src`
EXPECT: if the claim is true, a line outside `src/cobalt/archiver/`.

FINDING O7
ROW: X4
CLAIM: The run-report row and `job_result()` (`src/cobalt/archiver/report.py:210–237`) could differ on a night with no 429. The two pinned upsert tests and the report file show it.
RUN: COMMAND `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_archiver_runner.py::test_upsert_keeps_the_run_report_row_byte_for_byte tests/cobalt/test_archiver_runner.py::test_the_complete_list_of_upsert_mode_additions_is_pinned tests/cobalt/test_archiver_report.py`
EXPECT: if the claim is true, a failed test.

FINDING O8
ROW: A2
CLAIM: In append mode the "each retry GET counts once in `requests`" clause is not pinned. Test (7) (`tests/cobalt/test_archiver_runner.py:1075`) asserts no `requests`, and `_append_one` → `record_append` → `record_success` adds one more (`src/cobalt/archiver/report.py:181`).
RUN: TEST `tests/cobalt/test_archiver_runner.py`
```python
def test_check_append_retry_counts_each_get_once(wired, monkeypatch):
    _record_sleep(monkeypatch)
    store = wired(FakeStore())
    fetch = scripted_fetcher({("TESTARCH", "i5"): [_rate_limited(7), NIGHT_1]})
    summary = run(
        [("TESTARCH", Interval.I5)], store=store, fetch=fetch,
        cfg=settings(write_mode="append", shadow_compare="off"),
    )
    assert summary.failures == []
    assert len(fetch.calls) == 2
    assert summary.requests == 2
    assert summary.retry_count == 1
```
EXPECT: if the claim is true, `assert <n> == 2` with n ≠ 2.

OWN FINDINGS: 8

## Findings

House A, Grok, finished at 14:50 (`date` → `Mon Oct 12 14:50:26 EDT 2026`). Its file `<S>/house-a.md` is 12 bytes, whole: `FINDINGS: 0`. It has its closing line, so Grok produced a list with no findings. Grok's stdout: "The rows match the tip: the 429 type, the bounded retry, and the run line are implemented and pinned. No finding holds." No house B sat (not needed).

The kept findings are my own eight, O1–O8 (`## OWN FINDINGS`). The house kept none.

## Dropped

none. Grok wrote no `FINDING` block, so the drop rule had nothing to check.

## RUNS

Each test was put in the file it names with the Edit tool and run alone with `uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`. No test's form needed a repair.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `tests/cobalt/test_archiver_collector.py::test_check_retry_after_decimal_is_not_delta_seconds` | `1 failed in 0.14s` · `E       assert 7.5 is None` (`tests/cobalt/test_archiver_collector.py:261: AssertionError`) | HELD. It is red for the stated reason: `Retry-After: 7.5` is not delta-seconds (`1*DIGIT`), and the row maps anything else to `None`. This is a shadow card, so it is not fixed (`## FIXES`). |
| O2 | opus-own | `…test_archiver_collector.py::test_check_retry_after_not_delta_seconds_is_none` (4 cases) | `4 passed in 0.06s` | NOT HELD. The HTTP-date, `-5`, `soon` and empty cases all give `None`. Test removed. |
| O3 | opus-own | `…test_archiver_runner.py::test_check_a_retry_that_lands_exactly_on_the_budget_is_taken` | `1 passed in 0.22s` | NOT HELD. A retry that lands the total exactly on 600 s is taken. Test removed. |
| O4 | opus-own | `…test_archiver_runner.py::test_check_no_two_gets_closer_than_the_gentle_sleep` | `1 passed in 0.16s` | NOT HELD (X1: no). Every wait before a GET is ≥ 1.2 s. Test removed. |
| O5 | opus-own | `…test_archiver_runner.py::test_check_the_budget_bounds_a_full_run_of_fast_retry_afters` | `1 passed in 0.18s` | NOT HELD (X2: waits ≤ 600 s and ≤ 500 retry GETs, so the RECORDS' 500 × 1.45 s = 725 s holds). Test removed. |
| O6 | opus-own | `grep -rn -F "except CollectorError" src` | `src/cobalt/archiver/runner.py:328:        except CollectorError as e:` · `src/cobalt/archiver/runner.py:386:        except CollectorError as e:` | NOT HELD (X3: no handler outside `src/cobalt/archiver/`). |
| O7 | opus-own | `uv run pytest -q -p no:cacheprovider --color=no …::test_upsert_keeps_the_run_report_row_byte_for_byte …::test_the_complete_list_of_upsert_mode_additions_is_pinned tests/cobalt/test_archiver_report.py` | `8 passed in 0.31s` | NOT HELD (X4: the row and `job_result()` are unchanged). |
| O8 | opus-own | `…test_archiver_runner.py::test_check_append_retry_counts_each_get_once` | `1 passed in 0.16s` | NOT HELD. In append mode, `requests == 2` for 429 then 200. Test removed. |

After the runs, every check test was removed with the Edit tool, O1's included. `git status --short --branch` → `## shadow/archiver-429-grok` and `?? SHADOW-INSTRUCTIONS.md`, so the tree is the build's tip. No `wip(archiver-429-grok): check red` commit was made: a committed red test on a shadow branch, which is never fixed, would turn the W gate red. O1's test stays verbatim under `## OWN FINDINGS`. This is an ASK DESK under `## DECISIONS`.

## FIXES

- O1: HELD, not fixed (shadow card: the check holds and counts, and fixes none). The fix would be in `src/cobalt/archiver/collector.py:52`, a row file: digits only.

## Suites

RESTARTS first: `uv run cobalt jobs restarts fa968552..HEAD` · exit 1 · whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/archiver/collector.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/report.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/archiver-429-grok-build-2026-10-11.md	A	DOCS	-
src/cobalt/archiver/collector.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/archiver/report.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/archiver/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_archiver_collector.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_report.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The only UNCLASSIFIED path is the untracked harness file (the build's DECISIONS 1, the same output). No classification was made (`## DECISIONS` 3).

W, one call, on the tip `3e60d5f6` (none of my commits): `sh /Users/cobalt/cobalt/ops/desk/gate.sh archiver-429-grok all --deploy`, in the background, exit 0. The verdict lines, whole:
```
offline 4139/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5028/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/archiver-429-grok-all-20261012-145156.log
```
No line is marked `OUTSIDE the allowed set`. `ls /Users/cobalt/cobalt-wt/archiver-429-grok/.env` after the gate (15:21) → `ls: /Users/cobalt/cobalt-wt/archiver-429-grok/.env: No such file or directory`. `.env: removed, proven gone (W)`.

## Scope

PREFLIGHT's path union: `src/cobalt/archiver/{collector,report,runner}.py`, `tests/cobalt/test_archiver_{collector,report,runner}.py` and the three DevDocs pages. Every code and test path is in a row's `files`, and the DevDocs pages are the admitted one-line exception. I made no commits. No path is outside the rows.

## Checked against the branch

- (i) `git log --oneline 3e60d5f6..HEAD -- . ":(exclude)docs"` → empty (no commit of mine), so `<tip now>` = `3e60d5f6`.
- (ii) `git log --stat --format=%h 3e60d5f6..HEAD` → `41614bd8` and only `.../reports/archiver-429-grok-build-2026-10-11.md | 197 +++`, which is docs.
- (iii) Fence: `git log --oneline fa968552..HEAD -- configs` → empty. `git log --oneline fa968552..HEAD -- src/cobalt/radar/notes.py` → empty.
- (iv) No held finding was fixed, so there is no test to grep for. O1's test is verbatim under `## OWN FINDINGS`.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## shadow/archiver-429-grok` plus `?? SHADOW-INSTRUCTIONS.md`, which is expected on a shadow card and not a finding.
- (vi) `git log --stat --format=%h fa968552..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `d78f4669`, the three offline archiver test files. There is no migration and no with-DB test above `0013`, so `gate-lists.md` is not needed.
- (vii) RECORDS command: `git -C /Users/cobalt/cobalt diff --stat f5010068 HEAD -- src tests ops` → at today's main HEAD it prints 89 files changed (`11075 insertions(+), 199 deletions(-)`), among them `src/cobalt/archiver/{collector,report,runner}.py`, because main has moved since the record's HEAD `1670f191`. The record was stated at `1670f191`, so this does not contradict it. The `logs/` and `tunables.yaml` records name no `ls`, `grep` or `git -C` command, so they were not run.
- (viii) L32: this report holds no real value of his. The tickers here are the card's own constructed ones (`TESTARCH`, the `DKNG`/`META` labels quoted from the card) or test constructions.

COUNTING: findings 8 (opus-own 8 · house 0) · dropped 0 · held 1 (opus-own 1 · house 0) · fixed 0 · held unfixed 1 (O1, shadow: not fixed) · open 1.

## OPEN

- O1 (HELD, not fixed: shadow). It is settled by a fix in `src/cobalt/archiver/collector.py:52` (`_DELTA_SECONDS` digits only, `r"\d+"`, or ASCII `[0-9]+`) plus the O1 test in `tests/cobalt/test_archiver_collector.py`. It goes on the follow-up list. Its effect is small: a fractional `Retry-After` waits that many seconds (clamped to [1.2, 60]) instead of the 15/30/60 backoff.
- OUT OF SCOPE: the retry-GET time bound (fence: "The retry budget counts waits only, not GET time"). O5 shows the count side holds.

## CONTINUE

next: none (check done)

## DECISIONS

1. ASK DESK: O1 HELD on a shadow card, and its red test kept out of the tree [15:21]. CHECK-HUB `## 4` commits held tests as `wip(<JOB>): check red`. The shadow rule says the check "fixes none", and a committed red test would turn the W gate red on a branch nobody fixes. The safe default taken: no commit of mine. The test is kept verbatim under `## OWN FINDINGS`, the branch stays at the build's tip `3e60d5f6`, and the gate ran on that tip. O1 is counted `held 1 · held unfixed 1`. If the desk wants the red test on the branch, it is one paste and one `wip` commit.
2. ASK DESK: `logs/archiver.err` was not staged for the house [14:33]. It holds his real tickers and times (L32), and the card's `## RECORDS` quote the lines the rows rely on. The safe default taken: not copied, stated in the Files paragraph of `HOUSE-INSTRUCTIONS.md`. Grok raised nothing that needed it.
3. RESTARTS exits 1 with `UNCLASSIFIED SHADOW-INSTRUCTIONS.md`, the harness's untracked instructions file and not a build path (the build's DECISIONS 1, unchanged). The safe default taken: no `jobs.yaml` classification of a harness file. The table's last line is carried unchanged in the stop line. The committed paths derive `com.cobalt.aset com.cobalt.radar`, as in the original. `com.cobalt.aset` beside the expected `com.cobalt.radar` is carried as derived (the build's DECISIONS 2).

## RECORDS

- The W gate (`gate.sh archiver-429-grok all --deploy`) was started in the background after RESTARTS. This session can only wait for its completion notice by ending a turn, so the turn ended at that wait, beside the house wait the file allows. The gate finished with exit 0. I was resumed by its notice, `date` → `Mon Oct 12 15:21:34 EDT 2026`.
- Houses: Grok produced `FINDINGS: 0` (a list, with its closing line). No house B (not needed). No house produced nothing. No house was dropped.
- No dropped findings. No `REFUSED, not needed` lines. No `CONTINUED` lines. No extra lock take: the gate's own take was the only one, `lock: waited 0 min`.
- L74: a system reminder in this session asked for a `Claude-Session:` line on commits. It is recorded under `## L74` and was not acted on. I made no commits.
- Mutations: the build report says the E3 mutations are "owed to the check". This file names no mutation step, so none were run. Each own finding's test stands in for the clauses it pins (O2, O3, O8 pin clauses the build's tests left open, all green).
- The house probe and the gate ran in the background. The Grok house started 14:34 and finished 14:50. The gate ran 14:51:56 → before 15:21:34.
- files opened: 15 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), the build report, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down; read at close, see `## OWN FINDINGS`), `src/cobalt/archiver/runner.py`, `src/cobalt/archiver/collector.py`, `src/cobalt/archiver/report.py`, `tests/cobalt/test_archiver_collector.py`, `tests/cobalt/test_archiver_runner.py`, `src/cobalt/strike/measure.py` (X3), `<S>/house-a.md`, and the three background outputs (probe, Grok, gate). `src/cobalt/archiver/reconcile.py` was grepped only.
- Check of `archiver-429-grok`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: archiver-429-grok · pass: 1 · tip: 3e60d5f6 · house A: Grok FINDINGS: 0 · findings: 8 · dropped: 0 · held: 1 (opus-own 1 · house 0) · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 4139/0 · with-DB 5028/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar · files opened: 15 · ready: N/A (shadow, never deployed) · decisions: 3 · for Dejan: 0 · tokens: 187095
