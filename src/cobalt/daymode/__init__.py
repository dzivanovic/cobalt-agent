"""F6 two-stage day mode + `.htk` match check (Charter §3 F6, M4).

* `config.py`  — the ladder is DERIVED (`reduced` + aset.yaml's sheet
  order), and `reduced` is a ROLE whose sheet is a config pointer.
  Nothing here names `half` or `full` as a literal.
* `propose.py` — stage 1 is a system rule (lowest enabled, no input
  asked); stage 2 is the 09:00 proposal with an assembled reason.
* `match.py`   — the loaded `.htk` is ATTESTED, never read (Cobalt does
  not touch DAS), and a mismatch refuses card creation.
* `store.py`   — one `day_modes` row per trading day; stage 1 has none.
"""

from .config import REDUCED, DayModeConfig, load_daymode_config
from .match import SheetMismatch, assert_grade_allowed, assert_sheet_matches
from .propose import (
    BAND_MAX_KEY,
    BAND_MIN_KEY,
    NO_PRIOR_DRC,
    Proposal,
    decided_or_stage1,
    prior_trading_day,
    propose,
    stage1_mode,
)
from .store import DayModeError, DayModeStore

__all__ = [
    "BAND_MAX_KEY",
    "BAND_MIN_KEY",
    "NO_PRIOR_DRC",
    "REDUCED",
    "DayModeConfig",
    "DayModeError",
    "DayModeStore",
    "Proposal",
    "SheetMismatch",
    "assert_grade_allowed",
    "assert_sheet_matches",
    "decided_or_stage1",
    "load_daymode_config",
    "prior_trading_day",
    "propose",
    "stage1_mode",
]
