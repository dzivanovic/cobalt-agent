# `src/cobalt/aset/radar_panel.py`

View models, builders and renderers for the Trade Radar page. The pool layer (S2-P3) is read-only. The card ladder (S2-P2 STEP-8) reads `"user".radar_cards_v` and offers the trader's taps as `fetch` POSTs to the allowlisted `/radar/card/{id}/…` routes in `web.py`. The module itself never writes, never initializes a schema and never attests a note, because the ASET sheet's rendering helpers can do all three while painting.

## Views and validation

Every structured presentation object is a strict Pydantic model. `PoolRecord` and `MembershipRecord` validate the database-shaped reads before they become `PoolView`, `PoolRow`, `ChurnDelta` and `BannerView`.

`build_pool_view()` reads the pool row first, derives the membership trading day from `last_scan_at` in ET, validates the `radar.pool` mirror through `PoolBlock`, reads `radar.scan_interval`, then requests every membership episode for that pool/day. It fails loudly when any required source is absent or malformed, when a stored stage failed — except a per-ticker bars poll failure (`failed_stage='bars'` with its `poll failures: <n>` stamp and named rows), which renders as a `BARS POLL FAILED` DEGRADED banner naming each ticker, reason and since-time (R21 2026-09-21); a lifecycle refusal or dropped `bars` stage still fails — or when `radar_pool.members` disagrees with the number of open admitted episodes.

Membership categories are intentionally distinct:

- current: `entered_at` exists and `left_at` is absent;
- departed: both `entered_at` and `left_at` exist;
- never-admitted exclusion: `entered_at` is absent, whether its exclusion episode is still open or already closed.

The clock's current session and the stored scan session are separate fields. The rank-metric label is selected from the stored scan session, so rendering during `market_reset` or `overnight` does not index a three-session metric map with a five-session clock value.

## Cursor and freshness

`parse_since()` refuses missing, malformed, naive or future timestamps. The initial HTML request is an explicit snapshot with no churn. Refreshes count admitted `entered_at` and `left_at` values strictly later than the supplied cursor. The returned cursor is the greatest timestamp actually observed in the committed pool/membership read, never HTTP response time.

Staleness begins after twice `radar.scan_interval`. Source degradation, stale scans and retained prior-day data are separate banners. Configuration or store failures raise `RadarPanelError`; they never become a plausible zero-member view.

## The card ladder (S2-P2 STEP-8)

**One read.** `build_ladder_view()` calls `CardStore.radar_board_cards(today ET)` — every open `radar_cards_v` row plus today's terminal ones, each with its `card_dots` — and validates every row through `RadarCardRow`, whose fields are exactly the view's columns plus `dots: list[Dot]`. The module refuses to import if those columns and `cards.radar.FIELD_OWNERS` disagree, so a column cannot be added without its owner badge. P3's `CardView.from_contract` adapter and its contract fixture path are gone.

**Only what a card needs.** With no rows the ladder is `"No radar cards today"` and nothing else is read. With rows it reads, and fails loud on any of:
- the trader settings (`TraderSettings._build`) — sheet dollars and the day-mode config;
- today's rung, READ-ONLY: `DayModeStore.for_date` + `decided_or_stage1` (`_decided_rung`; tests pass `rung_source`);
- the `card.dot.red_max` / `card.dot.amber_max` tunables for dot colours.

**Order** is `cards.radar.ladder_order` — the one ladder order, shared with the receipt's tie policy: pinned ARMED/TRIGGERED/FILLED, WATCH by score with nulls last, one promoted card to #2 without moving its rank chip, terminal separate.

