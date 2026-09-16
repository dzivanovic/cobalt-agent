"""Deterministic ASET sizing math. Pure functions — no I/O, no LLMs.

Iteration 4 (ruled by Dejan, 2026-08-28): sizing is fixed-dollar-per-
grade, mirroring Dejan's DAS Trader Pro hotkey files exactly (sheet mode
full/half — see configs/cobalt/aset.yaml). The earlier daily-stop ×
grade-percentage model (docs/90 - References/aset_daily_position_sizer.html,
docs/90 - References/Daily_Stop_Model_Card.pdf) and its TEMP account÷100
prefill override are retired — one-path rule. Historical reference only;
no longer the math this module implements.

Config-completion follow-up (Dejan, 2026-08-28): which grades are
allowed to compute is no longer a hardcoded constant here — it's an
explicit `enabled_grades` argument, resolved by the caller from
`SheetModesConfig.enabled_grades`. This module still reads no config
directly; enabling a grade is purely a `configs/cobalt/aset.yaml` edit.

Slice 2.1a (Dejan, 2026-08-31): two typo guards, same pattern as
enabled_grades — thresholds are resolved by the caller from
`AsetConfig.validation` (configs/dev/aset.yaml) and passed in explicitly
rather than read here, so this module stays config-agnostic. Both are
hard rejects (SizingError), not warnings: a stop-distance guard on
compute_sizing (D3 — a 32% PCG stop typo nothing flagged) and a
fill-vs-entry-distance guard on compute_fill_recompute (D2 — a fat-
fingered 2518.91 fill against a 218.595 entry computed 0 shares and was
persisted twice before the real fill came in). The stop-vs-entry SIDE
check (long below / short above) moved to models.py's SizingInput — it
has no config dependency, so a Pydantic model validator is a better fit
than an engine argument.
"""

from collections.abc import Iterable
from decimal import Decimal
from typing import NamedTuple

from .models import Direction, FillRecompute, Grade, SizingInput, SizingResult

CENTS = Decimal("0.01")

# ≥25% distance change between the planned and actual-fill entry means
# the stop was likely picked against a different price than what was
# actually paid — flag it as possibly no longer structural rather than
# silently recomputing and moving on.
FILL_DISTANCE_WARNING_PCT = Decimal("25")


class SizingError(ValueError):
    """Invalid sizing input — fail loud, never guess."""


def compute_sizing(
    inp: SizingInput,
    enabled_grades: Iterable[Grade],
    max_stop_distance_pct: Decimal,
) -> SizingResult:
    if inp.grade not in enabled_grades:
        raise SizingError(
            f"Grade {inp.grade.value} is not enabled for sheet-mode compute "
            "(see configs/cobalt/aset.yaml enabled_grades) — no trade (SAW)."
        )

    # SizingInput's own model validator already refused a stop on the
    # wrong side of entry, so distance is guaranteed > 0 here.
    distance = abs(inp.entry - inp.stop)
    distance_pct = distance / inp.entry * Decimal("100")
    if distance_pct > max_stop_distance_pct:
        raise SizingError(
            f"Stop is {distance_pct.quantize(CENTS)}% from entry — exceeds the "
            f"{max_stop_distance_pct}% typo guard (configs/dev/aset.yaml "
            "validation.max_stop_distance_pct). Refusing, not warning."
        )

    risk_budget = inp.risk_dollars
    shares = int(risk_budget / distance)
    used_risk = distance * shares

    is_long = inp.direction is Direction.LONG
    target_1r = inp.entry + distance if is_long else inp.entry - distance
    target_2r = inp.entry + distance * 2 if is_long else inp.entry - distance * 2

    warnings: list[str] = []
    if shares < 1:
        warnings.append(
            "Position size rounds to zero: risk per share exceeds the allocated risk budget."
        )

    return SizingResult(
        input=inp,
        risk_budget=risk_budget.quantize(CENTS),
        per_share_risk=distance,
        shares=shares,
        used_risk=used_risk.quantize(CENTS),
        target_1r=target_1r.quantize(CENTS),
        target_2r=target_2r.quantize(CENTS),
        warnings=warnings,
    )


