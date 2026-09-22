"""Leg ROLES over `leg.legs()`'s output (TAXONOMY v0.7 §3.1; FINAL §3 D3,
[F-12]; setups one build STEP-4).

`leg.py` is unchanged, byte for byte (X16). Roles and termination are a
SEPARATE function over its legs plus the Range(micro) observation.

* `opening_drive` = the impulse leg starting at the RTH open: the first leg
  of the run (the evaluator hands in RTH bars from the session open). Its
  `direction` is that leg's.
* `terminated_by` — `A-07`, in Gemini's wording [F-12]: "When a micro-Range
  instantiates from the drive's extreme within a bounded retrace, the
  termination is consolidation." Built as:
    - the micro-Range instantiates FROM THE DRIVE'S EXTREME when its bound on
      the drive's side is the run's extreme so far (the top is the run's high
      for an up drive; the base its low for a down drive);
    - the retrace is the range's depth as a share of the drive
      (`(top − base) / (top − open)` up; `(top − base) / (open − base)` down);
    - within the bound `cfg(leg.consolidation_max_retrace)` → `consolidation`;
    - otherwise, when the first leg has ended (an opposing bar), `pullback`;
    - a drive still running (no opposing bar, no range) → no termination.
* `opening_drive_literal` is the taxonomy's literal reading, kept ONLY for
  X15 (the drive-then-range shape "under both readings"): the leg ends at the
  first opposing bar, so it is `consolidation` only when the micro-Range
  already includes that bar; else `pullback`.

Pure; a null key reads `leg.consolidation_max_retrace_unset` in the frame.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from decimal import Decimal, localcontext
from typing import Literal

from pydantic import BaseModel, ConfigDict

from cobalt.taxonomy.tunables import TunableRow

from .bars import WorkingBar
from .indicators import PRECISION
from .leg import LegObservation
from .micro_range import MicroRange

TUNABLE_KEYS = ("leg.consolidation_max_retrace",)


class OpeningDrive(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    direction: Literal["up", "down"] | None
    terminated_by: Literal["pullback", "consolidation"] | None
    reading: Literal["a07", "literal"]
    retrace: Decimal | None = None


def max_retrace(rows: Mapping[str, TunableRow]) -> Decimal | None:
    row = rows["leg.consolidation_max_retrace"]
    return None if row.value is None else Decimal(str(row.value))


def _from_extreme(run: Sequence[WorkingBar], direction: str, r: MicroRange) -> bool:
    upto = [b for b in run if b.ts < r.end_ts]
    return r.top == max(b.high for b in upto) if direction == "up" else r.base == min(b.low for b in upto)


def opening_drive(
    run: Sequence[WorkingBar], drive_legs: Sequence[LegObservation], micro: MicroRange | None, *,
    max_retrace: Decimal,
) -> OpeningDrive:
    if not drive_legs:
        return OpeningDrive(direction=None, terminated_by=None, reading="a07")
    first = drive_legs[0]
    direction = first.direction
    session_open = run[0].open
    if micro is not None and _from_extreme(run, direction, micro):
        with localcontext() as ctx:
            ctx.prec = PRECISION
            drive = micro.top - session_open if direction == "up" else session_open - micro.base
            retrace = (micro.top - micro.base) / drive if drive > 0 else None
        if retrace is not None and retrace <= max_retrace:
            return OpeningDrive(direction=direction, terminated_by="consolidation", reading="a07", retrace=retrace)
        if first.terminated:
            return OpeningDrive(direction=direction, terminated_by="pullback", reading="a07", retrace=retrace)
    if first.terminated:
        return OpeningDrive(direction=direction, terminated_by="pullback", reading="a07")
    return OpeningDrive(direction=direction, terminated_by=None, reading="a07")


def opening_drive_literal(
    run: Sequence[WorkingBar], drive_legs: Sequence[LegObservation], micro: MicroRange | None,
) -> OpeningDrive:
    if not drive_legs:
        return OpeningDrive(direction=None, terminated_by=None, reading="literal")
    first = drive_legs[0]
    if not first.terminated:
        return OpeningDrive(direction=first.direction, terminated_by=None, reading="literal")
    opposing_ts = drive_legs[1].start_ts
    inside = micro is not None and micro.start_ts <= opposing_ts
    return OpeningDrive(direction=first.direction, terminated_by="consolidation" if inside else "pullback",
                        reading="literal")


# ---------------------------------------------------------------------
# STEP-6 — pullback, impulse, pre_test (FINAL §3 D3; taxonomy §3.1)
# ---------------------------------------------------------------------
#
# In the frame's coordinates the long-side text's trade direction is `up`, so:
# * `Leg(pullback)` = the latest DOWN leg that is not the first leg (a pullback
#   terminates an impulse / the opening drive); `index` = its ordinal among the
#   pullbacks since the RTH open; `end` = its extreme (the low);
# * `Leg(impulse)` = the leg the pullback terminates (the one before it);
#   `Leg(opening_drive OR impulse)` = "the most recent leg of either role that
#   precedes the pullback" (FINAL §4) — that same leg, which is the opening
#   drive when the pullback is the second leg;
# * `Leg(pre_test)` (`A-14`, convention `leg.pre_test`): the run from the
#   session open to the pullback's first bar — the move before the test.
PRE_TEST_CONVENTION = "leg.pre_test"


class PullbackRoles(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    pullback: LegObservation | None
    index: int | None = None
    #: The leg the pullback terminates (impulse or opening drive).
    before: LegObservation | None = None
    before_role: Literal["opening_drive", "impulse"] | None = None


def pullback_roles(drive_legs: Sequence[LegObservation]) -> PullbackRoles:
    for k in range(len(drive_legs) - 1, 0, -1):
        if drive_legs[k].direction == "down":
            index = sum(1 for leg in drive_legs[1:k + 1] if leg.direction == "down")
            return PullbackRoles(pullback=drive_legs[k], index=index, before=drive_legs[k - 1],
                                 before_role="opening_drive" if k == 1 else "impulse")
    return PullbackRoles(pullback=None)


def pre_test_bars(run: Sequence[WorkingBar], roles: PullbackRoles) -> tuple[WorkingBar, ...]:
    """`Leg(pre_test)`: the run's bars before the pullback's first bar."""
    if roles.pullback is None:
        return ()
    return tuple(b for b in run if b.ts < roles.pullback.start_ts)


__all__ = [
    "OpeningDrive", "PRE_TEST_CONVENTION", "PullbackRoles", "TUNABLE_KEYS", "max_retrace", "opening_drive",
    "opening_drive_literal", "pre_test_bars", "pullback_roles",
]
