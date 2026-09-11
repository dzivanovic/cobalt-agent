"""Resolve the mandatory live/sim stamp for a card's trading day."""

from __future__ import annotations

from datetime import date


class AccountModeUnresolved(RuntimeError):
    """Neither a valid day override nor standing account mode exists."""


def _valid(value, source: str, day: date) -> str | None:
    if value is None:
        return None
    if value not in {"live", "sim"}:
        raise AccountModeUnresolved(
            f"account mode refused for {day}: {source} contains invalid value {value!r}; "
            "only live or sim is valid"
        )
    return value


def resolve(conn, day: date) -> str:
    """Day override, then standing trader setting; otherwise refuse."""
    row = conn.execute(
        "SELECT account_mode FROM day_modes WHERE trade_date = %s", (day,)
    ).fetchone()
    override = _valid(row[0] if row else None, "day_modes.account_mode", day)
    if override is not None:
        return override
    row = conn.execute(
        "SELECT value FROM trader_settings WHERE key = %s", ("aset.account_mode",)
    ).fetchone()
    standing = _valid(row[0] if row else None, "trader_settings['aset.account_mode']", day)
    if standing is not None:
        return standing
    raise AccountModeUnresolved(
        f"account mode refused for {day}: day_modes.account_mode is empty and "
        "trader_settings['aset.account_mode'] is empty; no card row was written"
    )


__all__ = ["AccountModeUnresolved", "resolve"]
