
    @property
    def computed(self) -> bool:
        return self.source in COMPUTED_SOURCES and self.tier == "deterministic" and self.factor not in DESK_FACTORS


def _half_up(value: Decimal, exp: Decimal = ONE) -> Decimal:
    return value.quantize(exp, rounding=ROUND_HALF_UP)


def grade_from_curve(value: Decimal, curve: Curve) -> tuple[Decimal, int]:
    """(unrounded, grade). Piecewise-linear between anchors, flat beyond
    the ends, clipped to 1–10, rounded half-up once."""
    anchors = curve.anchors
    with localcontext() as ctx:
        ctx.prec = 28
        if value <= anchors[0].x:
            raw = anchors[0].grade
        elif value >= anchors[-1].x:
            raw = anchors[-1].grade
        else:
            raw = anchors[-1].grade
            for lo, hi in zip(anchors, anchors[1:]):
                if lo.x <= value <= hi.x:
                    raw = lo.grade + (value - lo.x) * (hi.grade - lo.grade) / (hi.x - lo.x)
                    break
        raw = min(max(raw, ONE), TEN)
    return raw, int(_half_up(raw))


def _why(factor: QualityFactor, value: Decimal, grade: int) -> str:
    if factor.why_template:
        return factor.why_template.format(value=value, grade=grade)
    return f"{factor.name} {value} → {grade}"


def compute_dots(
    factors: Iterable[QualityFactor],
    observations: Mapping[str, FactorObservation],
    curves: Mapping[str, Curve] | None,
    *,
    at: datetime,
) -> list[Dot]:
    """Fresh dots for one scan. No taps, no history — `refresh_dots`
    carries those across from the stored row."""
    out: list[Dot] = []
    for position, factor in enumerate(factors):
        base = dict(factor=factor.name, position=position, tier=factor.tier)
        if factor.name in DESK_FACTORS:
            reason = DESK_NA_REASON[factor.name]
            out.append(Dot(
                **base, source="cobalt-degraded", role="shadow",
                na_reason=reason, engine_why=f"desk shadow: n/a ({reason})",
            ))
            continue
        if factor.source not in COMPUTED_SOURCES or factor.tier != "deterministic":
            out.append(Dot(**base, source="human", role="human"))
            continue
        obs = observations.get(factor.name)
        common = dict(**base, source=factor.source, role="shadow")
        if obs is None:
            out.append(Dot(**common, na_reason="MANUAL", engine_why=f"{factor.name}: no Cobalt computer — MANUAL"))
            continue
        inputs = dict(obs.inputs)
        if obs.stale:
            out.append(Dot(
                **common, engine_value=obs.value, engine_inputs=inputs, engine_formula=obs.formula,
                na_reason="input_stale", engine_why=f"{factor.name}: input stale — grade suppressed",
            ))
            continue
        if obs.value is None:
            out.append(Dot(
                **common, engine_inputs=inputs, engine_formula=obs.formula, na_reason="input_unavailable",
                engine_why=f"{factor.name}: unavailable ({obs.unavailable or 'no value'})",
            ))
            continue
        curve = (curves or {}).get(factor.name)
        if curve is None:
            out.append(Dot(
                **common, engine_value=obs.value, engine_inputs=inputs, engine_formula=obs.formula,
                na_reason="curve_unset", engine_why=f"{factor.name} {obs.value} — card.curves anchors unset",
            ))
            continue
        unrounded, grade = grade_from_curve(obs.value, curve)
        inputs["curve"] = curve.pairs()
        inputs["unrounded_grade"] = str(unrounded)
        out.append(Dot(
            **common, engine_value=obs.value, engine_grade=grade, engine_why=_why(factor, obs.value, grade),
            engine_inputs=inputs, engine_formula=obs.formula,
        ))
    return out
