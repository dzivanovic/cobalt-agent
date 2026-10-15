"""The spend ledger — his cap, enforced in code, as TOTAL demand (L53).

    scratch/classify-spend.jsonl      one line per metered call

Plan §5: "Before ANY `--run`: projected cost of the run + everything
already in the ledger > cap → REFUSED, zero calls. During a run: the
running total reaching the cap stops the run loud. A call whose returned
cost exceeds 10× its projection stops the run loud (the pricing
assumption is wrong)."

TOTAL DEMAND, NOT PER-RUN. `check()` adds the projection to everything
already spent across EVERY earlier run, so two runs that each fit under
the cap cannot together exceed it (L53: a budget check that measures one
consumer is not a budget check). The call ceiling is counted the same way.

ONLY `record()` CREATES THE FILE. A read, a check or a `--dry-run` leaves
no file behind, so "the ledger exists" means "a metered call was made" —
the offline build's CLOSE step relies on exactly that.

A line holds a call id, a cost, its source (`returned` by the response,
`computed` from tokens × the listed price, or `projected` — a call that
came back with no cost: its own projection, booked so the cap and the
ceiling see it; never 0) and a UTC time. Every POST that came back is
exactly one line. Never a request, a response or a header.
"""

from __future__ import annotations

import json
import math
import threading
from datetime import datetime, timezone
from pathlib import Path

LEDGER_NAME = "classify-spend.jsonl"

#: Plan §5: a returned cost above this multiple of its projection means
#: the pricing assumption is wrong, and the run stops.
OVERRUN_FACTOR = 10


class Ledger:
    def __init__(self, path: Path, *, cap_usd: float, call_ceiling: int):
        self.path = Path(path)
        self.cap_usd = float(cap_usd)
        self.call_ceiling = int(call_ceiling)
        # parallel mode: a read never sees a half-written line
        self._lock = threading.Lock()

    # -- reads (never create the file) ------------------------------------

    def entries(self) -> list[dict]:
        with self._lock:
            if not self.path.exists():
                return []
            return [json.loads(line) for line in self.path.read_text().splitlines() if line.strip()]

    def spent(self) -> float:
        return float(sum(e["cost_usd"] for e in self.entries()))

    def calls(self) -> int:
        return len(self.entries())

    # -- gates --------------------------------------------------------------

    def check(self, projected_usd: float, *, calls: int) -> None:
        """Refuse BEFORE any call when the total demand crosses the cap or
        the call ceiling."""
        from .collector import ClassifyError

        spent, made = self.spent(), self.calls()
        if spent + projected_usd > self.cap_usd:
            raise ClassifyError(
                f"spend cap: ledger ${spent:.6f} + projected ${projected_usd:.6f} "
                f"> cap ${self.cap_usd:.2f} — refused, zero calls (TOTAL demand, L53)"
            )
        if made + calls > self.call_ceiling:
            raise ClassifyError(
                f"call ceiling: ledger {made} + planned {calls} > ceiling "
                f"{self.call_ceiling} — refused, zero calls"
            )

    def stop_if(self, total: float | None = None) -> None:
        """The running check: the total reaching the cap stops the run."""
        from .collector import ClassifyError

        total = self.spent() if total is None else total
        if total >= self.cap_usd:
            raise ClassifyError(
                f"spend cap reached: ledger ${total:.6f} >= cap ${self.cap_usd:.2f} — run stopped"
            )

    def check_cost(self, *, returned: float, projected: float) -> None:
        from .collector import ClassifyError

        if returned > OVERRUN_FACTOR * projected:
            raise ClassifyError(
                f"returned cost ${returned:.8f} > {OVERRUN_FACTOR}x its projection "
                f"${projected:.8f} — the pricing assumption is wrong; run stopped"
            )

    # -- the one write --------------------------------------------------------

    def record(self, call_id: str, cost_usd: float, cost_source: str) -> None:
        """One line per metered call. `cost_source`: `returned`, `computed`
        or `projected` (a call that came back with no cost: its own
        projection, booked so the cap and the ceiling see it; never 0).
        A negative or non-finite cost is refused before the file is opened:
        it would lower (or poison) the total."""
        from .collector import ClassifyError

        cost = float(cost_usd)
        if not math.isfinite(cost) or cost < 0:
            raise ClassifyError(
                f"ledger cost {cost!r} is negative or not finite — refused, not recorded"
            )
        self.path.parent.mkdir(parents=True, exist_ok=True)
        line = {
            "call_id": call_id,
            "cost_usd": cost,
            "cost_source": cost_source,
            "at": datetime.now(timezone.utc).isoformat(),
        }
        with self._lock, self.path.open("a") as fh:
            fh.write(json.dumps(line) + "\n")


__all__ = ["LEDGER_NAME", "Ledger", "OVERRUN_FACTOR"]
