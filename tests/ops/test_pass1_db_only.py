"""lock-relief P2 — the build gate's pass 1 runs the with-DB tests only.

THIS tree's `BUILD-HUB.md` is read the way `ops/desk/gate.sh` reads it: in
`## W`, the one backticked line right after the `- (c) ` item that begins
`COBALT_ENV=dev uv run pytest`. It holds ` --db-only` once, directly after
`tests/cobalt tests/taxonomy`. `DEPLOY-HUB.md` STEP-G's pass 1 (read the same
way under `## STEP-G`) runs without it, on purpose: the deploy gate keeps
pass 1 whole on the merged tree, and the two commands differ by nothing else.
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PROMPTS = REPO / "docs" / "40 - DevDocs" / "prompts"
OPTION = " --db-only"


def section(path: Path, title: str) -> list[str]:
    body, inside = [], False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            inside = line.startswith("## " + title)
            continue
        if inside:
            body.append(line)
    return body


def pass1(path: Path, title: str) -> str:
    """gate.sh `after("c")`: the next non-blank line after `- (c) `, one backticked span."""
    lines = section(path, title)
    found = []
    for i, line in enumerate(lines):
        if line.startswith("- (c) "):
            for nxt in lines[i + 1:]:
                s = nxt.strip()
                if s:
                    if s.startswith("`COBALT_ENV=dev uv run pytest ") and s.endswith("`") and s.count("`") == 2:
                        found.append(s[1:-1])
                    break
    assert len(found) == 1, f"{path.name} {title}: {len(found)} pass-1 commands"
    return found[0]


def test_the_build_gate_pass1_holds_db_only_once_after_the_two_suites():
    command = pass1(PROMPTS / "BUILD-HUB.md", "W ")
    assert command.count(OPTION) == 1
    assert " tests/cobalt tests/taxonomy --db-only " in command


def test_the_deploy_gate_pass1_runs_without_db_only():
    assert "--db-only" not in pass1(PROMPTS / "DEPLOY-HUB.md", "STEP-G")


def test_the_two_pass1_commands_differ_by_the_option_alone():
    build = pass1(PROMPTS / "BUILD-HUB.md", "W ")
    deploy = pass1(PROMPTS / "DEPLOY-HUB.md", "STEP-G")
    assert build.replace(OPTION, "", 1) == deploy
