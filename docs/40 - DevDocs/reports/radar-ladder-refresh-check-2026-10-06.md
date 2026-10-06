# radar-ladder-refresh — CHECK (pass 1) — 2026-10-06

## §0 Headline
Check of `radar-ladder-refresh` at `d2330003`: Sol 6 findings, Grok 3, own 3 — 12 in all, 11 held and fixed, 0 dropped. The one other (A2, the X29 control's setup error) is out of scope and carried.
Real defect fixed: a `post()` that began and ended inside one tick's fetch let the tick swap in an older ladder (O3 = A1 = B1). It is closed by a `sendGeneration` sequence. The rest were weak static tests, now strengthened.
New tip `ed19060f`. Gate: offline 3963/0 · with-DB 4847/0 · live-note 146/0 · cobalt_dev 0013 F2 = F0 · .env removed. ready: YES.

## L74
One block arrived (a system reminder mid-session, 17:4x ET) asking commits to end with a `Claude-Session:` line. Recorded once, acted on none: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
- `sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md" · 0 · dcd63c49445959f63c7d858d936ffd3daf054e09
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R556 row · grep -n "^| R556 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 107:| R556 | 14:20 ET | HIS RULING ([words](cto-2026-10-06-words.md) `## R556`): fix the empty radar screen if the brain says GO (bandwidth, no blocker); desk asked the brain 14:20; on GO the desk launches the fix flow, no further ask to him. | HIS RULING · APPROVED |
RULING 2026-10-06 R556 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R556 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 8bceed0a20d4157786a85a2f0e44a76a1ff2bf30
RULING 2026-10-06 R556 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```
- House gate R17: `grep -n "^| R17 " ".../cto-2026-09-24.md"` · exit 0 · one row, line 35 (`| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` → STANDING `Bash(grok *)` … `| APPLIED: …`).
- House gate R19: `grep -n "^| R19 " ".../cto-2026-09-24.md"` · exit 0 · one row, line 37 (`| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` → STANDING the four house strings … `| APPLIED: …`).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · exit 0 · `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output WHOLE:
```
clock · date · 0 · Tue Oct  6 17:43:51 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-ladder-refresh-1006
head · git log --oneline -1; git log --stat --format=%h d2330003..HEAD · 0 · (5 lines)
    94ef37fe docs(radar-ladder-refresh): build report — d2330003
    94ef37fe
    
     .../radar-ladder-refresh-build-2026-10-06.md       | 173 +++++++++++++++++++++
     1 file changed, 173 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-ladder-refresh-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/radar-ladder-refresh-1006/docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md" · 0 · BUILT · job: radar-ladder-refresh · tip: d2330003 | on 8c554d77 | migration: none | offline 3952/0 | with-DB 4836/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 172093
range · git log --oneline 8c554d77..d2330003 · 0 · (2 lines)
    d2330003 fix(radar-ladder-refresh): the pool timer also refreshes the ladder through tickLadder (A, B, L1, L3)
    7ba8880e wip(radar-ladder-refresh): red — tickLadder static tests and route control (A, R556)
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h 8c554d77..d2330003` · exit 0:
```
d2330003

 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 src/cobalt/aset/radar_panel.py               | 32 ++++++++++++++++++++++++++--
 2 files changed, 33 insertions(+), 2 deletions(-)
7ba8880e

 tests/cobalt/test_radar_panel.py | 131 +++++++++++++++++++++++++++++++++++++++
 1 file changed, 131 insertions(+)
```
  Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`. Commit count 2.
- The card is not "DB: none" (no such header line): the DB-none row does not apply.
- `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check` · exit 1 · `No such file or directory` → fresh.
- House gates: as `## AUTHORIZATION`.
- `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` (background) · exit 0 · output WHOLE:
```
sol: UP
grok: UP
gemini: OUT — OK.
```
  → house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed — not mandatory; both seats are filled anyway.
- Self-check count in the build's last line: `3 of 3`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output WHOLE:
```
11437 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check/diff.md
15126 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check/files/54-radar-ladder-refresh-card.md
23148 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check/files/radar-ladder-refresh-build-2026-10-06.md
18267 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
81899 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check/files/wt/src/cobalt/aset/radar_panel.py
57094 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check/files/wt/tests/cobalt/test_radar_panel.py
357 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-ladder-refresh-check/rulings.md
STAGED 7 files · 207328 bytes · commits 2
```
`commits 2` = PREFLIGHT's count; `grep -c "^commit " <S>/diff.md` → `2`. The same `diff.md` and `rulings.md` serve Sol (house A).
`stage-copy.sh`, one call each (the card's `## READ` reports and files named by symbol, plus the control `test_s3_c3_panel_offline.py` row A names):
- `COPIED 9787 …/files/radar-screen-trace-2026-10-06.md`
- `COPIED 5521 …/files/cards-origin-survey-2026-10-06-r2.md`
- `COPIED 2425 …/files/radar-page-read-2026-10-06.md`
- `COPIED 104855 …/files/wt/src/cobalt/aset/web.py`
- `COPIED 38697 …/files/wt/tests/cobalt/test_radar_panel_cards.py`
- `COPIED 3017 …/files/wt/tests/experiments/stale_score/test_x29_ladder_render.py`
- `COPIED 31580 …/files/wt/tests/cobalt/test_s3_c3_panel_offline.py`
`<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the `Files:` paragraph.
Houses started 17:45 (`date` 17:45:43): Sol (`codex exec … gpt-5.6-sol …`, background) and Grok (`grok -m grok-4.7 --sandbox cobalt-job …`, background), cwd `<AGY>`; back in `<WT>`, `git status --short --branch` → `## ops/radar-ladder-refresh-1006`.

## OWN FINDINGS
Written by 17:47 ET (`date`), before either house's list was opened.

FINDING O1
ROW: A (2) · X1 · X3
CLAIM: `test_tick_never_swaps_over_work_in_progress` (`tests/cobalt/test_radar_panel.py:1159`) checks the name `activeElement` in each stretch, but each stretch also holds the bare read `const focused=document.activeElement;` / `const active=document.activeElement;` (`src/cobalt/aset/radar_panel.py:1579`, `:1589`), so the focused-input guard can be removed from either check and the test stays green.
RUN: COMMAND — with the Edit tool remove `(focused&&focused.tagName==='INPUT'&&layer.contains(focused))||` from `radar_panel.py:1580` (and, as a second run, `(active&&active.tagName==='INPUT'&&now.contains(active))||` from `:1590`), then `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::test_tick_never_swaps_over_work_in_progress`; undo.
EXPECT: `1 passed` under each mutation.

FINDING O2
ROW: A (4) · X3
CLAIM: `test_one_ladder_fetch_in_flight_and_none_while_a_post_sends` (`tests/cobalt/test_radar_panel.py:1191`) asserts `"ladderInFlight" in before`, which the assignment `ladderInFlight=true;` (`radar_panel.py:1581`) satisfies alone, so the in-flight check in the first guard (`:1580`) can be removed and the test stays green.
RUN: COMMAND — with the Edit tool remove `ladderInFlight||` from `radar_panel.py:1580`, then `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::test_one_ladder_fetch_in_flight_and_none_while_a_post_sends`; undo.
EXPECT: `1 passed` under the mutation.

FINDING O3
ROW: A (4) · X1
CLAIM: a `post()` that begins after the tick's `fetch('/radar')` (`radar_panel.py:1583`) and ends (its `finally{sending-=1;}`, `:1538`) before the tick's result lands leaves `sending` at 0 at the second guard (`:1590`), so the tick swaps a render older than the one `post()` just drew (`:1535`) — the row says "a stale response never overwrites the ladder `post()` itself just refreshed", and X1 asks for "a result that lands after one of these began"; nothing records that a post began during the fetch.
RUN: TEST — `tests/cobalt/test_radar_panel.py`:
```python
def test_a_post_that_begins_and_ends_inside_one_tick_drops_its_result():
    post = _js_body("async function post(cardId,path,body){")
    assert "posted+=1;" in post
    before, after, _ = _tick_stretches()
    assert "const seen=posted;" in before
    assert "posted!==seen" in after
```
EXPECT: `AssertionError` at `assert "posted+=1;" in post` (no post sequence exists at the tip).

## Findings
Sol finished 17:53 (`date` 17:53:19; its final message written by me to `<S>/house-a.md`, `FINDINGS: 6`). Grok finished 18:05 (`date` 18:05:16; it wrote `<S>/house-b.md` itself and replied with the path, `FINDINGS: 3`). Every block carries a `RUN:` followed by a `def test_` or an `uv run pytest` line: none dropped.

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| A1 | Sol | X1 | A `post()` that starts and finishes during the tick's fetch returns `sending` to 0, so the older tick response replaces the ladder `post()` just refreshed. | TEST |
| A2 | Sol | X3 | The named X29 control is not green on the tip: it errors at setup. | COMMAND |
| A3 | Sol | A | The failed-tick test only searches for `ladder-refresh-status` anywhere; removing `box.id=…` leaves it green. | TEST |
| A4 | Sol | A | The single-flight test never pins `let sending=0;` or `let ladderInFlight=false;`; removing either leaves it green. | TEST |
| A5 | Sol | A | The timer test does not reject a duplicated `setInterval(tickLadder,interval)` line. | TEST |
| A6 | Sol | A | The tests read only the first `tickLadder`; a later empty duplicate leaves them green. | TEST |
| B1 | Grok | X1 | Same race as A1/O3: the post-await check is only the live `sending>0`. | TEST |
| B2 | Grok | A | The WIP test stays green when both focus clauses are deleted, since `activeElement` remains in the bare reads. | TEST |
| B3 | Grok | A | The single-flight test stays green when the `ladderInFlight||` skip is deleted; the assignment satisfies it. | TEST |

## Dropped
none.

## RUNS
Each test was put into `tests/cobalt/test_radar_panel.py` with the Edit tool, after the R556 block. They ran together in ONE call, `uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line <the node ids>`. Each is independent and reads only `panel.PANEL_JS`, and the call quotes each test's own outcome. Result at tip `d2330003`: `10 failed in 0.44s`.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | Edit removed `(focused&&…layer.contains(focused))\|\|` (`:1580`) and `(active&&…now.contains(active))\|\|` (`:1590`), together with O2's mutation; then `uv run pytest … ::test_tick_never_swaps_over_work_in_progress ::test_one_ladder_fetch_in_flight_and_none_while_a_post_sends`; undone, `git diff --stat -- src` → empty | `PASSED …::test_tick_never_swaps_over_work_in_progress` · `2 passed in 0.35s` | HELD. Its standing test is `test_the_wip_test_fails_when_the_focus_guard_is_undone`, red at tip: `Failed: DID NOT RAISE <class 'AssertionError'>` (`:1250`) |
| O2 | own | Edit removed `ladderInFlight\|\|` from `:1580` (same call as O1) | `PASSED …::test_one_ladder_fetch_in_flight_and_none_while_a_post_sends` | HELD. Its standing test is `test_the_single_flight_test_fails_when_the_in_flight_skip_is_undone`, red at tip: `Failed: DID NOT RAISE` (`:1258`) |
| O3 | own | TEST `test_a_post_that_begins_and_ends_inside_one_tick_drops_its_result` | `assert 'posted+=1;' in "\n   status(cardId,'sending','pending'); sending+=1; …"` (`:1239`); renamed below `assert 'sendGeneration+=1;' in …` (`:1239`) | HELD. Form repaired once before the red commit: the variable name `posted` became `sendGeneration`, so one name serves O3, A1 and B1; the assertion is unchanged |
| A1 | Sol | TEST `test_tick_drops_a_response_when_a_post_completes_during_the_fetch` | `AssertionError: no monotonic post sequence records a post that starts and finishes during the tick fetch` (`:1257`) | HELD |
| A2 | Sol | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/stale_score/test_x29_ladder_render.py` | `ERROR at setup of test_x29_chip_and_slot_move_at_the_next_render_not_on_the_periodic_refresh` · `E       fixture 'offline_skip_guard' not found` (`tests/cobalt/conftest.py:262`) · `1 error in 0.08s`. `git diff --stat 8c554d77..d2330003 -- tests/experiments tests/cobalt/conftest.py` → no output | OUT OF SCOPE — the output is as claimed, but the build touches neither file, and the fix lies in fenced files (`## NOT IN THIS JOB`: "Editing an existing test, `test_x29_ladder_render.py` included"; "A red outside these rows goes under `## DECISIONS` as UNPROVEN (L70) … never fixed here"). Carried under `## DECISIONS` |
| A3 | Sol | TEST `test_failed_tick_test_rejects_a_created_status_without_its_required_id` | `Failed: DID NOT RAISE <class 'AssertionError'>` (`:1294`) | HELD |
| A4 | Sol | TEST `test_single_flight_test_requires_its_state_declarations` (2 params) | both `Failed: DID NOT RAISE <class 'AssertionError'>` (`:1308`) | HELD |
| A5 | Sol | TEST `test_tick_timer_test_rejects_a_duplicate_interval` | `Failed: DID NOT RAISE <class 'AssertionError'>` (`:1317`) | HELD |
| A6 | Sol | TEST `test_tick_test_rejects_a_later_duplicate_function` | `Failed: DID NOT RAISE <class 'AssertionError'>` (`:1329`) | HELD |
| B1 | Grok | TEST `test_x1_a_post_that_finishes_during_the_fetch_still_drops_the_tick` | `assert ('sendGeneration' in "await response.text() …" or 'sentDuring' in … or 'sending!==' in …)` (`:1341`) | HELD |
| B2 | Grok | TEST `test_undoing_the_focus_guard_turns_the_wip_test_red` | `AssertionError: shipped rule (2) stays green after the focus clause is deleted` (`:1354`) | HELD |
| B3 | Grok | TEST `test_undoing_the_inflight_skip_turns_rule4_red` | `AssertionError: rule (4) stays green if the in-flight skip is deleted` (`:1367`) | HELD, for the same defect as O2. Its last line asserts `"ladderInFlight||" in mutant` on the mutant it just built, so it can never pass. It was removed with the Edit tool before the red commit; its standing test is O2's |

Red commit: `1e7fe5f2 wip(radar-ladder-refresh): check red — O1 O2 O3 A1 A3 A4 A5 A6 B1 B2`. In that commit, the three standing tests above fail at the tip: `3 failed in 0.42s`.

## FIXES
One commit, `ed19060f fix(radar-ladder-refresh): a post that begins inside a tick's fetch drops its result; the guard tests pin each guard (check O1 O2 O3 A1 A3 A4 A5 A6 B1 B2)`, files `src/cobalt/aset/radar_panel.py` (`PANEL_JS` only), `tests/cobalt/test_radar_panel.py` and `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (one dated line).

| ids | fix |
|---|---|
| O3 · A1 · B1 | `let sendGeneration=0;` beside `let sending=0;`. `post()` raises it with `sending` (`sending+=1; sendGeneration+=1;`), and it never goes down. `tickLadder` takes `const seen=sendGeneration;` before its fetch, and its second guard adds `sendGeneration!==seen`. `sending` and its `finally` are unchanged |
| O1 · B2 | `TICK_GUARDS` gains `tagName==='INPUT'`, so test (2) needs the focus clause itself in both stretches |
| O2 · B3 · A4 | test (4) asserts that `ladderInFlight` sits inside the first guard's `if(…){return;}`, and that ` let sending=0;\n` and ` let ladderInFlight=false;\n` are in the script |
| A3 | test (3) needs `box.id='ladder-refresh-status'` in the catch |
| A5 · A6 | test (1) asserts `window.setInterval(tickLadder,interval);` occurs once and `function tickLadder(` occurs once |

Edits to the builder's new tests (added in this branch at `7ba8880e`, not on BASE) strengthen them only. Nothing was loosened. After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_s3_c3_panel_offline.py` → `167 passed, 11 skipped in 2.11s`. That covers every held test and the controls `test_radar_panel.py:1038`–`:1103`, `test_radar_panel_cards.py:495`–`:508`, `:646`–`:679` and `test_s3_c3_panel_offline.py:546`–`:550`. Each skip is `reaches cobalt_dev (lock-relief G1)` or `requires_db`, and the with-DB pass runs them.

## Suites
RESTARTS first: `uv run cobalt jobs restarts 8c554d77..HEAD` · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
There is no UNCLASSIFIED row.
Then `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-ladder-refresh-1006 all --deploy` ran on tip `ed19060f` (background) and exited 0. It took no `--deselect`, `--tickers` or `--migration`: the check adds no with-DB test and no migration. Verdict lines, WHOLE:
```
offline 3963/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4847/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-ladder-refresh-1006-all-20261006-180724.log
```
No skip is marked `OUTSIDE the allowed set`. Offline went from the build's 3952 to 3963. The difference is the 11 test ids this check adds: O3, the O1 and O2 standing tests, A1, A3, A4 ×2, A5, A6, B1 and B2. `ls /Users/cobalt/cobalt-wt/radar-ladder-refresh-1006/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union is `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py` and `tests/cobalt/test_radar_panel.py`. My commits touch those same three paths: row A's files, plus row B's page for the one dated line. Nothing else is touched.

## Checked against the branch
- (i) `git log --oneline d2330003..HEAD -- . ":(exclude)docs"` → `ed19060f fix(radar-ladder-refresh): … (check O1 O2 O3 A1 A3 A4 A5 A6 B1 B2)` · `1e7fe5f2 wip(radar-ladder-refresh): check red — O1 O2 O3 A1 A3 A4 A5 A6 B1 B2`. `<tip now>` = `ed19060f`.
- (ii) `git log --stat --format=%h d2330003..HEAD` → `ed19060f`: the page `radar_panel.md`, `src/cobalt/aset/radar_panel.py` and `tests/cobalt/test_radar_panel.py`; `1e7fe5f2`: `tests/cobalt/test_radar_panel.py`; `94ef37fe`: the build report (docs). Every path is in a row's files.
- (iii) Fence: `git log --oneline 8c554d77..HEAD -- src/cobalt/aset/web.py src/cobalt/cards tests/experiments PANEL_CSS` → empty. `git diff 8c554d77..HEAD -- src/cobalt/aset/radar_panel.py` shows no pool line, no `render_ladder` line, no `PANEL_CSS` line and no change to `window.setInterval(refreshPool,interval);`. `refreshLadder`'s body is byte-pinned by test (1).
- (iv) `grep -n -F "def test_" tests/cobalt/test_radar_panel.py` → O3 `:1243`, O1 `:1251`, O2 (and B3) `:1260`, A1 `:1268`, A3 `:1306`, A4 `:1325`, A5 `:1335`, A6 `:1344`, B1 `:1356`, B2 `:1367`, one line each. In (i), `1e7fe5f2` (red) sits below `ed19060f` (fix).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/radar-ladder-refresh-1006`.
- (vi) `git log --stat --format=%h 8c554d77..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_radar_panel.py` (offline tests). There is no migration and no with-DB test above 0013. `git diff 8c554d77..HEAD -- ops/desk/gate-lists.md` → empty, which is correct.
- (vii) Card record LIMIT: `grep -rln playwright tests/cobalt` → no output, as recorded.
- (viii) L32: this report holds no ticker, price or date of his. The test ticker in the build's route control is the suite's constructed fixture, used in 30 test files.

## OPEN
- A2: OUT OF SCOPE (fence), not open. `tests/experiments/stale_score/test_x29_ladder_render.py` errors at setup (`fixture 'offline_skip_guard' not found`). The build did not touch it, and the fix belongs to a later card on `tests/experiments/stale_score/conftest.py` or `tests/cobalt/conftest.py`.
- open: 0.

## CONTINUE
next: 8 (done)

## DECISIONS
- DECISION 1 (UNPROVEN, L70; outside the rows; carried, not fixed). Card row A names the control `test_x29_ladder_render.py:44`–`:63` "green on BASE and after, unedited". It cannot run: `ERROR at setup … fixture 'offline_skip_guard' not found` (`tests/cobalt/conftest.py:262`). The build changed neither file. The text constraints X29 reads are pinned by the build's test (1), whose byte pin of `refreshLadder` and pool timer assertions are green. Safe default taken: not fixed here (fence). The desk can give the conftest re-export a card of its own. Not his.

## RECORDS
- Started 17:43 ET (preflight `date`). Both houses started 17:45 (`date` 17:45:43). Own findings were written by 17:47 (`date` 17:47:20), before Sol finished at 17:53. Grok finished 18:05. The gate finished before 18:35 (`date` 18:35:00).
- Houses: A = Sol (`gpt-5.6-sol`) `FINDINGS: 6`; B = Grok (`grok-4.7`) `FINDINGS: 3`. Gemini probed `OUT — OK.` and was not seated.
- Dropped: none. No house produced nothing.
- No `REFUSED, not needed` line and no `CONTINUED`. The only lock take was the one inside `gate.sh`.
- L74: one block arrived asking for a `Claude-Session:` commit line. It is recorded under `## L74`; nothing was acted on.
- B3's test function was removed before the red commit: it asserts on its own mutant and can never pass. Its defect is held and fixed through O2's standing test.
- The O1 and O2 mutations ran in one Edit set, and each ran its own named test. Both were undone, and `git diff --stat -- src` → empty.
- `files opened: 12`. The Read tool and full-file reads opened: `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); `src/cobalt/aset/radar_panel.py` (`:1440`–`:1619`); `tests/cobalt/test_radar_panel.py` (`:1110`–`:1239`); the build report (`:95`–end); the house-probe output; Sol's output (final list); Grok's output; `<S>/house-b.md`; the gate output; and this report (written, not read). `areas/cobalt.md` (WHAT YOU READ (5)) was NOT opened in this session, an omission recorded as fact. The diff was read through `git diff`.
- Check of `radar-ladder-refresh`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-ladder-refresh · pass: 1 · tip: ed19060f · house A: Sol FINDINGS: 6 · findings: 12 · dropped: 0 · held: 11 · fixed: 11 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 3 · suites: offline 3963/0 · with-DB 4847/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181164
