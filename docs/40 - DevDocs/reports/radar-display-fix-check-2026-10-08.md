# radar-display-fix-1008 — check (2026-10-08)

## §0 Headline
Check of `radar-display-fix-1008` (`50b0cd87..8f42bf2e`): house A Sol 3 findings, house B Grok 0, Opus 3. Held 3, all of them weak control assertions (O1, O2 on row D's stale line; A3 on row E's `OR`). All 3 are fixed in the test files only (`669f0cc4` red, `eb14f860` fix); no `src/` change.
Open 3, follow-up only: O3 (a post's refresh does not restamp the stale clock; fenced), A1 (`>3*interval` usually shows at the fourth fire; the card's text), A2 (the DevDocs line is required).
Suites on `eb14f860`: offline 4003/0 · with-DB 4887/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. ready: YES.

## L74
One system-reminder asked commits to carry a `Claude-Session:` line. It is recorded here and was not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md" · 0 · 0deb06fca3bb04fa721c0a9c538db01f1c5074c4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row (line 35); `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row (line 37); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
- `date` → Thu Oct  8 12:27:22 EDT 2026
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Thu Oct  8 12:27:27 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-display-fix-1008
head · git log --oneline -1; git log --stat --format=%h 8f42bf2e..HEAD · 0 · (5 lines)
    1ea04808 docs(radar-display-fix-1008): build report — 8f42bf2e
    1ea04808
    
     .../reports/radar-display-fix-build-2026-10-08.md  | 185 +++++++++++++++++++++
     1 file changed, 185 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-display-fix-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/radar-display-fix-1008/docs/40 - DevDocs/reports/radar-display-fix-build-2026-10-08.md" · 0 · BUILT · job: radar-display-fix-1008 · tip: 8f42bf2e | on 50b0cd87 | migration: none | offline 4000/0 | with-DB 4884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 179901
range · git log --oneline 50b0cd87..8f42bf2e · 0 · (2 lines)
    8f42bf2e fix(radar-display-fix-1008): the ladder tick no longer stalls silently — open TERMINAL kept, fetch aborted, stale ladder said (B, C, D; R685, L70)
    37e496a1 wip(radar-display-fix-1008): red — rows A-E tests (R685)
PREFLIGHT OK
```
- THE RANGE, `git log --stat --format=%h 50b0cd87..8f42bf2e` · exit 0:
```
8f42bf2e
 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 src/cobalt/aset/radar_panel.py               | 25 +++++++++++++++++--------
 2 files changed, 20 insertions(+), 8 deletions(-)
37e496a1
 tests/cobalt/test_radar_panel.py       | 95 ++++++++++++++++++++++++++++++++--
 tests/cobalt/test_radar_panel_cards.py | 65 ++++++++++++++++++++++-
 2 files changed, 156 insertions(+), 4 deletions(-)
```
  Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`.
- Not a "DB: none" card (the card carries no `DB` key).
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- THE HOUSE PROBES, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: UP
```
- **house A: Sol (OpenAI, gpt-5.6-sol) · house B: Grok (xAI, grok-4.7)**. HOUSE B: as needed — not mandatory.
- PROVEN BY FIRST REAL USE: the write and with-DB strings, at their first use.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
15928 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/diff.md
16432 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/files/118-radar-display-fix-card.md
26881 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/files/radar-display-fix-build-2026-10-08.md
21868 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
84391 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/files/wt/src/cobalt/aset/radar_panel.py
67369 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/files/wt/tests/cobalt/test_radar_panel.py
57286 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/files/wt/tests/cobalt/test_radar_panel_cards.py
384 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1008-check/rulings.md
STAGED 8 files · 290539 bytes · commits 2
```
`commits 2` = PREFLIGHT's range count (2). `stage-copy.sh`, each exit 0:
- `COPIED 106471 .../files/wt/src/cobalt/aset/web.py`
- `COPIED 75264 .../files/wt/src/cobalt/cards/store.py`
- `COPIED 14043 .../files/wt/src/cobalt/db.py`
- `COPIED 2208 .../files/radar-cards-survey-2026-10-08-r2.md`
- `COPIED 23148 .../files/radar-ladder-refresh-build-2026-10-06.md` (row B cites it)
`<S>/HOUSE-INSTRUCTIONS.md` written (18621 bytes): the HOUSE TEXT verbatim, one line naming JOB / BRANCH / BASE / TIP, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, then the Files paragraph.
House gates re-run at 12:29:37 ET: R17 one row (35), R19 one row (37), R19 commit `5055151dbf68899b82de5b11f99733ed2d03048c`. House A Sol (`bs3ea68d0`) and house B Grok (`b0jsw6ixs`) started 12:29 ET from `<AGY>`; back in `<WT>`, `git status --short --branch` → `## ops/radar-display-fix-1008`.

