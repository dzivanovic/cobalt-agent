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

THE PROPOSAL RULE, and where it now lives. `propose()` starts at the
highest permitted rung and STEPS DOWN once per adverse signal, then
clamps into `enabled_modes`:

    proposed = clamp( max(lowest_enabled, ceiling_after_step_downs) )

MOVED OUT OF CODE (CTO review of S1-P2, 2026-09-04). The step-down rules
used to be an `if` ladder right here, so "what makes today a smaller day"
was a Python edit. Cobalt is a product for many traders and their rules
will differ, so the SET is now `daymode.stepdowns` in
`configs/cobalt/daymode.yaml` and this module WALKS it.

The split is deliberate and it is the only one that works:

* **The facts are code.** Whether the daily stop was hit, whether the
  prior DRC is informative, whether today is an early close, how long the
  close before it was, whether the band is ruled — every one of those is
  a query against the calendar, the card rows or a note. They cannot come
  from a YAML file; they are computed in `_facts()` below and each one is
  named by a `SIGNAL_IDS` id.
* **The effects are config.** What a fired fact COSTS (floor / N rungs
  down / nothing) and the words it contributes to the sentence he reads
  are the table's, row by row.

Every step-down still names itself in the reason string, so the sentence
stays a derivation and not a summary, and the rule set is still marked
PROVISIONAL in that sentence — it belongs to the Rules Engine session.
Moving it into config is what makes that session a config edit.
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
from datetime import date, datetime, time, timedelta
from typing import Any, Optional

from cobalt.session import session_clock
from cobalt.session import clock as clock_mod

from .config import (
    EFFECT_DOWN,
    EFFECT_FLOOR,
    EFFECT_NONE,
    SIGNAL_IDS,
    DayModeConfig,
    load_daymode_config,
)

#: The tunables rows F6 consumes. PLACEHOLDER values pending the Rules
#: Engine session — `validate` checks they EXIST; nothing pretends to
#: know what they should be.
BAND_MIN_KEY = "daymode.trade_count_band.min"
BAND_MAX_KEY = "daymode.trade_count_band.max"

#: The ET wall-clock boundary between stage 1 and stage 2. F16: "is it
#: stage 2 yet" is a predicate, so its threshold is a tunables row and
#: not a literal — read HERE, by `decided_or_stage1`, which is what
#: makes the row's named consumer true rather than aspirational. The
#: launchd schedule mirrors the same number, because launchd cannot read
#: a tunables row; `cobalt validate` prints it so a drift is visible.
STAGE2_OPEN_KEY = "daymode.stage2_open"

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


def stage2_open() -> time:
    """The ET time stage 2 begins, from tunables. No built-in default."""
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(STAGE2_OPEN_KEY)
    if row is None:
        raise RuntimeError(
            f"tunable {STAGE2_OPEN_KEY!r} is missing from tunables.yaml — F6 reads "
            "the stage boundary from config and has no built-in default (F16)."
        )
    hour, _, minute = str(row.value).partition(":")
    return time(int(hour), int(minute))


def stage1_mode(cfg: Optional[DayModeConfig] = None) -> str:
    """The pre-09:00 mode. A system rule, asking nothing."""
    return (cfg or load_daymode_config()).lowest_enabled


def _step_down(cfg: DayModeConfig, mode: str, rungs: int = 1) -> str:
    rank = cfg.rank(mode)
    return cfg.modes[max(0, rank - rungs)]


def _facts(
    cfg: DayModeConfig,
    day: date,
    *,
    daily_stop_hit: bool,
    drc_note: Optional[str],
    drc_informative: bool,
    prior_day: date,
    band: tuple[Any, Any],
) -> dict[str, bool]:
    """The FACTS, one per `SIGNAL_IDS` id. Code, because every one of
    them is a query — against the NYSE calendar, the prior day's cards,
    or the DRC note. The table decides what they COST."""
    clock = session_clock()
    band_min, band_max = band
    facts = {
        "daily_stop_hit": bool(daily_stop_hit),
        # "you did not write one" and "you wrote one and left it blank"
        # are different facts about his day, so they are two signals that
        # the table may price differently. They are mutually exclusive.
        "no_prior_drc": drc_note is None,
        "drc_not_informative": drc_note is not None and not drc_informative,
        "early_close_today": clock.calendar.is_early_close(day),
        "first_session_after_close": (day - prior_day).days > 1,
        "trade_count_band_placeholder": band_min is None or band_max is None,
    }
    missing = [s for s in SIGNAL_IDS if s not in facts]
    if missing:  # pragma: no cover - guarded by test_every_signal_has_a_fact
        raise RuntimeError(
            f"signal(s) {missing} are declared in SIGNAL_IDS and ruled in "
            "configs/cobalt/daymode.yaml but this module computes no fact for "
            "them — a rule that can never fire."
        )
    return facts


def apply_stepdowns(
    cfg: DayModeConfig, facts: dict[str, bool], *, day: date
) -> tuple[str, list[str]]:
    """Walk the config table over the facts. Returns (ceiling, clauses).

    Rows are applied IN CONFIG ORDER, which is what makes the table
    readable as a policy: a `floor` row later in the table overrides an
    earlier `down`, exactly as it reads. `effect: none` fires nothing and
    says so, so a rule ruled off is visible in the sentence rather than
    absent from it.
    """
    ceiling = cfg.highest_enabled
    clauses: list[str] = []
    for row in cfg.stepdowns:
        if not facts.get(row.signal):
            continue
        if row.effect == EFFECT_FLOOR:
            ceiling = cfg.lowest_enabled
        elif row.effect == EFFECT_DOWN:
            ceiling = _step_down(cfg, ceiling, row.rungs)
        elif row.effect == EFFECT_NONE:
            pass
        clauses.append(row.describe(ceiling))
    return ceiling, clauses


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
    drc_informative: Optional[bool] = None,
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

    if drc_informative is None:
        drc_informative = drc_note is not None
    prior = prior_trading_day(day)
    facts = _facts(
        cfg, day,
        daily_stop_hit=daily_stop_hit, drc_note=drc_note,
        drc_informative=drc_informative, prior_day=prior, band=band,
    )
    ceiling, signals = apply_stepdowns(cfg, facts, day=day)

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


def decided_or_stage1(
    row: Optional[dict[str, Any]],
    cfg: Optional[DayModeConfig] = None,
    now: Optional[datetime] = None,
) -> str:
    """The mode IN FORCE at `now`.

    Two ways to land on the stage-1 floor, and they are different:

    * **It is not stage 2 yet.** Before `daymode.stage2_open` (09:00 ET)
      the floor holds no matter what the row says. A decision cannot
      apply retroactively to the premarket in which no stop can rest —
      that is the system rule, not a preference, so it is not something a
      later decision reaches back and overrides.
    * **Stage 2, but unanswered.** A proposal is not a decision. An
      unanswered 09:00 question leaves the floor in place, which is the
      safe direction.
    """
    cfg = cfg or load_daymode_config()
    et = session_clock().to_et(now or clock_mod.now_utc())
    if et.time() < stage2_open():
        return cfg.lowest_enabled
    if row and row.get("decided"):
        return str(row["decided"])
    return cfg.lowest_enabled


__all__ = [
    "BAND_MAX_KEY",
    "apply_stepdowns",
    "BAND_MIN_KEY",
    "NO_PRIOR_DRC",
    "Proposal",
    "build_reason",
    "decided_or_stage1",
    "STAGE2_OPEN_KEY",
    "prior_trading_day",
    "propose",
    "stage1_mode",
    "stage2_open",
]
