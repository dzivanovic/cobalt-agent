"""F17 config: the job registry, `configs/cobalt/jobs.yaml`.

Pydantic-validated on load; a bad row CRASHES with its label. The
registry is the ONE place a job's kind, timeout, supervisor and schedule
are written down — the plist carries the schedule too, because launchd
cannot read YAML, and `cobalt validate` compares the two so a drift is
loud rather than discovered by a job that never fired.
"""

from __future__ import annotations

from datetime import datetime, time
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from .models import JobKind, Supervisor

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "jobs.yaml"
OPS_DIR = REPO_ROOT / "ops"
HEARTBEAT_LABEL = "com.cobalt.heartbeat"

#: launchd's weekday numbering, which this file mirrors: 1 = Monday.
WEEKDAY_NAMES = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 0: "Sun"}


class JobConfigError(RuntimeError):
    """Missing/invalid job registry — crash, never fall back."""


def parse_window(raw: str, key: str) -> tuple[time, time]:
    """`"06:00-23:00"` -> (time(6, 0), time(23, 0)). Fail-loud on anything
    else: a window nobody can parse is a window nobody is watching."""
    open_raw, sep, close_raw = str(raw).partition("-")
    if not sep:
        raise JobConfigError(
            f"tunable {key!r} = {raw!r} is not a window — expected 'HH:MM-HH:MM' ET."
        )

    def _t(part: str) -> time:
        hh, _, mm = part.strip().partition(":")
        try:
            return time(int(hh), int(mm))
        except ValueError:
            raise JobConfigError(
                f"tunable {key!r} = {raw!r} is not a window — {part.strip()!r} is "
                "not HH:MM."
            ) from None

    opens, closes = _t(open_raw), _t(close_raw)
    if closes <= opens:
        raise JobConfigError(
            f"tunable {key!r} = {raw!r} closes at or before it opens. A window that "
            "wraps midnight is not supported — say so explicitly rather than having "
            "the arithmetic quietly mean something else."
        )
    return opens, closes


