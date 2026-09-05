"""F17 config: the job registry, `configs/cobalt/jobs.yaml`.

Pydantic-validated on load; a bad row CRASHES with its label. The
registry is the ONE place a job's kind, timeout, supervisor and schedule
are written down — the plist carries the schedule too, because launchd
cannot read YAML, and `cobalt validate` compares the two so a drift is
loud rather than discovered by a job that never fired.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from .models import JobKind, Supervisor

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "jobs.yaml"
OPS_DIR = REPO_ROOT / "ops"

#: launchd's weekday numbering, which this file mirrors: 1 = Monday.
WEEKDAY_NAMES = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 0: "Sun"}


class JobConfigError(RuntimeError):
    """Missing/invalid job registry — crash, never fall back."""


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

    @model_validator(mode="after")
    def _one_shape(self) -> "Schedule":
        forms = [bool(self.at), self.every_min is not None, bool(self.every_min_tunable)]
        if sum(forms) != 1:
            raise ValueError(
                "a schedule is exactly one of: `at` (+ weekdays), `every_min`, or "
                "`every_min_tunable`."
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

    def describe(self) -> str:
        """The human string that lands in `jobs.expected_cadence`."""
        if self.at:
            days = ", ".join(WEEKDAY_NAMES[d] for d in sorted(self.weekdays))
            return f"{days} {self.at} ET"
        return f"every {self.interval_minutes()} min"


class JobSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    label: str = Field(min_length=1)
    kind: JobKind
    supervisor: Supervisor
    timeout_s: int = Field(gt=0)
    what: str = Field(min_length=1)
    schedule: Optional[Schedule] = None
    pidfile: Optional[str] = None

    @model_validator(mode="after")
    def _shape_matches_kind(self) -> "JobSpec":
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
    "OPS_DIR",
    "WEEKDAY_NAMES",
    "JobConfigError",
    "JobRegistry",
    "JobSpec",
    "Schedule",
    "load_job_registry",
]
