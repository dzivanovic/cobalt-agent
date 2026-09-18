"""True range, Wilder ATR and the volume band — conventions written down.

Astra R1-9 (L52-a): a named operand is not a traceable one. Every
convention a recompute needs is fixed here and carried on the
observation, so an auditor in another house can reproduce the number
from the stored bars alone:

ATR
  * true range of the FIRST bar in the window = high − low (no prior
    close exists inside the window; nothing outside it is read);
  * later bars: max(high − low, |high − prev close|, |low − prev close|);
  * seed = simple mean of the first `period` true ranges;
  * Wilder smoothing after the seed: atr = (atr·(period−1) + tr) / period;
  * warm-up: fewer than `period` bars → `InsufficientBars`, never a
    partial average.
  `period` is 14 (TAXONOMY v0.7 §3.8, "ATR(working_tf, 14)").

Volume band
  * sample = exactly the `n` bars immediately BEFORE the candidate bar
    (the candidate is never in its own sample);
  * mean = arithmetic mean; sigma = POPULATION standard deviation
    (divide by n);
  * threshold = mean + k·sigma, k from `extension.path_a_volume_sigma`;
  * fewer than `n` prior bars → `InsufficientBars`.

All arithmetic is `Decimal` at 28 significant digits, so the stored value
and an independent float recompute agree well inside 1e-6.
"""

from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from decimal import Decimal, localcontext
from typing import Literal, Protocol

from pydantic import AwareDatetime, BaseModel, ConfigDict

ATR_PERIOD = 14
PRECISION = 28


class InsufficientBars(ValueError):
    """Warm-up not met. Carries what was needed and what was there."""

    def __init__(self, what: str, needed: int, have: int):
        self.needed, self.have = needed, have
        super().__init__(f"{what}: needs {needed} bars, have {have}")


class OHLCV(Protocol):
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int


class AtrObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    value: Decimal
    period: int
    method: Literal["wilder"] = "wilder"
    seed: Literal["sma_first_period"] = "sma_first_period"
    first_true_range: Literal["high_minus_low"] = "high_minus_low"
    bars_used: int
    #: Intraday windows name their last bar; daily windows their session.
    last_bar_ts: AwareDatetime | None = None
    last_session_date: date | None = None


class VolumeBand(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    mean: Decimal
    sigma: Decimal
    k: Decimal
    threshold: Decimal
    n: int
    sigma_convention: Literal["population"] = "population"
    sample_first_ts: AwareDatetime | None = None
    sample_last_ts: AwareDatetime | None = None


def true_ranges(bars: Sequence[OHLCV]) -> list[Decimal]:
    out: list[Decimal] = []
    prev_close: Decimal | None = None
    for bar in bars:
        span = bar.high - bar.low
        if prev_close is None:
            out.append(span)
        else:
            out.append(max(span, abs(bar.high - prev_close), abs(bar.low - prev_close)))
        prev_close = bar.close
    return out


def wilder_atr(bars: Sequence[OHLCV], period: int = ATR_PERIOD) -> AtrObservation:
    if len(bars) < period:
        raise InsufficientBars("ATR", period, len(bars))
    with localcontext() as ctx:
        ctx.prec = PRECISION
        trs = true_ranges(bars)
        atr = sum(trs[:period], Decimal(0)) / period
        for tr in trs[period:]:
            atr = (atr * (period - 1) + tr) / period
    last = bars[-1]
    return AtrObservation(
        value=atr, period=period, bars_used=len(bars),
        last_bar_ts=getattr(last, "ts", None),
        last_session_date=getattr(last, "session_date", None),
    )


def volume_band(prior: Sequence[OHLCV], n: int, k: Decimal) -> VolumeBand:
    """The band from the `n` bars ending just before the candidate."""
    if n <= 0:
        raise ValueError(f"volume band n must be positive, got {n}")
    if len(prior) < n:
        raise InsufficientBars("volume band", n, len(prior))
    sample = list(prior)[-n:]
    with localcontext() as ctx:
        ctx.prec = PRECISION
        volumes = [Decimal(bar.volume) for bar in sample]
        mean = sum(volumes, Decimal(0)) / n
        variance = sum(((v - mean) ** 2 for v in volumes), Decimal(0)) / n
        sigma = variance.sqrt()
        threshold = mean + k * sigma
    return VolumeBand(
        mean=mean, sigma=sigma, k=k, threshold=threshold, n=n,
        sample_first_ts=getattr(sample[0], "ts", None),
        sample_last_ts=getattr(sample[-1], "ts", None),
    )


__all__ = [
    "ATR_PERIOD", "AtrObservation", "InsufficientBars", "OHLCV", "VolumeBand",
    "true_ranges", "volume_band", "wilder_atr",
]
