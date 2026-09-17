"""F3 picks — his pick against Cobalt's rank, recorded at the fill.

Charter F3: "DRC shows his pick and Cobalt's rank for every card". A PICK
is any card reaching FILLED (manual now, radar later; S2-P4 R2). One
`"user".picks` row per card, written by `record_pick()` INSIDE
`CardStore.fill()`'s transaction under `SAVEPOINT pick`. The row exists
now; DRC rendering lands in S3.

WHAT THE ROW SNAPSHOTS, AT PICK TIME
  * pool:  the admitted membership episode open at the fill instant for
    the ticker, in the configured pool (`radar.yaml` `pool_key`) — its
    `last_rank`, `rank_metric`, `rank_value` — plus the pool's size and
    last scan. `pool_basis` says why a pool field is null:
      'pool'                               the pool was readable
      'unavailable: pool row missing'      no `radar_pool` row
      'unavailable: pool degraded (...)'   the pool flagged degraded
      'unavailable: pool failed_stage=X'   the last scan failed a stage
    A ticker simply not in a readable pool is `not_in_pool = true` with
    `pool_basis = 'pool'`.
  * card score: `card_score` and its rank among open radar cards — only
    if S2-P2's `aset_sizings.card_score`/`conviction` columns exist. The
    cohort is WATCH/ARMED/TRIGGERED radar cards with a score, PLUS the
    picked card itself (Astra R1-6: after the FILLED hop it is no longer
    open and would drop out of its own ranking). `score_basis` names the
    outcome ('card_score' | 'unavailable: <reason>') and `score_inputs`
    stores the ordered cohort and the tie policy, so the rank replays
    (L57).

ONE CONNECTION. `record_pick` reads `system.radar_*` schema-qualified on
the USER connection it is handed (ADR-0008 permits qualified cross-side
reads); it opens no connection, switches no role and never commits — the
fill owns the transaction and the savepoint.
"""

from __future__ import annotations

import json
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from cobalt.radar.models import RankMetricName
from cobalt.session.clock import ET

#: The savepoint name `CardStore.fill()` wraps the pick in.
PICK_SAVEPOINT = "pick"

#: Open card states that form the card-score cohort (the pick joins them).
COHORT_STATES: tuple[str, ...] = ("WATCH", "ARMED", "TRIGGERED")

TIE_POLICY = (
    "competition ranking: rank = 1 + number of cohort cards with a strictly higher "
    "card_score; ties share a rank; cohort listed by (card_score desc, card_id asc)"
)

#: The number of top-ranked cards the focus view shows.
FOCUS_TOP_N = 4

P2_NOT_MERGED = "unavailable: S2-P2 not merged"


class PickError(RuntimeError):
    """A pick could not be recorded. Never refuses the fill (R2)."""


