"""F17c: the watchdog. What nobody wrote down, concluded from what is there.

Charter §3 F17: "a hung poller is surfaced as a zombie within one
heartbeat interval." Two conclusions, both RED:

* ZOMBIE — `running` past `timeout_s`, with `heartbeat_at` stale by more
  than `timeout_s / jobs.heartbeat_fraction`. Both halves are required.
  The archiver runs 23 minutes on a normal night; "started and did not
  finish" is true of a healthy long job and useless as a test. A stale
  HEARTBEAT is the signal, because the beater thread dies with the
  process it belongs to.

* MISSED — a one-shot whose most recent scheduled occurrence has passed
  (plus `jobs.missed_grace_min`) with no run finishing after it. This is
  the failure mode that actually bit: on 2026-09-03 both prefill jobs
  exited 78 with empty stdout and stderr, and nothing noticed until the
  morning note was not there.

  MISSED IS NOT A STATE. There is no row to move — it is a fact about the
  ABSENCE of a run, computed here at probe time. Writing it as a state
  would mean inventing a run to attach it to.

Residents supervised by launchd or a PID file are PROBED here rather than
concluded about: the watchdog asks `launchctl` (or reads the PID file)
and stamps `heartbeat_at` on their behalf, marking `heartbeat_source` so
nothing reads a probe's "the process exists" as a wrapper's "I am
working".
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Optional

from cobalt.session import clock as clock_mod
from cobalt.session.clock import ET, session_clock

from .config import JobRegistry, JobSpec, load_job_registry
from .models import RED_STATES, JobKind, JobState, Supervisor
from .store import JobStore

MISSED_GRACE_KEY = "jobs.missed_grace_min"


@dataclass
class Finding:
    """One job's verdict, ready for the heartbeat block."""

    label: str
    ok: bool
    state: str
    detail: str

    def line(self) -> str:
        mark = "OK  " if self.ok else "RED "
        return f"{mark} {self.label:<28} {self.state:<9} {self.detail}"


def _tunable_int(key: str) -> int:
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(key)
    if row is None:
        raise RuntimeError(
            f"tunable {key!r} is missing from tunables.yaml — the watchdog reads its "
            "thresholds from config and has no built-in defaults (F16)."
        )
    return int(row.value)


# ---------------------------------------------------------------------
# launchd / pidfile probes
# ---------------------------------------------------------------------


@dataclass(frozen=True)
class LaunchdStatus:
    """What `launchctl list` knows about one label.

    THREE DISTINCT ANSWERS, and conflating any two of them is how a red
    condition goes unseen:

    * `loaded=False` — launchd has never heard of this label. For a
      one-shot this is the ONLY failure mode that exists between runs:
      it has no PID to lose and no state to change, it simply will never
      fire again. Charter §3 F18's acceptance test is exactly this
      ("unload a plist -> red within one interval").
    * `loaded=True, pid=None` — registered with launchd, not currently
      running. Correct and healthy for a one-shot between runs; a
      FAILURE for a resident.
    * `last_exit` — launchd's own record of how the last run ended,
      which is the other half of what the Charter asks for ("every ops
      plist loaded + last exit code").
    """

    label: str
    loaded: bool
    pid: Optional[int]
    last_exit: Optional[int]
    detail: str


def launchctl_status(label: str, *, timeout: float = 5.0) -> LaunchdStatus:
    """Ask launchd about one label. Fail-loud: a `launchctl` that cannot
    be run RAISES rather than reporting "not loaded" — "the probe is
    broken" and "the job is gone" are different facts, and collapsing
    them is how a red condition becomes invisible (the same rule
    `cobalt.obsidian` keeps)."""
    binary = shutil.which("launchctl") or "/bin/launchctl"
    if not os.path.exists(binary):
        raise RuntimeError("launchctl not found — cannot probe launchd jobs.")
    proc = subprocess.run(
        [binary, "list"], capture_output=True, text=True, timeout=timeout
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"`launchctl list` exited {proc.returncode}: "
            f"{proc.stderr.strip() or '(no stderr)'}"
        )
    for line in proc.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) == 3 and parts[2].strip() == label:
            pid_raw, status_raw = parts[0].strip(), parts[1].strip()
            pid = int(pid_raw) if pid_raw.lstrip("-").isdigit() and pid_raw != "-" else None
            try:
                last_exit = int(status_raw)
            except ValueError:
                last_exit = None
            detail = (
                f"loaded, pid {pid}" if pid is not None
                else f"loaded, not running (last exit {status_raw})"
            )
            return LaunchdStatus(label, True, pid, last_exit, detail)
    return LaunchdStatus(
        label, False, None, None,
        "NOT LOADED in launchd — `launchctl list` does not know this label, so it "
        "will never fire again. Reload it: "
        f"launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/{label}.plist",
    )


