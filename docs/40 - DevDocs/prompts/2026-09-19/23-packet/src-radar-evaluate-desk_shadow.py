    formed_end = ext.culminating_bar_ts + timedelta(minutes=minutes)
    formation = Formation(
        extension_direction=ext.direction, trade_direction=trade_direction, setup_ref=setup_ref,
        trigger=trigger, extreme=extreme, stop=stop, stop_ref=placement.ref.value,
        formed_bar_ts=ext.culminating_bar_ts, formed_bar_end=formed_end, leg_count=ext.leg_count,
    )
    extra["direction"] = trade_direction
    i1_after = tuple(bar for bar in closed_i1 if bar.ts >= formed_end)
    return result(
        "formed", detail(consulted, path, ext.culminating_bar_ts), formation=formation,
        i1_after=i1_after, **extra,
    )


def card_why(td: TradeDef, formation: Formation) -> str:
    return (
        f"{formation.setup_ref} · Extension culminating (path A, {formation.leg_count} legs, "
        f"bar {formation.formed_bar_ts.astimezone(ET):%H:%M} ET) — {formation.trade_direction} on a "
        f"{formation.trigger.bars_cleared}-bar break at {formation.trigger.price}; stop "
        f"{formation.stop.price} beyond the {formation.stop_ref} extreme {formation.extreme.price}"
    )


def desk_shadow() -> DeskShadow:
    """S2: the desk supplies nothing — catalyst DESK_NA, both alignments
    DEFAULT_UNRULED (plan §8 ESCALATE 4)."""
    def entry(reason: str) -> DeskShadowEntry:
        return DeskShadowEntry(na_reason=reason, why_code=reason.lower(), formula_version=DESK_FORMULA_VERSION)

    return DeskShadow(
        catalyst=entry("DESK_NA"), market_alignment=entry("DEFAULT_UNRULED"),
        sector_alignment=entry("DEFAULT_UNRULED"),
    )


# ---------------------------------------------------------------------
