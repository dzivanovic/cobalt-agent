# radar-display-fix-1008-terra — check (shadow) 2026-10-11

## §0 Headline
Shadow check of `radar-display-fix-1008-terra` (Terra build `e544d94f`, shadow of card 118). House A Grok `FINDINGS: 4`, house B none (not needed). Opus own 2.
Six findings, 0 dropped. All 6 HELD by their runs (opus-own 2 · house 4) and none fixed (shadow). The main fault: a JS comment at `radar_panel.py:1618` repeats the old fetch text, so 3 tests are met by the comment (O2, A1, A2). The others: the `owned` single-write rule is not pinned (O1), `layer`/`focused` are read outside the `try` (A3), and the module page still states the TERMINAL pause (A4).
Suites on `e544d94f`: offline 4000/0 · with-DB 4884/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. RESTARTS (committed range) `com.cobalt.aset com.cobalt.radar`.

## L74
- A system notice mid-session asked commits to end with a `Claude-Session:` line. Recorded once here, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/370-shadow-radar-display-fix-1008-terra-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/370-shadow-radar-display-fix-1008-terra-card.md" · 0 · a7167077086295bc5c4ad4cd8bc142b482f7b3f6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/370-shadow-radar-display-fix-1008-terra-card.md" · 0 · nothing
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
House gates: `grep -n "^| R17 "` → one row (line 35); `grep -n "^| R19 "` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 12 11:42:12 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/radar-display-fix-1008-terra
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h e544d94f..HEAD · 0 · (5 lines)
    64810652 docs(radar-display-fix-1008-terra): build report — e544d94f
    64810652

     ...adar-display-fix-1008-terra-build-2026-10-11.md | 185 +++++++++++++++++++++
     1 file changed, 185 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-display-fix-1008-terra/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/radar-display-fix-1008-terra/docs/40 - DevDocs/reports/radar-display-fix-1008-terra-build-2026-10-11.md" · 0 · SHADOW BUILT · job: radar-display-fix-1008-terra · tip: e544d94f | on 50b0cd87 | offline 4000/0 | with-DB 4884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | decisions: 2 · builder: gpt-5.6-terra · gate: radar-display-fix-1008-terra-gate · passes: 2 · suites at first run: green · builder tokens: 140792 · wall: 46
range · git log --oneline 50b0cd87..e544d94f · 0 · (2 lines)
    e544d94f feat(radar-display-fix-1008-terra): rows
    d2ac0bf1 wip(radar-display-fix-1008-terra): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: expected on a shadow card, recorded, not a finding.
- THE RANGE typed: `git log --stat --format=%h 50b0cd87..e544d94f` →
```
e544d94f
 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 src/cobalt/aset/radar_panel.py               | 23 ++++++++++++++++-------
 2 files changed, 19 insertions(+), 7 deletions(-)
d2ac0bf1
 tests/cobalt/test_radar_panel.py       | 79 +++++++++++++++++++++++++++++++++-
 tests/cobalt/test_radar_panel_cards.py | 63 ++++++++++++++++++++++++++-
 2 files changed, 139 insertions(+), 3 deletions(-)
```
  Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`.
- Card is not "DB: none" (DB key left out, card RECORDS).
- `ls <S>` → `No such file or directory` (fresh).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 → `grok: UP` · `gemini: UP`. No `HOUSE A: OpenAI` header line → OpenAI not probed.
- house A: Grok · house B: none (not needed) — card `HOUSE B: as needed`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · output whole:
```
13739 <S>/diff.md
16598 <S>/files/370-shadow-radar-display-fix-1008-terra-card.md
25432 <S>/files/radar-display-fix-1008-terra-build-2026-10-11.md
20947 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
84474 <S>/files/wt/src/cobalt/aset/radar_panel.py
66184 <S>/files/wt/tests/cobalt/test_radar_panel.py
56846 <S>/files/wt/tests/cobalt/test_radar_panel_cards.py
754 <S>/rulings.md
STAGED 8 files · 284974 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-terra-check`; commits 2 = PREFLIGHT's range count.)
`stage-copy.sh`, one call each:
- `COPIED 2208 <S>/files/radar-cards-survey-2026-10-08-r2.md`
- `COPIED 23148 <S>/files/radar-ladder-refresh-build-2026-10-06.md`
- `COPIED 106471 <S>/files/wt/src/cobalt/aset/web.py`
- `COPIED 75264 <S>/files/wt/src/cobalt/cards/store.py`
- `COPIED 14043 <S>/files/wt/src/cobalt/db.py`
`<S>/HOUSE-INSTRUCTIONS.md` written (18369 bytes per `ls -la <S>`).
House A Grok started 11:43:49 EDT (`date`); gates R17, R19 re-run → one row each; `cd <AGY>` → grok line → `cd <WT>` → `git status --short --branch` → `## shadow/radar-display-fix-1008-terra` + `?? SHADOW-INSTRUCTIONS.md` (shadow, expected). House B: none (not needed).

