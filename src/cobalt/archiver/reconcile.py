"""The append-only night's DECISIONS, as pure functions.

Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md`
§3 (V2-3 completeness), §4 (progress and the candidate range), §6 (the
four-way comparison and withholding), §7 (gaps, empty exports,
regression, and the counting identities).

NOTHING HERE PERFORMS I/O. No database, no network, no file, and — the
one that keeps this testable at all — no clock: the fetch instant is an
argument. The store fetches, the runner calls these functions, and only
then does anything get written. A test asserts this module's source
carries none of those names.

WHY A SEPARATE WATERMARK AT ALL. `BarStore.watermark()` is `max(ts)`
over `system.bars`, and the radar poller writes that table too. The
poller keeps only bars newer than (its watermark − overlap), so a bar
that was ABSENT at poll time and appears LATER — a vendor restoration, a
late print — is dropped by the poller while `max(ts)` moves on without
it. Three houses produced the same sequence independently (Gemini's
Monday 14:00 restoration, Astra's Friday 10:02 addition, Grok's NVDA
Wednesday 10:17), and the same fact defeats a `max(ts)` gap test
(MSFT 08-27/09-04; AAPL re-added). So `archived_through` is the
archiver's own record, and the poller's maximum is REPORTED beside the
counters and used by nothing.

WHAT THE WATERMARK CLAIMS, AND WHAT IT DOES NOT. `archived_through` is
the `ts` — the bar OPEN, UTC — of the newest COMPLETE bar of an
ACCEPTED export. It records that the AVAILABLE export was processed
through that key. It does not claim the vendor supplied every bar, and
the report never says so: that is Known limit 5 (the newest-timestamp
check cannot detect interior or prefix truncation).

EVERY COUNT RECONCILES OR THE OBJECT CANNOT BE BUILT (L57).
`TargetCounts` carries the spec's identities in its own validator, so a
night whose numbers do not add up raises instead of rendering.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from enum import Enum
from typing import Mapping, NamedTuple
from zoneinfo import ZoneInfo

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .models import Bar, Interval

#: Sessions, and therefore session DATES, are defined in ET and nowhere
#: else (ADR-0007, and `cobalt.session.clock`'s own rule). Imported as a
#: zone rather than through the session clock because this module must
#: stay free of config reads — the calendar is not needed here: a
#: weekend or a holiday is simply a date the export does not carry.
ET = ZoneInfo("America/New_York")

#: §3 V2-3: the explicit interval -> duration map. An unknown interval
#: FAILS LOUD; there is no "assume one minute".
INTERVAL_MINUTES: dict[Interval, int] = {
    Interval.I1: 1,
    Interval.I2: 2,
    Interval.I5: 5,
    Interval.I15: 15,
    Interval.I30: 30,
}

#: §4, range (b): the current day plus this many most recent COMPLETED
#: trading sessions that the export actually carries. Two, not one,
#: because the houses showed one is not enough (a Friday→Monday
#: boundary loses the Friday additions Astra's sequence turns on).
STEADY_STATE_SESSIONS = 2

#: `system.bars` stores prices `NUMERIC(14, 4)` and volume `BIGINT`.
#: Equality is decided AFTER normalising to those, so `100.0` from the
#: vendor and `100.0000` from storage are the same bar, not a
#: restatement that withholds a target for a whole night.
PRICE_QUANTUM = Decimal("0.0001")

#: The wording §7 requires on a gap, verbatim, so the report and the
#: incident cannot drift apart.
GAP_WORDING = "unavailable from the tested export interface"


class ReconcileError(RuntimeError):
    """An input this module cannot reason about. Never a default."""


class IncidentKind(str, Enum):
    """The five kinds of `system.archive_incidents` (§11).

    Defined here, beside the decisions that raise them, and imported by
    the writer — one definition, not two (L3).
    """

    GAP = "gap"
    RESTATED = "restated"
    STORED_ONLY = "stored_only"
    EMPTY_EXPORT = "empty_export"
    REGRESSION = "regression"


class TargetStatus(str, Enum):
    """§7. FAILED = `restated`, `regression`, `empty_export`, any
    exception. DEGRADED = a `gap` with its usable range inserted, or
    `stored_only` keys seen. `inserted = 0` because everything was
    already stored is SUCCESS, not a failure."""

    SUCCESS = "success"
    DEGRADED = "degraded"
    FAILED = "failed"


# ---------------------------------------------------------------------
# Time and completeness (§3 V2-3)
# ---------------------------------------------------------------------


def interval_duration(interval: object) -> timedelta:
    """One bar's length. Fails loud on anything not in the map."""
    try:
        minutes = INTERVAL_MINUTES[interval]  # type: ignore[index]
    except (KeyError, TypeError):
        raise ReconcileError(
            f"unknown interval {interval!r} — the archiver's completeness rule "
            f"needs an explicit duration and has none for it. Known: "
            f"{sorted(i.value for i in INTERVAL_MINUTES)}."
        ) from None
    return timedelta(minutes=minutes)