def stop_distance(*, entry: Decimal, stop: Decimal, direction: Direction) -> Decimal:
    """|entry - stop|, after the side check. The one place both the
    stop-edit recompute and an UNSIZED radar card's stop edit (S2-P2,
    Astra R1-6) get their distance from: an unsized WATCH card has no
    risk budget to divide by, but its stop must still sit on the right
    side and its distance still feeds proximity."""
    if entry <= 0:
        raise SizingError("entry must be positive")
    if direction is Direction.LONG and stop >= entry:
        raise SizingError(
            f"Long stop ({stop}) must be below entry ({entry}) — refusing, not warning."
        )
    if direction is Direction.SHORT and stop <= entry:
        raise SizingError(
            f"Short stop ({stop}) must be above entry ({entry}) — refusing, not warning."
        )
    return abs(entry - stop)


class StopEditRecompute(NamedTuple):
    """What a moved stop does to the rest of the card (decision 11)."""

    per_share_risk: Decimal
    shares: int
    used_risk: Decimal
    shares_changed: bool


def recompute_for_stop(
    *,
    entry: Decimal,
    stop: Decimal,
    direction: Direction,
    risk_budget: Decimal,
    in_trade_shares: int | None = None,
) -> StopEditRecompute:
    """Re-derive risk from a moved stop. Mock decision 11: "Stop edits
    recompute shares/risk/targets/room live."

    THE IN-TRADE CASE IS NOT THE PRE-TRADE CASE, and conflating them
    would be a real trading error:

    * **Pre-trade (WATCH)** — the risk budget is fixed and the position
      is not on yet, so a wider stop buys FEWER shares.
      `shares = risk_budget / per_share_risk`, as at card creation.
    * **In-trade (FILLED)** — the shares are already bought. Moving the
      stop cannot un-buy them, so the share count is held and what
      changes is the OPEN RISK (`shares x per_share_risk`). Recomputing
      shares here would silently report a position he does not have.

    Pure arithmetic, no I/O — and the same expression `compute_sizing`
    uses, factored out rather than copied (one-path rule), so a stop
    edit can never disagree with the card it edits.
    """
    per_share_risk = stop_distance(entry=entry, stop=stop, direction=direction)
    if in_trade_shares is not None:
        return StopEditRecompute(
            per_share_risk=per_share_risk,
            shares=in_trade_shares,
            used_risk=(per_share_risk * in_trade_shares).quantize(CENTS),
            shares_changed=False,
        )
    shares = int(risk_budget / per_share_risk)
    return StopEditRecompute(
        per_share_risk=per_share_risk,
        shares=shares,
        used_risk=(per_share_risk * shares).quantize(CENTS),
        shares_changed=True,
    )


# ---------------------------------------------------------------------
# The radar ladder: keys, snap DOWN only (S2-P2 STEP-6, ruling R8)
# ---------------------------------------------------------------------

#: The keys a radar card offers, HIGH to LOW. D is not a key: it is the
#: SAW grade ($0), and "pass" is a state move, not a size.
LADDER_KEYS: tuple[Grade, ...] = (Grade.A_PLUS, Grade.A, Grade.B, Grade.C)


class KeyRefused(SizingError):
    """A key tap that cannot size — nothing enabled at or below it."""


class KeyOption(NamedTuple):
    """One key on the card: its grade, the dollars it sizes on today's
    sheet, and whether today's rung enables it. A disabled key still
    carries its would-be dollars so the greyed key tells the truth."""

    grade: Grade
    dollars: Decimal
    enabled: bool


def key_ladder(sheet_modes, sheet: str, enabled: Iterable[Grade]) -> tuple[KeyOption, ...]:
    """Every ladder key with `dollars_for(sheet, key)`. `sheet_modes` is
    the `SheetModesConfig` read from `trader_settings`; this module still
    reads no config itself."""
    allowed = set(enabled)
    return tuple(
        KeyOption(grade, sheet_modes.dollars_for(sheet, grade), grade in allowed)
        for grade in LADDER_KEYS
    )


