# `cobalt.radar.anatomy.in_play` — `InPlay.state`

Added 2026-09-21 in STEP-3 of the setups one build (FINAL §3 D1, "pool admission").

The stage evaluates only pool members. A member is therefore `active` while its membership is open, and `departed` once it has left the pool (`MemberInput.departed`). `DOMAIN = {active, departed}` is the atom's producible domain, so a def that compares `InPlay.state` to any other symbol is `not_evaluable: InPlay.state∌<value>` (E8). The function is pure and reads no tunable (`TUNABLE_KEYS = ()`). The atom is always known, so it declares no unavailability reason (X11).
