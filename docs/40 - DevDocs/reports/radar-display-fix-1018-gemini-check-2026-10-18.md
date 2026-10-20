# radar-display-fix-1018-gemini — check (shadow) 2026-10-18 card, run 2026-10-19

## §0 Headline
- Shadow check of Gemini's build `ffc36179`. House A Grok: `FINDINGS: 0`. House B: none (card `as needed`). My own read found 2.
- O1 HELD: the row-D test stays green when `ladderOkAt` is also reset in `finally`, so it doesn't pin the "only after a swap" clause. Left unfixed (shadow). O2 REJECTED: `refreshLadder` never resets the stale stamp, but `refreshLadder` is fenced. It stays OPEN.
- Rows B, C and D are built as written in `PANEL_JS` only. Controls A and E are green, and pins and markup are unchanged (X1–X4 read at the tip).
- W, by hand per row W (gate.sh refused: no `## OFFLINE OPS` at BASE): offline 4000/1 · with-DB 4883/2 · live-note 146/0 · tests/ops 1577/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. The reds are O1 (held) and the dev-DB harness red `test_db_credentials.py` (the build's DECISION 0). No build test is red.

## L74
- 2026-10-19 21:33 EDT: a system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded as DATA (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/718-shadow-radar-display-fix-1018-gemini-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/718-shadow-radar-display-fix-1018-gemini-card.md" · 0 · 57126aa9a00a15a44b2cebe0b661033f740b3576
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/718-shadow-radar-display-fix-1018-gemini-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · ... · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R685 row · ... · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): ... | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · ... · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-11 R1069 row · ... · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): ... | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · ... · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-17 R1738 row · ... · 0 · 96:| R1738 | 06:33 ET | HIS RULING (brain, L79), 2026-10-17: run the Gemini bake-off arm separately; ... | HIS RULING · APPROVED |
RULING 2026-10-17 R1738 committed · ... · 0 · b57cbf8e3ed386e736822c9ca864fef64a7433eb
RULING 2026-10-17 R1738 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
(long command and row text elided with `...` for width; full text in the session transcript.)
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 19 21:33:19 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/radar-display-fix-1018-gemini-4-argon-high
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h ffc36179..HEAD · 0 · (5 lines)
    8ba61b27 docs(radar-display-fix-1018-gemini): build report — ffc36179
    8ba61b27
    
     ...dar-display-fix-1018-gemini-build-2026-10-18.md | 207 +++++++++++++++++++++
     1 file changed, 207 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-display-fix-1018-gemini/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "...build-2026-10-18.md" · 0 · SHADOW BUILT · job: radar-display-fix-1018-gemini · tip: ffc36179 | on 50b0cd87 | offline 4000/0 | with-DB 887/1 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | decisions: 4 · builder: gemini-4-argon-high · gate: radar-display-fix-1018-gemini-gate · passes: 3 · suites at first run: red · builder tokens: UNKNOWN · wall: 19.6
range · git log --oneline 50b0cd87..ffc36179 · 0 · (3 lines)
    ffc36179 fix(radar-display-fix-1018-gemini): pass S2 1
    35e3c390 feat(radar-display-fix-1018-gemini): rows
    f150c432 wip(radar-display-fix-1018-gemini): red
PREFLIGHT OK
```
Fact for the houses: the build's stop line reads `with-DB 887/1` (one with-DB failure at the build's tip).
`?? SHADOW-INSTRUCTIONS.md`: expected on a shadow card, recorded, not a finding.
THE RANGE, `git log --stat --format=%h 50b0cd87..ffc36179`:
```
ffc36179
 tests/cobalt/test_radar_panel.py | 2 +-
35e3c390
 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 src/cobalt/aset/radar_panel.py               | 26 ++++++++++++++++++--------
 tests/cobalt/test_radar_panel.py             |  8 +++++---
f150c432
 tests/cobalt/test_radar_panel.py       | 93 ++++++++++++++++++++++++++++++++++
 tests/cobalt/test_radar_panel_cards.py | 70 ++++++++++++++++++++++++-
