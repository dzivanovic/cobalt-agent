# archiver-429-1009 — check report (2026-10-10)

## §0 Headline
Check of `archiver-429-1009` (`fa968552..188190dc`): house A Sol, 5 findings; house B Grok, 2; my own read, 2. Five held and all five are fixed in `a4aef3a0`:
- A 429 whose Retry-After is too large for a float now stays typed (O1, A4).
- Two A2 tests now go red on the row's reason (B1, B2).
- A DevDoc sentence is corrected (A3).
Three are open (O2, A1, A2) and one is out of scope (A5). The suites are green (offline 4145/0, with-DB 5034/0, live-note 146/0), `cobalt_dev` is back at 0013 and `.env` is removed. Three decisions remain, none for Dejan.

## L74
One block arrived in a system reminder, after the launch message, asking for commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and a `Claude-Session: https://claude.ai/code/session_01HK59Tv6dkt2sendQF8z3Mq` line. It is recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md" · 0 · 93e4c29a2e19d6cfc98811eb62a77ef62032c009
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output:
```
clock · date · 0 · Sat Oct 10 00:42:35 EDT 2026
status · git status --short --branch · 0 · ## ops/archiver-429-1009
head · git log --oneline -1; git log --stat --format=%h 188190dc..HEAD · 0 · (5 lines)
    6263eeee docs(archiver-429-1009): build report — 188190dc
    6263eeee
    
     .../reports/archiver-429-build-2026-10-09.md       | 214 +++++++++++++++++++++
     1 file changed, 214 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/archiver-429-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/s4-p2-1009/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/archiver-429-1009/docs/40 - DevDocs/reports/archiver-429-build-2026-10-09.md" · 0 · BUILT · job: archiver-429-1009 · tip: 188190dc | on fa968552 | migration: none | offline 4143/0 | with-DB 5032/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 227362
range · git log --oneline fa968552..188190dc · 0 · (2 lines)
    188190dc fix(archiver-429-1009): a 429 is typed and retried, bounded, and the run names its retries (A1, A2, B; L1, L53)
    fcf30714 wip(archiver-429-1009): red — 429 typed error, bounded retry, named retries (A1, A2, B)
PREFLIGHT OK
```
The lock: another session (`s4-p2-1009`) holds `.env`; I wait for it at my with-DB step (L76).

`git log --stat --format=%h fa968552..188190dc` · exit 0:
```
188190dc
 docs/40 - DevDocs/cobalt/archiver/collector.md |  9 +++
 docs/40 - DevDocs/cobalt/archiver/report.md    |  9 +++
 docs/40 - DevDocs/cobalt/archiver/runner.md    | 13 ++++
 src/cobalt/archiver/collector.py               | 39 ++++++++++-
 src/cobalt/archiver/report.py                  | 33 ++++++++++
 src/cobalt/archiver/runner.py                  | 89 +++++++++++++++++++++++---
 6 files changed, 183 insertions(+), 9 deletions(-)
fcf30714
 tests/cobalt/test_archiver_collector.py |  59 +++++++++
 tests/cobalt/test_archiver_report.py    |  26 ++++
 tests/cobalt/test_archiver_runner.py    | 222 +++++++++++++++++++++++++++++++-
 3 files changed, 306 insertions(+), 1 deletion(-)
```
Path union: the 3 docs pages, `src/cobalt/archiver/{collector,report,runner}.py`, `tests/cobalt/test_archiver_{collector,report,runner}.py`.

`ls <S>` · exit 1 · `No such file or directory` → fresh.

