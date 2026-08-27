# Data-Source Spike, Phase A — Finviz Elite Export API

**Method:** empirical probing only. There is no official Finviz API
documentation; the 9 screenshots in `docs/90 - References/` (Finviz's
own in-app "Automating Export" panels) were the starting point, not the
spec — several details below were discovered by direct HTTP requests
that contradict or extend what the screenshots show. Every finding is
tagged **CONFIRMED** (fetched, evidence attached) or **INFERRED**
(pattern/plausible, not independently verified) — the latter is Phase
B's job to close (Dejan capturing the Finviz web pages, including the
collapsed "Learn More" parameter panels the screenshots don't show).

**Constraints honored:** read-only GETs only; ~1.2s between requests
(≈50 requests total across two probe runs); auth token resolved via
the existing vault-backed `FinvizApiClient` and never printed or logged
— every URL and error string below is scrubbed. No FMP, no
TradingView, no pipeline/old-tree code changes.

**Probed:** 2026-08-27, against a live Finviz Elite Elite-tier account,
ticker MSFT as the reference instrument for `/export/stock`.

---

## 0. Confirmed baseline from the old tree (`FinvizApiClient` + friends)

Read: `src/cobalt_agent/skills/research/finviz_api.py` (the HTTP client —
KEEP-AS-IS per TRIAGE, "grows"), `finviz_extractor.py` (Playwright
scraper, TRIAGE-KILLed, browser-only info, not API-relevant),
`enrich_metadata.py` (a live caller), and the `dev_utils/live_run_finviz*`
scripts (thin wrappers, no new information).

**What the client already gets right (CONFIRMED against my own probing):**
- Base URL `https://elite.finviz.com`, token appended as `&auth=<token>`.
  Matches every screenshot exactly.
- `export.ashx?v=…&f=<filters>&c=<col indices>` for screener — the
  `.ashx` path still works but 301-redirects to `/export/screener` (the
  screenshots say this explicitly; I didn't re-verify the redirect
  itself since old-tree code is out of scope to touch, but the
  destination path is confirmed reachable directly).
- `f=` filter syntax (`key_value` comma-joined, e.g.
  `sh_price_o1,sh_avgvol_o5000`) — CONFIRMED, used throughout my probes.
- `c=` column-index selection — CONFIRMED exactly: requesting
  `c=0,1,2,3,4,5,6` returned precisely those 7 columns in that order.
- `MASTER_COLUMNS` (indices `0`–`150`, 151 total) — CONFIRMED: a single
  `c=0..150` request returned exactly 151 named columns (full list in
  §1 Screener below). The client's assumption that this is a stable,
  complete field universe is validated.
- `t=` as a direct multi-ticker override for `export.ashx` (used in
  `enrich_metadata.py`, bypassing the filter compiler) — CONFIRMED as a
  general pattern; ticker-list-via-`t=` also works on other endpoints
  (see per-family notes).

**Where probing contradicts or extends the client's assumptions:**

