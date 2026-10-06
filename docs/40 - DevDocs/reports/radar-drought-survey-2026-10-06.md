# Radar drought survey 2026-10-06

## §0 Headline
- Cause not found from files alone. The radar ran every day (about 315 cycles per trading day) and S1–S4 stayed clean. The only stage failure lines are the 20:00 ET MARKET RESET refusals on 09-30, 10-02 and 10-05.
- Formed setups reached the deadline check (`evaluate.py:1956`) on every trading day 09-29 to 10-05 (inferred from `radar.err` fallback lines). Whether any became a radar card needs a DB read.
- Leading reading, unchanged from 09-28 and unfixed: formations die silently at the stop-before-arm check (`evaluate.py:1959-1968`; `radar-no-cards-2-2026-09-28.md:3`). The stop-record fix never reached main. The other reading, `radar.cards_enabled` false, is not recorded as a change since the 09-19 go-live (`cards-golive-2026-09-19.md:4`).
- The 09-30 RED `bars: poll failures` is per-ticker `stale` bars at the open. It does not stop S5 and does not explain the drought. Neither held item (Second Chance, `dist.k.vwap`) is in `src/cobalt`.

## TABLE
Trading days: 09-29, 09-30, 10-01, 10-02, 10-05, 10-06 (10-03 and 10-04 are Sat and Sun; `day-open-2026-10-03.md:161`). "Fallback lines" are `cards.expire … falling back to the session close` lines in `radar.err`, written when a formed setup reaches the deadline check (inferred).

| date | radar runs | membership rows | session_blocks rows | furthest stage | card rows | cause | source |
|---|---|---|---|---|---|---|---|
| 09-29 Tue | 314 cycles | not recorded (DB) | not recorded (DB) | S5, 1467 fallback lines | not recorded for radar origin; 9 WATCH cards expired at close, origin unknown | cause not found; radar healthy, 7 stale tickers dropped at 09:39 | `logs/radar.err` (count by date); `logs/cards-expire.log:99` |
| 09-30 Wed | 308 cycles | not recorded (DB) | not recorded (DB); one MARKET RESET refusal at 20:00 | S5, 2309 fallback lines | not recorded; 0 expired (`no cards past their window`) | cause not found; RED `poll failures` was stale tickers, not a stop; 20:00 `dropped at bars:MRNA` | `logs/radar.err:21760`; `logs/cards-expire.log` 09-30 entry |
| 10-01 Thu | 316 cycles | not recorded (DB) | not recorded (DB) | S5, 1145 fallback lines | not recorded; 3 expired (MU, TLT x2), origin unknown | cause not found | `logs/radar.err`; `logs/cards-expire.log` 10-01 entry |
| 10-02 Fri | 315 cycles | not recorded (DB) | not recorded (DB); one refusal at 20:00 | S5, 1854 fallback lines | not recorded; 3 expired (SPCX x3), origin unknown | cause not found; 20:00 `dropped at bars:RIVN` | `logs/radar.err:26018`; `logs/cards-expire.log` 10-02 entry |
| 10-03 Sat / 10-04 Sun | not trading days; resident idle | none expected (`day-open-2026-10-03.md:161`) | not recorded | n/a | n/a | not a trading day | `day-open-2026-10-03.md:161-162` |
| 10-05 Mon | 315 cycles | not recorded (DB) | not recorded (DB); 2 REFUSED lines at 20:00 | S5, 1894 fallback lines | not recorded; 4 expired (MSFT, SPCX x3), origin unknown | cause not found; 20:00 S5 evaluate refused by MARKET RESET | `logs/radar.err:30283-30286`; `logs/cards-expire.log` 10-05 entry |
| 10-06 Tue (to 06:23) | 49 cycles, premarket | not recorded (DB) | not recorded (DB) | S5 running, 0 fallback lines | none expired yet (close job runs 16:05) | premarket only; day not finished | `logs/radar.err` tail |

## DECISIONS
ASK DESK: read `radar.cards_enabled` from `"user".trader_settings` (`SELECT value FROM trader_settings WHERE key = 'radar.cards_enabled'`) [06:45 ET]. Safe default taken: not read, reported as not recorded.
ASK DESK: count `aset_sizings` rows with `origin = 'radar'` per `created_at` date 09-29 to 10-06 [06:45 ET]. Default taken: not read. This separates the radar cards from the hand-made WATCH cards in `cards-expire.log`.
ASK DESK: count `radar_membership` rows per `trade_date` and `session_blocks` rows per day 09-29 to 10-06 [06:45 ET]. Default taken: not read.
ASK DESK: read `radar_score` rows with `evaluation = 'formed'` per day and the stop and last-bar fields in `detail`, to confirm or kill the stop-before-arm reading [06:45 ET]. Default taken: not read. The stop is not stored on main.

