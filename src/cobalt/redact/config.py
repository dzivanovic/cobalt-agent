"""F19 config: the outbound secret patterns, as data.

`configs/cobalt/redact.yaml`, Pydantic-validated on load. A regex that
does not compile CRASHES with its name, at load, rather than silently
matching nothing forever — a guard that fails open is worse than no
guard, because it is trusted.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "redact.yaml"

#: The group name a pattern declares when only PART of its match is the
#: secret — `postgresql://user:PASSWORD@host` keeps everything but the
#: password, because an unreadable DSN is a redactor people route around.
SECRET_GROUP = "secret"


class RedactConfigError(RuntimeError):
    """Missing/invalid redaction config — crash, never fall back."""


class Pattern(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    regex: str = Field(min_length=1)
    because: str = Field(min_length=1)

    @field_validator("regex")
    @classmethod
    def _compiles(cls, v: str) -> str:
        try:
            re.compile(v)
        except re.error as e:
            raise ValueError(f"regex does not compile: {e}") from e
        return v

    @property
    def compiled(self) -> re.Pattern:
        return re.compile(self.regex)

    @property
    def replaces_whole_match(self) -> bool:
        return SECRET_GROUP not in self.compiled.groupindex


class RedactConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    placeholder: str = Field(min_length=1)
    literal_min_length: int = Field(ge=4)
    patterns: list[Pattern] = Field(min_length=1)

    def placeholder_for(self, name: str) -> str:
        return self.placeholder.format(name=name)

    @field_validator("patterns")
    @classmethod
    def _unique_names(cls, v: list[Pattern]) -> list[Pattern]:
        names = [p.name for p in v]
        dupes = sorted({n for n in names if names.count(n) > 1})
        if dupes:
            raise ValueError(f"duplicate pattern name(s): {dupes}")
        return v

    @field_validator("placeholder")
    @classmethod
    def _names_the_kind(cls, v: str) -> str:
        if "{name}" not in v:
            raise ValueError(
                "placeholder must contain '{name}'. An operator has to learn WHICH "
                "kind of secret was about to leave — that is the whole diagnostic "
                "value a redaction leaves behind."
            )
        return v


def load_redact_config() -> RedactConfig:
    if not CONFIG_PATH.exists():
        raise RedactConfigError(
            f"redaction config not found: {CONFIG_PATH}. F19 has no built-in "
            "pattern set: a guard whose rules are invisible is a guard nobody "
            "can audit."
        )
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    if not isinstance(raw, dict) or "redact" not in raw:
        raise RedactConfigError(f"{CONFIG_PATH}: expected a 'redact' mapping")
    try:
        return RedactConfig(**raw["redact"])
    except ValidationError as e:
        raise RedactConfigError(f"{CONFIG_PATH}: invalid redaction config:\n{e}") from e


__all__ = [
    "CONFIG_PATH",
    "SECRET_GROUP",
    "Pattern",
    "RedactConfig",
    "RedactConfigError",
    "load_redact_config",
]
