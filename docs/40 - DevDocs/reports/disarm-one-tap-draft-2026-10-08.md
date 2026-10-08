# DISARM one-tap — drafter report 2026-10-08 (prompt 133, R689)

## §0 Headline
- Card `134` drafted: DISARM on `/radar` opens five reason chips; one chip tap disarms with that word as the reason. No typing, no confirm, `PANEL_JS` unchanged.
- Built per the brain's L79 amendment in prompt `133` (chips supersede the fixed string).
- Rows A–E: route list check (422 off-list), chip markup + one CSS line, script-seam control, ARM/TRIGGERED controls + ladder pin re-capture, RESTARTS run.
- Launch after card `118` merges; desk refills `BASE`.
- 0 for him.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/134-disarm-one-tap-card.md` (uncommitted; the desk commits it).
Header checked against `ops/desk/desk-launch.sh` build mode (`:721`–`:741`, `:894`–`:913`):
- `JOB: disarm-one-tap-1008` — `[a-z0-9-]` (`:731`–`:733`).
- `BRANCH: ops/disarm-one-tap-1008` — plain name (`:734`–`:736`); absent today, so no existing-branch refusal (`:909`).
- `WORKTREE: disarm-one-tap-1008` — one name, approved pattern (`:753`–`:755`); absent today.
- `BASE: 1d5aa3f3` — 8 hex, a commit (`:898`–`:899`).
- `REPORT: /Users/cobalt/cobalt-wt/disarm-one-tap-1008/docs/40 - DevDocs/reports/disarm-one-tap-build-2026-10-08.md` — matches `$WT/$wt/docs/40 - DevDocs/reports/*.md` (`:900`–`:903`).
- `RULINGS: 2026-10-08 R689` — shape `:737`–`:741`; row `cto-2026-10-08.md:42` holds `HIS RULING` and `APPROVED`, one row, committed at HEAD (`ruling_row` `:244`–`:271`).
- `TIP`, `CHECK REPORT`, `HOUSE B` empty; no `TAG`; `## ROWS` present (`:895`–`:896`); no `«FILL`.
- `DB` left out (`src/` and `tests/cobalt/` rows).

## DECISIONS
1. CHIPS, NOT A FIXED STRING. The brain's amendment in prompt `133` and the desk's message replace the fixed reason. Chips: `setup broke` · `no volume` · `market turned` · `changed mind` · `other`.
2. REVEAL THROUGH THE DOT-TRAY SEAM. The DISARM toggle is a `data-dot-toggle="disarm"` button with a hidden `.tap-strip disarm-chips` sibling, so `PANEL_JS` stays byte-identical. An open tray already pauses the ladder tick (`:1609`, `:1620`), so the chips do not vanish mid-choice. Row C pins that seam.
3. ONE LIST, IN `radar_panel.py`. `DISARM_REASONS` is read by both the panel and the route through the existing import (`web.py:75`). The route refuses a missing, blank or off-list value with 422 before the store. `_assert_reason` stays as the backstop.
4. A CALLER-SUPPLIED REASON IS REFUSED UNLESS IT IS A LISTED CHIP (the prompt's "ignored or capped" pick). The 80-character cap goes, since the list bounds the value. Three R627 tests are replaced by a per-chip test and an off-list test.
5. NO DRC READ-BACK NEEDS A CATEGORY. No DRC code reads the disarm reason. Replay carries `card_transitions.reason` verbatim. The chip word lands in the same column. A DRC line that prints it is out of this card.
6. ORDER WITH CARD `118`. Both cards touch `radar_panel.py` and `test_radar_panel_cards.py`. Build serially: 118 first, this card after it merges. The desk refills `BASE`, and the builder re-reads shifted lines. 118 changes no rendered markup, so this card's pin re-capture stands on 118's ladder.
7. `LADDER` carries the date (`OFF-LADDER — reports/cto-2026-10-08-words.md 2026-10-08 R689`). This follows the `CARD.md` shape `OFF-LADDER — <report> <date> R<n>` over the prompt's dateless value. `desk-launch.sh` checks only that it is non-empty.

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `1d5aa3f3` (2026-10-08, drafting). All `file:line` below read at that HEAD.
- `radar_panel.py`: `DISARM_TAP` `:1180`–`:1183` (input `:1181`); ARMED block `:1427`–`:1436` (disarm `:1435`); `ARM_BUTTON` `:1179`; `_card_form` `:1201`–`:1214`; `_dot_html` `:1116`, tray `:1139`; `PANEL_CSS` `:1523`, `:1531`, arm-key `:1532`; `PANEL_JS` `:1536`–`:1635` (toggle `:1575`–`:1576`, grade `:1577`–`:1578`, tap post `:1583`–`:1584`, guards `:1609`, `:1620`).
- `web.py`: import `:75`–`:82`; `askReason` `:174`, `:713`; `_TapInputRefused` `:1672`; `_card_tap` `:1775`–`:1796`; `/arm` `:2007`–`:2017`; `/disarm` `:2020`–`:2033` (80-char check `:2026`–`:2028`).
- `cards/store.py` `_assert_reason` `:383`–`:410`.
- `test_s3_c3_panel_offline.py`: `NEW_ROUTES` `:52`–`:53`; `GatedCards` `:102`–`:118`; R627 tests `:210`–`:295`; market reset `:459`–`:471`.
- `test_radar_panel_cards.py`: dot-tray regexes `:288`, `:294`; pins `:392`–`:399`; `_page` `:442`; pin test `:495`–`:510`; R627 block `:860`–`:952`; allowlist `:994`–`:999`.
- `test_radar_panel.py:1112` `TICK_GUARDS` holds `.tap-strip:not([hidden])`.
- Typed inputs on radar taps (`grep -n "<input name=\|_price_input(\|_card_form(" radar_panel.py`): only DISARM asks for text. ARM, TRIGGERED, PASS and the key row are buttons. FILLED @, move stop and correct take prefilled numbers. Exits take a prefilled price, plus a shares number on `typed` and a checkbox on `flat`. HOLDING takes an empty shares number. None of them is changed.
- DRC read-back: `grep -rln -i disarm src` → `cards/store.py`, `cards/models.py`, `aset/web.py`, `aset/radar_panel.py` only. `replay/cards.py:387`–`:391` carries `reason` verbatim; `replay/models.py:84`–`:89`.
- Restart class homes (`jobs/restarts.py`): `src/` files `static import reach` `:220`; tests `test/documentation; no resident` `:246`; the report `DOCS` `:225`–`:228`. Expected `com.cobalt.aset com.cobalt.radar`.
- `reports/cto-2026-10-08.md:42` R689 `APPROVED · HIS RULING`, present at `git show HEAD:`.
- `git rev-parse --verify --quiet ops/disarm-one-tap-1008` → exit 1. `ls /Users/cobalt/cobalt-wt` → no `disarm-one-tap-1008`.
- `desk-launch.sh` build checks read: `:700`–`:741`, `:752`–`:778`, `:894`–`:913`; `ruling_row` `:244`–`:271`.

DISARM CARD DRAFTED · decisions: 7
