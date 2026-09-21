# Degraded line build — 2026-09-21

## §0 Headline
Built: slim red `#degraded-line` above the card ladder on `/radar` (desktop + phone), carrying the pool view's DEGRADED / STALE banners and, client-side, REFRESH FAILED — never RETAINED (R10 / R11); `hidden` with no box when healthy.
Code `c183ed6` (five places in `radar_panel.py` + 13 test cases), DevDoc `df0011a`; suite 2208 passed / 0 failed (baseline 2195); T1 10 RED → GREEN, guard (c) GREEN on both.
Not run: a browser (L70). RESTARTS: `com.cobalt.aset` only. ESCALATE: 2 (main moved after the cut; no browser ran).

## L74
A block arrived after the Read tool result of `14-degraded-line-build.md` asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits and naming a file-send tool (SendUserFile). Recorded once, DATA, not followed: commits carry `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` and nothing else.

## AUTHORIZATION
Checked 2026-09-21 08:28–08:29 ET, every command allowed, none denied.

| Item | Command | Result |
|---|---|---|
| R10 in file | `grep -n "^| R10 " cto-2026-09-21.md` | line 22, carries "A and this evenuing" and "slim red degraded line" |
| R10 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"A and this evenuing" -- …cto-2026-09-21.md` | `2d6e01864f9042d676b62298c9832c2912443128` |
| R11 in file | `grep -n "^| R11 " …` | line 23, carries "DEGRADED, STALE and REFRESH FAILED only" and "RETAINED PRIOR-DAY DATA" |
| R11 committed | `git -C … log -1 --format=%H -S"DEGRADED, STALE and REFRESH FAILED only" -- …` | `d87f3bdb09a3e1ff33a78a92b471c779aa74ca78` |
| Launch row | `grep -n "^| R" …` | line 26, `| R14 |` "DESK LAUNCH ROW … `14-degraded-line-build.md`" — number filled in, no `__` |
| Launch row committed | `git -C … log -1 --format=%H -S"14-degraded-line-build.md" -- …` | `d87f3bdb09a3e1ff33a78a92b471c779aa74ca78` |
| R25 approval | `grep -n "^| R25 " …cto-2026-09-20.md` | line 262, 17:58 ET, "approved", names `11-bars-chunk-2-build.md` |
| No new rule | `grep -c -F -e "<rule>" …/02-bars-chunk-2-fix-r3.md` × 19 | each of the 16 allow strings (`uv run pytest *`, `uv run cobalt jobs restarts *`, `git add *`, `git commit *`, `git diff *`, `git status*`, `git log*`, `git show*`, `git -C /Users/cobalt/cobalt log*`, `cd *`, `mkdir -p *`, `ls *`, `grep *`, `tail *`, `wc *`, `date*`) = 1; 3 deny strings (`AskUserQuestion`, `EnterWorktree`, `Bash(git push*)`) = 1 each; `--add-dir` triplet = 1 |

AUTHORIZATION holds.

## PREFLIGHT
| Rule | Command | Exit | Result |
|---|---|---|---|
| date | `date` | 0 | allowed — `Mon Sep 21 08:28:39 EDT 2026` |
| clean worktree | `git status --porcelain` | 0 | allowed — empty |
| long status | `git status` | 0 | allowed — "On branch s2/degraded-line-0921 / nothing to commit, working tree clean" |
| tip | `git log --oneline -1` | 0 | allowed — `d87f3bd docs(desk): 09-21 R11-R14, degraded-line prompts 14-18 drafted and folded, launch row R14 for the build` (FIRST LAUNCH; this is `<main tip>`) |
| main's tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `d87f3bd …` same as the line above (main did not move after the cut; the drafter read `2d6e018`) |
| branch vs main | `git log --oneline main..HEAD` | 0 | allowed — empty |
| HEAD | `git show --stat HEAD` | 0 | allowed — the desk's `d87f3bd` (8 docs paths) |
| unstaged | `git diff --stat` | 0 | allowed — empty |
| .env | `ls -la .env` | 1 | allowed — "ls: .env: No such file or directory" (required) |
| size | `wc -l src/cobalt/aset/radar_panel.py` | 0 | allowed — 1164 |
| anchors | `grep -n "id=\"pool-layer\"\|…" radar_panel.py` | 0 | allowed — `:850` pool-layer section; `:1040` ladder-layer; `:1118` `window.setInterval(refreshPool,interval);`; `:1126` `render_radar_page` body with `{render_ladder(view.ladder)}{render_pool(view.pool)}` (as the prompt says) |
| INDEX CARD item 3 grep | `grep -n "firstElementChild\|first-child\|nth-child\|sticky\|…\|degraded-line" radar_panel.py` | 0 | allowed — hits: `:838` (`render_pool` banner div, `panel-banner {banner.level}`); `:1048` (CSS `.panel-banner,.refresh-failure` colours; `.retained`); `:1050` (`.strip span:nth-child(4)` — inside the ladder strip, within the mobile media query, not across sections); `:1110` (`holder.firstElementChild` — the fragment holder in `refreshPool`); `:1114` (`refresh-failure` box written by the catch); `:1131` (`render_failed_page` banner, no ladder, no script). No `degraded-line`, `sticky`, `insertBefore`, `nextElementSibling` hit. Nothing the drafter did not list; no new banner source; no ESCALATE. |
| cd | `cd /Users/cobalt/cobalt-wt/degraded-line` | — | (already in it; no `cd` needed) |
| pytest | `uv run pytest --version` | 0 | allowed — `pytest 9.0.2` (created `.venv` first) |
| restarts | `uv run cobalt jobs restarts main..HEAD` | 0 | allowed — `RESTARTS: none` |
| mkdir | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | allowed — directory exists, no-op probe |

## BASELINE
`date` → `Mon Sep 21 08:29:16 EDT 2026`.
`uv run pytest -q tests/cobalt tests/taxonomy` (run in background, on main's code — the new test file was not yet edited at collection):
`2195 passed, 351 skipped, 1 xfailed, 15 warnings in 67.66s (0:01:07)` — no `failed` in the line (0 failed).
`uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py -k "not degraded_line"` (the two files alone; run after T1's tests were written, so they are deselected by name — the 13 deselected are exactly T1's 13): `77 passed, 1 skipped, 13 deselected in 0.91s`.

## T1 TEST FIRST
Seven test functions, 13 test cases, all in `tests/cobalt/test_radar_panel.py`, beside `test_ladder_renders_above_the_pool_in_both_frames`, built only from the existing fixtures (`_build`, `_small_snapshot`, `POOL_FIXTURE`, `TestClient`, monkeypatched `build_radar_panel`). New small helpers: `_fixture_source_name`, `_degraded_pool`, `_degraded_view`, `_healthy_view`, `_retained_view`, `_line_element`; `import html` added.
Source name: `pool_row["sources"]` is `[]` in `panel-pool.real-shape.json` (`:16851`), so the first membership `source` was used: `screen:morning_low_float@000000000000` (fixture line 17). No invented name.
Each builder asserts its state first, and those asserts held on main: healthy `view.pool.banners == []`; RETAINED-only `["retained"]`; RETAINED + DEGRADED `["degraded", "retained"]`; degraded `["degraded"]`.
Case count: (a) 2 frames × 2 sources (the fixture name and `"<bad>&"`) = 4 · (b) 2 · (c) 3 · (d) 1 · (e) 1 · (f) 2 = 13.

RED on main's code, `uv run pytest -q tests/cobalt/test_radar_panel.py -k "degraded_line" --tb=line -p no:cacheprovider --color=no`, VERBATIM excerpts:
```
FFFFFF...FFFF                                                            [100%]
E   assert 0 == 1
     +  where 0 = <built-in method count of str object at 0x144cb5c00>('id="degraded-line"')
