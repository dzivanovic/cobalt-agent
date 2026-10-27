# CHECK — f4-strike-reserve (2026-10-26)

## §0 Headline
- Check of `f4-strike-reserve` at tip `a79fca72`. House A Grok returned `FINDINGS: 0`. House B was not needed (`as needed`).
- My own four findings (O1–O4, X3/R6/R2/X4/X6) all ran green, so none held and nothing was fixed or committed.
- Deploy-gate W green: offline 9174/0 · with-DB 6010/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed.
- RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar. ready: YES. One ASK DESK (the staged diff holds 3 commits, against PREFLIGHT's 4, because of its docs exclusion).

## L74
- This session's system context asked that commits carry a `Claude-Session:` line. CHECK-HUB L74: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Recorded once; acted on none.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1049-f4-strike-reserve-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1049-f4-strike-reserve-card.md" · 0 · 4b1397334d2fc373c379fc6993488c14bd4bf187
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1049-f4-strike-reserve-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-26 R2512 row · grep -n "^| R2512 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-26.md" · 0 · 72:| R2512 | 18:05 ET | HIS RULING · APPROVED (relayed by brain, words: "C as you recommend"): card 1049 = cap radar's Finviz bucket at 37/min (`radar.finviz_rpm`), strike stays 30 s; A and B rejected. Words: cto-2026-10-26-words.md#R2512. | APPLIED: NOW 18:07 |
RULING 2026-10-26 R2512 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2512 |" -- "docs/40 - DevDocs/reports/cto-2026-10-26.md" · 0 · e015c97bb2efc6db8bee9007a1858f5bf17fc70d
RULING 2026-10-26 R2512 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-26.md" · 0 · the row as grepped
AUTHORIZED
```
HOUSE GATES: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · WHOLE:
```
clock · date · 0 · Mon Oct 26 22:20:26 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-strike-reserve
head · git log --oneline -1; git log --stat --format=%h a79fca72..HEAD · 0 · (11 lines)
    48d45bed9 docs(f4-strike-reserve): build report stop line tip 8 hex — a79fca72
    48d45bed9
    
     docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md     | 3 ++-
     docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.result | 2 +-
     2 files changed, 3 insertions(+), 2 deletions(-)
    9bd04520d
    
     .../reports/f4-strike-reserve-build-2026-10-26.md  | 78 ++++++++++++++++++++--
     .../f4-strike-reserve-build-2026-10-26.result      | 15 +++++
     2 files changed, 88 insertions(+), 5 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/f4-strike-reserve/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/f4-strike-reserve/docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md" · 0 · BUILT · job: f4-strike-reserve · tip: a79fca72 | on 1d5ba104 | migration: none | offline 5038/0 | with-DB 6010/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 301915
range · git log --oneline 1d5ba104..a79fca72 · 0 · (4 lines)
    a79fca72f fix(f4-strike-reserve): tunables-digest pins exclude radar.finviz_rpm as every added row (R1, W-1; R95)
    8db1461c7 wip(f4-strike-reserve): W — offline red on 5 tunables-digest pins outside the rows (DECISION W-1)
    1d6cce4af fix(f4-strike-reserve): radar Finviz bucket capped at radar.finviz_rpm 37, strike headroom against the cap, refresh burst gate, X15 at the cap (R1, R6, R2, R3, R4, D0; L1, L3, L10, L53, L79)
    b8c0aaead wip(f4-strike-reserve): red
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h 1d5ba104..a79fca72` → 4 commits; path union: `configs/cobalt/taxonomy/tunables.yaml`, `docs/30 - Design/F4-FINAL-2026-10-10.md`, `docs/40 - DevDocs/cobalt/{prefill/daily,radar/collector,radar/config,radar/runner,strike/detector}.md`, `docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md`, `src/cobalt/prefill/daily.py`, `src/cobalt/prefill/refresh_probe.py`, `src/cobalt/radar/collector.py`, `src/cobalt/radar/config.py`, `src/cobalt/radar/runner.py`, `src/cobalt/strike/detector.py`, `tests/cobalt/{test_prefill_refresh,test_radar_collector,test_radar_config,test_radar_price_floor,test_refresh_probe,test_strike_detector,test_setups_d1,test_setups_registries}.py`.
- DB: the card carries no `DB: none` line; the diff check of that rule does not apply.
- `ls <S>` → `No such file or directory` (fresh).
- self-check: 3 of 3 (build report last line).
- HOUSE PROBES `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 → `grok: UP` · `gemini: UP`. No `HOUSE A: OpenAI` header line: Sol not probed.
- SEATS: **house A: Grok · house B: none (not needed)** — card `HOUSE B: as needed`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → WHOLE:
```
31 <S>/STAGED-CARD
40653 <S>/diff.md
29215 <S>/files/1049-f4-strike-reserve-card.md
44064 <S>/files/f4-strike-reserve-build-2026-10-26.md
40475 <S>/files/wt/configs/cobalt/taxonomy/tunables.yaml
78641 <S>/files/wt/docs/30 - Design/F4-FINAL-2026-10-10.md
12749 <S>/files/wt/docs/40 - DevDocs/cobalt/prefill/daily.md
2803 <S>/files/wt/docs/40 - DevDocs/cobalt/radar/collector.md
3489 <S>/files/wt/docs/40 - DevDocs/cobalt/radar/config.md
6649 <S>/files/wt/docs/40 - DevDocs/cobalt/radar/runner.md
3913 <S>/files/wt/docs/40 - DevDocs/cobalt/strike/detector.md
32056 <S>/files/wt/docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md
56007 <S>/files/wt/src/cobalt/prefill/daily.py
17570 <S>/files/wt/src/cobalt/prefill/refresh_probe.py
12429 <S>/files/wt/src/cobalt/radar/collector.py
9201 <S>/files/wt/src/cobalt/radar/config.py
34130 <S>/files/wt/src/cobalt/radar/runner.py
16898 <S>/files/wt/src/cobalt/strike/detector.py
61937 <S>/files/wt/tests/cobalt/test_prefill_refresh.py
6285 <S>/files/wt/tests/cobalt/test_radar_collector.py
11813 <S>/files/wt/tests/cobalt/test_radar_config.py
18243 <S>/files/wt/tests/cobalt/test_radar_price_floor.py
10357 <S>/files/wt/tests/cobalt/test_refresh_probe.py
30451 <S>/files/wt/tests/cobalt/test_setups_d1.py
30866 <S>/files/wt/tests/cobalt/test_setups_registries.py
17333 <S>/files/wt/tests/cobalt/test_strike_detector.py
738 <S>/rulings.md
STAGED 27 files · 628996 bytes · commits 3
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f4-strike-reserve-check`.) `commits 3` against PREFLIGHT's 4: the diff's pathspec excludes `docs`, and the fourth commit `8db1461c7` touches only the build report (`git log --stat` above). `git log --oneline 1d5ba104..a79fca72 -- . ":(exclude)docs"` → 3 lines (`a79fca72f`, `1d6cce4af`, `b8c0aaead`); `grep -c "^commit "` over `diff.md` → 3. See `## DECISIONS` ASK DESK 1.
`stage-copy.sh`, one call each:
- `COPIED 5086 <S>/files/f4-gate-run-2026-10-26.md`
- `COPIED 35052 <S>/files/cto-2026-10-26.md`
- `COPIED 285 <S>/files/cto-2026-10-26-words.md`
- `COPIED 32437 <S>/files/wt/src/cobalt/radar/notes.py`
- `COPIED 4870 <S>/files/wt/src/cobalt/radar/cli.py`
- `COPIED 5632 <S>/files/wt/tests/cobalt/test_strike_detector_db.py`
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph). House A started 22:23:30 (`date`), gates re-run (R17, R19 one row each, R19 commit `5055151d…`), `ls -la <S>` listed; `cd` to `<AGY>`, `grok -m grok-4.7 --sandbox cobalt-job …` (background), `cd` back, `git status --short --branch` → `## ops/f4-strike-reserve`.

