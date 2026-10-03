"""tests/ops — no test reaches the real launchd or a house (card 20 deploy-steps, row D5).

An autouse fixture puts a bin of stand-ins FIRST on PATH for every test here: `launchctl`, `codex`,
`grok`, `agy` and `curl` each print `REAL <name> REACHED BY A TEST` on stderr and exit 127. A test
that needs a stub of its own prepends its bin ahead of PATH, as before, and its stub wins.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

GUARDED = ("launchctl", "codex", "grok", "agy", "curl")


@pytest.fixture(scope="session")
def guard_bin(tmp_path_factory) -> Path:
    bin_ = tmp_path_factory.mktemp("ops-guard-bin")
    for name in GUARDED:
        p = bin_ / name
        p.write_text(f'#!/bin/sh\necho "REAL {name} REACHED BY A TEST" >&2\nexit 127\n')
        p.chmod(0o755)
    return bin_


@pytest.fixture(autouse=True)
def no_real_launchd_or_house(guard_bin, monkeypatch) -> Path:
    monkeypatch.setenv("PATH", f"{guard_bin}{os.pathsep}{os.environ.get('PATH', '')}")
    return guard_bin
