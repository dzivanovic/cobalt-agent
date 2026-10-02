"""ops/desk/house-probe.sh — one word from each outside house (card 19 worker-steps S5).

No house is called: `codex`, `grok` and `agy` are stubs on PATH that record their working
directory and arguments, one JSON line per call, and answer canned text. A tmp directory
stands in for /Users/cobalt/cobalt-wt (COBALT_WT_ROOT) and holds agy-trial/.
"""

from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
PROBE = REPO / "ops" / "desk" / "house-probe.sh"
CHECK_HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "CHECK-HUB.md"
LIMIT_TEXT = "You have hit your usage limit. It resets at a later hour."

RECORD = '''#!/usr/bin/env python3
import json, os, sys
with open(os.path.join(os.environ["PROBE_CALLS"], "{name}.jsonl"), "a") as f:
    f.write(json.dumps({{"cwd": os.getcwd(), "argv": sys.argv[1:]}}) + "\\n")
'''


def stub(bin_dir: Path, name: str, body: str) -> None:
    (bin_dir / name).write_text(RECORD.format(name=name) + body)
    (bin_dir / name).chmod(0o755)


@pytest.fixture
def houses(tmp_path):
    wt = tmp_path / "wt"
    (wt / "agy-trial").mkdir(parents=True)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    calls = tmp_path / "calls"
    calls.mkdir()
    stub(bin_dir, "codex", "print('OK')\n")
    stub(bin_dir, "grok", f"print({LIMIT_TEXT!r})\nprint('second line')\nsys.exit(1)\n")
    stub(bin_dir, "agy", "import time\ntime.sleep(30)\nprint('OK')\n")
    env = dict(
        os.environ, COBALT_WT_ROOT=str(wt), PROBE_CALLS=str(calls), HOUSE_PROBE_LIMIT="2",
        PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
    )
    return wt, calls, env


def probe(env: dict, *houses: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(PROBE), *houses], env=env, capture_output=True, text=True, timeout=120
    )


def calls_of(calls: Path, name: str) -> list[dict]:
    path = calls / f"{name}.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines()]


def test_all_three_by_default_up_out_and_timeout(houses):
    wt, calls, env = houses
    started = time.monotonic()
    done = probe(env)
    assert done.returncode == 0, done.stdout + done.stderr
    assert time.monotonic() - started < 25
    assert done.stdout.splitlines() == [
        "sol: UP",
        f"grok: OUT — {LIMIT_TEXT}",
        "gemini: OUT — TIMEOUT",
    ]


def test_naming_grok_alone_calls_only_grok_from_agy_trial(houses):
    wt, calls, env = houses
    done = probe(env, "grok")
    assert done.returncode == 0
    assert done.stdout.splitlines() == [f"grok: OUT — {LIMIT_TEXT}"]
    assert calls_of(calls, "codex") == [] and calls_of(calls, "agy") == []
    (call,) = calls_of(calls, "grok")
    assert Path(call["cwd"]).resolve() == (wt / "agy-trial").resolve()
    assert call["argv"] == [
        "--sandbox", "cobalt-job",
        "--allow", f"Write({wt}/agy-trial/scratch/tribunal-bars-0920/**)",
        "-p", "Reply with only the word OK.",
    ]


def test_the_sol_stub_sees_the_hub_files_probe_exactly(houses):
    wt, calls, env = houses
    done = probe(env, "sol")
    assert done.stdout.splitlines() == ["sol: UP"]
    line = next(ln for ln in CHECK_HUB.read_text().splitlines() if "THE SOL PROBE" in ln)
    spelled = next(s for s in re.findall(r"`([^`]*)`", line) if s.startswith("codex exec"))
    assert spelled.endswith(" < /dev/null")
    words = shlex.split(spelled[: -len(" < /dev/null")])
    assert words[0] == "codex"
    (call,) = calls_of(calls, "codex")
    assert call["argv"] == words[1:]


def test_gemini_is_spelled_as_the_hub_launch_with_a_three_minute_print_timeout(houses):
    wt, calls, env = houses
    done = probe(env, "gemini")
    assert done.stdout.splitlines() == ["gemini: OUT — TIMEOUT"]
    (call,) = calls_of(calls, "agy")
    assert Path(call["cwd"]).resolve() == (wt / "agy-trial").resolve()
    assert call["argv"] == [
        "--model", "gemini-3.1-pro-high", "--mode", "accept-edits", "--sandbox",
        "--print-timeout", "3m", "--add-dir", f"{wt}/agy-trial",
        "--print=Reply with only the word OK.",
    ]


def test_a_gemini_answer_with_the_harness_trailer_is_up(houses, tmp_path):
    wt, calls, env = houses
    stub(tmp_path / "bin", "agy", "print('OK')\nprint('[exited with code 0]')\n")
    done = probe(env, "gemini")
    assert done.stdout.splitlines() == ["gemini: UP"]


def test_a_house_that_says_nothing_is_out(houses, tmp_path):
    wt, calls, env = houses
    stub(tmp_path / "bin", "codex", "sys.exit(2)\n")
    done = probe(env, "sol")
    assert done.returncode == 0
    assert done.stdout.splitlines() == ["sol: OUT — (no output)"]


@pytest.mark.parametrize("args", [["claude"], ["sol", "sol"], ["SOL"]])
def test_a_bad_call_is_refused(houses, args):
    wt, calls, env = houses
    done = probe(env, *args)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert list(calls.iterdir()) == []
