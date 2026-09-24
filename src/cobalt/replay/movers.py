"""F13: the day's unfiltered top movers, their i1 archive, and the
benchmark diff against the pool (S2-P4 STEP-6, R5 as amended).

WHAT MOVED THAT WE NEVER SAW. Two unfiltered screener exports — gainers
(`o=-change`) and losers (`o=change`), `v` and the column list from
radar.yaml, NO filter string — are fetched once each through the one
transport (`finviz_get`) and the process TokenBucket, after the shared L53
demand gate. The top `radar.benchmark.top_n` rows per side go to
`system.movers_daily`; their i1 bars are archived for every ticker whose
bars do not already cover the session, whether or not any watchlist names
it. Movers with |change| >= `min_move_pct` are then diffed against the
day's `radar_membership` episodes:

* any admitted episode (`entered_at` set)      -> in play, no row
* only never-admitted episodes                  -> `excluded_by` = the most
                                                   recent one's value
* no episode at all                             -> `not_in_any_source`

A ticker on both sides becomes one row (the larger |change| carries it,
both sides recorded). A mover whose export row is not equity under R16
"C" — `Asset Type` non-blank OR `Industry` a fund industry — leaves the
benchmark.

WHICH ROW DECIDES. Both columns are required headers, so a COLUMN is
never missing: an export without one is a FAILED parse naming it. Only a
row's own CELL may be blank, and a blank `Asset Type` on an ordinary
stock is exactly what Finviz returns — that is all `unreported` means in
`gate_detail`. A blank `Change` cell is the one blank that decides a row
out: Finviz lists never-traded listings with no change at all, and such a
row is UNRANKED — never a `MoverRow`, never stored or benchmarked,
counted and logged per side, and a side with nothing but blank rows
FAILS. The decision is taken AT INGEST, off the parsed export
rows, because `movers_daily` stores no `industry` column: the
`StoredMover`s the benchmark receives on the live path come back from a
SELECT that never carried the second half of the rule. Under-reporting a
miss is the silent failure, so nothing here guesses either way.

HISTORY IS NEVER RELABELLED. A `--date` run for a past day reads the
exports retained under `data/radar-cache/<date>/movers-<side>-HHMMSS.csv`
and fetches no bars; if none are retained it refuses (R1-20).

ROWS ARE NEVER DELETED. A rerun that drops a mover out of the selected set
marks its row `active = false` so `"user".missed.mover_id` keeps its
target; an identical rerun (same export bytes, same values) changes
nothing (R2-1).

WHAT THE EXPORT REALLY HAD is recorded, never inferred. Each export keeps
its own row count (`exported_rows`) and `export_counts` writes
`min(top_n, exported)` per side into `job.result`, so a side Finviz
returned short of `top_n` reads as a fact rather than as missing rows.
Its unranked (blank-`Change`) rows are counted beside it, so the cap is
really `min(top_n, exported - unranked)` and the smoke compares against
that.
This is bookkeeping: the rows stored, benchmarked and archived are the
same `rows[:top_n]` in the same order, whether or not anyone counts them.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Callable, Optional

from loguru import logger

from cobalt import db, env
from cobalt.archiver.collector import FetchMetrics, fetch_bars, finviz_get, scrub
from cobalt.archiver.models import Bar, Interval
from cobalt.db import Side as DbSide
from cobalt.radar.collector import SourceFailure, parse_screener_csv
from cobalt.radar.config import (
    NotEquityConfig,
    RadarConfig,
    is_not_equity,
    screener_columns_param,
)
from cobalt.radar.config import load_config as load_radar_config
from cobalt.radar.notes import check_scheduled_demand
from cobalt.session.clock import ET
from cobalt.settings.models import BenchmarkSettings

from .cards import MINUTE, coverage, day_bars
from .models import (
    Episode,
    MissRow,
    MoverRow,
    MoversExport,
    MoversSideCount,
    ReplayError,
    ReplayInputError,
    StoredMover,
    canonical_json,
    sha256_json,
)

#: side -> the export's sort parameter. Gainers descend, losers ascend.
SIDES: dict[str, str] = {"gainers": "-change", "losers": "change"}

#: What the replay cannot run without. Both R16 columns are in here, so
#: neither can go missing quietly: an export without one is a FAILED
#: parse naming the header, never 61 rows that all read `unreported`.
REQUIRED_HEADERS = ["Ticker", "Change", "Volume", "Asset Type", "Industry"]

#: The exclusion values a never-admitted membership episode may carry.
EPISODE_EXCLUSIONS = {"config_cap", "not_equity", "screen_inactive", "manual"}

_CACHE_NAME = re.compile(r"^movers-(gainers|losers)-(\d{6})\.csv$")

__all__ = [
    "ArchiveOutcome", "MoversCollector", "MoversStore", "REQUIRED_HEADERS", "SIDES",
    "archive_movers", "benchmark_misses", "export_counts", "load_radar_config",
    "mover_is_not_equity", "not_equity_verdicts", "parse_change_pct",
    "parse_movers", "replay_request_count", "retained_exports",
]


def replay_request_count(top_n: int) -> int:
    """Replay's Finviz demand: two exports + one i1 fetch per top-N mover
    per side (L53, counted in the total)."""
    return 2 + 2 * top_n


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def parse_change_pct(raw: str) -> Decimal:
    text = (raw or "").strip()
    if not text.endswith("%"):
        raise SourceFailure(f"movers: Change {raw!r} is not a percentage")
    try:
        return Decimal(text[:-1])
    except InvalidOperation as e:
        raise SourceFailure(f"movers: Change {raw!r} is not a number") from e


def _optional_int(raw: Optional[str]) -> Optional[int]:
    if raw is None or not raw.strip():
        return None
    try:
        return int(Decimal(raw.replace(",", "")))
    except InvalidOperation as e:
        raise SourceFailure(f"movers: Volume {raw!r} is not a number") from e


def _optional_decimal(raw: Optional[str]) -> Optional[Decimal]:
    if raw is None or not raw.strip():
        return None
    try:
        return Decimal(raw)
    except InvalidOperation as e:
        raise SourceFailure(f"movers: value {raw!r} is not a number") from e


def parse_movers(
    payload: bytes,
    *,
    side: str,
    top_n: int,
    content_type: Optional[str],
    config: RadarConfig,
    fetched_at: datetime,
    source: str,
    cache_path: Optional[str] = None,
    check_order: bool = True,
) -> MoversExport:
    """One side's export -> its top `top_n` rows, ranked in export order.

    The export IS the ranking, so its order is verified: a gainers file
    whose Change is not non-increasing is the wrong sort (or the wrong
    side), and refusing it is cheaper than benchmarking against it.

    A row whose `Change` cell is EMPTY is unranked: skipped, counted in
    `unranked_rows`, one WARNING per side. Its position in the export
    does not matter — `rank` counts ranked rows only, and so does the
    sort check. Any other cell that is not a percentage still fails.
    """
    if side not in SIDES:
        raise SourceFailure(f"movers: unknown side {side!r}")
    header, raw_rows = parse_screener_csv(
        payload, source=f"movers-{side}", required_headers=REQUIRED_HEADERS, content_type=content_type,
    )
    # Both R16 columns are required headers, so both are read on every
    # row without asking whether the column is there — it is, or the
    # parse already failed above. A blank CELL stays None.
    asset_header = config.not_equity.asset_type_header
    industry_header = config.not_equity.industry_header
    rvol_header = config.export.metric_headers.rvol
    rows: list[MoverRow] = []
    unranked = 0
    for index, raw in enumerate(raw_rows, start=1):
        ticker = (raw.get("Ticker") or "").strip().upper()
        if not ticker:
            raise SourceFailure(f"movers-{side}: row {index} has no ticker")
        change = raw.get("Change", "")
        if (change or "").strip() == "":
            unranked += 1
            continue
        rows.append(MoverRow(
            side=side, rank=len(rows) + 1, ticker=ticker, change_pct=parse_change_pct(change),
            asset_type=(raw.get(asset_header) or None),
            industry=(raw.get(industry_header) or None),
            volume=_optional_int(raw.get("Volume")),
            rvol=_optional_decimal(raw.get(rvol_header)) if rvol_header in header else None,
        ))
    if unranked:
        if not rows:
            raise SourceFailure(f"movers-{side}: every one of {len(raw_rows)} rows has a blank Change")
        logger.warning("movers-{}: {} of {} rows have a blank Change — unranked, not stored, not benchmarked",
                       side, unranked, len(raw_rows))
    if check_order:
        changes = [r.change_pct for r in rows]
        descending = side == "gainers"
        broken = next(
            (i for i, (a, b) in enumerate(zip(changes, changes[1:]), start=1)
             if (b > a if descending else b < a)),
            None,
        )
        if broken is not None:
            raise SourceFailure(
                f"movers-{side}: Change is not sorted {'descending' if descending else 'ascending'} "
                f"at row {broken} — the wrong sort or the wrong side"
            )
    return MoversExport(
        side=side, fetched_at=fetched_at, export_sha256=hashlib.sha256(payload).hexdigest(),
        header=tuple(header), rows=tuple(rows[:top_n]), exported_rows=len(raw_rows),
        unranked_rows=unranked, source=source, cache_path=cache_path,
    )


def mover_is_not_equity(row: MoverRow, config: NotEquityConfig) -> bool:
    """A parsed export row through the ONE evaluator (L3).

    The only thing this adds is the two-key mapping `is_not_equity`
    reads; the OR itself lives there and nowhere else, so the movers
    benchmark and the radar's candidate gather cannot drift apart.
    """
    return is_not_equity(
        {config.asset_type_header: row.asset_type, config.industry_header: row.industry}, config
    )


def not_equity_verdicts(exports: Sequence[MoversExport]) -> dict[tuple[str, str], MoverRow]:
    """(side, ticker) -> the export row that decides that mover.

    Built ONCE per run, straight off the parsed exports, before anything
    is stored. This is the whole reason the rule works on the live path:
    `movers_daily` has no `industry` column, so the `StoredMover`s that
    come back from `MoversStore.reconcile` cannot answer the question
    themselves, and a row reconstructed from them would silently read
    every blank-`Asset Type` fund as an ordinary stock.

    A repeated (side, ticker) inside one run is loud: keeping the last
    one would make the verdict depend on export order, and an export
    that lists a ticker twice is a source fault, not a tie to break.
    """
    verdicts: dict[tuple[str, str], MoverRow] = {}
    for export in exports:
        for row in export.rows:
            key = (row.side, row.ticker)
            if key in verdicts:
                raise ReplayInputError(
                    f"movers-{row.side}: {row.ticker} appears twice in one run's exports "
                    f"(ranks {verdicts[key].rank} and {row.rank}) — no verdict can be chosen"
                )
            verdicts[key] = row
    return verdicts


def _verdict(
    verdicts: Mapping[tuple[str, str], MoverRow], *, side: str, ticker: str
) -> MoverRow:
    """The export row behind a stored mover, or a loud failure.

    Every `StoredMover` the benchmark sees came from an `exports` row of
    this same run, so a lookup miss is a bug in the run, not a data
    condition — there is no fallback that could guess the two columns
    back, and guessing is what the whole rule exists to stop (L1).
    """
    row = verdicts.get((side, ticker))
    if row is None:
        raise ReplayInputError(
            f"movers-{side}: {ticker} has no export row in this run's not-equity verdicts — "
            "every stored mover came from one"
        )
    return row


def export_counts(exports: Sequence[MoversExport], *, top_n: int) -> dict[str, MoversSideCount]:
    """Per side: what the export really had, and how many rows that allows.

    BOOKKEEPING ONLY. It reads the exports already in memory and selects,
    orders and drops nothing: `expected` is `min(top_n, exported -
    unranked)`, the same cap `parse_movers` already applied to the ranked
    rows, written down so the S2 smoke
    can check the stored count against the night's own export instead of
    a hand count of the cached CSV. A disagreement between the count and
    the rows kept, or a side seen twice, is loud (L1).
    """
    counts: dict[str, MoversSideCount] = {}
    for export in exports:
        if export.side in counts:
            raise ReplayInputError(f"two exports for side {export.side!r} in one run")
        expected = min(top_n, export.exported_rows - export.unranked_rows)
        if len(export.rows) != expected:
            raise ReplayInputError(
                f"movers-{export.side}: the export kept {len(export.rows)} of {export.exported_rows} "
                f"rows, not min(top_n {top_n}, exported {export.exported_rows} - unranked "
                f"{export.unranked_rows}) = {expected}"
            )
        counts[export.side] = MoversSideCount(exported=export.exported_rows, unranked=export.unranked_rows,
                                              top_n=top_n, expected=expected)
    return counts


# ---------------------------------------------------------------------------
# Collection (behind the collector interface, L9)
# ---------------------------------------------------------------------------


class MoversCollector:
    """Unfiltered exports and i1 fetches through the one transport and the
    process TokenBucket, each batch behind the shared L53 gate."""

    def __init__(
        self,
        token: str,
        *,
        config: RadarConfig,
        bucket,
        cache_root: Path,
        get: Callable[..., Any] = finviz_get,
        fetch_bars: Callable[..., Any] = fetch_bars,
    ):
        self.token = token
        self.config = config
        self.bucket = bucket
        self.cache_root = Path(cache_root)
        self._get = get
        self._fetch_bars = fetch_bars

    def _params(self, side: str) -> dict[str, object]:
        return {"v": self.config.export.v, "c": screener_columns_param(self.config.export.columns),
                "o": SIDES[side]}

    async def exports(self, *, top_n: int, now: datetime, cache: bool,
                      trade_date: Optional[date] = None) -> list[MoversExport]:
        """Both sides, live. `cache=False` (dry run) writes nothing."""
        check_scheduled_demand("replay", replay_top_n=top_n)
        trade_date = trade_date or now.astimezone(ET).date()
        out = []
        for side in SIDES:
            metrics: list[FetchMetrics] = []
            await self.bucket.acquire()
            try:
                response = await self._get("/export/screener", self._params(side), self.token,
                                           on_metrics=metrics.append)
            except Exception as e:
                raise SourceFailure(f"movers-{side}: {scrub(str(e))}") from e
            metric = metrics[-1] if metrics else None
            if metric is not None and metric.redirect_statuses:
                raise SourceFailure(f"movers-{side}: redirect statuses {list(metric.redirect_statuses)}")
            path = None
            if cache:
                folder = self.cache_root / trade_date.isoformat()
                folder.mkdir(parents=True, exist_ok=True)
                target = folder / f"movers-{side}-{now.astimezone(ET):%H%M%S}.csv"
                target.write_bytes(response.content)
                path = str(target)
            out.append(parse_movers(
                response.content, side=side, top_n=top_n,
                content_type=metric.content_type if metric else None, config=self.config,
                fetched_at=now, source="live", cache_path=path,
            ))
        return out

    async def bars(self, tickers: Sequence[str], *, top_n: int) -> tuple[dict[str, list[Bar]], dict[str, str]]:
        """i1 bars per ticker. A per-ticker failure is returned, not raised
        (archiver semantics: counted, and the job fails at the end)."""
        check_scheduled_demand("replay", replay_top_n=top_n)
        fetched: dict[str, list[Bar]] = {}
        failures: dict[str, str] = {}
        for ticker in tickers:
            await self.bucket.acquire()
            try:
                fetched[ticker] = await self._fetch_bars(ticker, Interval.I1, self.token)
            except Exception as e:  # noqa: BLE001 — counted per ticker, never swallowed
                failures[ticker] = f"{type(e).__name__}: {scrub(str(e))}"
        return fetched, failures


def retained_exports(cache_root: Path, trade_date: date, *, top_n: int, config: RadarConfig) -> list[MoversExport]:
    """A historical day's exports, as retained. Never a fresh fetch."""
    folder = Path(cache_root) / trade_date.isoformat()
    out = []
    for side in SIDES:
        found = sorted(
            (p for p in folder.glob(f"movers-{side}-*.csv") if _CACHE_NAME.match(p.name)),
            key=lambda p: p.name,
        ) if folder.is_dir() else []
        if not found:
            raise ReplayError(
                f"no retained movers export for {trade_date} ({side}) under {folder} — a historical "
                "run reads what was retained and never relabels a live fetch"
            )
        path = found[-1]
        stamp = _CACHE_NAME.match(path.name).group(2)
        fetched_at = datetime.combine(
            trade_date, datetime.strptime(stamp, "%H%M%S").time(), tzinfo=ET
        )
        out.append(parse_movers(path.read_bytes(), side=side, top_n=top_n, content_type="text/csv",
                                config=config, fetched_at=fetched_at, source="retained",
                                cache_path=str(path)))
    return out


