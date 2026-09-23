# ASET attest forensics — 09-22 first-trade refusal + second-computer "asks again" (2026-09-23)

## §0

`logs/aset.err` has **zero** lines for 09-22 before 09:35:08 ET, and **zero** occurrences ever (whole file, Aug 31–09-23) of `SheetMismatch`/`REFUSED`/`CONFLICT`/`DAY MODE UNRESOLVED` text tied to day-mode. His first-trade refusal left no server-log trace — not because it didn't happen, but because most refusal branches in `src/cobalt/aset/web.py` don't log at all (only one does, and it never fired that morning). The 09-22 production `attested_at` (13:35:52 UTC = 09:35:52 ET) is **28s after** the first SOFI card (09:35:24 ET) it supposedly gated, proving an earlier, untraceable attest already existed and was silently overwritten. `GET /` carries no `Cache-Control` header anywhere in `web.py`, so a second device can legally render a stale, pre-attest snapshot with no server round-trip at all — the leading code-grounded explanation for "asks again." Cause: **BUG** (small, logging + cache-header + no-history gaps) · fix size: **small**.

## Timeline, 09-22 04:00–09:40 ET (from `logs/aset.err` line numbers, file times as printed)

| Time (ET, from log) | Line | Event |
|---|---|---|
| — | — | **No `logs/aset.err` line exists for 09-22 before 09:35:08.** Process PID `23048` had been running continuously since before 09-21 11:45 (no restart logged overnight — confirmed: no `Started server process` line between the 09-21 11:45 radar error and the first 09-22 line). |
| 09:35:08.123–.160 | 4978–4986 | First 09-22 activity: config load, vault unlock, finviz token resolve — the machinery a `/size` (card) request triggers, not an `/attest`. No day-mode/attest log line accompanies it. |
| 09:35:23.604–.605 | 4987–4990 | Second vault/finviz unlock cycle (same pattern, ~15s later). |
| 09:35:24.697 | 4991 | `cobalt.aset.daily_note:_write_unit:189` — card `card-20260922T093524` (SOFI LONG C, `sheet_mode: half`) written. This card only writes if `assert_sheet_matches` already passed, i.e. `day_modes.attested_sheet` for 09-22 was already `half.htk` **before** this line. |
| 09:35:52 (13:35:52 UTC) | *(production row, desk-read, not in this log)* | `day_modes.attested_at` for 09-22 = `half.htk` — the **only** attest timestamp the row can hold (upsert overwrites in place). 28s after the card above. |
| through 10:38 | 5339–5362 | Further 09-22 card/fill writes proceed normally (`card-20260922T103642`, `fill-20260922T103642`) — no further refusals logged. |

No `logs/aset.err` line names his first refusal, an account-mode error, a note conflict, or a note-write failure anywhere in the 04:00–09:40 window (or anywhere else on 09-22).

## (1) Exact refusal text / path for the first 09-22 card, and when

**Cannot be produced from any log.** Grepped the full `logs/aset.err` (Aug 31–09-23, both `SheetMismatch`, `No hotkey file attested`, `sheet FULL loaded`, `is not enabled on the`, `aset.card REFUSED`, and bare `REFUSED`/`CONFLICT`): every pattern returns zero hits tied to day-mode, in this file's entire history, not just 09-22.

Code review of `src/cobalt/aset/web.py` explains why:
- The **only** day-mode refusal branch that logs anything is `/size`'s `except SheetMismatch as e:` → `logger.error("aset.card REFUSED (F6 match check): {}", e)` (web.py:987–988). This never fired on 09-22 (or ever, in this log).
- Every other refusal branch that can stop a card or an attest is **silent** at the loguru level:
  - `/size`: `except (SizingError, ConfigError, DevEntryRefused, SessionBlocked) as e:` (web.py:990) and the bare `except Exception` (web.py:992) — no `logger.error` call, banner-only.
  - `/attest`: `except (SheetMismatch, ConfigError, SessionBlocked) as e:` (web.py:1170) and `except Exception` (web.py:1172) — no `logger.error` call at all, on any failure path.
- `logs/aset.log` (uvicorn access log) cannot fill the gap either: every `/attest` POST in its history — 27 of them, three client identities (`10.200.2.66`, `100.82.85.27`, `100.73.178.42`) — returns `200 OK`, **including failed attests**, since none of the `/attest` exception branches set a non-200 status code. A refused attest and a successful one are indistinguishable in the access log.

Best-supported inference (not proof, L70): his first refusal was almost certainly the `/size` route's `SheetMismatch` "no hotkey file attested for today" branch (match.py:99–107) — the ordinary, by-design state of a fresh trading day before his first attest — hit sometime before 09:35:08, in the unlogged window. Nothing in the evidence distinguishes that from a genuine bug in that same window; there is no log line either way.

## (2) Can the stored attestation be lost, overwritten, or read as absent between his first attest and his first card?