| Client assumption | Finding |
|---|---|
| `get_news(ticker)` — passing a ticker filters the news feed (`news_export.ashx?t={ticker}`) | **CONTRADICTED.** `/export/news?v=1` and `/export/news?v=1&t=MSFT` returned byte-identical first rows (same headline, same everything) across the full response. `t=` appears to have **no effect** on `/export/news` — it always returns the general market feed. See §1 News and §4. |
| `get_quote()` targets `quote_export.ashx?t={ticker}&ty=c&p=d&b=1` | **Superseded, not confirmed necessary.** The documented current endpoint is `/export/stock?t=…&p=…` with no `ty=`/`b=` params at all (confirmed in the Stock screenshot's example URL). New-core `prefill.py` already moved off this legacy path for exactly this reason (the `.ashx` form 301-redirects). `ty=c`/`b=1` were not independently tested — they may be inert legacy params from an older API surface. |
| `PRESET_QUERIES` use `v=150`; `execute_dynamic_screener` uses `v=152` | **Not a contradiction.** The official screenshot's own example uses `v=111`. All three values I've now seen work — `v=` looks like a Finviz-internal "view/column-preset ID" selector, not a version number; multiple valid IDs coexist. |
| `PRESET_QUERIES` all include `ft=4` | **UNVERIFIED — not isolated.** I never tested `ft=` in isolation (the client always pairs it with a filter set). Meaning unconfirmed; likely a filter-type/universe toggle. Flagged for Phase B. |
| `tc=7` used nowhere in the old client, but discovered on the Insider screenshot | Confirmed as a working filter parameter (see §1 Insider) but its **value semantics are unknown** — "7" is a Finviz-internal transaction-type code, not a raw SEC Form 4 code letter. INFERRED that other integers select other transaction types; not probed. |

---

## 1. Per-family findings (all eleven)

Each entry: endpoint path, params tried, **CONFIRMED** result, and gaps.

### Screener — CONFIRMED, working exactly as documented
`GET /export/screener?v=<id>&f=<filters>&c=<col indices>&auth=…`
- `v=111` (default view) → 200, 11 columns (`No., Ticker, Company,
  Sector, Industry, Country, Market Cap, P/E, Price, Change, Volume`).
- `v=152&c=0,1,2,3,4,5,6` → 200, exactly the 7 requested columns.
- `v=152&c=0..150` (all indices) → 200, **all 151 named columns**,
  confirming the client's `MASTER_COLUMNS` claim. Full field list (a
  sample of the notable ones — Tier-1/Tier-2 relevant fields bolded):
  `No, Ticker, Company, Sector, Industry, Country, Market Cap, P/E,
  Forward P/E, PEG, P/S, P/B, P/Cash, P/FCF, Dividend Yield, Payout
  Ratio, EPS(ttm), EPS Growth (This/Next Year, Past/Next 5Y, QoQ), Sales
  Growth (Past 5Y, QoQ), **Shares Outstanding, Shares Float, Insider
  Ownership, Insider Transactions, Institutional Ownership,
  Institutional Transactions, Short Float, Short Ratio**, Return on
  (Assets/Equity/Invested Capital), Current/Quick Ratio, LT/Total
  Debt-to-Equity, Gross/Operating/Profit Margin, Performance (Week
  through YTD, plus **1/2/3/5/10/15/30-min and 1/2/4-hour rolling
  performance — 10 intraday-granularity columns**), Beta, **Average
  True Range**, Volatility (Week/Month), 20/50/200-day SMA, 50-day &
  52-week High/Low, RSI(14), Change from Open, Gap, Analyst Recom,
  Average/Relative Volume, Price, Change, Volume, **Earnings Date**,
  Target Price, IPO Date, After-Hours Close/Change/Volume, Book/Cash
  per share, Dividend, Employees, **EPS Next Q, Income, Optionable,
  Shortable, Short Interest, Float %**, OHL, Trades, [ETF-only block:
  Asset Type, ETF Type, Region, Category, Tags, AUM, NAV, Net Flows
  (1M/3M/YTD/1Y), multi-year Returns], **EPS/Revenue Surprise**,
  Exchange, Dividend TTM/Ex-Date, 52-Week Range, **News Time, News URL,
  News Title**, 3/5/10-year Performance, EPS/Sales Growth 3Y, Enterprise
  Value, EV/EBITDA, EV/Sales, Dividend Growth (1/3/5Y), Daily Digest.
- **New finding, not in any screenshot:** columns 135–137 (`News Time`,
  `News URL`, `News Title`) put a per-ticker latest-headline directly in
  screener output. Given `/export/news`'s `t=` filter doesn't work
  (above), **this may be the actual working path to per-ticker news**,
  not the dedicated News endpoint. INFERRED — only saw the column names
  exist and are part of the schema; didn't verify populated values for
  a specific low-news ticker vs. a high-news one.
- Gap: `ft=` parameter meaning unconfirmed (see §0).

### Portfolio — CONFIRMED endpoint exists, needs a real Dejan-owned ID
`GET /export/portfolio?pid=<id>&auth=…`
- Bare and `pid=1` both → **404, body `"Portfolio not found."`** — a
  specific, meaningful error (not a generic route-404), confirming the
  endpoint and `pid=` param both exist and are being validated, but no
  portfolio with ID `1` exists on this account. INFERRED that `pid=`
  needs one of Dejan's own saved-portfolio IDs from the Finviz UI —
  untested with a real one (none created yet). Gap for Phase B.

### Stock — see §2, the priority section.

### Groups — CONFIRMED reachable, response empty with params tried
`GET /export/groups?g=<?>&auth=…`
- Bare and `g=sector` both → **200, `text/csv`, empty body.** The route
  exists and doesn't error, but produces no rows with either param
  tried. INFERRED that a required param (view ID like `v=`, or a
  different `g=` enum value — Finviz's UI groups by sector, industry,
  country, capitalization) is missing. Gap for Phase B — this family is
  the least-confirmed of the eleven.

### Options — CONFIRMED
`GET /export/options?t=<ticker>&ty=oc&e=<expiry YYYY-MM-DD>&auth=…`
- `t=MSFT&ty=oc&e=2026-09-18` → 200, 206 rows, 17 columns: `Contract
  Name, Last Trade, Strike, Last Close, Bid, Ask, Change $, Change %,
  Volume, Open Int., Type, IV, Delta, Gamma, Theta, Vega, Rho`.
- Full Greeks present (Delta/Gamma/Theta/Vega/Rho) — stronger than
  §8 Tier-3's minimum ask (IV rank/skew/OI). IV rank/percentile and term
  structure are NOT directly given (only per-contract IV) — would need
  to be computed from repeated pulls across expiries/dates.
- `ty=` only tested as `oc`; other values (single-strike view?) INFERRED
  to exist, not probed (Tier-3 is "design now, build later" — matches
  the low-effort spend here).

### Latest Filings — CONFIRMED
`GET /export/latest-filings?t=<ticker>&o=<sort>&auth=…`
- `t=MSFT&o=-filingDate` → 200, 1828 rows, 6 columns: `Filing Date,
  Report Date, Form, Description, Filing, Document`.
- The `Form` column (10-K, 10-Q, 8-K, S-3, 424B5, Form 4, …) makes this
  a plausible, previously-unconsidered path toward §8 Tier-1's
  dilution-risk monitoring (effective S-3s/ATMs) — filter/scan `Form`
  client-side. Not filed as a direct requirements match originally;
  worth a design note.

### News — CONFIRMED, with the client-contradicting finding from §0
`GET /export/news?v=1[&t=<ticker>]&auth=…`
- `v=1` → 200, 180 rows, 5 columns: `Title, Source, Date, Url,
  Category`.
- `v=1&t=MSFT` → 200, 180 rows, **identical first row to the
  ticker-less call**. `t=` is not filtering. See §0's contradiction
  entry and §4.
- `v=` only tested as `1`; other values INFERRED to exist (maybe a
  blogs/press-release toggle) — not probed.

### Insider — CONFIRMED, filtering works
`GET /export/insiders?tc=<code>[&t=<ticker>]&auth=…`
- `tc=7` alone → 200, 200 rows (**hit what looks like a row cap** — see
  Managers/Funds below for a *documented* 500-row cap; 200 may be a
  separate, undocumented cap for this family, or coincidental — not
  isolated).
- `tc=7&t=MSFT` → 200, 94 rows — **different from the untargeted count,
  confirming `t=` DOES filter here** (unlike News). 12 columns: `Ticker,
  Owner, Owner CIK, Relationship, Date, Transaction, Cost, #Shares,
  Value ($), #Shares Total, SEC Form 4, SEC Form 4 Link`.
