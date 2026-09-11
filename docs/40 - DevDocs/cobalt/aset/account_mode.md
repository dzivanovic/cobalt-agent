# `src/cobalt/aset/account_mode.py`

Resolves a card's required `live` or `sim` stamp from the day's override, then the standing trader setting. Missing or invalid values raise `AccountModeUnresolved`; no default is invented.