**`CardView`** carries, per card: the live trigger/stop (`entry`/`stop`) and the formation evidence (`trigger_price`/`structural_stop`) side by side; 1R/2R from the live pair; grade, tapped/sized grade and snap notice; proposed key (null → "tap to propose") and score suppression; the key row (`KeyView` per A+/A/B/C: dollars on today's sheet, enabled, proposed, tapped, sized); dots; health pills; `badges` = `FIELD_OWNERS`.

**Dots (`DotView`).** Hollow means nothing counts toward conviction yet. A shadow dot stays hollow and shows `shadow n` (its engine grade) until he taps it; a human dot is hollow until tapped, never a neutral 5; a desk or N/A dot shows `n/a <reason>`. A tap fills the dot with his grade. Colour comes from his grade when tapped, else the engine grade. Owner is `YOU` for human or tapped dots, `COBALT` otherwise. Every dot of a live (non-terminal) card has a tap strip.

**Health** renders the pills the S5 stage stored on a FILLED card (`health.pills`); `n/a` renders as a dashed red pill, never a guessed status.

## Rendering

`render_pool()` and `render_ladder()` are pure and escape every source-controlled string. `render_radar_page()` renders the card ladder FIRST and the pool view BELOW it (desktop and phone frame; ruled 2026-09-21, R3); both layers keep their ids and the refreshers still replace them by id, so the order is page layout only. `render_degraded_line()` renders the slim red line ABOVE the card ladder (desktop and phone frame; ruled 2026-09-21, R10): the pool view's DEGRADED and STALE banner text — never RETAINED PRIOR-DAY DATA (R11) — `hidden` with no box when there is none, and `refreshPool` mirrors the DEGRADED / STALE banners of the pool layer it placed (or, on a failed refresh, the old layer's REFRESH FAILED) into it, writing only on a change — a second rendering, never a second degraded computation.

