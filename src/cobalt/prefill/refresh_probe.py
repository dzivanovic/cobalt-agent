"""`prefill probe <item>`: one F4 first-gate item, dev only (card 1047; F4 FINAL `## First-gate experiments`).

THE OUTPUT is ONE stdout line: `PROBE <item> OK <clause>` (exit 0),
`PROBE <item> FAIL <clause>` (exit 1) or `PROBE <item> NOT RUN — <reason>`
(exit 3). A clause carries names, counts, minutes and consumer names only:
never a URL, a query string, a token, a price or an env value.

THE BOUNDARY (the `checkpoint_probe.py` shape):
(a) DEV ONLY: `env.resolve_env()` must say `dev`; anything else is a FAIL
    line before anything is built or sent.
(b) NO NETWORK: every `httpx.AsyncClient` the run builds gets the probe's
    `httpx.MockTransport`; a request that reaches a real transport is
    stopped there and the line is `FAIL error network`.
(c) NO WRITE, NO DATABASE: no `VaultWriter`, no store, no `as_job`, no real
    token (the constructed one), no DM, no `launchctl`, no file written;
    loguru is off for `cobalt` while the run lasts (a fetch error names its
    URL).
(d) A crash is `FAIL error <ExceptionName>`, no message text.

X15 (F4-FINAL `:221`), IN PROCESS ON A VIRTUAL CLOCK (card DECISION 1): one
virtual `monotonic` / `sleep` / `now` drives three consumers from 08:40:00
ET on a constructed weekday to 08:46:00 ET:
- `radar`, a stand-in at its planned rpm through `finviz_get` (DECISION 2);
- `strike`, the real `StrikeDetector.tick` over 5 constructed ARMED cards,
  `fetch_bars`, a `TokenBucket` on the virtual clock;
- `refresh`, the real `_gated_fetch` at 08:43:00 ET: its gate, then its 3 GETs.
The mock transport counts every request (redirects included) per virtual
minute and answers 429 past the ceiling's 50th in a minute, as Finviz would.
OK iff no minute holds more than 50 and no 429 was answered.
"""

from __future__ import annotations

import asyncio
import contextvars
import heapq
import itertools
from collections import Counter
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal
from typing import Awaitable, Callable, Optional

import httpx
from loguru import logger

from cobalt import env

PROBE_ITEMS = ("X15",)
OK, FAIL, NOT_RUN = "OK", "FAIL", "NOT RUN"
EXIT = {OK: 0, FAIL: 1, NOT_RUN: 3}
#: L32: constructed values only.
TOKEN = "probe-token-constructed"
TICKERS = ("ZZA", "ZZB", "ZZC", "ZZD", "ZZE")
DAY = date(2026, 1, 6)
START = time(8, 40)
REFRESH_AT_S = 180
RUN_S = 360
#: FINAL :221's ceiling; the tunable must say the same or the item is not run.
FINAL_CEILING = 50
CONSEQUENCE = ("→ strike/refresh residual cannot ship as named; a strike-side reservation row on the F4 card "
               "before the plist loads (FINAL :221, L75)")
#: A fake clock that wakes exactly at a bucket's deficit can leave its token
#: at 0.9999… forever (float); real time always moves on.
_EPS = 1e-6
_MAX_SPINS = 100_000
_CONSUMER: contextvars.ContextVar[str] = contextvars.ContextVar("refresh_probe_consumer", default="unnamed")


@dataclass(frozen=True)
class X15Setup:
    """FINAL :221: 5 ARMED cards, the radar planned 40, ceiling 50.
    `redirects`: the mock answers the first n requests 302 (the tests')."""

    cards: int = 5
    radar_rpm: float = 40.0
    planned_rpm: float = 40.0
    headroom_rpm: float = 10.0
    redirects: int = 0


SETUP = X15Setup()


class ProbeRefused(RuntimeError):
    """The probe will not run here. Loud, as a FAIL line."""


class NotRun(RuntimeError):
    """The item cannot run its real shape here: a NOT RUN line, exit 3."""


class OffMock(httpx.TransportError):
    """A request reached a real transport; stopped before any connection."""


# ---------------------------------------------------------------------
# the virtual clock
# ---------------------------------------------------------------------


