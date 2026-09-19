"""Bar Archiver orchestration: the nightly full run and the on-demand
per-ticker backfill. Sequential, gentle rate, fail-loud per ticker —
one failure never aborts the run or gets silently skipped.

The database is not an argument anywhere in this module. `COBALT_ENV`
alone decides it (`cobalt.env.resolve_db_name()`, via `BarStore`) —
RULING 9 (2026-09-04). Before that this module threaded a
`db_name="cobalt_dev"` default through every entry point and exposed
it as a `--db-name` CLI flag, so the archiver kept writing PRODUCTION
bars into the dev database long after every other store had moved onto
the resolver. The flag is deleted rather than re-pointed: a per-run
override of the target database is exactly the hole RULING 7 closed
for `AsetConfig.db_name`.
"""

import asyncio
import sys

from loguru import logger

from . import incidents, progress, shadow
from .collector import CollectorError, fetch_bars, resolve_token
from .config import load_config
from .models import Interval
from .reconcile import IncidentDraft, IncidentKind, TargetStatus, plan_candidates, reconcile
from .report import RunSummary, append_run_report
from .settings import WriteMode, load_archiver_settings
from .store import BarStore

GENTLE_SLEEP_SECONDS = 1.2

#: The two tunables that name the premarket window R34 closed to the
#: backfill. Read, never hardcoded (L10): if Dejan moves the session, the
#: bound moves with it and the refusal message says so.
PREMARKET_OPEN_KEY = "session.premarket_open"
PREMARKET_CLOSE_KEY = "session.rth_open"

#: Minutes in a day, for the one place a backfill's window can run past
#: midnight and meet the NEXT morning's premarket.
_DAY_MINUTES = 1440


class BackfillWindowRefused(RuntimeError):
    """A manual backfill was invoked inside — or would run into — the
    premarket window that `cto-2026-09-19.md` §4 R34 "B" closed to it."""


def _premarket_window():
    """04:00-09:30 ET, from the session tunables."""
    from cobalt.radar.notes import DemandWindow
    from cobalt.taxonomy.loader import load_tunables

    tunables = load_tunables().by_key
    return DemandWindow.between(
        tunables[PREMARKET_OPEN_KEY].value, tunables[PREMARKET_CLOSE_KEY].value
    )


def _backfill_window(targets: list[tuple[str, Interval]], instant):
    """The window this backfill will ACTUALLY hold the transport for:
    `[instant, instant + len(targets) x GENTLE_SLEEP_SECONDS)` in ET.

    A manual backfill has no schedule, so before R34 it declared
    `window=None` — which `radar/notes.py` defines as UNBOUNDED and
    therefore counts against every other consumer's window, including
    the radar's 04:00 peak. It is not unbounded; it is bounded by the
    clock it was started on and by its own pacing bound, and that is
    what it now says. The conversion to whole minutes is
    `DemandWindow.from_at`, the same one the nightly `archiver`
    consumer's window is built with.
    """
    from cobalt.radar.notes import DemandWindow
    from cobalt.session.clock import SessionClock

    et = SessionClock.to_et(instant)
    seconds = max(1, round(len(targets) * GENTLE_SLEEP_SECONDS))
    return DemandWindow.from_at(f"{et.hour:02d}:{et.minute:02d}", seconds)


