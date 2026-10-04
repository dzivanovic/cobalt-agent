"""lock-relief P2, in its form after card 2026-10-03/03 (adoption-scripts L2) and card 03c M3.

The build gate's pass 1 runs the with-DB tests only: `ops/desk/gate-lists.md` `## PASS 1`,
the one command `ops/desk/gate.sh` runs, holds ` --db-only` once, directly after
`tests/cobalt tests/taxonomy`. The deploy gate runs pass 1 whole (his 2026-10-02 R154):
`DEPLOY-HUB.md` STEP-G calls `gate.sh … all --deploy`, which strips that one token
(tests/ops/test_gate.py pins the strip).
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PROMPTS = REPO / "docs" / "40 - DevDocs" / "prompts"
LISTS = REPO / "ops" / "desk" / "gate-lists.md"
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


def test_the_gate_lists_pass1_holds_db_only_once_after_the_two_suites():
    (command,) = [ln.strip() for ln in section(LISTS, "PASS 1") if ln.strip()]
    assert command.startswith("`COBALT_ENV=dev uv run pytest ") and command.endswith("`")
    assert command.split(" ").count("--db-only") == 1
    assert command.count(OPTION) == 1
    assert " tests/cobalt tests/taxonomy --db-only " in command


def test_the_deploy_hub_step_g_calls_the_gate_with_deploy():
    calls = [ln for ln in section(PROMPTS / "DEPLOY-HUB.md", "STEP-G") if "ops/desk/gate.sh " in ln]
    assert calls
    assert all(" all --deploy" in ln for ln in calls)