**Yes, by design, and it demonstrably happened once already that morning.**

- `DayModeStore.attest_sheet` (`src/cobalt/daymode/store.py:152–169`) upserts unconditionally: `attested_sheet = EXCLUDED.attested_sheet, attested_at = EXCLUDED.attested_at` — every call overwrites the prior value in place. There is **no history table**; the row can never show more than the single most recent attest. The 28-second gap between the first SOFI card (09:35:24, already sheet-matched) and the recorded `attested_at` (09:35:52) proves an earlier attest existed and was overwritten with no trace — the row alone can never answer "was it attested once or three times before the card."
- `_read_back_note_attestation` (web.py:466–491) runs on **every** `_daymode_state()` call, i.e. every page render, not just at attest time. If the daily note has a ticked `.htk` box that **disagrees** with the stored `attested_sheet`, `daymode_note.reconcile` (note.py:211–235) raises `NoteAttestationConflict`, and the banner becomes `⚠ DAY MODE UNRESOLVED — cards are refused until this is fixed` (web.py:561–563) — with the attest `<select>` form omitted entirely (it only renders in the non-error branch, web.py:606–618). This is a real, code-present way to lose the *appearance* of attestation across any device, but it never fired in this log's history (`daymode: note/selector attestation conflict` — zero hits) and the current 09-22 note (`half.htk` ticked, matching the DB) shows no unresolved conflict now.
- `_write_daymode_note` (web.py:535–556) is a "record stands even if this fails" design (per its own docstring) — a note-write failure after a successful attest is loud (`logger.error(... "daymode note write FAILED (attestation stands)")`, web.py:555) but never fired on 09-22 either.
- `trade_date`/ET boundary: `_today_et()` (web.py:445–446) is computed server-side from `session_clock().to_et(now_utc())` — not client/device time — so a device clock skew cannot shift which row is read.
- Deploy restart: ruled out — no `Started server process` line between the last 09-21 log entry and the first 09-22 one; the same PID (23048) served both days.
- `account_mode`: resolved entirely server-side per `trade_date` (`src/cobalt/aset/account_mode.py:23-40`, `day_modes.account_mode` then `trader_settings`), no device dependency.

## (3) Why does a second computer "ask again"?

The attested state is resolved **fully server-side** on every request — `DayModeStore.for_date` (store.py:55-61) queries by `trade_date` with no session/cookie/device key anywhere in the read path, and the `<select>` renders the currently-attested file as `selected` (web.py:606-609) from that same query. In principle a second device hitting the same `GET /` should show the current row immediately; no per-device cache, connection-pinning, or client-identity split was found in `db.py`, `store.py`, or `web.py`.

The gap: **`grep -n "Cache-Control" src/cobalt/aset/web.py` returns zero matches** — the day-mode banner page carries no `no-store`/`no-cache` directive anywhere. A browser is free to serve a previously-loaded copy of `/` (back/forward-cache or disk cache) without a network round-trip on the second device — which would show the pre-attest banner, with the attest form asking again, and would explain why nothing shows in `logs/aset.log`/`aset.err` for that "ask" (no request was made). This is the most defensible code-grounded explanation, but it is not proven to be what happened on 09-22 specifically — no log line records a `GET /` (the access log carries no timestamps, so a specific request on that morning cannot be isolated or ruled in/out).

The `NoteAttestationConflict` path in (2) is the other live candidate — device-independent (same for any computer, since it's evaluated server-side from the DB row + note file on every request) — but it also renders as an explicit "DAY MODE UNRESOLVED" error, not a bare re-ask, and never appears in the log.

## (4) Classification

**BUG — small, three independent gaps, none of them the trading-logic match check itself:**

1. Refusal logging is inconsistent: only `/size`'s `SheetMismatch` branch logs (web.py:987-988); `/size`'s `SizingError/ConfigError/DevEntryRefused/SessionBlocked`+generic (web.py:990,992) and **all** of `/attest`'s failure branches (web.py:1170,1172) are silent. Smallest fix: add a `logger.error(...)` call to each of those four `except` blocks, mirroring web.py:988's pattern — named file:lines above. (Not built, per instructions.)
2. `day_modes.attest_sheet` keeps no history (store.py:152-169) — every attest overwrites the last, so a repeated/second attest is structurally indistinguishable from a first one and can never be reconstructed after the fact.
3. `GET /` sets no `Cache-Control` header (web.py:852 route), leaving the attest banner eligible for stale client-side cache/bfcache reuse on a second device.

None of these is a defect in the F6 match-check logic itself (`assert_sheet_matches`, match.py:80-117, behaves as specified). The classification is BUG because the *evidence trail* around the refusal is missing by omission, not by any inherent unprovability — each gap above has a small, named fix.

## ESCALATE

None.

ASET ATTEST FORENSICS DONE · cause: BUG · fix size: small · ESCALATE: 0
