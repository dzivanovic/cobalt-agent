# `src/cobalt/drc/reconcile.py`

## What it does
The DRC reconcile (DRC D5; v2 §3 `:80` steps 1–6, S-C1 / S-C2, R67, R90). For each trade the build matched to a card (D3's match), it compares the trading-log export with the card's current legs, stores the diff, and on the event day's build writes the adjustment through C2's writer (`cobalt.cards.legs`) only. A writer refusal is never forced and never fails the build: it becomes an unresolved item, rendered and carried until resolved.

```
LegsGateway()                          the build's one door to cards.legs: position, history, record_correction, record_exit
diff(trade, position) -> dict          per leg seq: the export vs the current legs (pure)
writes_for(diff) -> list[dict]         the writes a diff asks for (pure)
apply(work, *, legs, now) -> dict      those writes; a LegRefused stops the card's writes and is returned as an item
for_trade(trade, inputs, card, ...)    one matched trade's stored keys, inputs and work
realized(card, rec, refused_cards)     realized R (realized_r.1) over the current legs read
unresolved(day, ...)                   the day's open items
```

## The diff (D5-1)
- seq 0: the export's entries together (shares, the average entry at 4 places, the first entry's time) against the card's current entry leg.
- seq k: the k-th export exit execution against Cobalt's exit leg of seq k.
- Fields compared: shares, price, time (to the second). Each row has a state: `match`, `mismatch` (with its fields), `export_only` (an export exit with no Cobalt leg), `cobalt_only` (a Cobalt leg with no export execution) or `entry_not_written` (a card with no entry leg).
- Held after each leg, on both sides.
- His rows (every leg not from the trading log) are listed as history.
- Stored once as `build_trade.derived["reconcile"]`, with `inputs["reconcile"]` naming the trading-log `drc_imports` id and the leg ids read.

## The writes (D5-2)
- A correction per mismatched leg, carrying only the differing fields, `flag = 'confirmed'`.
- An export exit Cobalt never recorded becomes a new exit leg: `record_exit` typed, at the build's clock (D5-b). Then one correction sets the export's time.
- Every write carries `source = 'trading_log'` and `source_import_id` = the trade's `trading_log_import_id`.
- A card with no legs gets no entry leg, because the entry writer carries no import id (D5-a). Its exits run on the pre-C1 basis that `running_shares` reads.
- A Cobalt leg with no export execution gets no write, because no writer removes a leg (D5-c). It becomes an unresolved item.
- Writes happen only on the event day's build (`build.build_date(check=True)`) and only for a trade with no `inputs.carried_from` (D5-d). A carried trade and a re-paired date store and render the diff, then `adjustment not written — <carried trade | re-paired date>`. The dry run is `plan_note` alone and writes nothing.

## The refusal (D5-3)
- An item holds the card id, trade id, leg ids, the export rows, the refusal text and `code` verbatim, and `since`.
- The items live on `build_day.derived["unresolved"]`. The note shows each as `unresolved: card <id> — <refusal>` in `drc-trades/reconcile` and in A31. The page shows it with K3-7's RESOLVE beside it.
- Items are carried from the DRC the day's book starts from (its seed's `from_day`) and kept from the day's earlier build.
- An item is cleared when this build's reconcile of its card succeeds (no refusal), or when a current `resolve` row of the day names its trade (a restated resolve is not current). One item per card, trade, code and refusal text.

## Realized R (D5-4)
- `cards.legs.realized_r` as `read_position` returns it, over the legs read after the writes. It is provisional while any current leg is estimated, and stored with `realized_r.1` and its legs.
- It reads `not computed — <reason>` when no card matched, the card has no legs, or the card's reconcile was refused (an open item other than D5-c's `no_writer`; `refused_cards`).

## 2026-10-04 — DRC D5
New module (card `prompts/2026-10-04/03-drc-d5-card.md`, rows D5-1 … D5-4). Tests: `tests/cobalt/test_drc_d5.py` (offline, through an in-memory legs door), `tests/cobalt/test_drc_d5_db.py` (the real writer, `migrated`), `tests/cobalt/test_drc_d5_experiments_db.py` (X11, RUN).

## 2026-10-04 — drc-d5 check
`unresolved` clears a carried item only on a SUCCESSFUL reconcile of its card (`reconciled_cards`: applied with no refusal), drops this build's own items for a resolved trade too, and folds items by (card, trade, code, refusal), so two D5-c items of one card are both carried. The diff keys are `export`, `export_only` and `export_held`, with no vendor name (L31). Check O2, A2, A4, A5.

## 2026-10-05 — drc-d5 check, pass 2
`refused_cards(items)` names the cards D5-4 reads as refused: every open item except D5-c's (`NO_WRITER_CODE`). A Cobalt leg with no export execution stops no write, so its card's realized R is computed over the current legs, not `not computed — the reconcile was refused`. Check B1.
