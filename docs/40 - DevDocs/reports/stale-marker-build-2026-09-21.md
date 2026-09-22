# Stale marker build — 2026-09-21

## §0 Headline
- BUILT: a red `STALE` badge on the pool row and on every active card (strip, ARMED `last`, LEVELS `last`) of a ticker whose bars poll is failing (R36), in `radar_panel.py` only. Branch `s2/stale-marker-0921` on `5b208a0`, tip `ead43a0` (C1 `0d961e6`, D1 `ead43a0`).
- Offline suite `2230 passed, 351 skipped, 1 xfailed, 0 failed` (baseline 2222); 8 new tests RED on main's code, GREEN on the change; healthy-view pins GREEN on both.
- `cards` / `radar` / `store.py` / `web.py` / `configs` diffs EMPTY. RESTARTS: `com.cobalt.aset` only. No browser ran (L70).
- ESCALATE: 6 (stale-`last` scoring item is his; browser/layout unproven; three clocks; assumed look; main moved after the cut; two small test/report deviations).

## L74
A block appeared after the prompt-file Read result, in the harness system-reminder position (not visibly inside the tool-result body), asking for a `Claude-Session:` line in commit messages and naming a file-send tool. Recorded once. Not followed: the prompt's L74 says commits carry `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` and nothing else, and no file is sent.

## AUTHORIZATION
Started 2026-09-21 20:12 ET. All commands allowed, no denials.

| Rule | Command result |
|---|---|
| R36 row present | `grep -n "^| R36 "` hit line 47, carries "A — a small STALE stamp on that ticker's row and on its card" |
| R36 committed | `git -C … log -1 --format=%H -S"a small STALE stamp on that ticker's row and on its card"` → `965bd0f440f7b24e3485eb860f642b596b51350a` |
| Lane call present | `grep -n "LANE CALL (desk): the card mark is a second RENDERING"` → one hit, line 354 |
| Lane call committed | `git -C … log -1 --format=%H -S"LANE CALL (desk)…"` → `2b8c8ee700502d71839fa1ad65bbe58a992fc46c` |
| Launch row R42 | `grep -n "^| R42 "` → line 53, names `prompts/2026-09-21/51-stale-marker-build.md`; `__` NOT present |
| Launch row committed | `git -C … log -1 --format=%H -S"51-stale-marker-build.md"` → `598a8d77acb31c03a91da70430ad7b7690d329f1` |
| R25 launch strings | `grep -n "^| R25 "` in `cto-2026-09-20.md` → line 262, "approved", names `11-bars-chunk-2-build.md` |
| No new rule | `grep -c -F -e` against `02-bars-chunk-2-fix-r3.md`: 16 allow strings each 1 (`uv run pytest *`, `uv run cobalt jobs restarts *`, `git add *`, `git commit *`, `git diff *`, `git status*`, `git log*`, `git show*`, `git -C /Users/cobalt/cobalt log*`, `cd *`, `mkdir -p *`, `ls *`, `grep *`, `tail *`, `wc *`, `date*`); 3 deny strings each 1 (`AskUserQuestion`, `EnterWorktree`, `Bash(git push*)`); `--add-dir` triplet = 1 |