def launchctl_pid(label: str, *, timeout: float = 5.0) -> tuple[Optional[int], str]:
    """(pid, detail). Kept as the narrow question residents ask."""
    status = launchctl_status(label, timeout=timeout)
    if status.pid is not None:
        return status.pid, f"launchd pid {status.pid}"
    return None, status.detail


def pidfile_alive(spec: JobSpec) -> tuple[bool, str]:
    """(alive, detail) for a detached resident tracked by a PID file."""
    path = spec.pidfile_path
    if path is None or not path.exists():
        return False, f"no pid file at {path} — the process was never started, or it cleaned up"
    raw = path.read_text().strip()
    if not raw.isdigit():
        return False, f"pid file {path} does not contain a pid ({raw[:40]!r})"
    pid = int(raw)
    try:
        os.kill(pid, 0)          # signal 0: existence check, changes nothing
    except ProcessLookupError:
        return False, f"pid {pid} from {path} is GONE — stale pid file, process is dead"
    except PermissionError:
        return True, f"pid {pid} exists (owned by another user)"
    return True, f"pid {pid} alive (from {path})"


# ---------------------------------------------------------------------
# schedule arithmetic — "should this have run by now?"
# ---------------------------------------------------------------------


def last_due(spec: JobSpec, now_et: datetime) -> Optional[datetime]:
    """The most recent CALENDAR moment this one-shot was scheduled to
    fire, at or before `now_et`. `None` for an interval job (which has no
    calendar moments — see `is_missed`) and for a resident.

    Weekday numbering is launchd's (1 = Monday), matching the plists this
    mirrors.
    """
    schedule = spec.schedule
    if schedule is None or schedule.interval_minutes() is not None:
        return None

    hh, _, mm = schedule.at.partition(":")
    hour, minute = int(hh), int(mm)
    # launchd: Sunday is 0 and 7; python's isoweekday() is Mon=1..Sun=7.
    wanted = {0 if d == 7 else d for d in schedule.weekdays}
    probe: date = now_et.date()
    for _ in range(14):
        iso = probe.isoweekday()
        launchd_day = 0 if iso == 7 else iso
        if launchd_day in wanted:
            due = datetime(
                probe.year, probe.month, probe.day, hour, minute, tzinfo=ET
            )
            if due <= now_et:
                return due
        probe -= timedelta(days=1)
    return None


def is_missed(
    spec: JobSpec, row: dict, *, now_et: datetime, grace: timedelta
) -> tuple[bool, str]:
    """Should this one-shot have run by now, and did it?

    TWO SHAPES, and they need different arithmetic — getting this wrong
    is how a job goes quiet without anyone noticing, which is the whole
    failure this probe exists for:

    * CALENDAR jobs (Mon-Fri 05:15) have moments. Missed = the last such
      moment passed more than `grace` ago and no run finished after it.
    * INTERVAL jobs (every 15 min) have no moments — `now - interval` is
      always exactly one interval ago, so a fixed grace larger than the
      interval would make them NEVER missable. The first draft of this
      function had exactly that bug: a 15-minute heartbeat against a
      30-minute grace reported green forever, including while stopped.
      Missed = the last finish is older than TWO intervals (one it should
      have run in, one of slack).
    """
    clock = session_clock()
    finished = row["finished_at"]
    finished_et = clock.to_et(finished) if finished else None
    cadence = spec.cadence or "(no cadence)"

    minutes = spec.schedule.interval_minutes() if spec.schedule else None
    if minutes is not None:
        # A WINDOWED interval job is not due outside its window, and an
        # overnight gap is its schedule working. Asked before the
        # arithmetic, because the arithmetic below has no way to tell a
        # seven-hour gap that is correct from one that is not.
        if not spec.schedule.due_now(now_et):
            return False, ""
        window = timedelta(minutes=minutes) * 2
        reference = finished_et or clock.to_et(row["registered_at"])
        # Inside a window, the clock starts when the window OPENS. The
        # first run of the day is due one interval after 06:00, not one
        # interval after last night's 23:00 — measuring from the older
        # of the two would report MISSED every morning at 06:00 sharp.
        opened = spec.schedule.window_opened_at(now_et)
        if opened is not None and opened > reference:
            reference = opened
        if now_et - reference <= window:
            return False, ""
        return True, (
            f"{cadence}; last finish "
            + (f"{finished_et:%Y-%m-%d %H:%M} ET" if finished_et else
               f"NEVER (registered {clock.to_et(row['registered_at']):%Y-%m-%d %H:%M} ET)")
            + f", measured from {reference:%Y-%m-%d %H:%M} ET"
            + f" — more than two intervals ({window.total_seconds() / 60:.0f} min) ago. "
            "An interval job is missed against its OWN cadence: a fixed grace wider "
            "than the interval would make it unmissable."
        )

    due = last_due(spec, now_et)
    if due is None or now_et - due <= grace:
        return False, ""
    if finished_et is not None and finished_et >= due:
        return False, ""

    # COBALT CANNOT MISS A RUN IT WAS NOT WATCHING FOR. A job registered
    # at 22:00 today has no record of this morning's 05:15 run, because
    # the table did not exist then — reporting that as MISSED would make
    # the FIRST heartbeat after this feature ships red for five jobs that
    # are all perfectly fine, and an alert that is wrong on day one is an
    # alert people learn to scroll past. The probe starts counting from
    # the first due moment AFTER registration.
    registered_et = clock.to_et(row["registered_at"]) if row.get("registered_at") else None
    if finished_et is None and registered_et is not None and due <= registered_et:
        return False, ""

    return True, (
        f"due {due:%Y-%m-%d %H:%M} ET ({cadence}); last finish "
        + (f"{finished_et:%Y-%m-%d %H:%M} ET" if finished_et else "NEVER")
        + ". The 09-03 prefill failures looked exactly like this: exit 78, "
        "empty stdout and stderr, noticed the next morning."
    )


