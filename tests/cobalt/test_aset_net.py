"""LAN-IP helper tests — no real network access, socket is faked."""

import socket

from cobalt.aset.net import local_lan_ip


class _FakeSocket:
    def __init__(self, sockname=None, raise_on_connect=False):
        self._sockname = sockname
        self._raise = raise_on_connect

    def connect(self, addr):
        if self._raise:
            raise OSError("network unreachable")

    def getsockname(self):
        return (self._sockname, 0)

    def close(self):
        pass


def test_local_lan_ip_returns_detected_address(monkeypatch):
    monkeypatch.setattr(
        socket, "socket", lambda *a, **k: _FakeSocket(sockname="192.168.1.42")
    )
    assert local_lan_ip() == "192.168.1.42"


def test_local_lan_ip_returns_none_on_failure(monkeypatch):
    monkeypatch.setattr(
        socket, "socket", lambda *a, **k: _FakeSocket(raise_on_connect=True)
    )
    assert local_lan_ip() is None