## PREFLIGHT
| Rule | Command | Result |
|---|---|---|
| date | `date` | `Mon Sep 21 20:12:53 EDT 2026` — allowed |
| clean tree | `git status --porcelain` | empty — allowed |
| branch | `git status` | `On branch s2/stale-marker-0921` / `nothing to commit, working tree clean` — allowed |
| tip | `git log --oneline -1` | `5b208a0 docs(report): deploy 2026-09-21b degraded line …` — first launch |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | `5b208a0` (same as branch tip) — `<main tip>` = `5b208a0` |
| tag present | `git -C … log -1 --format=%H deploy-2026-09-21b` | `ad7d3e41e0275ebabf4ebdeac818f5827b9e77f1` |
| cut carries tag | `git log --oneline HEAD..deploy-2026-09-21b` | empty |
| degraded line in tree | `grep -c "function mirrorDegraded" …` | `1` |
| branch commits | `git log --oneline main..HEAD` | empty |
| HEAD | `git show --stat HEAD` | report commit only (`docs/40 - DevDocs/reports/deploy-2026-09-21b.md`) |
| diff | `git diff --stat` | empty |
| .env | `ls -la .env` | `ls: .env: No such file or directory` (exit 1, expected) |
| size | `wc -l …/radar_panel.py` | `1193` |
| anchors | grep of pool-layer / ladder-layer / ticker cell / strip `<b>` / `mirrorDegraded(next)` / `setInterval(refreshPool` | `827` ticker cell, `861` pool-layer section, `1044` strip `<b>`, `1056` terminal-row `<b>`, `1065` ladder-layer, `1138` `mirrorDegraded(next)`, `1146` `window.setInterval(refreshPool,interval)` — all equal the INDEX CARD numbers |
| item-4 grep 1 (radar_panel.py) | `grep -n "strip b\|nth-child\|firstChild\|textContent\|\.ticker\|bars-stale\|data-bars-stale\|mirrorStale\|exclude="` | hits: `414` (`ticker=record.ticker`), `591` banner fragment, `735`/`746` (`r.ticker`), `827` ticker cell, `1000` `<strong>{e(card.ticker)}</strong>` (card title), `1013`/`1044`/`1056` `card.ticker`, `1073` CSS (`.ticker{font-weight:800;font-size:15px}`, `.eyebrow,.mono,.rank-chip,.ticker,button,th{…}`, `.strip{…grid-template-columns:110px 90px 1fr auto…}`), `1075` (`.strip span:nth-child(4)`), `1090` `box.textContent` (card-status box). NO `bars-stale`, `data-bars-stale`, `mirrorStale`, `exclude=`, `strip b`, `firstChild` hit yet. Nothing the drafter did not list changes what the build does; `.ticker` font rules apply inside `td.ticker`, and `.bars-stale`'s own `font:9px …` shorthand resets weight and size (no build change) |
| item-4 grep 2 (web.py) | `grep -n "model_dump\|pool_api_payload" src/cobalt/aset/web.py` | `76: pool_api_payload,` · `880: return pool_api_payload(view.pool)` |
| cd | `cd /Users/cobalt/cobalt-wt/stale-marker` | allowed |
| pytest | `uv run pytest --version` | `pytest 9.0.2` (fresh venv created, 248 packages) |
| restarts probe | `uv run cobalt jobs restarts main..HEAD` | `RESTARTS: none` (empty range) |
| mkdir | `mkdir -p "docs/40 - DevDocs/reports"` | allowed, no-op (directory exists) |