class CohortEntry(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    card_id: int
    card_score: int
    state: str


class PoolSnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")
    pool_member_id: int | None
    pool_basis: str = Field(min_length=1)
    pool_rank: int | None
    pool_size: int | None
    rank_metric: RankMetricName | None
    rank_value: Decimal | None
    pool_scan_id: int | None
    pool_scan_at: datetime | None

    @property
    def not_in_pool(self) -> bool:
        return self.pool_member_id is None


class ScoreSnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid")
    card_score: int | None
    card_score_rank: int | None
    focus_top4: bool | None
    score_basis: str = Field(min_length=1)
    score_inputs: dict[str, Any] = Field(min_length=1)

    @model_validator(mode="after")
    def _basis_matches(self) -> "ScoreSnapshot":
        ranked = self.score_basis == "card_score"
        if ranked != (self.card_score_rank is not None):
            raise ValueError("a card_score rank exists exactly when score_basis is 'card_score'")
        if not ranked and not self.score_basis.startswith("unavailable: "):
            raise ValueError("score_basis is 'card_score' or 'unavailable: <reason>'")
        return self


class PickRow(BaseModel):
    """One `"user".picks` row, validated before it is inserted."""

    model_config = ConfigDict(extra="forbid")
    card_id: int
    transition_id: int
    ticker: str = Field(min_length=1)
    picked_at: datetime
    session: str = Field(min_length=1)
    origin: str = Field(min_length=1)
    account_mode: str | None
    pool: PoolSnapshot
    score: ScoreSnapshot


class PickReportRow(BaseModel):
    """One FILLED transition of the day, left-joined to its pick."""

    model_config = ConfigDict(extra="forbid")
    transition_id: int
    card_id: int
    filled_at: datetime
    ticker: str
    state: str
    origin: str
    pick_id: int | None
    not_in_pool: bool | None
    pool_basis: str | None
    pool_rank: int | None
    pool_size: int | None
    rank_metric: RankMetricName | None
    rank_value: Decimal | None
    card_score: int | None
    card_score_rank: int | None
    focus_top4: bool | None
    score_basis: str | None


def configured_pool_key() -> str:
    """The pool a pick is ranked against — `radar.yaml`'s `pool_key`. A
    config error raises, inside the savepoint: pick not recorded, loud."""
    from cobalt.radar.config import load_config

    return load_config().pool_key


def rank_in_cohort(card_id: int, cohort: list[CohortEntry]) -> int:
    """Competition rank of `card_id` (see `TIE_POLICY`)."""
    own = next((entry for entry in cohort if entry.card_id == card_id), None)
    if own is None:
        raise PickError(f"card {card_id} is not in its own cohort — the pick must rank itself")
    return 1 + sum(1 for entry in cohort if entry.card_score > own.card_score)


def pool_snapshot(conn, *, ticker: str, at: datetime, pool_key: str) -> PoolSnapshot:
    pool = conn.execute(
        "SELECT members, last_scan_id, last_scan_at, degraded, degraded_sources, failed_stage "
        "FROM system.radar_pool WHERE pool_key = %s",
        (pool_key,),
    ).fetchone()
    empty = dict(pool_member_id=None, pool_rank=None, rank_metric=None, rank_value=None)
    if pool is None:
        return PoolSnapshot(**empty, pool_basis="unavailable: pool row missing",
                            pool_size=None, pool_scan_id=None, pool_scan_at=None)
    members, scan_id, scan_at, degraded, degraded_sources, failed_stage = pool
    scan = dict(pool_size=members, pool_scan_id=scan_id, pool_scan_at=scan_at)
    if failed_stage:
        return PoolSnapshot(**empty, **scan, pool_basis=f"unavailable: pool failed_stage={failed_stage}")
    if degraded:
        names = ", ".join(
            str(item.get("source", item)) if isinstance(item, dict) else str(item)
            for item in (degraded_sources or [])
        ) or "no source named"
        return PoolSnapshot(**empty, **scan, pool_basis=f"unavailable: pool degraded ({names})")
    member = conn.execute(
        "SELECT id, last_rank, rank_metric, rank_value FROM system.radar_membership "
        "WHERE pool_key = %s AND ticker = %s AND entered_at IS NOT NULL AND entered_at <= %s "
        "AND (left_at IS NULL OR left_at > %s) ORDER BY entered_at DESC, id DESC LIMIT 1",
        (pool_key, ticker, at, at),
    ).fetchone()
    if member is None:
        return PoolSnapshot(**empty, **scan, pool_basis="pool")
    member_id, last_rank, metric, value = member
    return PoolSnapshot(pool_member_id=member_id, pool_rank=last_rank, rank_metric=metric,
                        rank_value=value, **scan, pool_basis="pool")


def score_snapshot(conn, *, card_id: int) -> ScoreSnapshot:
    present = {
        row[0]
        for row in conn.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema = 'user' AND table_name = 'aset_sizings' "
            "AND column_name IN ('card_score', 'conviction')"
        ).fetchall()
    }

    def unavailable(reason: str, **extra: Any) -> ScoreSnapshot:
        return ScoreSnapshot(card_score=extra.pop("card_score", None), card_score_rank=None,
                             focus_top4=None, score_basis=reason,
                             score_inputs={"reason": reason, "columns_present": sorted(present), **extra})

    if "card_score" not in present:
        return unavailable(P2_NOT_MERGED)
    if "conviction" not in present:
        return unavailable("unavailable: S2-P2 conviction column absent")
    own = conn.execute(
        "SELECT card_score, conviction FROM aset_sizings WHERE id = %s", (card_id,)
    ).fetchone()
    if own is None:
        raise PickError(f"no aset_sizings row with id {card_id}")
    score, conviction = own
    if conviction is None:
        return unavailable("unavailable: no taps", card_score=score)
    if score is None:
        return unavailable("unavailable: card_score suppressed", conviction=str(conviction))
    rows = conn.execute(
        "SELECT id, card_score, state FROM aset_sizings WHERE card_score IS NOT NULL "
        "AND ((origin = 'radar' AND state = ANY(%s)) OR id = %s) ORDER BY card_score DESC, id",
        (list(COHORT_STATES), card_id),
    ).fetchall()
    cohort = [CohortEntry(card_id=r[0], card_score=r[1], state=r[2]) for r in rows]
    rank = rank_in_cohort(card_id, cohort)
    return ScoreSnapshot(
        card_score=score, card_score_rank=rank, focus_top4=rank <= FOCUS_TOP_N, score_basis="card_score",
        score_inputs={
            "tie_policy": TIE_POLICY,
            "cohort_states": list(COHORT_STATES),
            "focus_top_n": FOCUS_TOP_N,
            "conviction": str(conviction),
            "cohort": [entry.model_dump() for entry in cohort],
        },
    )


