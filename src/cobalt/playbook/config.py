"""F23 config: `configs/cobalt/playbook.yaml`, its own Pydantic family (L10).

`extra="forbid"`, strict types, and no default for any key: a typo or a
missing line fails the run loud (L1) instead of rendering with a guessed
value. Loaded inside `job_run` by the command, so a bad file is a failed
job row. No tunables rows (FINAL C7): these are render settings, not
trading thresholds.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "playbook.yaml"


class PlaybookConfigError(RuntimeError):
    """The playbook config file is missing or is not a mapping."""


class PlaybookConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    #: Cards per family deck, newest first; null = every card (FINAL [F-03]).
    latest_per_family: Optional[int] = Field(..., gt=0)
    #: Card rows per table slide. UNVERIFIED layout (E2, his eyes).
    rows_per_slide: int = Field(..., gt=0)
    #: `why` is cut to this many characters plus `…`. UNVERIFIED layout (E2).
    why_max_chars: int = Field(..., gt=0)
    #: Repo-relative (or absolute) folder the dated deck folders go under.
    out_dir: str = Field(..., min_length=1)

    def out_path(self) -> Path:
        path = Path(self.out_dir)
        return path if path.is_absolute() else REPO_ROOT / path


def load_playbook_config(path: Path = CONFIG_PATH) -> PlaybookConfig:
    """Read and validate the file. A bad key or type raises `ValidationError`."""
    if not path.exists():
        raise PlaybookConfigError(f"playbook config not found: {path}")
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise PlaybookConfigError(f"{path}: expected a YAML mapping, got {type(raw).__name__}")
    return PlaybookConfig.model_validate(raw)


__all__ = ["CONFIG_PATH", "PlaybookConfig", "PlaybookConfigError", "load_playbook_config"]
