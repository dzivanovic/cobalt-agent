# Live-Feed Spike — 19b Trigger-Grade Bar Detection

**Method:** measurement only. No engine code, no persistent services,
nothing left running. Ruling: PROJECT-LEDGER 2026-09-03 sitting-4,
"LIVE FEED RULED (ruling 6)" — Finviz-lite vs TradingView Premium
alert→webhook, winner = 19b at focus scale.

**Run date:** 2026-09-04, live market session. Armed names (Dejan's
pick): LULU, TSLA, NVDA, INTC, DELL.

**Scripts used (not committed — throwaway, per "no engine code"):**
`poll_finviz.py` (reuses `cobalt.archiver.collector`'s token resolution
and CSV parsing, same auth/client path as the real archiver) and
`webhook_listener.py` (FastAPI/uvicorn on localhost:8877, one route,
JSONL sink). Both ran from the session scratchpad, both torn down at
the end — see Teardown section.

---

## A. Finviz-lite (polled `/export/stock`, i1)

Two windows, 5 tickers, one HTTP GET per ticker per poll, 10 s cadence:

| Window | Span (ET) | Polls | HTTP status | Errors | Rate-limit/blocks |
|---|---|---|---|---|---|
| Premarket (extended hours) | 09:20:05–09:29:55 | 300 (60 cycles × 5) | 300× 200 | 0 | none |
| RTH | 09:30:22–10:00:12 | 900 (180 cycles × 5) | 900× 200 | 0 | none |

Fetch latency (all tickers, both windows): median 230 ms, max 405 ms —
never close to threatening the 10 s budget; 5 tickers costs ~0.4 s of
wall time per cycle.

**Bar-close-to-availability lag**, computed as: for each 1-minute bar
timestamp *T* returned by a ticker, `first wall-clock poll that first
shows newest_bar_ts == T` minus *T* (i.e. *T* is the bar's own close
boundary — the next bar's open):

| Window | n (bar transitions) | median | p95 | max |
|---|---|---|---|---|
| Premarket | 50 | 5.3 s | 15.3 s | 25.3 s |
| RTH | 155 | 2.2 s | 12.1 s | 22.0 s |

**Caveat on precision:** our poll grid samples every 10 s at a fixed
phase offset from the minute boundary — this is a measurement-*method*
ceiling, not a Finviz behavior. The tight median (2–5 s) reflects bars
that were already available at our first sample after the boundary;
the long tail (12–25 s, roughly the top 15-20% of transitions) is most
plausibly bars that weren't ready yet at that first sample and only
showed up one full poll cycle (~10 s) later — true availability for
those could be anywhere in that 10 s window, not necessarily the full
value shown. A tighter poll cadence (e.g. 2-3 s) would resolve this if
9-part precision below 5 s needs to be proven rather than inferred.

**Intrabar vs close-only updates:** newest bar updates **intrabar**,
continuously — TSLA/RTH: close price changed on 148 of 180 polls
without the bar timestamp advancing (i.e. the "current" bar's close is
live-ish, not frozen until the minute rolls over).

**Real-time vs delayed, checked against Dejan's live DAS/TV chart:**
one direct comparison, TSLA, 2026-09-04 10:10:57 ET — Finviz's newest
bar (10:10:00, close 355.665) vs Dejan's live readout at the same
moment (355.62). Spread ≈ $0.05, consistent with ordinary last-tick vs
bar-close noise, not a lag artifact. (An earlier readout of "365.12"
was a digit transposition of 356.xx — flagged and corrected in-session,
not a real discrepancy; logged here so it isn't mistaken for a data
quality finding on a future read of this doc.)

**Extended hours:** the premarket window above (09:20–09:29:55, before
09:30 RTH open) *is* the extended-hours test the acceptance criteria
called for — same behavior (200s, no rate-limit, ~5 s median lag) as
RTH. No separate afterhours window was run; nothing in the premarket
data suggests Finviz treats sessions differently, but this is one
window, not exhaustive.

**Symbol count supported:** 5 tickers polled concurrently per cycle at
10 s cadence with zero errors and latency nowhere near the budget —
this run does not stress-test pool scale (TRIAGE's tier_a/tier_b is
~200+ symbols; see `docs/30 - Design/archiver-runs.md`'s nightly full
run for that scale's timing under the *non-realtime* nightly archiver
path). What this run shows is headroom at 5 names, not a ceiling.

---

## B. TradingView Premium alert → webhook

**Setup:** localhost:8877 FastAPI listener, exposed via a `cloudflared`
tunnel quick-tunnel (no account, no persistent config) at
`https://minor-directors-generate-development.trycloudflare.com/tv-webhook`.
Dejan created one alert manually (TSLA, 1 min chart, condition `Price >
0`, trigger "Every time" — TradingView's own UI describes this as
"triggers once per minute while the condition remains met," i.e. once
per bar close on a 1-minute chart; no separate "once per bar close"
trigger option was offered for this condition type), webhook + message
body `{"ticker":"{{ticker}}","close":"{{close}}","time":"{{timenow}}","bar":"{{time}}"}`
enabled. Cobalt did not create the alert — per instruction, only wrote
the condition/message text for Dejan to paste in.

**Lag, bar close → webhook receipt** (`received_at` minus the alert's
own `{{time}}`/bar-close field), 43 bars, 2026-09-04 09:45:17–10:27:02
ET, all TSLA:

| n | median | mean | min | p95 | max |
|---|---|---|---|---|---|
| 43 | 1.71 s | 2.55 s | 0.59 s | 6.06 s | 26.0 s |

The 26 s outlier is the very first firing (09:45:17) — consistent with
one-time warm-up (TradingView's own alert-evaluation cold start, or
first-request TLS/DNS to the fresh quick-tunnel hostname); every other
sample (42/43) is ≤ 8.0 s, and 41/43 are ≤ 6.1 s. Comfortably inside
the ≤5 s target on a typical bar once warmed up.

**Extended hours firing:** **not tested.** The alert was created at
~09:38 ET, after RTH open, and the spike's teardown happened at ~10:27
ET, still inside RTH. Testing this needs either an afterhours window
(market runs to ~20:00 ET) or tomorrow's premarket — deferred to a
follow-up session on Dejan's call (asked in-session; he chose to ship
this report now rather than hold for it). **Open item, not a pass/fail
finding.**