The `STALE` badge (ruled 2026-09-21, R36): `build_pool_view` derives `PoolView.bars_stale_tickers` (ticker → `<reason> since HH:MM ET`, `exclude=True`, so `/api/radar/pool`'s JSON is unchanged) from `poll_failures`, only in the `poll_only` case — the state the `BARS POLL FAILED` banner names; a second rendering, never a second staleness computation. The badge sits in the ticker cell of a `current` pool row and, keyed by ticker (so a lifecycle-polled card outside the pool is marked too), inside the card strip's ticker, beside ARMED `last` and beside LEVELS `last`; never on departed / excluded rows or terminal cards. The row badge follows every pool refresh; `mirrorStale()` adds / removes the strip badge in place after `mirrorDegraded()` without re-sorting, re-fetching or opening / closing a card, and the two in-card badges follow the next reload or card action. It follows the POLLER's clock only (180 s, RTH, plus `error`), not the evaluator's or the pool STALE banner's. **Wording `STALE`, 9 px monospace and the red `.badge` geometry are ASSUMED — size, wording and colour were not ruled.**

- Each displayed card field renders as `data-field="<column>"` with its label and its `COBALT` / `YOU` / `LEDGER` badge (`BADGED_FIELDS`).
- Each dot is a button that toggles its hidden `tap-strip` of ten `data-grade` buttons.
- The key row (WATCH only; `KEY_EDITABLE`) shows every key with its dollars. A disabled key is greyed (`key-disabled`) but stays tappable, because a tap on it records the tapped key and sizes at the nearest enabled key below (R8). `pass` sits beside them. From ARMED on, the row says the key is frozen.
- The snap notice renders as an amber block; `card-status` shows the result of the last tap.
- `promote ↑` shows on WATCH cards from position 3; the promoted card shows `release ↓`.
- News and notes say no source is wired (S3); the chart slot is reserved. The detail order stays levels, rank + WHY, card, news, notes, chart.

`PANEL_JS` uses one delegated click handler. A tap `fetch`es `POST /radar/card/<id>/key | /dot/<factor> | /promote | /release` with a form body. A refusal shows `REFUSED <status> · <reason>` in the card; success re-fetches `GET /radar`, swaps only `#ladder-layer`, and restores which cards were open. The pool refresh loop is unchanged: it replaces only the pool layer and advances its cursor only after a successful replacement. The focus law holds — no `alert`, `confirm`, `prompt`, `.focus`, `autofocus`, form or meta refresh.

At `max-width:1149px` detail drops below the card; the 430 px rule uses a 366 px inner width, and `?frame=phone` adds the preview frame.

## Public functions

- `build_pool_view`, `build_ladder_view`, `build_radar_panel`
- `parse_since`, `pool_api_payload`
- `render_pool`, `render_degraded_line`, `render_ladder`, `render_radar_page`, `render_failed_page`

## Gotchas

- `order_cards()` (P3) is gone; `cards.radar.ladder_order` is the one order.
- Terminal cards are today's only: a card that expired yesterday is history, not ladder.
- The fixture `panel-cards.contract.json` is no longer read by the panel; the offline tests build `radar_cards_v` rows by running the S5 stage over the hub-cut bars fixture until the hub cuts `panel-cards.real-shape.json`.

---

## 2026-09-17 — S2-P4: value column (ruling R1, Astra R1-19)

`MembershipRecord` and `PoolRow` gain `rank_metric` (`RankMetricName | None`)
and `rank_value` (`Decimal | None`). On `MembershipRecord` both are
**required but nullable**. NULL is a pre-deploy episode. A row missing the
keys means a store forgot to select them, and it fails validation
(`RadarPanelError`). `_row` threads both through to `PoolRow`, so the name
shown is the per-row metric that actually ranked the ticker (a screen
override's name included), not the view-level session metric.

`render_pool` adds a `value` column after `ticker`. `_rank_value_cell`
prints `<metric> <value>`, with the stored NUMERIC normalized (trailing
zeros dropped, never rounded). It prints `—` when both are NULL and
`<metric> —` when only the value is NULL.

## 2026-09-24 — float handicap H1 STEP-7: the pool-row badge and the header state (v3 §4)

`MembershipRecord` gains `raw_rank`, `handicap_factor` and `handicap`
(`HandicapRecord | None`, validated against radar's own model). Like
`rank_metric`, they are required but nullable. `PoolRow` carries them
with `exclude=True`. `_handicap_cell`, in the ticker cell, renders the
following:

- A factor below 1 renders the COBALT-owned `HANDICAP (shadow)` badge
  plus `float <v>M / cap $<v>M → group (<reason>) · pos <p> → <effective>`.
- An unknown name the block skipped renders only the line
  `… → group (unknown) · unknown → not applied`.
- Factor 1 or NULL renders nothing.

Rows still sort by `last_rank`: shadow never moves a row.

`PoolView.handicap_state` and `handicap_detail` are both `exclude=True`
and are computed by `_handicap_state` from the block and
`degraded_sources`:

| Condition | handicap_state | handicap_detail |
|---|---|---|
| Block absent | `not configured` | — |
| `handicap` entry whose reason starts with `radar.handicap.INOPERATIVE` | `degraded — inoperative` | the reason minus that prefix (R54) |
| Any other `handicap` entry | `degraded` | its reason |
| `mode: live` | `degraded` | — (H1 never shows live) |
| Otherwise | `shadow` | — |

For a configured block, the pool header renders
`handicap: <state> (<detail>)`. The DEGRADED banner now appears when
`pool.degraded` is set or a `handicap` entry exists. A handicap-only
degradation leaves `degraded` False, and `_banner_name` names it
`handicap (<reason>)`.

**Gotcha — the healthy pins:** `test_radar_panel_cards.py`
SHA-pins the block-absent pool HTML and the API JSON, and that file is
not touched. So, with the block absent:

- `render_pool` output is main's, byte for byte.
- `render_radar_page` shows `handicap: not configured` in
  `#handicap-unconfigured`, above the pool layer. That line updates on
  page load only; a pool refresh does not update it.
- The new fields never reach `pool_api_payload`'s `pool` dict; its `html`
  carries them.

## 2026-09-28 — S3 exits C3: TRIGGERED and IN-TRADE (v3 §2 / §3 / §5; R67, R38)

**Models.** `LegView` (one `legs_current_v` row: `id`, `seq`, `kind`,
`shares`, `price`, `flag`, `price_source`, `at`, `stop_in_force`, `preset`,
`held_stated`) and `InTradeView` (`running`, `basis`, `legs`,
`realized_value` / `realized_provisional` / `realized_reason`, `stop_owner`,
`distance_change_pct` / `drift_warning_pct` / `drift_warned`). `CardView`
gains `position: InTradeView | None` and `position_error: str | None`.
`RadarCardRow` is unchanged (it must equal `FIELD_OWNERS`).

**The read.** `read_in_trade(card_id)` — READ-ONLY: `legs.read_position`
(THE running read + `realized_r`, on a transaction it rolls back),
`CardStore.stop_owner`, and the drift stored AT THE FILL = the FILLED
transition's evidence (`distance_change_pct`, `drift_warning_pct`,
`drift_warned`; an entry-price correction never rewrites it).
`build_ladder_view(…, position_reader=None)` reads it for every FILLED /
CLOSED row (default `read_in_trade`; `build_radar_panel` passes the argument
through). A read that fails is said ON THE CARD (`position_error` → a
`FAILED · position unreadable: …` line) instead of failing the ladder; a
CLOSED card with no legs (`no_position`, closed before C1) has none.

**Render.** Every tap is `_card_form(card_id, path, inner, source=…)`:
- on the panel, a `<div class="s3-form" data-card-id data-path data-card-tap>`
  whose `type="button" data-tap` button the panel script posts by `fetch`
  (the click handler collects the block's `input[name]` fields; an unticked
  checkbox posts nothing) — the ladder keeps its **focus law** (no `<form`,
  no native POST, no navigation; `test_rendered_page_with_cards_keeps_the_focus_law`);
- on the sheet (`source="sheet"`), a plain `<form method="post">` to the same
  route.

- **ARMED**: the `TRIGGERED` tap (O7 A).
- **TRIGGERED** (`_triggered_block`): three numbers — `last <price> · bar time
  not stored` (X6-R), `entry`, `stop` — the `FILLED @` tap (price prefilled
  from `last_price`, EMPTY when it is NULL — never the entry; hidden
  `prefill` = what the screen showed; shares prefilled from the card's
  `shares`, editable) and `PASS`.
- **IN-TRADE** (`_in_trade_block` → `render_in_trade`): `running <n> sh`
  (+ `(basis <b>)` when not `legs`), realized R with `(provisional)` or its
  reason, the drift line `drift <pct>% vs P <P>%` (`· WARNING — past plan`
  when warned) or `⚠ RE-READ STOP — setting fills.drift_warning_pct missing,
  warning not evaluated` when P was NULL at the fill; the stop line — his
  stop, the amber `YOURS` badge and `Δ <stop − structural> vs Cobalt` when
  `stop_owner` is `yours`, `Cobalt stop <structural_stop>` ALWAYS beside it
  (`NULL — no Cobalt stop` on a manual card); the note line — `↺ <cobalt
  value>` only when `structural_stop` is not NULL (O19 A) and `move stop`;
  ½ · ⅓ · flat (✓ checkbox, `confirm=1`) · typed (shares), each carrying
  `running_before` = the running it rendered and `prefill`; `HOLDING`; the
  current legs (price, shares, flag · source, ET time, `gap <stop_in_force −
  structural_stop>`) with `✓ correct` on each `estimated` leg.
- **CLOSED** (terminal): `_terminal_legs` lists the card's `estimated` legs
  with `✓ correct` ("estimated — confirm the price", v3 §3).
- `used_risk` is not rendered in IN-TRADE (C2's X-UR: it stays at the
  pre-exit count until the next stop edit). The NOTES section keeps its text
  (the note is C4's).

`PANEL_JS`: the `[data-tap]` branch of the click handler; the status line
shows `payload.notice` (e.g. the drift banner on a fill, "estimated — listed
for correction" on an exit) as it shows `snap_notice`.

**Gotcha — the pins.** `test_radar_panel_cards.py`'s `_ladder` passes a
constructed `POSITION` (L32) so the ladder never depends on a database, and
`PIN_HEALTHY_LADDER_SHA256` was re-captured for C3's new blocks (the pool and
API pins are untouched). The "FILLED never shows" check exempts the
`FILLED @` tap label (the design's words).
