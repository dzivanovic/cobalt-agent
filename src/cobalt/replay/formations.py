"""F12 formations: the trade_defs that formed and were never taken
(S2-P4 STEP-5, R4 as amended by Astra R1-21).

    formation_misses(report, context=…, evaluator_version=…) -> FormationOutcome

BOUND TO S2-P2's SHIPPED CONTRACT, NOT TO A PLANNED ONE. The plan named
the entrypoint `cobalt.radar.evaluate`; what S2-P2 actually ships is

    cobalt.radar.evaluate_cli.replay_formations(day, *, pool_key,
        slug_filter, radar_store, defs_source, daily_source, tunables,
        defaults, clock, out) -> ReplayReport

with the capability marker `cobalt.radar.evaluate.EVALUATOR_VERSION`.
The code follows the shipped names; `replay/runner.py` imports BOTH
modules statically (one for the callable, one for the marker) and never
accepts two spellings of one name. This module holds no import of
`cobalt.radar` at all, so replay still loads when S2-P2 is absent.

WHAT A FORMATION ROW NEEDS, AND WHERE IT COMES FROM. Migration 0009's
`kind='formation'` CHECK needs `trade_def_md5`, `formation_at` and
`pool_member_id`, and the unique index adds `formation_at` +
`pool_member_id` to the subject so two same-day formations of one
(ticker, trade_def) never collapse into one row. S2-P2's
`ReplayFormation` carries all three (`trade_def_md5`, `formed_bar_ts`,
`membership_id`) plus `score_inputs_sha256`, the retained score
receipt's reference — every one of them a value `evaluate_member`
already computed inside the read-only replay. No schema changed, no
second seam, nothing is written on P2's side.

THE SCORE-RECEIPT REFERENCE is content-addressed, not a row id: P2's
`--replay` path reads no receipt row, so it can name the retained
receipt only by its natural key `(membership_id, trade_def_md5)` in
`system.radar_score` together with that row's own `inputs_sha256`
column. Both go in the miss row's receipt (L57).

THE GATE. One gate, ruled: an existing radar card for that (member,
def, direction) SUPPRESSES the miss — the card path (F12) already
replays that subject, and one event never becomes two rows (L3).
Otherwise the row's `excluded_by` is `no_card`. `rule_10` is recorded as
NOT APPLICABLE rather than silently passed: a formation has no card and
no position of its own, and no position-level exclusion was ruled for
formations.

THE HORIZON is the card path's, through the ONE public window resolver
with no card window to resolve (`resolve_window(None, …)`), so
`W = session close`. THE ARITHMETIC is `cards.counterfactual()` — the
same trigger, gap-through fill, stop-wins-on-tie walk and rounding a
card gets, never a second implementation.
"""

from __future__ import annotations

import json
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Callable, Optional

from cobalt.archiver.models import Bar, Interval
from cobalt.session.clock import ET

from .cards import MINUTE, bar_json, counterfactual, coverage, day_bars, resolve_window
from .models import (
    FORMULA_VERSION,
    FormationCandidate,
    FormationCounts,
    FormationOutcome,
    FormationReplay,
    MissRow,
    RadarCardRef,
    ReplayError,
    ReplayInputError,
    WindowResolution,
    canonical_json,
    sha256_json,
)

#: The S2-P2 capability markers this binding was written against. A value
#: outside this set is a loud refusal, never a silent degrade (R1-21).
SUPPORTED_EVALUATORS = frozenset({"s2p2.1"})

#: P2's shipped replay entrypoint, recorded in the receipt of every row.
P2_MODULE = "cobalt.radar.evaluate_cli"
P2_CALLABLE = "replay_formations"
P2_MODEL = "ReplayFormation"
P2_MARKER = "cobalt.radar.evaluate.EVALUATOR_VERSION"

#: The `ReplayFormation` fields a miss row cannot be built without.
FORMATION_REQUIRED_FIELDS = frozenset({
    "membership_id", "trade_def_md5", "score_inputs_sha256", "seen_at",
    "ticker", "slug", "direction", "trigger", "stop", "formed_bar_ts",
})

#: The one `excluded_by` a formation row carries (R1-21).
NO_CARD = "no_card"
GATE_ORDER = ("existing_card",)
RULE_10_NOT_APPLICABLE = (
    "not applicable: a formation has no card and no position of its own; R1-21 rules a formation's "
    "exclusion `no_card`"
)