def _require_aware(ts: object, what: str) -> datetime:
    if not isinstance(ts, datetime) or ts.tzinfo is None or ts.utcoffset() is None:
        raise ReconcileError(
            f"REFUSED: {what} must be a tz-aware datetime, got {ts!r}. A naive "
            "value has no instant, and guessing the zone is the defect ADR-0007 "
            "had to undo across 4.75M bars."
        )
    return ts


def bar_closes_at(ts: datetime, interval: Interval) -> datetime:
    """A bar's `ts` is its OPEN; it closes one duration later."""
    return _require_aware(ts, "a bar timestamp") + interval_duration(interval)


def is_complete(ts: datetime, interval: Interval, fetch_started_at: datetime) -> bool:
    """§3 V2-3: eligible only when `ts + duration <= fetch_started_at`.

    `fetch_started_at` is captured BEFORE the request, so a bar that
    closes while the response is in flight is not eligible tonight. That
    makes the rule replayable: the same export and the same instant
    always select the same bars.
    """
    return bar_closes_at(ts, interval) <= _require_aware(
        fetch_started_at, "the fetch instant"
    )


def et_date(ts: datetime) -> date:
    """The America/New_York calendar date `ts` belongs to."""
    return _require_aware(ts, "a bar timestamp").astimezone(ET).date()


# ---------------------------------------------------------------------
# Normalisation (§6)
# ---------------------------------------------------------------------


def normalise_price(value: object) -> Decimal:
    """To `NUMERIC(14, 4)`, the column's own shape."""
    try:
        return Decimal(str(value)).quantize(PRICE_QUANTUM)
    except Exception as e:  # noqa: BLE001 - any unparseable value is loud
        raise ReconcileError(f"price {value!r} cannot be normalised: {e}") from e


def normalise_volume(value: object) -> int:
    try:
        return int(Decimal(str(value)))
    except Exception as e:  # noqa: BLE001
        raise ReconcileError(f"volume {value!r} cannot be normalised: {e}") from e


class BarValues(NamedTuple):
    """One bar's OHLCV, normalised. What equality is decided on."""

    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int

    def as_strings(self) -> dict[str, str]:
        return {
            "open": str(self.open),
            "high": str(self.high),
            "low": str(self.low),
            "close": str(self.close),
            "volume": str(self.volume),
        }


FIELD_ORDER = ("open", "high", "low", "close", "volume")


def bar_values(source: object) -> BarValues:
    """Normalised OHLCV of a `Bar`, or of anything with those five
    attributes (a database row wrapper, in the store)."""
    return BarValues(
        open=normalise_price(getattr(source, "open")),
        high=normalise_price(getattr(source, "high")),
        low=normalise_price(getattr(source, "low")),
        close=normalise_price(getattr(source, "close")),
        volume=normalise_volume(getattr(source, "volume")),
    )