class VirtualClock:
    """`monotonic`, `sleep` and `now` on one virtual time line. `run` advances
    it only when every live task waits on its `sleep`."""

    def __init__(self, start: datetime):
        self.start = start
        self.t = 0.0
        self._waiters: list = []
        self._seq = itertools.count()

    def monotonic(self) -> float:
        return self.t

    def now(self) -> datetime:
        return self.start + timedelta(seconds=self.t)

    def minute(self) -> str:
        from cobalt.session import SessionClock

        return f"{SessionClock.to_et(self.now()):%H:%M}"

    async def sleep(self, seconds: float) -> None:
        fut = asyncio.get_running_loop().create_future()
        heapq.heappush(self._waiters, (self.t + max(0.0, seconds) + _EPS, next(self._seq), fut))
        await fut

    async def run(self, coros: list[Awaitable], until_s: float) -> None:
        tasks = [asyncio.ensure_future(c) for c in coros]
        spins = 0
        try:
            while any(not t.done() for t in tasks):
                live = sum(not t.done() for t in tasks)
                if len(self._waiters) < live:
                    spins += 1
                    if spins > _MAX_SPINS:
                        raise RuntimeError("virtual clock stalled")
                    await asyncio.sleep(0)
                    continue
                spins = 0
                when, _, fut = heapq.heappop(self._waiters)
                if when >= until_s:
                    break
                self.t = when
                fut.set_result(None)
                await asyncio.sleep(0)
        finally:
            for t in tasks:
                t.cancel()
            done = await asyncio.gather(*tasks, return_exceptions=True)
        for result in done:
            if isinstance(result, BaseException) and not isinstance(result, asyncio.CancelledError):
                raise result


# ---------------------------------------------------------------------
# the transport: the count, the ceiling, constructed bodies
# ---------------------------------------------------------------------


@dataclass(frozen=True)
class Hit:
    minute: str
    consumer: str
    path: str
    status: int


class ProbeTransport:
    """The one transport of the run. Records (virtual minute, consumer, path,
    status) per request, never the query; 429 past `ceiling` in a minute."""

    def __init__(self, clock: VirtualClock, ceiling: int, *, redirects: int = 0):
        self.clock = clock
        self.ceiling = ceiling
        self.redirects = redirects
        self.records: list[Hit] = []
        self.mock = httpx.MockTransport(self.handle)

    def handle(self, request: httpx.Request) -> httpx.Response:
        minute = self.clock.minute()
        in_minute = sum(1 for r in self.records if r.minute == minute)
        if in_minute >= self.ceiling:
            status, response = 429, httpx.Response(429, text="")
        elif self.redirects > 0:
            self.redirects -= 1
            status, response = 302, httpx.Response(302, headers={"location": str(request.url)})
        else:
            status, response = 200, httpx.Response(200, text=self._body(request))
        self.records.append(Hit(minute, _CONSUMER.get(), request.url.path, status))
        return response

    def _body(self, request: httpx.Request) -> str:
        path = request.url.path
        if path.endswith("/stock"):
            # one i1 bar a minute before the run, high under every card's entry: no cross.
            stamp = f"{DAY:%m/%d/%Y} {(datetime.combine(DAY, START) - timedelta(minutes=1)):%I:%M %p}"
            return f"Date,Open,High,Low,Close,Volume\n{stamp},9.85,9.90,9.80,9.85,1000\n"
        if path.endswith("/economic"):
            return f"Event,Date,Time,Impact,For,Actual,Expected,Prior\nZZZ index,{DAY.isoformat()},08:30,3,,,1.0%,0.9%\n"
        if path.endswith("/earnings"):
            return f"Date,Ticker,Company\n{DAY.isoformat()} BMO,ZZE,Constructed Co\n"
        return ("No.,Ticker,Company,Sector,Industry,Country,Market Cap,P/E,Price,Change,Volume\n"
                "1,SPY,C,S,I,USA,1,1,500.00,0.10%,1000\n2,QQQ,C,S,I,USA,1,1,400.00,0.20%,1000\n"
                "3,IWM,C,S,I,USA,1,1,200.00,0.30%,1000\n")


def _probe_client(transport: httpx.AsyncBaseTransport) -> type:
    """`httpx.AsyncClient` with the probe's transport, whatever the caller passes."""
    base = httpx.AsyncClient

    class ProbeClient(base):
        def __init__(self, *args, **kwargs):
            kwargs["transport"] = transport
            kwargs["trust_env"] = False
            super().__init__(*args, **kwargs)

    return ProbeClient