- `tc=` value semantics (why "7") — INFERRED/unknown, gap for Phase B.

### Managers — CONFIRMED, exact mechanics as documented
- List: `GET /export/managers?search=<partial name>&auth=…` — `search=
  berkshire` → 200, 10 rows, 14 columns (`Name, Portfolio Manager,
  Investor ID, Report Date, Portfolio Value, # Investments, New
  Purchased, Sold Out, Added, Reduced, Top 10 Concentration (%),
  Turnover (%), Time Held Top 10, Time Held All`). **500-row cap is
  documented in-app** (screenshot text), not hit here since the search
  matched only 10.
- Holdings: `GET /export/managers/<investor ID>/holdings&auth=…` (path
  segment, not a query param — confirmed both the bare-ID form and the
  name-slug form work per the screenshot; I used the bare-ID form live)
  → 200, 30 rows, 14 columns (`Ticker, Name, Type, Sector, Industry,
  Shares Held, Market Value, % Portfolio, Prev. % Portfolio, Change in
  Shares, % Change, % Ownership, Avg. Price, Q 1st Owned`).

### Funds — CONFIRMED, identical mechanics to Managers
- List: `GET /export/funds?search=<partial name>&auth=…` — `search=
  fidelity` → 200, **exactly 500 rows** — the documented row cap
  **CONFIRMED hit** in practice. 14 columns (same shape as Managers'
  list).
- Holdings: `GET /export/funds/<fund ID>/holdings&auth=…` → 200, 482
  rows, 11 columns (`Ticker, Name, Asset Category, Balance, Units,
  Market Value, % Portfolio, Prev. % Portfolio, % Change, Payoff
  Profile, Country`).

