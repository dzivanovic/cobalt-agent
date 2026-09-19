"""The QUIET WINDOW — option A, ruled by the owner 2026-09-19 09:30 ET.

Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §8;
the ruling itself is `reports/cto-2026-09-19.md` §4 R8, "A on archiver".

WHAT IT GUARDS. Every command that MUTATES stored bars outside the
nightly run: `restate --apply` and `backfill-missing`. Previews and
every read-only command are always available.

THE FOUR RULES, mechanical:

  Q1  the session is OVERNIGHT — exactly the state in which the radar's
      cycle returns `idle:overnight` BEFORE any read or write
      (`radar/runner.py:173-176`). `MARKET_RESET` is NOT quiet: the
      radar is PAUSED there, not idle, and 20:30 belongs to the nightly
      run.
  Q2  the next boundary INTO a SCANNED session (premarket, RTH,
      aftermarket) is at least `quiet_before_open_min` away.
  Q3  `now >= last_scan_at + cycle_max_min + quiet_after_cycle_min`.
  Q4  the run-level advisory lock is held for the whole command
      (`store.run_lock`, §9 — enforced by the caller, not here).

Q1–Q3 are checked at command START **and again inside the repair
transaction immediately before COMMIT** — the shape of the radar's own
`gate` (`radar/runner.py:41-48`). A start-time check alone is exactly
what Astra's open-boundary sequence defeats.

WHY Q3 IS A DERIVATION AND NOT A MEASUREMENT. A scanning cycle stamps
its START instant into `system.radar_pool.last_scan_at`; the COMPLETION
instant is persisted nowhere (§2). So "the cycle has finished" is
derived from start + `cycle_max_min`, a STATED UPPER BOUND. That
estimate is precisely Gemini's and Astra's recorded dissent (§13) and
spec O-2 — option B (a per-target marker the POLLER checks inside its
own write transaction) was NOT taken and is carried to Sunday's
bars-lifecycle design. Nothing here touches the live poller.

REFUSING IS THE DEFAULT (L1). A missing pool row, a NULL `last_scan_at`
or an unreadable table REFUSES with "cannot prove the radar is quiet" —
it is never read as "no scan, therefore idle".

THERE IS NO `--force`. An override of this window is the owner's word,
recorded by the desk, and is a code or config change — never a flag
(L1, L37).
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from pydantic import BaseModel, ConfigDict

from cobalt.session.models import Session

ET = ZoneInfo("America/New_York")

#: The sessions in which the radar SCANS (`radar/runner.py:35`). The
#: quiet window is the complement of these, minus `MARKET_RESET`.
SCANNED_SESSIONS = (Session.PREMARKET, Session.RTH, Session.AFTERMARKET)

REFUSAL_OPENING = "REFUSED — not in a quiet window."
UNPROVEN = (
    "cannot prove the radar is quiet — system.radar_pool has no usable "
    "last_scan_at for this pool"
)
PREVIEW_LINE = "The preview (no --apply) is always available."


class QuietRefused(RuntimeError):
    """A repair refused because the window is not quiet. Exit code 2."""

    exit_code = 2

    def __init__(self, message: str, verdict: "QuietVerdict | None" = None):
        super().__init__(message)
        self.verdict = verdict


class QuietObservation(BaseModel):
    """What the reader saw. Pure data — the verdict is computed from it.

    Splitting the observation from the verdict is what makes §8 testable
    to the second without a database or a live radar: the two named
    boundary tests drive this object.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    now: datetime
    session: Session
    pool_key: str
    pool_row_present: bool
    #: The START of the last scanning cycle, or None (NULL / no row).
    last_scan_at: datetime | None
    #: The next boundary INTO a scanned session, from `now`.
    next_scanning_open: datetime | None
    next_scanning_session: Session | None
    #: When the current (or next) OVERNIGHT window begins.
    overnight_start: datetime
    #: The scanned-session open that FOLLOWS `overnight_start`.
    open_after_overnight: datetime | None


