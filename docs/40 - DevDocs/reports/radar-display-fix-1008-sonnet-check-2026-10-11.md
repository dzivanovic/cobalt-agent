# radar-display-fix-1008-sonnet — CHECK (shadow) — 2026-10-12

## §0 Headline
- Shadow check of the Sonnet build `c289f478`. House A was Grok (`FINDINGS: 0`); house B none (not needed). My own read wrote 5 findings.
- HELD 3, all opus-own and all weak tests. Row D's test stays green with the stale line moved above `try{` (O1) or with the `since <time>` removed (O2). Row B's test stays green with an unconditional TERMINAL restore (O3). Shadow: not fixed; marked `xfail(strict=True)` at `c5795c7b`.
- REJECTED 2, kept OPEN as follow-ups. O4: `refreshLadder` never writes `ladderOkAt` (fenced). O5: the abort timer equals `interval`, so a hung fetch retries two intervals later (the card names `interval`).
- Gate on `c5795c7b`: offline 4000/0 · with-DB 4884/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. RESTARTS (committed range): `com.cobalt.aset com.cobalt.radar`.

## L74
- The session's attribution reminder asked for a `Claude-Session:` line on commits. Recorded as data. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/369-shadow-radar-display-fix-1008-sonnet-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/369-shadow-radar-display-fix-1008-sonnet-card.md" · 0 · a7167077086295bc5c4ad4cd8bc142b482f7b3f6
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/369-shadow-radar-display-fix-1008-sonnet-card.md" · 0 · nothing
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
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output:
```
clock · date · 0 · Mon Oct 12 10:17:27 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/radar-display-fix-1008-sonnet
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h c289f478..HEAD · 0 · (9 lines)
    7e80cbf6 docs(radar-display-fix-1008-sonnet): build report — c289f478
    7e80cbf6

     ...dar-display-fix-1008-sonnet-build-2026-10-11.md | 70 ++++++++++++++++++----
     1 file changed, 57 insertions(+), 13 deletions(-)
    a1e9eaed

     ...dar-display-fix-1008-sonnet-build-2026-10-11.md | 171 +++++++++++++++++++++
     1 file changed, 171 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-display-fix-1008-sonnet/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "…/radar-display-fix-1008-sonnet-build-2026-10-11.md" · 0 · SHADOW BUILT · job: radar-display-fix-1008-sonnet · tip: c289f478 | on 50b0cd87 | offline 4000/0 | with-DB 4884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | decisions: 4 · builder: claude-sonnet-5-5 · gate: radar-display-fix-1008-sonnet-gate · passes: 2 · suites at first run: green · builder tokens: 806014 · wall: 1.8
range · git log --oneline 50b0cd87..c289f478 · 0 · (2 lines)
    c289f478 feat(radar-display-fix-1008-sonnet): rows
    08f6fa82 wip(radar-display-fix-1008-sonnet): red
PREFLIGHT OK
```
`?? SHADOW-INSTRUCTIONS.md` at the worktree root: expected on a shadow card, recorded, not a finding.

THE RANGE, `git log --stat --format=%h 50b0cd87..c289f478` · exit 0:
```
c289f478

 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 src/cobalt/aset/radar_panel.py               | 19 ++++++++++++++-----
 2 files changed, 17 insertions(+), 5 deletions(-)
08f6fa82

 tests/cobalt/test_radar_panel.py       | 89 ++++++++++++++++++++++++++++++++--
 tests/cobalt/test_radar_panel_cards.py | 71 +++++++++++++++++++++++++++
 2 files changed, 157 insertions(+), 3 deletions(-)
```
Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`.

`ls <S>` → `No such file or directory` (fresh).

HOUSE PROBES, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: UP
```
No `HOUSE A: OpenAI` header line on the card: Sol not probed. `house A: Grok · house B: none (not needed)` — card `HOUSE B: as needed`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0:
```
14840 …/radar-display-fix-1008-sonnet-check/diff.md
16604 …/files/369-shadow-radar-display-fix-1008-sonnet-card.md
34820 …/files/radar-display-fix-1008-sonnet-build-2026-10-11.md
21798 …/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
84389 …/files/wt/src/cobalt/aset/radar_panel.py
66962 …/files/wt/tests/cobalt/test_radar_panel.py
57401 …/files/wt/tests/cobalt/test_radar_panel_cards.py
754 …/rulings.md
STAGED 8 files · 297568 bytes · commits 2
```
`stage-copy.sh`, one call each:
- `COPIED 106471 …/files/wt/src/cobalt/aset/web.py`
- `COPIED 75264 …/files/wt/src/cobalt/cards/store.py`
- `COPIED 14043 …/files/wt/src/cobalt/db.py`
- `COPIED 2208 …/files/radar-cards-survey-2026-10-08-r2.md`
- `COPIED 23148 …/files/radar-ladder-refresh-build-2026-10-06.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (18313 bytes): HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
House A Grok started 10:19 EDT (`date` 10:19:05), gates re-checked (R17, R19 one row each). `git status --short --branch` after return → `## shadow/radar-display-fix-1008-sonnet` + `?? SHADOW-INSTRUCTIONS.md` (shadow, expected).