def _check_demand(targets: list[tuple[str, Interval]], mode: str, now=None):
    """L53 (S2-P4 R1-13/R2-5): the ONE shared total-demand gate, before
    the first request. The nightly run is the registry's `archiver`
    consumer, untouched by R34.

    A manual backfill is bounded TWICE, and both halves are the same
    fact stated to two audiences (`cto-2026-09-19.md` §4 R34 "B",
    2026-09-19 — the ruling that closed the archiver DevDoc's open
    deployment gate; the ceiling `radar.finviz_max_rpm` stays at 50 and
    is not read, written or reasoned about here):

    * it REFUSES, loudly, if the run would touch 04:00-09:30 ET — the
      premarket window, where the radar already holds the ceiling and
      where a throttle on a historically shared Finviz login costs a
      trading morning; and
    * it declares that same enforced interval as its `DemandWindow`, so
      the shared gate counts it where it really is instead of against
      every window at once.

    The two halves are written together on purpose: a declared window
    the runner did not enforce would be a lie to the demand model, and
    an enforced window the model never saw would leave the 04:00 peak
    exactly as overstated as `window=None` left it.
    """
    from cobalt.radar.notes import DemandConsumer, check_scheduled_demand

    if mode == "full":
        return check_scheduled_demand("archiver")

    instant = (now if now is not None else _now)()
    window = _backfill_window(targets, instant)
    premarket = _premarket_window()
    if window.overlaps(premarket) or window.end_min > _DAY_MINUTES + premarket.start_min:
        raise BackfillWindowRefused(
            f"REFUSED: the backfill is bounded out of {premarket.describe()} "
            f"(cto-2026-09-19.md §4 R34 \"B\") — this run would hold the "
            f"transport {window.describe()} for {len(targets)} request(s). "
            f"Start it outside the premarket window."
        )
    backfill = DemandConsumer(
        name="backfill", rpm=min(len(targets), 60 / GENTLE_SLEEP_SECONDS), window=window,
        basis=f"{len(targets)} request(s), pacing bound, {window.describe()}",
    )
    return check_scheduled_demand("backfill", extra=[backfill])


def _now():
    """The ONE system-clock read (`cobalt.session.clock.now_utc`).

    Imported inside the function so `reconcile` can stay clock-free and
    so a test can freeze the instant by passing `now=` rather than by
    patching a global.
    """
    from cobalt.session import clock

    return clock.now_utc()


def _trading_night(now):
    """The ET calendar date of `now` — the night an artifact is named for.

    Tribunal round 1, F6: this was `now.date()` on a UTC instant. The
    nightly run happens at 20:30 ET, which is already the NEXT UTC
    calendar day, so every artifact was named for the day after the
    trading night it recorded. Spec §5 writes
    `data/archiver-shadow/<YYYY-MM-DD>.jsonl` and names no timezone;
    resolved to ET here, which is the zone every other date in this
    system is stated in (sessions are defined in ET, storage is UTC).

    `SessionClock.to_et` is the conversion the codebase already has
    (`session/clock.py:262`) — a static method, so no config is loaded
    and no calendar is consulted, and it REFUSES a naive datetime rather
    than guessing a zone (ADR-0007).
    """
    from cobalt.session.clock import SessionClock

    return SessionClock.to_et(now).date()


async def _default_fetch(ticker, interval, token):
    """The real transport, behind the runner's `fetch=` test seam.

    A named wrapper rather than `fetch_bars` passed as a default value,
    because `test_finviz_consumers.py` scans this tree for `fetch_bars(`
    to build L53's TOTAL-DEMAND inventory. Handing the function around
    as a value would make this module invisible to that scan while it
    goes on sending exactly as many requests as before — a guard that
    stops seeing a consumer is worse than no guard.
    """
    return await fetch_bars(ticker, interval, token)


class _Withheld(Exception):
    """A target the comparison refused. Raised INSIDE the target's
    transaction so the `with` rolls it back; the evidence is persisted
    afterwards in a second, small transaction (Astra, V3-2)."""

    def __init__(self, plan):
        super().__init__(plan.reason)
        self.plan = plan


