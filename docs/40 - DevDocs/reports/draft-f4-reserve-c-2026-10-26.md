# draft-f4-reserve-c · 2026-10-26 · DRAFTED

## §0 Headline
- Card 1049 is redrafted in place around his ruling C. The rows are R1 (radar cap `radar.finviz_rpm` = 37), R2 (refresh gate: cap + headroom + 3 ≤ ceiling), R3 (X15 probe with the radar capped), R4 (the FINAL X13 amendment), R5 (RUN) and D0. The S1-S4 strike rows are gone. Strike is untouched.
- The cap is a real per-minute cap with no wider change. `TokenBucket` capacity is 1.0 (`radar/collector.py:55`), so a saturated bucket at 37 grants 37 requests in any half-open minute. Only the bucket's rpm source changes, at `runner.py:522` and in the two collector defaults.
- The plan fixture must move from 10/40 to 40/10. Under C, 10/40 gives 37 + 40 + 3 = 80, and every refresh test would be refused.
- The X13 1.0-under fixture stays admitted under C (37 + 1 + 3 = 41). This differs from the prompt's "keep the X13 change" (D2).
- Decisions: 5.

## DECISIONS
- ASK DESK: port4 (card 1068) also edits `radar/runner.py` and restarts radar. The card ships after it, back to back, and BASE `05366873` predates port4 [17:54]. Default: the desk resets BASE to a main that holds port4; the builder re-finds places by content.
- ASK DESK: the X13 1.0-under test (`test_prefill_refresh.py:652-657`) is admitted under C (41 ≤ 50). Refusing it would contradict C [17:54]. Default: it stays a green guard; the new refusing fixture is 30/20 (60 > 50); R4's amendment states both.
- ASK DESK: outside this card: (a) refresh is refused whenever the radar's planned rpm is under 37, and the live planned rpm is UNPROVEN; (b) when planned < 37, radar 37 + strike at its headroom can exceed 50 without refresh; (c) `radar/notes.py:640`'s cold-cycle estimate still divides by the ceiling [17:54]. Default: all three recorded in the card, none built.
- ASK DESK: scan cost: the brain's figure is ≈ 8% (3 → 3¼ min); the drafter's bucket-only bound is +16% (180 → 209 s) [17:54]. Default: the card's WHY gives both; the first live cycles measure it.
- ASK DESK: the window-open lead has no object under C, because the cap is in force all day [17:54]. Default: no lead.

## RECORDS
- 17:54 EDT `date`; `git rev-parse --short=8 main` → `e015c97b`.
- Read: prompt 1070; card 1049 (HEAD); `reports/draft-f4-reserve-amend-2026-10-26.md`; `reports/cto-2026-10-26.md:69-72`; `reports/cto-2026-10-26-words.md:1-4`; `reports/f4-gate-run-2026-10-26.md:6`, `:14-21`; card 1068 rows `:17`, `:25`; `topics/writing-rules.md`; `LAWS.md:136-137` (L10); `prompts/BUILD-HUB.md` RESTARTS (`:77-78`).
- Read with `git show main:`: `src/cobalt/radar/collector.py`, `runner.py`, `config.py`, `cli.py`, `notes.py` (`:270-299`, `:615-644`), `src/cobalt/strike/detector.py`, `src/cobalt/prefill/daily.py` (`:88-101`, `:670-819`), `src/cobalt/prefill/refresh_probe.py`, `src/cobalt/taxonomy/tunables.py`, `configs/cobalt/taxonomy/tunables.yaml` (`:665-744`), `docs/30 - Design/F4-FINAL-2026-10-10.md` (`:169-172`, `:218-223`), `tests/cobalt/test_radar_collector.py`, `test_radar_config.py`, `test_refresh_probe.py`, `test_prefill_refresh.py` (`:150-194`, `:605-690`).
- Proved with `git grep -n main`: collector `:42`, `:54`, `:55`, `:62`, `:78`, `:154`, `:256`; config `:200`, `:210`, `:222`; probe `:23`, `:62`, `:72`, `:77`, `:321`, `:407`; notes `:643`; tests prefill_refresh `:179`, `:182`, radar_config `:22`, `:220`, radar_collector `:34`, price_floor `:376`, refresh_probe `:59`, `:187`, `:233`. Collector constructions in `src`: only `runner.py:547`, `:559`, `:562` and `replay/cli.py:69`. `radar_bucket_rpm`, `refresh_burst_refusal`, `radar.finviz_rpm`, `radar_cap` absent on main (git grep exit 1). The plist is listed on disk.
- Filter-string check: `grep -c` of `exch_` and `f=` in the card → `0`.
- Card size: `wc -c` 14752 (HEAD, `git cat-file -s`) → 20371. The growth comes from six rows replacing four, plus the cap proof under WHY.
- 18:00:35 EDT `date`. Card 1049 and this report written; nothing run, no git write, nothing launched.

DRAFTED · decisions: 5