def record_pick(conn, card_id: int, transition_id: int, now: datetime, *, pool_key: str | None = None) -> int:
    """Write the pick row for the FILLED hop `transition_id`. Returns its id.

    Runs on the fill's open connection, inside `SAVEPOINT pick`; any
    exception is the caller's to roll back to the savepoint.
    """
    card = conn.execute(
        "SELECT ticker, origin, account_mode FROM aset_sizings WHERE id = %s", (card_id,)
    ).fetchone()
    if card is None:
        raise PickError(f"no aset_sizings row with id {card_id}")
    hop = conn.execute(
        "SELECT card_id, to_state, session FROM card_transitions WHERE id = %s", (transition_id,)
    ).fetchone()
    if hop is None or hop[0] != card_id or hop[1] != "FILLED":
        raise PickError(
            f"transition {transition_id} is not card {card_id}'s FILLED hop (got {hop!r})"
        )
    ticker, origin, account_mode = card
    row = PickRow(
        card_id=card_id,
        transition_id=transition_id,
        ticker=ticker,
        picked_at=now,
        session=hop[2],
        origin=origin,
        account_mode=account_mode,
        pool=pool_snapshot(conn, ticker=ticker, at=now, pool_key=pool_key or configured_pool_key()),
        score=score_snapshot(conn, card_id=card_id),
    )
    inserted = conn.execute(
        "INSERT INTO picks (card_id, transition_id, ticker, picked_at, session, origin, account_mode, "
        "pool_member_id, not_in_pool, pool_basis, pool_rank, pool_size, rank_metric, rank_value, "
        "pool_scan_id, pool_scan_at, card_score, card_score_rank, focus_top4, score_basis, score_inputs) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb) "
        "RETURNING id",
        (
            row.card_id, row.transition_id, row.ticker, row.picked_at, row.session, row.origin,
            row.account_mode, row.pool.pool_member_id, row.pool.not_in_pool, row.pool.pool_basis,
            row.pool.pool_rank, row.pool.pool_size, row.pool.rank_metric, row.pool.rank_value,
            row.pool.pool_scan_id, row.pool.pool_scan_at, row.score.card_score,
            row.score.card_score_rank, row.score.focus_top4, row.score.score_basis,
            json.dumps(row.score.score_inputs),
        ),
    ).fetchone()
    if inserted is None:
        raise PickError(f"pick INSERT for card {card_id} returned no id")
    return int(inserted[0])


def _fmt_value(metric: str | None, value: Decimal | None) -> str:
    if metric is None:
        return "—"
    return f"{metric} {'—' if value is None else format(value.normalize(), 'f')}"


def render_picks_report(
    rows: list[PickReportRow], *, day: date, cutoff: datetime | None
) -> tuple[str, int]:
    """(table text, MISSING count that fails the command).

    A FILLED transition with no pick prints MISSING. With `cutoff` (the P4
    deploy instant, K6), a gap before it prints `MISSING (before cutoff)`
    and is not counted — historical gaps stay visible, never fatal.
    """
    lines = [
        f"picks {day.isoformat()} — every FILLED transition that ET day",
        f"{'filled (ET)':<9} {'card':>6} {'ticker':<7} {'state':<7} {'pool':<14} "
        f"{'value':<18} {'score rank':<10} basis",
    ]
    counted = 0
    for row in rows:
        at = row.filled_at.astimezone(ET).strftime("%H:%M:%S")
        if row.pick_id is None:
            before = cutoff is not None and row.filled_at < cutoff
            if not before:
                counted += 1
            label = "MISSING (before cutoff)" if before else "MISSING"
            lines.append(f"{at:<9} {row.card_id:>6} {row.ticker} {row.state:<7} {label}")
            continue
        if row.not_in_pool:
            pool = "not in pool" if row.pool_basis == "pool" else "—"
        else:
            pool = f"#{row.pool_rank}/{row.pool_size}"
        score = "—" if row.card_score_rank is None else f"#{row.card_score_rank} ({row.card_score})"
        basis = row.score_basis if row.pool_basis == "pool" else f"{row.pool_basis}; {row.score_basis}"
        lines.append(
            f"{at:<9} {row.card_id:>6} {row.ticker} {row.state:<7} {pool:<14} "
            f"{_fmt_value(row.rank_metric, row.rank_value):<18} {score:<10} {basis}"
        )
    lines.append(f"{len(rows)} FILLED transition(s) · {counted} MISSING")
    return "\n".join(lines), counted


__all__ = [
    "COHORT_STATES",
    "CohortEntry",
    "FOCUS_TOP_N",
    "PICK_SAVEPOINT",
    "PickError",
    "PickReportRow",
    "PickRow",
    "PoolSnapshot",
    "ScoreSnapshot",
    "TIE_POLICY",
    "configured_pool_key",
    "pool_snapshot",
    "rank_in_cohort",
    "record_pick",
    "render_picks_report",
    "score_snapshot",
]