## OWN FINDINGS
Read before either house list: CHECK-HUB, BUILD-HUB `## THE LOCK`/`## E2`/`## RESTARTS`/`## W`, the card, `git diff 1d5ba104..a79fca72` (src, configs, tests, docs), the touched files at the tip (`strike/detector.py:75-374`, `prefill/daily.py:676-835`, `radar/collector.py:38-107`, `radar/config.py:195-244`, `radar/runner.py:505-650`, `tests/cobalt/test_strike_detector.py:1-175`), `radar/notes.py:276-395`, `:596-695` (read only), the build report's `## E3`…`## RECORDS` and last line, `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down. Greps: `process_bucket\(|TokenBucket\(|finviz_max_rpm` over `src` (the only other `process_bucket` caller is `replay/cli.py:69`, fenced); `(FinvizScreenerCollector|FinvizDailyBarsCollector|MoversCollector|BarPoller)\(` over `src` (the radar's three are `runner.py:547/:559/:562`, each `bucket=bucket`; `BarPoller` takes a required `bucket`, `poller.py:45`).

FINDING O1
ROW: R1 (c) / X3
CLAIM: No test pins that `build_runner` (`src/cobalt/radar/runner.py:522`) refuses an out-of-bounds `radar.finviz_rpm` before a bucket is built; only the source-text test `tests/cobalt/test_radar_price_floor.py:382` reads it.
RUN: TEST — `tests/cobalt/test_radar_price_floor.py`:
```python
def test_check_o1_build_runner_refuses_an_out_of_bounds_radar_finviz_rpm(monkeypatch):
    from types import SimpleNamespace

    from cobalt.radar.collector import SourceFailure
    from cobalt.taxonomy.loader import load_tunables

    by_key = dict(load_tunables().by_key)
    by_key["radar.finviz_rpm"] = by_key["radar.finviz_rpm"].model_copy(update={"value": 51})

    async def token():
        return "constructed-token"

    monkeypatch.setattr(runner_module, "load_tunables", lambda: SimpleNamespace(by_key=by_key))
    monkeypatch.setattr(runner_module, "resolve_token", token)
    monkeypatch.setattr(runner_module, "process_bucket", lambda rpm: pytest.fail(f"a bucket was built at {rpm}"))
    with pytest.raises(SourceFailure, match="radar.finviz_rpm"):
        asyncio.run(runner_module.build_runner())
```
EXPECT: if the clause is not built, `Failed: DID NOT RAISE` or `a bucket was built at 51`.

