# DISARM one-tap card 134: brain judgement of the draft's 7 DECISIONS · 2026-10-09
Source: `reports/disarm-one-tap-draft-2026-10-08.md` `## DECISIONS`; card `prompts/2026-10-08/134-disarm-one-tap-card.md`.

All 7 hold as KEEP. One fact is added to D6. Nothing goes to him.

1. CHIPS — KEEP. This is my predecessor's 10-08 answer (one-tap chips, L79 amendment in prompt 133).
2. DOT-TRAY SEAM — KEEP. `PANEL_JS` stays byte-identical, and an open tray already pauses the tick (`:1609`, `:1620`). Row C pins it.
3. ONE LIST IN `radar_panel.py` — KEEP. One source for panel and route. `_assert_reason` stays as the backstop.
4. OFF-LIST REFUSED, 80-CHAR CAP DROPPED — KEEP. The only caller of `POST /radar/card/{id}/disarm` is the panel (`grep -rnil disarm src` → `models.py`, `store.py`, `web.py`, `radar_panel.py`; route `web.py:2020-2033`). A missing reason, accepted today (`reason or None`, `:2030`), becomes 422. Every chip sends a word, and `other` covers the rest, so no live path breaks.
5. NO DRC CATEGORY — KEEP. No DRC code reads the reason, and replay carries it verbatim (`replay/cards.py:387-391`).
6. ORDER — KEEP, with a FACT: card 118 is already DEPLOYED (`752a8ce6`, R709), so `BASE: 1d5aa3f3` is stale. The desk refills `BASE` with current `main` at launch. The builder re-reads every cited line, because cards 137/150 and 126/149 landed since. ALSO SERIAL: the ARM-on-unsized display card (R719) touches the same ARM/DISARM block of `radar_panel.py` (`ARM_BUTTON` `:1179`, ARMED block `:1427-1436`). Card 134 builds first, and the ARM-unsized card launches on 134's merged tip.
7. LADDER WITH DATE — KEEP. This is the `CARD.md` shape.

FOR THE CHECK: "Brain 10-09 (disarm-one-tap-decisions-2026-10-09.md): D1-D7 KEEP; BASE refilled to main after 118's deploy; 134 builds before the ARM-on-unsized card, which bases on 134's merge."
