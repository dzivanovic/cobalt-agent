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