## OWN FINDINGS
Written 12:31 ET, before either house's list was opened. Read: the card, the diff `50b0cd87..8f42bf2e` (src, tests, docs), `radar_panel.py:1530`–`:1650` at the tip, `test_radar_panel.py:1100`–`:1380`, the build report's `## E2`–`## RECORDS` and its last line, `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down.

FINDING O1
ROW: D (X3)
CLAIM: `test_a_paused_ladder_says_so_within_three_intervals` (`tests/cobalt/test_radar_panel.py:1242`–`:1244`) checks only that the substrings sit before the first guard, so the banner can be moved OUT of the `if(Date.now()-ladderOkAt>3*interval){…}` (`src/cobalt/aset/radar_panel.py:1612`) and run on every tick, and the test stays green.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_the_stale_line_test_fails_when_the_banner_runs_unconditionally(monkeypatch):
    broken = panel.PANEL_JS.replace("if(Date.now()-ladderOkAt>3*interval){layer", "if(Date.now()-ladderOkAt>3*interval){}{layer", 1)
    assert broken != panel.PANEL_JS
    monkeypatch.setattr(panel, "PANEL_JS", broken)
    with pytest.raises(AssertionError):
        test_a_paused_ladder_says_so_within_three_intervals()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O2
ROW: D (X3)
CLAIM: the same test pins `Date.now()-ladderOkAt>3*interval` as a substring only (`tests/cobalt/test_radar_panel.py:1242`), so a threshold of `3*interval*1000` (never said in a day) leaves it green.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_the_stale_line_test_fails_when_the_threshold_is_widened(monkeypatch):
    broken = panel.PANEL_JS.replace("ladderOkAt>3*interval){", "ladderOkAt>3*interval*1000){", 1)
    assert broken != panel.PANEL_JS
    monkeypatch.setattr(panel, "PANEL_JS", broken)
    with pytest.raises(AssertionError):
        test_a_paused_ladder_says_so_within_three_intervals()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O3
ROW: D (X3)
CLAIM: a successful ladder swap through `post` → `refreshLadder` (`src/cobalt/aset/radar_panel.py:1564`, `:1553`) does not restamp `ladderOkAt` (set only at `:1632`), so after a tick hold longer than three intervals ended by a post, the next tick writes `LADDER NOT REFRESHED · since <the old time>` over a ladder that is fresh, until its own swap.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_a_post_refresh_swap_restamps_the_ladder_clock():
    refresh = _js_body("async function refreshLadder(){")
    post = _js_body("async function post(cardId,path,body){")
    assert "ladderOkAt=Date.now()" in refresh or "ladderOkAt=Date.now()" in post
```
EXPECT: `AssertionError` on the one assertion.