# ---------------------------------------------------------------------
# the sweep
# ---------------------------------------------------------------------


def sweep(
    *,
    store: Optional[JobStore] = None,
    registry: Optional[JobRegistry] = None,
    now: Optional[datetime] = None,
    probe: bool = True,
) -> list[Finding]:
    """Probe, conclude, persist, and report. F18 renders the result.

    `probe=False` skips the launchctl/pidfile calls — the unit tests use
    it; nothing in production does, because a heartbeat that did not
    actually look is a heartbeat that always says green.
    """
    store = store or JobStore()
    registry = registry or load_job_registry()
    store.ensure_schema()
    ts = now or clock_mod.now_utc()
    now_et = session_clock().to_et(ts)
    fraction = _tunable_int("jobs.heartbeat_fraction")
    grace = timedelta(minutes=_tunable_int(MISSED_GRACE_KEY))

    findings: list[Finding] = []
    rows = {r["label"]: r for r in store.all()}

    for spec in registry.jobs:
        row = rows.get(spec.label)

        # -- IS THIS JOB EVEN SUPPOSED TO BE LOADED? A registry row with
        # `enabled: false` is a job that has been BUILT and reviewed but
        # not yet handed over to launchd. Every check below asks a
        # question whose honest answer for such a job is "of course not"
        # — probing it would put a permanent red on the beat for a state
        # somebody chose deliberately, and a standing red is how a
        # heartbeat stops being read. It is REPORTED, not hidden: the
        # line is on the block, it just is not a failure.
        if not spec.enabled:
            findings.append(
                Finding(
                    spec.label, True, "disabled",
                    "registered but NOT LOADED BY DESIGN (`enabled: false` in "
                    "configs/cobalt/jobs.yaml) — nothing is probed and nothing is "
                    "claimed. Flip the flag as the last step of its handover.",
                )
            )
            continue

        # -- IS THE PLIST EVEN LOADED? Charter §3 F18: "every ops plist
        # loaded + last exit code". Asked of EVERY job, resident and
        # one-shot alike, and asked FIRST.
        #
        # This check was missing from the first version of this function,
        # and running the Charter's own acceptance test for real is what
        # found it: `launchctl bootout com.cobalt.cards-expire` and the
        # heartbeat stayed green, because a one-shot between runs looks
        # identical whether its plist is loaded or gone. An unloaded
        # one-shot has no PID to lose and no state to change — it simply
        # never fires again, and MISSED would not say so until its next
        # scheduled time plus the grace, which for a Friday-evening
        # unload is Monday.
        if probe:
            try:
                status = launchctl_status(spec.label)
            except Exception as e:  # noqa: BLE001
                findings.append(
                    Finding(spec.label, False, (row or {}).get("state", "unknown"),
                            f"launchd PROBE FAILED ({type(e).__name__}: {e}) — loaded "
                            "state UNKNOWN, which is not the same as loaded")
                )
                continue
            if not status.loaded:
                # A RESIDENT's row IS its liveness, so it is marked. A
                # ONE-SHOT's row is the record of its LAST RUN, and
                # "the plist is gone" is a fact about launchd, not about
                # that run — overwriting `state` and `exit_code` with it
                # would destroy the only record of how the job last
                # ended, and leave a stale `failed` behind after the
                # plist is reloaded (which is exactly what happened the
                # first time this ran: reload restored the plist and the
                # row still said failed). It is reported, not written.
                if row is not None and spec.kind is JobKind.RESIDENT:
                    store.mark_probe(spec.label, alive=False, detail=status.detail, now=ts)
                findings.append(Finding(spec.label, False, "not loaded", status.detail))
                continue

        if row is None:
            store.register(spec)
            findings.append(
                Finding(spec.label, False, "unregistered",
                        "no jobs row existed — registered now; nothing has run yet")
            )
            continue

        # -- residents someone else supervises: PROBE them -------------
        if spec.supervisor is not Supervisor.SELF:
            if not probe:
                findings.append(Finding(spec.label, True, row["state"], "probe skipped"))
                continue
            try:
                if spec.supervisor is Supervisor.LAUNCHD:
                    alive = status.pid is not None
                    detail = status.detail
                else:
                    alive, detail = pidfile_alive(spec)
            except Exception as e:  # noqa: BLE001 - a broken probe is its own red
                findings.append(
                    Finding(spec.label, False, row["state"],
                            f"PROBE FAILED ({type(e).__name__}: {e}) — liveness UNKNOWN, "
                            "which is not the same as 'up' and is reported as red")
                )
                continue
            store.mark_probe(spec.label, alive=alive, detail=detail, now=ts)
            findings.append(
                Finding(
                    spec.label, alive,
                    JobState.RUNNING.value if alive else JobState.FAILED.value,
                    f"{detail} [{spec.supervisor} probe]",
                )
            )
            continue

        # -- jobs the wrapper reports on -------------------------------
        state = row["state"]

        if state == JobState.RUNNING.value:
            started, beat = row["started_at"], row["heartbeat_at"]
            ran_for = (ts - started).total_seconds() if started else 0
            stale_for = (ts - beat).total_seconds() if beat else None
            stale_limit = spec.timeout_s / fraction
            if ran_for > spec.timeout_s and (stale_for is None or stale_for > stale_limit):
                reason = (
                    f"ZOMBIE: running {ran_for / 60:.0f} min (timeout "
                    f"{spec.timeout_s / 60:.0f} min) and the heartbeat is "
                    + (f"{stale_for / 60:.0f} min stale" if stale_for else "missing")
                    + f" (limit {stale_limit / 60:.0f} min). The beater thread dies "
                    "with its process, so a stale stamp means the process is gone."
                )
                store.mark_zombie(spec.label, reason=reason)
                findings.append(Finding(spec.label, False, JobState.ZOMBIE.value, reason))
            else:
                findings.append(
                    Finding(spec.label, True, state,
                            f"running {ran_for / 60:.0f} min, heartbeat fresh")
                )
            continue

        if state in {s.value for s in RED_STATES}:
            findings.append(
                Finding(spec.label, False, state,
                        (row["last_error"] or "no error text recorded")[:300])
            )
            continue

        # -- MISSED: a fact about an absent run, not a state -----------
        if spec.kind is JobKind.ONE_SHOT:
            missed, detail = is_missed(spec, row, now_et=now_et, grace=grace)
            if missed:
                findings.append(Finding(spec.label, False, f"{state} (MISSED)", detail))
                continue

        launchd_note = (
            f" · launchd: loaded, last exit {status.last_exit}"
            if probe and status.last_exit is not None else " · launchd: loaded"
        ) if probe else ""
        findings.append(
            Finding(
                spec.label, True, state,
                (
                    f"last finish {session_clock().to_et(row['finished_at']):%Y-%m-%d %H:%M} ET"
                    f", exit {row['exit_code']}"
                    if row["finished_at"] else "never run yet (registered, not yet due)"
                ) + launchd_note,
            )
        )

    return findings


def red(findings: list[Finding]) -> list[Finding]:
    return [f for f in findings if not f.ok]


__all__ = [
    "MISSED_GRACE_KEY",
    "Finding",
    "LaunchdStatus",
    "launchctl_status",
    "is_missed",
    "last_due",
    "launchctl_pid",
    "pidfile_alive",
    "red",
    "sweep",
]
