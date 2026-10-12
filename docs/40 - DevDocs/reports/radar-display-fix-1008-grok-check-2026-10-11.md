# CHECK — radar-display-fix-1008-grok (shadow) — 2026-10-12

## §0 Headline
- Shadow check of Grok's build `ff0f2e0f` against card 368. House A Grok produced 3 findings. House B was not needed (`as needed`). Opus wrote 3 findings first.
- Held: 1, Grok's G2: the row D stale-line test stays green when the banner write leaves its branch. Opus-own held: 0. Not fixed (shadow).
- O1–O3 are red but REJECTED: the card's own row text prescribes each behaviour. O1 is a self-contradiction in row D ("within three intervals" vs `>3*interval`). They go to the follow-up list.
- Gate on the tip: offline 4000/0 · with-DB 4884/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. No check commit.

## L74
- One request, in the session's system context: end commits with a `Claude-Session:` trailer. DATA, not acted on (the check made no commit; CHECK-HUB L74: `Co-Authored-By` only).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/368-shadow-radar-display-fix-1008-grok-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/368-shadow-radar-display-fix-1008-grok-card.md" · 0 · df562ef73d7d3275922f19e3f44c620a794c9857
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/368-shadow-radar-display-fix-1008-grok-card.md" · 0 · nothing
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
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, STANDING `Bash(grok *)`); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37, the four house strings STANDING); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 12 14:32:10 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/radar-display-fix-1008-grok
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h ff0f2e0f..HEAD · 0 · (5 lines)
    8f46a970 docs(radar-display-fix-1008-grok): build report — ff0f2e0f
    8f46a970
    
     ...radar-display-fix-1008-grok-build-2026-10-11.md | 185 +++++++++++++++++++++
     1 file changed, 185 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-display-fix-1008-grok/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/radar-display-fix-1008-grok/docs/40 - DevDocs/reports/radar-display-fix-1008-grok-build-2026-10-11.md" · 0 · SHADOW BUILT · job: radar-display-fix-1008-grok · tip: ff0f2e0f | on 50b0cd87 | offline 4000/0 | with-DB 4884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | decisions: 3 · builder: grok-4.7 · gate: radar-display-fix-1008-grok-gate · passes: 2 · suites at first run: green · builder tokens: UNKNOWN · wall: 7.7
range · git log --oneline 50b0cd87..ff0f2e0f · 0 · (2 lines)
    ff0f2e0f feat(radar-display-fix-1008-grok): rows
    d71ec3d5 wip(radar-display-fix-1008-grok): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md` at the worktree root: expected on a shadow card, recorded, not a finding.
- THE RANGE, typed: `git log --stat --format=%h 50b0cd87..ff0f2e0f` · exit 0:
```
ff0f2e0f

 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 src/cobalt/aset/radar_panel.py               | 24 ++++++++++++++++--------
 2 files changed, 19 insertions(+), 8 deletions(-)
d71ec3d5

 tests/cobalt/test_radar_panel.py       | 97 ++++++++++++++++++++++++++++++++--
 tests/cobalt/test_radar_panel_cards.py | 67 ++++++++++++++++++++++-
 2 files changed, 160 insertions(+), 4 deletions(-)
```
  Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`.
