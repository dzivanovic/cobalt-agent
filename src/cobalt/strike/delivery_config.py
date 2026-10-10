"""The strike delivery numbers and the hotkey label (S4-P2 S5).

`configs/cobalt/strike.yaml`, read by the ASET sheet (`aset/strike.py`): the
stream's tail and keepalive, the phone fallback's delay, and the hotkey
template (Charter §5 #4). Defaults live in the model, so a missing key — or a
missing file, said in one logged line — never breaks the running sheet; an
extra key, or a template naming a field it cannot fill, is refused by name.

Imports nothing of the detector: the sheet loads this module, never the
strike loop (`strike/__init__.py` imports nothing).
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from loguru import logger
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "strike.yaml"

#: What the alert and the DM say for a card with no `sheet_mode` or no
#: `sized_grade`: shown, never guessed.
UNSIZED = "n/a — unsized"
_FIELDS = {"DAYMODE": "", "KEY": "", "SIDE": ""}


class DeliveryConfigError(RuntimeError):
    """`strike.yaml` holds a key or a value the model refuses."""


class DeliverySettings(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    stream_tail_ms: int = Field(default=500, gt=0)
    keepalive_s: int = Field(default=15, gt=0)
    dm_after_s: int = Field(default=10, gt=0)
    hotkey_template: str = Field(default="{DAYMODE}-{KEY}-{SIDE}", min_length=1)

    @field_validator("hotkey_template")
    @classmethod
    def _fillable(cls, value: str) -> str:
        try:
            value.format(**_FIELDS)
        except (KeyError, IndexError, ValueError) as e:
            raise ValueError(f"names a field other than DAYMODE, KEY, SIDE ({e!r})") from None
        return value


def load_delivery_config(path: Path = CONFIG_PATH) -> DeliverySettings:
    if not path.exists():
        logger.warning("strike delivery: {} not found — the model defaults are used ({})", path,
                       DeliverySettings().model_dump())
        return DeliverySettings()
    raw = yaml.safe_load(path.read_text()) or {}
    if not isinstance(raw, dict):
        raise DeliveryConfigError(f"{path}: expected a mapping, got {type(raw).__name__}")
    try:
        return DeliverySettings(**raw)
    except ValidationError as e:
        named = "; ".join(f"{'.'.join(str(p) for p in err['loc'])}: {err['msg']}" for err in e.errors())
        raise DeliveryConfigError(f"{path}: refused — {named}") from e


def hotkey(template: str, *, sheet_mode: Optional[str], sized_grade: Optional[str], direction: str) -> str:
    """The template filled from the card, upper-cased; `UNSIZED` when the card
    carries no `sheet_mode` or no `sized_grade`."""
    if not sheet_mode or not sized_grade:
        return UNSIZED
    return template.format(DAYMODE=str(sheet_mode), KEY=str(sized_grade), SIDE=str(direction)).upper()


__all__ = ["CONFIG_PATH", "DeliveryConfigError", "DeliverySettings", "UNSIZED", "hotkey", "load_delivery_config"]