async def _run_targets(
    targets: list[tuple[str, Interval]],
    mode: str,
    *,
    store=None,
    fetch=None,
    settings=None,
    now=None,
) -> RunSummary:
    """One run over `targets`.

    `mode` is and stays the REPORT SCOPE ("full" / "backfill:<T>"). The
    WRITE mode is `archiver.write_mode`, a different name everywhere
    (§5) — and the dispatch on it happens BEFORE any append-specific
    step, which is Astra's rule: no new failure rule, no completeness
    cut, no range read may leak into an `upsert` night.

    `store` / `fetch` / `settings` / `now` are TEST seams, the same kind
    as `BarStore(db_name=…)`. Production passes none of them.

    S2-P4's L53 total-demand gate (`_check_demand`) stays the FIRST
    statement here, as it was before the write-mode dispatch landed:
    before the settings, before the store, before the lock, before the
    token — before anything that could send a request. The two changes
    are kept side by side by the 2026-09-19 rebase; neither is a choice
    against the other.
    """
    _check_demand(targets, mode, now=now)
    cfg = settings if settings is not None else load_archiver_settings()
    store = store if store is not None else BarStore()
    fetch_fn = fetch if fetch is not None else _default_fetch
    clock = now if now is not None else _now

    summary = RunSummary(mode=mode, write_mode=cfg.write_mode.value)

    # §9: the run-level advisory lock, in BOTH write modes. A second
    # archiver or a repair refuses loudly rather than interleaving.
    with store.run_lock(
        f"the archiver run ({mode}, write_mode={cfg.write_mode.value})"
    ):
        store.ensure_schema()
        token = await resolve_token()
        if cfg.write_mode is WriteMode.APPEND:
            await _append_targets(
                targets, store=store, fetch=fetch_fn, token=token,
                summary=summary, clock=clock,
            )
        else:
            await _upsert_targets(
                targets, store=store, fetch=fetch_fn, token=token,
                summary=summary, settings=cfg, clock=clock,
            )
    return summary


async def _upsert_targets(targets, *, store, fetch, token, summary, settings, clock) -> None:
    """TODAY'S NIGHT, unchanged: the whole export through `upsert_bars`.

    No completeness filter, no range cut, no comparison gate, no
    withholding, no new failure rule, no `archive_progress` write, no
    incident write, the same submitted-row count and the same run-report
    row. The ONLY additions are the lock (taken by the caller), the
    pre-write shadow read, and the `shadow` key plus its artifact.
    """
    total = len(targets)
    for i, (ticker, interval) in enumerate(targets, start=1):
        try:
            bars = await fetch(ticker, interval, token)
            if settings.shadow_enabled:
                _shadow_target(store, summary, ticker, interval, bars, settings, clock)
            rows = store.upsert_bars(bars)
            summary.record_success(ticker, rows)
            logger.info(f"[{i}/{total}] {ticker}/{interval.value}: {rows} rows")
        except CollectorError as e:
            summary.record_failure(ticker, interval.value, str(e))
            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {e}")
        except Exception as e:
            # Any other unexpected error is still a per-ticker failure,
            # never a reason to abort the whole run or store partial data.
            summary.record_failure(ticker, interval.value, f"{type(e).__name__}: {e}")
            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {type(e).__name__}: {e}")

        if i < total:
            await asyncio.sleep(GENTLE_SLEEP_SECONDS)

    if settings.shadow_enabled:
        summary.shadow = shadow.aggregate(
            summary.shadow_records, errors=summary.shadow_errors
        )
        if summary.shadow_records:
            path = shadow.write_records(
                summary.shadow_records,
                night=_trading_night(clock()),
                retention_nights=settings.shadow_retention_nights,
            )
            logger.info(f"shadow compare: {len(summary.shadow_records)} target(s) -> {path}")


def _shadow_target(store, summary, ticker, interval, bars, settings, clock) -> None:
    """The pre-write comparison. IT CAN NEVER FAIL A TARGET.

    Its own `try/except Exception` is what keeps a shadow defect out of
    the target's failure path — without it, a broken shadow would turn
    every target red and the night would look like a data outage.
    """
    try:
        archived_through = None
        record = shadow.observe(
            store, ticker=ticker, interval=interval, bars=bars,
            fetch_started_at=clock(), settings=settings,
            archived_through=archived_through,
        )
        summary.shadow_records.append(record)
    except Exception as e:  # noqa: BLE001 — deliberate: see the docstring
        summary.shadow_errors += 1
        logger.warning(
            f"shadow compare for {ticker}/{interval.value} failed and was "
            f"ignored: {type(e).__name__}: {e}"
        )