# ---------------------------------------------------------------------------
# The benchmark (pure)
# ---------------------------------------------------------------------------


def benchmark_misses(
    movers: Sequence[StoredMover],
    episodes: Sequence[Episode],
    *,
    settings: BenchmarkSettings,
    trade_date: date,
    not_equity: NotEquityConfig,
    verdicts: Mapping[tuple[str, str], MoverRow],
) -> list[MissRow]:
    """`kind='mover'` rows for every benchmark mover the pool never admitted.

    `verdicts` is this run's ingest lookup (`not_equity_verdicts`). The
    not-equity rule is applied to the EXPORT row it holds, never to the
    `StoredMover`: `movers_daily` has no `industry` column at all, and
    its `asset_type` is whatever a round trip returned rather than what
    tonight's export said. The receipt records the looked-up values for
    the same reason (L57) — a miss row has to replay without the table.
    """
    by_ticker: dict[str, list[StoredMover]] = {}
    for mover in movers:
        if mover.trade_date != trade_date:
            raise ReplayInputError(f"mover {mover.ticker} is for {mover.trade_date}, not {trade_date}")
        by_ticker.setdefault(mover.ticker, []).append(mover)
    episodes_by: dict[str, list[Episode]] = {}
    for ep in episodes:
        if ep.trade_date == trade_date:
            episodes_by.setdefault(ep.ticker, []).append(ep)

    rows: list[MissRow] = []
    for ticker in sorted(by_ticker):
        sides = by_ticker[ticker]
        lead = max(sides, key=lambda m: (abs(m.change_pct), m.id or 0))
        if abs(lead.change_pct) < settings.min_move_pct:
            continue
        lead_row = _verdict(verdicts, side=lead.side, ticker=lead.ticker)
        if mover_is_not_equity(lead_row, not_equity):
            continue
        eps = episodes_by.get(ticker, [])
        if any(e.entered_at is not None for e in eps):
            continue
        if eps:
            chosen = max(eps, key=lambda e: (e.first_seen_at or datetime.min.replace(tzinfo=ET), e.id or 0))
            if chosen.excluded_by not in EPISODE_EXCLUSIONS:
                raise ReplayInputError(
                    f"{ticker}: never-admitted episode {chosen.id} carries excluded_by "
                    f"{chosen.excluded_by!r} — not one of {sorted(EPISODE_EXCLUSIONS)}"
                )
            excluded_by, member_id = chosen.excluded_by, chosen.id
        else:
            excluded_by, member_id = "not_in_any_source", None
        episode_json = [
            {"id": e.id, "entered_at": e.entered_at.isoformat() if e.entered_at else None,
             "first_seen_at": e.first_seen_at.isoformat() if e.first_seen_at else None,
             "excluded_by": e.excluded_by, "source": e.source}
            for e in sorted(eps, key=lambda e: (e.first_seen_at or datetime.min.replace(tzinfo=ET), e.id or 0),
                            reverse=True)
        ]
        # `unreported` is a blank CELL on a column that is present — the
        # ordinary case for a stock. A missing column never gets here.
        gate_detail = {
            "change_pct": str(lead.change_pct), "side": lead.side, "rank": lead.rank,
            "sides": sorted(m.side for m in sides),
            "asset_type": lead_row.asset_type if lead_row.asset_type is not None else "unreported",
            "industry": lead_row.industry if lead_row.industry is not None else "unreported",
            "min_move_pct": str(settings.min_move_pct), "episodes": episode_json,
        }
        rows_by_side = {
            m.side: _verdict(verdicts, side=m.side, ticker=m.ticker) for m in sides
        }
        inputs = {
            "trade_date": trade_date.isoformat(),
            "movers": [
                {"id": m.id, "side": m.side, "rank": m.rank, "ticker": m.ticker, "change_pct": str(m.change_pct),
                 "asset_type": rows_by_side[m.side].asset_type, "industry": rows_by_side[m.side].industry,
                 "volume": m.volume, "rvol": str(m.rvol) if m.rvol is not None else None,
                 "export_sha256": m.export_sha256, "fetched_at": m.fetched_at.isoformat()}
                for m in sorted(sides, key=lambda m: m.side)
            ],
            "episodes": episode_json,
            "settings": settings.row(),
            # The rule the desk names, AND the config value it compared
            # against: a receipt that dropped the deciding value would no
            # longer replay the decision it records (L57).
            "not_equity_rule": "asset_type_or_etf_industry",
            "not_equity_industry_values": list(not_equity.industry_values),
        }
        receipt = {"inputs": inputs, "outputs": {"excluded_by": excluded_by, "gate_detail": gate_detail}}
        rows.append(MissRow(
            trade_date=trade_date, kind="mover", ticker=ticker, pool_member_id=member_id, mover_id=lead.id,
            excluded_by=excluded_by, gate_detail=gate_detail, receipt=json.loads(canonical_json(receipt)),
            inputs_sha256=sha256_json(inputs),
        ))
    return rows


