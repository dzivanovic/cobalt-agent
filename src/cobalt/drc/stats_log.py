"""The stats-log parser (DRC D1-4) — his trade journal's daily log, one
row per trade (R91: entries, targets, assumed and realized R:R, MAE/MFE,
best exit, playbooks).

The file's own name and extension are never read; it reaches this module
only after `detect.detect_kind` classified it `stats_log` (R114).
"""

from __future__ import annotations

ACCOUNT_NAME = "Account Name"
SYMBOL = "Symbol"
SIDE = "Side"
OPEN_DATE = "Open Date"
OPEN_TIME = "Open Time"
CLOSE_DATE = "Close Date"
CLOSE_TIME = "Close Time"
ENTRY = "Entry Price"
EXIT = "Exit Price"
TARGET = "Initial Target"
ASSUMED_RR = "Reward Ratio"
REALIZED_RR = "Realized RR"
PRICE_MAE = "Price MAE"
PRICE_MFE = "Price MFE"
POSITION_MAE = "Position MAE"
POSITION_MFE = "Position MFE"
BEST_EXIT = "Best Exit"
BEST_EXIT_PRICE = "Best Exit Price"
BEST_EXIT_TIME = "Best Exit Time"
GROSS_PNL = "Gross P&L"
NET_PNL = "Net P&L"
COMMISSION = "Commission"
FEE = "Fee"
QUANTITY = "Quantity"
EXECUTIONS = "Executions"
PLAYBOOK = "Playbook"

#: Every non-empty column name E1's stats-log header shows, in its order,
#: EXCEPT the one column whose name carries a vendor's name (L31: never
#: in code — neither required nor read). THE one copy: `detect` imports
#: it, nothing retypes it (L3). No stop column: E1 has none (R17 (4)).
REQUIRED: tuple[str, ...] = (
    ACCOUNT_NAME,
    "Adjusted Cost",
    "Adjusted Proceeds",
    "Avg Buy Price",
    "Avg Sell Price",
    "Exit Efficiency",
    BEST_EXIT,
    BEST_EXIT_PRICE,
    BEST_EXIT_TIME,
    CLOSE_DATE,
    CLOSE_TIME,
    COMMISSION,
    "Custom Tags",
    "Duration",
    ENTRY,
    EXECUTIONS,
    EXIT,
    GROSS_PNL,
    "Trade Risk",
    TARGET,
    "Instrument",
    "Spread Type",
    "Mistakes",
    NET_PNL,
    "Net ROI",
    OPEN_DATE,
    OPEN_TIME,
    "Pips",
    ASSUMED_RR,
    "Points",
    POSITION_MAE,
    POSITION_MFE,
    PRICE_MAE,
    PRICE_MFE,
    REALIZED_RR,
    "Return Per Pip",
    "Reviewed",
    "Setups",
    SIDE,
    "Status",
    PLAYBOOK,
    SYMBOL,
    "Ticks Value",
    "Ticks Per Contract",
    FEE,
    "Swap",
    "Rating",
    QUANTITY,
)

#: What the trade match reads (D1-4). A `partial` stats log missing any of
#: these leaves every row `unmatched — missing: <columns>` (R17 (5)).
MATCH_INPUTS: tuple[str, ...] = (SYMBOL, SIDE, OPEN_DATE, OPEN_TIME)

__all__ = ["MATCH_INPUTS", "REQUIRED"]
