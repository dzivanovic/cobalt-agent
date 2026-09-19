"""The PRE-WRITE shadow compare — the evidence for the owner's switch ruling.

Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §5,
and spec O-6.

WHY IT IS PRE-WRITE, AND WHY THAT IS THE WHOLE POINT. The first design
proposed an `audit` command run AFTER the nightly overlay. Three houses
refused it in round 3 with the same argument, and they were right: the
20:30 run's `INSERT … DO UPDATE` refreshes every in-window bar, so an
audit taken afterwards reads zeros by construction and cannot tell the
owner whether `append` would have halted any target. So the comparison
happens INSIDE the nightly run, per target, AFTER the fetch and BEFORE
that target's `upsert_bars` — and every record carries the literal
label `pre-write` so a reader of the artifact can see which it is.

IT CAN NEVER FAIL OR SLOW-FAIL A TARGET. The read is bounded by its own
`statement_timeout` (§10), the whole observation is wrapped by the
runner in `try/except Exception` and counted as `shadow_errors`, and
the target's `upsert_bars` runs whatever the shadow did. The 1.2 s
pacing is untouched. Tests drive an exception, a timeout and a slow read
and assert the target's write and the run summary are IDENTICAL to a
night with the shadow off.

IT IS READ-ONLY. No bar, progress row, incident or config is written.
The runner's fake store records every call, and the test asserts the
only write method reached on a shadow night is the target's own upsert.

THE ARTIFACT IS A RETAINED BASELINE, not a log. Refreshed storage alone
cannot show revision FREQUENCY — after tonight's overlay, last night's
difference is gone. So each night is a JSON-lines file under
`data/archiver-shadow/` (gitignored; never `git add`ed), and
`shadow-report` reads ACROSS nights to say which differing keys
PERSISTED, VANISHED or APPEARED. Astra and Grok both required exactly
that.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field

from .config import REPO_ROOT
from .models import Interval
from .reconcile import compare, et_date, split_export, steady_state_dates

#: `data/` is gitignored (`.gitignore:6`) — this directory is never a
#: committed path, and no `git add` in this build names it.
SHADOW_DIR = REPO_ROOT / "data" / "archiver-shadow"

#: The literal §5 requires on every record.
LABEL = "pre-write"


class ScopeResult(BaseModel):
    """One scope's four-way comparison, as the artifact carries it."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    scope: str
    candidates: int = 0
    already_stored_equal: int = 0
    differing: list[dict] = Field(default_factory=list)
    incoming_only: int = 0
    new: int = 0
    late: int = 0
    stored_only: int = 0
    would_withhold: bool = False
    #: True when EVERY differing key differs only in volume — the cheap
    #: question the owner will ask first, because a volume-only
    #: restatement is a different kind of worry from a price one.
    volume_only: bool = False


