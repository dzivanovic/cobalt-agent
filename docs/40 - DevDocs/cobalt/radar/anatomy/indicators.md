# `src/cobalt/radar/anatomy/indicators.py`

## What it does
True range, Wilder ATR and the volume band. Every convention a recompute needs is written down and carried on the observation (Astra R1-9, L52-a), so another house can reproduce each number from stored bars alone.

## Key functions/classes
- `true_ranges(bars)`: the first bar is `high − low`; later bars take max(high − low, |high − prev close|, |low − prev close|). Nothing outside the window is read.
- `wilder_atr(bars, period=14) -> AtrObservation`: seed = simple mean of the first `period` true ranges, then `(atr·(period−1) + tr)/period`. Fewer than `period` bars raises `InsufficientBars`, never a partial average.
- `volume_band(prior, n, k) -> VolumeBand`: the sample is exactly the `n` bars before the candidate; mean is arithmetic; sigma is POPULATION (÷n); threshold = mean + k·sigma.
- `OHLCV` is the protocol both `WorkingBar` and `DailyBar` satisfy.
- `ema(bars, period) -> EmaObservation` (S2-P2 STEP-7; Astra R1-12 found no step computing EMA9): the seed is the simple mean of the first `period` closes, then `alpha·close + (1−alpha)·ema` with `alpha = 2/(period+1)`. Fewer than `period` bars raises `InsufficientBars`. The period comes from `defaults.yaml` `ma.fast`.

## Gotchas
All arithmetic uses `Decimal` at 28 significant digits (`PRECISION`), so a float recompute agrees well inside 1e-6. The observation records `last_bar_ts` for intraday windows and `last_session_date` for daily ones.

## 2026-09-21 — seeding (setups one build STEP-3; FINAL §5 `A-05`, [F-10])

`seeded(fn, premarket, run, period) -> Seeded` is the ONE warm-up rule for the rolling indicators. It runs the ONE function each indicator already has (`ema`, `wilder_atr`) over the series it picks:

- with at least `period` complete premarket working buckets, the series is premarket + RTH run (`source="premarket"`), so the first RTH value continues the seeded series;
- otherwise, the RTH run alone (`source="rth_only"`);
- with neither long enough, `unavailable="insufficient_seed"` — later, never guessed.

So `atr_seeded` and the Extension's `atr_working` are both `wilder_atr`: one function, two named inputs ([F-10]). No second ATR function exists; a test asserts `__all__`. The frame picks the complete premarket buckets (`frame.premarket_buckets`). `WARMUP_CONVENTION = "frame.warmup_source"` names the `A-05` convention row this rule implements.