## OWN FINDINGS
Written before either house list was opened.

FINDING O1
ROW: D
CLAIM: Row D puts the whole body, the stale line included, inside the `try` (`src/cobalt/aset/radar_panel.py:1610`, `:1613`), but `test_a_paused_ladder_says_so_within_three_intervals` (`tests/cobalt/test_radar_panel.py:1231`–`:1242`) only orders `try{` before the first guard, so a stale line moved above `try{` (where `layer` is out of scope and a throw escapes the `catch`) stays green.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o1_the_paused_ladder_test_fails_when_the_stale_line_leaves_the_try(monkeypatch):
    head, rest = panel.PANEL_JS.split(TICK_HEAD, 1)
    start = rest.index("if(Date.now()-ladderOkAt>3*interval)")
    end = rest.index("\n", start)
    stale = rest[start:end]
    moved = rest[:start] + rest[end + 1 :]
    moved = moved.replace("try{", stale + "\n   try{", 1)
    broken = head + TICK_HEAD + moved
    assert broken != panel.PANEL_JS
    assert broken.index("if(Date.now()-ladderOkAt>3*interval)") < broken.index("try{", broken.index(TICK_HEAD))
    monkeypatch.setattr(panel, "PANEL_JS", broken)
    with pytest.raises(AssertionError):
        test_a_paused_ladder_says_so_within_three_intervals()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O2
ROW: D (X3)
CLAIM: The banner must say `since <time>` (`src/cobalt/aset/radar_panel.py:1613`), but no test pins the time: `test_a_paused_ladder_says_so_within_three_intervals` (`tests/cobalt/test_radar_panel.py:1237`) checks only the words `LADDER NOT REFRESHED`.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o2_the_paused_ladder_test_fails_when_the_since_time_is_dropped(monkeypatch):
    broken = panel.PANEL_JS.replace("since '+new Date(ladderOkAt).toLocaleTimeString()+' · ", "", 1)
    assert broken != panel.PANEL_JS
    monkeypatch.setattr(panel, "PANEL_JS", broken)
    with pytest.raises(AssertionError):
        test_a_paused_ladder_says_so_within_three_intervals()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O3
ROW: B (X1)
CLAIM: The restore must run only when TERMINAL was open (`src/cobalt/aset/radar_panel.py:1631`, `if(termOpen){…}`), but `test_an_open_terminal_does_not_pause_the_tick` (`tests/cobalt/test_radar_panel.py:1190`) checks only that `t.open=true` sits after the swap, so an unconditional restore (TERMINAL forced open on every swap) stays green.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o3_the_open_terminal_test_fails_when_the_restore_is_unconditional(monkeypatch):
    broken = panel.PANEL_JS.replace("if(termOpen){const t=", "if(true){const t=", 1)
    assert broken != panel.PANEL_JS
    monkeypatch.setattr(panel, "PANEL_JS", broken)
    with pytest.raises(AssertionError):
        test_an_open_terminal_does_not_pause_the_tick()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O4
ROW: D (X3)
CLAIM: `ladderOkAt` is written only in `tickLadder` (`src/cobalt/aset/radar_panel.py:1606`, `:1613`, `:1632`); `refreshLadder`'s swap after a post (`:1553`) leaves it stale, so a guard held after a post can show `LADDER NOT REFRESHED · since <time>` with a time earlier than the last real refresh.
RUN: COMMAND — `grep -n -F "ladderOkAt" src/cobalt/aset/radar_panel.py`
EXPECT: three lines, `:1606`, `:1613`, `:1632`, none in `:1546`–`:1555`.