@contextmanager
def _patched(*triples):
    """Set (owner, name, value) for the run; restore every one after."""
    saved = [(owner, name, getattr(owner, name)) for owner, name, _ in triples]
    try:
        for owner, name, value in triples:
            setattr(owner, name, value)
        yield
    finally:
        for owner, name, value in reversed(saved):
            setattr(owner, name, value)


@contextmanager
def _boundary(transport: ProbeTransport, plan):
    """(b) and (c): every client on the mock, a real transport stopped, the
    constructed token, the plan the strike loop reads."""
    from cobalt.prefill import calendar, daily, market

    reached: list[str] = []

    async def no_network(self, request):
        reached.append(request.url.path)
        raise OffMock("a request reached a real transport")

    def no_network_sync(self, request):
        reached.append(request.url.path)
        raise OffMock("a request reached a real transport")

    async def token() -> str:
        return TOKEN

    with _patched(
        (httpx, "AsyncClient", _probe_client(transport.mock)),
        (httpx.AsyncHTTPTransport, "handle_async_request", no_network),
        (httpx.HTTPTransport, "handle_request", no_network_sync),
        (market, "resolve_token", token),
        (calendar, "resolve_token", token),
        (daily, "read_plan", lambda: plan),
    ):
        yield reached


# ---------------------------------------------------------------------
# X15
# ---------------------------------------------------------------------


class _ProbeDay:
    """The constructed weekday: a full trading day."""

    def is_trading_day(self, day) -> bool:
        return True

    def is_early_close(self, day) -> bool:
        return False

    def describe(self, day) -> str:
        return f"{day}: a trading day (probe stub)"


class _ArmedCards:
    """The strike store: 5 constructed ARMED cards; a transition is recorded,
    never written."""

    def __init__(self, cards):
        self.cards = list(cards)
        self.moves: list[int] = []

    def strike_cards(self):
        return list(self.cards)

    def transition(self, card_id, to_state, **kw):
        self.moves.append(card_id)
        return len(self.moves)


@dataclass(frozen=True)
class _ConstructedDef:
    """The loaded def of every probe card: only `trigger` is read (`detector.py:192`)."""

    trigger: object


@dataclass
class _Ledger:
    intervals: list = field(default_factory=list)
    refresh: Optional[object] = None


def _cards(n: int, start: datetime):
    from cobalt.strike.detector import StrikeCard

    return [StrikeCard(card_id=i + 1, ticker=TICKERS[i], direction="long", state="ARMED",
                       trade_def_slug="probe-constructed", trade_def_md5="0" * 32, entry=Decimal("10.00"),
                       created_at=start - timedelta(minutes=30), armed_at=start - timedelta(minutes=10))
            for i in range(n)]


async def _radar(clock: VirtualClock, rpm: float, get: Callable[..., Awaitable]) -> None:
    from cobalt.archiver.collector import CollectorError

    _CONSUMER.set("radar")
    spacing = 60 / rpm
    for k in itertools.count():
        await clock.sleep(max(0.0, k * spacing - clock.monotonic()))
        try:
            await get("/export/screener", {"v": "111"}, TOKEN)
        except CollectorError:
            pass


async def _strike(clock: VirtualClock, detector, ledger: _Ledger) -> None:
    _CONSUMER.set("strike")
    while True:
        started = clock.monotonic()
        report = await detector.tick()
        ledger.intervals.append(report.interval_s)
        await clock.sleep(max(0.0, started + detector.interval_s() - clock.monotonic()))


async def _refresh(clock: VirtualClock, ledger: _Ledger) -> None:
    from cobalt.prefill.daily import _gated_fetch

    _CONSUMER.set("refresh")
    await clock.sleep(REFRESH_AT_S - clock.monotonic())
    ledger.refresh = await _gated_fetch(clock.now())


def _ceiling() -> Optional[int]:
    from cobalt.taxonomy.loader import load_tunables

    raw = load_tunables().by_key["radar.finviz_max_rpm"].value
    return None if raw is None else int(raw)


