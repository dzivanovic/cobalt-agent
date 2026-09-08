# Trade Radar Card — Spec v0.1

**Status:** design mock, not implementation. Interactive reference: `prototype.html`.
**Question the card answers:** what does the trader need to *see* to pull the trigger in seconds — not what the system computes.

---

## 1. Ownership badges

Every field on the card carries one of three owners. The badge is part of the design, not decoration.

| Badge | Meaning |
|---|---|
| `COBALT` (blue outline) | Computed by Cobalt from `trade_def`, sizer, and live data. Read-only unless stated. |
| `YOU` (amber outline) | Trader input or override. Also marks hollow judgment dots. |
| `N/A (MANUAL)` (solid red) | Cobalt could not read the value; the trader entered it. Loud on purpose. |

Once a trader overrides a Cobalt value (currently: stop), the badge flips to amber `YOURS` and a `↺ <cobalt value>` link restores it.

---

## 2. Lifecycle states

```
WATCH ──accept──▶ ARMED ──price hits trigger──▶ TRIGGERED ──fill──▶ IN-TRADE ──▶ TERMINAL
  ▲                 │                                                              (closed · passed · expired · missed)
  └────disarm───────┘
```

### 2.1 WATCH (default)
Purpose: decide whether to arm, and at what key.

- **Header** — rank chip (`#n · score`), ticker, direction arrow (long green ↑ / short red ↓), `setup → trade name`, one-line *why on radar* (≤ 90 chars, no numbers the dots already carry), day-mode badge, dashed `plan branch · empty` placeholder.
- **Semaphore** — one dot per entry variable. Solid = Cobalt-scored (red 0 / amber 1 / green 2 with a 1–10 grade in the reasons list). Hollow = judgment variable (Tape, Conviction) — trader scores it. Tap any dot → its WHY line; tap a hollow dot → 1–10 pick strip. Optional `reasons ⌄` expander lists every dot: colour · grade · category · reason.
- **Key row** — five grade buttons A+ / A / B / C / pass with dollar budget under each. Cobalt's proposed key is highlighted; keys outside `enabled_grades` are dimmed (dollars still shown). Trader may pick any enabled key.
- **Metrics strip** — Stop (editable), Shares, Risk $ used, Trigger + live signed distance.
- **Action row** — `ACCEPT · ARM {key}` primary, ▲ ▼ step the key within enabled grades.

### 2.2 ARMED
Purpose: wait. Nothing to decide except *disarm*.

- Locked summary strip: 🔒 key · shares · stop · risk $, badge `cobalt · locked`.
- Huge distance-to-trigger readout with last, %, and a progress bar toward trigger. Amber inside 25% of stop distance, green once through.
- `DISARM` secondary button; hotkey name shown (`{DAYMODE}-{KEY}-{SIDE}`).

### 2.3 TRIGGERED (strike alert)
Purpose: pull the trigger. This exact layout is the phone push notification.

- Ticker + arrow at 40px, `triggered · cobalt` badge.
- Three numbers only: **Key · Shares · Stop** at 34px.
- Hotkey name in a box. Nothing else is readable at a glance by design.

### 2.4 IN-TRADE
Purpose: manage the position. Key is frozen.

- **Stop line** — editable (±1¢ nudge, typed value, Enter commits, Esc cancels). *Room* to stop shown; red under 30% of planned distance.
- **Next exit** — 1R primary (green), 2R secondary.
- **Attempt** — `n / max` per ticker per day, "k left today".
- **Trail** — Cobalt proposes, trader selects one pill (from `trade_def` capabilities); optional WHY.
- **Trade health** — every scored entry variable re-checked live: holding (green dot) · ↓ deteriorating (amber pill) · ↓↓ broken (red pill). Summary `all holding` or `n deteriorating` with reasons line.
- **Shares running** — typed count, `½ off` / `⅓ off` / `flat` / `reset`. Scale buttons compound off the *running* count (DAS semantics). Shows sold count and open risk (running × room).
- **Fill recompute** — shares @ fill, Δ shares vs plan, Δ distance; ⚠ when distance drifts > 20%.

### 2.5 TERMINAL
Muted 55% strip: state · ticker · arrow · time · key/shares/stop · outcome note. Grouped by state / ticker / time.

---

## 3. Sizes

| `size` | Where | Notes |
|---|---|---|
| `leader` | Ladder #1 open | Full header incl. why line. |
| `compact` | Ladder #2…n open | Same content, tighter. |
| `strip` | Every collapsed ladder row | rank · ticker · setup → trade · key · sh · stop · distance · day-mode. 52px. |
| `phone` | 390px frame | Why line hidden in-trade; fill recompute collapses to one line. |

Card minimum width ≈ 560px for `leader` / `compact` (in-trade scale-out row is the widest). Phone inner width 366px.

---

## 4. Radar surface (ladder)

- One ladder, all N tickers as strips, ranked. **#1 and #2 open by default**; any row toggles open/closed; `collapse all` / `top 2` controls.
- Open row = card + **detail column** (rank breakdown, levels 1R/2R, why, reserved *notes · chart · news* slot). Detail sits beside the card and drops below it when the window is narrower than ~1150px. This lets the radar run at one-card width beside DAS or widen to show detail.
- **Promote ↑** on rows #3+: pins that ticker to #2. Rank chip is unchanged — position moves, Cobalt's opinion doesn't. `promoted · release` returns it.
- ARMED / IN-TRADE cards pin above WATCH regardless of score.

---

## 5. Math (from the ASET sizer)

```
day budget   = daily_stop × day_mode_mult        (¼ · ½ · 1; forced ¼ before 09:00)
key budget   = day budget × grade %              (A+ 80 · A 30 · B 15 · C 5 · pass 0)
distance     = |trigger − stop|
shares       = ⌊key budget ÷ distance⌋
risk used    = shares × distance
1R / 2R      = trigger ± distance / 2·distance
conviction   = mean(all dot grades incl. judgments) / 10
proximity    = clamp(1 − |last − trigger| ÷ (3 × distance), 0, 1)
rank score   = round(conviction × proximity × 100)
```

Score is exposed as an opaque number (not a visible sum) so per-dot weights can be added later without changing the UI.

---

## 6. Data contract (per ticker, as consumed by the card)

```
ticker, dir (long|short), setup, trade, why
trigger, last, stop, stopNote, fill
proposedKey, enabledGrades[]
dots[]: { label, score 0|1|2 | null, grade 1–10, why }   // score null = judgment dot
trails[], defaultTrail, trailWhy[]
attempt, attemptMax
health[]: { label, status ok|warn|bad, note }
hotkeyPrefix (optional; default = DAYMODE)
terminal (closed|passed|expired|missed), terminalTime
```

Session-level: `clock`, `dayMode`, `dailyStop`.

---

## 7. Visual system

- Background `#11151c` card on `#0d1117` surface; borders `#1f2531`; text `#e6e9ef` / `#aeb5c2` / `#7d8595` / `#5b6271`.
- Cobalt blue `#4f8dff`; trader amber `#d9a24a`; long green `#35c77a`; short/alert red `#ef5b6b`; manual-override red `#ff5c6c`.
- Type: JetBrains Mono for every number, ticker, badge, and control label; IBM Plex Sans for prose.
- Hit targets ≥ 44px on phone; scale-out buttons 34px on desktop.
