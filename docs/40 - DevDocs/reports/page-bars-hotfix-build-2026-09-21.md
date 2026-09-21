# Page bars hotfix build — 2026-09-21

## §0 Headline
- `/radar` no longer dies on a per-ticker bars poll failure: it renders with a red `BARS POLL FAILED` DEGRADED banner naming each ticker, reason and since-time (ET); `radar_panel.py` +11 lines, all inside `build_pool_view`; no `render_*`, CSS, JS, `web.py`, radar or store change.
- Every other failed stage (membership, pool_row, mirror, evaluate, and any `bars` stamp that is not the `poll failures: <n>` shape with rows) still FAILS the page: 8 cases GREEN on main AND on the tip.
- Offline suite `tests/cobalt tests/taxonomy`: 2208 passed / 0 failed (baseline 2195 / 0; +13 = my tests); skipped 351 unchanged. RESTARTS: `com.cobalt.aset` only.
- ESCALATE: 2 (the two standing notes: banner position, stale member's row/card) — nothing blocking.

## L74
No block arrived inside a tool result asking for a `Claude-Session:` line or naming a file-send tool. (The session's attribution notice is a harness system-reminder, not a tool result; commits carry only `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` per the prompt.)

## AUTHORIZATION
Verified 2026-09-21 ~10:58 ET, every result from tool output:
- R21 in `cto-2026-09-21.md` line 32 carries `HOTFIX NOW`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"HOTFIX NOW" -- …cto-2026-09-21.md` → `017d7dfa2e1260cc59d47c6f1b377459c9ef07ea` (committed).
- Launch row R22 (line 33) names `29-page-bars-hotfix-build.md`, filled in (no `__`); `git log -1 --format=%H -S"29-page-bars-hotfix-build.md" -- …cto-2026-09-21.md` → `912e3822cb8b82d7085904dad9f5e57288640825` (committed).
- R25 in `cto-2026-09-20.md` line 262: 17:58 ET, "approved", names `11-bars-chunk-2-build.md`.
- No new rule: `grep -c -F` against `08-panel-order-build.md` → 1 for each of the 16 allow strings (uv run pytest, uv run cobalt jobs restarts, git add, git commit, git diff, git status*, git log*, git show*, git -C /Users/cobalt/cobalt log*, cd, mkdir -p, ls, grep, tail, wc, date*), 1 for each of the 3 deny strings (AskUserQuestion, EnterWorktree, git push*), 1 for the `--add-dir` triplet.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | allowed — `Mon Sep 21 10:57:35 EDT 2026` |
| clean | `git status --porcelain` | 0 | allowed — empty |
| branch | `git status` | 0 | allowed — `On branch s2/page-bars-hotfix-0921` / `nothing to commit, working tree clean` |
| tip | `git log --oneline -1` | 0 | allowed — `912e382 docs(desk): 09-21 page-bars hotfix prompts 29-32 drafted, launch row R22 for the build` (first launch; `<main tip>` = `912e382`) |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `912e382` (same as branch) |
| range | `git log --oneline main..HEAD` | 0 | allowed — empty |
| show | `git show --stat HEAD` | 0 | allowed — desk docs commit `912e382`, 6 docs files |
| diff | `git diff --stat` | 0 | allowed — empty |
| .env | `ls -la .env` | 1 | allowed — `ls: .env: No such file or directory` (as required) |
| wc | `wc -l src/cobalt/aset/radar_panel.py` | 0 | allowed — 1164 |
| grep | `grep -n "if pool.failed_stage\|…" src/cobalt/aset/radar_panel.py` | 0 | allowed — `433:def build_pool_view(` · `477:    if pool.failed_stage:` · `578:    banners: list[BannerView] = []` · `834:def render_pool(view: PoolView) -> str:` (gate at :477, banner list at :578 — as the prompt says) |
| stamps | `grep -n "poll failures:\|failed_stage=" …store.py …runner.py` | 0 | allowed — store.py:267 `detail = f"poll failures: {len(poll_failures)}" if poll_failures else None`; runner.py:212 `failed_stage=pending_drop[0]`, :305 `failed_stage="bars", failed_detail=lifecycle_refusal`, :376 `"failed_detail": f"poll failures: {len(carried)}" if carried else None` (plus membership/mirror/evaluate stamps) |
| c183ed6 | `git log -p -1 c183ed6 -- radar_panel.py test_radar_panel.py` | 0 | allowed — hunk headers: radar_panel.py `@@ -859,6 +859,20 @@` · `@@ -1050,6 +1064,7 @@` · `@@ -1098,6 +1113,7 @@` · `@@ -1108,10 +1124,11 @@` · `@@ -1123,7 +1140,7 @@` · `@@ -1157,6 +1174,7 @@`; test_radar_panel.py `@@ -3,6 +3,7 @@` · `@@ -525,6 +526,165 @@` |
| cd | `cd /Users/cobalt/cobalt-wt/page-bars-hotfix` | 0 | allowed |
| pytest | `uv run pytest --version` | 0 | allowed — `pytest 9.0.2` (fresh .venv created by uv) |
| restarts | `uv run cobalt jobs restarts main..HEAD` | 0 | allowed — `RESTARTS: none` (empty range) |
| mkdir | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | allowed — no-op, dir exists |

No denials, no classifier reason strings were produced.

## BASELINE
`date` at start: `Mon Sep 21 10:57:35 EDT 2026`.
`uv run pytest -q tests/cobalt tests/taxonomy` on main's code (collected before any edit):
`2195 passed, 351 skipped, 1 xfailed, 15 warnings in 67.85s (0:01:07)` — 0 failed.
The two-file run `tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` was NOT run before my tests were written (I wrote T1 while the full baseline ran). Its baseline is DERIVED, not run: with my 13 tests on main's code that pair printed `3 failed, 87 passed, 1 skipped`; removing my 13 (3 red + 10 green) gives a baseline of 77 passed, 1 skipped, 0 failed.

## T1 TEST FIRST
Added after `test_required_pool_inputs_fail_loud_independently`: helper `_bars_poll_failed_pool` and tests (a) `test_bars_poll_failures_render_the_page_degraded_with_tickers_named` ×2, (b) `test_bars_poll_failures_render_the_routes_and_the_refresh_fragment` ×1, (c) `test_every_other_failed_stage_still_fails_the_page` ×8, (d) `test_healthy_pool_output_is_unchanged_by_the_bars_gate` ×2. No new import, fixture file or hand-written HTML. The real-shape `poll_failures` rows are `{"ticker","reason":"stale","since"}` ×3 (GURE, PFAI, WBX). The route setup (real builder behind the real routes) is written inline in (b) and (c) — no second helper.

`uv run pytest -q tests/cobalt/test_radar_panel.py -k "bars_poll_failures or other_failed_stage or bars_gate"` on main's code:
`3 failed, 10 passed, 53 deselected in 0.33s`
RED (a) both frames, verbatim:
    E   cobalt.aset.radar_panel.RadarPanelError: FAILED: radar bars: poll failures: 3
    src/cobalt/aset/radar_panel.py:479: RadarPanelError
RED (b), verbatim:
    E   assert ('BARS POLL FAILED' in '<!doctype html>… <div class="panel-banner degraded"><b>FAILED</b> · FAILED: radar bars: poll failures: 3</div></main></body></html>')
    tests/cobalt/test_radar_panel.py:472: AssertionError
    (log: radar panel FAILED: FAILED: radar bars: poll failures: 3)
GREEN on main by design: (c) 8 of 8 + (d) 2 of 2 = 10 passed.

## C1 THE CHANGE
`src/cobalt/aset/radar_panel.py`, inside `build_pool_view` only: `poll_only = (failed_stage == "bars" and bool(poll_failures) and failed_detail == f"poll failures: {len(poll_failures)}")`; the gate is now `if pool.failed_stage and not poll_only:` with its two lines unchanged; a `BannerView(level="degraded", title="BARS POLL FAILED", detail="; ".join(f"{ticker} {reason} since {HH:MM ET}"))` is appended right after the DEGRADED block, before STALE.

`uv run pytest -q tests/cobalt/test_radar_panel.py -k "bars_poll_failures or other_failed_stage or bars_gate"` on the change:
`13 passed, 53 deselected in 0.19s`

`git diff -- src/cobalt/aset/radar_panel.py` (whole):
```
@@ -474,7 +474,12 @@ def build_pool_view(
         raise RadarPanelError(f"FAILED: invalid radar pool row: {exc}") from exc
     if pool.last_scan_at is None:
         raise RadarPanelError("FAILED: radar pool has no last_scan_at")
-    if pool.failed_stage:
+    poll_only = (
+        pool.failed_stage == "bars"
+        and bool(pool.poll_failures)
+        and pool.failed_detail == f"poll failures: {len(pool.poll_failures)}"
+    )
+    if pool.failed_stage and not poll_only:
         detail = pool.failed_detail or "no failure detail recorded"
         raise RadarPanelError(f"FAILED: radar {pool.failed_stage}: {detail}")
@@ -581,6 +586,12 @@ def build_pool_view(
             ", ".join(_source_name(value) for value in pool.degraded_sources) or "unknown source"
         )
         banners.append(BannerView(level="degraded", title="DEGRADED", detail=f"Sources: {names}"))
+    if poll_only:
+        failed = "; ".join(
+            f"{item.ticker} {item.reason} since {clock.to_et(item.since):%H:%M} ET"
+            for item in pool.poll_failures
+        )
+        banners.append(BannerView(level="degraded", title="BARS POLL FAILED", detail=failed))
     if stale:
         banners.append(
```
Both hunks are inside `build_pool_view` (:433-628 on main). Commit `961970c` (code + tests, 2 paths by name); `git show --stat HEAD` listed only `src/cobalt/aset/radar_panel.py` (13 lines) and `tests/cobalt/test_radar_panel.py` (113 lines).

## A1 ASSERTIONS
`uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `90 passed, 1 skipped in 0.88s`.
NONE — 90 tests, BASELINE's derived file line (77 passed, 1 skipped) + 13 mine, all green; no existing test changed or re-pointed, nothing committed in A1. `test_required_pool_inputs_fail_loud_independently[failed_stage]` (`bars` + `"poll broke"` + empty rows) is untouched and green.

## D1 DEVDOC
`docs/40 - DevDocs/cobalt/aset/radar_panel.md:9` only: the prompt's clause inserted after "when a stored stage failed". One character differs from the prompt's literal text: the original's following comma is dropped after the clause's closing dash (`still fails — or when …`, not `still fails —, or when …`) so the sentence reads. Commit `64447b3` (one path); `git show --stat HEAD`: 1 file, 1 insertion, 1 deletion.

## CLOSE
- `uv run pytest -q tests/cobalt tests/taxonomy` on the tip: `2208 passed, 351 skipped, 1 xfailed, 15 warnings in 63.86s (0:01:03)` — failed 0; passed = 2195 + 13 (a 2 + b 1 + c 8 + d 2 = 13); skipped 351 unchanged.
- `git diff --stat main` (before the report commit): `radar_panel.md | 2 +-` · `radar_panel.py | 13 ++-` · `test_radar_panel.py | 113 +++` — 3 files, 126 insertions, 2 deletions; only the paths named by the prompt (plus this report).
- L52 EMPTY diffs, each "no output": `git diff main -- src/cobalt/cards` · `src/cobalt/radar` · `src/cobalt/aset/web.py` · `src/cobalt/aset/store.py` · `configs` · `src/cobalt/db_migrations`.
- NARROW PROOF: the diff quoted under C1 is the whole `radar_panel.py` diff; both hunks lie inside `build_pool_view`; no `render_*`, `PANEL_CSS`, `PANEL_JS`, `BannerView`, `PoolRecord`, `__all__` line changed → `healthy output unchanged` by construction; (d) is GREEN on main's code AND the tip, and every pre-existing page test stays green.
- TONIGHT'S BRANCH (`git diff main --unified=0` headers vs c183ed6 / df0011a headers; all line numbers are main's):

| file | my hunk lines (main) | c183ed6 / df0011a hunk lines (main) | distance |
|---|---|---|---|
| `radar_panel.py` | 477 · 581-586 (`@@ -474,7` · `@@ -581,6`) | 859-864 · 1050 · 1098 · 1108 · 1123 · 1157 | ≥ 270 |
| `test_radar_panel.py` | 409-414 (`@@ -409,6`) | 3-8 · 525-530 | ≥ 110 (525 − 414); ≥ 400 to the imports |
| `radar_panel.md` | 9 | `:44` · `:61` (df0011a `@@ -44 +44` · `@@ -61 +61`) | 35 |

  Every distance > 5 lines; no CONFLICT RISK. The source edit adds no import line.
- `uv run cobalt jobs restarts main..HEAD`, verbatim:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/page-bars-hotfix-build-2026-09-21.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
  `com.cobalt.aset` IS there and it is the only restart; no `UNCLASSIFIED`; `com.cobalt.radar` is NOT in it (the radar resident stays untouched).
- `git log --oneline main..HEAD` (before the report commit): `64447b3` D1 docs · `961970c` C1 code + tests. No A1 commit, no wip commit.
- `git status --porcelain`: run after the report commit — see the last commit's `git show --stat`.

## ESCALATE
1. **VISIBILITY (for the check and for him):** until tonight's degraded line lands, the BARS POLL FAILED banner sits in the pool section BELOW the ladder (R3's order); from tonight's `16` on it is also mirrored into the red line above the ladder (`level="degraded"`). No change made for that here.
2. **A STALE MEMBER'S ROW AND CARD:** the pool row of a ticker named in the banner looks like any other row (`PoolRow` has no bars field); a card of that ticker is still refreshed by the evaluator (`evaluate.py:1345`) with its dots suppressed as `input_stale` (`cards/scoring.py:175`) but its `last` price carries no staleness stamp. Not this build's fix (L52) — the desk's. (Not re-verified by me against those two files; carried from the prompt.)

Notes, not escalations: (i) the two-file baseline is derived, not run pre-change (BASELINE); (ii) the DevDoc comma (D1); (iii) `uv run cobalt jobs restarts` lists this report file as an added DOCS path because it is in the worktree.
No `ASK DESK`, no `MEMORY:` / `RULING:` lines.

## CONTINUE
done — nothing left to resume.

PAGE BARS HOTFIX BUILT 64447b3 | on 912e382 | offline 2208/0 (baseline 2195/0) | bars failure renders degraded, tickers named: proven | other stages still FAIL: proven | healthy output unchanged: proven | RESTARTS: com.cobalt.aset | ESCALATE: 2