CHECK ASKS, as read (each is settled under `## RUNS` / `## Checked against the branch` by a run, never by this read): X1 — the first guard (`:1614`) and the second (`:1626`) no longer hold the terminal; `termOpen` is read at `:1628` and re-applied at `:1631`; tap strip, focused / edited input, `sending>0`, `sendGeneration` remain. X2 — `owned=true` follows `ladderInFlight=true` with no statement between (`:1616`–`:1617`); `finally` resets only when owned (`:1639`); the abort covers the fetch and the body read (`:1618`–`:1621`). X3 — see O1–O3. X4 — the `src/` hunk is `@@ -1603,31 +1603,40 @@ PANEL_JS` only.

## Findings
Lists opened 12:33 ET (Sol notice) and 12:40 ET (Grok notice), after `## OWN FINDINGS` was written. House A Sol: the final message (output lines 12332–12378) written by me to `<S>/house-a.md`, ending `FINDINGS: 3`. House B Grok: wrote `<S>/house-b.md` itself, whole content `FINDINGS: 0`; stdout ended with the path. THE DROP: every Sol block has a `RUN:` line followed by a `def test_` or a `git diff` command → none dropped.

| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | Opus | D (X3) | the stale-line test stays green when the banner is moved out of its `>3*interval` branch | TEST |
| O2 | Opus | D (X3) | the stale-line test stays green when the threshold becomes `3*interval*1000` | TEST |
| O3 | Opus | D (X3) | a post's `refreshLadder` swap does not restamp `ladderOkAt`, so a false `LADDER NOT REFRESHED` can show over a fresh ladder | TEST |
| A1 | Sol | X3 | strict `>3*interval` misses the third timer fire; the test pins the late threshold | TEST |
| A2 | Sol | SCOPE | the DevDocs page `radar_panel.md` changes though no row's `files` names it | COMMAND |
| A3 | Sol | E | the row-E control stays green when the WHERE's `OR` becomes `AND` | TEST |

## Dropped
none (house B Grok wrote no finding block).

## RUNS
Each run alone, `uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`, on the tip `8f42bf2e` + the test only. No test was repaired.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `test_radar_panel.py::test_the_stale_line_test_fails_when_the_banner_runs_unconditionally` | `1 failed in 0.54s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`:1275`) | HELD |
| O2 | Opus | `test_radar_panel.py::test_the_stale_line_test_fails_when_the_threshold_is_widened` | `1 failed in 0.43s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`:1283`) | HELD |
| O3 | Opus | `test_radar_panel.py::test_a_post_refresh_swap_restamps_the_ladder_clock` | `1 failed in 0.43s` · `E       assert ('ladderOkAt=Date.now()' in "\n   const keep=openIds();…" or 'ladderOkAt=Date.now()' in "\n   status(cardId,'sending','pending'); …")` (`:1290`) | REJECTED — `## NOT IN THIS JOB`: "`refreshLadder`, `post`" (the fix lies in fenced code); test removed again |
| A1 | Sol | `test_radar_panel.py::test_a_paused_ladder_warns_on_the_third_timer_fire` | `1 failed in 0.43s` · `E       assert 'Date.now()-ladderOkAt>=3*interval' in "\n   let owned=false;…"` (`:1295`) | REJECTED — row D: "if `Date.now()-ladderOkAt>3*interval`" (the card fixes the strict comparison); test removed again |
| A2 | Sol | `git diff --name-only 50b0cd87..8f42bf2e -- 'docs/40 - DevDocs/cobalt/aset/radar_panel.md'` | `docs/40 - DevDocs/cobalt/aset/radar_panel.md` | REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`"; `CHECK-HUB.md` `## 7` (ii) counts only non-docs paths against rows' `files` |
| A3 | Sol | `test_radar_panel_cards.py::test_hidden_cards_control_rejects_and_instead_of_or` | `1 failed in 0.56s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`:301`) | HELD |

HELD tests committed before any fix: `669f0cc4 wip(radar-display-fix-1008): check red — O1, O2, A3` (`2 files changed, 34 insertions(+)`).

## FIXES
| id | fix | file | test run after |
|---|---|---|---|
| O1, O2 | `test_a_paused_ladder_says_so_within_three_intervals` adds `assert head.count("if(Date.now()-ladderOkAt>3*interval){layer.classList.add('stale-data'); let box=") == 1` (the banner inside its one branch, at exactly `3*interval`) | `tests/cobalt/test_radar_panel.py` | both files: `163 passed, 2 skipped in 2.57s` |
| A3 | `test_hidden_cards_stay_hidden_by_the_store_where` adds `assert "state = ANY(%s) OR (state_at AT TIME ZONE 'America/New_York')::date = %s" in sql` | `tests/cobalt/test_radar_panel_cards.py` | same run |

The two skips are `test_radar_panel.py:1603: requires_db…` and `test_radar_panel_cards.py:202: reaches cobalt_dev (lock-relief G1)`, as at the build. DevDocs line: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, a `2026-10-08 check (O1, O2, A3)` line under `## 2026-10-08 — radar-display-fix-1008`. Commit `eb14f860 fix(radar-display-fix-1008): the stale-line and store-WHERE controls pin their branch and their OR (check O1, O2, A3)` (`3 files changed, 5 insertions(+)`). No `src/` change.