FINDING O5
ROW: C (X2)
CLAIM: The abort timer is armed for exactly one `interval` (`src/cobalt/aset/radar_panel.py:1618`) after the tick already fired, so a hung fetch is aborted just after the next `setInterval` tick (`:1643`); that tick still sees `ladderInFlight` true and returns, so the flag stays true past one interval and the retry comes two intervals after the hang.
RUN: COMMAND — `grep -n -F "timer=setTimeout(()=>ctl.abort(),interval);" src/cobalt/aset/radar_panel.py`
EXPECT: one line, `1618:` with the timeout equal to `interval` (no margin below it).

## Findings
House A Grok finished; the notice came at 10:35 EDT (`date` 10:35:33). Its stdout, whole: `I'll read the house instructions in full first, … I’ll write that result./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-sonnet-check/house-a.md` · `[exited with code 0]`. `<S>/house-a.md` (12 bytes), whole: `FINDINGS: 0`.
House B: none (not needed; card `HOUSE B: as needed`).
No house finding to keep.

## Dropped
none (house A wrote no `FINDING` block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::test_check_o1_the_paused_ladder_test_fails_when_the_stale_line_leaves_the_try` | `E       Failed: DID NOT RAISE <class 'AssertionError'>` · `tests/cobalt/test_radar_panel.py:1275: Failed` · `1 failed in 0.62s` | HELD: the stale line moved above `try{` keeps row D's test green |
| O2 | opus-own | `uv run pytest … ::test_check_o2_the_paused_ladder_test_fails_when_the_since_time_is_dropped` | `E       Failed: DID NOT RAISE <class 'AssertionError'>` · `tests/cobalt/test_radar_panel.py:1283: Failed` · `1 failed in 0.43s` | HELD: the banner with its `since <time>` removed keeps row D's test green |
| O3 | opus-own | `uv run pytest … ::test_check_o3_the_open_terminal_test_fails_when_the_restore_is_unconditional` | `E       Failed: DID NOT RAISE <class 'AssertionError'>` · `tests/cobalt/test_radar_panel.py:1291: Failed` · `1 failed in 0.43s` | HELD: `if(true){` in place of `if(termOpen){` keeps row B's test green |
| O4 | opus-own | `grep -n -F "ladderOkAt" src/cobalt/aset/radar_panel.py` | `1606: let ladderOkAt=Date.now();` · `1613:   if(Date.now()-ladderOkAt>3*interval){…}` · `1632:     ladderOkAt=Date.now();` (none in `refreshLadder`, `:1546`–`:1555`) | REJECTED — card `## NOT IN THIS JOB`: "`refreshLadder`" is fenced; row B: "`refreshLadder` … is unchanged"; row D sets `ladderOkAt` "after each successful swap (after `:1623`)" in `tickLadder` only |
| O5 | opus-own | `grep -n -F "timer=setTimeout(()=>ctl.abort(),interval);" src/cobalt/aset/radar_panel.py` | `1618:     timer=setTimeout(()=>ctl.abort(),interval);` | REJECTED — row C: "Arm it … `timer=setTimeout(()=>ctl.abort(),interval);`" (the card names one `interval` exactly) |

The HELD tests, committed before any fix: `d0709011 wip(radar-display-fix-1008-sonnet): check red — O1 O2 O3` (`tests/cobalt/test_radar_panel.py`, 31 insertions). No test form was repaired.

## FIXES
Shadow card: the check counts and holds findings and fixes none (CHECK-HUB `## THE FLOW`, shadow clause).
- O1: HELD, not fixed (shadow) — `tests/cobalt/test_radar_panel.py` (`test_a_paused_ladder_says_so_within_three_intervals` would also need the stale line's index after `try{`).
- O2: HELD, not fixed (shadow) — `tests/cobalt/test_radar_panel.py` (the same test would also need to pin `since '+new Date(ladderOkAt).toLocaleTimeString()+'`).
- O3: HELD, not fixed (shadow) — `tests/cobalt/test_radar_panel.py` (`test_an_open_terminal_does_not_pause_the_tick` would also need to pin `if(termOpen){` around `t.open=true`).

## Suites
RESTARTS, `uv run cobalt jobs restarts 50b0cd87..HEAD` · exit 1, whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-1008-sonnet-build-2026-10-11.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The one UNCLASSIFIED row is the untracked `SHADOW-INSTRUCTIONS.md`, which is expected on a shadow card and never committed; the build recorded it the same way (its DECISION F1). The committed range at the tip, `uv run cobalt jobs restarts 50b0cd87..c5795c7b` · exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-1008-sonnet-build-2026-10-11.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
The gate's first call (with `--deselect` of O1–O3) was stopped during its offline phase, before any lock take. `gate.sh` applies `--deselect` to pass 1 only: it appends the ids to pass 2 and leaves the offline run untouched (`gate.sh:13`, `:434`–`:435`), so the held red tests would have failed W by construction. The task output was empty at the stop. After the stop, `ls -la …/radar-display-fix-1008-sonnet/.env` → `No such file or directory` and `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`. The three held tests were then marked `@pytest.mark.xfail(strict=True, reason="check O<n> held, shadow: not fixed")`, committed `c5795c7b`. The assertions are unchanged; a fix that closes the weakness makes them XPASS, and strict fails the test. The rows' files: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `160 passed, 2 skipped, 3 xfailed in 2.60s`. Gate started again on `c5795c7b`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-display-fix-1008-sonnet all --deploy`.

W, exit 0 (notice at 11:22 EDT, `date` 11:22:05). Verdict lines, whole:
```
offline 4000/0
lock: waited 16 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-display-fix-1008-sonnet-all-20261012-103709.log
```
No skip is marked `OUTSIDE the allowed set`. `grep -n -F "4 xfailed" <log>` → `863:4000 passed, 787 skipped, 4 xfailed, 36 warnings in 660.77s (0:11:00)`: E0 had 1 xfail, plus the 3 held tests. `.env`: `ls …/radar-display-fix-1008-sonnet/.env` → `No such file or directory` (11:22 EDT). RESTARTS: `com.cobalt.aset com.cobalt.radar` (committed range; `..HEAD` adds only the untracked `SHADOW-INSTRUCTIONS.md`).

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (the DevDocs line), `src/cobalt/aset/radar_panel.py` (rows B, C, D: inside `PANEL_JS` only, per the diff hunk `@@ -1603,31 +1603,40 @@ PANEL_JS = r"""`), `tests/cobalt/test_radar_panel.py` (B, C, D), `tests/cobalt/test_radar_panel_cards.py` (A, E). My commits: `tests/cobalt/test_radar_panel.py` only. Every path is a row's file or the DevDocs line. X4: no `src/` change outside `PANEL_JS`; the pins `:397`–`:399` are not in the diff.

## Checked against the branch
- (i) `git log --oneline c289f478..HEAD -- . ":(exclude)docs"` → `c5795c7b wip(radar-display-fix-1008-sonnet): check held O1 O2 O3 marked xfail strict (shadow, no fix)` · `d0709011 wip(radar-display-fix-1008-sonnet): check red — O1 O2 O3`. `<tip now>` = `c5795c7b`.
- (ii) `git log --stat --format=%h c289f478..HEAD` → `c5795c7b` `tests/cobalt/test_radar_panel.py | 3 +++` · `d0709011` `tests/cobalt/test_radar_panel.py | 31 +++` · `7e80cbf6` / `a1e9eaed` the build report only. No WIDENED path.
- (iii) `git log --oneline 50b0cd87..HEAD -- src/cobalt/aset/web.py src/cobalt/cards/store.py src/cobalt/db_migrations configs` → empty.
- (iv) `grep -n -F "def test_check_o" tests/cobalt/test_radar_panel.py` → `1265:` O1 · `1281:` O2 · `1290:` O3, one line each. Their `wip … check red` commit `d0709011` is in (i). There is no `fix(` commit (shadow: no fix).
- (v) `ls /Users/cobalt/cobalt-wt/radar-display-fix-1008-sonnet/.env` → `No such file or directory`; `git status --short --branch` → `## shadow/radar-display-fix-1008-sonnet` and `?? SHADOW-INSTRUCTIONS.md` (shadow, expected).
- (vi) `git log --stat --format=%h 50b0cd87..HEAD -- src/cobalt/db_migrations tests/cobalt` → no migration file and no new with-DB test file (`08f6fa82`, `d0709011`, `c5795c7b`: the two offline test files). No gate-lists edit is owed.
- (vii) Card RECORDS: `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` → empty (as recorded). `grep -c -F "radar panel FAILED" /Users/cobalt/cobalt/logs/aset.log` → `0`; `grep -c -F "radar pool refresh FAILED" …` → `0` (the file as it is today, 2026-10-12, not the 10-08 read).
- (viii) L32: this report holds no ticker, price or date of his; the test values are constructed.
- `?? SHADOW-INSTRUCTIONS.md`: expected on a shadow card, recorded, not a finding.

## OPEN
- O4 · REJECTED — `refreshLadder`'s swap (`radar_panel.py:1553`) never writes `ladderOkAt`, so after a post a held guard can show `LADDER NOT REFRESHED · since <time>` with a time before the last real refresh. The card fences `refreshLadder`. Settled by: a card that lets `refreshLadder` (or `post`) set `ladderOkAt`, or a ruling that the banner may under-report. FOLLOW-UP.
- O5 · REJECTED — the abort timer equals `interval` (`:1618`) and is armed after the tick fired, so a hung fetch is aborted just after the next tick, which still returns on `ladderInFlight`. The retry comes two intervals after the hang (X2: the flag stays true slightly past one interval). The card names `interval` exactly. Settled by: a card that arms the abort below `interval`, or a ruling that two intervals are acceptable. FOLLOW-UP.
- O1, O2, O3 · HELD, not fixed (shadow). The fix is in `tests/cobalt/test_radar_panel.py` (a row's file): the original builder's one fix round, then remove the `xfail` markers.

## CONTINUE
next: none — checked; the desk verifies and commits this report

## DECISIONS
- O1 · HELD, not fixed (shadow) — `tests/cobalt/test_radar_panel.py`: `test_a_paused_ladder_says_so_within_three_intervals` does not pin the stale line inside `try{` (row D, "the whole body, guards included, sits inside the `try`"). Run: `…::test_check_o1_the_paused_ladder_test_fails_when_the_stale_line_leaves_the_try` → `DID NOT RAISE`. For the original builder's one fix round: add the stale line's index after `try{`, then remove the `xfail` marker.
- O2 · HELD, not fixed (shadow) — `tests/cobalt/test_radar_panel.py`: the same test does not pin `since '+new Date(ladderOkAt).toLocaleTimeString()+'` (row D, X3). Run: `…::test_check_o2_…` → `DID NOT RAISE`. Fix round: pin the time expression, then remove the marker.
- O3 · HELD, not fixed (shadow) — `tests/cobalt/test_radar_panel.py`: `test_an_open_terminal_does_not_pause_the_tick` does not pin `if(termOpen){` around `t.open=true` (row B, X1). Run: `…::test_check_o3_…` → `DID NOT RAISE`. Fix round: pin the condition, then remove the marker.
- ASK DESK: `gate.sh --deselect` reaches pass 1 only and the offline run never, so a shadow check that holds and fixes none cannot pass W with its red tests committed as written. Default taken: commit the red evidence (`d0709011`), then mark the three tests `xfail(strict=True)` without touching their assertions (`c5795c7b`). W ran once, green. The first gate call was stopped in its offline phase before any lock take. [11:22 EDT]

## RECORDS
- Dropped findings: none. House A Grok: `FINDINGS: 0`. House B: none (not needed).
- No house produced nothing. No `REFUSED, not needed` line. No `CONTINUED`.
- Lock: one take, by `gate.sh` at W (`lock: waited 16 min`), released (`.env: removed`). The stopped first gate call took no lock: `.cobalt_dev.lock` and `.env` were absent after the stop.
- L74: the attribution reminder's `Claude-Session:` line, recorded under `## L74`, not acted on.
- files opened: 16 — `CHECK-HUB.md`, the card, `cto-2026-09-24.md` (grep), the house-probe output, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, the build report, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), the Grok task output, `<S>/house-a.md`, `ops/desk/gate.sh` (grep `deselect`), the first gate output (empty), the gate output, the gate log (grep), `logs/aset.log` (grep -c).
- Check of `radar-display-fix-1008-sonnet`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- Shadow: per the shadow clause the check fixed none of the held findings; `ready: N/A (shadow, never deployed)`.

CHECK DONE · job: radar-display-fix-1008-sonnet · pass: 1 · tip: c5795c7b · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 3 (opus-own 3 · house 0) · fixed: 0 · held unfixed: 3 · open: 5 · house B: none (not needed) · suites: offline 4000/0 · with-DB 4884/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 16 · ready: N/A (shadow, never deployed) · decisions: 4 · for Dejan: 0 · tokens: 174891
