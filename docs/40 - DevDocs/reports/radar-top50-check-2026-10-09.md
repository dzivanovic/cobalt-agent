# radar-top50-1009 — CHECK REPORT (2026-10-09)

## §0 Headline
Nine findings: three of mine, two from Sol, four from Grok. One held: A2 (Sol), where test A stayed green when the Over cap table was moved inside a `<details>`. It is fixed in the test only (`109bcfc0`). `radar_panel.py` is unchanged from the build.
Three findings are REJECTED and stay open: A1 and B2 (the DevDocs line, which `BUILD-HUB.md` E3 requires) and B1 (the `:587` excluded-field edit, a direct result of row A). Five were NOT HELD.
Deploy gate on `109bcfc0` (clean): offline 4039/0 · with-DB 4926/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. RESTARTS `com.cobalt.aset com.cobalt.radar`.
ready: YES. One DECISION (B1, ASK DESK), none for Dejan.

## L74
One `<system-reminder>` arrived at 12:44 ET asking that commits end with a `Claude-Session:` line. It is recorded here as data. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 0 · 975b3c8730d59de463714422f1c14cbf2a32b706
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row (`Bash(grok *)` standing). `grep -n "^| R19 "` → line 37, one row (four house strings standing). `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Fri Oct  9 12:44:49 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-top50-1009
head · git log --oneline -1; git log --stat --format=%h 1ad357a3..HEAD · 0 · (5 lines)
    d91b4640 docs(radar-top50-1009): build report — 1ad357a3
    d91b4640
    
     .../reports/radar-top50-build-2026-10-09.md        | 146 ++++++++++++++++++---
     1 file changed, 131 insertions(+), 15 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/radar-top50-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/radar-top50-1009/docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md" · 0 · BUILT · job: radar-top50-1009 · tip: 1ad357a3 | on 0e84db6f | migration: none | offline 4038/0 | with-DB 4925/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 1 · tokens: 128352
range · git log --oneline 0e84db6f..1ad357a3 · 0 · (4 lines)
    1ad357a3 fix(radar-top50-1009): top-50 list holds at most cap names; the rest render as Over cap (A, B; L1, L28, L70)
    d2f85749 wip(radar-top50-1009): red — over-cap pool test (A) and full-pool control (B)
    aac3a4c2 wip(radar-top50-1009): AUTHORIZATION — resumed, AUTHORIZED on R685
    e73aa9c9 wip(radar-top50-1009): AUTHORIZATION — R716 row rejected by authorize.sh
PREFLIGHT OK
```
THE RANGE typed, `git log --stat --format=%h 0e84db6f..1ad357a3` · exit 0: `1ad357a3` → `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (+3), `src/cobalt/aset/radar_panel.py` (+10 −1), `tests/cobalt/test_radar_panel.py` (+1 −1); `d2f85749` → `tests/cobalt/test_radar_panel.py` (+44); `aac3a4c2` and `e73aa9c9` → the build report only. Path union: `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md`.
`ls <S>` · exit 1 · `No such file or directory` → fresh.
House probe, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: UP
```
house A: Sol (OpenAI) · house B: Grok (xAI). Card `HOUSE B: as needed`; both up.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0:
```
6848 <S>/diff.md
6890 <S>/files/154-radar-top50-card.md
25212 <S>/files/radar-top50-build-2026-10-09.md
23020 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
3996 <S>/files/wt/docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md
84823 <S>/files/wt/src/cobalt/aset/radar_panel.py
70162 <S>/files/wt/tests/cobalt/test_radar_panel.py
384 <S>/rulings.md
STAGED 8 files · 221335 bytes · commits 2
```
`commits 2` = the two non-docs commits of PREFLIGHT's range (`d2f85749`, `1ad357a3`); the other two (`aac3a4c2`, `e73aa9c9`) touch only the build report, which the diff's `:(exclude)docs` leaves out. `grep -c "^commit " <S>/diff.md` → `2`.
`stage-copy.sh` (files `## READ` names by symbol): `COPIED 24574 <S>/files/wt/src/cobalt/radar/store.py`, `COPIED 20664 <S>/files/wt/src/cobalt/radar/pool.py`.
`<S>/HOUSE-INSTRUCTIONS.md` written: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` (the card has none), `## RECORDS`, the Files paragraph.
Started 12:45:59 ET (`date`), gates R17/R19 re-grepped (one row each): house A Sol (`b66rgaoy2`), house B Grok (`b1jnh64eu`). Return: `git status --short --branch` → `## ops/radar-top50-1009`.

