"""Tiny LAN-IP helper for startup URL printing. No new dependency.

Uses a UDP "connect" (no packet is actually sent — UDP connect just asks
the OS to pick a route) to find which local interface would be used to
reach an external address; that interface's address is the one other
devices on the LAN would use to reach this machine.
"""

import socket


def local_lan_ip() -> str | None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return None
    finally:
        s.close()
