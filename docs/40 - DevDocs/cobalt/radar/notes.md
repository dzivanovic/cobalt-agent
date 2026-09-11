# `src/cobalt/radar/notes.py`

Reads each source note once as bytes, hashes the note and every YAML fence, dispatches strict block kinds, checks pool overrides and request budget, and mirrors status through `TraderSettingsStore.put`. An invalid pool freezes membership decisions.

