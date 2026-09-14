"""day-open's own ruled numbers — L53: ceilings and cadences are ruled,
never settled silently in a config file, but they still live in
`tunables.yaml` as rows with a named consumer (F16), the same as every
other threshold in the engine.

Two new rows (`dayopen.*`); the rest of day-open's thresholds REUSE
existing tunables rather than duplicating them (L3 one-path rule):

    session.premarket_open     (04:00 ET) — C2/C3's "has the scan started"
    session.aftermarket_close  (20:00 ET) — C6's "previous evening" anchor

Both are read through `cobalt.session.clock`, not re-declared here.
"""

from __future__ import annotations

from dataclasses import dataclass

from cobalt.taxonomy.loader import TaxonomyConfigError, load_tunables
from cobalt.taxonomy.tunables import TunableUnit

#: C4 EXPECT: `system.session_blocks` rows with actor `^vaultwrite:heartbeat:`
#: for the report date. A moving baseline (RULED 2026-09-14, A) — never a
#: literal in checks.py.
C4_EXPECTED_KEY = "dayopen.c4_expected_session_blocks"

#: C6 EXPECT: no gap between two beats since the prior evening wider than
#: this many minutes.
C6_MAX_GAP_KEY = "dayopen.c6_max_gap_min"

DAYOPEN_KEYS = (C4_EXPECTED_KEY, C6_MAX_GAP_KEY)


class DayOpenConfigError(RuntimeError):
    """A day-open tunable is missing or the wrong shape — crash, never guess."""


@dataclass(frozen=True)
class DayOpenConfig:
    c4_expected_session_blocks: int
    c6_max_gap_min: int


def load_dayopen_config() -> DayOpenConfig:
    try:
        registry = load_tunables().by_key
    except TaxonomyConfigError as e:
        raise DayOpenConfigError(f"day-open tunables unavailable: {e}") from e

    def _int(key: str, unit: TunableUnit) -> int:
        row = registry.get(key)
        if row is None:
            raise DayOpenConfigError(
                f"tunable {key!r} is missing from tunables.yaml — day-open has no "
                "built-in default (F16)."
            )
        if row.unit is not unit:
            raise DayOpenConfigError(
                f"tunable {key!r} has unit {row.unit.value!r}, expected {unit.value!r}"
            )
        return int(row.value)

    return DayOpenConfig(
        c4_expected_session_blocks=_int(C4_EXPECTED_KEY, TunableUnit.COUNT),
        c6_max_gap_min=_int(C6_MAX_GAP_KEY, TunableUnit.MIN),
    )


__all__ = [
    "C4_EXPECTED_KEY",
    "C6_MAX_GAP_KEY",
    "DAYOPEN_KEYS",
    "DayOpenConfig",
    "DayOpenConfigError",
    "load_dayopen_config",
]