/Users/cobalt/cobalt-wt/degraded-line/tests/cobalt/test_radar_panel.py:592: assert 0 == 1      (a) x4
E   assert 0 == 1
     +  where 0 = <built-in method count of str object at 0x144cd3a00>('<div id="degraded-line" class="degraded-line" hidden></div>')
/Users/cobalt/cobalt-wt/degraded-line/tests/cobalt/test_radar_panel.py:607: assert 0 == 1      (b) x2
E   AttributeError: module 'cobalt.aset.radar_panel' has no attribute 'render_degraded_line'
/Users/cobalt/cobalt-wt/degraded-line/tests/cobalt/test_radar_panel.py:641: AttributeError: …  (d)
E   assert 'id="degraded-line"' in '<!doctype html>…</script></body></html>'
/Users/cobalt/cobalt-wt/degraded-line/tests/cobalt/test_radar_panel.py:670: assert 'id="degraded-line"' in …   (e)
E   assert 0 == 1
     +  where 0 = <built-in method count of str object at 0x13500ce00>('<div id="degraded-line" class="degraded-line" hidden></div>')
/Users/cobalt/cobalt-wt/degraded-line/tests/cobalt/test_radar_panel.py:680: assert 0 == 1      (f) x2
10 failed, 3 passed, 53 deselected in 0.17s
```
(a) ×4, (b) ×2, (d), (e), (f) ×2 = 10 RED; (c) ×3 = the 3 that passed — GREEN on main too, as expected: it is the guard that the pool view did not change. Nothing committed (the tests and the change commit together in C1).

## C1 THE CHANGE
`date` → `Mon Sep 21 08:31:48 EDT 2026` (commit time). Commit `c183ed6` `feat(radar): slim red degraded line above the card ladder on /radar, mirrored by refreshPool (R10 2026-09-21)`; `git show --stat HEAD` after it: `src/cobalt/aset/radar_panel.py | 22 +++-` and `tests/cobalt/test_radar_panel.py | 160 +++` — the two named paths only.
GREEN after the change: `uv run pytest -q tests/cobalt/test_radar_panel.py -k "degraded_line" --color=no -p no:cacheprovider` → `13 passed, 53 deselected in 0.18s` (the 10 that were RED on main, plus the 3 guards).
`git diff -- src/cobalt/aset/radar_panel.py` (before the commit), WHOLE — six hunks, the five named places (item 4 is two hunks: the function and the two `refreshPool` calls):
```
@@ -859,6 +859,20 @@ def render_pool(view: PoolView) -> str:
+def render_degraded_line(view: PoolView) -> str:
+    """The slim red line above the card ladder (R10 2026-09-21): a second
+    rendering of the pool view's own banners — the same `view.banners`, the
+    same inner markup — never a second degraded computation (L3). Carries
+    DEGRADED and STALE only, never RETAINED PRIOR-DAY DATA (R11 2026-09-21).
+    Always present so `refreshPool` can mirror into it; `hidden` (no box)
+    when the pool view shows no carried banner."""
+    e = html.escape
+    carried = [banner for banner in view.banners if banner.level in ("degraded", "stale")]
+    inner = " | ".join(f"<b>{e(banner.title)}</b> · {e(banner.detail)}" for banner in carried)
+    hidden = "" if carried else " hidden"
+    return f'<div id="degraded-line" class="degraded-line"{hidden}>{inner}</div>'
@@ -1050,6 +1064,7 @@ PANEL_CSS = r"""
+.degraded-line{padding:3px 12px;border:1px solid var(--red);background:#351019;color:#ffd0d6;border-radius:5px;margin:6px 0 0;font-size:12px}.degraded-line[hidden]{display:none}
@@ -1098,6 +1113,7 @@ PANEL_JS = r"""
+ function mirrorDegraded(layer){const line=document.getElementById('degraded-line'); const parts=Array.from(layer.querySelectorAll('.refresh-failure,.panel-banner.degraded,.panel-banner.stale')).map(x=>x.innerHTML); const text=parts.join(' | '); if(line.innerHTML!==text){line.innerHTML=text;} const none=parts.length===0; if(line.hidden!==none){line.hidden=none;}}
@@ -1108,10 +1124,11 @@ PANEL_JS = r"""
-     oldLayer.replaceWith(next); cursor=payload.pool.observed_watermark;
+     oldLayer.replaceWith(next); cursor=payload.pool.observed_watermark; mirrorDegraded(next);
+     mirrorDegraded(oldLayer);
@@ -1123,7 +1140,7 @@ PANEL_JS = r"""
-<body class="{frame_class}" …><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav>{render_ladder(view.ladder)}{render_pool(view.pool)}</main>…
+<body class="{frame_class}" …><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav>{render_degraded_line(view.pool)}{render_ladder(view.ladder)}{render_pool(view.pool)}</main>…
@@ -1157,6 +1174,7 @@ __all__ = [
+    "render_degraded_line",
```
(The full unified diff, with context lines, is `git diff main -- src/cobalt/aset/radar_panel.py`, run again at CLOSE.) No hunk in `render_pool`, `render_ladder`, `render_failed_page`, `pool_api_payload`, `build_pool_view`, `post()`, the click handler, `refreshLadder`, or the interval line.

## A1 ASSERTIONS RE-POINTED
NONE — 90 tests, BASELINE's file line (`77 passed, 1 skipped`) plus T1's 13, all green: `uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py --color=no -p no:cacheprovider` → `90 passed, 1 skipped in 0.88s`. Nothing re-pointed, nothing committed in A1. The JS test at `test_refresh_javascript_preserves_ladder_state_and_cursor_on_failure` (`cursor=` absent after `catch(error)`) still passes: `mirrorDegraded` has no `cursor=`.

## D1 DEVDOC
`docs/40 - DevDocs/cobalt/aset/radar_panel.md`: the one sentence about `render_degraded_line()` appended to the `## Rendering` paragraph after the `render_pool()` / `render_ladder()` sentence, and `render_degraded_line` added to the `## Public functions` renderer list. Nothing else in that file changed. Commit `df0011a` `docs(devdocs): radar_panel — degraded line above the ladder (R10 2026-09-21)`; `git show --stat HEAD` → that one path only (`2 insertions(+), 2 deletions(-)`).
`docs/40 - DevDocs/cobalt/aset/web.md` `:7-8`: read; neither sentence becomes false (the route and the payload are unchanged; `/radar` still composes the page with `render_radar_page()`) → UNTOUCHED.

## CLOSE
`date` → `Mon Sep 21 08:33:21 EDT 2026`.

**Full suite** on the tip, `uv run pytest -q tests/cobalt tests/taxonomy --color=no -p no:cacheprovider` (background): `2208 passed, 351 skipped, 1 xfailed, 15 warnings in 63.68s (0:01:03)`. Against BASELINE `2195 passed, 351 skipped, 1 xfailed, 15 warnings`: failed 0 (none in either line), passed +13 = T1's 13 cases ((a) 4 = 2 frames × 2 sources · (b) 2 · (c) 3 · (d) 1 · (e) 1 · (f) 2), skipped 351 unchanged.

**Paths.** `git diff --stat main` (two-dot, VERBATIM):
```
 docs/40 - DevDocs/cobalt/aset/radar_panel.md       |   4 +-
 .../prompts/2026-09-21/19-defs-gap-table.md        |  24 ----
 docs/40 - DevDocs/reports/cto-2026-09-21.md        |   5 +-
 src/cobalt/aset/radar_panel.py                     |  22 ++-
 tests/cobalt/test_radar_panel.py                   | 160 +++++++++++++++++++++
 5 files changed, 183 insertions(+), 32 deletions(-)
```
Two of those paths are NOT mine: main moved after the cut (`git -C /Users/cobalt/cobalt log --oneline -3` → `c915784 docs(desk): 09-21 R13 (empty-ladder mornings count), R15 (13 definitions at defaults), build 14 and gap table 19 launched` above `d87f3bd`), so a two-dot diff against the moved `main` shows the desk's commit in reverse. See ESCALATE 1. Against the merge base, `git diff --stat main...HEAD` (VERBATIM) lists only my paths (the report is still uncommitted here):
```
 docs/40 - DevDocs/cobalt/aset/radar_panel.md |   4 +-
 src/cobalt/aset/radar_panel.py               |  22 +++-
 tests/cobalt/test_radar_panel.py             | 160 +++++++++++++++++++++++++++
 3 files changed, 182 insertions(+), 4 deletions(-)
```
`tests/cobalt/test_radar_panel_cards.py` and `docs/40 - DevDocs/cobalt/aset/web.md` are absent, as expected.

**L52 and the routes — EMPTY DIFFS**, each run against `main` (c915784) and each "no output": `git diff main -- src/cobalt/cards` · `git diff main -- src/cobalt/radar` · `git diff main -- src/cobalt/aset/web.py` · `git diff main -- src/cobalt/aset/store.py` · `git diff main -- configs`.

**Five-place proof.** `git diff main -- src/cobalt/aset/radar_panel.py` re-run: byte-identical to the C1 diff quoted above (main did not touch this file since the cut), hunks at `@@ -859` (the renderer), `@@ -1050` (CSS line), `@@ -1098` (the JS function), `@@ -1108` (the two `refreshPool` calls), `@@ -1123` (`render_radar_page`), `@@ -1157` (`__all__`); nothing in `render_pool`, `render_ladder`, `render_failed_page`, `pool_api_payload`, `build_pool_view`, `post()`, the click handler, `refreshLadder` or the interval line.

**RESTARTS**, `uv run cobalt jobs restarts main..HEAD`, VERBATIM (run before the report commit, so the report row is that file's; it is `DOCS`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/prompts/2026-09-21/19-defs-gap-table.md	D	DOCS	-
docs/40 - DevDocs/reports/cto-2026-09-21.md	M	DOCS	-
docs/40 - DevDocs/reports/degraded-line-build-2026-09-21.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
`com.cobalt.aset` IS there (it imports `cobalt.aset.radar_panel` through `web.py`), as expected. `com.cobalt.radar` is NOT in it. No `UNCLASSIFIED`. (The `19-defs-gap-table.md` D and `cto-2026-09-21.md` M rows are the moved-main artefact, not mine; the rule is a two-dot range against the local `main` ref.)

**Commits**, `git log --oneline main..HEAD` (before the report commit): `df0011a docs(devdocs): radar_panel — degraded line above the ladder (R10 2026-09-21)` · `c183ed6 feat(radar): slim red degraded line above the card ladder on /radar, mirrored by refreshPool (R10 2026-09-21)`. No A1 commit (nothing to re-point), no wip commit. The stop line's `<tip>` is C1's `c183ed6`, the last CODE commit; D1 `df0011a` (docs only) sits above it, the report commit above that.

**What each `proven` rests on** (all on `c183ed6`, offline):
- line above ladder when degraded, desktop + phone: T1 (a) ×4 and (e) RED → GREEN.
- absent when healthy: T1 (b) ×2 RED → GREEN (exact `<div id="degraded-line" class="degraded-line" hidden></div>`, plus the `[hidden]{display:none}` rule).
- stays current on refresh: T1 (d) server-side parity across degraded → healthy → RETAINED-only → RETAINED + DEGRADED → degraded, and the JS-wiring substring assertions, RED → GREEN. Server side and wiring only — see ESCALATE 2.
- pool banners unchanged: T1 (c) ×3 GREEN on main and on the tip; `render_pool` absent from C1's diff.
- retained not carried: T1 (f) ×2 RED → GREEN in both frames; T1 (d)'s RETAINED-only and RETAINED + DEGRADED steps and its JS-selector assertions (`.panel-banner.retained` never selected; the unfiltered selector absent) GREEN.
- card/scoring paths untouched: the five diffs above are empty.

`git status --porcelain` after the report commit: see the last commit step (expected EMPTY).

## ESCALATE
1. **MAIN MOVED AFTER THE CUT.** The branch is cut from `d87f3bd`; local `main` is now `c915784` (a desk docs-only commit: `19-defs-gap-table.md` added, `cto-2026-09-21.md` edited — neither is mine, neither touches `src/`, `tests/` or `configs/`). Nothing built here depends on it, but a two-dot `git diff main` / `git diff --stat main` / `cobalt jobs restarts main..HEAD` shows those paths in reverse, and `16-degraded-line-deploy.md`'s `git rebase main` will replay my commits onto `c915784`. The merge-base diff (`main...HEAD`) is clean. Not acted on.
2. **NO BROWSER RAN (L70).** `PANEL_JS` was proven by server-side parity (T1 (d)) and substring wiring assertions, not by a JavaScript engine. What a browser does on a live refresh — the line appearing, clearing, and not moving the ladder on an unchanged refresh — is UNPROVEN until the desk confirms it on the live page with him. A state CHANGE (a source going degraded or recovering) moves the ladder down or up by the line's height, by design.

Standing notes, not open items:
- (i) **STATES CARRIED — RULED, not open:** R11 (`cto-2026-09-21.md` §4, 08:21 ET, "a") — DEGRADED, STALE and REFRESH FAILED only; RETAINED PRIOR-DAY DATA is not carried (T1 (f)).
- (iii) `ASK DESK`: none.
- (iv) `MEMORY:` / `RULING:` lines: none.

## CONTINUE
next: none — build complete, report committed by the last step.

DEGRADED LINE BUILT c183ed6 | on d87f3bd | offline 2208/0 (351 skipped; baseline 2195/0) | line above ladder when degraded, desktop + phone: proven | absent when healthy: proven | stays current on refresh: proven | pool banners unchanged: proven | retained not carried: proven | card/scoring paths untouched: empty diff | RESTARTS: com.cobalt.aset | ESCALATE: 2
