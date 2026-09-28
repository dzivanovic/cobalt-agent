"""`InPlay.state` — the name's radar pool admission (FINAL §3 D1; setups
one build STEP-3).

Only pool members are evaluated, so a member is `active` while its
membership is open and `departed` once it left the pool (the stage's
`MemberInput.departed`). Pure; reads no tunable.
"""

from __future__ import annotations

from typing import Literal

TUNABLE_KEYS: tuple[str, ...] = ()
DOMAIN = frozenset({"active", "departed"})


def in_play_state(*, departed: bool) -> Literal["active", "departed"]:
    return "departed" if departed else "active"


__all__ = ["DOMAIN", "TUNABLE_KEYS", "in_play_state"]
