"""tests/ops/conftest.py — no test reaches the real launchd or a house (card 20 deploy-steps, row D5).

Each guarded name is resolved on PATH BEFORE anything is run: when it resolves to anything but the
guard's stand-in, the test fails there and calls nothing, so this file never reaches the real
`/bin/launchctl`, a house's CLI or the network, not even when the guard is missing.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

GUARDED = ("launchctl", "codex", "grok", "agy", "curl")
SENTENCE = "REAL {} REACHED BY A TEST"


def stand_in(name: str) -> str:
    found = shutil.which(name, path=os.environ.get("PATH", ""))
    head = Path(found).read_bytes()[:400] if found else b""
    assert SENTENCE.format(name).encode() in head, f"{name} resolves to {found}: the real one answers"
    return found


@pytest.mark.parametrize("name", GUARDED)
def test_each_guarded_name_resolves_to_the_stand_in(name):
    stand_in(name)


@pytest.mark.parametrize("name", GUARDED)
def test_a_script_with_no_stub_reaches_the_stand_in_exit_127_and_the_sentence(name, tmp_path):
    stand_in(name)
    script = tmp_path / "calls.sh"
    script.write_text(f"#!/bin/sh\n{name} print gui/501/com.cobalt.aset\n")
    done = subprocess.run(["sh", str(script)], capture_output=True, text=True, timeout=30)
    assert done.returncode == 127, done.stdout + done.stderr
    assert done.stderr.strip() == SENTENCE.format(name)
    assert done.stdout == ""


def test_a_stub_a_test_places_ahead_still_wins(tmp_path):
    stand_in("launchctl")
    own = tmp_path / "bin"
    own.mkdir()
    stub = own / "launchctl"
    stub.write_text("#!/bin/sh\necho \"stub $*\"\n")
    stub.chmod(0o755)
    env = dict(os.environ, PATH=f"{own}{os.pathsep}{os.environ['PATH']}")
    done = subprocess.run(
        ["sh", "-c", "launchctl print gui/501/com.cobalt.aset"], env=env, capture_output=True,
        text=True, timeout=30,
    )
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout == "stub print gui/501/com.cobalt.aset\n"
    assert "REACHED BY A TEST" not in done.stderr
