"""Pydantic models for the Bar Archiver."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


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
    ts: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int = Field(ge=0)