- Card has no `DB: none` key: the DB-none path check does not apply.
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · `grok: UP` / `gemini: UP`. No `HOUSE A: OpenAI` header line → Sol not probed.
- Seats: `house A: Grok · house B: none (not needed)` — card `HOUSE B: as needed`.
- No `HOUSE A: none` overrule on the card.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
16172 …/radar-display-fix-1008-grok-check/diff.md
16592 …/radar-display-fix-1008-grok-check/files/368-shadow-radar-display-fix-1008-grok-card.md
24038 …/radar-display-fix-1008-grok-check/files/radar-display-fix-1008-grok-build-2026-10-11.md
21141 …/radar-display-fix-1008-grok-check/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
84388 …/radar-display-fix-1008-grok-check/files/wt/src/cobalt/aset/radar_panel.py
67576 …/radar-display-fix-1008-grok-check/files/wt/tests/cobalt/test_radar_panel.py
57446 …/radar-display-fix-1008-grok-check/files/wt/tests/cobalt/test_radar_panel_cards.py
754 …/radar-display-fix-1008-grok-check/rulings.md
STAGED 8 files · 288107 bytes · commits 2
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920`.) Commits 2 = PREFLIGHT's range count.
`stage-copy.sh`, one call each, for the files `## READ` / `## ROWS` name that the script cannot derive:
- `COPIED 106471 …/files/wt/src/cobalt/aset/web.py`
- `COPIED 75264 …/files/wt/src/cobalt/cards/store.py`
- `COPIED 14043 …/files/wt/src/cobalt/db.py`
- `COPIED 2208 …/files/radar-cards-survey-2026-10-08-r2.md`
- `COPIED 23148 …/files/radar-ladder-refresh-build-2026-10-06.md`
`<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the `Files:` paragraph.
House A Grok started 14:34 ET (`date` 14:34:05 before the launch), from `<AGY>`; `cd <WT>` then `git status --short --branch` → `## shadow/radar-display-fix-1008-grok` / `?? SHADOW-INSTRUCTIONS.md`.

## OWN FINDINGS
Written by 14:36 ET (`date`), before the house list was opened.

FINDING O1
ROW: D (X3)
CLAIM: The stale line fires on `Date.now()-ladderOkAt>3*interval` (`src/cobalt/aset/radar_panel.py:1612`), but ticks land on whole intervals from load (`:1642`) and `ladderOkAt` is stamped after the fetch returns (`:1631`, a latency δ>0 after its tick), so after a good swap the banner first shows at the FOURTH tick (4I−δ > 3I; at 3I−δ it is still < 3I), not "within three intervals" as row D says.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o1_a_paused_ladder_is_said_by_the_third_tick_after_a_swap():
    import re
    body = _js_body(TICK_HEAD)
    found = re.search(r"Date\.now\(\)-ladderOkAt>(\d+)\*interval", body)
    assert found, "no stale threshold in the tick"
    n = int(found.group(1))
    interval, latency = 1000, 50  # constructed: a swap stamped 50 ms after its tick
    first = next(k for k in range(1, 20) if k * interval - latency > n * interval)
    assert first <= 3, f"the banner first shows at tick {first} after a swap"
```
EXPECT: `AssertionError: the banner first shows at tick 4 after a swap`.

FINDING O2
ROW: C (X2)
CLAIM: The abort timer is armed for exactly one interval after the tick fires (`src/cobalt/aset/radar_panel.py:1617`), so a hung fetch is aborted just AFTER the next `setInterval` tick (`:1642`); that tick still sees `ladderInFlight` true and returns (`:1613`): the flag outlives one interval by the arming delay and a hung fetch always costs the next tick.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o2_a_hung_fetch_is_aborted_before_the_next_tick():
    body = _js_body(TICK_HEAD)
    armed = body[body.index("timer=setTimeout(()=>ctl.abort(),") :]
    delay = armed[len("timer=setTimeout(()=>ctl.abort(),") : armed.index(")")]
    assert delay.strip() != "interval", "the abort lands after the next tick, which skips"
```
EXPECT: `AssertionError: the abort lands after the next tick, which skips`.

FINDING O3
ROW: D (X3)
CLAIM: `ladderOkAt` is stamped only in `tickLadder` (`src/cobalt/aset/radar_panel.py:1631`); `refreshLadder` (`:1546`–`:1555`, run after every post, `:1564`) swaps in a fresh ladder without stamping it, so after a tap-strip pause longer than three intervals ended by a tap, the next tick paints `LADDER NOT REFRESHED · since <old time>` over the ladder that was just refreshed (until its own fetch swaps).
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_check_o3_a_post_refresh_also_stamps_the_ladder_fresh():
    source = panel.PANEL_JS
    stamped = _js_body("async function refreshLadder(){") + _js_body("async function post(cardId,path,body){")
    assert "ladderOkAt=Date.now()" in stamped, "a post's refresh leaves ladderOkAt at the old time"
