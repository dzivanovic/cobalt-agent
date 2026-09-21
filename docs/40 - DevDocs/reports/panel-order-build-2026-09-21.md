# Panel order build — 2026-09-21 (hub `panel-order-build-0921`, Sonnet 5)

## §0 Headline
- R3 built: `/radar` now renders the CARD LADDER above the POOL VIEW, desktop and phone (`render_radar_page`, one line, `radar_panel.py:1126`); tests first (RED `8583 < 6418` → GREEN), commits `291ce7b` (change + tests), `5dc5819` (two DevDoc edits).
- Offline suite `2195 passed, 351 skipped, 1 xfailed, 0 failed` (baseline `2192 passed`, +3 = my tests); radar files `77 passed, 1 skipped`; A1 nothing to re-point.
- Empty diffs: `src/cobalt/cards`, `src/cobalt/radar`, `web.py`, `store.py`, `configs`. RESTARTS: `com.cobalt.aset` (no `com.cobalt.radar`, no UNCLASSIFIED).
- ESCALATE: 2 — (i) degradation banners now sit below the ladder (his call, nothing changed); (ii) main moved after the cut (`03b12e0`, desk docs only), so `git diff --stat main` shows `cto-2026-09-21.md`; my own change is the four allowed paths.

## L74
- Recorded ONCE (L74). After the first Read of the prompt file, the harness appended an attribution reminder asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits/PR bodies and naming a file-send tool (`SendUserFile`). Per this prompt (INDEX CARD L74) and LAWS.md L74: not followed; commits carry `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` and nothing else.

## AUTHORIZATION
Started 2026-09-21 06:36 ET (`date`: `Mon Sep 21 06:36:22 EDT 2026`). All checks run by me, tool output quoted.
- R3 present: `grep -n "^| R3 "` on main's `cto-2026-09-21.md` → line 14, "RADAR PAGE ORDER, his words: … my top should always be trade radar and the cards that should be always on top of the page because that's what I'm working on." → the CARD LADDER / TRADE RADAR section is ALWAYS the top of `/radar`.
- R3 COMMITTED: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"my top should always be trade radar" -- "docs/40 - DevDocs/reports/cto-2026-09-21.md"` → `1be40a45d62970d54794559aa5706052dd28c686` (non-empty).
- Launch row: `grep -n "^| R" …cto-2026-09-21.md` → line 16 `| R4 | 06:35 ET | — NO WORDS OF HIS: a DESK LAUNCH ROW … numbered because prompts/2026-09-21/08-panel-order-build.md's AUTHORIZATION greps this table for it …` — number filled in (`R4`, not `R__`), names `08-panel-order-build.md`.
- Launch row COMMITTED: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"08-panel-order-build.md" -- …cto-2026-09-21.md` → `2c8f3d587952de2ca3b964e672c36e3e24867091` (non-empty).
- R25: `grep -n "^| R25 " …/cto-2026-09-20.md` → line 262 `| R25 | 17:58 ET | "approved" — … launch lines of prompts/2026-09-20/10-bars-chunk-1a-build.md AND prompts/2026-09-20/11-bars-chunk-2-build.md exactly as written …` — names `11-bars-chunk-2-build.md` and "approved".
- NO NEW RULE: `grep -c -F -e "<rule>" …/prompts/2026-09-21/02-bars-chunk-2-fix-r3.md` (quotes included), one call each:

| # | rule | count |
|---|---|---|
| 1 | `"Bash(uv run pytest *)"` | 1 |
| 2 | `"Bash(uv run cobalt jobs restarts *)"` | 1 |
| 3 | `"Bash(git add *)"` | 1 |
| 4 | `"Bash(git commit *)"` | 1 |
| 5 | `"Bash(git diff *)"` | 1 |
| 6 | `"Bash(git status*)"` | 1 |
| 7 | `"Bash(git log*)"` | 1 |
| 8 | `"Bash(git show*)"` | 1 |
| 9 | `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 |
| 10 | `"Bash(cd *)"` | 1 |
| 11 | `"Bash(mkdir -p *)"` | 1 |
| 12 | `"Bash(ls *)"` | 1 |
| 13 | `"Bash(grep *)"` | 1 |
| 14 | `"Bash(tail *)"` | 1 |
| 15 | `"Bash(wc *)"` | 1 |
| 16 | `"Bash(date*)"` | 1 |
| deny 1 | `"AskUserQuestion"` | 1 |
| deny 2 | `"EnterWorktree"` | 1 |
| deny 3 | `"Bash(git push*)"` | 1 |
| triplet | `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt` | 1 (≥1) |