class Schedule(BaseModel):
    """When a one-shot is due. Either a wall-clock time on given
    weekdays (a `StartCalendarInterval` plist), or an interval."""

    model_config = ConfigDict(extra="forbid")

    at: Optional[str] = None
    weekdays: list[int] = Field(default_factory=list)
    every_min: Optional[int] = Field(default=None, gt=0)
    #: F16: an interval that is a THRESHOLD reads its value from a
    #: tunables row rather than carrying a literal here. The heartbeat's
    #: own cadence is the one that matters — it is the number every
    #: "within one interval" claim in Charter §3 F18 is measured against.
    every_min_tunable: Optional[str] = None
    #: The ET clock window an interval job is due INSIDE, as "HH:MM-HH:MM",
    #: read from a tunables row (F16 — a window is a threshold).
    #:
    #: WHY A WINDOW IS PART OF THE SCHEDULE AND NOT OF THE JOB. Without
    #: it, `is_missed` compares an interval job's last finish against two
    #: of its own intervals and nothing else — which is correct for a job
    #: that runs all night (the heartbeat) and WRONG for one that stops
    #: at 23:00 and starts again at 06:00. A 60-minute job would be
    #: reported MISSED at 01:05 every single night for a gap that is its
    #: schedule working exactly as written. The window is the only thing
    #: that tells those two shapes apart.
    window_tunable: Optional[str] = None

    @model_validator(mode="after")
    def _one_shape(self) -> "Schedule":
        forms = [bool(self.at), self.every_min is not None, bool(self.every_min_tunable)]
        if sum(forms) != 1:
            raise ValueError(
                "a schedule is exactly one of: `at` (+ weekdays), `every_min`, or "
                "`every_min_tunable`."
            )
        if self.window_tunable:
            if self.at:
                raise ValueError(
                    "`window_tunable` belongs to an INTERVAL schedule — a calendar "
                    "`at` time is already a single moment and has no window."
                )
            if not self.weekdays:
                raise ValueError(
                    "`window_tunable` needs `weekdays` — a window that does not say "
                    "which days it opens on cannot answer 'was this due?' on a Sunday."
                )
        if self.at:
            try:
                hh, _, mm = self.at.partition(":")
                if not (0 <= int(hh) <= 23 and 0 <= int(mm) <= 59):
                    raise ValueError
            except ValueError:
                raise ValueError(f"schedule.at {self.at!r} is not HH:MM ET") from None
            if not self.weekdays:
                raise ValueError("schedule.at needs `weekdays` (launchd numbering, 1=Mon)")
        bad = [d for d in self.weekdays if d not in WEEKDAY_NAMES]
        if bad:
            raise ValueError(f"unknown weekday number(s) {bad} — launchd uses 0=Sun..6=Sat")
        return self

    def interval_minutes(self) -> Optional[int]:
        """The interval, resolving the tunable if that is how it is set."""
        if self.every_min is not None:
            return self.every_min
        if not self.every_min_tunable:
            return None
        from cobalt.taxonomy.loader import load_tunables

        row = load_tunables().by_key.get(self.every_min_tunable)
        if row is None:
            raise JobConfigError(
                f"tunable {self.every_min_tunable!r} is missing from tunables.yaml — "
                "a job schedule reads its interval from config and has no built-in "
                "default (F16)."
            )
        return int(row.value)

    def window(self) -> Optional[tuple[time, time]]:
        """(open, close) in ET, resolving the tunable. None when the
        schedule has no window and the job is due around the clock."""
        if not self.window_tunable:
            return None
        from cobalt.taxonomy.loader import load_tunables

        row = load_tunables().by_key.get(self.window_tunable)
        if row is None:
            raise JobConfigError(
                f"tunable {self.window_tunable!r} is missing from tunables.yaml — a "
                "job window is read from config and has no built-in default (F16)."
            )
        return parse_window(str(row.value), self.window_tunable)

    def due_now(self, now_et: datetime) -> bool:
        """Is this schedule's job due to be running at `now_et`?

        Only ever False for a WINDOWED interval schedule — every other
        shape is due whenever its own arithmetic says so, and answering
        "no" for them here would hide a real miss.
        """
        span = self.window()
        if span is None:
            return True
        if self.weekdays:
            iso = now_et.isoweekday()
            launchd_day = 0 if iso == 7 else iso
            if launchd_day not in set(self.weekdays):
                return False
        opens, closes = span
        return opens <= now_et.time() <= closes

    def window_opened_at(self, now_et: datetime) -> Optional[datetime]:
        """The moment today's window opened, for a `now_et` inside it."""
        span = self.window()
        if span is None:
            return None
        opens = span[0]
        return now_et.replace(
            hour=opens.hour, minute=opens.minute, second=0, microsecond=0
        )

    def describe(self) -> str:
        """The human string that lands in `jobs.expected_cadence`."""
        if self.at:
            days = ", ".join(WEEKDAY_NAMES[d] for d in sorted(self.weekdays))
            return f"{days} {self.at} ET"
        base = f"every {self.interval_minutes()} min"
        span = self.window()
        if span is None:
            return base
        days = (
            ", ".join(WEEKDAY_NAMES[d] for d in sorted(self.weekdays))
            if self.weekdays else "every day"
        )
        return f"{base} {span[0]:%H:%M}-{span[1]:%H:%M} ET, {days}"

    def calendar_entries(self) -> list[dict[str, int]]:
        """The `StartCalendarInterval` array a windowed interval schedule
        is worth in launchd — one entry per weekday per firing.

        launchd has no "every N minutes between 06:00 and 23:00": it has
        `StartInterval` (which never stops) and `StartCalendarInterval`
        (which is a list of moments). A window is therefore EXPANDED into
        moments here, and the test suite compares this list against the
        plist's own array so the two can never drift.
        """
        minutes = self.interval_minutes()
        span = self.window()
        if minutes is None or span is None:
            return []
        opens, closes = span
        entries: list[dict[str, int]] = []
        for day in sorted(self.weekdays):
            cursor = opens.hour * 60 + opens.minute
            last = closes.hour * 60 + closes.minute
            while cursor <= last:
                entries.append(
                    {"Weekday": day, "Hour": cursor // 60, "Minute": cursor % 60}
                )
                cursor += minutes
        return entries


class JobSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    label: str = Field(min_length=1)
    kind: JobKind
    supervisor: Supervisor
    timeout_s: int = Field(gt=0)
    what: str = Field(min_length=1)
    schedule: Optional[Schedule] = None
    pidfile: Optional[str] = None
    #: Is this job's plist supposed to be LOADED in launchd right now?
    #:
    #: Default True, because that is what every job in this registry has
    #: always meant. `enabled: false` is the narrow, declared case of a
    #: job that is BUILT, registered and reviewable but deliberately not
    #: yet handed over to launchd — `com.cobalt.herdr` is the first, and
    #: it exists because the handover has to happen at the keyboard (the
    #: server being registered is the one hosting the session that would
    #: register it).
    #:
    #: THE FLAG SUPPRESSES THE PROBE, NOT THE ROW. A disabled job is
    #: still in the registry, still has to have a plist in ops/, still
    #: has its schedule cross-checked by the suite. What it does not get
    #: is a red "NOT LOADED in launchd" every 15 minutes for a state
    #: somebody chose on purpose — which is exactly the kind of standing
    #: red that teaches a reader to scroll past the heartbeat.
    #:
    #: Flipping it to true is the LAST step of a handover, after the
    #: bootstrap: true means "launchd should hold this, tell me if it
    #: does not".
    enabled: bool = True

    #: The watcher must keep watching while the global stop is active. This
    #: defaults false and is valid only for the heartbeat; widening the
    #: exemption requires a code review, not one permissive YAML line.
    kill_switch_exempt: bool = False

    #: Repo-relative config files this RESIDENT RE-READS AT RUNTIME.
    #:
    #: THE LAW THIS SERVES, ruled three times (2026-09-04, 2026-09-08 on
    #: aset.yaml, 2026-09-09 on tunables.yaml): a config-shape change and
    #: the restart of every resident that reads that file are ONE ACTION.
    #: The 09-09 case is the one to remember — the 09-08 seat-usage deploy
    #: added a `TunableUnit.WINDOW` row to tunables.yaml and its plan said
    #: "nothing else is restarted". The ASET sheet re-reads that file on
    #: every request, through code that predated the enum value, so from
    #: roughly 19:00 to 07:06 the page he trades beside answered HTTP 200
    #: and refused every card. The deploy was right about its own job and
    #: wrong about everybody else's.
    #:
    #: EVERY ENTRY IS DERIVED FROM THE CODE, never guessed: a row here
    #: claims that a specific loader call reads a specific file on a
    #: request path, and the 2026-09-09 ops report cites file:line for
    #: each one. A guessed row is worse than an empty list, because
    #: `cobalt jobs readers` is trusted to be complete.
    #:
    #: ONE-SHOTS LEAVE IT EMPTY, and `cobalt validate` enforces that: a
    #: one-shot re-reads everything every time it runs, by definition —
    #: it starts, reads, exits. There is no stale process to restart, so
    #: rows here would be noise diluting the ones that mean something.
    #:
    #: KNOWN GAP, deliberately not papered over: this is RE-READS, not
    #: reads. A resident that loads a config ONCE AT STARTUP also needs a
    #: restart when it changes, and `com.cobalt.agent` (the old tree) is
    #: exactly that shape — it caches settings in a singleton at first
    #: construction (`cobalt_agent/config.py:410`). That wants its own
    #: field; see the 09-09 report's ESCALATE.
    reads: list[str] = Field(default_factory=list)
    #: Static Python roots used by `cobalt jobs restarts`. None means the
    #: declaration is missing and therefore conservatively restarts all.
    imports: Optional[list[str]] = None

    @model_validator(mode="after")
    def _shape_matches_kind(self) -> "JobSpec":
        if self.kill_switch_exempt and self.label != HEARTBEAT_LABEL:
            raise ValueError(
                f"{self.label}: `kill_switch_exempt` is reserved for "
                f"{HEARTBEAT_LABEL}; the stop must still stop every other job"
            )
        if self.kind is JobKind.ONE_SHOT and self.reads:
            raise ValueError(
                f"{self.label}: `reads` belongs to a RESIDENT. A one-shot re-reads "
                "everything every time it runs — there is no stale process to "
                "restart, so naming files here dilutes the rows that do mean "
                "something."
            )
        bad = [p for p in self.reads if Path(p).is_absolute() or ".." in Path(p).parts]
        if bad:
            raise ValueError(
                f"{self.label}: `reads` entries are REPO-RELATIVE with no `..`: {bad}"
            )
        if self.kind is JobKind.ONE_SHOT and self.schedule is None:
            raise ValueError(
                f"{self.label}: a one-shot needs a `schedule` — the MISSED probe "
                "asks 'should this have run by now', and without a schedule there "
                "is no answer, only silence."
            )
        if self.supervisor is Supervisor.PIDFILE and not self.pidfile:
            raise ValueError(f"{self.label}: supervisor `pidfile` needs a `pidfile` path")
        if self.supervisor is not Supervisor.PIDFILE and self.pidfile:
            raise ValueError(
                f"{self.label}: `pidfile` is set but the supervisor is "
                f"{self.supervisor} — nothing would read it."
            )
        return self

    @property
    def cadence(self) -> Optional[str]:
        return self.schedule.describe() if self.schedule else None

    @property
    def pidfile_path(self) -> Optional[Path]:
        return (REPO_ROOT / self.pidfile) if self.pidfile else None

    @property
    def plist_path(self) -> Path:
        return OPS_DIR / f"{self.label}.plist"


class JobRegistry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jobs: list[JobSpec] = Field(min_length=1)
    kill_phrase: str = Field(min_length=1)
    resume_phrase: str = Field(min_length=1)

    @model_validator(mode="after")
    def _unique_labels(self) -> "JobRegistry":
        labels = [j.label for j in self.jobs]
        dupes = sorted({l for l in labels if labels.count(l) > 1})
        if dupes:
            raise ValueError(f"duplicate job label(s): {dupes}")
        if self.kill_phrase.strip().upper() == self.resume_phrase.strip().upper():
            raise ValueError("kill_phrase and resume_phrase must differ")
        return self

    @property
    def by_label(self) -> dict[str, JobSpec]:
        return {j.label: j for j in self.jobs}

    def readers_of(self, path: str) -> list[JobSpec]:
        """Every RESIDENT that re-reads `path` at runtime — the jobs a
        change to that file must restart, in one action with the change.

        Normalised through `Path` so `./configs/cobalt/x.yaml` and
        `configs/cobalt/x.yaml` are the same file: an operator typing a
        path from a `git status` line must not get an empty answer on a
        leading `./`.
        """
        wanted = Path(path).as_posix().lstrip("./")
        return [
            j
            for j in self.jobs
            if any(Path(p).as_posix() == wanted for p in j.reads)
        ]

    @property
    def read_paths(self) -> list[str]:
        """Every path any row claims to re-read, deduplicated."""
        return sorted({p for j in self.jobs for p in j.reads})

    def spec(self, label: str) -> JobSpec:
        try:
            return self.by_label[label]
        except KeyError:
            raise JobConfigError(
                f"unknown job label {label!r}. Registered: "
                f"{', '.join(sorted(self.by_label))} (configs/cobalt/jobs.yaml)."
            ) from None


def load_job_registry() -> JobRegistry:
    if not CONFIG_PATH.exists():
        raise JobConfigError(
            f"job registry not found: {CONFIG_PATH}. F17 has no built-in job list: "
            "a job nobody declared is a job nobody watches."
        )
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    if not isinstance(raw, dict):
        raise JobConfigError(f"{CONFIG_PATH}: expected a YAML mapping")
    try:
        return JobRegistry(**raw)
    except ValidationError as e:
        raise JobConfigError(f"{CONFIG_PATH}: invalid job registry:\n{e}") from e


__all__ = [
    "CONFIG_PATH",
    "HEARTBEAT_LABEL",
    "OPS_DIR",
    "WEEKDAY_NAMES",
    "parse_window",
    "JobConfigError",
    "JobRegistry",
    "JobSpec",
    "Schedule",
    "load_job_registry",
]
