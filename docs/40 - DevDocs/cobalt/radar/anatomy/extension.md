# `src/cobalt/radar/anatomy/extension.py`

## What it does
`detect_extension(run, params) -> ExtensionObservation` detects an intraday Extension (TAXONOMY v0.7 §3.2) over the run from the session open to the last closed working bar. The run's direction is the sign of last close − session open.

## The two paths (R4)
- **Path A (lands cards):** a bar in the run direction whose volume is at least the volume band threshold of the `n` bars before it, AND whose body is strictly wider than every earlier body of the run. The latest such bar is the culmination, and the result is `instantiated=True, state="culminating", path="A"`.
- **Path B-only:** |last close − open| ≥ `path_b_atr` × ATR(14) with no path-A bar. The catalyst is unknown in S2, so this reports `path="B_only"`, `unavailable="catalyst_ref_unknown"`, with `instantiated` and `state` both None. It is logged by the dry-run and never produces a card, but it is not reported as "not instantiated" either.

## Key functions/classes
`ExtensionParams.from_tunables(rows)` reads `extension.path_a_volume_ma_bars` (n), `extension.path_a_volume_sigma` (k) and `extension.path_b_atr`. A missing or unmeasured row raises. The observation stores every intermediate: session open, last close, the culminating bar's ts, volume and body, the widest prior body, the band, the ATR, the distance in ATRs and the params.

## Gotchas
Any incomplete bucket in the run gives `unavailable="incomplete_bucket"`. Fewer than max(n+1, 14) bars gives `insufficient_bars`. The value is never computed from part of the run. A run that closes exactly at its open has no direction and is not instantiated.

## 2026-09-22 — D4, the lifecycle (setups one build STEP-5; FINAL §3 D4, [F-03 · X10])

`extension_lifecycle(run, ext, params, ema9=, slope_bars=)` is a SEPARATE function over `detect_extension`'s output. `ExtensionObservation`, path A / path B and `TUNABLE_KEYS` stay byte-identical: the committed day's dumps are pinned on the start code in `tests/cobalt/test_setups_d4.py`.

**The construction** (in the module), for a culminated run in direction d:

- **The turn** is the run's tracked extreme, `structure.tracked_extreme` (the `turn_low` / `turn` refs).
- **`reverting`** starts at the first bar after the turn that moves against d and clears the extremes of the `n` preceding bars (`A-08`, `extension.snapback_bars_cleared`).
- **`backside`** follows once reverting. It needs ≥ `extension.backside_hh_min` higher highs and ≥ `extension.backside_hl_min` higher lows (the turn's low is the first swing low), with the last close above EMA9 and EMA9 rising over `slope_norm.bars`. If the slope's inputs are missing the state is unavailable (`slope_norm.bars_unset` / `insufficient_seed`), never guessed.
- `building` / `extending` / `resuming` have no rule in the FINAL and are not produced; E8 names them.

**Production safety (NN#16).** `lifecycle_params` returns `<key>_unset` for a null `LIFECYCLE_KEYS` row. While `A-08` is null (committed config), the frame's `Extension.state` reads exactly today's `culminating | none`, so Rubberband is unchanged. Once the row is filled, a culminated Extension moves on to `reverting` after its snapback. That is by the taxonomy's lifecycle; it is an ESCALATE in the build report.

**X10 FAILED.** On a constructed backside day that recovers past the open, the Extension's direction (sign of last − open, `:96-103`) flips, so the backside shape never forms. The same construction before the open forms long. The FINAL offers two fixes, Grok's and Fable's, and chooses neither. Nothing here implements either.