## OWN FINDINGS
Written before either house's list was opened.

FINDING O1
ROW: A
CLAIM: the over-cap section is pinned only through `render_pool`; the two callers that ship it, `render_radar_page` (`src/cobalt/aset/radar_panel.py:1657`–`:1665`) and `pool_api_payload` (`:1673`–`:1674`), are not read with over-cap rows by any test (build DECISIONS 2), and the API JSON must hold 50 `current` rows and no `over_cap` key while its `html` carries `T51` under the heading.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_o1_over_cap_reaches_the_page_and_the_api_html_but_not_the_json():
    pool_row, rows = _open_admitted_copies(51, members=51)
    view, _ = _build(pool_row=pool_row, members=rows)
    heading = 'Over cap — open admitted beyond cap <span class="count">1</span>'

    page = panel.render_radar_page(view)
    assert heading in page
    assert page.index('<tr data-episode-id="10051"') > page.index(heading)

    payload = panel.pool_api_payload(view.pool)
    assert heading in payload["html"]
    assert payload["html"].index('<tr data-episode-id="10051"') > payload["html"].index(heading)
    assert "over_cap" not in payload["pool"]
    assert len(payload["pool"]["current"]) == 50
    assert "T51" not in [row["ticker"] for row in payload["pool"]["current"]]
    assert payload["pool"]["members"] == 51
```
EXPECT: if the callers drop or misplace the section, a failing `assert heading in page` / `in payload["html"]` or the index order; green otherwise.

FINDING O2
ROW: A
CLAIM: the row says the over-cap table is "never inside a `<details>`" and sits on the line after `Current admitted` (`src/cobalt/aset/radar_panel.py:1083`); test A (`tests/cobalt/test_radar_panel.py:859`–`:874`) asserts neither, so a move into the `Departed` `<details>` would stay green.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_o2_over_cap_table_sits_after_current_and_outside_every_details():
    pool_row, rows = _open_admitted_copies(51, members=51)
    view, _ = _build(pool_row=pool_row, members=rows)
    rendered = panel.render_pool(view.pool)
    current = rendered.index('Current admitted <span class="count">50</span>')
    over = rendered.index("Over cap — open admitted beyond cap")
    first_details = rendered.index("<details>")
    assert current < over < first_details
    assert rendered[current:over].count("</table>") == 1
    assert "<details>" not in rendered[current:over]
```
EXPECT: green on the tip if the code is right; red (`current < over < first_details`) if the table sits in or after a `<details>`.

FINDING O3
ROW: A
CLAIM: the split at `src/cobalt/aset/radar_panel.py:647` is pinned only on the snapshot path (`since=None`); the refresh path (`snapshot=False`, `since` set), which the page's JS uses through `pool_api_payload` (`:1607`), is not tested with an over-cap pool.
RUN: TEST — `tests/cobalt/test_radar_panel.py`
```python
def test_o3_refresh_path_also_splits_the_over_cap_rows():
    pool_row, rows = _open_admitted_copies(51, members=51)
    view, _ = _build(
        since=NOW - timedelta(minutes=5), snapshot=False, pool_row=pool_row, members=rows
    )
    assert len(view.pool.current) == 50
    assert [row.ticker for row in view.pool.over_cap] == ["T51"]
    assert 'Over cap — open admitted beyond cap <span class="count">1</span>' in panel.render_pool(view.pool)
```
EXPECT: green on the tip if the refresh path splits as the snapshot does; `assert 51 == 50` if not.