async def _append_targets(targets, *, store, fetch, token, summary, clock) -> None:
    """THE APPEND NIGHT (§6, §7). One transaction per target (§4)."""
    total = len(targets)
    for i, (ticker, interval) in enumerate(targets, start=1):
        fetch_started_at = clock()
        try:
            bars = await fetch(ticker, interval, token)
        except CollectorError as e:
            # Today's behaviour, kept: the collector fails a whole target
            # on an empty response, a header-only response or one bad
            # row. In `append` mode the target additionally gets an
            # `empty_export` incident so the heartbeat sees it (§7).
            summary.record_failure(ticker, interval.value, str(e))
            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {e}")
            _persist_incidents(
                store,
                [
                    IncidentDraft(
                        kind=IncidentKind.EMPTY_EXPORT,
                        ticker=ticker,
                        interval=interval.value,
                        detail={
                            "collector_error": str(e),
                            "fetch_started_at": fetch_started_at.isoformat(),
                        },
                    )
                ],
                run_id=summary.run_id,
                now=clock(),
            )
        except Exception as e:
            summary.record_failure(ticker, interval.value, f"{type(e).__name__}: {e}")
            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {type(e).__name__}: {e}")
        else:
            _append_one(
                store, summary, ticker, interval, bars, fetch_started_at, clock, i, total
            )

        if i < total:
            await asyncio.sleep(GENTLE_SLEEP_SECONDS)


def _append_one(store, summary, ticker, interval, bars, fetch_started_at, clock, i, total) -> None:
    try:
        with store.target_transaction() as conn:
            archived_through = progress.read_archived_through(conn, ticker, interval)
            plan = plan_candidates(
                ticker=ticker, interval=interval, bars=bars,
                fetch_started_at=fetch_started_at, archived_through=archived_through,
            )
            stored = (
                store.bars_in_range(
                    conn, ticker, interval, plan.range_start, plan.range_end
                )
                if plan.needs_stored_read
                else {}
            )
            outcome = reconcile(plan, stored)
            if outcome.archived_through_after is None:
                raise _Withheld(outcome)

            inserted = store.insert_new_bars(conn, list(outcome.to_insert))
            conflicts = len(outcome.to_insert) - inserted
            if conflicts < 0:
                raise RuntimeError(
                    f"{ticker}/{interval.value}: the server reported {inserted} "
                    f"insert(s) for {len(outcome.to_insert)} offered key(s) — "
                    "the counters cannot reconcile (L57)."
                )
            now = clock()
            # A `gap` incident is persisted BEFORE progress advances (§7):
            # the window between the old watermark and this export's
            # oldest bar must be on the record before the watermark moves
            # past it.
            for draft in outcome.incidents:
                incidents.open_or_refresh(conn, draft, run_id=summary.run_id, now=now)
            progress.upsert_progress(
                conn, plan=outcome, run_id=summary.run_id, now=now
            )
            counts = outcome.counts(inserted=inserted, concurrent_conflicts=conflicts)
    except _Withheld as withheld:
        # The transaction is already rolled back. The evidence goes in a
        # SECOND small transaction, or it dies with the one that failed.
        outcome = withheld.plan
        summary.record_append_failure(ticker, interval.value, outcome)
        _persist_incidents(
            store, outcome.incidents, run_id=summary.run_id, now=clock()
        )
        logger.error(
            f"[{i}/{total}] {ticker}/{interval.value}: {outcome.status.value.upper()} "
            f"— {outcome.reason}"
        )
        return
    except Exception as e:
        summary.record_failure(ticker, interval.value, f"{type(e).__name__}: {e}")
        logger.error(
            f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {type(e).__name__}: {e}"
        )
        return

    summary.record_append(ticker, outcome, counts)
    level = logger.info if outcome.status is TargetStatus.SUCCESS else logger.warning
    level(
        f"[{i}/{total}] {ticker}/{interval.value}: {outcome.status.value} — "
        f"{counts.inserted} inserted, {counts.concurrent_conflicts} conflict(s), "
        f"{outcome.reason}"
    )