#: The retained score receipt a formation's numbers came from.
SCORE_RECEIPT_TABLE = "system.radar_score"
SCORE_RECEIPT_COLUMN = "inputs_sha256"


@dataclass
class FormationSources:
    """Exactly the arguments S2-P2's `replay_formations` takes, minus the
    day, the slug filter and the output sink. Production passes the same
    stores the resident uses; a test passes its own."""

    pool_key: str
    radar_store: Any
    defs_source: Callable[[], tuple[list, dict]]
    daily_source: Callable[[str, date], Any]
    tunables: Any
    defaults: Any
    clock: Any


@dataclass
class FormationContext:
    """What replay needs to turn P2's formations into miss rows. Every
    field is a callable so that nothing is read when P2 is absent."""

    trade_date: date
    session_close: datetime
    bars_for: Callable[[str], list[Bar]]
    radar_cards: Callable[[], Sequence[RadarCardRef]]


# ---------------------------------------------------------------------------
# P2's formations -> replay's candidates
# ---------------------------------------------------------------------------


def formation_candidates(report: Any, *, evaluator_version: str) -> list[FormationCandidate]:
    """P2's `ReplayReport.formations`, in replay's vocabulary.

    `entry`/`stop` take the SAME mapping the live card path takes
    (`RadarCardSpec.entry = trigger_price`, `.stop = structural_stop`).
    """
    if evaluator_version not in SUPPORTED_EVALUATORS:
        raise ReplayError(
            f"S2-P2 evaluator version {evaluator_version!r} is not one this binding was written against "
            f"({sorted(SUPPORTED_EVALUATORS)}) — refusing rather than replaying an unknown contract"
        )
    out: list[FormationCandidate] = []
    for f in report.formations:
        missing = sorted(name for name in FORMATION_REQUIRED_FIELDS if not hasattr(f, name))
        if missing:
            raise ReplayError(f"S2-P2 formation is missing {missing} — {P2_MODULE}.{P2_MODEL} changed shape")
        out.append(FormationCandidate(
            membership_id=f.membership_id, ticker=f.ticker, slug=f.slug, trade_def_md5=f.trade_def_md5,
            direction=f.direction, entry=Decimal(f.trigger), stop=Decimal(f.stop),
            formed_at=f.formed_bar_ts, seen_at=f.seen_at, score_inputs_sha256=f.score_inputs_sha256,
            evaluator_version=evaluator_version,
        ))
    return out


# ---------------------------------------------------------------------------
# One formation
# ---------------------------------------------------------------------------


def _suppressor(candidate: FormationCandidate, cards: Sequence[RadarCardRef]) -> Optional[RadarCardRef]:
    return next(
        (c for c in cards
         if (c.pool_member_id, c.trade_def_slug, c.direction) == candidate.subject_key()),
        None,
    )