House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: OUT — OK.
```
house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). `HOUSE B: as needed`; both are up.

Write and with-DB strings: proven at first real use (below).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0:
```
27533 <S>/diff.md
12568 <S>/files/206-archiver-429-card.md
28827 <S>/files/archiver-429-build-2026-10-09.md
3168 <S>/files/wt/docs/40 - DevDocs/cobalt/archiver/collector.md
5910 <S>/files/wt/docs/40 - DevDocs/cobalt/archiver/report.md
12312 <S>/files/wt/docs/40 - DevDocs/cobalt/archiver/runner.md
10266 <S>/files/wt/src/cobalt/archiver/collector.py
12416 <S>/files/wt/src/cobalt/archiver/report.py
25646 <S>/files/wt/src/cobalt/archiver/runner.py
9740 <S>/files/wt/tests/cobalt/test_archiver_collector.py
5175 <S>/files/wt/tests/cobalt/test_archiver_report.py
47928 <S>/files/wt/tests/cobalt/test_archiver_runner.py
384 <S>/rulings.md
STAGED 13 files · 201873 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/archiver-429-1009-check`; the script printed absolute paths.) `commits 2` = PREFLIGHT's range count 2. `grep -c "^commit " <S>/diff.md` → `2`.
The `## READ` files the script does not derive:
- `stage-copy.sh …/src/cobalt/radar/notes.py <S>/files/wt/src/cobalt/radar/notes.py` → `COPIED 30852 …`
- `stage-copy.sh …/configs/cobalt/jobs.yaml <S>/files/wt/configs/cobalt/jobs.yaml` → `COPIED 19699 …`
- `stage-copy.sh /Users/cobalt/cobalt/logs/archiver.err <S>/files/archiver.err` → exit 1, `REFUSED: the source is not under a job worktree or the main tree's docs/: /Users/cobalt/cobalt/logs/archiver.err`. The script refuses this path by design. Not copied: see `## DECISIONS` (ASK DESK). Sol can read the absolute path. Grok relies on the card's `## RECORDS`, which quote the log lines.
`<S>/HOUSE-INSTRUCTIONS.md` written: the HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, then the Files paragraph.

Start, 00:44:37 EDT (`date`). The two house gates were rerun: R17 gives one row, line 35; the R19 commit is `5055151d…`. `ls -la <S>` lists diff.md, files/, HOUSE-INSTRUCTIONS.md and rulings.md. `cd <AGY>`. Sol started (bg `b091vfwof`); its line takes `<S>` as an absolute path. Grok started (bg `bfa1pnnsj`), writing `house-b.md`. `cd <WT>`; `git status --short --branch` → `## ops/archiver-429-1009`.

## OWN FINDINGS
Written before either house's list was opened. Read: the diff (`<S>/diff.md`), `runner.py:160–580`, `report.py:100–280`, `collector.py` (diff hunks), `radar/notes.py:330–375`, `radar/collector.py:170–290`, `replay/movers.py:328–396`, `strike/measure.py` and `radar/poller.py` (their `except` sites), `tests/cobalt/test_replay_demand.py`.

FINDING O1
ROW: A1
CLAIM: `_retry_after_seconds` (`src/cobalt/archiver/collector.py:33–40`, at the tip `:83–90`) returns `float(int(value))` for any all-digit header. A valid delta-seconds value too large for a float raises `OverflowError` inside the `except httpx.HTTPStatusError` block of `finviz_get`. The 429 then reaches `fetch_bars`'s generic `except Exception` and comes out as a plain `CollectorError` (`int too large to convert to float`), not as `FinvizRateLimited`, so it is never retried.
RUN: TEST `tests/cobalt/test_archiver_collector.py`
```python
def test_check_o1_a_huge_retry_after_is_still_a_typed_rate_limit(monkeypatch):
    _transport_answering(monkeypatch, 429, {"Retry-After": "9" * 400})
    with pytest.raises(FinvizRateLimited):
        asyncio.run(fetch_bars("TESTARCH", Interval.I5, "synthetic-token"))
```
EXPECT: `Failed: DID NOT RAISE <class 'cobalt.archiver.collector.FinvizRateLimited'>`, or a `CollectorError` whose message carries `int too large to convert to float`, propagating out of `pytest.raises`.

FINDING O2
ROW: X3
CLAIM: No `except CollectorError` exists outside `src/cobalt/archiver/`. Replay's `MoversCollector.bars` (`src/cobalt/replay/movers.py:394–395`) catches `Exception` and records `f"{type(e).__name__}: …"`, so a 429 on a replay i1 fetch now reads `FinvizRateLimited: …` where it read `CollectorError: …` before. That is a visible text change in a consumer the card says "behaves as today".
RUN: TEST `tests/cobalt/test_replay_demand.py`
```python
def test_check_o2_a_429_reads_as_before_in_the_replay_failure_text():
    from cobalt.archiver.collector import FinvizRateLimited

    async def fetch_429(ticker, interval, token, **kwargs):
        raise FinvizRateLimited("Fetch failed for AAA/i1: Finviz HTTP failed: 429", retry_after=7.0)

    collector = movers_mod.MoversCollector(
        "token", config=movers_mod.load_radar_config(), bucket=_NoWaitBucket(), cache_root=Path("/nonexistent"),
        get=fetch_429, fetch_bars=fetch_429,
    )
    fetched, failures = asyncio.run(collector.bars(["AAA"], top_n=10))
    assert fetched == {}
    assert failures["AAA"].startswith("CollectorError: "), failures["AAA"]
```
EXPECT: `AssertionError: FinvizRateLimited: Fetch failed for AAA/i1: Finviz HTTP failed: 429`.