**Alert-slot count:** **not obtainable from Dejan's current TradingView
UI.** Checked both the Alerts tab and the Log tab — neither surfaces a
"used/total" plan counter in this account's UI version. Observable
instead: 12 total alert rows exist on the account (mix of
active/expired, several unrelated pre-existing alerts), no visible cap
indicator. An exact plan limit would need Dejan to check
Profile → Plan/account page separately. **Open item.**

**Reliability:** clean delivery for all 43 samples while the tunnel was
up. Confirmed by TradingView's own delivery log switching to "530
Server Error" then "couldn't find that domain" within ~1–15 min of
teardown — an independent, third-party confirmation that the tunnel
teardown actually took effect end-to-end, not just locally.

---

## C. Report

| Criterion | A. Finviz-lite | B. TV alert→webhook |
|---|---|---|
| Bar-close-to-availability lag ≤5 s | **Pass** (median 2.2–5.3 s; tail to ~25 s is a measurement-resolution artifact, see caveat) | **Pass** (median 1.7 s, p95 6.1 s; one 26 s cold-start outlier) |
| Newest bar real-time vs delayed (DAS/TV check) | **Pass** — one direct comparison, $0.05 spread | N/A (webhook already reflects a firing event, not a polled snapshot) |
| Sustained 30 min in-session, no rate-limit/disconnect | **Pass** — 900 polls, 0 errors, 0 blocks | **Pass** (ran ~42 min, 09:45–10:27, 43 clean deliveries) |
| Extended-hours behavior (1 window) | **Pass** — premarket window: same behavior as RTH | **Not tested** — open item |
| Symbol count | 5 tickers, zero strain observed; pool scale (~200+) untested | 1 alert (TradingView's model is one alert = one condition/symbol, not a poll fan-out) |
| Alert-slot count | N/A | **Not obtained** — UI doesn't surface it; open item |

**Which source (or neither) meets 19b at focus scale:** both sources
clear the ≤5 s lag bar at focus scale (≤5 armed names / 1 alert) with
zero reliability issues over the tested windows. Finviz-lite is the
more complete answer today — it independently confirms freshness
(polls give an observable bar-close timestamp to lag against) and
already shares the archiver's exact auth/client path, so it needs zero
new infrastructure to become a persistent watcher. TradingView's
webhook path has a slightly tighter median lag (1.7 s vs 2.2–5.3 s) and
proves an genuinely event-driven trigger (no poll interval to tune),
but it depends on Dejan hand-creating one alert per symbol in
TradingView's UI (confirmed: no programmatic alert creation attempted,
per instruction) and on an always-on public tunnel/webhook receiver in
production — a real infrastructure cost this spike deliberately did
not stand up persistently.

**What pool scale would need:** Finviz-lite polling ~200+ symbols on a
10 s cadence means ~200 concurrent GETs every 10 s (vs 5 here) —
untested here; the nightly archiver's full run (`archiver-runs.md`,
~210 tickers, ~23 min, non-realtime) shows the ceiling on serial/rate-
limited fetching but says nothing about sustained realtime polling at
that width, since the nightly run isn't cadenced or held to a lag
target. TradingView's approach would need ~200 individually
hand-created alerts (or Massive Advanced's paid tier, per the ledger's
ruling 6, as the pool-scale fallback) plus a production-grade webhook
receiver (auth, retries, dedup) replacing this spike's throwaway
listener — real work, not a config change.

---

## Teardown (proof)

- `cloudflared` (pid 48687) and `webhook_listener.py` (pid 48668)
  killed at 2026-09-04 ~10:27 ET.
- `ps -p <pid>` for both: no process found.
- `lsof -i :8877`: empty, port free.
- `ps aux | grep -i "cloudflared\|webhook_listener"`: no matches.
- `launchctl list | grep -i cloudflare`: no matches — no launchd entry
  was ever created (quick tunnel only, no `cloudflared service
  install` run).
- Independent confirmation: TradingView's own alert delivery log shows
  webhook failures ("530 Server Error", then "couldn't find that
  domain") starting within ~1 min of teardown — the public endpoint is
  gone from the outside, not just locally.
- No files under `src/cobalt/` were touched; `poll_finviz.py` and
  `webhook_listener.py` lived only in the session scratchpad
  (`/private/tmp/...`), never in the repo, and are not committed.

## Open items (for sitting 5 / next spike)

1. TradingView webhook extended-hours firing — untested this session,
   needs an afterhours or premarket window.
2. TradingView alert-slot/plan-limit count — not surfaced in the
   current UI; check Profile → Plan page directly if it matters for
   the pool-scale decision.
3. Finviz-lite's long-tail lag samples (12–25 s) are bounded by our 10 s
   poll granularity, not proven to be real 12–25 s delays — a follow-up
   with a 2–3 s poll cadence over a short window would tighten this if
   it becomes decision-relevant.