def replay_formation(
    candidate: FormationCandidate,
    bars: Sequence[Bar],
    *,
    trade_date: date,
    window: WindowResolution,
    session_close: datetime,
    radar_cards: Sequence[RadarCardRef],
) -> FormationReplay:
    """Replay one formation. PURE — see the module docstring for the rules."""
    if candidate.formed_at.astimezone(ET).date() != trade_date:
        raise ReplayInputError(
            f"formation {candidate.ticker} {candidate.slug} formed {candidate.formed_at.isoformat()}, "
            f"which is not trade date {trade_date.isoformat()}"
        )

    def done(status: str, reason: str, miss: Optional[MissRow] = None) -> FormationReplay:
        return FormationReplay(membership_id=candidate.membership_id, ticker=candidate.ticker,
                               status=status, reason=reason, miss=miss)

    card = _suppressor(candidate, radar_cards)
    if card is not None:
        return done("suppressed", f"radar card {card.card_id} already covers "
                                  f"{candidate.subject_key()} — the card path owns this subject")

    todays = day_bars(bars, trade_date)
    cov = coverage(todays, start=candidate.seen_at, end=session_close)
    if not cov["covered"]:
        return done("input_stale", f"input_stale: {cov['reason']}")

    outcome = counterfactual(
        todays, subject=f"formation {candidate.ticker} {candidate.slug} @ {candidate.formed_at.isoformat()}",
        direction=candidate.direction, entry=candidate.entry, stop_at=lambda _at: candidate.stop,
        start_at=candidate.seen_at, window_end=window.resolved_end, session_close=session_close,
    )
    if outcome.status != "ok":
        return done(outcome.status, outcome.reason)
    walk = outcome.walk

    considered = sorted(c.card_id for c in radar_cards if c.pool_member_id == candidate.membership_id)
    gate_detail: dict[str, Any] = {
        "order": list(GATE_ORDER),
        "existing_card": {
            "fired": False, "matched": None,
            "key": {"pool_member_id": candidate.membership_id, "trade_def_slug": candidate.slug,
                    "direction": candidate.direction},
            "cards_considered": considered,
        },
        "window": {"fired": False, "window_end": walk.window_end.isoformat(),
                   "trigger_ts": walk.trigger.ts.isoformat(), "source": window.source,
                   "detail": window.detail},
        "rule_10": {"applies": False, "reason": RULE_10_NOT_APPLICABLE},
        "trade_count_band": "unset",
    }

    before_start = [b for b in todays if b.ts <= candidate.seen_at][-1:]
    after_end = [b for b in todays if b.ts + MINUTE >= session_close][:1]
    consumed = sorted({b.ts: b for b in (*before_start, *walk.searched, *after_end)}.values(), key=lambda b: b.ts)
    inputs = {
        "formula_version": FORMULA_VERSION,
        "trade_date": trade_date.isoformat(),
        "formation": {
            "membership_id": candidate.membership_id, "ticker": candidate.ticker, "slug": candidate.slug,
            "trade_def_md5": candidate.trade_def_md5, "direction": candidate.direction,
            "entry": str(candidate.entry), "stop": str(candidate.stop),
            "formed_at": candidate.formed_at.isoformat(), "seen_at": candidate.seen_at.isoformat(),
        },
        "p2_contract": {
            "evaluator_version": candidate.evaluator_version, "module": P2_MODULE, "callable": P2_CALLABLE,
            "model": P2_MODEL, "marker": P2_MARKER, "required_fields": sorted(FORMATION_REQUIRED_FIELDS),
        },
        "score_receipt": {
            "table": SCORE_RECEIPT_TABLE, "column": SCORE_RECEIPT_COLUMN,
            "key": {"membership_id": candidate.membership_id, "trade_def_md5": candidate.trade_def_md5},
            "inputs_sha256": candidate.score_inputs_sha256,
            "note": "content-addressed: P2's read-only replay reads no receipt row and reports no score id",
        },
        "window": {"resolved_end": window.resolved_end.isoformat(), "source": window.source,
                   "detail": window.detail},
        "session_close": session_close.isoformat(),
        "radar_cards": [
            {"card_id": c.card_id, "pool_member_id": c.pool_member_id, "trade_def_slug": c.trade_def_slug,
             "direction": c.direction, "state": c.state,
             "created_at": c.created_at.isoformat() if c.created_at else None}
            for c in sorted(radar_cards, key=lambda c: c.card_id)
        ],
        "eligibility": "bar_start + 1 minute <= horizon",
        "bars": [bar_json(b) for b in consumed],
    }
    outputs = {
        "coverage": coverage(consumed, start=candidate.seen_at, end=session_close),
        "trigger_bar": bar_json(walk.trigger), "stop": str(walk.stop),
        "window_end": walk.window_end.isoformat(), "horizon_end": walk.horizon_end.isoformat(),
        "eligible_bar_ts": [b.ts.isoformat() for b in walk.eligible],
        "walked_bar_ts": [b.ts.isoformat() for b in walk.walked],
        "fill_price": str(walk.fill_price), "exit_ts": walk.exit_bar.ts.isoformat(),
        "exit_price": str(walk.exit_price), "exit_reason": walk.exit_reason,
        "cf_r": str(walk.cf_r), "mfe_r": str(walk.mfe_r),
        "excluded_by": NO_CARD, "gate_detail": gate_detail,
    }
    miss = MissRow(
        trade_date=trade_date, kind="formation", ticker=candidate.ticker, direction=candidate.direction,
        trade_def_md5=candidate.trade_def_md5, formation_at=candidate.formed_at,
        pool_member_id=candidate.membership_id, excluded_by=NO_CARD, gate_detail=gate_detail,
        entry=candidate.entry, stop=walk.stop, trigger_ts=walk.trigger.ts, fill_price=walk.fill_price,
        horizon_end=walk.horizon_end, exit_ts=walk.exit_bar.ts, exit_price=walk.exit_price,
        exit_reason=walk.exit_reason, cf_r=walk.cf_r, mfe_r=walk.mfe_r, bars_watermark=consumed[-1].ts,
        formula_version=FORMULA_VERSION, receipt=json.loads(canonical_json({"inputs": inputs, "outputs": outputs})),
        inputs_sha256=sha256_json(inputs),
    )
    return done("miss", f"excluded_by {NO_CARD}", miss)


