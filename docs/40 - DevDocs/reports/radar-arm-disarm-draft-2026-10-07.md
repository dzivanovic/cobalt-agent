# radar-arm-disarm — draft report (2026-10-07, R627)

## §0 Headline
- SHORT FIX, not a rework. Two `/radar/card/{id}/arm` and `/disarm` routes through `_card_tap` → `CardStore.transition` (the `/triggered`, `/pass` mirror), two tap blocks in `_card_detail`, one CSS line.
- The move edge needs NO change: `CardStore.transition` already enforces the edge, ARM-only-when-sized, the DISARM reason and the session gate under the row lock. A double ARM is refused by the edge, not idempotent.
- Not `/card/{id}/move`: on a refusal it answers HTML 200, which the panel would show as `saved` (L1).
- Correction to the brain: the sheet's ARM / DISARM already render for radar cards (`open_cards` has no origin filter). The gap is the `/radar` page only.
- RESTARTS `com.cobalt.aset com.cobalt.radar`; `DB` key left out. Serial after card 89, which touches the same file and pin.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/92-radar-arm-disarm-card.md`. Rows: A (ARM route), B (DISARM route + 80-char cap), C (the two taps + CSS), D (negative controls, allowlists, ladder pin), E (RUN `jobs restarts`).
- One fill token: `BASE`. Drafted at `95e40f47`.

## DECISIONS
- ASK DESK: ARM renders on every WATCH card; an unsized one shows the store's UNSIZED refusal on tap. Default: always render. Alternative: render only once `shares` is set, which hides why there is no ARM [10:27 EDT].
- ASK DESK: the DISARM reason is free text, capped at 80 characters by the radar route (422). The sheet keeps no cap. Default: cap in the route. Alternative: no cap, or a cap in `_assert_reason` for both pages, which touches the store [10:27 EDT].
- ASK DESK: two routes, `/arm` and `/disarm`, one per verb as `/triggered` and `/pass` are. Alternative: one `/radar/card/{id}/move` taking `to=`, which would mirror the sheet's FILLED and CLOSED branches [10:27 EDT].
- ASK DESK: `PIN_HEALTHY_LADDER_SHA256` is re-captured with a comment line, after card 89's re-capture. Default: re-pin. Alternative: none; the markup must change [10:27 EDT].

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `95e40f47` (2026-10-07 10:27 EDT). `git -C /Users/cobalt/cobalt diff --stat f6d31607 HEAD -- src tests configs` → no output.
- `reports/cto-2026-10-07-words.md:10`–`:11`: R627, read.
- `src/cobalt/aset/radar_panel.py:1100`–`:1637`, read whole: key row `:1144`–`:1168`, `_card_form` `:1195`–`:1208`, WATCH `:1400`–`:1404`, ARMED `:1405`–`:1412`, card-status `:1430`, `PANEL_CSS` `:1495`–`:1504`, `PANEL_JS` `post` `:1530`–`:1540`, click handler `:1541`–`:1557`, `tickLadder` `:1578`–`:1603`.
- `src/cobalt/aset/web.py`: `askReason` `:174`–`:179`; `:630`–`:778` (`_card_controls` labels `:672`–`:676`, `_needs_reason` `:683`–`:689`, buttons `:709`–`:722`, `_open_cards_section` `:759`–`:778`); `card_move` `:1379`–`:1438`; `:1480`–`:1819` (`/key` `:1554`, `pass` `:1565`–`:1567`, `_card_tap` `:1775`–`:1796`, `/triggered` `:1799`); `/pass` `:1849`–`:1857`; `:1970`–`:2014` (`/stop`, `/stop/reset`). Route list by grep `@app\.(post|get)\(`.
- `src/cobalt/cards/store.py:231`–`:422` (`open_cards`, `transition`, `_assert_reason`). `src/cobalt/cards/models.py:85`–`:134`, `:139`–`:161`, `:199`–`:204`.
- `tests/cobalt/test_radar_panel_cards.py` (759 lines): `:1`–`:240`, `:380`–`:759`. `tests/cobalt/test_s3_c3_panel_offline.py`: `:1`–`:200`, `:340`–`:448` (grep of its route lists and helpers). `tests/cobalt/test_radar_cards_db.py:169` (UNSIZED pinned, grep).
- `docs/00 - Project/SPRINT-LADDER-v0_1.md:65`: F7, read.
- RESTARTS reads: `src/cobalt/jobs/restarts.py:210`–`:249`; `configs/cobalt/jobs.yaml:39`, `:90`, `:184`, `:194` (grep); importers of `cobalt.aset.web` / `radar_panel` (grep `src/`). Chain `cli.py:82` → `voice/cli.py:29` → `voice/turn.py:43` from card 89's RECORDS, valid because `src` is unchanged since `f6d31607`.
- `docs/40 - DevDocs/prompts/CARD.md`, read whole; precedent `prompts/2026-10-07/89-radar-direction-color-card.md`, `reports/radar-direction-color-draft-2026-10-07.md`.
- Nothing was run beyond reads. No git write, no launch.

RADAR ARM DISARM CARD DRAFTED · decisions: 4
