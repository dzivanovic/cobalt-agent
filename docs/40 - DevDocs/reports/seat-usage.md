# Seat usage — daily

What the agent seats cost, per model, per day. Written hourly inside
`seat_usage.window` by `com.cobalt.seat-usage`; the tables are generated
and are rewritten in place every run.

**The two cells under each date are yours.** `weekly_pct_open:` and
`weekly_pct_close:` are the weekly-allowance percentages the harnesses show
you at the start and the end of the day — the one number in this file
that no tool on this machine can read. They sit OUTSIDE the generated
unit, they are seeded blank once, and nothing here ever writes them
again once they have a value (L28 clause 2a).

**"API-equivalent $" is not a bill.** The seats run on consumer plans
(L29); this column is what the same tokens would have cost at published
API rates, which is the only comparable number available. Read it as a
size, not as an amount owed.

Newest day first.

<!-- cobalt:days -->
<!-- cobalt:section seat-usage:2026-10-03 -->
### 2026-10-03

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-10-03 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `gpt-5.6-sol` | codex · — | 4,399,872 | 0 | 26,395 | $4.19 | $0.00 |
| `grok-4.7-build` | grok · — | 6,376,448 | 0 | 349,031 | $2.61 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 865 | $0.00 [^free] | $0.00 |
| `claude-opus-5-5` | claude · — | 831,688,138 | 11,742,376 | 3,459,198 | **unpriced** | — |
| `claude-sonnet-5-5` | claude · — | 3,831,455 | 346,962 | 64,410 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 51,809,833 | 1,643,157 | 142,317 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 77,568 | 0 | 385 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $6.80 · **917,510,831** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 1,552,421 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-10-03 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20261003 --until 20261003 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-10-03 -->
<!-- /cobalt:section seat-usage:2026-10-03 -->
<!-- cobalt:section seat-usage:2026-10-02 -->
### 2026-10-02

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-10-02 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `grok-4.7-build` | grok · — | 2,670,592 | 0 | 117,130 | $0.90 | $0.00 |
| `claude-opus-5-5` | claude · — | 601,988,275 | 8,520,680 | 2,471,947 | **unpriced** | — |
| `claude-sonnet-5-5` | claude · — | 23,982,085 | 885,133 | 180,883 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 49,039,573 | 2,343,788 | 368,944 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $0.90 · **692,879,449** tokens across 4 model(s), seats: claude, grok
**Fresh input tokens:** 310,419 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