## Findings
House A (Sol) completed at 12:50:21 ET (`date`); its final message, ending `FINDINGS: 2`, written by me to `<S>/house-a.md`. House B (Grok) completed at 12:58:07 ET; it wrote `<S>/house-b.md` itself, ending `FINDINGS: 4`, and replied with that path. Every block of both lists carries a `RUN:` line followed by a test function or one command with an allowed beginning: none dropped.

| id | house | row | claim | run |
|---|---|---|---|---|
| A1 | Sol | SCOPE | the build adds a dated entry to `docs/40 - DevDocs/cobalt/aset/radar_panel.md:218`, a file no row lists | COMMAND |
| A2 | Sol | A | test A stays green when the over-cap table is moved inside the first `<details>`; the placement is not pinned | TEST |
| B1 | Grok | SCOPE | the edit at `test_radar_panel.py:587` (adding `"over_cap"` to the excluded set) fixes a red outside the rows, which the fence says is never fixed here | COMMAND |
| B2 | Grok | SCOPE | the DevDocs entry at `radar_panel.md:218` is outside row A's files | COMMAND |
| B3 | Grok | C | the report blob at `1ad357a3` says the rows and RESTARTS were not run, so it does not quote row C's line | COMMAND |
| B4 | Grok | SCOPE | the report's skip `test_radar_panel.py:1647` names a blank line; `requires_db` is at `:1641` | COMMAND |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::test_o1_over_cap_reaches_the_page_and_the_api_html_but_not_the_json` | `1 passed in 0.46s` | NOT HELD — the page and the API `html` carry the section; JSON has 50 `current` rows and no `over_cap`. Test removed. |
| O2 | own | `… ::test_o2_over_cap_table_sits_after_current_and_outside_every_details` | `1 passed in 0.36s` | NOT HELD — the code places it right; the weak-test half of the claim is A2's, which holds. Test removed. |
| O3 | own | `… ::test_o3_refresh_path_also_splits_the_over_cap_rows` | `1 passed in 0.35s` | NOT HELD — the refresh path splits the same. Test removed. |
| A1 | Sol | `git diff --name-only 0e84db6f..1ad357a3 -- 'docs/40 - DevDocs/cobalt/aset/radar_panel.md'` | `docs/40 - DevDocs/cobalt/aset/radar_panel.md` | REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`". The output is as claimed; the hub requires the line. OPEN. |
| A2 | Sol | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py::test_a_over_cap_test_rejects_moving_the_section_inside_details` | `1 failed in 0.40s`; first failing line `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`tests/cobalt/test_radar_panel.py:943`) | HELD — test A stays green with the table inside `<details>`, for the stated reason. |
| B1 | Grok | `git diff 0e84db6f..1ad357a3 -- tests/cobalt/test_radar_panel.py` | shows `+        "bars_stale_tickers", "handicap_state", "handicap_detail", "over_cap"}` | REJECTED — row A: "Add `over_cap: … Field(default_factory=list, exclude=True)` … It is excluded, so the API JSON and the healthy pins do not change", in row A's file `tests/cobalt/test_radar_panel.py`. The edit is the direct result of row A; the payload is unchanged. The build's DECISIONS 1 already asks it. OPEN. |
| B2 | Grok | `git diff --stat 0e84db6f..1ad357a3 -- "docs/40 - DevDocs/cobalt/aset/radar_panel.md"` | `docs/40 - DevDocs/cobalt/aset/radar_panel.md \| 3 +++` / `1 file changed, 3 insertions(+)` | REJECTED — as A1 (`BUILD-HUB.md` `## E3` requires the line). OPEN. |
| B3 | Grok | `git show 1ad357a3:"docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md"` | the blob at `1ad357a3` holds `Not run. Rows built: 0 of 3.` and `## RESTARTS` / `Not run.` | NOT HELD — red for another reason: the report at `1ad357a3` is the authorization-stop text; the build report was committed at `d91b4640` (docs-only, above `TIP`, allowed by PREFLIGHT), and that report quotes `RESTARTS: com.cobalt.aset com.cobalt.radar` under `## RESTARTS`. My own run of row C at 12:59 ET prints the same line (`## Suites`). |
| B4 | Grok | `grep -n requires_db tests/cobalt/test_radar_panel.py` | (run with my four finding tests in the file, +58 lines) `1699:requires_db = pytest.mark.skipif(`, `1701: reason=…`, `1706:@requires_db` → at the tip `:1641` and `:1648` | NOT HELD — the report quotes pytest's own skip line. With the file at +22 lines, pytest printed `SKIPPED [1] tests/cobalt/test_radar_panel.py:1669: requires_db …`, i.e. the `@requires_db` line minus one, the same offset as `:1647` against `:1648` at the tip. The report copies the tool's output. |