class ShadowRecord(BaseModel):
    """One target's night, as one line of the artifact."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    label: str = LABEL
    ticker: str
    interval: str
    fetch_started_at: str
    fetched: int
    export_oldest: str | None
    export_newest: str | None
    raw_export_newest: str | None
    archived_through: str | None
    stored_rows_read: int
    #: Whether the RADAR POLLER can write this target at all. The poller
    #: writes i1 and only i1 (`radar/poller.py:88`), so this is decided
    #: from the interval rather than by reading the live pool — the
    #: archiver's night does not query the radar's tables.
    poller_writable: bool
    bootstrap: ScopeResult
    steady_state: ScopeResult

    def as_line(self) -> str:
        return json.dumps(self.model_dump(), sort_keys=True, default=str)


def _scope(scope: str, candidates, stored, *, archived_through) -> ScopeResult:
    result = compare(candidates, stored)
    late = (
        0
        if archived_through is None
        else sum(1 for k in result.incoming_only if k <= archived_through)
    )
    differing = [d.as_detail() for d in result.differing]
    volume_only = bool(differing) and all(
        {f["field"] for f in d["fields"]} == {"volume"} for d in differing
    )
    return ScopeResult(
        scope=scope,
        candidates=len(candidates),
        already_stored_equal=len(result.equal),
        differing=differing,
        incoming_only=len(result.incoming_only),
        new=len(result.incoming_only) - late,
        late=late,
        stored_only=len(result.stored_only),
        would_withhold=bool(result.differing),
        volume_only=volume_only,
    )


def observe(
    store,
    *,
    ticker: str,
    interval: Interval,
    bars,
    fetch_started_at,
    settings,
    archived_through=None,
) -> ShadowRecord:
    """What `append` WOULD have done to this target tonight.

    ONE read of the stored rows over the eligible export's range; both
    scopes are then computed in memory, so the steady-state scope costs
    no second query.

    This function does not catch its own exceptions — the RUNNER does,
    once, and counts `shadow_errors`. Swallowing here would hide a
    systematically broken shadow behind a clean-looking night.
    """
    split = split_export(list(bars), interval, fetch_started_at)
    eligible = split.eligible
    stored: dict = {}
    if eligible:
        with store.target_transaction() as conn:
            _bound_statement(conn, settings.shadow_statement_timeout_s)
            stored = store._bars_in_range(
                conn, ticker, interval, split.export_oldest, split.export_newest
            )

    steady_dates = set(steady_state_dates(eligible, fetch_started_at))
    steady = tuple(b for b in eligible if et_date(b.ts) in steady_dates)
    steady_keys = {b.ts for b in steady}

    return ShadowRecord(
        ticker=ticker,
        interval=interval.value,
        fetch_started_at=fetch_started_at.isoformat(),
        fetched=split.fetched,
        export_oldest=split.export_oldest.isoformat() if split.export_oldest else None,
        export_newest=split.export_newest.isoformat() if split.export_newest else None,
        raw_export_newest=split.raw_newest.isoformat() if split.raw_newest else None,
        archived_through=archived_through.isoformat() if archived_through else None,
        stored_rows_read=len(stored),
        poller_writable=interval is Interval.I1,
        bootstrap=_scope("bootstrap", eligible, stored, archived_through=archived_through),
        steady_state=_scope(
            "steady_state",
            steady,
            {k: v for k, v in stored.items() if k in steady_keys},
            archived_through=archived_through,
        ),
    )


def _bound_statement(conn, timeout_s: int) -> None:
    """The shadow's read is bounded, not trusted (§5, §10).

    `set_config(..., is_local => true)` rather than a `SET LOCAL` string
    so the value reaches the server as a PARAMETER — and so it expires
    with the transaction rather than leaking onto a pooled session.
    """
    conn.execute(
        "SELECT set_config('statement_timeout', %s, true)", (str(int(timeout_s) * 1000),)
    )


# ---------------------------------------------------------------------
# The artifact
# ---------------------------------------------------------------------


def write_records(records, *, night: date, retention_nights: int) -> Path:
    """Append tonight's records to `data/archiver-shadow/<date>.jsonl`.

    Append rather than replace: `run_full` and a manual `--backfill`
    can both happen on one night, and the second must not erase the
    first's evidence.
    """
    SHADOW_DIR.mkdir(parents=True, exist_ok=True)
    path = SHADOW_DIR / f"{night.isoformat()}.jsonl"
    with open(path, "a", encoding="utf-8") as handle:
        for record in records:
            handle.write(record.as_line() + "\n")
    apply_retention(retention_nights=retention_nights, today=night)
    return path


def apply_retention(*, retention_nights: int, today: date) -> list[Path]:
    """Delete nights older than the window. Returns what was removed.

    Bounded by the FILENAME's date, not by mtime: a file copied or
    restored keeps its night, and an mtime-based sweep would keep
    whatever was touched last rather than whatever is recent.
    """
    if not SHADOW_DIR.exists():
        return []
    cutoff = today - timedelta(days=retention_nights - 1)
    removed: list[Path] = []
    for path in sorted(SHADOW_DIR.glob("*.jsonl")):
        try:
            night = date.fromisoformat(path.stem)
        except ValueError:
            continue
        if night < cutoff:
            path.unlink()
            removed.append(path)
    return removed


def read_night(night: date) -> list[dict]:
    path = SHADOW_DIR / f"{night.isoformat()}.jsonl"
    if not path.exists():
        return []
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def recent_nights(limit: int) -> list[tuple[str, list[dict]]]:
    """The most recent `limit` nights present, oldest first."""
    if not SHADOW_DIR.exists():
        return []
    paths = sorted(SHADOW_DIR.glob("*.jsonl"))[-limit:]
    return [
        (
            path.stem,
            [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ],
        )
        for path in paths
    ]


def differing_keys(records) -> set[tuple[str, str, str]]:
    """`(ticker, interval, ts)` of every key that differed, bootstrap scope."""
    keys: set[tuple[str, str, str]] = set()
    for record in records:
        for difference in record.get("bootstrap", {}).get("differing", []):
            keys.add((record["ticker"], record["interval"], difference["ts"]))
    return keys


def persisted_vanished_appeared(nights) -> dict[str, list]:
    """Across nights: which differing keys survived, went away, are new.

    `nights` is `[(label, keys_or_records), …]`, oldest first. PURE:
    the command reads the artifacts and hands the sets in, so the
    arithmetic is testable without a filesystem.

    This is the number the owner needs and the one a post-write audit
    cannot produce: a difference that VANISHES was healed by the very
    overlay `append` would stop doing.
    """
    sets = []
    for _, payload in nights:
        if isinstance(payload, set):
            sets.append(payload)
        else:
            sets.append(differing_keys(payload))
    if not sets:
        return {"persisted": [], "vanished": [], "appeared": []}
    first, last = sets[0], sets[-1]
    earlier = set().union(*sets[:-1]) if len(sets) > 1 else set()
    return {
        "persisted": sorted(last & earlier),
        "vanished": sorted(first - last),
        "appeared": sorted(last - earlier),
    }


def aggregate(records, *, errors: int) -> dict:
    """`job.result["shadow"]` (§5): what a night's shadow saw, in one dict."""
    by_interval: dict[str, int] = {}
    poller_writable = 0
    archiver_only = 0
    volume_only = 0
    any_ohlc = 0
    late = 0
    new = 0
    for record in records:
        scope = record.bootstrap
        late += scope.late
        new += scope.new
        if not scope.would_withhold:
            continue
        by_interval[record.interval] = by_interval.get(record.interval, 0) + 1
        if record.poller_writable:
            poller_writable += 1
        else:
            archiver_only += 1
        if scope.volume_only:
            volume_only += 1
        else:
            any_ohlc += 1
    return {
        "label": LABEL,
        "targets_compared": len(records),
        "targets_errored": errors,
        "would_withhold_by_interval": by_interval,
        "would_withhold_poller_writable": poller_writable,
        "would_withhold_archiver_only": archiver_only,
        "volume_only": volume_only,
        "any_ohlc": any_ohlc,
        "late": late,
        "new": new,
    }


__all__ = [
    "LABEL",
    "SHADOW_DIR",
    "ScopeResult",
    "ShadowRecord",
    "aggregate",
    "apply_retention",
    "differing_keys",
    "observe",
    "persisted_vanished_appeared",
    "read_night",
    "recent_nights",
    "write_records",
]
