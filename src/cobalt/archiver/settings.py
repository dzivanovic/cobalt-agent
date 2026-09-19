"""The archiver's engine tunables — ONE Pydantic model, read through the
ONE tunables loader (spec §10; L3, L10, L53).

WHY THIS MODULE EXISTS AT ALL. The append-only redesign
(`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md`) adds a
WRITE MODE to a job that writes market history every night, and L7 says
a flip from one source of truth to another is never a default that
drifted — it is a shadow run, numbers, and the owner's ruling. So the
mode is a config row with exactly two legal spellings, validated on
load, printed by `cobalt validate`, and pinned to `upsert` by a test.

THERE IS NO SECOND YAML READER HERE (L3). `configs/cobalt/taxonomy/
tunables.yaml` is the registry that already carries
`radar.poll_overlap_bars`; this module reads it through
`cobalt.taxonomy.loader.load_tunables()` exactly as `radar/config.py`
does, and adds a schema on top.

FAIL LOUD, NAMING THE KEY (L1). Every refusal below names the tunables
key an operator has to go and fix — `archiver.write_mode`, not
`write_mode`. A missing row is a crash, never a built-in default: a
defaulted write mode is the one failure this whole design exists to
make impossible.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

from cobalt.taxonomy.loader import TaxonomyConfigError, load_tunables
from cobalt.taxonomy.tunables import TunableRow, TunableUnit


class ArchiverSettingsError(RuntimeError):
    """A tunables row the archiver needs is missing, mistyped or illegal."""


class WriteMode(str, Enum):
    """The nightly write path. EXACTLY these two spellings (§10).

    `upsert` is today's behaviour byte for byte (§5, mode isolation):
    the whole export through `ON CONFLICT DO UPDATE`. `append` is the
    design's night: only bars that do not exist are inserted, and no
    stored row is ever rewritten.
    """

    UPSERT = "upsert"
    APPEND = "append"


class ShadowCompare(str, Enum):
    """The pre-write shadow comparison, the evidence for the switch (§5).

    `off` is the operational lever if the shadow read ever costs a
    night (O-6): it turns the read off without deploying code.
    """

    ON = "on"
    OFF = "off"


#: The seven rows this module reads, with the unit each one must carry.
#: The unit check is not ceremony: a `min` row silently read as a
#: `count` is how a ten-minute quiet window becomes ten of something
#: else.
ARCHIVER_TUNABLE_UNITS: dict[str, TunableUnit] = {
    "archiver.write_mode": TunableUnit.LABEL,
    "archiver.shadow_compare": TunableUnit.LABEL,
    "archiver.shadow_statement_timeout_s": TunableUnit.COUNT,
    "archiver.shadow_retention_nights": TunableUnit.COUNT,
    "archiver.repair.quiet_before_open_min": TunableUnit.MIN,
    "archiver.repair.quiet_after_cycle_min": TunableUnit.MIN,
    "archiver.repair.cycle_max_min": TunableUnit.MIN,
}

#: `archiver.repair.<name>` -> the field of `RepairSettings`.
_REPAIR_FIELDS = {
    "archiver.repair.quiet_before_open_min": "quiet_before_open_min",
    "archiver.repair.quiet_after_cycle_min": "quiet_after_cycle_min",
    "archiver.repair.cycle_max_min": "cycle_max_min",
}

#: `<top-level key>` -> the field of `ArchiverSettings`.
_TOP_FIELDS = {
    "archiver.write_mode": "write_mode",
    "archiver.shadow_compare": "shadow_compare",
    "archiver.shadow_statement_timeout_s": "shadow_statement_timeout_s",
    "archiver.shadow_retention_nights": "shadow_retention_nights",
}

#: field -> the tunables key it came from, for error messages.
_FIELD_KEYS = {
    **{field: key for key, field in _TOP_FIELDS.items()},
    **{field: key for key, field in _REPAIR_FIELDS.items()},
}


def _positive_int(value: object, key: str) -> int:
    """A count of whole minutes or seconds. `bool` is not an integer here
    and `"10"` is not a number — a YAML row that quotes its value is a
    row somebody edited by hand, and coercing it hides that."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(
            f"{key} must be a positive INTEGER, got "
            f"{type(value).__name__} {value!r}"
        )
    if value <= 0:
        raise ValueError(f"{key} must be a positive integer, got {value!r}")
    return value