def replay_formation_from_receipt(receipt: dict[str, Any]) -> FormationReplay:
    """Recompute a stored formation miss from its receipt's inputs ONLY (L57)."""
    inputs = receipt["inputs"]
    if inputs.get("formula_version") != FORMULA_VERSION:
        raise ReplayInputError(f"receipt formula {inputs.get('formula_version')!r} is not {FORMULA_VERSION!r}")
    f, contract, reference = inputs["formation"], inputs["p2_contract"], inputs["score_receipt"]
    candidate = FormationCandidate(
        membership_id=f["membership_id"], ticker=f["ticker"], slug=f["slug"],
        trade_def_md5=f["trade_def_md5"], direction=f["direction"], entry=Decimal(f["entry"]),
        stop=Decimal(f["stop"]), formed_at=datetime.fromisoformat(f["formed_at"]),
        seen_at=datetime.fromisoformat(f["seen_at"]), score_inputs_sha256=reference["inputs_sha256"],
        evaluator_version=contract["evaluator_version"],
    )
    bars = [
        Bar(ticker=candidate.ticker, interval=Interval.I1, ts=b["ts"], open=Decimal(b["open"]),
            high=Decimal(b["high"]), low=Decimal(b["low"]), close=Decimal(b["close"]), volume=int(b["volume"]))
        for b in inputs["bars"]
    ]
    return replay_formation(
        candidate, bars, trade_date=date.fromisoformat(inputs["trade_date"]),
        window=WindowResolution(**inputs["window"]),
        session_close=datetime.fromisoformat(inputs["session_close"]),
        radar_cards=[RadarCardRef(**row) for row in inputs["radar_cards"]],
    )


# ---------------------------------------------------------------------------
# The day
# ---------------------------------------------------------------------------


def formation_misses(report: Any, *, context: FormationContext, evaluator_version: str) -> FormationOutcome:
    """Every formation of the day, as rows and counts. Reads only."""
    candidates = formation_candidates(report, evaluator_version=evaluator_version)
    cards = list(context.radar_cards())
    window = resolve_window(None, context.trade_date)
    rows: list[MissRow] = []
    tally = {"suppressed": 0, "no_trigger": 0, "input_stale": 0}
    for candidate in candidates:
        replayed = replay_formation(
            candidate, context.bars_for(candidate.ticker), trade_date=context.trade_date,
            window=window, session_close=context.session_close, radar_cards=cards,
        )
        if replayed.status == "miss":
            rows.append(replayed.miss)
        else:
            tally[replayed.status] += 1
    subjects = [row.subject() for row in rows]
    if len(set(subjects)) != len(subjects):
        raise ReplayInputError(
            "two formation rows share one subject — the extended key (member, formation_at) did not separate them"
        )
    return FormationOutcome(
        status=evaluator_version, rows=tuple(rows),
        counts=FormationCounts(candidates=len(candidates), misses=len(rows), **tally),
    )


__all__ = [
    "FORMATION_REQUIRED_FIELDS", "GATE_ORDER", "NO_CARD", "P2_CALLABLE", "P2_MARKER", "P2_MODEL",
    "P2_MODULE", "SCORE_RECEIPT_COLUMN", "SCORE_RECEIPT_TABLE", "SUPPORTED_EVALUATORS",
    "FormationContext", "FormationSources", "formation_candidates", "formation_misses",
    "replay_formation", "replay_formation_from_receipt",
]