def _persist_incidents(store, drafts, *, run_id: str, now) -> None:
    """A SECOND transaction, for evidence whose own one was rolled back.

    Its failure is logged and swallowed: losing the incident row is bad,
    losing the run because the incident row could not be written is
    worse, and the target has already been recorded as failed.
    """
    if not drafts:
        return
    try:
        with store.target_transaction() as conn:
            for draft in drafts:
                incidents.open_or_refresh(conn, draft, run_id=run_id, now=now)
    except Exception as e:  # noqa: BLE001
        logger.error(f"could not persist archive incident(s): {type(e).__name__}: {e}")


async def run_full() -> RunSummary:
    """Nightly job: archive every enabled Lists-note archive target.

    Writes to whichever database `COBALT_ENV` names (RULING 9)."""
    cfg = load_config()
    targets = cfg.archive_targets()
    logger.info(f"Bar Archiver full run: {len(targets)} (ticker, interval) targets")
    summary = await _run_targets(targets, mode="full")
    path = append_run_report(summary)
    logger.info(
        f"Run complete: {len(summary.tickers)} tickers, {summary.rows_written} rows, "
        f"{len(summary.failures)} failures, {summary.duration_str()}. Report: {path}"
    )
    return summary


async def run_backfill(ticker: str) -> RunSummary:
    """On-demand: fetch the Lists note's backfill-default intervals.

    Same database rule as `run_full` — `COBALT_ENV`, never an argument.
    """
    cfg = load_config()
    targets = cfg.backfill_targets(ticker)
    logger.info(f"Bar Archiver backfill for {ticker}: {len(targets)} targets")
    summary = await _run_targets(targets, mode=f"backfill:{ticker}")
    path = append_run_report(summary)
    logger.info(
        f"Backfill complete: {summary.rows_written} rows, "
        f"{len(summary.failures)} failures, {summary.duration_str()}. Report: {path}"
    )
    return summary


def _archive_nightly() -> None:
    """The scheduled nightly run, inside its F17 job row.

    Only the FULL run is the job. A `--backfill TICKER` is an operator
    fetching one symbol on demand; recording it as the nightly run would
    mark the night satisfied and silence the MISSED probe for a run that
    never happened.
    """
    from cobalt.jobs.entrypoint import as_job

    with as_job("com.cobalt.archiver") as job:
        summary = asyncio.run(run_full())
        # THIS is what makes F18's "archiver freshness (last run + rows
        # written)" answerable without a second table. `job_result()`
        # returns today's five keys, plus `shadow` when the pre-write
        # comparison ran and `append` in append mode (§5).
        job.result = summary.job_result()
        if summary.failures:
            # Raised, so the job row lands on `failed` with its exit code
            # and its error text — F18 turns red on exactly this.
            raise RuntimeError(
                f"{len(summary.failures)} archiver failure(s): "
                + "; ".join(summary.failures[:5])
            )
        if not summary.healthy:
            # V2-9: a DEGRADED target — a gap whose usable range was
            # still appended, or stored keys the download did not carry —
            # is not a failure of the run, but the night is NOT healthy
            # and the job row must say so rather than reporting green.
            raise RuntimeError(
                f"{summary.degraded_targets} DEGRADED archiver target(s) — "
                f"{summary.gap_targets} gap(s). See `cobalt archiver incidents`."
            )


def main() -> None:
    import os

    # Same rationale as aset/__main__.py: the old tree's config loader
    # used to dump vault secrets at DEBUG on import (fixed at the source
    # 2026-08-24; this is cheap standing insurance, left in place).
    os.environ.setdefault("LOGURU_LEVEL", "INFO")

    import argparse

    parser = argparse.ArgumentParser(prog="archiver", description="Cobalt Bar Archiver")
    parser.add_argument(
        "--backfill",
        metavar="TICKER",
        help="Fetch the backfill-default intervals for one ticker instead of the full nightly run.",
    )
    args = parser.parse_args()

    from cobalt.jobs.entrypoint import JobStopped

    if args.backfill:
        summary = asyncio.run(run_backfill(args.backfill))
        if summary.failures:
            sys.exit(1)
        return

    try:
        _archive_nightly()
    except JobStopped as e:
        # Exit 0: a deliberate stop is not a failure (F17d).
        print(f"NOT RUN — {e}")
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