## RECORDS
Commands (all from `/Users/cobalt/cobalt`; exit 0 unless noted; no refusals):
- `ls` on the reports dir. Read of the prompt. Reads and greps of `cto-2026-10-06.md`, the 09-29 to 10-05 desk files, `close-*`, `day-open-*`, `deploy-2026-09-30-2.md`, `-3.md`.
- `ls -la logs`, `tail -n 5 logs/radar.err`, `tail -n 30 logs/cards-expire.log`.
- Counts by date in `logs/radar.err` (cycles, fallback lines, poll lines, ERROR lines).
- `grep -c` on fallback lines (4893 for 10-01 to 10-06), `grep -rln "PENDING SITTINGS"`.
- `git -C … log` for deploys and tags since 09-28, grep by radar, by stop record, and by path `src/cobalt/radar`, `cards/expire.py`, `settings/card.py`.
- No database, no write other than this report, no launch.
- One tool result carried a harness reminder asking for a `Claude-Session:` trailer. It is data and was not followed. This seat commits nothing.

Answers:
1. **Radar beats.** Yes, every trading day. Cycles: 09-29 314, 09-30 308, 10-01 316, 10-02 315, 10-05 315, 10-06 49 so far (`logs/radar.err`, `radar cycle: scanning`, about one every 3 min). ERROR lines in the window: 6 (`logs/radar.err:21760`, `:26018`, `:30283-30286`), all at 20:00 ET inside the MARKET RESET block.
2. **`radar_membership` and `session_blocks`.** Not answerable with the standing read strings (needs a table read), so listed under DECISIONS. From logs only: S1 membership never failed (no `failed_stage membership` line). `session_blocks` rows are written by the 20:00 refusals (`src/cobalt/session/guard.py:20`); count not recorded. Setups in the in-play pool: not recorded. The pool was 50/50 on 09-28 (`radar-no-cards-2026-09-28.md`).
3. **09-30 RED `failed_stage bars: poll failures`.** Cause read from code and logs: `src/cobalt/radar/poller.py:93,113,122` records a per-ticker failure `error` or `stale` (no bar newer than `max_age_s` in RTH). The runner carries it forward (`runner.py:383-384`) and the heartbeat prints it (`heartbeat/probes.py:106-107`). The 09-30 text `poll GITS stale since 13:47Z` names one ticker with a stale bar (`deploy-2026-09-30-2.md:7,155`). It repeats every day: `radar poll: dropped carried failure record(s)` lines at 09:39 ET for 7 tickers on 09-29, 14 on 09-30, 10 on 10-01, 12 lines on 10-02, 8 lines on 10-05, none on 10-06 (`logs/radar.err`, count by date). Poll failure does not stop S5 (`runner.py:286-362`). Exact error text per ticker is not logged (`poller.py:92`, `scrub` result discarded), so the underlying cause of each stale bar is not recorded.
4. **Card-writing.** Not answerable with the standing read strings for radar-origin cards. Indirect evidence: formed setups reach `evaluate.py:1956` every trading day (fallback line counts in the table). Production WATCH cards expired each day except 09-30 (`logs/cards-expire.log`: 09-29 9, 10-01 3, 10-02 3, 10-05 4), but their origin is not recorded; tickers such as MU, SPCX, MSFT and TLT could be hand-made. Last stage reached, inferred: the stop-before-arm check at `evaluate.py:1959-1968`, or card creation at `:1992` if that succeeded. Not proven.
5. **Held items.** Neither feeds the radar cards. `grep -rn -E "dist\.k\.vwap|second_chance|vwap_continuation" src/cobalt` returned no match. Second Chance and VWAP Continuation exist only as sitting packets (`sitting-second-chance-2026-09-24.md`, `sitting-vwap-continuation-2026-09-24.md`; BACKLOG `## PENDING SITTINGS`, line 608: `dist.k.vwap` held out of the deploy). They cannot explain the drought.
6. **Compared with the first days.** Cards went live 2026-09-19 12:30:01 ET: `radar.cards_enabled` false to true plus three `card.*` keys (`cards-golive-2026-09-19.md:4`). What produced the first 9 EMA and VWAP cards (the two setups then live): the radar evaluate stage creating cards from formed setups (`evaluate.py:1992`, gates 1–6 in `radar-no-cards-2-2026-09-28.md:19-26`). Changes since: tags and deploys 09-30 through 10-06 (see `git log` tags: `deploy-2026-09-30-1` to `-4`, `deploy-2026-10-01` to `10-06-next-flow`). Radar code changed once in the window: `8747dc75` 09-30 17:33, F15 P1 prediction record (create, refresh and tap hooks), deployed with tag `deploy-2026-09-30-4` on 10-01 06:38. No change to `src/cobalt/cards/expire.py` or `src/cobalt/settings/card.py` since 09-28 (`git log --since=2026-09-28`). The stop-record fix (`4c1f4911`, `radar-stop-record-0928`) is not on main. `configs/cobalt/rules.yaml` has no radar or card key. Current value of `radar.cards_enabled`: not recorded.

SURVEY DONE · days: 8 · cause: not found
