"""F20: the chief of staff — one resident session he talks to in a Mattermost DM.

* `listener.py` — the deterministic DM reader (L2): kill phrase first, then one turn row per post
* `session.py`  — the Agent SDK wrapper; the SDK is imported only inside its functions
* `tools.py`    — the in-process tool server: read tools and request tools, no approve verb (L37)
* `store.py`    — `cobalt_cos_sessions`, `cobalt_cos_turns` (USER side)
* `run.py`      — the resident loop of `com.cobalt.cos` (registered `enabled: false`)

Nothing here imports the SDK at module top: `import cobalt.cli` (the radar's
import root) must not load it.
"""