Check asks, from my read (each confirmed by the runs at `## RUNS` / `## Suites`; none carries a finding):
- X1: every retry waits `_retry_wait` ≥ `GENTLE_SLEEP_SECONDS` before its GET (`runner.py:197`, `:227`; backoff 15/30/60 s). The between-target sleep (`:329–330`, `:409–410`) is unchanged, and no other HTTP call sits in the target loop. I found no path that sends two archiver GETs less than 1.2 s apart.
- X2: the waits are capped at 600 s (`:219`). GET time is fenced (`## NOT IN THIS JOB`), and the card's `## RECORDS` give the bound of 2229 s < 2400 s.
- X4: `job_result()` and `append_run_report` are untouched by the diff (`report.py` gains only the retry members). On a night with no 429, `requests` counts exactly as before, since the `+= 1` sits only on a retry. The two pinned tests run in the suites.

## Findings
Sol finished at 00:49:39 EDT (`b091vfwof`, exit 0). I wrote its final message to `<S>/house-a.md`; it ends `FINDINGS: 5`. Grok finished at 00:58:56 EDT (`bfa1pnnsj`, exit 0). It wrote `<S>/house-b.md` itself, ending `FINDINGS: 2`, and its stdout was the path. Ids: Sol = A1–A5, Grok = B1–B2.

| id | house | row | claim | run |
|---|---|---|---|---|
| A1 | Sol | SCOPE | The vendor name `Finviz` is in the identifier `FinvizRateLimited` (`collector.py:61`) | COMMAND |
| A2 | Sol | SCOPE | The tip changes three DevDocs pages outside the rows' files | COMMAND |
| A3 | Sol | B | `report.md:116` says the outcome is `""` when no failure matches; the code renders `ok` | COMMAND |
| A4 | Sol | A1 | An all-digit `Retry-After` too large for a float raises `OverflowError`, so the 429 becomes a plain `CollectorError` | TEST |
| A5 | Sol | X2 | The budget counts waits only; retry GET time can carry the run past its window | TEST |
| B1 | Grok | A2 | `test_a_429_past_the_retry_max_fails_the_target` builds its input from `RETRY_429_MAX`, so on the after-A1 tree it errors `AttributeError`, not the row's reason | COMMAND |
| B2 | Grok | A2 | The budget test reads `RETRY_429_BUDGET_SECONDS` first, so the after-A1 red is `AttributeError`, not the sum | COMMAND |