```
EXPECT: `AssertionError: a post's refresh leaves ladderOkAt at the old time`.

Read and found no finding (each by reading the file, nothing run yet): row A (`card_id` is the view row's real key, `test_radar_panel_cards.py:87`; ET day via `store.days`), row B (`:1625`–`:1630`, X1: the four work-in-progress guards stay in both checks), row C's scope (`:1608` before `try{`), row D ownership (`:1616`, `:1638`; a guard throw lands in `catch` with `owned` false), row E (SQL text and params), X4 (the diff is only inside `PANEL_JS`, `:1606`–`:1638`).

## Findings
House A Grok: `<S>/house-a.md` (written by Grok, 2512 bytes, 14:50), last line `FINDINGS: 3`. Notice at 14:51 ET (`date`); `ls -la <S>` showed `house-a.md`. Grok's stdout: its progress lines and the path. House B: none (not needed).
| id | house | row | claim | run |
|---|---|---|---|---|
| G1 | Grok | C | the hung-fetch test stays green when the abort delay becomes `interval*3` (prefix match) | TEST |
| G2 | Grok | D | the stale-line test stays green when the banner write is moved outside the `>3*interval` branch | TEST |
| G3 | Grok | SCOPE | the tip changes `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, a file no row lists | COMMAND |

## Dropped
none: `grep -n -F "RUN:"` over `house-a.md` → lines 4, 21, 40; each is followed by a `def test_` function or a `git diff` command line.

## RUNS
Each test was pasted into `tests/cobalt/test_radar_panel.py` with the Edit tool and run alone with `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::<test>`.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `::test_check_o1_a_paused_ladder_is_said_by_the_third_tick_after_a_swap` | `1 failed in 0.62s` · `E       AssertionError: the banner first shows at tick 4 after a swap` | REJECTED — row D: "if `Date.now()-ladderOkAt>3*interval`" (the card prescribes the strict 3-interval threshold, and the build's own test pins it, `test_radar_panel.py:1243`). Red for the stated reason: the same row says "it shows on screen within three intervals", and the threshold shows it at the 4th tick after a swap. The card contradicts itself. OPEN |
| O2 | opus-own | `::test_check_o2_a_hung_fetch_is_aborted_before_the_next_tick` | first run `1 passed in 0.35s`: a FORM error, since the slice ended at the first `)`, the one in `()=>`. Repaired once, slicing after the prefix, assertion unchanged → `1 failed in 0.47s` · `E       AssertionError: the abort lands after the next tick, which skips` | REJECTED — row C: "`timer=setTimeout(()=>ctl.abort(),interval);`". OPEN |
| O3 | opus-own | `::test_check_o3_a_post_refresh_also_stamps_the_ladder_fresh` | `1 failed in 0.39s` · `E       AssertionError: a post's refresh leaves ladderOkAt at the old time` | REJECTED — row D: "set it to `Date.now()` after each successful swap (after `:1623`)", the tick's own swap; `## NOT IN THIS JOB`: "`refreshLadder`, `post`". OPEN |
| G1 | Grok | `::test_a_three_interval_abort_leaves_the_hung_test_green` | `1 passed in 0.34s` (the mutation DID raise) | NOT HELD — test removed |
| G2 | Grok | `::test_banner_text_outside_the_branch_leaves_the_paused_test_green` | `1 failed in 0.39s` · `E       Failed: DID NOT RAISE <class 'AssertionError'>` | HELD, NOT FIXED — `tests/cobalt/test_radar_panel.py` (a rows' file; shadow card: the check fixes none) |
| G3 | Grok | `git diff --stat 50b0cd87 ff0f2e0f -- "docs/40 - DevDocs/cobalt/aset/radar_panel.md"` | ` docs/40 - DevDocs/cobalt/aset/radar_panel.md \| 3 +++` / ` 1 file changed, 3 insertions(+)` | REJECTED — `BUILD-HUB.md` E3: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`" (and CHECK-HUB `## 7` (ii) exempts `docs/` paths). OPEN |
After the runs, all six tests were removed again with the Edit tool. `git status --short --branch` → `## shadow/radar-display-fix-1008-grok` / `?? SHADOW-INSTRUCTIONS.md`: the tree is the build's tip. No `wip(<JOB>): check red` commit was made (DECISION 2).

## FIXES
- G2: HELD, NOT FIXED — `tests/cobalt/test_radar_panel.py` (shadow card: the check counts and fixes none). The held test is Grok's FINDING 2 in `<S>/house-a.md`, quoted verbatim there.
No commit of the check's.

## Suites
RESTARTS, before the gate: `uv run cobalt jobs restarts 50b0cd87..HEAD` · exit 1 · whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-1008-grok-build-2026-10-11.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The committed paths give `com.cobalt.aset com.cobalt.radar` (row F's expected value). The other four labels come only from the untracked `SHADOW-INSTRUCTIONS.md` (DECISION 3).

THE GATE: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-display-fix-1008-grok all --deploy` (no `--deselect`/`--tickers`/`--migration`: every new test is offline, no migration) · started 14:52 · exit 0 · verdict lines whole:
```
offline 4000/0
lock: waited 18 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-display-fix-1008-grok-all-20261012-145243.log
```
- `grep -n -F "OUTSIDE the allowed set" <log>` → nothing (exit 1).
- `grep -n -F "code: " <log>` → `927:` / `1158:` / `1858:` / `1912:` `code: 8f46a970 (DIRTY: 1 path(s))`. `8f46a970` is the docs-only build-report commit above `TIP` `ff0f2e0f`, and the 1 dirty path is the untracked `SHADOW-INSTRUCTIONS.md`.
- Pass 1 command, `<log>:935`: `$ COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect …` (the gate-lists PASS 1 line; the full command is in the log).
- `ls <WT>/.env` after the gate (15:38) → `No such file or directory`.

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py` (plus the build report, docs). Each non-docs path is in a row's `files`. The check made no commit. `git diff --stat 50b0cd87 ff0f2e0f -- src` → `src/cobalt/aset/radar_panel.py | 24 …` only, and the hunk (`diff.md`) sits wholly inside `PANEL_JS` (`:1606`–`:1638`): X4, no rendered markup changes, and the pins are green in the offline suite. No path reaches a score, rank, grade or size: the change is page script only.

## Checked against the branch
(i) `git log --oneline ff0f2e0f..HEAD -- . ":(exclude)docs"` → empty. No check commit, so `<tip now>` = `ff0f2e0f`.
(ii) `git log --stat --format=%h ff0f2e0f..HEAD` → `8f46a970`, the build report only (docs).
(iii) fence: `git log --oneline 50b0cd87..HEAD -- src/cobalt/aset/web.py src/cobalt/cards/store.py src/cobalt/db.py src/cobalt/db_migrations configs` → empty.
(iv) held finding G2: not fixed and not committed (shadow; DECISION 2). There is no `def` to grep on the branch, and the test text is in `<S>/house-a.md` FINDING 2.
(v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## shadow/radar-display-fix-1008-grok` and `?? SHADOW-INSTRUCTIONS.md` (expected on a shadow card, recorded, not a finding).
(vi) `git log --stat --format=%h 50b0cd87..HEAD -- src/cobalt/db_migrations tests/cobalt` → `d71ec3d5` (the two test files) only. No migration and no with-DB test above `0013`, so no gate-lists line is owed.
(vii) RECORDS: `wc -l /Users/cobalt/cobalt/logs/aset.log` → `22148` (the log has grown since the 10-08 read of 15527 lines, so the line numbers are not re-checkable today). `grep -c -F "radar panel FAILED" /Users/cobalt/cobalt/logs/aset.log` → `0`. `grep -n -F "imports: [cobalt.cli]" <WT>/configs/cobalt/jobs.yaml` → `194:    imports: [cobalt.cli]` (matches `jobs.yaml:194`).
(viii) L32: the report holds no ticker, price or date of his. The test values quoted are the constructed values from the card and the tests.
A and E controls (builder DECISION 3, no mutation run): read only. Row A's `store.days == [date(2026,10,8)]` with `now` 10-09 01:30Z goes red if the day turns UTC, and row E's tuple equality goes red if `EXPIRED` joins `RADAR_OPEN_STATES`. Neither was run as a mutation here.

## OPEN
- O1 REJECTED (row D threshold `>3*interval` vs the same row's "within three intervals"). It settles if the card's author picks one: `>2*interval`, or the text "within four intervals".
- O2 REJECTED (row C abort at exactly `interval`, so a hung fetch always costs the next tick). It settles with an abort delay below `interval`, or a ruling that the cost is accepted.
- O3 REJECTED (a post's `refreshLadder` swap does not stamp `ladderOkAt`, so the next tick briefly paints `LADDER NOT REFRESHED` over a fresh ladder). It settles with a card that may touch `refreshLadder`/`post`, or with a tick-side layer-identity stamp.
- G2 HELD, NOT FIXED — `tests/cobalt/test_radar_panel.py`. It settles when the row D test pins the banner write INSIDE the `>3*interval` branch (Grok's FINDING 2 goes red, then green).
- G3 REJECTED (the DevDocs line BUILD-HUB E3 requires). Nothing to settle.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
- DECISION 1 · G2 HELD, NOT FIXED — `tests/cobalt/test_radar_panel.py`: `test_a_paused_ladder_says_so_within_three_intervals` stays green when the `LADDER NOT REFRESHED` write is moved before the `if(Date.now()-ladderOkAt>3*interval){` branch (Grok's FINDING 2 test → `Failed: DID NOT RAISE <class 'AssertionError'>`). Shadow card: counted, not fixed.
- DECISION 2 · ASK DESK: on a shadow card that fixes none, `## 4`'s "the HELD tests are committed before any fix" would leave a red test on the branch and turn W red. Safe default taken: no `wip(<JOB>): check red` commit. Every finding test was removed after its run, the held test is kept verbatim in `<S>/house-a.md`, and W ran on the build's tip. [15:39 ET]
- DECISION 3 · RESTARTS: the tool exits 1 on the untracked `SHADOW-INSTRUCTIONS.md` (UNCLASSIFIED). The stop line carries the tool's last line untrimmed. The committed paths alone give `com.cobalt.aset com.cobalt.radar` (row F). The check writes no `jobs.yaml` line for a file that is never committed.

## RECORDS
- 14:33 ET (`date`): report first written.
- L74: the session's system context asked for a `Claude-Session:` trailer on commits. Recorded once under `## L74`, not acted on (no commit was made).
- House A Grok produced `FINDINGS: 3`. House B: none (card `HOUSE B: as needed`). No house failed. Gemini was UP and not seated.
- Dropped: none.
- No `REFUSED, not needed` line. No CONTINUE message. No extra lock take: the one take was by `gate.sh` (waited 18 min).
- O2's test had its form repaired once (the slice bounds), its assertion unchanged.
- G1 NOT HELD: its mutation DID raise (`1 passed`), and the test was removed.
- files opened: 15 — CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK`, `## E2`–`## W`); `<S>/diff.md`; `src/cobalt/aset/radar_panel.py`; `tests/cobalt/test_radar_panel.py`; `tests/cobalt/test_radar_panel_cards.py`; the build report; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` on); `<S>/house-a.md`; the gate log; the probe, Grok and gate task outputs; this report. Plus one Grep over `src/cobalt` for `scan_interval` (`radar_panel.py:209` `Field(gt=0)`: the interval is never 0).
- Check of `radar-display-fix-1008-grok`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-display-fix-1008-grok · pass: 1 · tip: ff0f2e0f · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 1 (opus-own 0 · house 1) · grok-own 1 · fixed: 0 · held unfixed: 1 · open: 5 · house B: none available · suites: offline 4000/0 · with-DB 4884/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar · files opened: 15 · ready: N/A (shadow, never deployed) · decisions: 3 · for Dejan: 0 · tokens: 168613