def snap_down(tapped: Grade, enabled: Iterable[Grade]) -> tuple[Grade | None, str | None]:
    """(sized, notice). R8: the tapped key if enabled; otherwise the
    nearest ENABLED key BELOW it, with a notice; otherwise (None, the
    refusal). Never up — a key he did not reach for is never sized."""
    if tapped not in LADDER_KEYS:
        raise KeyRefused(
            f"{tapped.value} is not a ladder key (keys: "
            f"{', '.join(g.value for g in LADDER_KEYS)})"
        )
    allowed = set(enabled)
    if tapped in allowed:
        return tapped, None
    for grade in LADDER_KEYS[LADDER_KEYS.index(tapped) + 1:]:
        if grade in allowed:
            return grade, (
                f"{tapped.value} is not enabled today — recorded {tapped.value}, "
                f"sized at {grade.value}, the nearest enabled key below"
            )
    return None, (
        f"{tapped.value} is not enabled today and nothing enabled below it "
        f"(enabled: {', '.join(sorted(g.value for g in allowed)) or 'none'}) — refused, no size"
    )


class KeySizing(NamedTuple):
    tapped_grade: Grade
    sized_grade: Grade
    snap_notice: str | None
    result: SizingResult


def size_at_key(
    tapped: Grade,
    *,
    ticker: str,
    entry: Decimal,
    stop: Decimal,
    direction: Direction,
    sheet_modes,
    sheet: str,
    enabled: Iterable[Grade],
    max_stop_distance_pct: Decimal,
) -> KeySizing:
    """Size a radar card at a tapped key: `snap_down`, then the ONE
    sizing path (`compute_sizing`) at the snapped key's sheet dollars.
    The notice names the dollars so the amber line reads on its own."""
    allowed = list(enabled)
    sized, notice = snap_down(tapped, allowed)
    if sized is None:
        raise KeyRefused(notice)
    dollars = sheet_modes.dollars_for(sheet, sized)
    result = compute_sizing(
        SizingInput(
            ticker=ticker, grade=sized, direction=direction, sheet_mode=sheet,
            risk_dollars=dollars, entry=entry, stop=stop,
        ),
        allowed,
        max_stop_distance_pct,
    )
    if notice is not None:
        notice = f"{notice} (${dollars} on the {sheet} sheet)"
    return KeySizing(tapped, sized, notice, result)


def compute_fill_recompute(
    original: SizingResult,
    actual_fill: Decimal,
    max_fill_distance_pct: Decimal,
) -> FillRecompute:
    """Recompute shares at the actual fill price, same grade dollars and
    same stop. Note-only — never persisted to Postgres as a new row."""
    if actual_fill <= 0:
        raise SizingError("actual_fill must be positive")

    inp = original.input
    fill_vs_entry_pct = abs(actual_fill - inp.entry) / inp.entry * Decimal("100")
    if fill_vs_entry_pct > max_fill_distance_pct:
        raise SizingError(
            f"Fill {actual_fill} is {fill_vs_entry_pct.quantize(CENTS)}% from card "
            f"entry {inp.entry} — exceeds the {max_fill_distance_pct}% typo guard "
            "(configs/dev/aset.yaml validation.max_fill_distance_pct). "
            "Refusing — nothing written."
        )

    new_distance = abs(actual_fill - inp.stop)
    if new_distance == 0:
        raise SizingError("Actual fill and stop cannot be the same price.")

    risk_budget = inp.risk_dollars
    recomputed_shares = int(risk_budget / new_distance)
    recomputed_used_risk = (new_distance * recomputed_shares).quantize(CENTS)

    planned_distance = original.per_share_risk
    distance_change_pct = (
        abs(new_distance - planned_distance) / planned_distance * Decimal("100")
    ).quantize(CENTS)

    structural_warning = None
    if distance_change_pct >= FILL_DISTANCE_WARNING_PCT:
        structural_warning = "stop may no longer be structural — re-read the level."

    return FillRecompute(
        original=original,
        actual_fill=actual_fill,
        recomputed_shares=recomputed_shares,
        recomputed_used_risk=recomputed_used_risk,
        share_delta=recomputed_shares - original.shares,
        distance_change_pct=distance_change_pct,
        structural_warning=structural_warning,
    )