## OWN FINDINGS
Written before either house list was opened.

FINDING O1
ROW: D
CLAIM: Row D's `test_a_skipped_tick_never_clears_another_fetchs_in_flight_flag` (`tests/cobalt/test_radar_panel.py:1247`–`:1251`) claims "`owned=true;` is the only write to `owned` after its declaration" but counts only `owned=true;`; a second write `owned=false;` after `owned=true;` (`src/cobalt/aset/radar_panel.py:1616`) makes `finally` (`:1639`) never reset `ladderInFlight`, latching the tick for good, and that test stays green.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_a_second_write_to_owned_is_caught(monkeypatch):
    broken = panel.PANEL_JS.replace("owned=true;\n", "owned=true; owned=false;\n", 1)
    assert broken != panel.PANEL_JS
    monkeypatch.setattr(panel, "PANEL_JS", broken)
    with pytest.raises(AssertionError):
        test_a_skipped_tick_never_clears_another_fetchs_in_flight_flag()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O2
ROW: C
CLAIM: A JS comment `// fetch('/radar',{headers:{accept:'text/html'}}) now carries the abort signal below.` (`src/cobalt/aset/radar_panel.py:1618`) carries the exact needle `test_tick_refreshes_the_ladder_on_the_pool_timer_without_reload` asserts (`tests/cobalt/test_radar_panel.py:1148`), so that assertion is met by a comment, not by the real call (`:1619`), and `_tick_stretches()` (`tests/cobalt/test_radar_panel.py:1136`) and the row C/D tests index `fetch('/radar'` at the comment.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_the_tick_names_its_fetch_once_outside_a_comment():
    body = _js_body(TICK_HEAD)
    assert body.count("fetch('/radar'") == 1
    assert "//" not in body