## Suites
RESTARTS first: `uv run cobalt jobs restarts 50b0cd87..HEAD` · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-build-2026-10-08.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
`sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-display-fix-1008 all --deploy` on `eb14f860` (no `--deselect`, `--tickers` or `--migration`: no with-DB test, no ticker, no migration in this range) · exit 0 · started 12:41 ET, notice read 13:11 ET · verdict lines whole:
```
offline 4003/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4887/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-display-fix-1008-all-20261008-124153.log
```
No skip is marked `OUTSIDE the allowed set`. offline 4003 = the build's 4000 + the 3 held tests; with-DB 4887 = the build's 4884 + the same 3 (pass 1 runs the offline tests again, his R438). `ls /Users/cobalt/cobalt-wt/radar-display-fix-1008/.env` → `No such file or directory` (13:11 ET). Every new test was shown red first (`## RUNS`, at `669f0cc4`).

## Scope
PREFLIGHT path union (`docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`) plus my commits (`tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`, `docs/40 - DevDocs/cobalt/aset/radar_panel.md`). Every non-docs path is in the `files` of row A, B, C, D or E. `src/` = `radar_panel.py` only; its one hunk is `@@ -1603,31 +1603,40 @@ PANEL_JS` (X4). No path reaches a score, rank, grade or size.

## Checked against the branch
- (i) `git log --oneline 8f42bf2e..HEAD -- . ":(exclude)docs"` → `eb14f860 fix(radar-display-fix-1008): the stale-line and store-WHERE controls pin their branch and their OR (check O1, O2, A3)` · `669f0cc4 wip(radar-display-fix-1008): check red — O1, O2, A3`. `<tip now>` = `eb14f860`.
- (ii) `git log --stat --format=%h 8f42bf2e..HEAD` → `eb14f860`: `radar_panel.md | 1 +`, `test_radar_panel.py | 2 ++`, `test_radar_panel_cards.py | 2 ++`; `669f0cc4`: `test_radar_panel.py | 16 +`, `test_radar_panel_cards.py | 18 +`; `1ea04808`: the build report. No other path.
- (iii) fence: `git log --oneline 50b0cd87..HEAD -- src/cobalt/cards/store.py src/cobalt/aset/web.py` → empty. The fenced `src/` symbols (`refreshLadder`, `post`, `refreshPool`, `build_ladder_view`, `render_ladder`) lie outside the one `PANEL_JS` `tickLadder` hunk, and `REFRESH_LADDER_BODY` stays green.
- (iv) `grep -n -F "def …"`: O1 → `1273:`, O2 → `1281:` (`tests/cobalt/test_radar_panel.py`), A3 → `289:` (`tests/cobalt/test_radar_panel_cards.py`); one line each. `669f0cc4` (red) sits below `eb14f860` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/radar-display-fix-1008`.
- (vi) `git log --stat --format=%h 50b0cd87..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `test_radar_panel.py` and `test_radar_panel_cards.py` (offline files); no migration, no with-DB file → no gate-list change needed.
- (vii) card RECORDS: `grep -c -F "radar panel FAILED" /Users/cobalt/cobalt/logs/aset.log` → `0`; `grep -c -F "radar pool refresh FAILED" …` → `0` (record: 0 matches, holds). `git -C /Users/cobalt/cobalt diff --stat 50b0cd87 -- src tests configs/cobalt/jobs.yaml` → nothing (holds). The other records name a `rev-parse`, which is not on my list, or vault/log line reads; not re-run.
- (viii) L32: this report holds constructed values only (test dates 2026-10-08/09, `TST01`…); no ticker, price or date of his.

