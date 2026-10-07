## §0 Headline
- Card `89-radar-direction-color-card.md` row C amended: the long/short identity now drops the CARD `direction` field and the IN-TRADE `{direction}` text, besides the title and 1R/2R.
- Both direction prints proven at main HEAD `102fbf96`.
- Control proves the card body, the WATCH state and every other element are unchanged by direction.

## CHANGES
- Card line 20 (row C, `red first` cell): the `expanded` identity now removes three things: the `LEVELS` 1R/2R fields; the CARD `<span class="field" data-field="direction">…</span>`; the IN-TRADE running line's `{direction}` text. Chose dropping the three fields over comparing only the `dir-` count and other blocks, as the narrower edit. The row states what the control proves.

## DECISIONS

## RECORDS
- `radar_panel.py:1435` read: CARD section calls `_field(card, "direction", "direction", card.direction)`.
- `radar_panel.py:1105`–`:1111` read: `_field` emits `<span class="field" data-field="{field}">label badge value`, so the field is a removable span.
- `radar_panel.py:1340`–`:1341` read: IN-TRADE `<div class="running"><b>{running}</b> · {direction} · {realized}</div>`.
- `radar_panel.py:1358` read: IN-TRADE is built with `direction=card.direction`.
- `radar_panel.py:908` read: sign by direction (the 1R/2R difference).
- Main HEAD at read: `102fbf9674c5`; the card cites `src` lines read at `f6d31607`, and the preflight records `src` unchanged since.
- `BASE`, `TIP`, `CHECK REPORT`, `HOUSE B`: not touched.

RADAR COLOR CARD AMENDED · decisions: 0