# ---------------------------------------------------------------------------
# The archive
# ---------------------------------------------------------------------------


@dataclass
class ArchiveOutcome:
    archived_ids: list[int] = field(default_factory=list)
    incomplete: list[str] = field(default_factory=list)
    failures: dict[str, str] = field(default_factory=dict)
    would_fetch: list[str] = field(default_factory=list)
    rows_written: int = 0


async def archive_movers(
    movers: Sequence[StoredMover],
    *,
    collector,
    bar_store,
    trade_date: date,
    rth_open: datetime,
    close: datetime,
    top_n: int,
    dry_run: bool,
    now: Optional[datetime] = None,
    deadline: Optional[datetime] = None,
    rpm: Optional[int] = None,
) -> ArchiveOutcome:
    """Archive i1 bars for every top-N mover not already covering the session.

    "Some bars that day" is not coverage (R1-12): the stored bars must span
    the RTH open to the close before a mover is marked archived, and a
    fetch that still leaves a gap is counted `incomplete`, never archived.
    Work that cannot finish before the deadline at the bucket's rate
    refuses before the first request (R1-16).
    """
    day_start = datetime.combine(trade_date, datetime.min.time(), tzinfo=ET)
    day_end = day_start + timedelta(days=1)
    outcome = ArchiveOutcome()
    ids_by_ticker: dict[str, list[int]] = {}
    for mover in movers:
        ids_by_ticker.setdefault(mover.ticker, []).append(mover.id)

    def covered(ticker: str) -> bool:
        stored = day_bars(
            bar_store.bars_in_range(
                None, ticker, Interval.I1, day_start, day_end,
                end_inclusive=False, as_bars=True),
            trade_date)
        return coverage(stored, start=rth_open, end=close)["covered"]

    to_fetch = []
    for ticker in ids_by_ticker:
        if covered(ticker):
            outcome.archived_ids.extend(i for i in ids_by_ticker[ticker] if i is not None)
        else:
            to_fetch.append(ticker)
    if dry_run:
        outcome.would_fetch = to_fetch
        return outcome
    if to_fetch and deadline is not None and now is not None and rpm:
        needed = timedelta(seconds=len(to_fetch) * 60 / rpm)
        if now + needed > deadline:
            raise ReplayError(
                f"movers archive: {len(to_fetch)} fetch(es) at {rpm} rpm need {needed}, past the "
                f"deadline {deadline.isoformat()} — refused before the first request"
            )
    if not to_fetch:
        return outcome
    fetched, failures = await collector.bars(to_fetch, top_n=top_n)
    outcome.failures.update(failures)
    for ticker in to_fetch:
        if ticker not in fetched:
            continue
        outcome.rows_written += bar_store.upsert_bars(fetched[ticker])
        if covered(ticker):
            outcome.archived_ids.extend(i for i in ids_by_ticker[ticker] if i is not None)
        else:
            outcome.incomplete.append(ticker)
    outcome.archived_ids.sort()
    return outcome


