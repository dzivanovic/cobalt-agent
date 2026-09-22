"""ANCHORS — what a formation hangs on (FINAL §2.4: `extension_direction`
becomes `anchor {object, direction, bar_ts}`; setups one build STEP-4).

A definition's anchor is chosen by the OBJECT its preconditions name, never
by a trade's name: the first row whose object a precondition atom names
wins. Each row resolves, on a FRAME, the anchor's direction (frame
coordinates) and its bar — the formation's bar — or the note that says why
there is nothing to form on.

* `Extension` — today's anchor, byte-identical: the culminating bar of an
  Extension with a direction (A-01 is applied by the stage, in frame terms).
* `Range(micro)` — the bar at which the live micro-Range instantiated; the
  direction is the long-side text's trade side (`up` in frame coordinates).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict

from cobalt.taxonomy.trade_def import TradeDef


class FrameAnchor(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    object: str
    #: In the frame's coordinates.
    direction: Literal["up", "down"]
    bar_ts: AwareDatetime


@dataclass(frozen=True)
class AnchorResolver:
    object: str
    #: The atom prefix a precondition names to hang on this object.
    prefix: str
    resolve: Callable[[Any], FrameAnchor | str]


def _extension(frame) -> FrameAnchor | str:
    ext = frame.extension
    if ext.direction is None or ext.culminating_bar_ts is None:
        return "no culminating bar to form on"
    return FrameAnchor(object="Extension", direction=ext.direction, bar_ts=ext.culminating_bar_ts)


def _micro_range(frame) -> FrameAnchor | str:
    obs = frame.objects["Range(micro)"]
    r = None if isinstance(obs, str) else obs.range
    if r is None:
        return "no instantiated micro-Range to form on"
    return FrameAnchor(object="Range(micro)", direction="up", bar_ts=r.instantiated_ts)


ANCHORS: tuple[AnchorResolver, ...] = (
    AnchorResolver("Extension", "Extension.", _extension),
    AnchorResolver("Range(micro)", "Range(micro).", _micro_range),
)


def anchor_for(td: TradeDef) -> AnchorResolver | None:
    """The anchor row a definition hangs on, or None."""
    named = [atom for p in td.preconditions for atom in p.required_atoms]
    for row in ANCHORS:
        if any(atom.startswith(row.prefix) for atom in named):
            return row
    return None


__all__ = ["ANCHORS", "AnchorResolver", "FrameAnchor", "anchor_for"]