### Calendar — CONFIRMED, but a near-term window only, NOT deep history
`GET /export/calendar/{economic|earnings|dividends}?dateFrom=<date>&auth=…`
- All three sub-types respond: economic (8 cols, 64 rows), earnings (14
  cols incl. EPS/Revenue estimate-actual-surprise, 34 rows), dividends
  (6 cols, 116 rows) with `dateFrom=2026-08-20` (a week before the
  probe date, 2026-08-27).
- **`dateFrom` does not unlock historical archives.** A follow-up direct
  test: `dateFrom=2020-01-01` (far past) → **0 rows**; `dateFrom=
  2026-08-27` (today) → 34 rows, all dated today. The calendar exports
  hold a **narrow rolling window around the present** (roughly the
  surrounding 1–2 weeks in the first test), not a queryable historical
  archive — `dateFrom` filters *within* that window, it doesn't extend
  it backward. CONFIRMED via two independent probes.
- This matters for §8's "catalyst calendar" (fine — it's inherently a
  forward/near-term concept) but rules out using this endpoint for
  historical earnings-date backtesting; that needs the `earnings`
  columns already present in the Screener's 151-column export instead
  (`Earnings Date`, `EPS Next Q`) or FMP (out of scope here).

---

## 2. PRIORITY — `/export/stock`: intervals and history depth

**Fixed columns, all intervals:** `Date, Open, High, Low, Close, Volume`
(6 columns) — Volume is **present at every granularity tested**,
directly resolving §7's "re-verify volume availability" flag. **CONFIRMED.**

### 2a. Intervals (`p=` parameter)

Tested the full requested set (`i1, i5, i15, i30, h, d, w, m`) plus bare
numeric guesses (`1, 5, 15, 30, 60`) to check whether unrecognized
values silently default rather than error.

