                f"({self._b['session.aftermarket_close']:%H:%M}) — on a full "
                "day market_reset begins the moment aftermarket ends"
            )

    # -- the day's shape ---------------------------------------------

    def windows_for(self, day: date) -> list[Window]:
        """The ordered [start, end) ET windows of `day`. Empty list = the
        whole day is overnight (weekend or holiday)."""
        if not self.calendar.is_trading_day(day):
            return []

        early = self.calendar.is_early_close(day)
        rth_close = self._b[
            "session.early_close.rth_close" if early else "session.rth_close"
        ]
        am_close = self._b[
            "session.early_close.aftermarket_close" if early else "session.aftermarket_close"
        ]
        return [
            Window(Session.PREMARKET, self._b["session.premarket_open"], self._b["session.rth_open"]),
            Window(Session.RTH, self._b["session.rth_open"], rth_close),
            Window(Session.AFTERMARKET, rth_close, am_close),
            Window(
                Session.MARKET_RESET,
                self._b["session.market_reset_open"],
                self._b["session.market_reset_close"],
            ),
        ]

    # -- the two questions -------------------------------------------

    def session(self, ts: datetime) -> Session:
        """The session `ts` falls in. `ts` MUST be tz-aware."""
        et = self.to_et(ts)
        for window in self.windows_for(et.date()):
            if window.start <= et.time() < window.end:
                return window.session
        return Session.OVERNIGHT

    def next_boundary(self, ts: datetime) -> tuple[datetime, Session]:
