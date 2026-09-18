# `src/cobalt/aset/radar_panel.py`

Read-only view-model, builder, and rendering layer for the S2-P3 Trade Radar panel. It has no persistence methods and never calls the ASET sheet's rendering helpers, because those helpers can initialize schemas or attest a note while painting the write-capable sheet.

## Views and validation

Every structured presentation object is a strict Pydantic model. `PoolRecord` and `MembershipRecord` validate the database-shaped reads before they become `PoolView`, `PoolRow`, `ChurnDelta`, and `BannerView`. `CardView`, `DotView`, `HealthView`, `LadderView`, and `RadarPanelView` are the typed card-shell contract.

`build_pool_view()` reads the pool row first, derives the membership trading day from `last_scan_at` in ET, validates the `radar.pool` mirror through `PoolBlock`, reads `radar.scan_interval`, and then requests every membership episode for that pool/day. It fails loudly when any required source is absent or malformed, when a stored stage failed, or when `radar_pool.members` disagrees with the number of open admitted episodes.

Membership categories are intentionally distinct:

- current: `entered_at` exists and `left_at` is absent;
- departed: both `entered_at` and `left_at` exist;
- never-admitted exclusion: `entered_at` is absent, whether its exclusion episode is still open or already closed.

The clock's current session and the stored scan session are separate fields. The rank-metric label is selected from the stored scan session, so rendering during `market_reset` or `overnight` does not attempt to index a three-session metric map with a five-session clock value.

## Cursor and freshness

`parse_since()` refuses missing, malformed, naive, or future timestamps. The initial HTML request is an explicit snapshot with no churn. Refreshes count admitted `entered_at` and `left_at` values strictly later than the supplied cursor. The returned cursor is the greatest timestamp actually observed in the committed pool/membership read, never HTTP response time, so scan-start timestamps cannot be skipped by a later request.

Staleness begins after twice the configured `radar.scan_interval`. Source degradation, stale scans, and retained prior-day data are separate banners. Configuration or store failures raise `RadarPanelError`; they never become a plausible zero-member view.

## Card shell

`CardView.from_contract()` adapts the hub-cut `aset_sizings`-shape fixture while requiring UI-only fields such as WHY, dots, health, and trails to be supplied explicitly. It never invents absent presentation data. Contract cards preserve supplied 1R/2R values; non-contract cards derive only those two targets from stored trigger/stop/direction. It does not compute score, sizing, shares, grade budget, or risk used.

`order_cards()` pins ARMED, TRIGGERED, and FILLED (`IN-TRADE` on display) above WATCH cards, sorts WATCH by descending `card_score`, and moves terminal cards to the muted terminal section. `build_ladder_view()` reads open cards and returns the ruled F8 empty state when no radar-origin card exists. A radar-origin row fails loudly until S2-P2 wires the complete contract.

## Rendering

`render_pool()` and `render_ladder()` are pure functions using `html.escape` for source-controlled text. `render_radar_page()` composes them with inline local CSS and JavaScript. The first two cards are open, other cards remain 52 px strips, and `collapse all` / `top 2` are client-only. Promote and judgment controls are disabled with `title="S2-P2"`.

The detail order is levels, rank + WHY, news, notes, then an empty chart slot. At `max-width:1149px` detail drops below the card; the 430 px phone rule uses a 366 px inner width, and `?frame=phone` adds the preview frame.

The refresh loop replaces only the complete pool layer, including its status/count/session/timestamp labels. It advances the cursor only after a successful HTTP/JSON/fragment replacement. Failure retains the last data, marks it stale, and adds a red refresh-failure banner; replacing the pool layer after recovery removes only that transport failure while preserving server-side degraded/stale banners. Ladder DOM is untouched, so expansion state survives.

## Public functions

- `build_pool_view`, `build_ladder_view`, `build_radar_panel`
- `parse_since`, `order_cards`, `pool_api_payload`
- `render_pool`, `render_ladder`, `render_radar_page`, `render_failed_page`

