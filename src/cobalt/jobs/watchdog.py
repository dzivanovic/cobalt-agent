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


def launchctl_pid(label: str, *, timeout: float = 5.0) -> tuple[Optional[int], str]:
    """(pid, detail) from `launchctl list`. `None` = loaded-but-not-running
    or not loaded at all, and the detail says which.

    Fail-loud: a `launchctl` that cannot be run RAISES rather than
    reporting "not running". "The probe is broken" and "the job is down"
    are different facts and collapsing them is how a red condition
    becomes invisible — the same rule `cobalt.obsidian` keeps.
    """
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
            if pid_raw.isdigit():
                return int(pid_raw), f"launchd pid {pid_raw}"
            return None, (
                f"loaded but NOT RUNNING (last exit {status_raw}) — launchctl "
                "shows no pid"
            )
    return None, "NOT LOADED in launchd — `launchctl list` does not know this label"


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
        window = timedelta(minutes=minutes) * 2
        reference = finished_et or clock.to_et(row["registered_at"])
        if now_et - reference <= window:
            return False, ""
        return True, (
            f"{cadence}; last finish "
            + (f"{finished_et:%Y-%m-%d %H:%M} ET" if finished_et else
               f"NEVER (registered {reference:%Y-%m-%d %H:%M} ET)")
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
                    pid, detail = launchctl_pid(spec.label)
                    alive = pid is not None
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

        findings.append(
            Finding(
                spec.label, True, state,
                (
                    f"last finish {session_clock().to_et(row['finished_at']):%Y-%m-%d %H:%M} ET"
                    f", exit {row['exit_code']}"
                    if row["finished_at"] else "never run yet (registered, not yet due)"
                ),
            )
        )

    return findings


def red(findings: list[Finding]) -> list[Finding]:
    return [f for f in findings if not f.ok]


__all__ = [
    "MISSED_GRACE_KEY",
    "Finding",
    "is_missed",
    "last_due",
    "launchctl_pid",
    "pidfile_alive",
    "red",
    "sweep",
]
