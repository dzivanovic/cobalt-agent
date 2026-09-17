"""F12: replay the day's unfilled cards over i1 bars — counterfactual R
and the gate that excluded each miss (S2-P4 STEP-5, R4 as amended).

    replay_card(card, bars, trade_date=, window=, session_close=, positions=)

PURE. Bars, transitions, stop edits and positions come in as values; one
typed `CardReplay` comes out. Nothing here reads a clock, a database or
a config file, which is what lets `replay_from_receipt` recompute every
stored number from the receipt alone (L57).

THE ONE FORMULA (R4, R1-9):

* Trigger = the first i1 bar starting at or after `created_at` whose
  high >= entry (long) / low <= entry (short). `fill_price` = the planned
  entry, or the bar's OPEN when that bar opened beyond it (gap-through).
* Exit = the first eligible bar that touches the stop (low <= stop long /
  high >= stop short) — on the trigger bar itself a touch counts, so a
  same-bar tie goes to the stop — at the stop; otherwise the close of the
  last eligible bar, `exit_reason = horizon_end`.
* cf_r = (exit − fill_price) / |planned_entry − stop| × (+1 long, −1 short),
  rounded half-up to 4 dp once. A gapped long 100/99 filled at 102 and
  stopped is −3R, not −1R: the numerator is the actual fill, the
  denominator the planned risk.
* mfe_r = the best favourable excursion from `fill_price` up to and
  including the exit bar, same units. A BAR-LEVEL OBSERVATION, never a
  second R: within one OHLC bar the order of high and low is unknowable.

THE HORIZON (R1-10, R2-4, R3-2). `W = min(resolved window end, actual
session close)`. `H = W` when `trigger_ts <= W`, else `H = session close`.
i1 bars are stamped at bar START, so a bar is eligible only when its whole
minute has elapsed by the cutoff: `bar_start + 1 minute <= H`. A trigger
that leaves no eligible completed bar writes no row (`input_stale`).

THE GATES (R4, R1-11), first match in this fixed order:

1. `rule_10` — the two-open-position PROXY for rule 10: >= 2 OTHER cards
   FILLED and not CLOSED at `trigger_ts`. The rule's stop-at-card-level
   exemption is not computed and is recorded `unavailable`, never passed.
2. `window` — `trigger_ts > W`.
3. the card's state at `trigger_ts`, from `card_transitions` ordered by
   `(at, id)`: WATCH/MISSED -> `unarmed`, PASSED -> `passed`,
   ARMED/TRIGGERED -> `not_filled`, EXPIRED -> `window`. FILLED/CLOSED
   cannot occur for a candidate and refuse loud.

`trade_count_band` is recorded `unset` while its tunables are null (plan
§8 item 2) and is never an `excluded_by` value.

COVERAGE (R1-12). "Some bars that day" is not evidence. The day's bars
must reach back to the card's creation (a bar at or before `created_at`)
and forward to the close (a bar whose minute ends at or after it);
otherwise the card is `input_stale` — counted, surfaced, never a fake R.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Sequence
from datetime import date, datetime, timedelta
from decimal import ROUND_HALF_UP, Decimal
from typing import Any, Callable, Optional

from cobalt import db, env
from cobalt.archiver.models import Bar, Interval
from cobalt.db import Side
from cobalt.session.clock import ET

from .models import (
    FORMULA_VERSION,
    CardCandidate,
    CardReplay,
    MissKind,
    MissRow,
    PositionSpan,
    ReconcileCounts,
    ReplayInputError,
    StopEdit,
    TransitionRow,
    WindowResolution,
    canonical_json,
    sha256_json,
)

MINUTE = timedelta(minutes=1)
FOUR_DP = Decimal("0.0001")

#: The fixed gate order (R4). Rendered into every `gate_detail`.
GATE_ORDER = ("rule_10", "window", "state")

#: As-of-trigger state -> `excluded_by`. Exhaustive over `CardState`
#: (asserted in the tests): a state missing here is a refusal, not a pass.
STATE_GATE: dict[str, Optional[str]] = {
    "WATCH": "unarmed",
    "MISSED": "unarmed",
    "PASSED": "passed",
    "ARMED": "not_filled",
    "TRIGGERED": "not_filled",
    "EXPIRED": "window",
    "FILLED": None,
    "CLOSED": None,
}

RULE_10_PROXY = "two_open_positions"


def _round(value: Decimal) -> Decimal:
    return value.quantize(FOUR_DP, rounding=ROUND_HALF_UP)


def _iso(value: Optional[datetime]) -> Optional[str]:
    return value.isoformat() if value is not None else None


def _bar_json(bar: Bar) -> dict[str, str]:
    return {
        "ts": bar.ts.isoformat(), "open": str(bar.open), "high": str(bar.high),
        "low": str(bar.low), "close": str(bar.close), "volume": str(bar.volume),
    }


# ---------------------------------------------------------------------------
# Pure pieces
# ---------------------------------------------------------------------------


def day_bars(bars: Iterable[Bar], trade_date: date) -> list[Bar]:
    """The bars whose ET date is `trade_date`, sorted; a duplicate
    timestamp is a corrupt input and refuses."""
    out = sorted((b for b in bars if b.ts.astimezone(ET).date() == trade_date), key=lambda b: b.ts)
    for a, b in zip(out, out[1:]):
        if a.ts == b.ts:
            raise ReplayInputError(f"{b.ticker}: duplicate i1 bar at {b.ts.isoformat()}")
    return out


def coverage(bars: Sequence[Bar], *, start: datetime, end: datetime) -> dict[str, Any]:
    """Do `bars` (one ticker, one day, sorted) span [start, end]?

    Covered = a bar starting at or before `start` AND a bar whose minute
    ends at or after `end`. Interior gaps are recorded, not gated: a
    minute with no trade has no i1 bar, and that is not missing data.
    """
    if not bars:
        return {"covered": False, "reason": "no i1 bars for the trade date", "count": 0}
    first, last = bars[0].ts, bars[-1].ts
    gaps = [int((b.ts - a.ts) / MINUTE) for a, b in zip(bars, bars[1:])]
    detail = {
        "count": len(bars), "first": first.isoformat(), "last": last.isoformat(),
        "max_gap_min": max(gaps, default=0), "start": start.isoformat(), "end": end.isoformat(),
    }
    if first > start:
        return {"covered": False, "reason": f"bars begin {first.isoformat()}, after {start.isoformat()}", **detail}
    if last + MINUTE < end:
        return {"covered": False, "reason": f"bars end {last.isoformat()}, before {end.isoformat()}", **detail}
    return {"covered": True, "reason": "covered", **detail}


def ordered_transitions(transitions: Iterable[TransitionRow]) -> list[TransitionRow]:
    return sorted(transitions, key=lambda t: (t.at, t.id if t.id is not None else -1))


def state_at(transitions: Sequence[TransitionRow], instant: datetime) -> TransitionRow:
    """The transition in force at `instant`, `(at, id)` order.

    Two rows at the same instant with no id cannot be ordered, and the
    state they leave behind is then a guess — refused, not guessed.
    """
    ordered = ordered_transitions(transitions)
    upto = [t for t in ordered if t.at <= instant]
    if not upto:
        raise ReplayInputError(
            f"card {transitions[0].card_id if transitions else '?'}: no transition at or before "
            f"{instant.isoformat()} — a card has a state from its genesis row on"
        )
    last = upto[-1]
    tied = [t for t in upto if t.at == last.at]
    if len(tied) > 1 and any(t.id is None for t in tied):
        raise ReplayInputError(
            f"card {last.card_id}: {len(tied)} transitions share {last.at.isoformat()} and "
            "carry no id — their order, and so the state at the trigger, is unknowable"
        )
    return last


def stop_as_of(card: CardCandidate, instant: datetime) -> tuple[Decimal, list[dict[str, str]]]:
    """The stop in force at `instant`: the card's current stop, walked back
    through every edit made after `instant` (R1-11: never the current
    mutable value when it has since moved)."""
    later = sorted((e for e in card.stop_edits if e.at > instant), key=lambda e: (e.at, e.id or 0))
    stop = later[0].from_stop if later else card.stop
    return stop, [
        {"at": e.at.isoformat(), "from_stop": str(e.from_stop), "to_stop": str(e.to_stop)}
        for e in sorted(card.stop_edits, key=lambda e: (e.at, e.id or 0))
    ]


def _touches_entry(bar: Bar, direction: str, entry: Decimal) -> bool:
    return bar.high >= entry if direction == "long" else bar.low <= entry


def _touches_stop(bar: Bar, direction: str, stop: Decimal) -> bool:
    return bar.low <= stop if direction == "long" else bar.high >= stop


def _favourable(bar: Bar, direction: str, fill: Decimal) -> Decimal:
    return bar.high - fill if direction == "long" else fill - bar.low


# ---------------------------------------------------------------------------
# The replay
# ---------------------------------------------------------------------------


def replay_card(
    card: CardCandidate,
    bars: Iterable[Bar],
    *,
    trade_date: date,
    window: WindowResolution,
    session_close: datetime,
    positions: Sequence[PositionSpan],
) -> CardReplay:
    """Replay one candidate. See the module docstring for every rule."""
    if not card.transitions:
        raise ReplayInputError(f"card {card.id}: no transitions — no card exists without a state")
    todays = day_bars(bars, trade_date)
    cov = coverage(todays, start=card.created_at, end=session_close)

    def stale(reason: str) -> CardReplay:
        return CardReplay(card_id=card.id, ticker=card.ticker, status="input_stale", reason=reason)

    if not cov["covered"]:
        return stale(f"input_stale: {cov['reason']}")

    search = [b for b in todays if b.ts >= card.created_at and b.ts + MINUTE <= session_close]
    trigger = next((b for b in search if _touches_entry(b, card.direction, card.entry)), None)
    if trigger is None:
        return CardReplay(card_id=card.id, ticker=card.ticker, status="no_trigger",
                          reason="entry never traded through before the close")

    trigger_ts = trigger.ts
    w_end = min(window.resolved_end, session_close)
    horizon = w_end if trigger_ts <= w_end else session_close
    eligible = [b for b in search if b.ts >= trigger_ts and b.ts + MINUTE <= horizon]
    if not eligible:
        return stale(
            f"input_stale: trigger bar {trigger_ts.isoformat()} leaves no completed bar by "
            f"horizon {horizon.isoformat()}"
        )

    stop, edits = stop_as_of(card, trigger_ts)
    risk = abs(card.entry - stop)
    if risk == 0:
        raise ReplayInputError(f"card {card.id}: entry equals stop ({card.entry}) — no R unit")
    if (card.direction == "long" and stop > card.entry) or (card.direction == "short" and stop < card.entry):
        raise ReplayInputError(
            f"card {card.id}: {card.direction} stop {stop} is on the wrong side of entry {card.entry}"
        )

    if card.direction == "long":
        fill = trigger.open if trigger.open > card.entry else card.entry
    else:
        fill = trigger.open if trigger.open < card.entry else card.entry

    exit_bar, exit_price, exit_reason = eligible[-1], eligible[-1].close, "horizon_end"
    best = Decimal(0)
    walked: list[Bar] = []
    for bar in eligible:
        walked.append(bar)
        best = max(best, _favourable(bar, card.direction, fill))
        if _touches_stop(bar, card.direction, stop):
            exit_bar, exit_price, exit_reason = bar, stop, "stop"
            break
    sign = Decimal(1) if card.direction == "long" else Decimal(-1)
    cf_r = _round((exit_price - fill) / risk * sign)
    mfe_r = _round(best / risk)

    # -- gates, fixed order ------------------------------------------------
    open_others = sorted(p.card_id for p in positions if p.card_id != card.id and p.open_at(trigger_ts))
    rule_10 = len(open_others) >= 2
    window_fired = trigger_ts > w_end
    in_force = state_at(card.transitions, trigger_ts)
    if in_force.to_state not in STATE_GATE:
        raise ReplayInputError(f"card {card.id}: unknown state {in_force.to_state!r} at the trigger")
    state_gate = STATE_GATE[in_force.to_state]
    if state_gate is None:
        raise ReplayInputError(
            f"card {card.id}: state {in_force.to_state} at the trigger — a candidate never reached FILLED"
        )
    excluded_by = "rule_10" if rule_10 else ("window" if window_fired else state_gate)
    gate_detail = {
        "order": list(GATE_ORDER),
        "rule_10": {
            "proxy": RULE_10_PROXY, "fired": rule_10, "open_card_ids": open_others,
            "uncomputed": {"stop_at_card_level_exemption": "unavailable"},
        },
        "window": {"fired": window_fired, "window_end": w_end.isoformat(),
                   "trigger_ts": trigger_ts.isoformat()},
        "state": {"state": in_force.to_state, "transition_id": in_force.id,
                  "at": in_force.at.isoformat(), "maps_to": state_gate},
        "trade_count_band": "unset",
    }

    # -- receipt ---------------------------------------------------------------
    # The consumed set: the bar that proves the start is covered, every
    # searched bar, and the bar that proves the close is covered — exactly
    # what `replay_from_receipt` needs to reach the same answer.
    before_start = [b for b in todays if b.ts <= card.created_at][-1:]
    after_end = [b for b in todays if b.ts + MINUTE >= session_close][:1]
    consumed = sorted({b.ts: b for b in (*before_start, *search, *after_end)}.values(), key=lambda b: b.ts)
    inputs = {
        "formula_version": FORMULA_VERSION,
        "trade_date": trade_date.isoformat(),
        "card": {
            "id": card.id, "ticker": card.ticker, "direction": card.direction,
            "entry": str(card.entry), "stop_current": str(card.stop),
            "created_at": card.created_at.isoformat(), "window_ref": card.window_ref,
        },
        "stop_edits": edits,
        "transitions": [
            {"id": t.id, "card_id": t.card_id, "from_state": t.from_state,
             "to_state": t.to_state, "at": t.at.isoformat()}
            for t in ordered_transitions(card.transitions)
        ],
        "window": {"resolved_end": window.resolved_end.isoformat(), "source": window.source,
                   "detail": window.detail},
        "session_close": session_close.isoformat(),
        "positions": [
            {"card_id": p.card_id, "filled_at": p.filled_at.isoformat(), "closed_at": _iso(p.closed_at)}
            for p in sorted(positions, key=lambda p: (p.filled_at, p.card_id))
        ],
        "eligibility": "bar_start + 1 minute <= horizon",
        "bars": [_bar_json(b) for b in consumed],
    }
    outputs = {
        "coverage": coverage(consumed, start=card.created_at, end=session_close),
        "trigger_bar": _bar_json(trigger), "stop_as_of_trigger": str(stop),
        "window_end": w_end.isoformat(), "horizon_end": horizon.isoformat(),
        "eligible_bar_ts": [b.ts.isoformat() for b in eligible],
        "walked_bar_ts": [b.ts.isoformat() for b in walked],
        "fill_price": str(fill), "exit_ts": exit_bar.ts.isoformat(), "exit_price": str(exit_price),
        "exit_reason": exit_reason, "cf_r": str(cf_r), "mfe_r": str(mfe_r),
        "excluded_by": excluded_by, "gate_detail": gate_detail,
    }
    receipt = {"inputs": inputs, "outputs": outputs}
    miss = MissRow(
        trade_date=trade_date, kind="card", ticker=card.ticker, direction=card.direction,
        card_id=card.id, excluded_by=excluded_by, gate_detail=gate_detail,
        entry=card.entry, stop=stop, trigger_ts=trigger_ts, fill_price=fill,
        horizon_end=horizon, exit_ts=exit_bar.ts, exit_price=exit_price, exit_reason=exit_reason,
        cf_r=cf_r, mfe_r=mfe_r, bars_watermark=consumed[-1].ts, formula_version=FORMULA_VERSION,
        receipt=json.loads(canonical_json(receipt)), inputs_sha256=sha256_json(inputs),
    )
    return CardReplay(card_id=card.id, ticker=card.ticker, status="miss",
                      reason=f"excluded_by {excluded_by}", miss=miss)


def replay_from_receipt(receipt: dict[str, Any]) -> CardReplay:
    """Recompute a stored card miss from its receipt's inputs ONLY (L57).

    Refuses when the inputs no longer hash to the stored digest's source —
    the caller compares `miss.inputs_sha256` against the row's.
    """
    inputs = receipt["inputs"]
    if inputs.get("formula_version") != FORMULA_VERSION:
        raise ReplayInputError(
            f"receipt formula {inputs.get('formula_version')!r} is not {FORMULA_VERSION!r}"
        )
    c = inputs["card"]
    card = CardCandidate(
        id=c["id"], ticker=c["ticker"], direction=c["direction"], entry=Decimal(c["entry"]),
        stop=Decimal(c["stop_current"]), created_at=datetime.fromisoformat(c["created_at"]),
        window_ref=c["window_ref"],
        transitions=tuple(TransitionRow(**t) for t in inputs["transitions"]),
        stop_edits=tuple(
            StopEdit(at=e["at"], from_stop=Decimal(e["from_stop"]), to_stop=Decimal(e["to_stop"]))
            for e in inputs["stop_edits"]
        ),
    )
    bars = [
        Bar(ticker=card.ticker, interval=Interval.I1, ts=b["ts"], open=Decimal(b["open"]),
            high=Decimal(b["high"]), low=Decimal(b["low"]), close=Decimal(b["close"]),
            volume=int(b["volume"]))
        for b in inputs["bars"]
    ]
    return replay_card(
        card, bars,
        trade_date=date.fromisoformat(inputs["trade_date"]),
        window=WindowResolution(**inputs["window"]),
        session_close=datetime.fromisoformat(inputs["session_close"]),
        positions=[PositionSpan(**p) for p in inputs["positions"]],
    )


# ---------------------------------------------------------------------------
# The window, through the public resolver
# ---------------------------------------------------------------------------


def resolve_window(ref: Optional[str], trade_date: date) -> WindowResolution:
    """`cards.expire.window_end_for` — the ONE public resolver — as an
    aware instant. Its early-close fallback only fires for an ambiguous
    ref; the caller still takes `min(this, actual close)` (R1-10)."""
    from cobalt.cards.expire import window_end_for

    end = window_end_for(ref, trade_date)
    return WindowResolution(
        resolved_end=datetime.combine(trade_date, end.at, tzinfo=ET),
        source=end.source, detail=end.detail,
    )


def session_close_for(trade_date: date, clock=None) -> datetime:
    """The trade date's ACTUAL RTH close (early-close aware), from the
    session clock — never a literal 16:00."""
    from cobalt.session import Session, session_clock

    clock = clock or session_clock()
    rth = next((w for w in clock.windows_for(trade_date) if w.session is Session.RTH), None)
    if rth is None:
        raise ReplayInputError(f"{trade_date} is not a trading day ({clock.calendar.describe(trade_date)})")
    return datetime.combine(trade_date, rth.end, tzinfo=ET)


# ---------------------------------------------------------------------------
# USER side: candidates, positions, and the versioned missed corpus
# ---------------------------------------------------------------------------


class MissedStore:
    """`"user".missed` and the card reads behind it.

    ADR-0008 D2 — USER side: cards, transitions and misses are one
    trader's record. System data the replay needs (bars, movers,
    membership) is read by SYSTEM stores and passed in as values; no
    connection here ever writes the system schema.
    """

    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    # -- reads ---------------------------------------------------------------

    def candidates(self, trade_date: date) -> list[CardCandidate]:
        """Cards created that ET day whose history never reached FILLED."""
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT s.id, s.ticker, s.direction, s.entry, s.stop, s.created_at
                FROM aset_sizings s
                WHERE (s.created_at AT TIME ZONE 'America/New_York')::date = %s
                  AND NOT EXISTS (SELECT 1 FROM card_transitions t
                                  WHERE t.card_id = s.id AND t.to_state = 'FILLED')
                ORDER BY s.created_at, s.id
                """,
                (trade_date,),
            )
            cards = [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]
            ids = [c["id"] for c in cards]
            transitions: dict[int, list[TransitionRow]] = {i: [] for i in ids}
            edits: dict[int, list[StopEdit]] = {i: [] for i in ids}
            if ids:
                for tid, card_id, frm, to, at in conn.execute(
                    "SELECT id, card_id, from_state, to_state, at FROM card_transitions "
                    "WHERE card_id = ANY(%s) ORDER BY at, id", (ids,),
                ).fetchall():
                    transitions[card_id].append(
                        TransitionRow(id=tid, card_id=card_id, from_state=frm, to_state=to, at=at)
                    )
                for eid, card_id, at, frm, to in conn.execute(
                    "SELECT id, card_id, at, from_stop, to_stop FROM card_stop_edits "
                    "WHERE card_id = ANY(%s) ORDER BY at, id", (ids,),
                ).fetchall():
                    edits[card_id].append(StopEdit(id=eid, at=at, from_stop=frm, to_stop=to))
        return [
            CardCandidate(
                id=c["id"], ticker=c["ticker"], direction=str(c["direction"]).lower(),
                entry=c["entry"], stop=c["stop"], created_at=c["created_at"],
                transitions=tuple(transitions[c["id"]]), stop_edits=tuple(edits[c["id"]]),
            )
            for c in cards
        ]

    def positions(self, trade_date: date) -> list[PositionSpan]:
        """Every card FILLED before the day ended and not CLOSED before it
        began — overnight holds included (rule_10 counts open positions)."""
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT f.card_id, min(f.at) AS filled_at,
                       (SELECT min(c.at) FROM card_transitions c
                        WHERE c.card_id = f.card_id AND c.to_state = 'CLOSED') AS closed_at
                FROM card_transitions f
                WHERE f.to_state = 'FILLED'
                  AND (f.at AT TIME ZONE 'America/New_York')::date <= %s
                GROUP BY f.card_id
                """,
                (trade_date,),
            ).fetchall()
        spans = [PositionSpan(card_id=r[0], filled_at=r[1], closed_at=r[2]) for r in rows]
        return [
            s for s in spans
            if s.closed_at is None or s.closed_at.astimezone(ET).date() >= trade_date
        ]

    def current(self, trade_date: date, kind: Optional[MissKind] = None) -> list[dict[str, Any]]:
        """The CURRENT rows for a day (the miss line publishes only these)."""
        sql = (
            "SELECT id, kind, ticker, direction, card_id, mover_id, pool_member_id, excluded_by, "
            "gate_detail, cf_r, mfe_r, inputs_sha256, replay_run_id, run_seq "
            "FROM missed WHERE user_id = current_setting('cobalt.trader_id')::int "
            "AND trade_date = %s AND is_current"
        )
        params: list[Any] = [trade_date]
        if kind is not None:
            sql += " AND kind = %s"
            params.append(kind)
        with self._connect() as conn:
            cur = conn.execute(sql + " ORDER BY kind, ticker, id", params)
            return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]

    # -- the one write: versioned reconciliation (R2-1 / R3-1) ---------------

    def reconcile(
        self,
        *,
        run_id: str,
        trade_date: date,
        kind: MissKind,
        rows: Sequence[MissRow],
        before_commit: Optional[Callable[[str], None]] = None,
    ) -> ReconcileCounts:
        """Make `rows` the current set of `kind` misses for `trade_date`.

        ONE serialized USER transaction, in the ruled order:
        (1) retire every predecessor this run replaces or drops
            (`is_current = false`, `retired_by_run_id`) — freeing the
            partial unique slot first;
        (2) INSERT the replacements;
        (3) link each predecessor's `superseded_by` to its replacement.
        A subject whose inputs hash and `excluded_by` are unchanged is left
        alone (an identical rerun writes nothing). `before_commit(stage)`
        is a test seam called after each stage.
        """
        for row in rows:
            if row.trade_date != trade_date or row.kind != kind:
                raise ReplayInputError(f"reconcile({trade_date}, {kind}) given a {row.kind} row for {row.trade_date}")
        subjects = [r.subject() for r in rows]
        if len(set(subjects)) != len(subjects):
            raise ReplayInputError(f"reconcile({trade_date}, {kind}): two rows share one subject")
        hook = before_commit or (lambda stage: None)

        conn = self._connect()
        conn.autocommit = False
        try:
            conn.execute("SELECT pg_advisory_xact_lock(hashtext(%s))", (f"replay:missed:{trade_date}",))
            cur = conn.execute(
                """
                SELECT id, trade_date, kind, ticker, card_id, trade_def_md5, formation_at,
                       pool_member_id, excluded_by, inputs_sha256, run_seq
                FROM missed
                WHERE user_id = current_setting('cobalt.trader_id')::int
                  AND trade_date = %s AND kind = %s AND is_current
                FOR UPDATE
                """,
                (trade_date, kind),
            )
            existing: dict[tuple, dict[str, Any]] = {}
            for r in cur.fetchall():
                rec = dict(zip([d.name for d in cur.description], r))
                key = (
                    rec["trade_date"], rec["kind"], rec["ticker"], rec["card_id"] or 0,
                    rec["trade_def_md5"] or "",
                    rec["formation_at"].isoformat() if rec["formation_at"] else "",
                    rec["pool_member_id"] if rec["kind"] == "formation" else 0,
                )
                existing[key] = rec

            unchanged, replace, new = 0, [], []
            for row in rows:
                prior = existing.get(row.subject())
                if prior is None:
                    new.append(row)
                elif prior["inputs_sha256"] == row.inputs_sha256 and prior["excluded_by"] == row.excluded_by:
                    unchanged += 1
                else:
                    replace.append((prior, row))
            wanted = set(subjects)
            dropped = [rec for key, rec in existing.items() if key not in wanted]

            retire_ids = [p["id"] for p, _ in replace] + [rec["id"] for rec in dropped]
            if retire_ids:
                conn.execute(
                    "UPDATE missed SET is_current = false, retired_by_run_id = %s WHERE id = ANY(%s)",
                    (run_id, retire_ids),
                )
            hook("retired")

            links: list[tuple[int, int]] = []
            for prior, row in [(None, r) for r in new] + replace:
                new_id = self._insert(conn, row, run_id=run_id,
                                      run_seq=1 if prior is None else int(prior["run_seq"]) + 1)
                if prior is not None:
                    links.append((prior["id"], new_id))
            hook("inserted")

            for prior_id, new_id in links:
                conn.execute("UPDATE missed SET superseded_by = %s WHERE id = %s", (new_id, prior_id))
            hook("linked")
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return ReconcileCounts(inserted=len(new), superseded=len(replace), retired=len(dropped),
                               unchanged=unchanged)

    @staticmethod
    def _insert(conn, row: MissRow, *, run_id: str, run_seq: int) -> int:
        got = conn.execute(
            """
            INSERT INTO missed (
                trade_date, kind, ticker, direction, card_id, trade_def_md5, formation_at,
                pool_member_id, mover_id, excluded_by, gate_detail, entry, stop, trigger_ts,
                fill_price, horizon_end, exit_ts, exit_price, exit_reason, cf_r, mfe_r,
                bars_watermark, formula_version, receipt, inputs_sha256, replay_run_id, run_seq)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s::jsonb, %s, %s, %s)
            RETURNING id
            """,
            (
                row.trade_date, row.kind, row.ticker, row.direction, row.card_id, row.trade_def_md5,
                row.formation_at, row.pool_member_id, row.mover_id, row.excluded_by,
                canonical_json(row.gate_detail), row.entry, row.stop, row.trigger_ts, row.fill_price,
                row.horizon_end, row.exit_ts, row.exit_price, row.exit_reason, row.cf_r, row.mfe_r,
                row.bars_watermark, row.formula_version, canonical_json(row.receipt),
                row.inputs_sha256, run_id, run_seq,
            ),
        ).fetchone()
        if got is None:
            raise ReplayInputError("missed INSERT returned no id")
        return int(got[0])


__all__ = [
    "GATE_ORDER", "MINUTE", "MissedStore", "RULE_10_PROXY", "STATE_GATE", "coverage",
    "day_bars", "ordered_transitions", "replay_card", "replay_from_receipt", "resolve_window",
    "session_close_for", "state_at", "stop_as_of",
]
