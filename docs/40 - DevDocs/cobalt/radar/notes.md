# `src/cobalt/radar/notes.py`

Reads each source note once as bytes, hashes the note and every YAML fence, dispatches strict block kinds, checks pool overrides and the ruled cap-at-scan-cadence request budget, and mirrors status through `TraderSettingsStore.put`. `parse_note_bytes` gives prospective validation the identical parser without temporary files. An invalid pool freezes membership decisions.
