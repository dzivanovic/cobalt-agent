"""Pydantic models for the Bar Archiver."""

from __future__ import annotations

from datetime import timezone
from decimal import Decimal
from enum import Enum

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_validator


class Interval(str, Enum):
    """The only intervals this archiver ever requests or stores.

    Deliberately excludes h/d/w/m: hourly isn't used by any tier, and
    daily/weekly/monthly are never archived (Finviz serves 10y+ of
    those on demand — DATA-SOURCE-MEMO.md). A validated enum, not a
    free string — the footgun law: bare/unrecognized `p=` values
    silently return daily data from Finviz with no error.
    """

    I1 = "i1"
    I2 = "i2"
    I5 = "i5"
    I15 = "i15"
    I30 = "i30"


class Bar(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ticker: str = Field(min_length=1, max_length=12)
    interval: Interval
    # ADR-0007: tz-aware ONLY, and normalized to UTC. A naive datetime is
    # how 4.75M rows came to hold ET digits under a `+00` label — psycopg
    # hands a naive value to `timestamptz` and Postgres stamps it with the
    # session TimeZone, silently. `AwareDatetime` makes that a loud
    # Pydantic failure at the boundary instead of a wrong row three weeks
    # later.
    ts: AwareDatetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int = Field(ge=0)

    @field_validator("ts")
    @classmethod
    def _to_utc(cls, v):
        """Store one representation. An aware value in any zone is
        accepted and converted; the column is UTC and so is the model."""
        return v.astimezone(timezone.utc)