_Generated 2026-10-02 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20261002 --until 20261002 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-10-02 -->
<!-- /cobalt:section seat-usage:2026-10-02 -->
<!-- cobalt:section seat-usage:2026-10-01 -->
### 2026-10-01

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-10-01 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `grok-4.7-build` | grok · — | 4,640,640 | 0 | 230,913 | $1.81 | +$1.17 |
| `claude-opus-5-5` | claude · — | 453,873,689 | 4,973,434 | 1,348,835 | **unpriced** | — |
| `claude-sonnet-5-5` | claude · — | 78,250,308 | 1,371,483 | 221,123 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $1.81 · **545,724,843** tokens across 3 model(s), seats: claude, grok
**Fresh input tokens:** 814,418 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-opus-5-5`, `claude-sonnet-5-5`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

_Generated 2026-10-01 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20261001 --until 20261001 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-10-01 -->
<!-- /cobalt:section seat-usage:2026-10-01 -->
<!-- cobalt:section seat-usage:2026-09-30 -->
### 2026-09-30

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-30 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `grok-4.7-build` | grok · — | 14,852,224 | 0 | 365,948 | $4.06 | +$1.53 |
| `gpt-5.6-sol` | codex · — | 44,544 | 0 | 522 | $0.09 | $0.00 |
| `claude-opus-5-5` | claude · — | 495,939,951 | 9,240,058 | 2,709,333 | **unpriced** | — |
| `claude-sonnet-5-5` | claude · — | 309,916,595 | 3,156,411 | 1,077,017 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 9,678,795 | 268,139 | 26,803 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $4.14 · **848,390,159** tokens across 5 model(s), seats: claude, codex, grok
**Fresh input tokens:** 1,113,819 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

_Generated 2026-09-30 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260930 --until 20260930 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-30 -->
<!-- /cobalt:section seat-usage:2026-09-30 -->
<!-- cobalt:section seat-usage:2026-09-29 -->
### 2026-09-29

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-29 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `grok-4.7-build` | grok · — | 29,904,000 | 0 | 557,148 | $7.88 | $0.00 |
| `gpt-5.6-sol` | codex · — | 4,723,712 | 0 | 17,813 | $4.66 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 611 | $0.00 [^free] | $0.00 |
| `claude-opus-5-5` | claude · — | 913,676,119 | 10,462,944 | 2,659,943 | **unpriced** | — |
| `claude-sonnet-5-5` | claude · — | 215,829,122 | 6,021,710 | 2,271,159 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 223,201,430 | 2,759,077 | 933,911 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 10,180,864 | 0 | 17,517 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $12.54 · **1,426,405,332** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 3,188,252 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-29 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260929 --until 20260929 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-29 -->
<!-- /cobalt:section seat-usage:2026-09-29 -->
<!-- cobalt:section seat-usage:2026-09-28 -->
### 2026-09-28

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-28 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 234,687,327 | 4,946,745 | 2,144,141 | $86.93 | $0.00 |
| `grok-4.7-build` | grok · — | 39,218,304 | 0 | 830,906 | $11.29 | +$1.13 |
| `gpt-5.6-sol` | codex · — | 8,686,080 | 0 | 51,298 | $8.90 | +$4.69 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 20,543 | $0.00 [^free] | $0.00 |
| `claude-opus-5-5` | claude · — | 1,136,947,818 | 12,382,050 | 3,776,312 | **unpriced** | — |
| `claude-sonnet-5-5` | claude · — | 105,314,250 | 3,183,753 | 1,037,087 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 15,648,896 | 0 | 47,045 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $107.11 · **1,573,842,841** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 4,920,286 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-opus-5-5`, `claude-sonnet-5-5`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-28 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260928 --until 20260928 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-28 -->
<!-- /cobalt:section seat-usage:2026-09-28 -->
<!-- cobalt:section seat-usage:2026-09-27 -->
### 2026-09-27

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-27 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 129,366,723 | 2,529,247 | 890,074 | $44.69 | +$15.63 |
| `gpt-5.6-sol` | codex · — | 2,214,784 | 0 | 26,135 | $3.26 | $0.00 |
| `grok-4.7-build` | grok · — | 1,779,328 | 0 | 150,625 | $0.98 | $0.00 |
| `claude-opus-5-5` | claude · — | 98,463,847 | 2,565,889 | 661,787 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 106,459,985 | 1,917,609 | 442,466 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 1,927,808 | 0 | 6,873 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $48.93 · **350,388,091** tokens across 6 model(s), seats: claude, codex, grok
**Fresh input tokens:** 984,911 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

_Generated 2026-09-27 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260927 --until 20260927 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-27 -->
<!-- /cobalt:section seat-usage:2026-09-27 -->
<!-- cobalt:section seat-usage:2026-09-26 -->
### 2026-09-26

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-26 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| _no seat activity recorded_ | — | 0 | 0 | 0 | $0.00 | — |

**Day total (API-equivalent):** $0.00 · **0** tokens across 0 model(s)
**Fresh input tokens:** 0 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