```
Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`.
`ls <S>` → No such file or directory (fresh).
House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: UP
```
house A: Grok · house B: none (not needed) — the card's `HOUSE B` line is `as needed`; no `HOUSE A:` header line.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, whole:
```
49 <S>/STAGED-CARD
17054 <S>/diff.md
18343 <S>/files/718-shadow-radar-display-fix-1018-gemini-card.md
40384 <S>/files/radar-display-fix-1018-gemini-build-2026-10-18.md
21979 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
84394 <S>/files/wt/src/cobalt/aset/radar_panel.py
67600 <S>/files/wt/tests/cobalt/test_radar_panel.py
57087 <S>/files/wt/tests/cobalt/test_radar_panel_cards.py
1116 <S>/rulings.md
STAGED 9 files · 308006 bytes · commits 3
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-display-fix-1018-gemini-check`; commits 3 = PREFLIGHT's range count.)
`stage-copy.sh`, one call each (`## READ` files named by symbol, and the reports `## ROWS` / `## READ` name):
- `COPIED 106471 <S>/files/wt/src/cobalt/aset/web.py`
- `COPIED 75264 <S>/files/wt/src/cobalt/cards/store.py`
- `COPIED 14043 <S>/files/wt/src/cobalt/db.py`
- `COPIED 2208 <S>/files/radar-cards-survey-2026-10-08-r2.md`
- `COPIED 23148 <S>/files/radar-ladder-refresh-build-2026-10-06.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim + the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS + Files paragraph).
House launch: `date` → Mon Oct 19 21:35:02 EDT 2026; both house gates re-run (R17 line 35, R19 line 37); `ls -la <S>` → diff.md, files/, HOUSE-INSTRUCTIONS.md, rulings.md, STAGED-CARD; `cd <AGY>`; Grok started (background, task `bxlipoqav`); `cd <WT>`; `git status --short --branch` → `## shadow/radar-display-fix-1018-gemini-4-argon-high` + `?? SHADOW-INSTRUCTIONS.md` (expected on a shadow card).

## OWN FINDINGS
FINDING O1
ROW: D
CLAIM: `test_a_paused_ladder_says_so_within_three_intervals` (`tests/cobalt/test_radar_panel.py:1321`ff) checks only that the FIRST `ladderOkAt=Date.now();` in the tick body comes after `now.replaceWith(next);`; a second write in `finally` (`src/cobalt/aset/radar_panel.py:1640`), which resets the stamp on every skipped tick so `LADDER NOT REFRESHED` never shows, keeps it green — the row's "set it to Date.now() after each successful swap" (only there) is not pinned.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o1_the_stale_test_fails_when_the_stamp_is_also_set_in_finally(monkeypatch):
    broken = panel.PANEL_JS.replace("}finally{clearTimeout(timer);", "}finally{ladderOkAt=Date.now(); clearTimeout(timer);", 1)
    assert broken != panel.PANEL_JS
    monkeypatch.setattr(panel, "PANEL_JS", broken)
    with pytest.raises(AssertionError):
        test_a_paused_ladder_says_so_within_three_intervals()
```
EXPECT: `Failed: DID NOT RAISE <class 'AssertionError'>`.

FINDING O2
ROW: D / X3
CLAIM: `refreshLadder` (`src/cobalt/aset/radar_panel.py:1546`–`:1555`), run after every saved post (`:1564`), swaps in a fresh ladder but never sets `ladderOkAt`, so a ladder refreshed by a post while the tick stays held (e.g. another tap strip open) still says `LADDER NOT REFRESHED · since <old time>` at `:1614`.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o2_a_post_refresh_also_resets_the_stale_stamp():
    assert "ladderOkAt=Date.now()" in _js_body("async function refreshLadder(){")
```
EXPECT: `AssertionError: assert 'ladderOkAt=Date.now()' in '\n   const keep=openIds();...'`.

## Findings
House A Grok: completion notice at `date` → Mon Oct 19 21:49:23 EDT 2026; `ls -la <S>` → `house-a.md` 12 bytes (written by Grok; its stdout ended with that path and `[exited with code 0]`). `<S>/house-a.md`, whole: `FINDINGS: 0`.
House B: none (not needed).
No house finding to keep.

