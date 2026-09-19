class Formation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    extension_direction: Literal["up", "down"]
    trade_direction: Literal["long", "short"]
    setup_ref: str
    trigger: TriggerLevel
    extreme: TrackedExtreme
    stop: StructuralStop
    stop_ref: str
    formed_bar_ts: AwareDatetime
    formed_bar_end: AwareDatetime
    leg_count: int | None


class MemberEvaluation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
FACTOR_COMPUTERS = ("atrs_from_open", "rvol", "Extension.leg_count", "htf_level_proximity")


def _factor_observations(
    ext: ExtensionObservation, member: MemberInput, *, intraday_stale: bool, daily_ok: bool,
    last_price: Decimal | None, scan_interval: int,
) -> dict[str, FactorObservation]:
    out: dict[str, FactorObservation] = {}
    atr = ext.atr
    out["atrs_from_open"] = FactorObservation(
        value=ext.distance_from_open_atr, stale=intraday_stale,
        unavailable=ext.unavailable if ext.distance_from_open_atr is None else None,
        inputs={"session_open": _s(ext.session_open), "last_close": _s(ext.last_close),
                "atr": _s(atr.value) if atr else None, "atr_period": atr.period if atr else None,
                "atr_bars_used": atr.bars_used if atr else None},
        formula="|last_close - session_open| / ATR(working_tf, 14) wilder, sma seed",
    )
    if member.rvol is None or member.rvol.value is None:
        out["rvol"] = FactorObservation(value=None, unavailable="no_rvol_observation", formula="screener RVOL")
    else:
        stale = intraday_staleness(
            observed_at=member.rvol.observed_at, as_of=member.as_of, scan_interval=scan_interval
        ).stale
        out["rvol"] = FactorObservation(
            value=Decimal(str(member.rvol.value)), stale=stale,
            inputs={"rvol": str(member.rvol.value), "observed_at": member.rvol.observed_at.isoformat(),
                    "source": member.rvol.source, "precedence": member.rvol.precedence},
            formula="screener RVOL (precedence screen>list, note order, source id)",
        )
    out["Extension.leg_count"] = FactorObservation(
        value=None if ext.leg_count is None else Decimal(ext.leg_count), stale=intraday_stale,
        unavailable=ext.unavailable, inputs={"leg_count": ext.leg_count},
        formula="legs in the run direction, terminated by one opposing bar",
    )
    if not daily_ok or member.daily is None or last_price is None:
        out["htf_level_proximity"] = FactorObservation(
            value=None, stale=member.daily is not None and not daily_ok,
            unavailable=member.daily_status if member.daily is None else "no_last_price",
            formula="min(|last - prior high|, |last - prior low|) / daily ATR(14)",
        )
    else:
        try:
            prox = htf_level_proximity(member.daily, member.trade_date, last_price)
            out["htf_level_proximity"] = FactorObservation(
                value=prox.value,
                inputs={"reference": prox.reference, "level": str(prox.level), "last_price": str(last_price),
                        "daily_atr": str(prox.atr.value), "prior_session": prox.prior.session_date.isoformat()},
                formula="min(|last - prior high|, |last - prior low|) / daily ATR(14)",
            )
        except (NoDailyBars, InsufficientBars) as e:
            out["htf_level_proximity"] = FactorObservation(value=None, unavailable=type(e).__name__, formula="")
    return out
