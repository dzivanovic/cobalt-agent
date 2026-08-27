"""Watchlist config loader — config-as-code (TRIAGE cross-cutting law).

Single source: configs/cobalt/watchlists.yaml. Pydantic-validated on
load; a bad or missing file crashes with the file path and detail — no
silent fallback. configs/cobalt/ is a second sanctioned new-core config
location alongside configs/dev/ (CLAUDE.md's config boundary law) — the
old loader's glob (configs/*.yaml) is top-level only and never reaches
either subdirectory.
"""

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from .models import Interval

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "watchlists.yaml"


class ConfigError(RuntimeError):
    """Config missing or invalid — crash loudly."""


class Tier(BaseModel):
    model_config = ConfigDict(extra="forbid")

    description: str = Field(min_length=1)
    intervals: list[Interval]
    tickers: list[str]


class WatchlistsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tier_a: Tier
    tier_b: Tier
    tier_c: Tier

    def archive_targets(self) -> list[tuple[str, Interval]]:
        """Every (ticker, interval) pair this config says to archive.

        tier_c is deliberately excluded (no archiving) — its presence
        in the config is for future use only.
        """
        targets: list[tuple[str, Interval]] = []
        for tier in (self.tier_a, self.tier_b):
            for ticker in tier.tickers:
                for interval in tier.intervals:
                    targets.append((ticker, interval))
        return targets

    def backfill_targets(self, ticker: str) -> list[tuple[str, Interval]]:
        """All of tier_a's intervals for one ticker (the on-demand backfill path)."""
        return [(ticker, interval) for interval in self.tier_a.intervals]


def load_config() -> WatchlistsConfig:
    if not CONFIG_PATH.exists():
        raise ConfigError(f"Watchlists config not found: {CONFIG_PATH}.")
    raw = yaml.safe_load(CONFIG_PATH.read_text())
    if not isinstance(raw, dict):
        raise ConfigError(f"{CONFIG_PATH}: expected a YAML mapping, got {type(raw).__name__}")
    try:
        return WatchlistsConfig(**raw)
    except ValidationError as e:
        raise ConfigError(f"{CONFIG_PATH}: invalid watchlists config:\n{e}") from e
