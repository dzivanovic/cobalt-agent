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
<!-- cobalt:section seat-usage:2026-09-16 -->
### 2026-09-16

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-16 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
|---|---|---:|---:|---:|---:|---:|
| `claude-opus-5` | claude · write seat — L29 floor for vault/DB/migration paths | 142,156,462 | 2,212,083 | 781,338 | $112.74 | +$3.13 |
| `claude-sonnet-5` | claude · mechanical, non-write only — L29 ceiling for this tier | 162,081,582 | 1,146,790 | 410,067 | $41.11 | $0.00 |
| `grok-4.6-build` | grok · build + research seat | 643,456 | 0 | 19,266 | $0.23 | $0.00 |
| `mainframe` | qwen · local lane (L23) — delegated mundane work, token conservation | 0 | 0 | 827 | $0.00 [^free] | $0.00 |
| `gpt-6-astra` | codex · reviewer seat — read-only role (L33) | 3,721,728 | 0 | 18,227 | **unpriced** | — |

**Day total (API-equivalent):** ≥ $154.08 · **313,840,275** tokens across 5 model(s), seats: claude, codex, grok, qwen
**Fresh input tokens:** 648,449 — not a column above because it is a rounding error beside cache reads, but it is priced into the dollar figures.

> **UNPRICED MODELS: `gpt-6-astra`.** These were used today and the pinned tool's offline pricing table has no rate for them, so their cost is missing rather than zero, and the day total above is a FLOOR. Fix by bumping the pin in `configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by letting the job reach the network.

[^free]: `mainframe` — the local Qwen3.8-27B MLX server on this Mac (L23's local lane). Its cost is electricity and the Mac Studio, not API spend — $0 here is the true number, not a missing one, so it never raises the hourly unpriced warning.

_Generated 2026-09-16 21:00 EDT by `seatusage.report` · ccusage 20.0.20 (MIT, pinned) · offline pricing, no network at run time._
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