## Dropped
None. Every block has a `RUN:` line followed by a test function or a `grep` / `git diff` command.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_archiver_collector.py::test_check_o1_a_huge_retry_after_is_still_a_typed_rate_limit` | `1 failed in 0.12s`; `E OverflowError: int too large to convert to float` at `collector.py:83`, then `E cobalt.archiver.collector.CollectorError: Fetch failed for TESTARCH/i5: int too large to convert to float` | HELD |
| O2 | own | `… tests/cobalt/test_replay_demand.py::test_check_o2_a_429_reads_as_before_in_the_replay_failure_text` | `1 failed in 0.20s`; `E AssertionError: FinvizRateLimited: Fetch failed for AAA/i1: Finviz HTTP failed: 429` | REJECTED — `## NOT IN THIS JOB`: "A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here." The fix lies in `replay/movers.py`, which is also fenced ("any change to how they handle `CollectorError`"). The test was removed again; OPEN, `## DECISIONS` 2 (the builder's DECISION 2, now with a red) |
| A1 | Sol | `grep -n -F "class FinvizRateLimited" src/cobalt/archiver/collector.py` | `61:class FinvizRateLimited(CollectorError):` | REJECTED — card row A1 names the class `FinvizRateLimited(CollectorError)` verbatim; it names the data source, as `finviz_get` already does. OPEN |
| A2 | Sol | `git diff --name-only fa968552..188190dc -- "docs/40 - DevDocs/cobalt/archiver"` | `collector.md`, `report.md`, `runner.md` | REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`". OPEN |
| A3 | Sol | ``grep -n -F 'else `""`' "docs/40 - DevDocs/cobalt/archiver/report.md"`` | ``116:`failed` when a `failures` entry starts `<T>/<i>:`, else `""`).`` | HELD (the page misreads `report.py:165`, which renders `ok`) |
| A4 | Sol | `… tests/cobalt/test_archiver_collector.py::test_a_429_with_an_unrepresentable_delta_stays_typed` | `1 failed in 0.08s`; `E AssertionError: assert False` `+ where False = isinstance(CollectorError('Fetch failed for TESTARCH/i5: int too large to convert to float'), FinvizRateLimited)` | HELD (same defect as O1) |
| A5 | Sol | `… tests/cobalt/test_archiver_runner.py::test_retry_budget_bounds_the_whole_retry_elapsed_time` | `1 failed`; `E assert 2700.0 <= 2400.0` (300 simulated retry GETs at a constructed 7 s each) | REJECTED — `## NOT IN THIS JOB`: "The retry budget counts waits only, not GET time (bounded at 2229 s, `## RECORDS`)". The test was removed again; OPEN |
| B1 | Grok | `grep -n -F "RETRY_429_MAX + 1" tests/cobalt/test_archiver_runner.py` | `1003: fetch = sequenced({("TESTARCH", "i5"): [rate_limited()] * (runner_mod.RETRY_429_MAX + 1)})`, `1006: assert len(fetch.calls) == runner_mod.RETRY_429_MAX + 1 == 4` | HELD (the output shown; the builder's own `## RECORDS` say E2's (2) first red was `AttributeError … RETRY_429_MAX`) |
| B2 | Grok | `grep -n -F "RETRY_429_BUDGET_SECONDS" tests/cobalt/test_archiver_runner.py` | `934:` (comment), `1044: assert sum(retry_waits) <= runner_mod.RETRY_429_BUDGET_SECONDS == 600`, and `1173:` (the A5 test, since removed) | HELD (the output shown) |

Held tests committed before any fix: `4dd6fb31 wip(archiver-429-1009): check red — O1, A4` (`tests/cobalt/test_archiver_collector.py`). A3, B1 and B2 are COMMAND findings; their before/after outputs are under `## FIXES`. No test form was repaired.

## FIXES
| id | fix | proof |
|---|---|---|
| O1, A4 | `collector.py` `_retry_after_seconds`: `float(int(value))` inside `try … except (OverflowError, ValueError): return None` (row A1: "unparseable → `None`") | both tests green in the 5-file run below |
| A3 | `docs/40 - DevDocs/cobalt/archiver/report.md:116`: "else `ok`; `""` when the run took no retry" | the A3 grep → nothing (exit 1) |
| B1, B2 | `tests/cobalt/test_archiver_runner.py`: both tests build their input and bound from the literals (4, 600); the constants are asserted last (`== 4`, `== 600`) | The greps now show only the final asserts (`1016: assert runner_mod.RETRY_429_MAX + 1 == 4`, `1054: assert runner_mod.RETRY_429_BUDGET_SECONDS == 600`). Mutation, made and undone with Edit: `_fetch_retrying_429` reduced to one `return await fetch(...)`, both tests run → `2 failed`, `test_archiver_runner.py:1008: AssertionError: assert 1 == 4` and `:1049: assert 0 == 600`: the row's reasons. After the undo, `git diff --stat` shows no `runner.py` |

After the fixes: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_archiver_collector.py tests/cobalt/test_archiver_runner.py tests/cobalt/test_archiver_report.py tests/cobalt/test_replay_demand.py tests/cobalt/test_finviz_consumers.py` → `113 passed, 1 xfailed in 5.02s`. The DevDocs line was added to `collector.md`. Commit: `a4aef3a0 fix(archiver-429-1009): an unrepresentable Retry-After keeps the 429 typed; two A2 tests red on the row's reason; report DevDoc outcome wording (check O1, A4, A3, B1, B2)`.

