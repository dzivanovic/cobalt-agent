"""Config for the seat-usage report: `configs/cobalt/seat_usage.yaml`.

Pydantic-validated on load; a bad file CRASHES with the field that is
wrong. No built-in defaults for anything the report's numbers depend on
— a report that silently priced a day from a fallback would be a report
nobody could audit.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "seat_usage.yaml"


class SeatUsageConfigError(RuntimeError):
    """Missing or invalid seat-usage config — crash, never fall back."""


class ToolSpec(BaseModel):
    """The external tool, as the four-gate law (L15) requires it pinned.

    `version` is compared against what the binary reports on every run.
    A mismatch is a CRASH: the value of pinning is that a bump is a
    decision somebody made, not a number that changed shape overnight.
    """

    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    version: str = Field(min_length=1)
    binary: str = Field(min_length=1)
    license: str = Field(min_length=1)
    offline: bool = True

    @property
    def binary_path(self) -> Path:
        return Path(self.binary).expanduser()


class SeatUsageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tool: ToolSpec
    report_path: str = Field(min_length=1)
    unpriced_is_loud: bool = True
    #: model name -> why its $0 is the true number
    zero_cost_models: dict[str, str] = Field(default_factory=dict)
    #: model name -> the role that model is INTENDED to hold. A hint.
    roles: dict[str, str] = Field(default_factory=dict)

    @property
    def report_file(self) -> Path:
        return REPO_ROOT / self.report_path

    def role_hint(self, model: str) -> Optional[str]:
        """The configured role for a model, or None — never a guess."""
        return self.roles.get(model)

    def is_free(self, model: str) -> bool:
        return model in self.zero_cost_models


def load_seat_usage_config(path: Optional[Path] = None) -> SeatUsageConfig:
    target = path or CONFIG_PATH
    if not target.exists():
        raise SeatUsageConfigError(
            f"seat-usage config not found: {target}. The report reads its tool "
            "pin, its role hints and its free-model list from config and has no "
            "built-in defaults."
        )
    raw = yaml.safe_load(target.read_text())
    if not isinstance(raw, dict):
        raise SeatUsageConfigError(f"{target}: expected a YAML mapping")
    try:
        return SeatUsageConfig(**raw)
    except ValidationError as e:
        raise SeatUsageConfigError(f"{target}: invalid seat-usage config:\n{e}") from e


__all__ = [
    "CONFIG_PATH",
    "REPO_ROOT",
    "SeatUsageConfig",
    "SeatUsageConfigError",
    "ToolSpec",
    "load_seat_usage_config",
]
