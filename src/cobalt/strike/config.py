"""The strike numbers (S4-P1 T1, L53): four `tunables.yaml` rows, unit-checked.

No `strike.finviz_max_rpm` and no fixed poll interval (DECISION D2): the one
ceiling is `radar.finviz_max_rpm`, and the interval is derived from the
headroom the radar leaves (`detector.poll_interval`).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cobalt.taxonomy.loader import TUNABLES_PATH, load_tunables
from cobalt.taxonomy.tunables import TunableUnit

STRIKE_TUNABLE_UNITS = {
    "strike.poll_interval_min": TunableUnit.DURATION,
    "strike.max_armed": TunableUnit.COUNT,
    "strike.alert_criterion_s": TunableUnit.DURATION,
    "strike.missed_sweep_interval": TunableUnit.DURATION,
}


class StrikeConfigError(RuntimeError):
    """A strike row is missing, unmeasured or carries the wrong unit."""


@dataclass(frozen=True)
class StrikeSettings:
    poll_interval_min: int
    max_armed: int
    alert_criterion_s: int
    missed_sweep_interval: int


def check(path: Path = TUNABLES_PATH) -> StrikeSettings:
    """Every strike row present, measured and in its unit — else refused,
    naming the key or the unit."""
    registry = load_tunables(path).by_key
    values: dict[str, int] = {}
    for key, unit in STRIKE_TUNABLE_UNITS.items():
        row = registry.get(key)
        if row is None:
            raise StrikeConfigError(f"tunables.yaml: missing {key}")
        if row.unit is not unit:
            raise StrikeConfigError(f"tunables.yaml: {key} has unit {row.unit.value}, expected {unit.value}")
        if row.value is None:
            raise StrikeConfigError(f"tunables.yaml: {key} is unmeasured")
        values[key.removeprefix("strike.")] = int(row.value)
    return StrikeSettings(**values)


def validate_command_lines() -> list[str]:
    """What `cobalt validate` prints for the strike rows (the archiver's shape)."""
    settings = check()
    return [
        "",
        f"Strike (S4-P1): {len(STRIKE_TUNABLE_UNITS)} tunables rows resolved.",
        f"  strike.poll_interval_min = {settings.poll_interval_min} s (the floor under the derived interval)",
        f"  strike.max_armed = {settings.max_armed}",
        f"  strike.alert_criterion_s = {settings.alert_criterion_s} s",
        f"  strike.missed_sweep_interval = {settings.missed_sweep_interval} s",
        "  ceiling: radar.finviz_max_rpm, shared (no strike ceiling of its own)",
    ]


__all__ = ["STRIKE_TUNABLE_UNITS", "StrikeConfigError", "StrikeSettings", "check", "validate_command_lines"]
