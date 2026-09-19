def htf_level_proximity(series: DailySeries, trade_date: date, last_price: Decimal) -> HtfProximity:
    prior = prior_session(series, trade_date)
    atr = daily_atr(series, trade_date)
    if atr.value <= 0:
        raise InsufficientBars("daily ATR is zero — proximity undefined", ATR_PERIOD, 0)
    to_high, to_low = abs(last_price - prior.high), abs(last_price - prior.low)
    reference, level, distance = (
        ("prior_high", prior.high, to_high) if to_high <= to_low else ("prior_low", prior.low, to_low)
    )
    with localcontext() as ctx:
        ctx.prec = PRECISION
        value = distance / atr.value
    return HtfProximity(
        value=value, reference=reference, level=level, last_price=last_price, prior=prior, atr=atr
    )

