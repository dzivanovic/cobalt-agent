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
# the card header line that alone lets Sol be probed (his 2026-10-10 R920, card 298 S3)
OPENAI_LINE = "HOUSE A: OpenAI — his 2026-01-02 R2"

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


def card_file(tmp_path: Path, header: str = "", rows: str = "", name: str = "card.md") -> Path:
    """A constructed card: header lines, then `## ROWS` and what sits under it."""
    path = tmp_path / name
    path.write_text(
        "JOB: x-job\nBRANCH: ops/x-job\nRULINGS: 2026-01-02 R2\n"
        f"{header}\n## ROWS\n| row | what |\n{rows}"
    )
    return path


def hub_sol_probe_words() -> list[str]:
    """The `codex exec …` spelling of the hub's THE SOL PROBE line, as argv."""
    line = next(ln for ln in CHECK_HUB.read_text().splitlines() if "THE SOL PROBE" in ln)
    spelled = next(s for s in re.findall(r"`([^`]*)`", line) if s.startswith("codex exec"))
    assert spelled.endswith(" < /dev/null")
    return shlex.split(spelled[: -len(" < /dev/null")])


def test_no_card_probes_grok_and_gemini_and_never_calls_codex(houses):
    wt, calls, env = houses
    started = time.monotonic()
    done = probe(env)
    assert done.returncode == 0, done.stdout + done.stderr
    assert time.monotonic() - started < 25
    assert calls_of(calls, "codex") == []
    assert done.stdout.splitlines() == [
        f"grok: OUT — {LIMIT_TEXT}",
        "gemini: OUT — TIMEOUT",
    ]


@pytest.mark.parametrize(
    ("header", "rows"),
    [
        ("", ""),
        ("HOUSE A: none — overruled 2026-10-10 R1", ""),
        ("HOUSE A: OpenAI", ""),
        ("  " + OPENAI_LINE, ""),
        ("HOUSE A: OpenAI — overruled 2026-01-02 R2", ""),
        (OPENAI_LINE + " and more", ""),
        ("", OPENAI_LINE + "\n"),
    ],
    ids=["plain", "none-overruled", "openai-alone", "indented", "overruled", "tail", "under-rows"],
)
def test_a_card_without_the_openai_line_makes_no_codex_call(houses, tmp_path, header, rows):
    wt, calls, env = houses
    card = card_file(tmp_path, header, rows)
    done = probe(env, "--card", str(card))
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines() == [
        f"grok: OUT — {LIMIT_TEXT}",
        "gemini: OUT — TIMEOUT",
    ]
    assert calls_of(calls, "codex") == []


def test_a_card_with_the_line_probes_sol_first_with_the_hub_spelling(houses, tmp_path):
    wt, calls, env = houses
    card = card_file(tmp_path, OPENAI_LINE)
    done = probe(env, "--card", str(card))
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines() == [
        "sol: UP",
        f"grok: OUT — {LIMIT_TEXT}",
        "gemini: OUT — TIMEOUT",
    ]
    words = hub_sol_probe_words()
    assert words[0] == "codex"
    (call,) = calls_of(calls, "codex")
    assert call["argv"] == words[1:]


@pytest.mark.parametrize("with_card", [False, True], ids=["sol-alone", "plain-card-sol"])
def test_naming_sol_without_the_line_is_refused(houses, tmp_path, with_card):
    wt, calls, env = houses
    args = ["--card", str(card_file(tmp_path)), "sol"] if with_card else ["sol"]
    done = probe(env, *args)
    assert done.returncode == 1
    assert done.stderr.startswith(
        "REFUSED: house 'sol' is probed only when the card header carries"
    ), done.stderr
    assert list(calls.iterdir()) == []


def test_naming_sol_with_the_line_probes_only_sol(houses, tmp_path):
    wt, calls, env = houses
    card = card_file(tmp_path, OPENAI_LINE)
    done = probe(env, "--card", str(card), "sol")
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines() == ["sol: UP"]
    assert len(calls_of(calls, "codex")) == 1
    assert calls_of(calls, "grok") == [] and calls_of(calls, "agy") == []


