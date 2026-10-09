# arm-unsized draft — 2026-10-09

## §0 Headline
- Card `prompts/2026-10-09/152-arm-unsized-card.md` written, uncommitted: JOB `arm-unsized-1009`, BASE `6f55636b`, RULINGS `2026-10-09 R719`.
- Fix: `CardView.sized` = the store's four-column rule (`store.py:310`); an unsized WATCH card renders ARM with HTML `disabled` and "ARM · tap a key first". Only `radar_panel.py` changes, plus one CSS line.
- Red: `test_arm_is_inert_on_an_unsized_watch_card_and_live_once_sized`, with a per-column partner. Control: a real `CardStore` behind a fake connection still returns 409 UNSIZED on a direct POST, and `store.py` and `web.py` diff is empty.
- The fixture's WATCH card is unsized, so the R627 ARM assertion (`test_radar_panel_cards.py:979`) and `PIN_HEALTHY_LADDER_SHA256` (`:481`) move (row B).

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/152-arm-unsized-card.md`. Rows: A (red, the fix), B (R627 test and ladder pin follow), C (control, store guard), D (RUN restarts).

## DECISIONS
- ASK DESK: disabled or a label? [11:33 ET] Default taken: both, the sheet's form: HTML `disabled` plus the reason in the label (`web.py:352`, `:357`). The radar `key-disabled` form (`radar_panel.py:1154`–`:1160`) stays tappable on purpose, so it does not fit a control that must not act.
- ASK DESK: `DB: none` as the prompt said? [11:33 ET] Default taken: the key is left out. `CARD.md` allows `none` only when every file sits under `ops/`, `tests/ops/` or `docs/`. Every new test is still offline.
- ASK DESK: the page's rule from `sized_grade` or from the four columns? [11:33 ET] Default taken: the four columns, the store's exact list (`store.py:310`), carried as `CardView.sized`. `CardView` lacks `used_risk` (`radar_panel.py:378`–`:420`).

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `6f55636b` (read before 11:33 ET). `git -C /Users/cobalt/cobalt log --oneline -3` → `6f55636b docs(desk): brain handover 10-09`, `0e84db6f`, `63e5008d`.
- `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` → empty.
- `ls` of the card, this report and `reports/arm-unsized-build-2026-10-09.md` → all absent before writing. `reports/cto-2026-10-09.md` present; R719 at `:12`.
- Read: `src/cobalt/aset/radar_panel.py` `:240`–`:438`, `:895`–`:934`, `:1130`–`:1218`, `:1395`–`:1439`, `:1531`–`:1532`, `:1540`–`:1589`. Searched for `disabled|sized|ARM|arm-key`.
- Read: `src/cobalt/cards/store.py` `:105`–`:116`, `:255`–`:329`, `:1374`–`:1389`. Searched for imports, `assert_writable` and `conn.commit|rollback|close` (`:372`–`:381`).
- Read: `src/cobalt/aset/web.py` `:330`–`:364`, `:1775`–`:1814`, `:1995`–`:2029`. Searched for `disabled` across `src/cobalt/aset` (one HTML `disabled` site, `web.py:357`).
- Read: `tests/cobalt/test_radar_panel_cards.py` `:100`–`:201`, `:380`–`:404`, `:476`–`:595`, `:756`–`:777`, `:848`–`:859`, `:940`–`:1044`. Searched for `CardView(` (one constructor, `radar_panel.py:911`) and `PANEL_CSS` across `tests/`.
- Read: `tests/cobalt/test_s3_c3_panel_offline.py` `:15`–`:37`, `:60`–`:159`, `:205`–`:260`. Searched for `UNSIZED|/arm` across `tests/`.
- Read: `tests/cobalt/test_radar_cards_db.py` `:150`–`:179`.
- RESTARTS class homes: `src/cobalt/jobs/restarts.py:220` (`static import reach`, `radar_panel.py`), `:246` (`test/documentation; no resident`, both test files), `:225`–`:228` (`DOCS`, reports). `configs/cobalt/jobs.yaml:39` `com.cobalt.aset`, `:184` `com.cobalt.radar`, `:194` `imports: [cobalt.cli]`. Expected: `com.cobalt.aset com.cobalt.radar`.
- Read: `prompts/CARD.md`, `prompts/2026-10-08/118-radar-display-fix-card.md`, `Memory/topics/writing-rules.md`.

ARM UNSIZED CARD DRAFTED · decisions: 3
