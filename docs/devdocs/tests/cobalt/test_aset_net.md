# `tests/cobalt/test_aset_net.py`

## What it does
Tests `net.local_lan_ip()` with a fake socket — no real network access,
runs identically offline or on a plane.

## Key functions/classes (what's covered, not defined)
- `_FakeSocket` — a minimal stand-in implementing `connect`,
  `getsockname`, `close`; can be configured to return a canned address
  or raise `OSError` on connect.
- `test_local_lan_ip_returns_detected_address` — monkeypatches
  `socket.socket` to the fake, asserts the detected address round-trips.
- `test_local_lan_ip_returns_none_on_failure` — fake raises `OSError` on
  connect, asserts `local_lan_ip()` returns `None` rather than
  propagating the exception (matches the module's documented degrade-
  gracefully behavior).

## Data flow in/out
None — `socket.socket` is monkeypatched, no real sockets are opened.

## Config it reads
None.