```
EXPECT: `assert 2 == 1` (the comment and the real fetch).

## Findings
House A Grok finished 12:03:41 EDT (`date` at the notice); `<S>/house-a.md` 3935 bytes, written by Grok, ends `FINDINGS: 4`. House B: none (not needed).
- O1 · opus-own · D · `owned=true;`-only count leaves a second write `owned=false;` (permanent latch) uncaught by the row D test · TEST
- O2 · opus-own · C · a JS comment carries the old fetch needle; the tests index `fetch('/radar'` at the comment · TEST
- A1 · Grok · C · the pool-timer pin's fetch needle sits only in the comment; changing the real URL leaves it green · TEST
- A2 · Grok · C · the hung-fetch test's `signal:ctl.signal` check is met by text on the comment line, not the call · TEST
- A3 · Grok · D · `const layer=` and `const focused=` reads sit before `try{`, unpinned · TEST
- A4 · Grok · SCOPE · the DevDocs page's standing tick rules still say the tick skips while TERMINAL is open · COMMAND

## Dropped
none — every block carries a `RUN:` line followed by a `def test_` or one `grep` line (`grep -n -F "RUN:"` over `house-a.md` reads 4 lines, one per block).

## RUNS
Each TEST was put in `tests/cobalt/test_radar_panel.py` with the Edit tool (after `test_the_bare_in_flight_reset_mutation_is_caught`) as written, with no change to its form, and run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::<test>`.
- O1 · opus-own · `test_a_second_write_to_owned_is_caught` · `1 failed in 0.58s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` · HELD (shadow: fixes none)
- O2 · opus-own · `test_the_tick_names_its_fetch_once_outside_a_comment` · `1 failed in 0.39s` · `E       assert 2 == 1` (on `body.count("fetch('/radar'") == 1`) · HELD (shadow: fixes none)
- A1 · Grok · `test_the_pool_timer_pin_tracks_the_executable_tick_fetch` · `1 failed in 0.39s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` · HELD (shadow: fixes none)
- A2 · Grok · `test_hung_fetch_pin_requires_the_signal_on_the_call` · `1 failed in 0.39s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` · HELD (shadow: fixes none)
- A3 · Grok · `test_tick_preamble_reads_sit_inside_the_try` · `1 failed in 0.39s` · `E       assert 16 > 170` (on `body.index("document.getElementById('ladder-layer')") > try_at`). Row D: "The whole body, guards included, sits inside the `try`"; it names only `owned`, `ctl` and `timer` to sit before `try{` · HELD (shadow: fixes none)
- A4 · Grok · the command carries `\|`, which this seat may not type (UNATTENDED RULES: one fixed string per grep call); run as its two fixed-string halves: `grep -n -F "TERMINAL is open" "docs/40 - DevDocs/cobalt/aset/radar_panel.md"` → `204:… (2) It never destroys work in progress: it skips, and drops a result that lands, while a tap strip is open, TERMINAL is open, a ladder input has focus, …`; `grep -n -F "preserves open TERMINAL" …` → `215:\`tickLadder\` preserves open TERMINAL details, aborts hung fetches, and reports a ladder that has not refreshed.` The output shows the claim: the module page still states the TERMINAL pause as a standing rule (:204) and the dated line (:215) does not retract it. The SCOPE half (the page is not a row file) is not held: CHECK-HUB `## 5` and BUILD-HUB E3 admit one dated DevDocs line in the changed module's page · HELD, stale doc part only (shadow: fixes none)
SHADOW: the card is a shadow card (SHADOW OF: 118), on which the check counts and holds findings and fixes none (CHECK-HUB `## THE FLOW`). So no `wip(<JOB>): check red` commit was made: the five tests were removed again with the Edit tool, and `git status --short --branch` → `## shadow/radar-display-fix-1008-terra` + `?? SHADOW-INSTRUCTIONS.md` (the tree is the build's tip). Each test lives verbatim under `## OWN FINDINGS` (O1, O2) and in `<S>/house-a.md` (A1–A3), for the original builder's fix round.

## FIXES
none — shadow card, fixes none. Held and not fixed here: O1, O2, A1, A2, A3, A4 (all six inside the rows' files: `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, plus the DevDocs page's dated line for A4).

## Suites
RESTARTS first: `uv run cobalt jobs restarts 50b0cd87..HEAD` → exit 1, whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-1008-terra-build-2026-10-11.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The one UNCLASSIFIED path is the untracked shadow file `SHADOW-INSTRUCTIONS.md` (expected on a shadow card, never committed); it is not classified (it is no code path; the build's DECISION 1 carries it). Committed range: `uv run cobalt jobs restarts 50b0cd87..e544d94f` → exit 0, last line `RESTARTS: com.cobalt.aset com.cobalt.radar` (row F, as the card expects).
W: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-display-fix-1008-terra all --deploy` on `e544d94f` (no commit of mine) → exit 0, verdict lines whole:
```
offline 4000/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4884/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-display-fix-1008-terra-all-20261012-120445.log
```
No skip marked `OUTSIDE the allowed set`. `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## shadow/radar-display-fix-1008-terra` + `?? SHADOW-INSTRUCTIONS.md` (shadow, expected).

## Scope
PREFLIGHT path union: `src/cobalt/aset/radar_panel.py` (rows B, C, D — `PANEL_JS` only, diff hunks at `:1603`–`:1639`), `tests/cobalt/test_radar_panel.py` (B, C, D), `tests/cobalt/test_radar_panel_cards.py` (A, E), `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (the admitted dated DevDocs line). My commits: none. No path outside the rows' files.
X4: `git diff --name-only 50b0cd87..HEAD -- src` → `src/cobalt/aset/radar_panel.py` alone; the hunks lie inside `PANEL_JS` (`:1536`–`:1645`); the pins `PIN_HEALTHY_*` are not in the diff.

## Checked against the branch
- (i) `git log --oneline e544d94f..HEAD -- . ":(exclude)docs"` → empty (no commit of mine); `<tip now>` = `e544d94f`.
- (ii) `git log --stat --format=%h e544d94f..HEAD` → `64810652` · the build report only (docs).
- (iii) `git log --oneline 50b0cd87..HEAD -- src/cobalt/aset/web.py src/cobalt/cards/store.py src/cobalt/db_migrations` → empty. The fenced names inside `radar_panel.py` (`build_ladder_view`, `render_ladder`, `refreshLadder`, `refreshPool`, `post`, the CSS) are outside the diff's hunks (the `git diff` read at `## 2`).
- (iv) no HELD finding was fixed (shadow); no check-red commit.
- (v) `ls <WT>/.env` and `git status`: under `## Suites` / `## 8`.
- (vi) `git log --stat --format=%h 50b0cd87..HEAD -- src/cobalt/db_migrations tests/cobalt` → `d2ac0bf1` · the two offline test files; no migration, no with-DB test above `0013` → no gate-list change owed.
- (vii) card RECORDS: `grep -c -F "radar panel FAILED" /Users/cobalt/cobalt/logs/aset.log` → `0` (NO SERVER FAILURE holds on today's file); `wc -l /Users/cobalt/cobalt/logs/aset.log` → `21825` (the file has grown since the record's 15527; its line refs are a 10-08 reading and are not re-read); `git -C /Users/cobalt/cobalt log --oneline -1 50b0cd87` → `50b0cd87 docs(desk): radar display-fix drafter 55902983 launched` (BASE).
- (viii) L32: this report holds only constructed test values and the card's own dates.

## OPEN
Shadow card: every held finding is held and not fixed here, for the original builder's one fix round:
- O1 (D): pin "`owned=true;` is the only write to `owned`" in `test_a_skipped_tick_never_clears_another_fetchs_in_flight_flag`, e.g. `body.count("owned=") == 2`. Settled by O1's test going green.
- O2 / A1 / A2 (C): remove the comment at `radar_panel.py:1618`; amend the needle at `test_radar_panel.py:1148` to the real call text `fetch('/radar',{headers:{accept:'text/html'},signal:ctl.signal})`; pin `signal:ctl.signal` on the call line itself. Settled by O2's, A1's and A2's tests going green.
- A3 (D): move `const layer=…` and `const focused=…` inside `try{` (row D, "the whole body … inside the `try`"). Settled by A3's test going green.
- A4 (D, doc): a dated line in `docs/40 - DevDocs/cobalt/aset/radar_panel.md` saying the TERMINAL pause of rule (2) at `:204` is withdrawn (R685). Settled by the line.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none. The six held findings are the shadow's grade data. A shadow is never deployed, so they block no next step; they are listed under `## OPEN`.

## RECORDS
- Dropped findings: none.
- Every house produced a list: Grok `FINDINGS: 4`. House B not seated (`HOUSE B: as needed`; Gemini UP and not needed).
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (the one take was by `gate.sh`, waited 0 min).
- L74: one system notice asked for a `Claude-Session:` line; recorded under `## L74`, not acted on.
- A4's command was run as two fixed-string greps (its `\|` is not typeable here); recorded under `## RUNS`.
- Of WHAT YOU READ (5), `areas/cobalt.md` was not opened. The card, the diff and the build report were enough to judge the rows; it is recorded here, not hidden.
- files opened: 10 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); the build report; `src/cobalt/aset/radar_panel.py` (`:1530`–`:1647`); `tests/cobalt/test_radar_panel.py` (`:1100`–`:1389`); `<S>/house-a.md`; three task outputs (house probe, Grok, gate).
- Check of `radar-display-fix-1008-terra`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-display-fix-1008-terra · pass: 1 · tip: e544d94f · house A: Grok FINDINGS: 4 · findings: 6 · dropped: 0 · held: 6 (opus-own 2 · house 4) · fixed: 0 · held unfixed: 6 · open: 6 · house B: none available · suites: offline 4000/0 · with-DB 4884/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 10 · ready: N/A (shadow, never deployed) · decisions: 0 · for Dejan: 0 · tokens: 160927