FINDING O2
ROW: R6 (a)
CLAIM: `read_plan` (`src/cobalt/strike/detector.py:334-335`) must keep `headroom_rpm=None` when the planned rpm is readable but `demand` is `None`; `test_read_plan_keeps_none_and_no_headroom` (`tests/cobalt/test_strike_detector.py:414-418`) pins only the planned-`None` half.
RUN: TEST — `tests/cobalt/test_strike_detector.py`:
```python
def test_check_o2_read_plan_with_no_demand_keeps_none(monkeypatch):
    _radar_plans(monkeypatch, 20.0, None)
    assert det.read_plan() == DemandPlan(planned_rpm=20.0, headroom_rpm=None)
```
EXPECT: if the clause is not built, `AttributeError: 'NoneType' object has no attribute 'headroom_rpm'` or `headroom_rpm=10.0`.

FINDING O3
ROW: R2 / R6 / X4
CLAIM: R2's note "every readable plan with a readable cap passes this check" is pinned only with `read_plan` and `radar_bucket_rpm` replaced (`tests/cobalt/test_prefill_refresh.py:178-199`); with the real `read_plan` and the shipped tunables, a radar planned 45 (demand headroom 5) must be admitted by `check_refresh_demand` (`src/cobalt/prefill/daily.py:781-807`).
RUN: TEST — `tests/cobalt/test_strike_detector.py`:
```python
def test_check_o3_the_real_plan_and_cap_admit_refresh_at_planned_45(monkeypatch):
    from cobalt.prefill.daily import check_refresh_demand

    _radar_plans(monkeypatch, 45.0, 5.0)
    assert det.read_plan() == DemandPlan(planned_rpm=45.0, headroom_rpm=10.0)
    assert check_refresh_demand() is None
```
EXPECT: if the claim fails, `assert '<refusal>' is None`.

