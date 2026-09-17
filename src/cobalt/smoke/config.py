"""Loads a smoke suite file — L10: "bad file crashes with a line number".

YAML is parsed twice from the same text: `yaml.compose` keeps the node
tree with its start marks, `yaml.safe_load` feeds the Pydantic schema.
A validation error's location (`checks → 3 → expect → 0 → op`) is walked
down the node tree to the deepest node that exists, and that node's line
is the one reported. A key the file never wrote (a missing required
field) resolves to the line of the mapping that should have carried it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from pydantic import ValidationError

from .models import SmokeSuite

REPO_ROOT = Path(__file__).resolve().parents[3]
SUITES_DIR = REPO_ROOT / "configs" / "cobalt" / "smoke"


class SmokeConfigError(RuntimeError):
    """A suite file that cannot load. `line` is 1-based, or None."""

    def __init__(self, path: Path, line: Optional[int], message: str):
        self.path = path
        self.line = line
        where = f"{path}:{line}" if line is not None else str(path)
        super().__init__(f"{where}: {message}")


def suite_path(name: str) -> Path:
    return SUITES_DIR / f"{name}.yaml"


def _line_for(root: yaml.Node, loc: tuple) -> int:
    node = root
    for part in loc:
        if isinstance(node, yaml.MappingNode):
            match = next((v for k, v in node.value if getattr(k, "value", None) == part), None)
            if match is None:
                continue  # a union tag, or a key the file never wrote
            node = match
        elif isinstance(node, yaml.SequenceNode) and isinstance(part, int):
            if part >= len(node.value):
                break
            node = node.value[part]
        else:
            break
    return node.start_mark.line + 1


def load_suite(path: Path) -> SmokeSuite:
    path = Path(path)
    try:
        text = path.read_text()
    except OSError as e:
        raise SmokeConfigError(path, None, f"unreadable: {e}") from e
    try:
        root = yaml.compose(text)
        raw = yaml.safe_load(text)
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None) or getattr(e, "context_mark", None)
        line = mark.line + 1 if mark is not None else None
        raise SmokeConfigError(path, line, f"YAML error: {getattr(e, 'problem', None) or e}") from e
    if root is None or not isinstance(raw, dict):
        raise SmokeConfigError(path, 1, "a suite file is a mapping with `suite`, `title`, `checks`")
    try:
        return SmokeSuite.model_validate(raw)
    except ValidationError as e:
        first = e.errors()[0]
        loc = tuple(first["loc"])
        line = _line_for(root, loc)
        where = " → ".join(str(p) for p in loc)
        more = f" (+{e.error_count() - 1} more)" if e.error_count() > 1 else ""
        raise SmokeConfigError(path, line, f"{where}: {first['msg']}{more}") from e


__all__ = ["REPO_ROOT", "SUITES_DIR", "SmokeConfigError", "load_suite", "suite_path"]