def values_from_row(row) -> BarValues:
    """The same thing from a positional `(open, high, low, close, volume)`
    row, which is how the store hands over what it read."""
    o, h, low_, c, v = row
    return BarValues(
        open=normalise_price(o),
        high=normalise_price(h),
        low=normalise_price(low_),
        close=normalise_price(c),
        volume=normalise_volume(v),
    )


# ---------------------------------------------------------------------
# Splitting an export into what is eligible (§3 V2-3, §7)
# ---------------------------------------------------------------------


class Eligibility(BaseModel):
    """What an export contains, split the way §7's identity counts it."""

    model_config = ConfigDict(frozen=True, extra="forbid", arbitrary_types_allowed=True)

    fetched: int = Field(ge=0)
    invalid: int = Field(ge=0)
    duplicate_input_keys: int = Field(ge=0)
    incomplete: int = Field(ge=0)
    eligible: tuple[Bar, ...] = ()
    raw_oldest: datetime | None = None
    raw_newest: datetime | None = None
    export_oldest: datetime | None = None
    export_newest: datetime | None = None


def split_export(
    bars: list[Bar], interval: Interval, fetch_started_at: datetime
) -> Eligibility:
    """Duplicates, then completeness. Bounds over ELIGIBLE bars only.

    `invalid` is 0 by construction while the collector fails a whole
    target on one bad row (`collector.py:146-170`); the counter exists so
    §7's identity survives a collector that one day returns partials.
    """
    _require_aware(fetch_started_at, "the fetch instant")
    seen: set[datetime] = set()
    eligible: list[Bar] = []
    duplicates = 0
    incomplete = 0
    raw: list[datetime] = []

    for item in bars:
        raw.append(item.ts)
        if item.ts in seen:
            duplicates += 1
            continue
        seen.add(item.ts)
        if not is_complete(item.ts, interval, fetch_started_at):
            incomplete += 1
            continue
        eligible.append(item)

    eligible.sort(key=lambda b: b.ts)
    keys = [b.ts for b in eligible]
    return Eligibility(
        fetched=len(bars),
        invalid=0,
        duplicate_input_keys=duplicates,
        incomplete=incomplete,
        eligible=tuple(eligible),
        raw_oldest=min(raw) if raw else None,
        raw_newest=max(raw) if raw else None,
        export_oldest=keys[0] if keys else None,
        export_newest=keys[-1] if keys else None,
    )


# ---------------------------------------------------------------------
# The candidate range (§4)
# ---------------------------------------------------------------------


def steady_state_dates(bars, fetch_started_at: datetime) -> tuple[date, ...]:
    """Range (b): the current ET day plus the `STEADY_STATE_SESSIONS`
    most recent COMPLETED session dates the export carries.

    Sessions are America/New_York calendar DATES PRESENT IN THE EXPORT —
    no 24-hour arithmetic. A weekend, a holiday and a half day need no
    special case: a weekend simply has no date, and a half day has one
    that ends early. That is why this function needs no calendar.
    """
    today = et_date(_require_aware(fetch_started_at, "the fetch instant"))
    present = sorted({et_date(b.ts) for b in bars})
    completed = [d for d in present if d < today]
    return tuple(sorted(set(completed[-STEADY_STATE_SESSIONS:]) | {today}))


