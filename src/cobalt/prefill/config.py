"""Config loaders for the Slice 2 prefill engine.

Config-as-code (TRIAGE cross-cutting law): three files, three Pydantic
schemas, all fail-loud on load — no silent defaults. The daily note's
own directory/filename pattern is deliberately NOT duplicated here; it
already lives in `AsetConfig.daily_note` (configs/dev/aset*.yaml) and
callers read that directly (one-path rule).
"""

from pathlib import Path
from typing import Literal, Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[3]
RULES_CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "rules.yaml"
STRATEGIES_CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "strategies.yaml"
PREFILL_CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "prefill.yaml"
TEMPLATES_DIR = REPO_ROOT / "configs" / "cobalt" / "templates"


class PrefillConfigError(RuntimeError):
    """Missing/invalid prefill config — crash, never fall back."""


RuleCategory = Literal[
    "process", "sizing", "time_window", "re_entry", "circuit_breaker", "hard_stop"
]


class RuleItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    category: RuleCategory
    text: str = Field(min_length=1)
    source: Optional[str] = None


class MantraItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    text: str = Field(min_length=1)


class RulesConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    rules: list[RuleItem] = Field(min_length=1)
    mantras: list[MantraItem] = Field(default_factory=list)


class StrategyItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    reversion: bool = False


class StrategiesConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    strategies: list[StrategyItem] = Field(default_factory=list)

    def is_reversion(self, strategy_name: Optional[str]) -> bool:
        if not strategy_name:
            return False
        name = strategy_name.strip()
        return any(s.name == name and s.reversion for s in self.strategies)


class PrefillPathsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    trades_dir: str = Field(min_length=1)
    review_dir: str = Field(min_length=1)
    drc_filename_pattern: str = Field(min_length=1)
    trade_filename_pattern: str = Field(min_length=1)


def _load_yaml_mapping(path: Path, top_key: str) -> dict:
    if not path.exists():
        raise PrefillConfigError(f"Config not found: {path}")
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict) or top_key not in raw:
        raise PrefillConfigError(f"{path}: expected a '{top_key}' mapping")
    return raw[top_key]


def load_rules_config() -> RulesConfig:
    if not RULES_CONFIG_PATH.exists():
        raise PrefillConfigError(f"Rules config not found: {RULES_CONFIG_PATH}")
    raw = yaml.safe_load(RULES_CONFIG_PATH.read_text())
    if not isinstance(raw, dict):
        raise PrefillConfigError(f"{RULES_CONFIG_PATH}: expected a YAML mapping")
    try:
        return RulesConfig(**raw)
    except ValidationError as e:
        raise PrefillConfigError(f"{RULES_CONFIG_PATH}: invalid rules config:\n{e}") from e


def load_strategies_config() -> StrategiesConfig:
    if not STRATEGIES_CONFIG_PATH.exists():
        raise PrefillConfigError(f"Strategies config not found: {STRATEGIES_CONFIG_PATH}")
    raw = yaml.safe_load(STRATEGIES_CONFIG_PATH.read_text())
    if not isinstance(raw, dict):
        raise PrefillConfigError(f"{STRATEGIES_CONFIG_PATH}: expected a YAML mapping")
    try:
        return StrategiesConfig(**raw)
    except ValidationError as e:
        raise PrefillConfigError(
            f"{STRATEGIES_CONFIG_PATH}: invalid strategies config:\n{e}"
        ) from e


def load_prefill_paths() -> PrefillPathsConfig:
    data = _load_yaml_mapping(PREFILL_CONFIG_PATH, "prefill")
    try:
        return PrefillPathsConfig(**data)
    except ValidationError as e:
        raise PrefillConfigError(
            f"{PREFILL_CONFIG_PATH}: invalid prefill paths config:\n{e}"
        ) from e
