# ASET sheet survey — 2026-10-01 (read-only; time from `date`: Thu Oct 1 07:57 EDT 2026)

## §0
- A filled card leaves the sheet only when an exit, a correction or a HOLDING count brings its running shares to 0; the exit, HOLDING and correction forms exist on `/radar` (radar cards) and on the old sheet (manual cards). `/radar` has no form for a manual card. PASS, EXPIRE and MISSED never apply to a FILLED card.
- Nothing expires or day-rolls a FILLED card: a card still holding shares stays open into the next trading day on both pages until you exit it.
- The only timer refresh is `/radar`: it re-fetches the pool every 100 s. `/` has no auto-refresh. The fixed voice box at the bottom-right resizes itself after each page load. I could not prove which of these you saw jump.
- Deprecation: no written ruling retires the old sheet. Your 09-23 R30 words ("we're going to go away from it") and a BACKLOG row ("the successor lane that retires the sheet") say it is going away, but no plan names a date or scope.
- The old sheet holds functions `/radar` lacks (create a card, size, attest, day-mode and settings lines, manual-card controls). Q5 lists them.

## 1. How does a card end and leave the sheet?

**Control that ends a card (all routes in `src/cobalt/aset/web.py`):**

| Ends it | Route | What he types / taps | Page, control |
|---|---|---|---|
| exit ½ ⅓ flat typed | `POST /radar/card/{id}/exit` `:1778` → `legs.record_exit` `:1806`; the leg that makes running 0 calls `_close_if_zero` (`cards/legs.py:228`, called `:439`) | price (required, `:1790-1793`); `typed` also a share count; `flat` commits `confirmed` only with ✓ (`:1801-1805`) | radar card: `/radar`, expanded card, IN-TRADE block (`radar_panel.py:1357`, forms `:1319-1323`). manual card: `/`, "Open cards (F7)", the card's in-trade block (`web.py:1925-1947`, posts `source=sheet`) |
| HOLDING X | `POST .../held` `:1832` → `legs.record_held` `:601`; `_close_if_zero` `legs.py:662` | the share count he holds; 0 closes (`:1839-1842`) | same two places (`radar_panel.py:1324-1328`) |
| correct a leg | `POST .../correct` `:1856` → `legs.record_correction` `:480`; `_close_if_zero` `legs.py:586` | leg id, price and/or shares (`:1866-1878`) | same blocks' leg rows (`_leg_rows`, `radar_panel.py:1344`); a CLOSED manual card's estimated legs on `/` (`web.py:1950-1981`); a CLOSED radar card's estimated legs in the `/radar` TERMINAL list (`radar_panel.py:1363`) |
| PASS | `POST .../pass` `:1767` is TRIGGERED → PASSED. `.../key` with `pass` `:1481-1483` is WATCH → PASSED. On `/`, a PASS button on any card whose edge exists (`web.py:653-656`, `:690-702`) | a tap | `/radar`: key row "pass" (`radar_panel.py:1166`) and the TRIGGERED block's PASS (`:1223`). `/`: PASS button |
| EXPIRE | job `cobalt cards expire`, weekdays 16:05 (`configs/cobalt/jobs.yaml:233-238`) and the radar evaluator (`radar/evaluate.py:1937`). Both act on WATCH, ARMED, TRIGGERED only (`cards/expire.py:71`, `:182`, `:285`) | nothing | no control; the old sheet draws an EXPIRE button for those states (`web.py:655`) |
| MISSED | `/card/{id}/move` to MISSED, WATCH only (`cards/models.py:93-94`); needs a typed reason (`web.py:663-669`) | a reason | `/` only. `/radar` has no MISSED control (not found in `radar_panel.py`) |