class CandidatePlan(BaseModel):
    """Everything decided BEFORE the stored rows are read.

    The store read is bounded by this plan, which is why it is a
    separate object: one read of the candidate range per target (§6).
    """

    model_config = ConfigDict(frozen=True, extra="forbid", arbitrary_types_allowed=True)

    ticker: str
    interval: Interval
    fetch_started_at: datetime
    bootstrap: bool
    archived_through_before: datetime | None
    candidates: tuple[Bar, ...]
    range_dates: tuple[date, ...]
    below_range: int = Field(ge=0)
    eligibility: Eligibility

    @property
    def needs_stored_read(self) -> bool:
        """An empty or regressed export is refused before any read."""
        return not self.refusal and bool(self.candidates)

    @property
    def refusal(self) -> IncidentKind | None:
        if not self.eligibility.eligible:
            return IncidentKind.EMPTY_EXPORT
        if (
            self.archived_through_before is not None
            and self.eligibility.export_newest is not None
            and self.eligibility.export_newest < self.archived_through_before
        ):
            return IncidentKind.REGRESSION
        return None

    @property
    def range_start(self) -> datetime | None:
        """The oldest key the store read must cover."""
        return self.candidates[0].ts if self.candidates else None

    @property
    def range_end(self) -> datetime | None:
        return self.candidates[-1].ts if self.candidates else None


def plan_candidates(
    *,
    ticker: str,
    interval: Interval,
    bars: list[Bar],
    fetch_started_at: datetime,
    archived_through: datetime | None = None,
) -> CandidatePlan:
    """§4's candidate range: the UNION of

      (a) every eligible bar with `ts > archived_through`, and
      (b) every eligible bar whose ET date is in `steady_state_dates`.

    NO PROGRESS ROW IS A BOOTSTRAP: every eligible key of the available
    export is reconciled once, regardless of rows the poller already
    stored. Range (b) is what catches a bar the vendor adds BELOW the
    watermark — the case a `max(ts)` watermark loses.
    """
    split = split_export(bars, interval, fetch_started_at)
    bootstrap = archived_through is None
    if archived_through is not None:
        _require_aware(archived_through, "archived_through")

    if bootstrap:
        candidates = split.eligible
        dates = steady_state_dates(split.eligible, fetch_started_at)
    else:
        dates = steady_state_dates(split.eligible, fetch_started_at)
        date_set = set(dates)
        candidates = tuple(
            b
            for b in split.eligible
            if b.ts > archived_through or et_date(b.ts) in date_set
        )

    return CandidatePlan(
        ticker=ticker,
        interval=interval,
        fetch_started_at=fetch_started_at,
        bootstrap=bootstrap,
        archived_through_before=archived_through,
        candidates=candidates,
        range_dates=dates,
        below_range=len(split.eligible) - len(candidates),
        eligibility=split,
    )


# ---------------------------------------------------------------------
# The four-way comparison (§6)
# ---------------------------------------------------------------------


