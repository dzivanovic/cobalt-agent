"""The ONE reader of his fill-drift setting (S3 exits v3 §4; his ruling
O2 = A, `cto-2026-09-28.md` R35).

    "user".trader_settings  key  fills.drift_warning_pct   value  a JSON number > 0

The fill's drift warning is `distance_change_pct > P` with P this value
(`aset.engine.compute_fill_recompute`). There is NO committed default
(L53): a missing key returns None and the fill is still recorded — the
warning is simply not evaluated, and the sheet says so in the RE-READ
STOP banner (L1: loud, never a refusal). A PRESENT key whose value is not
a number > 0 raises naming the key (L1: a bad config crashes).

Not loadable yet: `cobalt settings load` accepts only the keys
`settings/models.py` declares, and that file is the DRC lane's to edit
(the S-MIG seam). Until the desk settles which lands first, the key is
absent and every fill carries the banner (C1 report, X-S).
"""

from __future__ import annotations

from decimal import Decimal
from typing import Any, Optional

from .models import TraderSettingsError

DRIFT_WARNING_PCT_KEY = "fills.drift_warning_pct"

#: The sheet's banner when the key is missing — the words are the design's.
DRIFT_NOT_EVALUATED = (
    f"RE-READ STOP — setting {DRIFT_WARNING_PCT_KEY} missing, warning not evaluated"
)

_ABSENT = object()


def _raw(source) -> Any:
    """The stored JSON value, or `_ABSENT`. `source` is an open connection
    (the fill reads inside its own transaction) or anything with
    `values()` — `TraderSettingsStore`, or a constructed store in tests
    (L69)."""
    if hasattr(source, "execute"):
        row = source.execute(
            "SELECT value FROM trader_settings WHERE key = %s", (DRIFT_WARNING_PCT_KEY,)
        ).fetchone()
        return _ABSENT if row is None else row[0]
    return source.values().get(DRIFT_WARNING_PCT_KEY, _ABSENT)


def drift_warning_pct(source) -> Optional[Decimal]:
    """P, or None when he has not set it. Raises `TraderSettingsError`
    naming the key when the stored value is not a number > 0."""
    value = _raw(source)
    if value is _ABSENT:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise TraderSettingsError(
            f"trader_settings[{DRIFT_WARNING_PCT_KEY!r}] = {value!r}: expected a number > 0 "
            "(the drift warning's percent threshold)"
        )
    pct = Decimal(str(value))
    if not pct.is_finite() or pct <= 0:
        raise TraderSettingsError(
            f"trader_settings[{DRIFT_WARNING_PCT_KEY!r}] = {value!r}: expected a number > 0 "
            "(the drift warning's percent threshold)"
        )
    return pct


__all__ = ["DRIFT_NOT_EVALUATED", "DRIFT_WARNING_PCT_KEY", "drift_warning_pct"]
