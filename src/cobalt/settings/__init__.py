"""The trader's own settings — `"user".trader_settings` (ADR-0008 D3.4).

WHY THIS IS ITS OWN MODULE. The settings inside it belong to two
consumers (`cobalt.aset` and `cobalt.daymode`) and to neither of them:
the sheet dollars are read by the sizing engine, the DRC and the daily
note; the day-mode ladder is read by the proposer, the matcher and the
web sheet. Hanging the table off either module would make the other one
import it sideways for data it half-owns. It is the TRADER'S settings, so
it gets the module that says so.

The public surface is two objects and one law:

    TraderSettings.from_db(store)     the runtime's only reader
    TraderSettings.from_yaml(dir)     seeding only, never the runtime
    `cobalt settings load` / `show`   the one write path

and the law is that nothing in the runtime reads a YAML for these values
any more. `load_sheet_modes_config()` and `load_daymode_config()` keep
their names and their call sites — every one of them now resolves through
the database.
"""

from .models import (
    DAYMODE_KEYS,
    SETTING_KEYS,
    SHEET_KEYS,
    TraderSettings,
    TraderSettingsError,
)
from .store import TraderSettingsStore

__all__ = [
    "DAYMODE_KEYS",
    "SETTING_KEYS",
    "SHEET_KEYS",
    "TraderSettings",
    "TraderSettingsError",
    "TraderSettingsStore",
]