| `p=` value | Valid? | Rows (MSFT) | Span (first → last) | Extended hours? |
|---|---|---|---|---|
| `d` (daily) | ✅ CONFIRMED | 2522 | 08/16/2016 → 08/27/2026 (**~10.0 years**) | n/a |
| `w` (weekly) | ✅ CONFIRMED | 524 | 08/19/2016 → 08/27/2026 (**~10.0 years**) | n/a |
| `m` (monthly) | ✅ CONFIRMED | 486 | **03/31/1986** → 08/27/2026 (**~40.4 years — full listing history**, MSFT IPO'd March 1986) | n/a |
| `i1` (1-min) | ✅ CONFIRMED | 9451 | 08/13/2026 04:00 AM → 08/27/2026 06:04 AM (**~14 calendar days**) | **Yes** — starts 04:00 AM (premarket) |
| `i5` (5-min) | ✅ CONFIRMED | 2905 | 08/06/2026 04:00 AM → 08/27/2026 06:00 AM (**~21 calendar days**) | **Yes** — starts 04:00 AM |
| `i15` (15-min) | ✅ CONFIRMED | 390 | 08/06/2026 09:30 AM → 08/26/2026 3:45 PM (**~3 weeks**) | **No** — starts 09:30 AM (regular session only) |
| `i30` (30-min) | ✅ CONFIRMED | 2600 | **11/07/2025** 09:30 AM → 08/26/2026 3:30 PM (**~9.6 months**) | No — regular session only |
| `h` (hourly) | ✅ CONFIRMED | 1400 | **11/07/2025** 09:30 AM → 08/26/2026 3:00 PM (**~9.6 months**, same start date as `i30`) | No — regular session only |
| bare `1`/`5`/`15`/`30`/`60` | ❌ **Not intraday selectors** | 2522 (identical to `p=d` in every case) | identical to daily | n/a |

**Key findings:**
- Intraday bars exist and are real (not a daily-bar reformat) —
  timestamps carry HH:MM, granularity between consecutive rows matches
  the requested interval.
- **Depth is tiered, not uniform**, and the tiers don't follow interval
  size monotonically: `{i1, i5}` ≈ 2–3 weeks (with premarket/after-hours
  included), `{i15}` ≈ 3 weeks (regular hours only — the extended-hours
  cutoff happens between `i5` and `i15`), `{i30, h}` ≈ **9.6 months**
  (regular hours only, both sharing the exact same start date
  11/07/2025), `{d, w}` ≈ **10 years**, `{m}` ≈ **full listing history**.
- Bare numeric `p=` values are **silently ignored**, falling back to
  daily — they are not shorthand for `i5`/`i15`/etc. Anyone guessing
  `p=5` expecting 5-minute bars gets daily data with no error. This is
  a real footgun worth encoding as a validated enum in any new-core
  collector, not a free-text param.

### 2b. History depth / date-range parameters — Dejan's hypothesis

**Hypothesis under test:** ~10 years of history is available at *any*
timeframe via explicit range/date parameters (`dateFrom`, `dateTo`,
`range`, `limit`, `start`, `end` all tried as plausible names).

**Result: REFUTED for the parameter names tried; depth is fixed per
interval, not user-extendable via any of these seven guesses.**

Evidence — every one of the following, layered on top of `p=d`
(2522-row baseline) or `p=i1` (9451-row baseline), returned **exactly
the same row count and date span as the bare request, with zero effect**:
`dateFrom=2016-08-27`; `dateFrom=2016-08-27&dateTo=2026-08-27`;
`range=10y`; `range=1y`; `limit=5000`; `start=2016-08-27`;
`start=2016-08-27&end=2026-08-27`. Retested `dateFrom` and `range=10y`
on `p=i1` specifically (in case date-range only applies to intraday,
where the default window is shallow) — same null result: still 9451
rows, still the same ~2-week span.

**So, per interval, empirically:**
- **Daily/weekly: ~10 years is correct** — but it's the *fixed*
  window, not a floor extendable further back. Dejan's "10 years"
  instinct is right for these two intervals specifically.
- **Monthly: much more than 10 years** — full history back to listing.
  The "~10 years at any timeframe" framing undersells monthly.
- **Intraday (1–15 min): far short of 10 years** — 2–3 weeks only, a
  hard ceiling as tested. **30-min/hourly is the deepest intraday tier
  at ~9.6 months** — still nowhere near 10 years.
- **No confirmed mechanism extends any of these.** This directly
  bounds the backtesting design: a strategy backtest needing minute-
  granularity bars over months/years **cannot be built on Finviz
  alone** — Finviz's own depth ceiling for sub-hourly bars is weeks,
  not years. Daily/weekly backtesting over the past decade is
  well-supported; monthly essentially unlimited; 30-min/hourly
  backtesting is limited to the trailing ~9–10 months.

**Caveat or this section is over-claimed:** only seven plausible
parameter names were tried, chosen by pattern-matching Calendar's own
confirmed `dateFrom=YYYY-MM-DD` syntax plus common API conventions.
This is a real, evidence-backed **CONFIRMED negative result for those
seven names** — it is *not* proof no working parameter exists at all.
The Stock screenshot's own Google Sheets snippet literally names the
concept `[tickerAndTimeframeAndOptionallyDateRange]`, strongly implying
*some* date-range mechanism is real and documented somewhere Finviz
didn't expose to a static screenshot (the collapsed "Learn More" panel
on that page). **This is the single highest-value thing for Phase B to
resolve** — screenshotting that expanded panel would likely either
name the correct parameter or confirm it doesn't exist for this account
tier.

### 2c. What this means for the two consumers named in the task

- **Setups engine (live detection):** well served. 1-min/5-min bars
  with premarket included cover live intraday pattern detection for
  the trading day and the past couple of weeks for context/backtesting
  a *recent* setup by hand.