_Generated 2026-09-26 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260926 --until 20260926 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-26 -->
<!-- /cobalt:section seat-usage:2026-09-26 -->
<!-- cobalt:section seat-usage:2026-09-25 -->
### 2026-09-25

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-25 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 408,710,670 | 7,876,508 | 3,307,553 | $146.33 | $0.00 |
| `grok-4.7-build` | grok · — | 12,694,656 | 0 | 752,049 | $7.55 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 807 | $0.00 [^free] | $0.00 |
| `claude-opus-5-5` | claude · — | 522,899,371 | 10,510,287 | 3,014,364 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 249,267,405 | 4,277,254 | 1,126,068 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $153.88 · **1,229,471,712** tokens across 5 model(s), seats: claude, grok, qwen
**Fresh input tokens:** 5,034,720 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-25 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260925 --until 20260925 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-25 -->
<!-- /cobalt:section seat-usage:2026-09-25 -->
<!-- cobalt:section seat-usage:2026-09-24 -->
### 2026-09-24

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-24 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 454,450,921 | 8,331,129 | 3,086,840 | $154.40 | +$14.27 |
| `grok-4.7-build` | grok · — | 16,200,960 | 0 | 921,759 | $8.35 | +$0.25 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 562 | $0.00 [^free] | $0.00 |
| `claude-opus-5-5` | claude · — | 1,652,417,075 | 13,076,063 | 3,735,092 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 235,059,101 | 4,359,826 | 996,163 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $162.76 · **2,397,783,728** tokens across 5 model(s), seats: claude, grok, qwen
**Fresh input tokens:** 5,148,237 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-24 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260924 --until 20260924 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-24 -->
<!-- /cobalt:section seat-usage:2026-09-24 -->
<!-- cobalt:section seat-usage:2026-09-23 -->
### 2026-09-23

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-23 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 583,609,075 | 10,289,190 | 3,388,656 | $191.76 | +$1.50 |
| `grok-4.7-build` | grok · — | 13,625,984 | 0 | 898,970 | $7.89 | $0.00 |
| `gpt-5.6-sol` | codex · — | 46,848 | 0 | 533 | $0.13 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 2,963 | $0.00 [^free] | $0.00 |
| `claude-opus-5-5` | claude · — | 1,045,660,376 | 15,920,411 | 4,662,431 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 2,586,934 | 185,089 | 28,048 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 12,160 | 0 | 5 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $199.78 · **1,685,665,753** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 4,748,080 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-23 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260923 --until 20260923 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-23 -->
<!-- /cobalt:section seat-usage:2026-09-23 -->
<!-- cobalt:section seat-usage:2026-09-22 -->
### 2026-09-22

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-22 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 275,207,885 | 5,189,863 | 1,272,075 | $221.31 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 626,279,984 | 7,637,411 | 3,064,793 | $186.18 | +$10.19 |
| `grok-4.7-build` | grok · — | 11,988,864 | 0 | 878,820 | $7.49 | +$0.88 |
| `gpt-5.6-sol` | codex · — | 1,899,648 | 0 | 26,054 | $2.84 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 844 | $0.00 [^free] | $0.00 |
| `claude-opus-5-5` | claude · — | 531,859,206 | 7,702,049 | 2,295,327 | **unpriced** | — |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 188,939,638 | 3,762,832 | 1,053,653 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $417.83 · **1,674,881,393** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 5,822,447 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `claude-opus-5-5`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-22 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260922 --until 20260922 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-22 -->
<!-- /cobalt:section seat-usage:2026-09-22 -->
<!-- cobalt:section seat-usage:2026-09-21 -->
### 2026-09-21

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-21 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 467,136,646 | 8,808,535 | 2,543,464 | $385.26 | +$14.65 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 352,128,837 | 8,044,886 | 3,012,857 | $132.74 | $0.00 |
| `gpt-5.6-sol` | codex · — | 3,381,760 | 0 | 27,434 | $3.91 | $0.00 |
| `grok-4.7-build` | grok · — | 3,076,480 | 0 | 193,388 | $3.42 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 6,827,264 | 0 | 253,439 | $2.70 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 758 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 490,350,964 | 4,648,322 | 1,285,140 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 9,427,072 | 0 | 35,899 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $528.04 · **1,365,149,444** tokens across 8 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 3,966,299 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-21 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260921 --until 20260921 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-21 -->
<!-- /cobalt:section seat-usage:2026-09-21 -->
<!-- cobalt:section seat-usage:2026-09-20 -->
### 2026-09-20

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-20 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 582,606,181 | 7,261,200 | 1,814,932 | $409.31 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 128,800,577 | 3,999,865 | 1,685,550 | $57.31 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 5,051,264 | 0 | 203,650 | $2.24 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 684 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 177,309,378 | 2,087,837 | 619,366 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 8,004,992 | 0 | 38,445 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $468.87 · **921,413,668** tokens across 6 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 1,929,747 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-20 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260920 --until 20260920 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-20 -->
<!-- /cobalt:section seat-usage:2026-09-20 -->
<!-- cobalt:section seat-usage:2026-09-19 -->
### 2026-09-19

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-19 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 895,085,406 | 7,943,438 | 2,283,369 | $580.87 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 367,501,697 | 11,168,926 | 3,524,215 | $147.64 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 9,744,512 | 0 | 992,881 | $6.37 | $0.00 |
| `claude-haiku-4-5-20251001` | claude · — | 62,123 | 55,061 | 435 | $0.12 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 1,067 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 258,280,706 | 1,930,775 | 739,436 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 7,883,776 | 0 | 55,645 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $735.00 · **1,572,486,916** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 5,233,448 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-19 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260919 --until 20260919 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-19 -->
<!-- /cobalt:section seat-usage:2026-09-19 -->
<!-- cobalt:section seat-usage:2026-09-18 -->
### 2026-09-18

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-18 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 297,364,780 | 4,144,733 | 1,054,477 | $216.51 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 72,227,860 | 1,751,466 | 522,881 | $26.68 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 3,199,616 | 0 | 128,908 | $1.27 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 845 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 194,032,103 | 1,784,196 | 415,197 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $244.46 · **577,461,840** tokens across 5 model(s), seats: claude, grok, qwen
**Fresh input tokens:** 834,778 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-18 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260918 --until 20260918 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-18 -->
<!-- /cobalt:section seat-usage:2026-09-18 -->
<!-- cobalt:section seat-usage:2026-09-17 -->
### 2026-09-17

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-17 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 100,512,188 | 2,174,827 | 590,066 | $86.49 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 88,483,267 | 636,493 | 213,738 | $22.38 | $0.00 |
| `claude-haiku-4-5-20251001` | claude · — | 315,637 | 58,934 | 3,602 | $0.17 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 27,904 | 0 | 331 | $0.03 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 786 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 92,615,357 | 1,517,548 | 296,992 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $109.07 · **287,642,329** tokens across 6 model(s), seats: claude, grok, qwen
**Fresh input tokens:** 194,659 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-17 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260917 --until 20260917 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-17 -->
<!-- /cobalt:section seat-usage:2026-09-17 -->
<!-- cobalt:section seat-usage:2026-09-16 -->
### 2026-09-16

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-16 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 144,622,561 | 2,286,982 | 797,750 | $115.13 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 206,521,598 | 1,716,295 | 469,131 | $52.86 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 643,456 | 0 | 19,266 | $0.23 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 827 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 10,122,805 | 188,425 | 57,080 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 3,721,728 | 0 | 18,227 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $168.23 · **371,836,106** tokens across 6 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 649,975 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-16 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260916 --until 20260916 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-16 -->
<!-- /cobalt:section seat-usage:2026-09-16 -->
<!-- cobalt:section seat-usage:2026-09-15 -->
### 2026-09-15

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-15 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 97,658,709 | 1,779,902 | 418,135 | $30.84 | $0.00 |
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 23,729,872 | 1,091,151 | 305,416 | $29.54 | $0.00 |
| `gpt-5.6-sol` | codex · — | 14,283,776 | 0 | 62,013 | $10.19 | $0.00 |
| `claude-haiku-4-5-20251001` | claude · — | 84,396 | 22,159 | 431 | $0.05 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 29,568 | 0 | 1,018 | $0.04 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 7,308 | $0.00 [^free] | $0.00 |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 5,259,008 | 0 | 24,393 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $70.66 · **145,893,987** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 1,136,732 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-15 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260915 --until 20260915 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-15 -->
<!-- /cobalt:section seat-usage:2026-09-15 -->
<!-- cobalt:section seat-usage:2026-09-14 -->
### 2026-09-14

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-14 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 91,942,353 | 1,356,515 | 442,624 | $28.01 | +$0.98 |
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 12,373,680 | 545,215 | 176,951 | $16.08 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 4,151,040 | 0 | 188,770 | $1.79 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 18,683 | $0.00 [^free] | $0.00 |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 2,956,288 | 0 | 43,386 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $45.88 · **116,494,266** tokens across 5 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 2,298,761 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-14 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260914 --until 20260914 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-14 -->
<!-- /cobalt:section seat-usage:2026-09-14 -->
<!-- cobalt:section seat-usage:2026-09-13 -->
### 2026-09-13

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-13 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 103,141,415 | 1,472,695 | 533,376 | $31.73 | +$0.18 |
| `gpt-5.6-sol` | codex · — | 4,120,448 | 0 | 25,398 | $3.62 | $0.00 |
| `claude-haiku-4-5-20251001` | claude · — | 213,198 | 85,063 | 8,916 | $0.24 | $0.00 |
| `gpt-5.6-terra` | codex · — | 11,008 | 0 | 36 | $0.01 | — |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 6,935 | $0.00 [^free] | $0.00 |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 5,685,120 | 0 | 44,992 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $35.60 · **116,129,721** tokens across 6 model(s), seats: claude, codex, qwen
**Fresh input tokens:** 781,121 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-13 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260913 --until 20260913 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-13 -->
<!-- /cobalt:section seat-usage:2026-09-13 -->
<!-- cobalt:section seat-usage:2026-09-12 -->
### 2026-09-12

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-12 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 60,591,526 | 671,469 | 258,220 | $17.39 | $0.00 |
| `gpt-5.6-sol` | codex · — | 12,907,008 | 0 | 80,356 | $11.13 | $0.00 |
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 1,660,503 | 66,054 | 17,780 | $1.94 | $0.00 |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 1,483,008 | 0 | 24,922 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $30.46 · **78,395,464** tokens across 4 model(s), seats: claude, codex
**Fresh input tokens:** 634,618 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