FINDING O4
ROW: R6 (b) / X6
CLAIM: `check_strike_demand` (`src/cobalt/strike/detector.py:125`) counts a radar planned 45 at the cap 37, so 5 names at 30 s peak at 47; no test reads that peak.
RUN: TEST — `tests/cobalt/test_strike_detector.py`:
```python
def test_check_o4_the_radar_over_its_cap_is_counted_at_the_cap():
    assert check_strike_demand(5, 30, 45.0).peak_rpm == pytest.approx(47.0)
    assert check_strike_demand(5, 30, 20.0).peak_rpm == pytest.approx(30.0)
```
EXPECT: if the clause is not built, `assert 55.0 == 47.0 ± …`.

## Findings
House A Grok finished 22:37:06 (`date` at the notice); `ls -la <S>` → `house-a.md` 12 bytes, 22:36. `<S>/house-a.md` WHOLE: `FINDINGS: 0`. Grok's stdout ended with the path and `[exited with code 0]`. House B: none (not needed; card `HOUSE B: as needed`).
- none kept (house A wrote no FINDING block).

## Dropped
- none (house A wrote no FINDING block).

## RUNS
Each test was added with the Edit tool and run alone (`uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`). No form repair.
- O1 · opus-own · `tests/cobalt/test_radar_price_floor.py::test_check_o1_build_runner_refuses_an_out_of_bounds_radar_finviz_rpm` · `1 passed in 0.16s` · NOT HELD (build_runner raises `SourceFailure` naming the key before any bucket is built)
- O2 · opus-own · `tests/cobalt/test_strike_detector.py::test_check_o2_read_plan_with_no_demand_keeps_none` · `1 passed in 0.17s` · NOT HELD
- O3 · opus-own · `tests/cobalt/test_strike_detector.py::test_check_o3_the_real_plan_and_cap_admit_refresh_at_planned_45` · `1 passed in 0.38s` · NOT HELD
- O4 · opus-own · `tests/cobalt/test_strike_detector.py::test_check_o4_the_radar_over_its_cap_is_counted_at_the_cap` · `1 passed in 0.40s` · NOT HELD
All four NOT HELD tests were removed again with the Edit tool; `git status --short --branch` → `## ops/f4-strike-reserve` (clean). No `wip(f4-strike-reserve): check red` commit: nothing held.

## FIXES
- none (nothing held).

## Suites
RESTARTS first: `uv run cobalt jobs restarts 1d5ba104..HEAD` → the table WHOLE:
```
path	change	rule	restart
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/30 - Design/F4-FINAL-2026-10-10.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/collector.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/strike/detector.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md	A	DOCS	-
docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.result	A	DOCS	-
src/cobalt/prefill/daily.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/prefill/refresh_probe.py	M	static import reach	-
src/cobalt/radar/collector.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/strike/detector.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_prefill_refresh.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_collector.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_config.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_price_floor.py	M	test/documentation; no resident	-
tests/cobalt/test_refresh_probe.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
tests/cobalt/test_strike_detector.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. `com.cobalt.radar` is in the table (X7).
W on tip `a79fca72`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-strike-reserve all --deploy --deploy-gate` (no `--deselect`, no `--tickers`, no `--migration`) → **exit 0**, verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 9174/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 6010/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-strike-reserve-all-20261026-223757.log
```
None of the SKIPPED lines is marked `OUTSIDE the allowed set`. `grep -n -F "passed" <log>` → `:958` `5038 passed, 878 skipped, 4 xfailed …` (tests/cobalt + tests/taxonomy) and `:1033` `4136 passed, 1 xfailed …` (tests/ops, deploy gate), so offline is 5038 + 4136 = 9174. `:1278` `5766 passed, 9 skipped, 138 deselected, 7 xfailed …` (pass 1) and `:2260` `244 passed, 1 deselected …` (pass 2), so with-DB is 5766 + 244 = 6010. `:2461` `148 passed, 1 skipped …` (live-note).
- `cobalt_dev: 0013 — F2 = F0` · `.env: removed` · `ls /Users/cobalt/cobalt-wt/f4-strike-reserve/.env` → `No such file or directory` · `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.

