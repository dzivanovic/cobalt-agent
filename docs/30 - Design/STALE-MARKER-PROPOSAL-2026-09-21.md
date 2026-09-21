# STALE MARKER — proposal (2026-09-21)

Proposer seat `stale-marker-design-0921` (Opus 5), read-only, from `prompts/2026-09-21/49-propose-stale-marker.md`.
Ruling this serves: `cto-2026-09-21.md` §4 R36, 16:06 ET, "A" — a small STALE stamp on a stale ticker's pool row and on its card; the `BARS POLL FAILED` banner stays. Ladder: `S2 · Radar panel (§5 host)` (row) + `F8 Card at precondition` (card).
All `file:line` are on MAIN at `965bd0f` unless a branch is named. PROVEN = read in the file; UNPROVEN = not checkable from reads (L70).

## 1. Fact base

| # | Claim | file:line | |
|---|---|---|---|
| F1 | Per-ticker staleness exists today as `radar_pool.poll_failures` (jsonb list of `{ticker, reason, since}`), one row per pool | `radar/store.py:185,194,201` | PROVEN |
| F2 | Two reasons only: `error` (fetch or upsert failed, any session) and `stale` (newest bar older than `radar.poll_bar_max_age_s`, RTH only) | `radar/poller.py:93,113,121-122` | PROVEN |
| F3 | The `stale` threshold is already his: `radar.poll_bar_max_age_s = 180`, "ruled 2026-09-14 (Dejan)". The stamp needs no new number (L53) | `configs/cobalt/taxonomy/tunables.yaml:513-520` | PROVEN |
| F4 | Lifetime: rewritten every S4 cycle; an entry is removed on its ticker's next good fetch or fresh bar; a ticker no longer polled is dropped; S2 carries the previous S4 outcome forward | `poller.py:66-81,116,124`; `store.py:268-273`; `runner.py:356-361,375-376,385` | PROVEN |
| F5 | Polled tickers = admitted pool members + departed tickers with an OPEN card (lifecycle polling), so a card's ticker can be in `poll_failures` with no current pool row | `runner.py:238-267` | PROVEN |
| F6 | The panel already reads it: `PoolRecord.poll_failures: list[PollFailure]` from the same `pool_row` read | `aset/radar_panel.py:67-75,93,464,472` | PROVEN |
| F7 | The page renders it only in the `poll_only` case (`failed_stage='bars'` + detail `poll failures: <n>`); every other failed stage fails the whole page, so no mark is ever needed there | `radar_panel.py:477-484` | PROVEN |
| F8 | The banner is built from exactly that list — `BARS POLL FAILED`, `"<ticker> <reason> since HH:MM ET"` | `radar_panel.py:589-594` | PROVEN |
| F9 | The ticker set is NOT carried out of `build_pool_view`: `PoolView` has no per-ticker field; `PoolRow` has none | `radar_panel.py:148-164,174-192` | PROVEN |
| F10 | **A pool row renders NO `last`/price cell.** Cells: rank · ticker · value (rank metric) · session · source · entered · left · excluded by. The R36 premise "row still shows `last`" is, for the row, "row looks like any healthy row" | `radar_panel.py:822-833,840-841` | PROVEN |
| F11 | A card shows `last` in two places: ARMED state block and the LEVELS detail; the strip shows score · ticker · setup · state/key/shares/stop | `radar_panel.py:967,997,1029-1032` | PROVEN |
| F12 | Card `last` = `radar_cards_v.last_price`, written by the S5 refresh; the ladder never reads the pool row | `radar_panel.py:250,707,748`; `radar/evaluate.py:803` | PROVEN |
| F13 | `build_radar_panel` holds BOTH views in one request — the card side can reach the ticker set with no new query | `radar_panel.py:787-800` | PROVEN |
| F14 | `render_radar_page` is the one place both renderers are called | `radar_panel.py:1134-1137` | PROVEN |
| F15 | Refresh: `refreshPool` replaces ONLY `#pool-layer` every `scan_interval` s; the ladder is re-fetched only after a card POST (`refreshLadder`), keeping open cards. A periodic refresh never moves the ladder today | `radar_panel.py:1077-1086,1093,1114-1129` | PROVEN |
| F16 | So a card stamp rendered server-side stays at its page-load value until a reload or a card action, unless the pool refresh mirrors it (as tonight's degraded line does) | `radar_panel.py:1129`; `s2/degraded-line-0921` `88602cc` `mirrorDegraded` | PROVEN |
| F17 | Write paths: `radar_panel.py` is read-only (docstring; no write call in the builders/renderers). No line a build touches is on a write path (L29) | `radar_panel.py:3-9` | PROVEN |
| F18 | A card does NOT FORM on stale bars: `input_stale` return before formation when intraday bars are older than 2 × `radar.scan_interval` (100 → 200 s) | `radar/evaluate.py:529-534,598-599`; `tunables.yaml:467-468` | PROVEN |
| F19 | An OPEN card IS REFRESHED on stale bars: no evaluation-state guard before `refresh_card`; it recomputes proximity from `ev.last_price` (last stored closed bar, else entry) and writes `last_price` | `evaluate.py:1329-1349,776-777,803` | PROVEN |
| F20 | Stale computed dots go `input_stale` and suppress `card_score` — UNLESS the trader tapped them: tapped dots are exempt from suppression, so a fully tapped card SCORES on a stale `last`, and the ladder orders WATCH by `card_score` | `cards/scoring.py:172-175,247-251,264-267`; `cards/radar.py:177,181` | PROVEN (code path); occurrence in production UNPROVEN |
| F21 | Three staleness clocks exist: poller (180 s, RTH, + `error`), evaluator (2 × scan_interval by bar ts, all sessions), pool `STALE` banner (2 × interval since `last_scan_at`). The stamp can honestly render only the poller's — the one the banner names | `poller.py:121`; `evaluate.py:532`; `radar_panel.py:582` | PROVEN |

## 2. The row mark (his ruling = the design decision)

- **Change:** `build_pool_view` derives `bars_stale_tickers` (sorted, de-duplicated tickers of `pool.poll_failures`) — only when `poll_only`, else empty; carried on `PoolView` as an in-memory field with `Field(exclude=True)` so `pool_api_payload`'s JSON stays byte-identical (`radar_panel.py:1146`). Nothing new is read, computed or stored (L3: a second rendering of F1/F8).
- **Render:** `_pool_table` / `render_row` gets the set; a stale ticker's `current` row gets, INSIDE its ticker cell, after the ticker text: `<b class="bars-stale" title="<reason> since HH:MM ET">STALE</b>`. `departed`/`excluded` rows of the same ticker: no mark (they are not polled for the pool) — open question Q3.
- **Look (ASSUMED):** wording `STALE`; 9 px monospace, red text `var(--red)`, 1 px red border, radius 3 px, padding 1×3 — the existing `.badge` geometry in red. One CSS rule appended to `PANEL_CSS`.
- **Desktop + phone:** inline in the ticker `<td>`; at ≤700 px the table already scrolls (`PANEL_CSS` `:1061`), the ticker cell is the second column so the stamp stays in view; no new column, no header change.
- **Refresh:** automatic — `refreshPool` swaps the whole pool fragment (F15), so stale → fresh → stale follows the next scan with no JS change. The ladder is never touched by this chunk.
- **Section attribute (for §3's mirror):** when the set is non-empty, `#pool-layer` also carries `data-bars-stale="GURE PFAI"`; absent when empty (healthy bytes unchanged).

## 3. The card mark

- **Change:** `render_radar_page` passes `view.pool.bars_stale_tickers` to `render_ladder(view.ladder, bars_stale=…)` (keyword, default empty). No field on `CardView`, `RadarCardRow`, `radar_cards_v`, any route or any stored column. Keyed by TICKER, so a lifecycle-polled card outside the pool (F5) is marked too.
- **Where:** the same `STALE` stamp (a) in the strip, right after the ticker `<b>` (`:1030`) — visible collapsed, desktop and phone; (b) beside `last` in the ARMED block (`:967`) and in LEVELS' `last` field (`:997`) — the two places `last` is shown. Terminal rows: no mark (not live; Q4).
- **Refresh without moving the ladder:** a `mirrorStale(layer)` in `PANEL_JS`, called after `oldLayer.replaceWith(next)` beside tonight's `mirrorDegraded(next)`: reads `data-bars-stale` of the new pool layer and adds/removes the strip stamp in place per `.ladder-item` (ticker from its `.strip b` text). No re-sort, no re-fetch, no open/close change; order and DOM position of every card unchanged (his 06:32 complaint). The two `last` stamps inside the expanded card follow on the next reload / card action (ASSUMED acceptable; Q2).
- **L52 finding: `RENDERING`.** The mark is a second rendering of the stored `poll_failures` the banner already renders (F1, F6, F8, F13): nothing computed beyond a set of names, nothing scored, nothing reordered, no new field/payload/column. What on the card changes: ONLY an added `STALE` stamp in the strip, ARMED `last` line and LEVELS `last` field of a card whose ticker is in the set; every number, dot, key, score and position is untouched.
- **Separate, NOT part of the stamp → ESCALATE:** an open card is refreshed and can SCORE on stale bars (F19, F20). That is a scoring question (L52, full bar) — his.

## 4. Deliberately NOT changed

Banner text/position; tonight's degraded line; scoring, ranking, admission, `ladder_order`, the proposed key, any dot; `refresh_card` (F19); the evaluator's or poller's thresholds (F21); `stamp_poll`'s S4-over-S3 overwrite (`store.py:270-273`, carried, not this item); `pool_api_payload` JSON; routes in `web.py`; CSS other than one appended rule; terminal rows; the pool `STALE` / `stale-data` outline.

## 5. Chunks, seats, restarts, evenings

| Chunk | Paths | Seat (L29) | RESTARTS (L42) |
|---|---|---|---|
| 1 · row mark + `bars_stale_tickers` + section attribute | `aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `docs/40 - DevDocs/cobalt/aset/radar_panel.md` | no write path (F17) → any implementation seat; today's hotfix precedent = Sonnet 5 | `com.cobalt.aset` (same module as `deploy-2026-09-21h`; GUESS from precedent until `cobalt jobs restarts <range>`) |
| 2 · card mark + `mirrorStale` | same file + `tests/cobalt/test_radar_panel_cards.py` + same DevDoc | same | `com.cobalt.aset` (same guess) |

- Sequencing: both touch `render_radar_page`, `PANEL_CSS`, `PANEL_JS` — the exact lines `s2/degraded-line-0921` (`88602cc`) edits. Any build branches off main AFTER tonight's `16` deploy (≈20:02 ET) lands; `mirrorStale` is called next to `mirrorDegraded`.
- Chunk 1 can build on his ruling alone; chunk 2 waits for the desk's lane call (L52/L67). One branch, two commits, one deploy is the cheapest if the lane allows.
- **Evenings to live: 1** (Tue 09-22, both chunks) if the desk names chunk 2 `RENDERING` → build + ≥3 checkers; **2** if chunk 2 takes a tribunal first (row Tue, card Wed). `com.cobalt.aset` is not bound by L43's radar window, but L43's one-deploy-per-evening holds.

## 6. Test plan (L45 — the real rendered page, real-shape `poll_failures` rows like `test_radar_panel.py:420-427`)

1. Stale: pool row `{"ticker":"GURE","reason":"stale",…}` + GURE a current member + an open GURE card → `/radar` (both frames) contains exactly one row stamp inside GURE's ticker cell and the strip stamp in GURE's `.ladder-item`; ARMED fixture: stamp beside `last`; LEVELS: stamp beside `last`; no other ticker stamped. Names asserted, not counts only.
2. Outside pool: open card, ticker in `poll_failures`, no current row → card stamped, no row stamped.
3. Healthy: `poll_failures = []` → `render_radar_page` and `/api/radar/pool` byte-identical to the pre-change output (golden from main), both frames; no `bars-stale` string, no `data-bars-stale`.
4. Other failed stage (`evaluate`, `mirror`, lifecycle refusal) → still the FAILED page (existing `:495` holds unchanged).
5. Refresh stale → fresh → stale via the real `/api/radar/pool` fragment + `mirrorStale` (same harness as `:641`): row stamp follows each fragment; strip stamp added/removed; `.ladder-item` order, `open` classes and card count identical before/after every step.
6. JSON: `pool_api_payload` keys unchanged (`bars_stale_tickers` absent).

## 7. Open questions (checker / tribunal)

1. Coverage: the stamp follows the poller's clock only (F21). A card the evaluator marks `input_stale` outside RTH, or between 180 s and 200 s, may carry no stamp — accept, or does "stale" need one definition? (His, L53 — not a value proposed here.)
2. Should the expanded card's two `last` stamps also be mirrored live, or is next-reload enough?
3. Mark `departed` rows of a lifecycle-polled ticker too?
4. Terminal rows: confirm no mark.
5. `.strip b` text as the ticker key in JS vs adding `data-ticker` (which changes healthy card bytes).
6. `Field(exclude=True)` vs letting the JSON grow one key — which does `test_api_json_and_html_are_from_same_builder_output` (`:698`) want?