- **Backtesting:** partially served. Daily/weekly strategies: ~10 years,
  solid. Monthly: essentially unlimited. Anything needing systematic
  minute-or-hour-granularity backtesting across a real sample (§ Charter
  requirements' n≥30, TRIAGE sample-size law) over more than ~9 months
  **needs a second data source** — this was already flagged as a Pass 4
  gap in the original assessment and remains genuinely open; Phase A
  narrows exactly how much of a gap it is (30-min/hourly = ~9.6 months,
  not zero, but not enough for a multi-year minute-bar backtest).

---

## 3. Summary table

| Family | Confirmed capabilities | Gaps (Phase B / follow-up) | MVP relevance |
|---|---|---|---|
| **Screener** | Full 151-column field universe; arbitrary filter/column combos; multiple valid `v=` view IDs | `ft=` param meaning unverified | **Pillar 1 backbone** (already validated by existing `FinvizApiClient` usage) |
| **Portfolio** | Endpoint + `pid=` param exist (404 error confirms both) | No real portfolio ID to test against yet | Low — not named in requirements |
| **Stock** | 6-col OHLCV at 8 real granularities (d/w/m/i1/i5/i15/i30/h); volume present everywhere; depth tiers empirically mapped | **History-depth param name unconfirmed** (highest-priority Phase B item) | **Critical** — setups engine + backtesting both depend on this |
| **Groups** | Route reachable, 200 | Returns empty with every param tried — least-confirmed family | Unclear — not a named §7/§8 requirement |
| **Options** | Full per-contract chain incl. all 5 Greeks | IV rank/skew/term-structure need computing from repeated pulls, not given directly | Tier-3, "design now build later" — matches spike depth |
| **Latest Filings** | Per-ticker SEC filing list with `Form` type, sortable | — | **New candidate path** for §8 dilution-risk (S-3/424B) monitoring |
| **News** | General market feed works | **`t=` ticker filter does not work** — contradicts old client's assumption; Screener's `News Time/URL/Title` columns may be the real per-ticker path (unverified) | §5 news-monitoring agent — needs this resolved before building on it |
| **Insider** | Ticker filtering confirmed works; SEC Form 4 fields | `tc=` code meanings unknown | Directly satisfies §8 Tier-1 "insider transactions" |
| **Managers** | List (search, documented 500-row cap) + holdings (path-based, both ID forms work) | — | Satisfies §8 Tier-1 "institutional ownership concentration" |
| **Funds** | Identical mechanics to Managers; 500-row cap directly hit | — | Same as Managers |
| **Calendar** | Economic/Earnings/Dividends all respond | **Near-term window only — not a historical archive**; `dateFrom` doesn't reach back | Satisfies §8 "catalyst calendar" (forward-looking, as intended); does NOT serve historical earnings-date backtesting |

---

## 4. Contradictions with COBALT-REQUIREMENTS §7/§8

Located via the root pointer stub → `docs/00 - Project/COBALT-REQUIREMENTS.md`.

1. **§7 "single-stock up-to-the-minute OHLC bars (re-verify volume
   availability)" — RESOLVED, not a contradiction.** Volume is present
   in every `/export/stock` response at every interval tested. The
   flagged open question is closed: yes.
2. **§7/§5 implicitly assume Finviz news can be scoped per-ticker (the
   news-monitoring agent, catalyst tagging) — CONTRADICTED as currently
   testable.** `/export/news?t=<ticker>` does not filter; it silently
   returns the general market feed regardless. Anything designed around
   `FinvizApiClient.get_news(ticker)` actually filtering by ticker will
   silently get the wrong (unfiltered) data, not an error. This needs
   fixing at design time — either confirm the Screener's `News
   Time/URL/Title` columns as the real per-ticker path, or accept Finviz
   news as market-wide only and rely on other sources (FinancialJuice,
   X) for per-ticker news, per §7's own source list.
3. **§8 Tier-1 "halt/SSR status" — CONFIRMED GAP, Finviz cannot serve
   this.** None of the 151 screener columns nor any of the ten other
   families carry a halt or short-sale-restriction flag. This was
   already implicitly understood (not claimed as a Finviz field in
   §7), but Phase A makes it explicit: this requirement needs a
   different, direct-exchange or broker-side source entirely — no
   amount of Finviz Elite tier unlocks it.
4. **§8 Tier-1 "short interest and borrow" — partially served.**
   `Short Float`, `Short Ratio`, `Short Interest`, and a `Shortable`
   boolean are all present in the Screener's 151-column export
   (CONFIRMED). Actual **borrow fee/rate is not present anywhere** —
   `Shortable` is a yes/no flag, not a cost. Borrow-rate still needs a
   broker/borrow-desk source.
5. **§8 Tier-1 "cash runway" — partially served.** `Cash/sh` exists in
   the Screener export; runway (cash ÷ burn rate) still requires a
   burn-rate figure Finviz doesn't provide (EDGAR/FMP territory, both
   already named in §7 for exactly this).

No other direct contradictions found. The Calendar near-term-window
finding (§1/§3) isn't a contradiction of §8's "catalyst calendar"
wording — it's consistent with a forward-looking calendar concept — but
it does rule out using that specific endpoint for anything requiring
historical catalyst-date lookups, which the requirements doc doesn't
explicitly ask for but which the backtesting pillar might assume without
this memo.

---

## Appendix — raw probe log

Full request/response log (91 requests across two probe runs, tokens
scrubbed) preserved at the session scratchpad; not committed to the
repo (working artifact, not a versioned deliverable). Re-running the
probe script against this memo's claims is straightforward if Phase B
raises a specific new hypothesis to test — ask, and it's a ~2-minute
follow-up given the reusable `FinvizApiClient` token-resolution path
already in place.