_Generated 2026-09-12 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260912 --until 20260912 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-12 -->
<!-- /cobalt:section seat-usage:2026-09-12 -->
<!-- cobalt:section seat-usage:2026-09-11 -->
### 2026-09-11

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-11 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 3,500,248 | 118,494 | 19,332 | $1.37 | $0.00 |
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 30,516 | 17,398 | 16 | $0.19 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 56,168 | $0.00 [^free] | $0.00 |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 296,448 | 0 | 2,496 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $1.56 · **5,849,217** tokens across 4 model(s), seats: claude, codex, qwen
**Fresh input tokens:** 1,808,101 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-11 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260911 --until 20260911 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-11 -->
<!-- /cobalt:section seat-usage:2026-09-11 -->
<!-- cobalt:section seat-usage:2026-09-10 -->
### 2026-09-10

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-10 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `gpt-5.6-sol` | codex · — | 45,127,168 | 0 | 282,321 | $37.10 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 89,344,917 | 1,064,764 | 331,304 | $25.44 | $0.00 |
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 16,049,684 | 750,953 | 324,708 | $23.66 | $0.00 |
| `gpt-5.6-terra` | codex · — | 994,816 | 0 | 15,569 | $0.74 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 287,232 | 0 | 4,626 | $0.10 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 29 | $0.00 [^free] | $0.00 |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 1,584,000 | 0 | 17,243 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $87.04 · **158,091,916** tokens across 7 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 1,912,582 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-10 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260910 --until 20260910 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-10 -->
<!-- /cobalt:section seat-usage:2026-09-10 -->
<!-- cobalt:section seat-usage:2026-09-09 -->
### 2026-09-09

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-09 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 94,401,908 | 991,048 | 229,827 | $59.15 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 27,648 | 0 | 2,373 | $0.03 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 6,302 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 52,477,269 | 1,547,755 | 255,056 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 27,392 | 0 | 322 | **unpriced** | — |
| `cobalt-test-q8-sw` | qwen · — | 0 | 0 | 690 | **unpriced** | — |
| `cobalt-test-q4-orig` | qwen · — | 0 | 0 | 3,268 | **unpriced** | — |
| `cobalt-test-q4-sw` | qwen · — | 0 | 0 | 719 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $59.17 · **151,737,016** tokens across 8 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 1,765,439 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `cobalt-test-q4-orig`, `cobalt-test-q4-sw`, `cobalt-test-q8-sw`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-09 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260909 --until 20260909 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-09 -->
<!-- /cobalt:section seat-usage:2026-09-09 -->
<!-- cobalt:section seat-usage:2026-09-08 -->
### 2026-09-08

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-08 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 247,387,943 | 2,182,935 | 576,265 | $153.65 | $0.00 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 31,987,063 | 247,202 | 116,249 | $8.55 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 182,656 | 0 | 1,116 | $0.03 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 129 | $0.00 [^free] | $0.00 |
| `claude-fable-5-1` | claude · planning + architect seat — L29 above the floor, at Dejan's call | 17,237,638 | 354,319 | 118,151 | **unpriced** | — |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 11,904 | 0 | 82 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $162.23 · **300,510,518** tokens across 6 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 106,866 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `claude-fable-5-1`, `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-08 23:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
_Command: `/Users/cobalt/.npm-global/bin/ccusage daily --json --breakdown --since 20260908 --until 20260908 --by-agent --offline`_
<!-- /cobalt:unit seat-usage:2026-09-08 -->
<!-- /cobalt:section seat-usage:2026-09-08 -->