All 19 counts = 1; triplet ≥ 1. Result: AUTHORIZED. LAWS.md read in full (INDEX CARD item 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | allowed — `Mon Sep 21 06:36:22 EDT 2026` |
| clean tree | `git status --porcelain` | 0 | allowed — empty |
| branch | `git status` | 0 | allowed — `On branch s2/panel-order-0921` / `nothing to commit, working tree clean` |
| tip | `git log --oneline -1` | 0 | allowed — `2c8f3d5 docs(desk): 09-21 panel-order prompts 08-09 drafted, launch row R4 for the build` (FIRST launch; = main's tip; `<main tip>` = `2c8f3d5`) |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `2c8f3d5 docs(desk): 09-21 panel-order prompts 08-09 drafted, launch row R4 for the build` (equal) |
| branch vs main | `git log --oneline main..HEAD` | 0 | allowed — empty |
| HEAD stat | `git show --stat HEAD` | 0 | allowed — commit `2c8f3d5`, 4 files (the desk's prompts 08/09, `cto-2026-09-21.md`, `panel-order-draft-2026-09-21.md`), 190 insertions |
| unstaged | `git diff --stat` | 0 | allowed — empty |
| .env | `ls -la .env` | 1 | allowed — `ls: .env: No such file or directory` (required) |
| size | `wc -l src/cobalt/aset/radar_panel.py` | 0 | allowed — `1164 src/cobalt/aset/radar_panel.py` |
| anchors | `grep -n "id=\"pool-layer\"\|id=\"ladder-layer\"\|render_pool(view.pool)" src/cobalt/aset/radar_panel.py` | 0 | allowed — `850: return f'''<section id="pool-layer" …`; `1040: return f"""<section id="ladder-layer">…`; `1126: <body class="{frame_class}" … {render_pool(view.pool)}{render_ladder(view.ladder)}</main><script>{PANEL_JS}</script></body></html>'''` — `render_radar_page`'s line IS `:1126`, as the prompt says |
| order-dependency grep | `grep -n "firstElementChild\|first-child\|nth-child\|sticky\|nextElementSibling\|previousElementSibling\|insertBefore\|children\[" src/cobalt/aset/radar_panel.py` | 0 | allowed — TWO hits, both the drafter's: `1050: @media (max-width:700px){.strip{…}.strip span:nth-child(4){display:none}…` (inside a card strip, not across sections) and `1110: const next=holder.firstElementChild; if(!next){throw new Error('empty pool fragment');}` (first element of the POOL FRAGMENT `holder`, not of the page). No `first-child`, `sticky`, `nextElementSibling`, `previousElementSibling`, `insertBefore`, `children[` hit. |
| cd | `cd /Users/cobalt/cobalt-wt/panel-order` | 0 | allowed |
| pytest | `uv run pytest --version` | 0 | allowed — `pytest 9.0.2` (uv created `.venv` and installed 248 packages in this fresh worktree) |
| restarts probe | `uv run cobalt jobs restarts main..HEAD` | 0 | allowed — `path	change	rule	restart` / `RESTARTS: none` (empty range) |
| mkdir probe | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | allowed — directory already existed; no-op |

`git add` / `git commit`: probed by first real use (below). No denials in PREFLIGHT.

ORDER-DEPENDENCY VERIFICATION (INDEX CARD item 3 — read, not trusted): I read `PANEL_CSS` (`:1046-1053`) and `PANEL_JS` (`:1056-1120`) whole. CSS: no `+` / `~` sibling combinator anywhere, no `:first-child`, no `position:sticky` (only `.ladder-item{position:relative}` / `.promote{position:absolute}` inside a card); the `@media` rules at `:1049-1051` style `.expanded`, `.detail-pane`, `.strip`, `.radar-wrap`, `.pool-stats`, `.layer-head`, `table`, `body`, `.phone-frame` — none selects a section by position. JS: `refreshLadder` swaps `document.getElementById('ladder-layer')` by id (`:1071-1073`); `refreshPool` swaps `#pool-layer` by id (`:1104`, `:1111`) and `firstElementChild` (`:1110`) is on the detached `holder` fragment; `cursor` (`:1101`) is read at script run time from the script at the end of `<body>`, after both sections exist. The only hits are the drafter's two. Verdict: NO order dependency; nothing to escalate on this item. Route: `web.py:857-867` calls `render_radar_page(view, phone_frame=phone_frame)` with `phone_frame = frame == "phone"` (read only).

## BASELINE
`date` → `Mon Sep 21 06:39:01 EDT 2026` (after the runs below).
- `uv run pytest -q tests/cobalt tests/taxonomy` (background), main's tree, verbatim summary: `2192 passed, 351 skipped, 1 xfailed, 15 warnings in 68.70s (0:01:08)` — `0 failed`.
- `uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py`, verbatim: `74 passed, 1 skipped in 0.87s`.
- Pre-check for A1 (grep, read): the only tests touching the page renderer are `test_radar_panel.py:509` (`'class="phone-frame"' in …`) and `:619` (`rendered = panel.render_radar_page(view)`); `test_radar_panel_cards.py:345-349` index within one rendered ladder. None compares a `pool-layer` index with a `ladder-layer` index.

## T1 TEST FIRST
Added to `tests/cobalt/test_radar_panel.py` (uncommitted until C1): `test_ladder_renders_above_the_pool_in_both_frames` (parametrized `phone_frame` False/True, over `_build()`'s view and the real `render_radar_page`, `render_pool`, `render_ladder`; no invented HTML — L45) after `test_css_has_exact_responsive_contract_and_phone_frame`, and `test_radar_route_serves_the_ladder_above_the_pool_in_both_frames` (real `/radar` and `/radar?frame=phone` through `TestClient(web_module.app)` with the file's `route_view` fixture and `monkeypatch.setattr(web_module, "build_radar_panel", lambda **_kwargs: route_view)`) after `test_panel_has_no_write_or_focus_stealing_markup`.

RED against today's (pool-first) code — `uv run pytest -q tests/cobalt/test_radar_panel.py -k "above_the_pool"`, verbatim failing lines:
```
E       assert 8583 < 6418   (test_ladder_renders_above_the_pool_in_both_frames[False]: ladder-layer index 8583, pool-layer index 6418)
E       assert 8594 < 6429   (test_ladder_renders_above_the_pool_in_both_frames[True])
E           assert 8583 < 6418   (test_radar_route_serves_the_ladder_above_the_pool_in_both_frames)
  FAILED tests/cobalt/test_radar_panel.py::test_ladder_renders_above_the_pool_in_both_frames[False] - assert 8583 < 6418
  FAILED tests/cobalt/test_radar_panel.py::test_ladder_renders_above_the_pool_in_both_frames[True] - assert 8594 < 6429
  FAILED tests/cobalt/test_radar_panel.py::test_radar_route_serves_the_ladder_above_the_pool_in_both_frames - assert 8583 < 6418
  (the three lines above are indented by two spaces here only, so no line of this report other than the stop line starts with `FAILED` — L71)
3 failed, 50 deselected in 0.24s
```
The count-equals-1 assertions (both ids appear exactly once) passed before the failing order line, so the RED is the ORDER and nothing else. (The parenthesised notes on the first three lines are mine; the rest is tool output.)

## C1 THE CHANGE
`render_radar_page` only (`src/cobalt/aset/radar_panel.py:1126`): swapped `{render_pool(view.pool)}{render_ladder(view.ladder)}` → `{render_ladder(view.ladder)}{render_pool(view.pool)}`.
- GREEN: `uv run pytest -q tests/cobalt/test_radar_panel.py -k "above_the_pool"` → `3 passed, 50 deselected in 0.17s`.
- `git diff -- src/cobalt/aset/radar_panel.py` whole (one `-`/`+` pair, inside `render_radar_page`):
```
@@ -1123,7 +1123,7 @@ PANEL_JS = r"""
 def render_radar_page(view: RadarPanelView, *, phone_frame: bool = False) -> str:
     frame_class = "phone-frame" if phone_frame else ""
     return f'''<!doctype html>…<style>{PANEL_CSS}</style></head>
-<body class="{frame_class}" … <nav><a href="/">ASET sheet</a></nav>{render_pool(view.pool)}{render_ladder(view.ladder)}</main><script>{PANEL_JS}</script></body></html>'''
+<body class="{frame_class}" … <nav><a href="/">ASET sheet</a></nav>{render_ladder(view.ladder)}{render_pool(view.pool)}</main><script>{PANEL_JS}</script></body></html>'''
```
(long lines abbreviated with `…` here only; the full unabbreviated diff is under CLOSE — `2 files changed` for the commit: `radar_panel.py | 2 +-`, `test_radar_panel.py | 25 +++`.)
- Commit `291ce7b` `feat(radar): the card ladder renders above the pool view on /radar, desktop and phone (R3 2026-09-21)`; `git show --stat HEAD` listed only `src/cobalt/aset/radar_panel.py` (2 +-) and `tests/cobalt/test_radar_panel.py` (25 +). `git add` and `git commit` were probed by this first real use: both allowed.

## A1 ASSERTIONS RE-POINTED
NONE — 77 tests (+1 skipped), the same 74 passed / 1 skipped as BASELINE's file line plus T1's 3 new tests, all green. `uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `77 passed, 1 skipped in 0.87s`. No existing assertion was touched; nothing committed in A1.

## D1 DEVDOC
Commit `5dc5819` `docs(devdocs): radar_panel + web — ladder above pool on /radar (R3 2026-09-21)`; `git show --stat HEAD` listed only the two DevDocs (2 +-, 2 +-).
- `docs/40 - DevDocs/cobalt/aset/radar_panel.md:44`: appended ONE sentence — "`render_radar_page()` renders the card ladder FIRST and the pool view BELOW it (desktop and phone frame; ruled 2026-09-21, R3); both layers keep their ids and the refreshers still replace them by id, so the order is page layout only."
- `docs/40 - DevDocs/cobalt/aset/web.md:7`: `pool-first page` → `ladder-first (card ladder above the pool view, R3 2026-09-21) page`, nothing else.

## CLOSE
Each proof its own call; results verbatim.
- **Suite** — `uv run pytest -q tests/cobalt tests/taxonomy` (background) on tip `5dc5819`: `2195 passed, 351 skipped, 1 xfailed, 15 warnings in 64.40s (0:01:04)` — `0 failed`. Against BASELINE `2192 passed, 351 skipped, 1 xfailed`: failed 0 = 0; passed +3 = T1's three tests (two parametrized page cases + one route test — the run counts exactly as the prompt expected); skipped 351 = 351; xfailed 1 = 1.
- **`git diff --stat main`** (run BEFORE the report commit) — verbatim:
```
 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  2 +-
 docs/40 - DevDocs/cobalt/aset/web.md         |  2 +-
 docs/40 - DevDocs/reports/cto-2026-09-21.md  | 11 +----------
 src/cobalt/aset/radar_panel.py               |  2 +-
 tests/cobalt/test_radar_panel.py             | 25 +++++++++++++++++++++++++
 5 files changed, 29 insertions(+), 13 deletions(-)
```
  Four paths are in the allowed list. `docs/40 - DevDocs/reports/cto-2026-09-21.md` is NOT one of them — it is not my change: MAIN MOVED after the cut (`git -C /Users/cobalt/cobalt log --oneline -4` → tip `03b12e0 docs(desk): 09-21 panel-order build 9937d0bd launched (R4), sessions table 06:37`, one desk docs commit above `2c8f3d5`; `git show --stat main` → only `cto-2026-09-21.md`, 10 insertions / 1 deletion), so `git diff main` shows that commit reversed. My branch's own change, `git diff --stat main...HEAD` (merge-base form), verbatim: `radar_panel.md 2 +-`, `web.md 2 +-`, `radar_panel.py 2 +-`, `test_radar_panel.py 25 +++++++++++++++++++++++++` = `4 files changed, 28 insertions(+), 3 deletions(-)` — exactly the allowed set (`test_radar_panel_cards.py` ABSENT, as expected). Recorded under ESCALATE (ii).
- **L52 AND THE ROUTES — EMPTY DIFFS:** `git diff main -- src/cobalt/cards` → no output. `git diff main -- src/cobalt/radar` → no output. `git diff main -- src/cobalt/aset/web.py` → no output. `git diff main -- src/cobalt/aset/store.py` → no output. `git diff main -- configs` → no output.
- **THE ONE-LINE PROOF** — `git diff main -- src/cobalt/aset/radar_panel.py`, whole:
```
diff --git a/src/cobalt/aset/radar_panel.py b/src/cobalt/aset/radar_panel.py
index fdf0beb..3920791 100644
--- a/src/cobalt/aset/radar_panel.py
+++ b/src/cobalt/aset/radar_panel.py
@@ -1123,7 +1123,7 @@ PANEL_JS = r"""
 def render_radar_page(view: RadarPanelView, *, phone_frame: bool = False) -> str:
     frame_class = "phone-frame" if phone_frame else ""
     return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Cobalt · Trade Radar</title><style>{PANEL_CSS}</style></head>
-<body class="{frame_class}" data-refresh-seconds="{view.pool.scan_interval}"><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav>{render_pool(view.pool)}{render_ladder(view.ladder)}</main><script>{PANEL_JS}</script></body></html>'''
+<body class="{frame_class}" data-refresh-seconds="{view.pool.scan_interval}"><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav>{render_ladder(view.ladder)}{render_pool(view.pool)}</main><script>{PANEL_JS}</script></body></html>'''
 
 
 def render_failed_page(message: str, *, phone_frame: bool = False) -> str:
```
  One `-`/`+` pair inside `render_radar_page`; nothing in `PANEL_CSS`, `PANEL_JS`, `render_pool`, `render_ladder`, `render_failed_page`.
- **RESTARTS (L42)** — `uv run cobalt jobs restarts main..HEAD`, verbatim (run before the report commit; the `main..HEAD` range also picks up main's desk-docs commit, which is why `cto-2026-09-21.md` appears — it is documentation either way):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/reports/cto-2026-09-21.md	M	DOCS	-
docs/40 - DevDocs/reports/panel-order-build-2026-09-21.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
  `com.cobalt.aset` IS there (`static import reach`, as the prompt expected — it imports `cobalt.aset.radar_panel` through `web.py`). `com.cobalt.radar` is NOT in it. No `UNCLASSIFIED`.
- **`git log --oneline main..HEAD`** (before the report commit): `5dc5819 docs(devdocs): radar_panel + web — ladder above pool on /radar (R3 2026-09-21)` and `291ce7b feat(radar): the card ladder renders above the pool view on /radar, desktop and phone (R3 2026-09-21)` — C1, D1; no A1, no wip.
- `<tip>` in the stop line = `5dc5819` (D1, the last commit on the branch before the report commit); the LAST CODE commit is C1 `291ce7b`. `<main tip>` = `2c8f3d5` (the sha PREFLIGHT found; main has since moved to `03b12e0`, see above).
- After the report commit I run `git show --stat HEAD` (must list the report only) and `git status --porcelain` (must be empty); their output cannot be inside the commit it describes — it is in my final reply and the desk verifies it (L35).
- "proven" basis: T1's test was RED on main's order (`8583 < 6418`, `8594 < 6429`) and is GREEN on `5dc5819` (`3 passed`); pool content unchanged is proven by `panel.render_pool(view.pool) in page` and `panel.render_ladder(view.ladder) in page` (byte-for-byte) plus the three pool-part index assertions, in both frames.

## ESCALATE
1. **(i) VISIBILITY, NOT CODE — for the check and for him:** the pool section carries the page's loud-degradation surfaces (`#refresh-status` / `REFRESH FAILED`, the `panel-banner` source banners, the `stale-data` outline — `radar_panel.py:849-851`, `:1113-1114`); after the swap they sit BELOW the ladder, not at the top of the page. The ruling moves the pool "below … still visible", and moving a banner out of the pool would change pool content, which is NOT ordered — so nothing was changed; whether a degraded banner should also show above the ladder is HIS call (L9), not mine.
2. **(ii) `git diff --stat main` listed a path outside the allowed set** — `docs/40 - DevDocs/reports/cto-2026-09-21.md` (11 lines). Evidence above: main moved after the cut (`03b12e0`, the desk's own docs commit, `git show --stat main` → that file only); my branch did not touch it (`git diff --stat main...HEAD` lists the four allowed paths only). Nothing for me to fix; the desk should know the branch base is `2c8f3d5` while main is `03b12e0` when it reads `main..<tip>` for the check and when it merges (a docs-only divergence).
- `ASK DESK:` none. `MEMORY:` / `RULING:` none. Denials: none. NOT RUN: nothing.
- ESCALATE count: 2.

## CONTINUE
done — no step left. Nothing to resume.

PANEL ORDER BUILT 5dc5819 | on 2c8f3d5 | offline 2195/0 (351 skipped; baseline 2192/0) | ladder above pool, desktop + phone: proven | pool content unchanged: proven | card/scoring/route paths untouched: empty diff | RESTARTS: com.cobalt.aset | ESCALATE: 2