class RepairSettings(BaseModel):
    """The quiet window's three numbers (§8).

    `cycle_max_min` is a STATED UPPER BOUND on a radar cycle's length,
    not a measurement: the radar persists a cycle's START and never its
    completion (§2), so Q3 derives "the cycle has finished" from
    start + this bound. That is precisely Gemini's and Astra's dissent
    (§13) and spec O-2 — it is recorded here so the next reader of this
    file meets it before relying on the number.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    quiet_before_open_min: int
    quiet_after_cycle_min: int
    cycle_max_min: int

    @field_validator("quiet_before_open_min", "quiet_after_cycle_min", "cycle_max_min", mode="before")
    @classmethod
    def _positive(cls, v, info):
        return _positive_int(v, _FIELD_KEYS[info.field_name])


class ArchiverSettings(BaseModel):
    """Spec §10's seven keys, resolved once per process."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    write_mode: WriteMode
    shadow_compare: ShadowCompare
    shadow_statement_timeout_s: int
    shadow_retention_nights: int
    repair: RepairSettings

    @field_validator("write_mode", mode="before")
    @classmethod
    def _exact_write_mode(cls, v):
        """No `strip()`, no `lower()`, no coercion (L1).

        `Append`, ` upsert` and `""` are refused rather than repaired,
        because the repair a human would expect ("they obviously meant
        append") is exactly the silent switch of the production write
        path that L7 forbids.
        """
        legal = [m.value for m in WriteMode]
        if not isinstance(v, str) or v not in legal:
            raise ValueError(
                f"archiver.write_mode must be EXACTLY one of {legal} — got "
                f"{v!r}. Case, surrounding whitespace and an empty value are "
                "all refused: the write mode of the nightly archiver is the "
                "owner's ruling (L7), never a near-miss that was tidied up."
            )
        return v

    @field_validator("shadow_compare", mode="before")
    @classmethod
    def _exact_shadow_compare(cls, v):
        legal = [m.value for m in ShadowCompare]
        if not isinstance(v, str) or v not in legal:
            raise ValueError(
                f"archiver.shadow_compare must be EXACTLY one of {legal} — got {v!r}"
            )
        return v

    @field_validator("shadow_statement_timeout_s", "shadow_retention_nights", mode="before")
    @classmethod
    def _positive(cls, v, info):
        return _positive_int(v, _FIELD_KEYS[info.field_name])

    @property
    def shadow_enabled(self) -> bool:
        """Whether tonight writes a shadow artifact.

        §5: the shadow compare is the evidence for the switch and runs
        only in `upsert` mode. In `append` the same comparison IS the
        gate, so the key is ignored there rather than doubling the read.
        """
        return self.write_mode is WriteMode.UPSERT and self.shadow_compare is ShadowCompare.ON


def _value(registry: dict[str, TunableRow], key: str) -> object:
    row = registry.get(key)
    if row is None:
        raise ArchiverSettingsError(
            f"tunables.yaml: missing {key} — the archiver reads every one of "
            f"its {len(ARCHIVER_TUNABLE_UNITS)} settings from config and has "
            "no built-in default (L1, L10)."
        )
    expected = ARCHIVER_TUNABLE_UNITS[key]
    if row.unit is not expected:
        raise ArchiverSettingsError(
            f"tunables.yaml: {key} has unit {row.unit.value!r}, expected "
            f"{expected.value!r}"
        )
    return row.value


def load_archiver_settings(
    registry: dict[str, TunableRow] | None = None,
) -> ArchiverSettings:
    """Resolve spec §10's seven keys into the one settings model.

    `registry` is a TEST seam (the `by_key` mapping the loader already
    returns); production passes nothing and reads the shipped file.
    """
    if registry is None:
        try:
            registry = load_tunables().by_key
        except TaxonomyConfigError as e:
            raise ArchiverSettingsError(f"archiver settings unavailable: {e}") from e

    payload = {field: _value(registry, key) for key, field in _TOP_FIELDS.items()}
    payload["repair"] = {
        field: _value(registry, key) for key, field in _REPAIR_FIELDS.items()
    }
    try:
        return ArchiverSettings(**payload)
    except ValidationError as e:
        raise ArchiverSettingsError(
            "tunables.yaml: invalid archiver settings:\n" + _name_the_keys(e)
        ) from e


def _name_the_keys(error: ValidationError) -> str:
    """Pydantic reports `write_mode`; an operator needs `archiver.write_mode`.

    The mapping is done here rather than with validation aliases so that
    the nested `repair.*` rows read the same way as the top-level ones
    and there is one place to look when a message is wrong.
    """
    lines = []
    for item in error.errors():
        loc = [str(part) for part in item["loc"] if not str(part).startswith("function-")]
        field = loc[-1] if loc else ""
        key = _FIELD_KEYS.get(field, field)
        lines.append(f"  {key}: {item['msg']}")
    return "\n".join(lines)


def validate_command_lines() -> list[str]:
    """What `cobalt validate` prints for this config family (L10).

    A list of lines rather than `print` calls so the gate is testable
    without running the whole F16 sweep (which reads the vault).
    """
    settings = load_archiver_settings()
    return [
        "",
        f"Archiver (spec §10): {len(ARCHIVER_TUNABLE_UNITS)} tunables rows resolved.",
        f"  archiver.write_mode = {settings.write_mode.value} "
        f"(legal: {', '.join(m.value for m in WriteMode)}; the switch to "
        "'append' is the owner's ruling on the shadow numbers, L7)",
        f"  archiver.shadow_compare = {settings.shadow_compare.value} "
        f"-> shadow artifact tonight: {'yes' if settings.shadow_enabled else 'no'}",
        f"  archiver.shadow_statement_timeout_s = {settings.shadow_statement_timeout_s}",
        f"  archiver.shadow_retention_nights = {settings.shadow_retention_nights}",
        f"  archiver.repair.quiet_before_open_min = {settings.repair.quiet_before_open_min}",
        f"  archiver.repair.quiet_after_cycle_min = {settings.repair.quiet_after_cycle_min}",
        f"  archiver.repair.cycle_max_min = {settings.repair.cycle_max_min} "
        "(a STATED upper bound on a radar cycle, not a measurement — spec O-2)",
    ]


__all__ = [
    "ARCHIVER_TUNABLE_UNITS",
    "ArchiverSettings",
    "ArchiverSettingsError",
    "RepairSettings",
    "ShadowCompare",
    "WriteMode",
    "load_archiver_settings",
    "validate_command_lines",
]
