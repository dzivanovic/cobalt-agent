"""F18 heartbeat host (Charter §3 F18, M10).

Every `heartbeat.interval_min` minutes: probe every service, sweep every
job row, write one red/green block into today's daily note as an L28
unit, and DM on any red (plus one green summary a day).

The Charter's second, out-of-band channel is email via the Layer-B Google
OAuth path. That send path DOES NOT EXIST in this repo — see
`runner.out_of_band()` for what was searched for and what was found —
so every red says so out loud and the second channel is carried to P4.
"""

from .probes import Probe
from .render import Beat
from .runner import run_beat, take_beat

__all__ = ["Beat", "Probe", "run_beat", "take_beat"]