@pytest.mark.parametrize("shape", ["no-path", "missing", "twice"])
def test_a_bad_card_call_is_refused(houses, tmp_path, shape):
    wt, calls, env = houses
    args = {
        "no-path": ["--card"],
        "missing": ["--card", str(tmp_path / "no-such-card.md")],
        "twice": [
            "--card", str(card_file(tmp_path, name="a.md")),
            "--card", str(card_file(tmp_path, name="b.md")),
        ],
    }[shape]
    done = probe(env, *args)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: --card "), done.stderr
    assert "is none of" not in done.stderr
    assert list(calls.iterdir()) == []


def test_check_hub_seat_order_is_grok_gemini_and_openai_only_by_header():
    """His 2026-10-10 R920, R921 (card 298 S1): the hub's SEAT ORDER is Grok, Gemini; OpenAI
    sits only with the card header line, and the old OpenAI-first lines are gone."""
    lines = CHECK_HUB.read_text().splitlines()
    head = (
        'SEAT ORDER: Grok (xAI, grok-4.7) · Gemini (Google). OpenAI (Sol) sits only when the card '
        'header carries "HOUSE A: OpenAI — his <date> R<n>"'
    )
    assert len([ln for ln in lines if ln.startswith(head)]) == 1
    assert not any("OpenAI up → A = OpenAI" in ln for ln in lines)
    assert not any("OpenAI (Sol, `gpt-5.6-sol`) · Grok" in ln for ln in lines)
    assert len(lines) == 127  # card 386 L2, L6 (two), L8: four shadow lines


def test_check_hub_probe_step_calls_the_script_with_the_card():
    """His 2026-10-10 R920 (card 298 S2): PREFLIGHT's probe step passes the card, Sol only with
    the header line proved by AUTHORIZATION, and the SOL launch label says so."""
    lines = CHECK_HUB.read_text().splitlines()
    (probe_line,) = [ln for ln in lines if "THE SOL PROBE" in ln]
    assert 'house-probe.sh --card "<card>"' in probe_line
    assert "(all three" not in probe_line
    assert "log -1 --format=%H -S" not in probe_line
    (sol_label,) = [ln for ln in lines if ln.startswith("- **SOL")]
    assert "HOUSE A: OpenAI — his <date> R<n>" in sol_label


def test_naming_grok_alone_calls_only_grok_from_agy_trial(houses):
    wt, calls, env = houses
    done = probe(env, "grok")
    assert done.returncode == 0
    assert done.stdout.splitlines() == [f"grok: OUT — {LIMIT_TEXT}"]
    assert calls_of(calls, "codex") == [] and calls_of(calls, "agy") == []
    (call,) = calls_of(calls, "grok")
    assert Path(call["cwd"]).resolve() == (wt / "agy-trial").resolve()
    assert call["argv"] == [
        "-m", "grok-4.7",
        "--sandbox", "cobalt-job",
        "--allow", f"Write({wt}/agy-trial/scratch/tribunal-bars-0920/**)",
        "-p", "Reply with only the word OK.",
    ]


def test_card03_l7_both_grok_spellings_pin_the_model_first():
    """His 2026-10-03 R3: every Grok seat runs grok-4.7 — `-m grok-4.7` directly after the
    command word, in the probe and in the usage line of the header."""
    lines = PROBE.read_text().splitlines()
    spelled = [ln for ln in lines if re.search(r"^#\s+grok -|\bexec grok -", ln)]
    assert len(spelled) == 2, spelled
    for line in spelled:
        words = line.split("grok", 1)[1].split()
        assert words[:2] == ["-m", "grok-4.7"], line
    assert any("R3" in ln and "grok-4.7" in ln for ln in lines if ln.startswith("#")), "the header names no row"


def test_the_sol_stub_sees_the_hub_files_probe_exactly(houses, tmp_path):
    wt, calls, env = houses
    done = probe(env, "--card", str(card_file(tmp_path, OPENAI_LINE)), "sol")
    assert done.stdout.splitlines() == ["sol: UP"]
    words = hub_sol_probe_words()
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
    done = probe(env, "--card", str(card_file(tmp_path, OPENAI_LINE)), "sol")
    assert done.returncode == 0
    assert done.stdout.splitlines() == ["sol: OUT — (no output)"]


@pytest.mark.parametrize("args", [["claude"], ["sol", "sol"], ["SOL"]])
def test_a_bad_call_is_refused(houses, args):
    wt, calls, env = houses
    done = probe(env, *args)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert list(calls.iterdir()) == []