- Edge table: FILLED can go only to CLOSED (`cards/models.py:105`). So PASS, EXPIRE and MISSED are never offered on a FILLED card.
- **The refused CLOSE button on the old sheet.** `_card_controls` renders a button for every legal edge, and FILLED → CLOSED is legal (`web.py:690`), so a CLOSE button is drawn on a FILLED card. `POST /card/{id}/move` refuses `to=CLOSED` (`:1382-1391`: "this route never closes"). The card is closed only by an exit, HOLDING or a correction. The refused button is therefore always on the page for a FILLED card.
- **Manual FILLED card:** on `/` only. `radar_cards_v` is `origin = 'radar'`, so a manual card is not on `/radar` (`web.py:1925-1931`).
- **Radar FILLED card:** on `/radar`. It is not offered the exit forms on `/` (`_sheet_in_trade` returns "" unless `origin == MANUAL`, `web.py:1934-1935`). It still appears in the `/` list with the CLOSE button, because `open_cards()` has no origin filter (`cards/store.py:231-244`).
- **Overnight.** `open_cards()` selects every non-terminal card with no date filter (`cards/store.py:235-243`). The radar ladder reads `RADAR_OPEN_STATES = WATCH, ARMED, TRIGGERED, FILLED` regardless of date (`cards/store.py:968`, query `:1019-1030`; the ladder read at `:1047-1061` adds terminal cards only for today). `expire_due` skips FILLED (`expire.py:182`). Searching `expire|carry|stale|session_date` under `src/cobalt/cards` and `src/cobalt/aset` finds no carry-over or day-roll code for a FILLED card. Result: a FILLED card stays open the next trading day on both pages until his exit/HOLDING/correction brings running to 0. WATCH, ARMED and TRIGGERED cards from an earlier day are expired by the 16:05 job against their own day (`expire.py:187-195`).
- The `/` list shows terminal cards nowhere except today's CLOSED manual cards with an estimated leg (`web.py:1961`, `_today_et()`).

## 2. What makes the prompt at the bottom jump on refresh?

**Pages that refresh themselves (from `src/cobalt`):**
- `/radar` only: `window.setInterval(refreshPool, interval)` (`radar_panel.py:1576`); `interval` = `data-refresh-seconds` = `radar.scan_interval` (`:1559`, `:1589`; value 100 s, `configs/cobalt/taxonomy/tunables.yaml:675-676`). It fetches `/api/radar/pool` (`:1563`) and replaces only `#pool-layer` (`:1568`). The ladder is replaced only after one of his taps (`refreshLadder`, `:1518-1527`, called by `post` `:1534`).
- No `<meta http-equiv=refresh>`, no `setInterval` and no `location.reload` anywhere else under `src/cobalt` (grep of `setInterval|http-equiv|location.reload` finds only `radar_panel.py:1576`). `/`, `/drc` and `/card/{id}/move` do not refresh themselves.
- `/card/{id}/move` is the result page of a POST (`web.py:1359`); a browser refresh there re-submits that POST. I did not test what the browser does.

**Elements whose position depends on cards:**
- `/radar`: the pool layer sits below the ladder (`radar_panel.py:1589`, `render_ladder` then `render_pool`). The ladder's height follows the number of active cards, the top two expanded (`:1451`, `open_class` for index ≤ 2), plus the terminal list. When a card opens/closes, everything below moves. The 100 s pool replace changes the pool block's own height (banners, `+entered/−left` churn line, `:1045-1055`).
- `/`: the closing note "Every computed sizing persists…" (`web.py:442`) and the sizing form follow the open-cards block (`:405`, built from `:758`), whose height follows the number of open cards, in-trade blocks (`:1944`) and today's estimated legs (`:1950`).
- Both pages: the voice box is `position:fixed; right:16px; bottom:16px` (`voice/web.py:200`). The card list does not move it. Its height changes when `/voice/status` returns banner lines after each load (`:299`, `banner()` `:218-223`) and when `#cv-reply` text changes, so its top edge moves on every page load.

I cannot name the exact element he saw jump. See UNPROVEN.

## 3. Which page is for what?