class QuietVerdict(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    quiet: bool
    failures: tuple[str, ...] = ()
    earliest_allowed_start: datetime | None = None
    text: str = ""


def _et(ts: datetime | None) -> str:
    return "unknown" if ts is None else f"{ts.astimezone(ET):%Y-%m-%d %H:%M:%S %Z}"


def _minutes(delta: timedelta) -> int:
    """Whole minutes, truncated toward zero — an operator reads "6 min",
    not "6.17 min", and rounding UP would overstate the distance to a
    boundary the rule is trying to keep away from."""
    return int(delta.total_seconds() // 60)


def quiet_verdict(observation: QuietObservation, settings) -> QuietVerdict:
    """PURE. Q1–Q3 against one observation. Q4 is the caller's lock."""
    repair = settings.repair
    need_after = repair.cycle_max_min + repair.quiet_after_cycle_min
    failures: list[str] = []

    # --- Q1 -----------------------------------------------------------
    if observation.session is not Session.OVERNIGHT:
        if observation.session is Session.MARKET_RESET:
            failures.append(
                "Q1 radar idle: session=market_reset — the radar is PAUSED there, "
                "not idle, and 20:30 belongs to the nightly archiver run."
            )
        else:
            failures.append(
                f"Q1 radar idle: session={observation.session.value} — the radar "
                "scans in premarket, RTH and aftermarket."
            )

    # --- Q2 -----------------------------------------------------------
    if observation.next_scanning_open is None:
        failures.append(
            "Q2 before the next session: the session clock could not find the "
            "next scanning open."
        )
    else:
        distance = observation.next_scanning_open - observation.now
        if distance < timedelta(minutes=repair.quiet_before_open_min):
            failures.append(
                f"Q2 before the next session: the next scanning session opens in "
                f"{_minutes(distance)} min; need >= {repair.quiet_before_open_min} min."
            )

    # --- Q3 -----------------------------------------------------------
    if not observation.pool_row_present or observation.last_scan_at is None:
        failures.append(f"Q3 after the last poll cycle: {UNPROVEN}.")
        allowed_by_cycle = None
    else:
        allowed_by_cycle = observation.last_scan_at + timedelta(minutes=need_after)
        age = observation.now - observation.last_scan_at
        if observation.now < allowed_by_cycle:
            failures.append(
                f"Q3 after the last poll cycle: the last scan STARTED "
                f"{_minutes(age)} min ago; need >= {need_after} min "
                f"({repair.cycle_max_min} min derived cycle bound + "
                f"{repair.quiet_after_cycle_min} min quiet)."
            )

    earliest = _earliest_allowed(observation, settings, allowed_by_cycle)

    if not failures:
        return QuietVerdict(quiet=True, earliest_allowed_start=observation.now)

    return QuietVerdict(
        quiet=False,
        failures=tuple(failures),
        earliest_allowed_start=earliest,
        text=refusal_text(observation, settings, failures, earliest),
    )


def _earliest_allowed(
    observation: QuietObservation, settings, allowed_by_cycle: datetime | None
) -> datetime | None:
    """The first instant at which all three rules would hold.

    `None` when it cannot be stated: either the radar's quiet cannot be
    PROVEN (no pool row), or the next overnight window is too short to
    hold the repair at all — both are honest answers, and inventing a
    time for either is what L1 forbids.
    """
    if allowed_by_cycle is None:
        return None
    candidate = max(allowed_by_cycle, observation.overnight_start, observation.now)
    if observation.open_after_overnight is None:
        return None
    latest = observation.open_after_overnight - timedelta(
        minutes=settings.repair.quiet_before_open_min
    )
    return candidate if candidate <= latest else None


def refusal_text(observation, settings, failures, earliest) -> str:
    """§8's refusal, verbatim in shape: one line per failed rule, then
    the summary carrying every OBSERVED value and the earliest start."""
    repair = settings.repair
    need_after = repair.cycle_max_min + repair.quiet_after_cycle_min
    age = (
        "no usable last_scan_at"
        if observation.last_scan_at is None or not observation.pool_row_present
        else f"{_minutes(observation.now - observation.last_scan_at)} min ago"
    )
    distance = (
        "unknown"
        if observation.next_scanning_open is None
        else f"in {_minutes(observation.next_scanning_open - observation.now)} min"
    )
    lines = list(failures)
    lines.append(
        f"{REFUSAL_OPENING} session={observation.session.value} · "
        f"last radar scan started {_et(observation.last_scan_at)} ({age}; "
        f"need >= {need_after} min) · next scanning session opens "
        f"{_et(observation.next_scanning_open)} ({distance}; need >= "
        f"{repair.quiet_before_open_min} min) · earliest allowed start: "
        f"{_et(earliest)}. {PREVIEW_LINE}"
    )
    if not observation.pool_row_present or observation.last_scan_at is None:
        lines.append(UNPROVEN + ".")
    return "\n".join(lines)


# ---------------------------------------------------------------------
# Reading the observation (the only I/O in this module)
# ---------------------------------------------------------------------


def observe(*, now, pool_reader, clock, pool_key: str) -> QuietObservation:
    """Build the observation from the radar's OWN clock and pool row.

    `pool_reader` is injected — one callable returning the pool row (or
    None) — so the whole of §8 can be driven by a constructed row in a
    test without a database, and so this module never opens a
    connection of its own.
    """
    row = pool_reader(pool_key)
    last_scan_at = row.get("last_scan_at") if row else None
    session = clock.session(now)
    next_open, next_session = _next_scanning_open(clock, now)
    overnight_start = now if session is Session.OVERNIGHT else _next_overnight(clock, now)
    open_after, _ = _next_scanning_open(clock, overnight_start)
    return QuietObservation(
        now=now,
        session=session,
        pool_key=pool_key,
        pool_row_present=row is not None,
        last_scan_at=last_scan_at,
        next_scanning_open=next_open,
        next_scanning_session=next_session,
        overnight_start=overnight_start,
        open_after_overnight=open_after,
    )


def _next_scanning_open(clock, ts):
    """Walk `next_boundary` until a SCANNED session starts.

    The walk is what makes a weekend, a holiday and an early close
    correct for free — `SessionClock.next_boundary` already knows them
    (`session/clock.py:230-254`).
    """
    cursor = ts
    for _ in range(16):
        boundary, session = clock.next_boundary(cursor)
        if session in SCANNED_SESSIONS:
            return boundary, session
        cursor = boundary
    return None, None


def _next_overnight(clock, ts):
    cursor = ts
    for _ in range(16):
        boundary, session = clock.next_boundary(cursor)
        if session is Session.OVERNIGHT:
            return boundary
        cursor = boundary
    return ts


# ---------------------------------------------------------------------
# The guard a repair command runs inside
# ---------------------------------------------------------------------


class _Guard:
    def __init__(self, observe_fn, settings, what: str):
        self._observe = observe_fn
        self._settings = settings
        self._what = what

    def check(self) -> QuietVerdict:
        verdict = quiet_verdict(self._observe(), self._settings)
        if not verdict.quiet:
            raise QuietRefused(verdict.text, verdict)
        return verdict

    def check_before_commit(self) -> QuietVerdict:
        """The SECOND check, inside the transaction, immediately before
        COMMIT. Raising here is what rolls the repair back — a start-time
        check alone is what Astra's open-boundary sequence defeats."""
        return self.check()


@contextmanager
def guarded_repair(*, observe, settings, what: str):
    """START check, then the caller's work, then its own pre-commit check.

    The caller must call `guard.check_before_commit()` INSIDE its
    transaction: only the caller knows where its commit is, and a guard
    that tried to own the transaction would have to own the connection
    too — which §4 gives to the target.
    """
    guard = _Guard(observe, settings, what)
    guard.check()
    yield guard


def require_quiet(*, observe, settings, what: str) -> QuietVerdict:
    """One-shot start check, for a command with no transaction of its own."""
    return _Guard(observe, settings, what).check()


__all__ = [
    "PREVIEW_LINE",
    "REFUSAL_OPENING",
    "SCANNED_SESSIONS",
    "UNPROVEN",
    "QuietObservation",
    "QuietRefused",
    "QuietVerdict",
    "guarded_repair",
    "observe",
    "quiet_verdict",
    "refusal_text",
    "require_quiet",
]
