"""aset orphan on bootout (card prompts/2026-10-10/222-aset-orphan-card.md, rows A and B).

A KeepAlive resident whose plist sets `AbandonProcessGroup` true leaves every process of its group
but launchd's own pid alive on `launchctl bootout` (launchd.plist(5)). When launchd's pid is `uv`
and the python is its child, the python survives the bootout, keeps the voice scratch `flock` and
`:5010`, and every KeepAlive restart fails (`ScratchLocked`).

Row A: `ops/start_aset.sh` syncs the environment, then execs the venv python itself, so launchd's
pid IS the python. Row B: no KeepAlive plist under `ops/` pairs `AbandonProcessGroup` true with a
launchd pid that is not the final process. Plists and scripts are read from this repo (`REPO`); the
negative control builds its plists and scripts under `tmp_path`. Nothing is run or loaded.
"""

from __future__ import annotations

import plistlib
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
OPS = REPO / "ops"
LIVE_OPS = "/Users/cobalt/cobalt/ops/"
ASET_SCRIPT = OPS / "start_aset.sh"
SYNC_LINE = "uv sync --inexact"
EXEC_LINE = 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset'


def code_lines(script: Path) -> list[str]:
    """The script's non-blank, non-comment lines, stripped."""
    lines = (line.strip() for line in script.read_text().splitlines())
    return [line for line in lines if line and not line.startswith("#")]


def orphan_prone(plist: Path, ops_dir: Path) -> str | None:
    """A reason when the plist is a KeepAlive job with `AbandonProcessGroup` true whose launchd pid
    is not the final process; else None. A program under /Users/cobalt/cobalt/ops/ is read from
    `ops_dir`, so the tree under test is the one checked."""
    with plist.open("rb") as handle:
        spec = plistlib.load(handle)
    if not spec.get("KeepAlive"):
        return None
    if spec.get("AbandonProcessGroup") is not True:
        return None
    program = spec["ProgramArguments"][0]
    if Path(program).name == "uv":
        return f"{program}: launchd's pid is uv; its child is abandoned on bootout"
    path = ops_dir / program[len(LIVE_OPS):] if program.startswith(LIVE_OPS) else Path(program)
    if path.suffix != ".sh":
        return None
    lines = code_lines(path)
    last = lines[-1] if lines else ""
    words = last.split()
    if len(words) < 2 or words[0] != "exec":
        return f"{path.name} ends {last!r}: not an exec, launchd's pid is the shell"
    if Path(words[1].strip('"')).name == "uv":
        return f"{path.name} ends {last!r}: exec uv run, launchd's pid is uv"
    return None


def keepalive_plists() -> list[Path]:
    """Every ops/com.cobalt.*.plist whose KeepAlive key is set: radar first, the rest sorted."""
    found = []
    for plist in sorted(OPS.glob("com.cobalt.*.plist")):
        with plist.open("rb") as handle:
            if "KeepAlive" in plistlib.load(handle):
                found.append(plist)
    radar = [p for p in found if p.stem == "com.cobalt.radar"]
    return radar + [p for p in found if p.stem != "com.cobalt.radar"]


RESIDENTS = keepalive_plists()


# Row A ----------------------------------------------------------------------------------------


def test_a1_start_aset_syncs_then_execs_the_venv_python():
    lines = code_lines(ASET_SCRIPT)
    assert lines[-2:] == [SYNC_LINE, EXEC_LINE]
    held = [line for line in ASET_SCRIPT.read_text().splitlines() if "uv run" in line]
    assert held == []


# Row B ----------------------------------------------------------------------------------------


@pytest.mark.parametrize("plist", RESIDENTS, ids=[p.stem for p in RESIDENTS])
def test_b1_no_keepalive_plist_abandons_a_child(plist):
    assert orphan_prone(plist, OPS) is None


def test_b2_the_keepalive_set_holds_radar_and_aset():
    labels = [p.stem for p in RESIDENTS]
    assert labels[0] == "com.cobalt.radar"
    assert "com.cobalt.aset" in labels


def _plist(tmp_path: Path, name: str, program: str, keepalive: bool, abandon: bool) -> Path:
    spec: dict = {"Label": f"com.constructed.{name}", "ProgramArguments": [program, "run"]}
    if keepalive:
        spec["KeepAlive"] = True
    if abandon:
        spec["AbandonProcessGroup"] = True
    path = tmp_path / f"com.constructed.{name}.plist"
    with path.open("wb") as handle:
        plistlib.dump(spec, handle)
    return path


def _script(ops_dir: Path, name: str, last_line: str) -> str:
    ops_dir.mkdir(exist_ok=True)
    (ops_dir / name).write_text(f"#!/bin/bash\nset -e\n# constructed\ncd /x\n{last_line}\n\n")
    return LIVE_OPS + name


def test_b3_negative_control_on_constructed_plists(tmp_path):
    ops_dir = tmp_path / "ops"
    uv = "/constructed/bin/uv"
    assert orphan_prone(_plist(tmp_path, "uv", uv, True, True), ops_dir) is not None
    via_uv = _script(ops_dir, "start_uv.sh", "exec uv run python -m x")
    assert "exec uv run" in orphan_prone(_plist(tmp_path, "via-uv", via_uv, True, True), ops_dir)
    via_venv = _script(ops_dir, "start_venv.sh", "exec /venv/bin/python -m x")
    assert orphan_prone(_plist(tmp_path, "via-venv", via_venv, True, True), ops_dir) is None
    assert orphan_prone(_plist(tmp_path, "no-keepalive", uv, False, True), ops_dir) is None
    assert orphan_prone(_plist(tmp_path, "no-abandon", uv, True, False), ops_dir) is None
