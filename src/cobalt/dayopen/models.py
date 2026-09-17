"""The shapes `cobalt day-open` renders: one `CheckResult` per check (C1-C6),
rolled up into one `Overall`. L57 (explainability): every derived value
ships with its stored inputs, so `overall_verdict` is a pure function
over the six results, not a judgement made while rendering.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date as Date
from datetime import datetime
from enum import Enum
from typing import Protocol, Sequence


class Verdict(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    #: A named, ruled condition (e.g. "no fill yet") — reported, never a
    #: failure. Day-open's six checks do not emit it; `cobalt smoke` does
    #: (S2-P4 STEP-9) and shares this roll-up rather than owning a second.
    KNOWN = "KNOWN"
    ERROR = "ERROR"


class Overall(str, Enum):
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"


@dataclass(frozen=True)
class CheckResult:
    """One check's outcome. `raw` is the verbatim captured output this
    check's verdict was quoted from — never composed, per the RULING's
    "each capturing raw output verbatim" (L57)."""

    id: str
    title: str
    verdict: Verdict
    detail: str
    raw: str


class HasVerdict(Protocol):
    verdict: Verdict


def overall_verdict(results: Sequence[HasVerdict]) -> Overall:
    """RULED (this build, 2026-09-14): ERROR outranks FAIL.

    A check whose own command or query failed (no data collected) is a
    broken probe; a check that ran and found a number outside EXPECT is
    a real finding about the morning, not about day-open itself. Written
    down here rather than left to be inferred at render time, so the
    OVERALL line is replayable from this rule alone (L57):

        RED   — any check is ERROR
        AMBER — no ERROR, but any check is FAIL
        GREEN — every check is PASS or KNOWN (KNOWN never lowers it,
                plan-s2-p4 §1 F17)

    An EMPTY list raises: a sweep that checked nothing is not GREEN (L1).
    """
    if not results:
        raise ValueError("overall_verdict: no check results — nothing was checked")
    if any(r.verdict is Verdict.ERROR for r in results):
        return Overall.RED
    if any(r.verdict is Verdict.FAIL for r in results):
        return Overall.AMBER
    return Overall.GREEN


@dataclass(frozen=True)
class DayOpenReport:
    report_date: Date
    generated_at: datetime
    checks: list[CheckResult]
    overall: Overall


__all__ = ["CheckResult", "DayOpenReport", "Overall", "Verdict", "overall_verdict"]