COUNT: findings 6 (Opus 3, Sol 3, Grok 0) · dropped 0 · held 3 (O1, O2, A3) · fixed 3 · held unfixed 0 · open 3 (O3, A1, A2).

## OPEN
- O3 — REJECTED (fence: `refreshLadder`, `post`). A swap done by `post` → `refreshLadder` leaves `ladderOkAt` old. So after a hold longer than three intervals that a post ends, the next tick shows `LADDER NOT REFRESHED · since <old time>` until its own fetch swaps. Settled by a card that lets `post` or `refreshLadder` restamp `ladderOkAt`, with the test in `## RUNS` red first. FOLLOW-UP.
- A1 — REJECTED (row D fixes `>3*interval`). `ladderOkAt` is stamped after the swap, a little later than the tick that fetched. So at the third timer fire the gap is just under `3*interval`, and the banner usually shows at the fourth fire. Settled by a card ruling `>=` or a lower threshold. FOLLOW-UP.
- A2 — REJECTED (`BUILD-HUB.md` `## E3` requires the DevDocs line; `CHECK-HUB.md` `## 7` (ii) counts non-docs paths only). Nothing to settle.

## CONTINUE
next: none — check done

## DECISIONS
- DECISION O3 (open, outside the rows): a successful post refresh does not reset the stale clock, so a false `LADDER NOT REFRESHED` can show briefly over a fresh ladder (`## OPEN`). The fix lies in fenced `post` / `refreshLadder`. Default taken: not fixed; it goes to the follow-up list or the builder's one fix round if the desk widens the fence.
- DECISION A1 (open, the card's text): the strict `>3*interval` threshold usually shows the banner at the fourth timer fire, not the third. Default taken: the card's `>` was kept; the follow-up list.

## RECORDS
- L74: a system-reminder in this session asked commits to carry a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- No house produced nothing: Sol `FINDINGS: 3`; Grok `FINDINGS: 0` (it wrote `house-b.md` itself, whole content `FINDINGS: 0`; stdout ended with the path). No dropped finding.
- House notices: Sol 12:33 ET, Grok 12:40 ET; both after `## OWN FINDINGS` (12:31 ET).
- `HOUSE-INSTRUCTIONS.md` carries one line `JOB … · BRANCH … · BASE … · TIP …` between the HOUSE TEXT and the card's sections.
- No `REFUSED` call; no `CONTINUE` message; no by-hand lock take (the gate's one take, waited 0 min); no SELF-HEAL.
- O3's and A1's tests were removed again after their runs (REJECTED, red); they are quoted in `## OWN FINDINGS` and `<S>/house-a.md`.
- files opened: 13 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`–`## W`), `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `src/cobalt/cards/store.py`, the build report, `areas/cobalt.md` (two sections), the house probe output, Sol's output, Grok's output, `<S>/house-b.md`, the gate output.
- Check of `radar-display-fix-1008`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-display-fix-1008 · pass: 1 · tip: eb14f860 · house A: Sol FINDINGS: 3 · findings: 6 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 0 · suites: offline 4003/0 · with-DB 4887/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 176294