A2's test was put in `tests/cobalt/test_radar_panel.py` unchanged (no form repair). O1–O3 were removed with Edit; `git diff --stat` → `tests/cobalt/test_radar_panel.py | 18 ++++++++++++++++++` (A2 only). Committed `6eb13b04 wip(radar-top50-1009): check red — A2`.

## FIXES
| id | fix | file | test run | commit |
|---|---|---|---|---|
| A2 | test A now asserts `current_at < rendered.index(heading) < rendered.index("<details>")` and `"<details>" not in rendered[current_at : rendered.index(heading)]` (the row: "on the line after `Current admitted` … never inside a `<details>`"); `radar_panel.py` unchanged | `tests/cobalt/test_radar_panel.py`; DevDocs line in `docs/40 - DevDocs/cobalt/aset/radar_panel.md` | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `166 passed, 2 skipped in 2.36s` (skips: `test_radar_panel.py:1669: requires_db: radar read-layer integration needs cobalt_dev`, `test_radar_panel_cards.py:202: reaches cobalt_dev (lock-relief G1)`) | `109bcfc0 fix(radar-top50-1009): test A pins the Over cap table after Current admitted and outside every details (check A2)` |

## Suites
RESTARTS, `uv run cobalt jobs restarts 0e84db6f..HEAD` (12:59 ET, HEAD `109bcfc0`), exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
Nothing UNCLASSIFIED. It matches the card's row C and `## RECORDS`.
W, `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-top50-1009 all --deploy` (started 12:59, done 13:27:56 ET), exit 0. No `--deselect`, `--tickers` or `--migration`: no with-DB test and no migration are in this branch. Verdict lines, whole:
```
offline 4039/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4926/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-top50-1009-all-20261009-125927.log
```
Log facts, each from `grep -n -F`:
- `code: 109bcfc0 (clean)` (`:931`, `:1163`, `:1957`, `:2011`).
- `4039 passed, 790 skipped, 1 xfailed` (`:867`). That is the build's 4038 plus A2's one test.
- Pass 1: `4731 passed, 7 skipped, 89 deselected, 3 xfailed` (`:1092`). Pass 2: `195 passed, 1 deselected` (`:1898`). 4731 + 195 = 4926.
- Live-note: `146 passed, 1 skipped` (`:2086`).
- `OUTSIDE` → nothing.
`.env`: `ls /Users/cobalt/cobalt-wt/radar-top50-1009/.env` → `No such file or directory` (13:27 ET). `git status --short --branch` → `## ops/radar-top50-1009`.

## Scope
PREFLIGHT path union: `src/cobalt/aset/radar_panel.py` and `tests/cobalt/test_radar_panel.py` (row A's files), plus `docs/40 - DevDocs/cobalt/aset/radar_panel.md` and the build report (docs). My commits add `tests/cobalt/test_radar_panel.py` (rows A and B's test file) and the DevDocs page. Nothing lies outside the rows' files.

