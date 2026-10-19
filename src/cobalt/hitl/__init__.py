"""F20 HITL: a requested action, his tap on the `/hitl` page, a deterministic executor.

* `actions.py`  — the catalog (`agents.create`, `agents.deactivate`) and `request_action`
* `card.py`     — the card DM (through `notify.mattermost.send_dm`, so F19 redacts it)
* `store.py`    — `cobalt_hitl_requests` (USER side)
* `executor.py` — runs approved rows inside the CoS resident, never in the aset process

The approve path is the two routes in `cobalt.aset.web` and nothing else (L37).
"""
