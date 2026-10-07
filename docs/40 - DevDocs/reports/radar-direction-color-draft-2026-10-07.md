# radar-direction-color — draft report (2026-10-07, R625)

## §0 Headline
- SHORT FIX, not a rework. One `src/` file, `src/cobalt/aset/radar_panel.py`: the strip and title markup (`:1422`–`:1424`, `:1467`–`:1468`) plus one `PANEL_CSS` line. Tests go in `tests/cobalt/test_radar_panel_cards.py`.
- Long cards get a green strip fill and green title text; short cards get red. The colours are the existing `--green`/`--red` and the dots' fills `#0f2a1c`/`#3a1119`; there is no new colour value.
- The strip gets the `↑`/`↓` arrow, which it lacks today, so direction is never colour alone. An unknown direction shows `direction ?` and stays neutral.
- RESTARTS: `com.cobalt.aset com.cobalt.radar`. `DB` key left out: the job writes nothing and its tests are offline.
- Card: `prompts/2026-10-07/89-radar-direction-color-card.md`, BASE fill only.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md`: rows A (class + arrow map), B (CSS tint), C (negative controls + the ladder pin re-capture), D (RUN `jobs restarts`).
- One fill token: `BASE`. Drafted at `f6d31607`.

## DECISIONS
- ASK DESK: what is tinted. Default: the strip background plus border, and the title text. Alternative: a left border bar on the strip only. A design question for him [10:21 EDT].
- ASK DESK: the strip gains an arrow at the start of its third span. That is the only new visible glyph, and the order needs it so direction is never colour alone. Default: add it. Alternative: put it in the first span, which wraps at the 75px phone column (`:1499`) [10:21 EDT].
- ASK DESK: `PIN_HEALTHY_LADDER_SHA256` (`test_radar_panel_cards.py:396`) is re-captured on the build with a comment line, as on 09-23 and 09-28 (`:393`–`:394`). Default: re-pin. Alternative: none, because the ladder markup must change [10:21 EDT].

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `f6d31607` (2026-10-07, before 10:21 EDT). `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` → no output.
- `reports/cto-2026-10-07-words.md:7`–`:8`: R625, read.
- `src/cobalt/aset/radar_panel.py` reads: `:225`–`:240` (`RadarCardRow`, `direction` `Literal` `:234`), `:375`–`:385` (`CardView`, `:381`), `:865`–`:867` (row validation → `FAILED: invalid radar card row`), `:895`–`:915` (row → view; sign `:908`), `:1370`–`:1500` (`_card_detail`, `render_ladder`, `PANEL_CSS`; title `:1422`–`:1424`, WATCH `:1402`–`:1403`, CARD field `:1435`, terminal `:1481`, strip `:1465`–`:1471`, `:root` `:1496`, rules `:1497`, `@media` `:1498`–`:1500`), `:1501` (phone frame), `:1555`–`:1562` (`mirrorStale` reads `.strip b` `firstChild`, `:1559`), `:1611`–`:1624` (`render_radar_page`, `render_failed_page`).
- `src/cobalt/aset/web.py:899`–`:912`: `/radar`; the same renderer for both frames; a `RadarPanelError` becomes the FAILED page.
- `tests/cobalt/test_radar_panel_cards.py`: `:13`–`:62`, `:119`–`:260`, `:384`–`:520`; pins `:393`–`:397`, `:507`; ticker `<b>` asserts `:472`, `:519`. Grep of `tests/` for `→`, `data-toggle-card`, `<span>#`, `rank-chip`, `card-title`, `↑`, `↓`: none reads the strip's third span or the title, besides the pin.
- Existing direction colour: `.direction.long{color:var(--green)}.direction.short{color:var(--red)}` (`:1497`), reused.
- Missing direction today: no card renders. Validation fails and the page shows FAILED. The title's `"↑" if long else "↓"` (`:1423`) is an unreachable guess; row A removes it.
- RESTARTS reads: `configs/cobalt/jobs.yaml:39`, `:90`, `:184`, `:194`. Importers of `radar_panel`: `aset/web.py:75`, `:2014`, `:2040`. Chain to `cobalt.cli`: `cli.py:82` → `voice/cli.py:29` → `voice/turn.py:43` → `voice/confirm.py:77`. Class rules: `src/cobalt/jobs/restarts.py:216`–`:220` (src), `:225`–`:228` (DOCS), `:245`–`:246` (tests). Precedent: `prompts/2026-10-06/54-radar-ladder-refresh-card.md` `## RECORDS` RESTARTS.
- `docs/40 - DevDocs/prompts/CARD.md`: read whole (header keys, `DB` rule).
- Nothing run beyond reads; no git write, no launch.

RADAR DIRECTION COLOR CARD DRAFTED · decisions: 3