| Page | Shows | Only this page has | `/radar` equal? |
|---|---|---|---|
| `/` (`web.py:874`, `_render` `:345`) | env/vault/day-mode banner (`:399-402`), attest form (`:623`), settings change line (`:1272`), "Open cards (F7)" with state buttons, stop edit, one-click fill (`:635-736`, `:739-760`), sizing form (`:406-441`), voice box | create a card: `/size` `:969`, fill form `/fill` `:1075`, attest `/attest` `:1202`, settings change line `/settings/daily` `:1304`, `/settings/daily/apply` `:1319`, last-price prefetch `/api/prefill` `:957`; manual-card exits (`:1925`); ARM/DISARM/TRIGGERED/MISSED/EXPIRE/PASS buttons (`:653-702`); one-click FILLED on a manual card (`:671-687`) | none of create, size, attest or settings: no such forms in `radar_panel.py` (grep of `attest`, `/size` finds no form). Radar has its own key/size taps (`web.py:1472`), exits, HOLDING, correct, stop edit (`:1893`) and ↺ reset (`:1906`) |
| `/radar` (`web.py:879`, `radar_panel.py:1581`) | card ladder (#1, #2 expanded), TERMINAL list, POOL VIEW with 100 s refresh (`:1042`, `:1576`) | key taps A+/A/B/C/pass (`:1472`), dot taps (`:1524`), promote/release (`:1563-1568`), TRIGGERED / FILLED @ / PASS taps (`:1717-1767`), IN-TRADE exits ½ ⅓ flat typed, HOLDING, correct, stop edit and reset | n/a |
| `/drc` (`web.py:2025`) | the date's DRC inputs and day's cards, read-only (`:2011-2032`) | file import `/drc/import` `:2035`, "No trades today" `:2055`, folder scan `:2069` | none, none on the sheet either |
| `/card/{id}/move` | no page of its own: a POST (`web.py:1359`) that returns the `/` page with a banner (`:1416`) | the old sheet's state-change route; refuses FILLED and CLOSED (`:1372-1391`) | n/a. Radar uses `/radar/card/{id}/…` |

- A radar card never gets the one-click FILLED button (`web.py:671-672`); a radar card's route to FILLED is TRIGGERED then the `/fill` tap.
- Radar equals for a manual card's exits: the same routes, reached from `/` with `source=sheet` (`web.py:1586-1587`, `:1925-1947`).
- MISSED: old-sheet button only (`web.py:655`, `:663-669`); no `/radar` control found.
- DISARM (ARMED → WATCH, needs a reason): old-sheet button only (`web.py:653`, `:663-669`); no `/radar` control found (`radar_panel.py` ARMED block has only the TRIGGERED tap, `:1405-1412`).

## 4. Is the old sheet deprecated?

No ruling found that retires, replaces or hides it. What exists:
- His words, 09-23 R30: "So it doesn't need to be fixed on the asset sheet because we're going to go away from it. But if this logic is going to go forward into the new process, I need it reviewed and fixed. Obviously," (`docs/40 - DevDocs/reports/cto-2026-09-23.md:33`, repeated in `docs/00 - Project/PROJECT-LEDGER.md:1916`). The desk's answer in the same row: "a build row in the lane that retires the sheet".
- `docs/00 - Project/BACKLOG.md:335`: "One build row for the successor lane that retires the sheet (the day-mode / radar-panel path that lives on)". It names a lane, no date or scope.
- `docs/40 - DevDocs/reports/cto-2026-09-21.md:25`: his question "does he work from the ASET sheet or from the radar — 'If I use the radar, I can't do my morning cards for today's trade session'". The 09-23 line quoted above: "While the engine is in shadow (L7) he works his morning cards on the ASET sheet, `/radar` beside it."
- `docs/30 - Design/S3-EXITS-v3-2026-09-22.md` and the `C3-4` code treat the sheet as the home of manual-card exits (`web.py:1925-1931`).
- The vault memory root (excluding `_retired/`, `_imports/`): the only "ASET sheet" hits are `areas/cobalt-sprints.md:11` (S1 acceptance), `topics/trading.md:12` (his desk tabs) and two long lines in `areas/cobalt-sprints.md:49`, `:69` that I read for the pattern and found no retire/replace/hide ruling. `docs/00 - Project/` has no retire/replace plan beyond the two rows above.

## 5. What would retiring it take?

Functions the old sheet has and `/radar` lacks (§3):
1. Create a manual card: the sizing form, `/size`, `/api/prefill`.
2. The fill recompute form (`/fill`, `web.py:1075`) for a manual card; `/radar` fills only an existing TRIGGERED radar card.
3. Attest the .htk and the day-mode banner (`/attest`, `web.py:1202`, `:571-632`). `/radar` taps need a resolved day mode (`_todays_rung`, `:1463`) but show no banner or attest form.
4. The settings change line (`/settings/daily`, `/settings/daily/apply`).
5. Manual-card controls: the in-trade exits for manual cards (`:1925`), DISARM and MISSED, and today's CLOSED manual cards' estimated-leg corrections (`:1950`).
6. Closing a manual card needs a manual card to be on a page that can reach it; `/radar` cannot list one (`radar_cards_v` is `origin = 'radar'`).

## UNPROVEN
- Which element he saw jump. I read the code only, not his browser. The fixed voice box (`voice/web.py:200`) and the card list on `/` are the two candidates for the bottom of the page; the pool block is the candidate on `/radar`.
- What his browser does on refresh of `/card/498/move` (re-POST prompt or not). I did not run a browser.
- Whether a FILLED card can really sit across an overnight in production: the code shows no expiry for it, but I ran no query against the database.
- Whether the two long lines in `areas/cobalt-sprints.md` (`:49`, `:69`) hold a sheet-retirement ruling beyond the greps I ran (`ASET sheet`, retire/replace/hide near `sheet`).
- Whether the radar scan cadence in production is the 100 s in `tunables.yaml:675-676`; a runtime override table was not read.
- Why the `/` sheet shows a CLOSE button that always refuses: derived from the edge table (`models.py:105`) and `_card_controls` (`web.py:690`); I did not render the page.

SURVEY DONE · questions: 5 · unproven: 6