## Dropped
none (house A wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::test_check_o1_the_stale_test_fails_when_the_stamp_is_also_set_in_finally` (run with O2 in one call) | `F` · `tests/cobalt/test_radar_panel.py:1367: Failed` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` | HELD — the D test stays green with `ladderOkAt=Date.now();` added to `finally`; not fixed (shadow card: the check fixes none) |
| O2 | opus-own | `…::test_check_o2_a_post_refresh_also_resets_the_stale_stamp` (same call) | `tests/cobalt/test_radar_panel.py:1372: AssertionError` · `E       assert 'ladderOkAt=Date.now()' in "\n   const keep=openIds();\n   const response=await fetch('/radar',…"` · summary `2 failed in 0.62s` | REJECTED — card `## NOT IN THIS JOB`: "`refreshLadder`"; row B: "`refreshLadder` … is unchanged" (pinned byte for byte by `REFRESH_LADDER_BODY`). Red for its stated reason; OPEN. Its test removed again with Edit (kept out of the suites because the fence forbids its fix) |
Held test committed: `git commit … -- tests/cobalt/test_radar_panel.py` → `[shadow/radar-display-fix-1018-gemini-4-argon-high 9cc84e59] wip(radar-display-fix-1018-gemini): check red — O1` · `1 file changed, 8 insertions(+)`.

## FIXES
- O1: HELD, NOT FIXED — `tests/cobalt/test_radar_panel.py` (shadow card: the check counts and holds and fixes none, CHECK-HUB `## THE FLOW`). The fix would be one assertion in `test_a_paused_ladder_says_so_within_three_intervals`: `body.count("ladderOkAt=")==1`.

## Suites
RESTARTS (BUILD-HUB `## RESTARTS`, before W): `uv run cobalt jobs restarts 50b0cd87..HEAD` → exit 1, whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-1018-gemini-build-2026-10-18.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The one UNCLASSIFIED row is the untracked, never-committed `SHADOW-INSTRUCTIONS.md` (expected on a shadow card; the build's ASK DESK 1). The committed paths derive `com.cobalt.aset com.cobalt.radar` = row F's expectation. Not classified (the file is never committed).

THE GATE CALL as `## 6` types it: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-display-fix-1018-gemini all --deploy --deploy-gate` → exit 1, whole:
```
no ## OFFLINE OPS
REFUSED: the lists file does not hold every command gate.sh runs: /Users/cobalt/cobalt-wt/radar-display-fix-1018-gemini/ops/desk/gate-lists.md
```
Row W applies (BASE's `gate-lists.md` has no `## OFFLINE OPS`): W run by hand with BASE's own lines (`git show 50b0cd87:ops/desk/gate-lists.md`, the same lines the build report quotes under `## W`). PASS 1 was run as the deploy's whole pass 1 (his R438, `--deploy`: the one ` --db-only` token removed, everything else byte-equal), the shape `gate.sh --deploy` would run. On `<tip now>` = `9cc84e59` (TIP `ffc36179` plus my held O1 test):
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (`.env` absent: `ls` → No such file) → exit 1, `1 failed, 4000 passed, 787 skipped, 1 xfailed, 36 warnings in 638.59s (0:10:38)`. The one red: `tests/cobalt/test_radar_panel.py:1367: Failed` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` = my held O1 (left red: shadow, fixes none). Build tests: 4000 passed = the build's 4000/0.
- tests/ops (deploy gate): BASE's lists hold no `## OFFLINE OPS` line; run once on its own, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0, `1577 passed, 1 xfailed, 15 warnings in 454.88s (0:07:34)`.
- (b) `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh radar-display-fix-1018-gemini 90` → exit 0, `lock taken: radar-display-fix-1018-gemini`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's (`2186 Oct 19 22:01`). `<FP>` → F0 `664	35	272c95bbb12241e3611e4b36326ccf87`. PROOF ONLY → `NOTHING WAS APPLIED`, `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, `TABLES 0011` = `## LEVEL 0013` → LEVEL 0013 (`code: 9cc84e59 (DIRTY: 1 path(s))`, the untracked SHADOW-INSTRUCTIONS.md).
- (c) PASS 1, whole (deploy): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect …` (BASE's PASS 1 with ` --db-only` removed, its 18 `--deselect`s byte-equal) → exit 1, `2 failed, 4694 passed, 7 skipped, 83 deselected, 3 xfailed, 43 warnings in 760.55s (0:12:40)`. Reds: (1) `tests/cobalt/test_db_credentials.py:211: AssertionError` · `E         At index 0 diff: 'cobalt_apply_system' != 'cobalt_backup'` · `E         Left contains 2 more items, first extra item: 'cobalt_system'` (the harness red of the build's DECISION 0; neither file in the diff); (2) `tests/cobalt/test_radar_panel.py:1367: Failed` (O1). SKIPPED, all 7 in `## ALLOWED SKIPS` or naming `COBALT_LIVE_VAULT_ROOT` / `COBALT_TEST_LIVE_DRC`: `test_cards_picks.py:388`, `test_cards_picks.py:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266`, `test_s3_c4_experiments.py:95`, `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` → `0001` … `0022` applied, `content UNCHANGED on every table`, no `CHANGED` → `dev forward: APPLIED 22:15:33` (`date`). F1 `893	44	126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2 (BASE's line) → exit 0, `189 passed, 1 deselected, 5 warnings in 222.42s (0:03:42)`.
- (c3r) STRAY ROWS: not read; no test of this build or of this check writes to cobalt_dev (every new test is offline).
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → `0022` … `0014` rolled back, `content UNCHANGED on every table`. F2 `664	35	272c95bbb12241e3611e4b36326ccf87` = F0 field for field → `cobalt_dev: 0013 — F2 = F0`. `release-devdb-lock.sh radar-display-fix-1018-gemini` → `lock released` (22:20:04); `ls …/.env` → `No such file or directory` → `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE (`.env` absent) → exit 0, `146 passed, 1 skipped, 15 warnings in 25.21s`; skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` → `live-note 146/0`.
- with-DB `<d>` = 4694 + 189 = 4883, failed 2 (O1 held; `test_db_credentials.py` harness).
SUITES: offline 4000/1 · with-DB 4883/2 · live-note 146/0. Every red is either my held O1 (left unfixed on a shadow card) or the dev-DB-level harness red of `test_db_credentials.py` (the build's DECISION 0). No build test is red.

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (DevDocs line, admitted), `src/cobalt/aset/radar_panel.py` (rows B, C, D), `tests/cobalt/test_radar_panel.py` (B, C, D), `tests/cobalt/test_radar_panel_cards.py` (A, E). My commits: `tests/cobalt/test_radar_panel.py` (a row's test file). X4: the one `src/` hunk is `@@ -1603,31 +1603,41 @@ PANEL_JS = r"""` (inside `PANEL_JS`, `tickLadder` and the `ladderOkAt` line beside `ladderInFlight`); no rendered-markup function changed; the three pins are green (inside the offline 4000).

## Checked against the branch
- (i) `git log --oneline ffc36179..HEAD -- . ":(exclude)docs"` → `9cc84e59 wip(radar-display-fix-1018-gemini): check red — O1`; `<tip now>` = `9cc84e59`.
- (ii) `git log --stat --format=%h ffc36179..HEAD` → `9cc84e59` `tests/cobalt/test_radar_panel.py | 8 ++++++++`; `8ba61b27` the build report (docs). No path outside a row's files.
- (iii) fence: `git log --oneline 50b0cd87..HEAD -- src/cobalt/aset/web.py src/cobalt/cards/store.py` → empty. The range stat (PREFLIGHT) holds no other `src/` file and no test file but the two allowed. `refreshLadder` is unchanged (`test_tick_refreshes_the_ladder_on_the_pool_timer_without_reload` pins it byte for byte; green).
- (iv) `grep -n -F "def test_check_o1_the_stale_test_fails_when_the_stamp_is_also_set_in_finally" tests/cobalt/test_radar_panel.py` → `1363:` one line; its `wip … check red — O1` commit is in (i); no `fix(` commit (shadow: none made).
- (v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## shadow/radar-display-fix-1018-gemini-4-argon-high` + `?? SHADOW-INSTRUCTIONS.md` (expected on a shadow card, recorded, not a finding).
- (vi) `git log --stat --format=%h 50b0cd87..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `test_radar_panel.py` and `test_radar_panel_cards.py` (offline tests); no migration, no with-DB test → no gate-lists change needed.
- (vii) card RECORDS commands: `grep -c -F "radar panel FAILED" /Users/cobalt/cobalt/logs/aset.log` → `0`; `grep -c -F "radar pool refresh FAILED" …/aset.log` → `0` (record: 0 matches — holds); `wc -l …/aset.log` → `29443` (the record's `15527` was read 2026-10-08; the log has grown since, so the record's line numbers can't be checked against today's count); `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` → nothing (holds today).
- (viii) L32: this report holds no ticker, price or trade date of his; the dates are the card's constructed test values and run clocks.

## OPEN
- O1 — HELD, NOT FIXED (shadow: the check fixes none). Settled by one assertion in `test_a_paused_ladder_says_so_within_three_intervals` pinning a single `ladderOkAt=` write (e.g. `assert body.count("ladderOkAt=")==1`), then `test_check_o1_…` passes.
- O2 — REJECTED (fence: `refreshLadder`). A follow-up card could have `refreshLadder` (or `post`) reset `ladderOkAt`. Until then a post-driven refresh while the tick stays held still shows `LADDER NOT REFRESHED`.

## CONTINUE
next: none — CLOSE done; the desk verifies, commits the report and the `.result` file

## DECISIONS
- O1 HELD, NOT FIXED — `tests/cobalt/test_radar_panel.py`: `test_a_paused_ladder_says_so_within_three_intervals` checks only the first `ladderOkAt=Date.now();` after the swap. With a second write added in `finally`, which would silence `LADDER NOT REFRESHED` for good, it stays green (`test_check_o1_…` → `Failed: DID NOT RAISE`, `:1367`, commit `9cc84e59`). Shadow card: the check fixes none. It goes to the builder's ONE fix round (his R438). Safe default: the red test is left committed as the held finding's proof.
- DECISION 0 (W PASS 1, harness): `tests/cobalt/test_db_credentials.py:211` is red at 0013 (`'cobalt_apply_system' != 'cobalt_backup'`, 2 extra roles). It is the same red as the build's DECISION 0; neither file is in this diff. Not a finding of this build (L70: it goes under DECISIONS as UNPROVEN, per the card's fence). The desk decides how the harness red counts.
- ASK DESK 1 [Mon Oct 19 21:52 EDT 2026]: RESTARTS on `50b0cd87..HEAD` exits 1 on the untracked `SHADOW-INSTRUCTIONS.md` (UNCLASSIFIED). Safe default: not classified (never committed). The committed paths derive `com.cobalt.aset com.cobalt.radar`, and the stop line carries those.
- ASK DESK 2 [Mon Oct 19 21:53 EDT 2026]: `gate.sh … all --deploy --deploy-gate` refuses on this BASE (`no ## OFFLINE OPS`). Safe default: row W by hand with BASE's lines, PASS 1 as the deploy's whole pass (` --db-only` removed, as `--deploy` does), and tests/ops run on its own. The gate has no `log:` path; this report holds the outputs.

## RECORDS
- Dropped findings: none. House that produced nothing: none (Grok produced `FINDINGS: 0` with its closing line).
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (one take, W, 22:01 → 22:20:04).
- L74: one system reminder asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on.
- `.result` file written beside this report (`radar-display-fix-1018-gemini-check-2026-10-18.result`). This seat has no listed string to commit in `/Users/cobalt/cobalt`, so the desk commits it with the report.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh a40faa10` → `context 202600 of 400000 — ok`.
- files opened: 11 — CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); `<S>/diff.md`; the build report; `src/cobalt/aset/radar_panel.py`; `tests/cobalt/test_radar_panel.py`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `ops/desk/gate.sh` (header and parser, to read its refusal); `git show 50b0cd87:ops/desk/gate-lists.md`; `<S>/house-a.md` (after `## OWN FINDINGS`). Tool output files of background runs are not counted.
- Check of `radar-display-fix-1018-gemini`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-display-fix-1018-gemini · pass: 1 · tip: 9cc84e59 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 (opus-own 1 · house 0) · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 4000/1 · with-DB 4883/2 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 11 · ready: N/A (shadow, never deployed) · decisions: 4 · for Dejan: 0 · tokens: 202600