def _clause(records: list[Hit], ledger: _Ledger, ceiling: int) -> tuple[str, str]:
    minutes = Counter(r.minute for r in records)
    consumers = Counter(r.consumer for r in records)
    throttled = Counter(r.consumer for r in records if r.status == 429)
    peak = max(minutes.values(), default=0)
    peak_at = next((m for m in sorted(minutes) if minutes[m] == peak), "-")
    stable = [s for s in ledger.intervals if s is not None]
    parts = [
        f"peak {peak}/min at {peak_at}",
        "per minute " + ", ".join(f"{m}={minutes[m]}" for m in sorted(minutes)),
        *(f"{c} {consumers[c]}" for c in ("radar", "strike", "refresh")),
        f"429 {sum(throttled.values())}"
        + (" (" + ", ".join(f"{c}={n}" for c, n in sorted(throttled.items())) + ")" if throttled else ""),
        f"strike interval {stable[-1] if stable else 'none'} s",
        "refresh gate admitted",
    ]
    clause = " · ".join(parts)
    if peak > ceiling or throttled:
        return FAIL, f"{clause} {CONSEQUENCE}"
    return OK, clause


def _x15(setup: X15Setup) -> tuple[str, str]:
    from cobalt.archiver.collector import fetch_bars, finviz_get
    from cobalt.radar.collector import TokenBucket
    from cobalt.session import SessionClock
    from cobalt.session.clock import ET
    from cobalt.strike.config import check
    from cobalt.strike.detector import DemandPlan, StrikeDetector
    from cobalt.taxonomy.trade_def import SimpleTrigger

    ceiling = _ceiling()
    if ceiling != FINAL_CEILING:
        raise NotRun(f"ceiling {ceiling}, not the FINAL's {FINAL_CEILING}")
    start = datetime.combine(DAY, START, tzinfo=ET).astimezone(timezone.utc)
    clock = VirtualClock(start)
    transport = ProbeTransport(clock, ceiling, redirects=setup.redirects)
    plan = DemandPlan(planned_rpm=setup.planned_rpm, headroom_rpm=setup.headroom_rpm)
    definition = _ConstructedDef(SimpleTrigger(type="bar_break", confirmation_policy={"type": "intrabar"}))
    detector = StrikeDetector(
        store=_ArmedCards(_cards(setup.cards, start)), fetch=fetch_bars, token=TOKEN,
        defs=lambda slug: ("0" * 32, definition) if slug == "probe-constructed" else None,
        stored_bars=lambda ticker, since, until: [], settings=check(), plan=lambda: plan,
        session_of=SessionClock.from_config(calendar=_ProbeDay()).session, now=clock.now,
        bucket_factory=lambda rpm: TokenBucket(rpm, monotonic=clock.monotonic, sleep=clock.sleep),
    )
    ledger = _Ledger()
    with _boundary(transport, plan) as reached:
        try:
            asyncio.run(clock.run([_radar(clock, setup.radar_rpm, finviz_get), _strike(clock, detector, ledger),
                                   _refresh(clock, ledger)], RUN_S))
        except Exception:
            if reached:
                return FAIL, "error network"
            raise
    if reached:
        return FAIL, "error network"
    if ledger.refresh is None:
        raise RuntimeError("the refresh never ran")
    if ledger.refresh.refused is not None:
        raise NotRun(f"refresh refused by the gate: {ledger.refresh.refused}")
    return _clause(transport.records, ledger, ceiling)


ITEMS: dict[str, Callable] = {"X15": _x15}
assert set(ITEMS) == set(PROBE_ITEMS), "PROBE_ITEMS and the probe's items disagree"


def _dev_only() -> None:
    try:
        mode = env.resolve_env()
    except env.EnvConfigError as e:
        raise ProbeRefused(str(e).split(". ")[0] + ".") from None
    if mode != env.DEV:
        raise ProbeRefused(f"{env.ENV_VAR}={mode} (dev only)")


def _verdict(item: str) -> tuple[str, str]:
    # a fetch error's log line names its URL; the probe's line carries counts only.
    logger.disable("cobalt")
    try:
        _dev_only()
        return ITEMS[item](SETUP)
    except ProbeRefused as e:
        return FAIL, f"refused: {e}"
    except NotRun as e:
        return NOT_RUN, f"— {e}"
    except Exception as e:  # noqa: BLE001 - a crash is a FAIL line; its message may carry a URL
        return FAIL, f"error {type(e).__name__}"
    finally:
        logger.enable("cobalt")


def main(item: str) -> int:
    verdict, clause = _verdict(item)
    clause = " ".join(clause.split())
    print(f"PROBE {item} {verdict} {clause}")
    return EXIT[verdict]


__all__ = ["PROBE_ITEMS", "ProbeTransport", "SETUP", "VirtualClock", "X15Setup", "main"]
