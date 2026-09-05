"""F6 stage 2: the 09:00 proposal, and the sentence that justifies it.

Charter §3 F6 (M4): "at 09:00 Cobalt proposes with reason from prior DRC
+ running goal + context; his approve/overrule with reason persists."

TWO STAGES, ONE LADDER:

* **Stage 1, before 09:00** — the LOWEST ENABLED mode, by system rule.
  No input is asked for. This is market mechanics, not a personal gate:
  no stop can rest premarket, so the floor is not a judgement anyone
  needs to make at 05:15. It is `config.lowest_enabled` and nothing else,
  and it is not persisted (see store.py).
* **Stage 2, at 09:00** — this module. Cobalt proposes; he approves or
  overrules with a reason; until he answers, the sheet stays on stage 1.

THE PROPOSAL RULE, and its honest status. `propose()` starts at the
highest permitted rung and STEPS DOWN once per adverse signal, then
clamps into `enabled_modes`:

    proposed = clamp( max(lowest_enabled, ceiling_after_step_downs) )

Every step-down names itself in the reason string, so the sentence is a
derivation and not a summary. **The step-down set below is PROVISIONAL
and belongs to the Rules Engine design session** — it is deliberately
crude, it is marked as such in the reason he reads, and the whole
`_SIGNALS` list is meant to be replaced wholesale rather than tuned.
`daymode.trade_count_band.{min,max}` ship as PLACEHOLDER tunables rows
for the same reason: until he rules them, an unruled band is itself an
adverse signal that pins the proposal to the floor, which is the
conservative direction to be wrong in.

At S1, with `enabled_modes: [reduced]`, the clamp makes the proposal
`reduced` every single time — the ladder logic still runs in full and
the tests exercise the higher rungs by enabling them in config, which is
the point of deriving the ladder rather than hardcoding it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any, Optional

from cobalt.session import session_clock

from .config import DayModeConfig, load_daymode_config

#: The tunables rows F6 consumes. PLACEHOLDER values pending the Rules
#: Engine session — `validate` checks they EXIST; nothing pretends to
#: know what they should be.
BAND_MIN_KEY = "daymode.trade_count_band.min"
BAND_MAX_KEY = "daymode.trade_count_band.max"

#: The literal the reason carries when no DRC can be found for the prior
#: trading day. Loud, and surfaced in the sheet banner — an absent DRC is
#: information, not a blank.
NO_PRIOR_DRC = "no prior DRC"


@dataclass
class Proposal:
    trade_date: date
    proposed: str
    reason: str
    stage1_mode: str
    signals: list[str] = field(default_factory=list)
    prior_trading_day: Optional[date] = None
    prior_filled: int = 0
    drc_note: Optional[str] = None


def stage1_mode(cfg: Optional[DayModeConfig] = None) -> str:
    """The pre-09:00 mode. A system rule, asking nothing."""
    return (cfg or load_daymode_config()).lowest_enabled


def _step_down(cfg: DayModeConfig, mode: str) -> str:
    rank = cfg.rank(mode)
    return cfg.modes[max(0, rank - 1)]


def prior_trading_day(day: date) -> date:
    """The last trading day strictly before `day`, by the NYSE calendar."""
    clock = session_clock()
    probe = day - timedelta(days=1)
    for _ in range(30):
        if clock.calendar.is_trading_day(probe):
            return probe
        probe -= timedelta(days=1)
    raise RuntimeError(f"no trading day found in the 30 days before {day}")


def build_reason(
    cfg: DayModeConfig,
    day: date,
    *,
    prior_day: date,
    prior_filled: int,
    daily_stop_hit: bool,
    drc_note: Optional[str],
    band: tuple[Any, Any],
    signals: list[str],
    proposed: str,
) -> str:
    """The sentence he reads at 09:00. Assembled from four named inputs.

    Never an LLM: this is a derivation from counted rows and config, and
    a figure Cobalt cannot source is stated as absent rather than filled
    in (fail-loud, and CLAUDE.md's "extracted figures require verbatim
    source quotes").
    """
    clock = session_clock()
    band_min, band_max = band
    parts = [
        f"prior trading day {prior_day} ({clock.calendar.describe(prior_day).split(' is ')[-1]}): "
        f"{prior_filled} FILLED card(s)"
        + (", DAILY STOP marker present" if daily_stop_hit else ""),
        f"prior DRC: {drc_note or NO_PRIOR_DRC}",
        f"today: {clock.calendar.describe(day).split(' is ')[-1]}",
        "trade-count band: "
        + (
            f"{band_min}-{band_max}"
            if band_min is not None and band_max is not None
            else "PLACEHOLDER (unruled, pending the Rules Engine session)"
        ),
    ]
    ladder = " < ".join(cfg.modes)
    body = " · ".join(parts)
    step = "; ".join(signals) if signals else "no adverse signal"
    return (
        f"{body}. Ladder {ladder}; enabled {cfg.enabled_modes}; "
        f"step-downs: {step}. Proposed {proposed} "
        f"(= {cfg.sheet_for(proposed)} sheet, keys "
        f"{[g.value for g in cfg.enabled_grades_for(proposed)]})."
    )


def propose(
    day: date,
    *,
    cfg: Optional[DayModeConfig] = None,
    prior_filled: int = 0,
    daily_stop_hit: bool = False,
    drc_note: Optional[str] = None,
    band: tuple[Any, Any] = (None, None),
) -> Optional[Proposal]:
    """Cobalt's 09:00 proposal for `day`, or None if `day` does not trade.

    A Sunday, a Saturday and a holiday get NO PROPOSAL AND NO ROW —
    there is no day to size. Returning None rather than raising is
    deliberate: the launchd job fires seven days a week and a weekend is
    not an error condition.
    """
    cfg = cfg or load_daymode_config()
    clock = session_clock()
    if not clock.calendar.is_trading_day(day):
        return None

    ceiling = cfg.highest_enabled
    signals: list[str] = []

    if daily_stop_hit:
        ceiling = cfg.lowest_enabled
        signals.append("daily stop hit on the prior trading day -> floor")
    if drc_note is None:
        ceiling = _step_down(cfg, ceiling)
        signals.append(f"{NO_PRIOR_DRC} -> one rung down")
    if clock.calendar.is_early_close(day):
        ceiling = _step_down(cfg, ceiling)
        signals.append("early close today -> one rung down")
    prior = prior_trading_day(day)
    if (day - prior).days > 1:
        ceiling = _step_down(cfg, ceiling)
        signals.append(f"first session after a {(day - prior).days - 1}-day close -> one rung down")
    band_min, band_max = band
    if band_min is None or band_max is None:
        ceiling = cfg.lowest_enabled
        signals.append("trade_count_band is PLACEHOLDER (unruled) -> floor")

    # max(floor, ceiling), then clamped into what is actually permitted.
    floor = cfg.lowest_enabled
    proposed = ceiling if cfg.rank(ceiling) > cfg.rank(floor) else floor
    if cfg.rank(proposed) > cfg.rank(cfg.highest_enabled):
        proposed = cfg.highest_enabled
        signals.append(f"clamped to the highest enabled mode ({cfg.highest_enabled})")
    if not cfg.is_enabled(proposed):
        # The ladder can point at a rung that exists but is not permitted
        # (a quarter sheet declared before it is turned on). Walk DOWN to
        # the nearest enabled rung — never up.
        proposed = max(
            (m for m in cfg.enabled_modes if cfg.rank(m) <= cfg.rank(proposed)),
            key=cfg.rank,
            default=floor,
        )
        signals.append(f"nearest enabled rung at or below -> {proposed}")

    return Proposal(
        trade_date=day,
        proposed=proposed,
        reason=build_reason(
            cfg, day,
            prior_day=prior, prior_filled=prior_filled, daily_stop_hit=daily_stop_hit,
            drc_note=drc_note, band=band, signals=signals, proposed=proposed,
        ),
        stage1_mode=cfg.lowest_enabled,
        signals=signals,
        prior_trading_day=prior,
        prior_filled=prior_filled,
        drc_note=drc_note,
    )


def decided_or_stage1(row: Optional[dict[str, Any]], cfg: Optional[DayModeConfig] = None) -> str:
    """The mode IN FORCE right now.

    "Until decided after 09:00, the sheet stays on the stage-1 mode."
    A proposal is not a decision — an unanswered 09:00 question leaves
    the floor in place, which is the safe direction.
    """
    cfg = cfg or load_daymode_config()
    if row and row.get("decided"):
        return str(row["decided"])
    return cfg.lowest_enabled


__all__ = [
    "BAND_MAX_KEY",
    "BAND_MIN_KEY",
    "NO_PRIOR_DRC",
    "Proposal",
    "build_reason",
    "decided_or_stage1",
    "prior_trading_day",
    "propose",
    "stage1_mode",
]