# ---------------------------------------------------------------------------
# SYSTEM side: system.movers_daily
# ---------------------------------------------------------------------------


class MoversStore:
    """`system.movers_daily`. ADR-0008 D2 — SYSTEM side: market data."""

    SIDE = DbSide.SYSTEM
    _COLUMNS = ("id, trade_date, side, rank, ticker, change_pct, asset_type, volume, rvol, "
                "export_sha256, fetched_at, bars_archived")

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def active(self, trade_date: date) -> list[StoredMover]:
        with self._connect() as conn:
            cur = conn.execute(
                f"SELECT {self._COLUMNS} FROM movers_daily WHERE trade_date = %s AND active "
                "ORDER BY side, rank", (trade_date,))
            return [StoredMover(**dict(zip([d.name for d in cur.description], r))) for r in cur.fetchall()]

    def reconcile(self, *, run_id: str, trade_date: date, exports: Sequence[MoversExport]) -> list[StoredMover]:
        """Make each export's top rows the ACTIVE set for its side, in one
        SYSTEM transaction. Unchanged rows stay; changed or dropped rows
        are deactivated (never deleted); new or changed rows are inserted."""
        conn = self._connect()
        conn.autocommit = False
        try:
            conn.execute("SELECT pg_advisory_xact_lock(hashtext(%s))", (f"replay:movers:{trade_date}",))
            for export in exports:
                cur = conn.execute(
                    "SELECT id, ticker, rank, change_pct, asset_type, volume, rvol, export_sha256 "
                    "FROM movers_daily WHERE trade_date = %s AND side = %s AND active FOR UPDATE",
                    (trade_date, export.side),
                )
                current = {r[1]: r for r in cur.fetchall()}
                wanted = {row.ticker: row for row in export.rows}
                stale = []
                for ticker, rec in current.items():
                    row = wanted.get(ticker)
                    same = row is not None and (
                        rec[2], rec[3], rec[4], rec[5], rec[6], rec[7]
                    ) == (row.rank, row.change_pct, row.asset_type, row.volume, row.rvol, export.export_sha256)
                    if same:
                        wanted.pop(ticker)
                    else:
                        stale.append(rec[0])
                if stale:
                    conn.execute("UPDATE movers_daily SET active = false WHERE id = ANY(%s)", (stale,))
                for row in wanted.values():
                    conn.execute(
                        "INSERT INTO movers_daily (trade_date, side, rank, ticker, change_pct, asset_type, "
                        "volume, rvol, export_sha256, fetched_at, replay_run_id) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (trade_date, export.side, row.rank, row.ticker, row.change_pct, row.asset_type,
                         row.volume, row.rvol, export.export_sha256, export.fetched_at, run_id),
                    )
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return self.active(trade_date)

    def mark_bars_archived(self, ids: Sequence[int]) -> None:
        if not ids:
            return
        with self._connect() as conn:
            conn.execute("UPDATE movers_daily SET bars_archived = true WHERE id = ANY(%s)", (list(ids),))
