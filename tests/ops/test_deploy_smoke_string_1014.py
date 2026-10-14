"""The read-only smoke string on the deploy line (card 2026-10-14/537, rows S1 and S2; class K5,
his 2026-10-12 R1138; brain R1466).

Read on the real files, as tests/ops/test_hub_lines.py reads them; BASE by `git show`, the shape
of tests/ops/test_build_hub_no_clutter.py. Against BASE only the deploy launch line and the
per-section production-string counts of STANDING-LIST.md are compared: cards 521 and 523 edit
other lines of these files and deploy in either order with this one.
"""

from __future__ import annotations

import shlex
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
BASE = "7aa5d470"
SMOKE = "Bash(COBALT_ENV=production uv run cobalt smoke *)"
HEARTBEAT = "Bash(COBALT_ENV=production uv run cobalt heartbeat show*)"
BACKUP_RUN = "Bash(COBALT_ENV=production uv run cobalt backup run*)"
PROD = "Bash(COBALT_ENV=production"


def hub_line(name: str) -> str:
    lines = [ln for ln in (HUBS / name).read_text(encoding="utf-8").splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1, f"{name}: {len(lines)} launch lines"
    return lines[0]


def tools(line: str, option: str) -> list[str]:
    """The strings after `--allowedTools` or `--disallowedTools`, up to the next option."""
    words = shlex.split(line)
    out, inside = [], False
    for w in words:
        if w.startswith("--"):
            inside = w == option
            continue
        if inside:
            out.append(w)
    return out


def base_text(name: str) -> str:
    done = subprocess.run(["git", "show", f"{BASE}:docs/40 - DevDocs/prompts/{name}"], cwd=REPO,
                          capture_output=True, text=True, check=True)
    return done.stdout


def base_hub_line(name: str) -> str:
    lines = [ln for ln in base_text(name).splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1, f"{name} at {BASE}: {len(lines)} launch lines"
    return lines[0]


def section(text: str, n: str) -> str:
    """The text of `## <n>. ` up to the next `## ` heading (or the end of the file)."""
    return text.split(f"\n## {n}. ", 1)[1].split("\n## ", 1)[0]


# ---- S1: DEPLOY-HUB.md line 11 ---------------------------------------------------------------


def test_s1_the_deploy_line_allows_cobalt_smoke_once():
    line = hub_line("DEPLOY-HUB.md")
    allow = tools(line, "--allowedTools")
    assert allow.count(SMOKE) == 1, [s for s in allow if "COBALT_ENV=production" in s]
    i = allow.index(SMOKE)
    assert allow[i - 1] == HEARTBEAT and allow[i + 1] == BACKUP_RUN, allow[i - 1:i + 2]
    assert [s for s in tools(line, "--disallowedTools") if "cobalt smoke" in s] == []


def test_s1_no_other_allow_or_deny_string_changes():
    line = hub_line("DEPLOY-HUB.md")
    then = base_hub_line("DEPLOY-HUB.md")
    assert [s for s in tools(line, "--allowedTools") if s != SMOKE] == tools(then, "--allowedTools")
    assert tools(line, "--disallowedTools") == tools(then, "--disallowedTools")
    assert line.replace(f'"{SMOKE}" ', "", 1) == then


# ---- S2: STANDING-LIST.md ## 3. --------------------------------------------------------------


def test_s2_the_standing_list_deploy_section_names_the_smoke_string_once():
    s3 = (HUBS / "STANDING-LIST.md").read_text(encoding="utf-8").split("\n## 3. ", 1)[1].split("\n## 4. ", 1)[0]
    assert s3.count(SMOKE) == 1
    rows = s3.splitlines()
    (i,) = [k for k, ln in enumerate(rows) if SMOKE in ln]
    assert rows[i].startswith(f"| `{SMOKE}` |"), rows[i]
    assert rows[i - 1].startswith(f"| `{HEARTBEAT}` |"), rows[i - 1]
    assert rows[i + 1].startswith(f"| `{BACKUP_RUN}` |"), rows[i + 1]
    cell = rows[i].split("`", 2)[1]
    assert cell in tools(hub_line("DEPLOY-HUB.md"), "--allowedTools")


def test_s2_the_other_sections_production_strings_stand():
    now = (HUBS / "STANDING-LIST.md").read_text(encoding="utf-8")
    then = base_text("STANDING-LIST.md")
    # the string sits nowhere outside ## 3. (test above: once there)
    assert now.count(SMOKE) == section(now, "3").count(SMOKE)
    for n in ("1", "2", "4", "5", "6", "7", "8", "9"):
        assert section(now, n).count(PROD) == section(then, n).count(PROD), n
