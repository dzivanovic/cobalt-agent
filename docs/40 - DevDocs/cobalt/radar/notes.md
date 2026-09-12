# `src/cobalt/radar/notes.py`

Reads each source note once as bytes, hashes the note and every YAML fence, dispatches strict block kinds, checks pool overrides and the ruled request budget, and mirrors status through `TraderSettingsStore.put`. `parse_note_bytes` gives prospective validation the identical parser without temporary files. An invalid pool freezes membership decisions.

The budget check (`planned_total_rpm`) computes total Finviz transport demand — pool bar-polling + one request per screen + one request per list ticker-chunk — because all three consumers share the single resident scan cadence (`RadarRunner` runs collection and the bar poller in the same cycle). A pool-only check gives false assurance, the same shape as the pre-fix `radar sources` validating only Lists.