## Suites
RESTARTS (`BUILD-HUB.md` `## RESTARTS`), `uv run cobalt jobs restarts fa968552..HEAD` · exit 0: the same 10 rows as the build's table (collector/report/runner `.py` → `static import reach` `com.cobalt.aset,com.cobalt.radar`; tests → `test/documentation; no resident`; docs → `DOCS`). Last line `RESTARTS: com.cobalt.aset com.cobalt.radar`. No `UNCLASSIFIED`.

W, on tip `a4aef3a0`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh archiver-429-1009 all --deploy` (no `--deselect`, `--tickers` or `--migration`: no with-DB test, ticker or migration is added) · `run_in_background` · exit 0. Verdict lines whole:
```
offline 4145/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5034/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/archiver-429-1009-all-20261010-010159.log
```
- offline `4145/0`: the build's 4143 plus my 2 collector tests.
- `grep -n -F "OUTSIDE the allowed set" <log>` → nothing (exit 1).
- `grep -n -F "F0: " <log>` → `887:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`. `grep -n -F "F2: " <log>` → `1979:F2: 664 35 272c95bbb12241e3611e4b36326ccf87`: F2 = F0 → **`cobalt_dev: 0013 — F2 = F0`**. `grep -n -F "dev forward: APPLIED" <log>` → `1100:dev forward: APPLIED 01:25:47`.
- `.env`: the gate printed `.env: removed`; my `ls /Users/cobalt/cobalt-wt/archiver-429-1009/.env` gave `No such file or directory` at 01:30:41 EDT. **`.env: removed, proven gone (W)`.**
- RESTARTS: `com.cobalt.aset com.cobalt.radar`, as derived.

## Scope
PREFLIGHT's path union (3 docs pages, `src/cobalt/archiver/{collector,report,runner}.py`, `tests/cobalt/test_archiver_{collector,report,runner}.py`) plus my commits: `src/cobalt/archiver/collector.py` (row A1's file), `tests/cobalt/test_archiver_collector.py` and `tests/cobalt/test_archiver_runner.py` (rows A1 and A2's tests), and the DevDocs lines in `docs/40 - DevDocs/cobalt/archiver/{collector,report}.md`. Nothing else. The O2 and A5 tests were added to `test_replay_demand.py` and `test_archiver_runner.py` for their runs and removed again, uncommitted (`git status` before the red commit showed only `test_archiver_collector.py` modified).

## Checked against the branch
- (i) `git log --oneline 188190dc..HEAD -- . ":(exclude)docs"` → `a4aef3a0 fix(archiver-429-1009): an unrepresentable Retry-After keeps the 429 typed; two A2 tests red on the row's reason; report DevDoc outcome wording (check O1, A4, A3, B1, B2)` · `4dd6fb31 wip(archiver-429-1009): check red — O1, A4`. `<tip now>` = `a4aef3a0`.
- (ii) `git log --stat --format=%h 188190dc..HEAD` → `a4aef3a0`: the two DevDocs pages, `src/cobalt/archiver/collector.py`, `tests/cobalt/test_archiver_runner.py`. `4dd6fb31`: `tests/cobalt/test_archiver_collector.py`. `6263eeee`: the build report. Every non-docs path is in a row's `files` or is a test file. No WIDENED.
- (iii) Fence: `git log --oneline fa968552..HEAD -- configs src/cobalt/radar/notes.py` → nothing. The other fence items (cadence, the plist, a `fetch_bars(` call, radar/replay/strike handling) have no path in the range (ii).
- (iv) `grep -n -F "def test_check_o1_a_huge_retry_after_is_still_a_typed_rate_limit" tests/cobalt/test_archiver_collector.py` → `251:…`. `grep -n -F "def test_a_429_with_an_unrepresentable_delta_stays_typed" …` → `257:…`. The red commit `4dd6fb31` sits below the fix `a4aef3a0` in (i). A3, B1 and B2 are COMMAND findings; their before/after greps are under `## FIXES`.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/archiver-429-1009`.
- (vi) `git log --stat --format=%h fa968552..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `test_archiver_{collector,report,runner}.py`, all offline. No migration and no with-DB test, so no gate-list entry is owed.
- (vii) No card `## RECORDS` line names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command (the one git record is a `diff --stat`). Nothing to run.
- (viii) L32: this report holds constructed test values only (`TESTARCH`, `AAA`, `TEST*`). The tickers `DKNG` / `META` appear only where the card's own rows and the build's test values carry them; no price or date of his.