## Checked against the branch
- (i) `git log --oneline 1ad357a3..HEAD -- . ":(exclude)docs"` → `109bcfc0 fix(radar-top50-1009): test A pins the Over cap table after Current admitted and outside every details (check A2)`, `6eb13b04 wip(radar-top50-1009): check red — A2`. `<tip now>` = `109bcfc0`.
- (ii) `git log --stat --format=%h 1ad357a3..HEAD`:
  - `109bcfc0` → `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `tests/cobalt/test_radar_panel.py`
  - `6eb13b04` → `tests/cobalt/test_radar_panel.py`
  - `d91b4640` → the build report
  The only non-docs path is a test file.
- (iii) Fence. `git log --oneline 0e84db6f..HEAD -- src/cobalt/radar/pool.py src/cobalt/radar/store.py src/cobalt/radar/runner.py src/cobalt/aset/web.py` → empty. `git log --oneline 0e84db6f..HEAD -- src tests` → only `109bcfc0`, `6eb13b04`, `1ad357a3`, `d2f85749`. Its `--stat` form over `src/cobalt/db_migrations tests/cobalt` shows only `tests/cobalt/test_radar_panel.py`. With the PREFLIGHT range, no `src/` file but `radar_panel.py` and no test file but `test_radar_panel.py` is touched.
- (iv) `grep -n -F "def test_a_over_cap_test_rejects_moving_the_section_inside_details" tests/cobalt/test_radar_panel.py` → `893:` (one line). `6eb13b04` (red) sits below `109bcfc0` (fix) in (i).
- (v) `ls <WT>/.env` → No such file. `git status --short --branch` → `## ops/radar-top50-1009`.
- (vi) Gate lists: no migration file and no with-DB test file in `0e84db6f..HEAD` (the `--stat` above). Nothing to carry.
- (vii) No card `## RECORDS` line names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command (they name `rev-parse` and `diff --stat`). Nothing to run.
- (viii) L32: the report holds constructed values only (`T1`…`T51`, ids `10001`…`10051`). No ticker, price or date of his.

## OPEN
- A1 (Sol) / B2 (Grok) · REJECTED — `BUILD-HUB.md` `## E3` requires one dated line per changed module under `docs/40 - DevDocs/cobalt/`. Would settle it: the desk confirms that the hub's DevDocs rule covers a file the card's rows do not list.
- B1 (Grok) · REJECTED — row A makes `over_cap` an excluded field in its own test file, and the `:587` set lists excluded fields. Would settle it: the desk's answer to DECISIONS 1 (the builder's DECISIONS 1 asks the same).

## CONTINUE
next: done

## DECISIONS
1. ASK DESK — B1: the build added `"over_cap"` to the excluded-field set in `test_bars_stale_leaves_the_api_json_unchanged` (`tests/cobalt/test_radar_panel.py:587`). Grok reads that as fixing a red outside the rows, which the card's fence (`## NOT IN THIS JOB`, last line) forbids. I read it as row A's own consequence in row A's own test file, because row A orders the field `exclude=True`. Without the edit the offline suite has 1 failed. Default taken: kept as built, and listed under `## OPEN`.

## RECORDS
- Dropped findings: none.
- Every house produced a list: Sol `FINDINGS: 2`, Grok `FINDINGS: 4`.
- Grok's stdout was only the path, and it wrote `house-b.md` itself. Sol's final message was copied by me to `house-a.md`.
- Grok's B4 ran while my O1–O3 and A2 tests were still in the file (+58 lines). Its line numbers are mapped back to the tip under `## RUNS`.
- One lock take, the gate's own (`lock: waited 0 min`). No extra take.
- No `REFUSED, not needed` line and no `CONTINUED` line.
- The L74 line is under `## L74`.
- Not read: `areas/cobalt.md` (WHAT YOU READ (5)), `src/cobalt/radar/store.py` and `src/cobalt/radar/pool.py`. The last two were staged for the houses by `stage-copy.sh`, and the card fences both.
- files opened: 14 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, the build report, `<S>/rulings.md`, `<S>/diff.md` (head), `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (tail), the house-probe output, Sol's output, Grok's output, `<S>/house-b.md`, the gate output.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 9f800028` → `context 153816 of 400000 — ok` (13:28 ET).
- Check of `radar-top50-1009`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-top50-1009 · pass: 1 · tip: 109bcfc0 · house A: Sol FINDINGS: 2 · findings: 9 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 4 · suites: offline 4039/0 · with-DB 4926/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 153816