class FieldDifference(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    field: str
    stored: str
    vendor: str


class KeyDifference(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    ts: datetime
    fields: tuple[FieldDifference, ...]

    def as_detail(self) -> dict:
        return {
            "ts": self.ts.isoformat(),
            "fields": [f.model_dump() for f in self.fields],
        }


class Comparison(BaseModel):
    """The four ways a key can land (§6). Nothing here decides anything —
    the decision is `reconcile`'s."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    equal: tuple[datetime, ...] = ()
    differing: tuple[KeyDifference, ...] = ()
    incoming_only: tuple[datetime, ...] = ()
    stored_only: tuple[datetime, ...] = ()


def compare(candidates, stored: Mapping[datetime, BarValues]) -> Comparison:
    """`candidates` are the vendor's bars over the candidate range;
    `stored` is what the database holds OVER THAT SAME RANGE.

    Equality is decided on normalised values, so a difference is a real
    restatement rather than a rendering of the same number.
    """
    equal: list[datetime] = []
    differing: list[KeyDifference] = []
    incoming_only: list[datetime] = []
    incoming_keys = set()

    for item in candidates:
        incoming_keys.add(item.ts)
        held = stored.get(item.ts)
        if held is None:
            incoming_only.append(item.ts)
            continue
        vendor = bar_values(item)
        if vendor == held:
            equal.append(item.ts)
            continue
        fields = tuple(
            FieldDifference(
                field=name,
                stored=held.as_strings()[name],
                vendor=vendor.as_strings()[name],
            )
            for name in FIELD_ORDER
            if getattr(held, name) != getattr(vendor, name)
        )
        differing.append(KeyDifference(ts=item.ts, fields=fields))

    stored_only = tuple(sorted(k for k in stored if k not in incoming_keys))
    return Comparison(
        equal=tuple(sorted(equal)),
        differing=tuple(sorted(differing, key=lambda d: d.ts)),
        incoming_only=tuple(sorted(incoming_only)),
        stored_only=stored_only,
    )


# ---------------------------------------------------------------------
# The counters (§7) — the identities live in the model
# ---------------------------------------------------------------------


class TargetCounts(BaseModel):
    """One target's numbers, which RECONCILE or the object does not exist.

    The identities, verbatim from §7:

        fetched = invalid + duplicate_input_keys + incomplete
                  + below_range + candidates
        candidates = already_stored_equal + differing + incoming_only
        incoming_only = new + late
        WITHHELD: withheld = incoming_only, inserted = 0,
                  concurrent_conflicts = 0
        otherwise: withheld = 0,
                   incoming_only = inserted + concurrent_conflicts

    `stored_only` is reported BESIDE the identities: its keys are not
    candidates, so folding it in would make the arithmetic lie.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    fetched: int = Field(ge=0)
    invalid: int = Field(ge=0)
    duplicate_input_keys: int = Field(ge=0)
    incomplete: int = Field(ge=0)
    below_range: int = Field(ge=0)
    candidates: int = Field(ge=0)
    already_stored_equal: int = Field(ge=0)
    differing: int = Field(ge=0)
    incoming_only: int = Field(ge=0)
    new: int = Field(ge=0)
    late: int = Field(ge=0)
    withheld: int = Field(ge=0)
    inserted: int = Field(ge=0)
    concurrent_conflicts: int = Field(ge=0)
    stored_only: int = Field(ge=0)

    @model_validator(mode="after")
    def _identities(self) -> "TargetCounts":
        parts = (
            self.invalid + self.duplicate_input_keys + self.incomplete
            + self.below_range + self.candidates
        )
        if self.fetched != parts:
            raise ValueError(
                f"fetched ({self.fetched}) != invalid + duplicate_input_keys + "
                f"incomplete + below_range + candidates ({parts})"
            )
        split = self.already_stored_equal + self.differing + self.incoming_only
        if self.candidates != split:
            raise ValueError(
                f"candidates ({self.candidates}) != already_stored_equal + "
                f"differing + incoming_only ({split})"
            )
        if self.incoming_only != self.new + self.late:
            raise ValueError(
                f"incoming_only ({self.incoming_only}) != new + late "
                f"({self.new + self.late})"
            )
        if self.withheld:
            if self.withheld != self.incoming_only:
                raise ValueError(
                    f"a WITHHELD target withholds every incoming-only key: "
                    f"withheld ({self.withheld}) != incoming_only "
                    f"({self.incoming_only})"
                )
            if self.inserted or self.concurrent_conflicts:
                raise ValueError(
                    "a WITHHELD target inserts nothing: inserted "
                    f"({self.inserted}) and concurrent_conflicts "
                    f"({self.concurrent_conflicts}) must both be 0"
                )
        else:
            written = self.inserted + self.concurrent_conflicts
            if self.incoming_only != written:
                raise ValueError(
                    f"incoming_only ({self.incoming_only}) != inserted + "
                    f"concurrent_conflicts ({written}) — every offered key is "
                    "either committed by this run or lost the race to the "
                    "poller; neither is allowed to go unaccounted for"
                )
        return self


# ---------------------------------------------------------------------
# The decision (§6, §7)
# ---------------------------------------------------------------------


class IncidentDraft(BaseModel):
    """What the writer will persist. Pure data — no id, no clock."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    kind: IncidentKind
    ticker: str
    interval: str
    range_start: datetime | None = None
    range_end: datetime | None = None
    detail: dict = Field(default_factory=dict)


class TargetPlan(BaseModel):
    """One target's decided night, before anything is written."""

    model_config = ConfigDict(frozen=True, extra="forbid", arbitrary_types_allowed=True)

    ticker: str
    interval: Interval
    bootstrap: bool
    status: TargetStatus
    reason: str
    fetch_started_at: datetime
    archived_through_before: datetime | None
    archived_through_after: datetime | None
    to_insert: tuple[Bar, ...] = ()
    withheld: int = Field(default=0, ge=0)
    incidents: tuple[IncidentDraft, ...] = ()
    differences: tuple[KeyDifference, ...] = ()
    stored_only_keys: tuple[datetime, ...] = ()
    export_oldest: datetime | None = None
    export_newest: datetime | None = None
    raw_export_oldest: datetime | None = None
    raw_export_newest: datetime | None = None
    unassessed_before: datetime | None = None
    stored_rows_read: int = Field(default=0, ge=0)
    range_dates: tuple[date, ...] = ()
    #: Reported, never used in a decision (§4, §7).
    poller_watermark: datetime | None = None

    #: Filled by `reconcile`; the raw material of `counts()`.
    fetched: int = Field(default=0, ge=0)
    invalid: int = Field(default=0, ge=0)
    duplicate_input_keys: int = Field(default=0, ge=0)
    incomplete: int = Field(default=0, ge=0)
    below_range: int = Field(default=0, ge=0)
    candidates: int = Field(default=0, ge=0)
    already_stored_equal: int = Field(default=0, ge=0)
    differing: int = Field(default=0, ge=0)
    incoming_only: int = Field(default=0, ge=0)
    new: int = Field(default=0, ge=0)
    late: int = Field(default=0, ge=0)

    @property
    def healthy(self) -> bool:
        """§7 / V2-9: any FAILED or DEGRADED target makes the nightly
        job's result not healthy."""
        return self.status is TargetStatus.SUCCESS

    def counts(self, *, inserted: int, concurrent_conflicts: int) -> TargetCounts:
        """The validated counters, once the write is known.

        There is no way to build these numbers except through here, and
        `TargetCounts` refuses a set that does not reconcile — so a night
        that cannot explain itself raises rather than renders (L57, L1).
        """
        return TargetCounts(
            fetched=self.fetched,
            invalid=self.invalid,
            duplicate_input_keys=self.duplicate_input_keys,
            incomplete=self.incomplete,
            below_range=self.below_range,
            candidates=self.candidates,
            already_stored_equal=self.already_stored_equal,
            differing=self.differing,
            incoming_only=self.incoming_only,
            new=self.new,
            late=self.late,
            withheld=self.withheld,
            inserted=inserted,
            concurrent_conflicts=concurrent_conflicts,
            stored_only=len(self.stored_only_keys),
        )


def _base_fields(plan: CandidatePlan, stored_rows_read: int, poller_watermark) -> dict:
    split = plan.eligibility
    return {
        "ticker": plan.ticker,
        "interval": plan.interval,
        "bootstrap": plan.bootstrap,
        "fetch_started_at": plan.fetch_started_at,
        "archived_through_before": plan.archived_through_before,
        "export_oldest": split.export_oldest,
        "export_newest": split.export_newest,
        "raw_export_oldest": split.raw_oldest,
        "raw_export_newest": split.raw_newest,
        "range_dates": plan.range_dates,
        "stored_rows_read": stored_rows_read,
        "poller_watermark": poller_watermark,
        "fetched": split.fetched,
        "invalid": split.invalid,
        "duplicate_input_keys": split.duplicate_input_keys,
        "incomplete": split.incomplete,
        "below_range": plan.below_range,
        "candidates": len(plan.candidates),
    }


def reconcile(
    plan: CandidatePlan,
    stored: Mapping[datetime, BarValues],
    *,
    poller_watermark: datetime | None = None,
) -> TargetPlan:
    """The whole of §6 and §7 for one target, as one function (L3).

    `stored` is what the database holds over `plan`'s candidate range.
    For a refused plan (`empty_export`, `regression`) it is ignored: the
    refusal is decided before any read, which is why a failed target
    costs no query.
    """
    base = _base_fields(plan, len(stored), poller_watermark)
    split = plan.eligibility

    # ---- refusals decided before any read ---------------------------
    refusal = plan.refusal
    if refusal is IncidentKind.EMPTY_EXPORT:
        rows = split.fetched
        return TargetPlan(
            **{**base, "candidates": 0, "below_range": 0},
            status=TargetStatus.FAILED,
            reason=(
                "empty export — the download carried no eligible complete bar "
                f"({rows} row(s) fetched, {split.incomplete} incomplete). "
                "Progress is unchanged and the next non-empty night still "
                "bootstraps."
            ),
            archived_through_after=None,
            incidents=(
                IncidentDraft(
                    kind=IncidentKind.EMPTY_EXPORT,
                    ticker=plan.ticker,
                    interval=plan.interval.value,
                    detail={
                        "fetched": rows,
                        "incomplete": split.incomplete,
                        "duplicate_input_keys": split.duplicate_input_keys,
                        "fetch_started_at": plan.fetch_started_at.isoformat(),
                        "raw_newest": split.raw_newest.isoformat() if split.raw_newest else None,
                    },
                ),
            ),
        )

    if refusal is IncidentKind.REGRESSION:
        before = plan.archived_through_before
        newest = split.export_newest
        return TargetPlan(
            **{**base, "candidates": 0, "below_range": len(split.eligible)},
            status=TargetStatus.FAILED,
            reason=(
                f"regression — the export's newest eligible bar ({newest.isoformat()}) "
                f"is strictly older than archived_through ({before.isoformat()}). "
                "Progress is unchanged; this observation never becomes the baseline."
            ),
            archived_through_after=None,
            incidents=(
                IncidentDraft(
                    kind=IncidentKind.REGRESSION,
                    ticker=plan.ticker,
                    interval=plan.interval.value,
                    range_start=newest,
                    range_end=before,
                    detail={
                        "export_newest": newest.isoformat(),
                        "export_oldest": split.export_oldest.isoformat(),
                        "archived_through": before.isoformat(),
                        "raw_export_newest": (
                            split.raw_newest.isoformat() if split.raw_newest else None
                        ),
                        "fetch_started_at": plan.fetch_started_at.isoformat(),
                    },
                ),
            ),
        )

    # ---- the comparison ---------------------------------------------
    result = compare(plan.candidates, stored)
    incidents: list[IncidentDraft] = []

    # GAP is persisted BEFORE progress advances (§7), so it is recorded
    # first whatever happens below.
    gap = (
        not plan.bootstrap
        and split.export_oldest is not None
        and plan.archived_through_before is not None
        and split.export_oldest > plan.archived_through_before
    )
    if gap:
        incidents.append(
            IncidentDraft(
                kind=IncidentKind.GAP,
                ticker=plan.ticker,
                interval=plan.interval.value,
                range_start=plan.archived_through_before,
                range_end=split.export_oldest,
                detail={
                    "wording": GAP_WORDING,
                    "suspected_unavailable": True,
                    "proven_missing": False,
                    "archived_through": plan.archived_through_before.isoformat(),
                    "export_oldest": split.export_oldest.isoformat(),
                    "export_newest": split.export_newest.isoformat(),
                    "session_dates": [d.isoformat() for d in plan.range_dates],
                },
            )
        )

    if result.stored_only:
        incidents.append(
            IncidentDraft(
                kind=IncidentKind.STORED_ONLY,
                ticker=plan.ticker,
                interval=plan.interval.value,
                range_start=result.stored_only[0],
                range_end=result.stored_only[-1],
                detail={
                    "keys": [k.isoformat() for k in result.stored_only],
                    "note": "flagged; NOTHING is deleted",
                },
            )
        )

    incoming = result.incoming_only
    before = plan.archived_through_before
    late = 0 if plan.bootstrap else sum(1 for k in incoming if before is not None and k <= before)
    shared = {
        **base,
        "already_stored_equal": len(result.equal),
        "differing": len(result.differing),
        "incoming_only": len(incoming),
        "new": len(incoming) - late,
        "late": late,
        "differences": result.differing,
        "stored_only_keys": result.stored_only,
        "unassessed_before": split.export_oldest if plan.bootstrap else None,
    }

    # ---- a restatement WITHHOLDS the whole target (§6) ---------------
    if result.differing:
        incidents.append(
            IncidentDraft(
                kind=IncidentKind.RESTATED,
                ticker=plan.ticker,
                interval=plan.interval.value,
                range_start=result.differing[0].ts,
                range_end=result.differing[-1].ts,
                detail={
                    "differing": [d.as_detail() for d in result.differing],
                    "withheld": len(incoming),
                    "normalisation": "NUMERIC(14,4) prices, integer volume",
                },
            )
        )
        return TargetPlan(
            **shared,
            status=TargetStatus.FAILED,
            reason=(
                f"restated — {len(result.differing)} stored key(s) differ from the "
                "download after normalisation. NO insert for this target tonight, "
                "stored rows untouched, progress unchanged. There is no automatic "
                "repair, by constant factor or otherwise: run "
                f"`cobalt archiver restate {plan.ticker} {plan.interval.value}` "
                "(preview first, then --apply inside a quiet window)."
            ),
            archived_through_after=None,
            to_insert=(),
            withheld=len(incoming),
            incidents=tuple(incidents),
        )

    # ---- accepted ----------------------------------------------------
    to_insert = tuple(b for b in plan.candidates if b.ts in set(incoming))
    newest = split.export_newest
    after = newest if before is None else max(before, newest)

    if gap:
        status = TargetStatus.DEGRADED
        reason = (
            f"gap — the export begins at {split.export_oldest.isoformat()}, after "
            f"archived_through {before.isoformat()}. The window between them is "
            f"{GAP_WORDING} (suspected unavailable, not proven missing). The usable "
            f"range is appended: {len(to_insert)} key(s) offered."
        )
    elif result.stored_only:
        status = TargetStatus.DEGRADED
        reason = (
            f"{len(result.stored_only)} stored key(s) are absent from the download. "
            "Flagged; nothing deleted."
        )
    else:
        status = TargetStatus.SUCCESS
        reason = (
            f"{len(to_insert)} key(s) offered, {len(result.equal)} already stored and "
            "equal."
            + ("" if to_insert else " Nothing new — this is a success, not a failure.")
        )

    return TargetPlan(
        **shared,
        status=status,
        reason=reason,
        archived_through_after=after,
        to_insert=to_insert,
        withheld=0,
        incidents=tuple(incidents),
    )


__all__ = [
    "BarValues",
    "CandidatePlan",
    "Comparison",
    "Eligibility",
    "FIELD_ORDER",
    "FieldDifference",
    "GAP_WORDING",
    "INTERVAL_MINUTES",
    "IncidentDraft",
    "IncidentKind",
    "KeyDifference",
    "PRICE_QUANTUM",
    "ReconcileError",
    "STEADY_STATE_SESSIONS",
    "TargetCounts",
    "TargetPlan",
    "TargetStatus",
    "bar_closes_at",
    "bar_values",
    "compare",
    "et_date",
    "interval_duration",
    "is_complete",
    "normalise_price",
    "normalise_volume",
    "plan_candidates",
    "reconcile",
    "split_export",
    "steady_state_dates",
    "values_from_row",
]