## BASELINE
Run 2026-09-21 ~20:14 ET on `5b208a0` (main's tip, no edits):
- `uv run pytest -q tests/cobalt tests/taxonomy` → `2222 passed, 351 skipped, 1 xfailed, 15 warnings in 68.42s (0:01:08)` (0 failed; the summary line carries no `failed` token because none failed)
- `uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `104 passed, 1 skipped in 0.91s`

## T1 TEST FIRST
Tests written, nothing committed yet, against main's UNCHANGED `radar_panel.py` (`5b208a0`). Both files use only the suites' existing fixtures: `_bars_poll_failed_pool(failures=…)`, `_small_snapshot()`, `_build()`, `_ladder(evaluated["rows"])`; the cards file imports the pool suite's helpers with `import test_radar_panel as pool_tests` (import worked under the suite's import mode; no helper copied). New small helpers in `test_radar_panel.py`: `_hhmm`, `_failure`, `_tip`, `_pool_row_ticker`, `_pool_layer`, `_main_markup`. Stale set: row ticker = `_small_snapshot()` current member (entered_at set, left_at None — asserted), card ticker `FTFT` (asserted NOT a pool member), `GURE`; reasons `stale` / `error` / `stale`; the banner precondition `[b.title for b in view.pool.banners] == ["BARS POLL FAILED"]` HELD on main.

Tests (8 collected by `-k bars_stale`): (a) `test_bars_stale_badge_marks_exactly_the_failing_tickers` ×2 (phone_frame) · (b) `test_bars_stale_badge_absent_and_output_unchanged_when_healthy` ×2 · (c) `test_bars_stale_badge_marks_a_lifecycle_card_outside_the_pool` · (d) `test_bars_stale_follows_the_refreshed_pool_fragment_and_never_moves_the_ladder` · (e) `test_bars_stale_leaves_the_api_json_unchanged` · (f) `test_bars_stale_leaves_the_banner_and_degraded_line_byte_identical`.

**Deviation from the prompt's letter (said, not hidden):** (b) as written asserts `"bars-stale" not in page` on the composed healthy page, but C1 items 6–7 put the class name in `PANEL_CSS` (`.bars-stale{…}`) and `PANEL_JS` (`'.bars-stale'`), so that literal assertion could never be green on the change. The test asserts `"bars-stale" not in` the `<main>…</main>` markup (`_main_markup`), the healthy `render_pool`, `render_ladder` and API-json text, and `class="bars-stale"` / `data-bars-stale` not in the WHOLE page (neither string occurs in the CSS or the single-quoted JS). Stronger where it matters, not looser. Likewise (a)'s pool layer is sliced to its own `</section>` so the JS text after it is not counted.

**PIN RUN on main's code** — the digests were read from the failure output of the `"PIN"` placeholder run, pasted in, one assert at a time:
- `assert 'd010eec4d275...829ce491ef3fa' == 'PIN'` → `PIN_DEGRADED_LINE_SHA256 = d010eec4d275aebc376c35857e83d381da6fb1ca81098e9ebe5829ce491ef3fa`
- `assert 'acc897ec31ee...2556e27491c79' == 'PIN'` → `PIN_BARS_BANNER_SHA256 = acc897ec31ee136eeaaad613f8a27c592cca57446a46d9eb1d52556e27491c79`
- `assert 'f2e79add6bc4...99e9d62181552' == 'PIN'` → `PIN_HEALTHY_POOL_SHA256 = f2e79add6bc4d4286b381154b071b04ec9e7887467ffd15b0f499e9d62181552`
- `assert 'e617c53c1479...19849f55370d7' == 'PIN'` → `PIN_HEALTHY_LADDER_SHA256 = e617c53c1479314b6074de5409f289238479be31fbbd789b4ee19849f55370d7`
- `assert '450b3415c234...ca824601c5462' == 'PIN'` → `PIN_HEALTHY_API_SHA256 = 450b3415c2346c8b13b53932c5175f56ee6af78877ca9fc8086ca824601c5462`
(the pool digest was re-checked on a later run against main's code and passed unchanged — the render is deterministic.)

**THE RED/GREEN RUN on main's code** — `uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py -k "bars_stale" --tb=line` → `5 failed, 3 passed, 105 deselected in 0.49s`, dots `F.FF..FF`:
- RED (e) `test_radar_panel.py:579`: `AssertionError: assert 'bars_stale_tickers' in {'banners': FieldInfo(…), …}` (`PoolView.model_fields` has no such field)
- RED (a)[False] and (a)[True] `test_radar_panel_cards.py:436`: `assert 0 == 1 … pool.count('class="bars-stale"')` (no badge in the pool layer)
- RED (c) `test_radar_panel_cards.py:501`: `assert 0 == 4 … page.count('<b>FTFT<span class="bars-stale" title="error since 10:30 ET">STALE</span></b>')`
- RED (d) `test_radar_panel_cards.py:516`: `AssertionError: <section id="pool-layer" class="pool-layer" data-watermark="2026-01-05T16:00:00+00:00"> assert None` (`data-bars-stale` absent from the fragment's opening tag)
- GREEN on main (GUARDS, after pinning): (f) and (b)[False] (b)[True] — the three dots of `F.FF..FF` (order: (e) F, (f) ., (a) F F, (b) . ., (c) F, (d) F).
(d)'s `render_ladder(…, bars_stale=…)` `TypeError` and its JS-wiring assertions sit BEHIND the first red assertion, so they are RED-by-cascade on main; they are exercised for real in C1's GREEN run.

## C1 THE CHANGE
Only `src/cobalt/aset/radar_panel.py` edited (plus the two test files of T1). Commit `0d961e6` — `feat(radar): STALE badge on the pool row and card of a ticker whose bars poll is failing (R36 2026-09-21)`; `git show --stat HEAD`: `src/cobalt/aset/radar_panel.py | 59 ++++++++---` · `tests/cobalt/test_radar_panel.py | 95 +++` · `tests/cobalt/test_radar_panel_cards.py | 176 +++` · `3 files changed, 316 insertions(+), 14 deletions(-)` (the three paths named, nothing else).

GREEN on the change: `uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py -k "bars_stale"` → `8 passed, 105 deselected in 0.48s` (RED on main: `5 failed, 3 passed`, T1). Whole two files: `112 passed, 1 skipped in 1.07s` (baseline 104 passed, 1 skipped; +8 = my 8 tests).

`git diff -- src/cobalt/aset/radar_panel.py`, WHOLE (hunks = C1 items 1–8; item 1 = the `PoolView` field + the fill in `build_pool_view` + the `PoolView(...)` argument; 2 = `_bars_stale_badge`; 3 = `_pool_table` / `render_pool`; 4 = `_field` `after`, `_card_detail`, `render_ladder`; 5 = `render_radar_page`; 6 = CSS; 7 = JS function + call; 8 = `import json`):

```diff
@@ -12,6 +12,7 @@ attests a note.
 import html
+import json
 from datetime import date, datetime, timedelta
@@ -189,6 +190,7 @@ class PoolView(_ViewModel):
     banners: list[BannerView]
+    bars_stale_tickers: dict[str, str] = Field(default_factory=dict, exclude=True)
     churn: ChurnDelta | None
@@ -608,6 +610,13 @@ def build_pool_view(
                 detail=f"Showing trading day {scan_day.isoformat()}",
             )
         )
