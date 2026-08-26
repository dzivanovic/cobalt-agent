# `src/cobalt/aset/net.py`

## What it does
A tiny helper that finds this machine's LAN-reachable IP address, for
printing the reachable URL(s) on startup when `server.bind: lan` is
active. No new dependency — uses a standard UDP-connect idiom.

## Key functions/classes
- `local_lan_ip() -> str | None` — opens a UDP socket, "connects" it to
  `8.8.8.8:80` (this never actually sends a packet — UDP connect just
  asks the OS to pick a route/interface for that destination), then
  reads back the local address the OS chose via `getsockname()`. That
  address is the one other devices on the LAN would use to reach this
  machine. Returns `None` on any `OSError` (e.g. no network) rather than
  raising — this is a startup-banner nicety, not core functionality, so
  it degrades to "couldn't detect, check manually" instead of crashing
  the server.

## Data flow in/out
**In:** nothing (no arguments).
**Out:** an IPv4 address string, or `None`.

## Config it reads
None.