COUNTING: findings 9 (own 2, Sol 5, Grok 2) · dropped 0 · held 5 (O1, A3, A4, B1, B2) · fixed 5 · held unfixed 0 · open 3 (O2, A1, A2) · out of scope 1 (A5).

## OPEN
- O2 (own, X3) — REJECTED (fence: a red outside the rows is not fixed here). Replay's `MoversCollector.bars` (`replay/movers.py:395`) now writes `FinvizRateLimited: …` where it wrote `CollectorError: …` on a 429. Catching, counting and exit codes are unchanged. Would settle it: a ruling that the text change is acceptable, or a replay card that pins the old text. `## DECISIONS` 2.
- A1 (Sol, SCOPE) — REJECTED (card row A1 names `FinvizRateLimited`). Would settle it: nothing; the card's own text names the class.
- A2 (Sol, SCOPE) — REJECTED (`BUILD-HUB.md` `## E3` requires the dated DevDocs line). Would settle it: nothing; the hub requires the pages.
- A5 (Sol, X2) — OUT OF SCOPE (`## NOT IN THIS JOB`: "The retry budget counts waits only, not GET time (bounded at 2229 s, `## RECORDS`)"). Its red rests on a constructed 7 s per retry GET, 300 retries; the card's record bounds the real GET time at ≤ 725 s.

## CONTINUE
next: none (check done)

## DECISIONS
1. ASK DESK: `stage-copy.sh` refused `/Users/cobalt/cobalt/logs/archiver.err` (`REFUSED: the source is not under a job worktree or the main tree's docs/`). That file is in the card's `## READ`. Should a log the card reads be staged for a confined house, and by which script? [01:30 EDT]. Safe default taken: not copied and no new copy route tried (never more access). The house instructions say so; Sol could read the absolute path, and Grok relied on the card's `## RECORDS`, which quote the log lines.
2. O2 / the builder's DECISION 2, now with a red (L70 proved): on a 429, replay's i1 failure text reads `FinvizRateLimited: …` instead of `CollectorError: …` (`replay/movers.py:395`). The test `test_check_o2_a_429_reads_as_before_in_the_replay_failure_text` (`tests/cobalt/test_replay_demand.py`, text under `## OWN FINDINGS`) ran `1 failed`: `AssertionError: FinvizRateLimited: Fetch failed for AAA/i1: Finviz HTTP failed: 429`. Fenced, so not fixed here and the test was removed. Safe default: left as is; it ships on the follow-up list.
3. RESTARTS derives `com.cobalt.aset` next to the expected `com.cobalt.radar` (the card's record: any other label is a decision). This is the builder's DECISION 1, unchanged by my commit. Safe default: the line as derived, nothing trimmed; the deploy decides the restart.

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: none. Gemini's probe line `gemini: OUT — OK.`; it was not seated (A and B were both up).
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (W's gate only, `lock: waited 0 min` after the gate's own wait; started 01:01, verdict at 01:30).
- L74: one block arrived (see `## L74`); not acted on.
- The two rejected tests (O2, A5) were added for their runs and removed again with Edit; neither was committed.
- B1/B2 proof mutation: `_fetch_retrying_429` cut to one fetch, run, undone with Edit. `git diff --stat` afterwards showed no `src/cobalt/archiver/runner.py`.
- files opened: 22 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` … `## W`); the build report (`## RESTARTS` … end); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `<S>/diff.md`; `<S>/rulings.md`; `src/cobalt/archiver/runner.py`; `src/cobalt/archiver/report.py`; `src/cobalt/archiver/collector.py`; `src/cobalt/radar/notes.py`; `src/cobalt/radar/collector.py`; `src/cobalt/replay/movers.py`; `src/cobalt/radar/evaluate.py` (lines 735–754, a grep hit); `tests/cobalt/test_replay_demand.py`; `tests/cobalt/test_archiver_runner.py`; `docs/40 - DevDocs/cobalt/archiver/report.md`; `docs/40 - DevDocs/cobalt/archiver/collector.md`; the house probe output; Sol's output (final message); Grok's output and `<S>/house-b.md`; the gate output.
- **Check of `archiver-429-1009`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).**

CHECK DONE · job: archiver-429-1009 · pass: 1 · tip: a4aef3a0 · house A: Sol FINDINGS: 5 · findings: 9 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 2 · suites: offline 4145/0 · with-DB 5034/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 22 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 207006
