# draft-f4-reserve-fix · 2026-10-26 · card 1049 edited in place

## §0 Headline
- Card `prompts/2026-10-26/1049-f4-strike-reserve-card.md` edited in place; header unchanged. Lines read at main `d94b8e07`.
- Total rule: the refresh gate refuses (new S4: `headroom_rpm < REFRESH_GETS` → no GET), and the strike loop's reservation (S1, S2) keeps the strike loop at most headroom − 3, so the gate's one comparison covers radar + strike + 3 ≤ 50.
- Preflight 2i fixed: S2 runs today's `poll_interval` first, so a `None` headroom ends in `IntervalRefused` before any subtraction. Notes answered: `JobConfigError` is wrapped as `RadarNoteError` (new test), the window is `[opens, closes + 1 min)`.
- 06:48 429: a separate finding, not covered (D3). Next: the Sonnet preflight on 1049.

## DECISIONS
- ASK DESK: strike interval 30 s → 43 s inside 05:45–15:45 ET (5 names, radar 40), weighed against `strike.alert_criterion_s`; for the brain [11:31]. Default: 43 s, as built.
- ASK DESK: S4 breaks the FINAL X13 fixture "a plan `1.0` under the ceiling must pass and must GET" (`F4-FINAL-2026-10-10.md:219`), because 49 + 3 = 52; the card edits `test_prefill_refresh.py:652-657` to refuse it and adds a 3.0-under admit [11:31]. Default: the edit as written; the desk amends FINAL `:219`.
- ASK DESK: the 06:48 tier_a 429 is a separate finding. No scheduled consumer runs at 06:48 (prefill-daily `jobs.yaml:234` 05:15, checkpoints from `:262` 07:15, archiver `:296` 20:30, refresh unloaded). `scheduled_consumers` counts only radar, archiver and replay (`radar/notes.py:358-380`), so no gate counts prefill-daily or the checkpoints. The minute's third consumer is UNPROVEN (L70). The reservation leaves 3 rpm free 05:45–15:45 even when refresh is idle; the card makes no claim about 06:48 [11:31]. Default: its own card, starting from the 429's log line.
- ASK DESK: the reservation starts `lead_s` (this tick's unreserved interval) before the window opens. Without the lead, a tick at 05:44:50 at 30 s pushes 3 strike GETs at the old rate into minute 05:45 (40 + 8 + 3 = 51); this is new beyond the preflight [11:31]. Default: the lead, as S1 writes it.

## RECORDS
- 11:30:52 EDT `date`; `git rev-parse --short=8 main` → `d94b8e07`.
- Read: the prompt 1059; card 1049; `reports/f4-reserve-preflight-2026-10-26.md`; `reports/f4-gate-run-2026-10-26.md` (`:6` X9, `:19` the probe line, via `git grep main`); `topics/writing-rules.md`; `areas/cobalt.md` `## What Cobalt is`, `## Build rules`; `reports/cto-2026-10-26.md:13` (R2491), `:47` (06:48).
- `git show main:` read whole: `src/cobalt/strike/detector.py`, `src/cobalt/radar/notes.py`, `src/cobalt/prefill/daily.py`, `src/cobalt/jobs/config.py`, `configs/cobalt/jobs.yaml`, `tests/cobalt/test_prefill_refresh.py`, `docs/30 - Design/F4-FINAL-2026-10-10.md` (`:170`, `:219-221`, `:286`).
- `git grep -n main` proofs: detector `:103-105`, `:111`, `:167-172`, `:238`, `:273-279`, `:310`, `:313`; notes `:173-215`, `:244`, `:282`, `:358-380`, `:384-391`, `:436`, `:635`; jobs/config `:34`, `:39`, `:48`, `:55`, `:60`, `:171`, `:217`; daily `:98`, `:100`, `:682`, `:708`, `:759-797`, `:800-806`; tunables `:702-703` (50), `:1148-1149` (`05:45-15:45`), `:1160-1161` (30); test_strike_detector `:36`, `:107`, `:145-148`, `:163-165`; test_prefill_refresh `:179-191`, `:622-681`; radar/runner `:573`, `:607-616`; jobs.yaml `:234`, `:262`, `:296`.
- `git grep -c` for `refresh_burst_refusal|refresh_reservation|REFRESH_BURST_RPM` on main: no match (the DEPLOY PROOF before-values of 0 hold).
- ARITHMETIC: 40 + 7 + 3 → ⌈300/7⌉ = 43 s, 6.98 rpm, 49.98; radar 30: ⌈300/17⌉ = 18 s; S4 at 48/2 refused, 47/3 admitted (47 + 3 = 50), 49/1 refused.
- `wc -c` on the card: 8886 before, 14752 after. The growth is S4, the `None` guard, the wrap, the lead, CHECK ASK X6 and `## DECISIONS`.
- 11:32:51 EDT `date`. I ran only reads, made no git write, and launched nothing.

DRAFTED · decisions: 4