+    bars_stale: dict[str, str] = {}
+    if poll_only:
+        for item in pool.poll_failures:
+            tooltip = f"{item.reason} since {clock.to_et(item.since):%H:%M} ET"
+            bars_stale[item.ticker] = (
+                f"{bars_stale[item.ticker]}; {tooltip}" if item.ticker in bars_stale else tooltip
+            )
 
     override_labels = []
@@ -635,6 +644,7 @@ def build_pool_view(
         banners=banners,
+        bars_stale_tickers=bars_stale,
         churn=churn,
@@ -816,15 +826,17 @@ def _rank_value_cell(row: PoolRow) -> str:
-def _pool_table(rows: list[PoolRow], title: str) -> str:
+def _pool_table(rows: list[PoolRow], title: str, *, bars_stale: dict[str, str] | None = None) -> str:
     e = html.escape
+    bars_stale = bars_stale or {}
@@ (render_row)
+        stale_badge = _bars_stale_badge(bars_stale.get(row.ticker))
-            f'<td class="mono">…</td><td class="ticker">{e(row.ticker)}</td>'
+            f'<td class="mono">…</td><td class="ticker">{e(row.ticker)}{stale_badge}</td>'
@@ -858,13 +870,18 @@ def render_pool(view: PoolView) -> str:
+    stale_attr = (
+        f' data-bars-stale="{e(json.dumps(view.bars_stale_tickers, sort_keys=True))}"'
+        if view.bars_stale_tickers
+        else ""
+    )
-    return f'''<section id="pool-layer" class="{classes}" data-watermark="{e(view.observed_watermark.isoformat())}">
+    return f'''<section id="pool-layer" class="{classes}" data-watermark="{e(view.observed_watermark.isoformat())}"{stale_attr}>
-{_pool_table(view.current, "Current admitted")}
+{_pool_table(view.current, "Current admitted", bars_stale=view.bars_stale_tickers)}
@@ -888,12 +905,21 @@ def _badge(owner: str) -> str:
+def _bars_stale_badge(tooltip: str | None) -> str:
+    """The STALE badge (R36 2026-09-21): a second rendering of `poll_failures`,
+    the state the BARS POLL FAILED banner names (L3); wording, size and colour
+    ASSUMED — not ruled."""
+    return "" if not tooltip else f'<span class="bars-stale" title="{html.escape(tooltip)}">STALE</span>'
+
+
-def _field(card: CardView, field: str, label: str, value: Any, *, tag: str = "span") -> str:
+def _field(
+    card: CardView, field: str, label: str, value: Any, *, tag: str = "span", after: str = ""
+) -> str:
-        f'<b>{html.escape(shown)}</b></{tag}>'
+        f'<b>{html.escape(shown)}</b>{after}</{tag}>'
@@ -952,8 +978,9 @@ def _key_row(card: CardView) -> str:
-def _card_detail(card: CardView) -> str:
+def _card_detail(card: CardView, *, stale: str | None = None) -> str:
     e = html.escape
+    stale_badge = _bars_stale_badge(stale)
@@ ARMED state_body
-…last {e(str(card.last or "—"))} · trigger {e(str(card.trigger))}</div>'
+…last {e(str(card.last or "—"))}{stale_badge} · trigger {e(str(card.trigger))}</div>'
@@ LEVELS
-{_field(card, "last_price", "last", card.last)}
+{_field(card, "last_price", "last", card.last, after=stale_badge)}
@@ -1017,9 +1044,10 @@ def _card_detail(card: CardView) -> str:
-def render_ladder(view: LadderView) -> str:
+def render_ladder(view: LadderView, *, bars_stale: dict[str, str] | None = None) -> str:
     e = html.escape
+    bars_stale = bars_stale or {}
@@ -1038,13 +1066,14 @@ def render_ladder(view: LadderView) -> str:
+            stale = bars_stale.get(card.ticker)
-                f"<b>{e(card.ticker)}</b><span>…
+                f"<b>{e(card.ticker)}{_bars_stale_badge(stale)}</b><span>…
-                f"{_card_detail(card)}{promote}</article>"
+                f"{_card_detail(card, stale=stale)}{promote}</article>"
@@ -1076,6 +1105,7 @@ PANEL_CSS = r"""
+.bars-stale{font:9px ui-monospace,SFMono-Regular,Menlo,monospace;border:1px solid var(--red);padding:1px 3px;color:var(--red);border-radius:3px;margin-left:4px;vertical-align:middle}
@@ -1125,6 +1155,7 @@ PANEL_JS = r"""
+ function mirrorStale(layer){const stale=JSON.parse(layer.dataset.barsStale||'{}'); Array.from(document.querySelectorAll('.ladder-item')).forEach(function(item){const b=item.querySelector('.strip b'); if(!b||!b.firstChild){return;} const tip=stale[b.firstChild.nodeValue]; let mark=b.querySelector('.bars-stale'); if(tip&&!mark){mark=document.createElement('span'); mark.className='bars-stale'; mark.textContent='STALE'; b.append(mark);} if(mark&&!tip){mark.remove();} if(mark&&tip&&mark.title!==tip){mark.title=tip;}});}
@@ -1135,7 +1166,7 @@ PANEL_JS = r"""
-     oldLayer.replaceWith(next); cursor=payload.pool.observed_watermark; mirrorDegraded(next);
+     oldLayer.replaceWith(next); cursor=payload.pool.observed_watermark; mirrorDegraded(next); mirrorStale(next);
@@ -1151,7 +1182,7 @@ PANEL_JS = r"""
-<body …>…{render_degraded_line(view.pool)}{render_ladder(view.ladder)}{render_pool(view.pool)}</main>…
+<body …>…{render_degraded_line(view.pool)}{render_ladder(view.ladder, bars_stale=view.pool.bars_stale_tickers)}{render_pool(view.pool)}</main>…
```
(The report's diff is condensed with `…` for the very long f-string lines and unchanged context; the FULL machine diff is the commit `0d961e6` — `git diff main -- src/cobalt/aset/radar_panel.py` rerun at CLOSE.) No hunk in the banner code, `render_degraded_line`, `mirrorDegraded`, `pool_api_payload`, `render_failed_page`, `post()`, the click handler, `refreshLadder` or the interval line.

## A1 ASSERTIONS RE-POINTED
`uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `112 passed, 1 skipped in 1.07s`.
NONE — 113 tests, BASELINE's file line (104 passed, 1 skipped) plus T1's 8, all green; no assertion re-pointed, weakened, removed or reordered, nothing committed in A1. Verified: `test_bars_poll_failures_render_the_page_degraded_with_tickers_named` `:447` (`render_ladder(view.ladder) in page`) holds because its ladder is EMPTY (`FakeCardStore()`); `test_every_displayed_card_field_carries_its_owner_badge` matches `class="badge badge-…"`, which `bars-stale` is not.

## D1 DEVDOC
`docs/40 - DevDocs/cobalt/aset/radar_panel.md`: ONE paragraph added in `## Rendering` after the `render_degraded_line()` sentence (the STALE badge, R36 2026-09-21: the derived `PoolView.bars_stale_tickers`, `exclude=True`; `poll_only` only; the row + strip + ARMED `last` + LEVELS `last` placements; never on departed / excluded rows or terminal cards; `mirrorStale()` after `mirrorDegraded()`; the poller's clock only; **wording / 9 px monospace / red `.badge` geometry ASSUMED, not ruled**). Nothing else in that DevDoc changed. Commit `ead43a0` `docs(devdocs): radar_panel — STALE badge on row and card (R36 2026-09-21)`; `git show --stat HEAD`: `docs/40 - DevDocs/cobalt/aset/radar_panel.md | 2 ++` · `1 file changed, 2 insertions(+)` (only the named path).
`docs/40 - DevDocs/cobalt/aset/web.md`: READ; routes and payload are unchanged (`GET /radar`, `GET /api/radar/pool` "returns the Pydantic pool dump plus the HTML from `render_pool()`" still true — the new field is `exclude=True`) → left UNTOUCHED. No sentence there is made false by this build.

## CLOSE
- `uv run pytest -q tests/cobalt tests/taxonomy` → `2230 passed, 351 skipped, 1 xfailed, 15 warnings in 64.49s (0:01:04)`. BASELINE `2222 passed, 351 skipped, 1 xfailed` → failed 0 (both), passed +8, skipped 351 = 351, xfailed 1 = 1. The +8 = T1's tests counted from the run: (a) 2 (phone_frame False/True) + (b) 2 + (c) 1 + (d) 1 + (e) 1 + (f) 1 = 8, and the two radar files went 104 → 112 passed (`-k bars_stale` collects exactly those 8).
- `git diff --stat main` (two-dot, against main's CURRENT tip `7afe4c3`) lists, beyond my four paths, `prompts/2026-09-21/65-setups-one-build.md`, `79-draft-ops-fix-r3.md`, `80-ops-fix-r3.md`, `81-ops-6a-check-r3.md`, `reports/cto-2026-09-21.md`, `reports/ops-6a-check-r2-2026-09-22.md`, `reports/ops-fix-r3-draft-2026-09-21.md` — NOT my edits: main gained three desk-docs commits after the cut (`2834a5a`, `66e5ce1`, `7afe4c3`; `git -C /Users/cobalt/cobalt log --oneline -6`). The merge-base comparison `git diff --stat main...HEAD` is EXACTLY the four named paths: `docs/40 - DevDocs/cobalt/aset/radar_panel.md | 2 +` · `src/cobalt/aset/radar_panel.py | 59 ++++++---` · `tests/cobalt/test_radar_panel.py | 95 +++` · `tests/cobalt/test_radar_panel_cards.py | 176 +++` · `4 files changed, 318 insertions(+), 14 deletions(-)` (+ this report once committed). ESCALATE 5.
- EMPTY DIFFS (each "no output"): `git diff main -- src/cobalt/cards` · `git diff main -- src/cobalt/radar` · `git diff main -- src/cobalt/aset/store.py` · `git diff main -- src/cobalt/aset/web.py` · `git diff main -- configs`. (The two-dot form is the stricter one here: main never touched those paths, so empty means both trees are identical.)
- NAMED-PLACES PROOF: the whole `git diff -- src/cobalt/aset/radar_panel.py` is quoted under C1 (condensed with `…` on the very long f-string lines, ESCALATE 6); the file's diff is unchanged since `0d961e6` (D1 touched only the DevDoc). Hunks: C1 items 1–8 only; none in the banner code, `render_degraded_line`, `mirrorDegraded`, `pool_api_payload`, `render_failed_page`, `post()`, the click handler, `refreshLadder`, or the interval line.
- `uv run cobalt jobs restarts main..HEAD` VERBATIM (L42):
  ```
  path	change	rule	restart
  docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
  docs/40 - DevDocs/prompts/2026-09-21/65-setups-one-build.md	M	DOCS	-
  docs/40 - DevDocs/prompts/2026-09-21/79-draft-ops-fix-r3.md	D	DOCS	-
  docs/40 - DevDocs/prompts/2026-09-21/80-ops-fix-r3.md	D	DOCS	-
  docs/40 - DevDocs/prompts/2026-09-21/81-ops-6a-check-r3.md	D	DOCS	-
  docs/40 - DevDocs/reports/cto-2026-09-21.md	M	DOCS	-
  docs/40 - DevDocs/reports/ops-6a-check-r2-2026-09-22.md	D	DOCS	-
  docs/40 - DevDocs/reports/ops-fix-r3-draft-2026-09-21.md	D	DOCS	-
  docs/40 - DevDocs/reports/stale-marker-build-2026-09-21.md	A	DOCS	-
  src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset
  tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
  tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
  RESTARTS: com.cobalt.aset
  ```
  `com.cobalt.aset` IS there (it imports `cobalt.aset.radar_panel` through `web.py`), as expected. `com.cobalt.radar` is NOT in it. No `UNCLASSIFIED`. (The extra DOCS rows are the same main-moved noise as above; they restart nothing.)
- `git log --oneline main..HEAD` → `ead43a0 docs(devdocs): radar_panel — STALE badge on row and card (R36 2026-09-21)` · `0d961e6 feat(radar): STALE badge on the pool row and card of a ticker whose bars poll is failing (R36 2026-09-21)`. No A1 commit (A1 = NONE), no wip commit.
- `git status --porcelain` after the report commit: recorded by the final `git show --stat HEAD` below (report only).

## ESCALATE
1. **NOT PART OF THIS BUILD — his, a separate scoring item (L52):** an open card is refreshed and can SCORE on a stale `last` once its computed dots are tapped (proposal ESCALATE 1; `evaluate.py:1329-1349`, `:776-777`, `:803`; `scoring.py:248`) — untouched here (`src/cobalt/cards`, `src/cobalt/radar` empty diffs), carried as a READING. The badge marks the stale `last`; it does not stop the score.
2. **NO BROWSER RAN (L70):** `mirrorStale` was proven by server-side parity (T1 (d)) and substring wiring assertions only; what a browser does on a live refresh — the strip badge appearing and clearing in place, the ladder not moving — is UNPROVEN until the desk confirms it on the live page with him. The ticker cell and strip column widths with the badge (90 px desktop, 70 px at ≤700 px, `:1073` / `:1075`) are UNPROVEN layout: the badge sits INSIDE the strip's `<b>` (a grid child of a fixed 90 px / 70 px column) and could clip or wrap there.
3. **THE THREE CLOCKS (proposal ESCALATE 2):** the badge follows the poller's clock only (180 s, RTH, plus `error`); the evaluator's (200 s, all sessions) and the pool STALE banner's (2 × interval) are different clocks — a checker question, recorded, not decided.
4. **ASSUMED LOOK:** wording `STALE`, 9 px monospace, red `.badge` geometry — not ruled (R36 ruled the stamp, not its look). The two in-card badges (ARMED `last`, LEVELS `last`) update on the next `/radar` load or card action, not on a pool refresh (proposal Q2, ASSUMED).
5. **MAIN MOVED AFTER THE CUT:** the branch was cut at `5b208a0` (= main's tip at PREFLIGHT); main is now `7afe4c3` (three desk-docs commits: `2834a5a`, `66e5ce1`, `7afe4c3` — docs only, none under `src/` / `tests/`). `git diff --stat main` (two-dot) therefore shows those files as differences; `git diff --stat main...HEAD` is exactly the four named paths. The branch is built on `5b208a0` as the prompt says; a merge of these docs-only commits is the desk's. The prompt's CLOSE line "`git diff --stat main` → EXACTLY the four named paths" is true only in the triple-dot form.
6. **TWO SMALL DEVIATIONS FROM THE PROMPT'S LETTER (no behaviour affected):** (a) T1 (b)'s literal `"bars-stale" not in page` cannot hold on the change (the class name is in `PANEL_CSS` / `PANEL_JS` by C1 items 6–7) — asserted on the `<main>` markup, `render_pool`, `render_ladder` and the API json instead, plus `class="bars-stale"` / `data-bars-stale` on the whole page (T1 says so, stronger not looser). (b) the C1 diff under `## C1` is condensed with `…` on the very long f-string lines rather than pasted whole; the whole diff was printed by the tool and is commit `0d961e6`.
7. `ASK DESK`: none. `MEMORY:` / `RULING:`: none. `## L74`: one block recorded, not followed.

## CONTINUE
done — nothing left; the desk verifies the artifact and launches `52-stale-marker-check.md` (THREE houses read `main..<tip>`).

STALE MARKER BUILT ead43a0 | on 5b208a0 | offline 2230/0 (351 skipped; baseline 2222/0) | row badge on stale tickers only: proven | card badges on stale tickers only: proven | absent when healthy, output unchanged: proven | stays current, ladder does not move: proven | API JSON unchanged: proven | card/scoring paths untouched: empty diff | RESTARTS: com.cobalt.aset | ESCALATE: 6