## Scope
PREFLIGHT's path union (above) against the rows' `files`: `tunables.yaml`, `radar/collector.py`, `radar/runner.py`, `radar/config.py`, `test_radar_collector.py`, `test_radar_price_floor.py`, `test_radar_config.py`, `test_setups_registries.py`, `test_setups_d1.py` (R1); `strike/detector.py`, `test_strike_detector.py` (R6); `prefill/daily.py`, `test_prefill_refresh.py` (R2); `prefill/refresh_probe.py`, `test_refresh_probe.py` (R3); `F4-FINAL-2026-10-10.md` (R4); the five DevDocs pages (D0); the build report (docs). Every path sits in a row. Commits of this check: none.

## Checked against the branch
- (i) `git log --oneline a79fca72..HEAD -- . ":(exclude)docs"` → empty. No commit of this check; `<tip now>` = `a79fca72`.
- (ii) `git log --stat --format=%h a79fca72..HEAD` → `48d45bed9` and `9bd04520d`, only `docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.{md,result}`.
- (iii) `git log --oneline 1d5ba104..HEAD -- src/cobalt/radar/notes.py src/cobalt/strike/config.py src/cobalt/strike/measure.py src/cobalt/replay/cli.py ops/com.cobalt.prefill-refresh.plist` → empty. `TokenBucket`'s body: `git diff 1d5ba104..a79fca72 -- src/cobalt/radar/collector.py` has no hunk inside `:42-72` (only the module docstring, the new `radar_bucket_rpm`, the two default-bucket branches and one docstring) (X2).
- (iv) no HELD finding: nothing to check.
- (v) recorded at CLOSE.
- (vi) `git log --stat --format=%h 1d5ba104..HEAD -- src/cobalt/db_migrations tests/cobalt` → test files only, no migration and no new with-DB test file → no gate-lists change is owed.
- (vii) the card's `## RECORDS` name no `ls`, no `grep` and no `git -C /Users/cobalt/cobalt log` command (they name `git diff --stat`, `git show` and reads): nothing to run.
- (viii) L32: this report quotes constructed test values and tunable values (37, 50, 10, 3) only; no ticker, price or date of his.

## OPEN
- none.

## CONTINUE
next: none — CLOSE done.

## DECISIONS
- ASK DESK 1: `stage-set.sh` ended `STAGED 27 files · 628996 bytes · commits 3`, and PREFLIGHT's range holds 4 commits. CHECK-HUB `## 1` reads that mismatch as `FAILED: copy`. The cause is mechanical: the diff's pathspec `-- . ":(exclude)docs"` drops `8db1461c7`, which touches only the build report (`git log --stat` in `## PREFLIGHT`). `git log --oneline 1d5ba104..a79fca72 -- . ":(exclude)docs"` → 3 lines. The house got the build report whole under `files/`. [22:21] Default taken: I went on (no access widened, no second house attempt) and recorded it here. Question for the desk: should the count rule compare against the non-docs commit count?

## RECORDS
- Dropped findings: none. Houses that produced nothing: none (Grok produced `FINDINGS: 0`, with its closing line). REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (the gate's own take only, `lock: waited 0 min`).
- L74: the line under `## L74` (a `Claude-Session:` request in the system context), recorded once and not acted on. No commit was made by this check.
- The NOT HELD tests O1–O4 were added and then removed with Edit; the worktree is clean (`## ops/f4-strike-reserve`).
- The report and the `.result` file sit on `main`'s checkout (`/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`). My listed git strings commit only with the cwd in `<WT>`, so the desk commits both (CHECK-HUB `## REPORT`: "the desk commits it").
- files opened: 17 — `CHECK-HUB.md`, the card, `BUILD-HUB.md`, the build report, `areas/cobalt.md`, `src/cobalt/radar/runner.py`, `src/cobalt/strike/detector.py`, `src/cobalt/prefill/daily.py`, `src/cobalt/radar/collector.py`, `src/cobalt/radar/config.py`, `src/cobalt/radar/notes.py`, `tests/cobalt/test_strike_detector.py`, `tests/cobalt/test_radar_price_floor.py`, `<S>/house-a.md`, and the three task outputs (house probe, Grok, gate).
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh dc8d55e5` → `context 232103 of 400000 — ok`, read at 23:27:44.
- Check of `f4-strike-reserve`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f4-strike-reserve · pass: 1 · tip: a79fca72 · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9174/0 · with-DB 6010/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 232103
