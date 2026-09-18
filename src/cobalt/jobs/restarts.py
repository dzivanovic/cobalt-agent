"""Derive resident restarts from a git diff, runtime reads, and static imports."""

from __future__ import annotations

import ast
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .config import REPO_ROOT, JobRegistry, load_job_registry
from .models import JobKind


#: Root markdown files that are documentation only (CLAUDE.md, D6).
ROOT_DOCS = frozenset({"README.md", "CLAUDE.md", "AGENTS.md", "QWEN.md"})
#: Agent-CLI harness files kept under ops/: read by a vendor CLI, never by a
#: Cobalt process (the Grok sandbox profile, 2026-09-17).
HARNESS_FILES = frozenset({"ops/grok-sandbox.toml"})
#: Git's own bookkeeping — files the VERSION CONTROL SYSTEM reads and no
#: Cobalt process ever opens, so they can derive no restart (2026-09-18;
#: S2-P2 ESCALATE 14, carried three times).
#:
#: An EXPLICIT LIST, deliberately, and never a glob on dotfiles: `.env` is a
#: dotfile the runtime very much reads, and the next dotfile nobody has
#: thought about is exactly the case ESCALATE exists for. A path earns its
#: way onto this list by someone establishing it has no runtime reader.
#: `.claude/` is NOT here — it is already HARNESS, which is what it is (L3).
REPO_META = frozenset({".gitignore", ".gitattributes", ".gitmodules"})
#: Operator scripts under ops/ — run by a human or an agent at a shell, never
#: imported by Cobalt and never named by a plist (2026-09-18).
#:
#: Explicit, for the same reason as REPO_META and with a sharper example:
#: `ops/*.sh` would be flatly wrong, because `ops/start_aset.sh` and
#: `ops/start_mainframe.sh` ARE read — they are what their residents' plists
#: execute. Living in ops/ says nothing about who reads a file.
OPS_TOOLS = frozenset({"ops/cto-desk.sh"})


class RestartError(RuntimeError):
    """The requested revision or import graph could not be classified."""


@dataclass(frozen=True)
class Change:
    path: str
    change: str


@dataclass(frozen=True)
class Classification:
    path: str
    change: str
    rule: str
    restarts: tuple[str, ...]
    escalate: bool = False


def _git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=False
    )
    if proc.returncode:
        raise RestartError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def changes(git_range: str) -> list[Change]:
    right = git_range.rsplit("...", 1)[-1].rsplit("..", 1)[-1]
    rows: dict[str, str] = {}

    def collect(text: str) -> None:
        for line in text.splitlines():
            if not line.strip():
                continue
            parts = line.split("\t")
            status = parts[0]
            path = parts[-1]
            rows[path] = status[0]

    collect(_git("diff", "--name-status", git_range))
    if right in {"HEAD", "WORKTREE"}:
        collect(_git("diff", "--name-status"))
        collect(_git("diff", "--cached", "--name-status"))
        for path in _git("ls-files", "--others", "--exclude-standard").splitlines():
            rows[path] = "A"
    return [Change(path, rows[path]) for path in sorted(rows)]


def _module_for(path: Path) -> str | None:
    try:
        rel = path.relative_to(REPO_ROOT / "src")
    except ValueError:
        return None
    if rel.suffix != ".py":
        return None
    parts = list(rel.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def _resolve_from(module: str, node: ast.ImportFrom) -> str | None:
    if node.level == 0:
        return node.module
    package = module.split(".")[:-1]
    if node.level > len(package) + 1:
        return None
    base = package[: len(package) - node.level + 1]
    if node.module:
        base.extend(node.module.split("."))
    return ".".join(base)


def import_graph() -> tuple[dict[str, set[str]], set[str]]:
    modules = {
        module: path
        for path in (REPO_ROOT / "src").rglob("*.py")
        if (module := _module_for(path))
    }
    graph: dict[str, set[str]] = {module: set() for module in modules}
    dynamic_unknown: set[str] = set()
    for module, path in modules.items():
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as e:
            raise RestartError(f"cannot parse imports in {path}: {e}") from e
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                graph[module].update(alias.name for alias in node.names if alias.name in modules)
            elif isinstance(node, ast.ImportFrom):
                target = _resolve_from(module, node)
                if target in modules:
                    graph[module].add(target)
                if target:
                    for alias in node.names:
                        child = f"{target}.{alias.name}"
                        if child in modules:
                            graph[module].add(child)
            elif isinstance(node, ast.Call):
                name = ""
                if isinstance(node.func, ast.Name):
                    name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    name = node.func.attr
                if name in {"import_module", "__import__", "run"} and node.args:
                    first = node.args[0]
                    if isinstance(first, ast.Constant) and isinstance(first.value, str):
                        target = first.value.split(":", 1)[0]
                        if target in modules:
                            graph[module].add(target)
                        elif target.startswith(("cobalt.", "cobalt_agent.")):
                            dynamic_unknown.add(module)
                    elif name in {"import_module", "__import__"}:
                        dynamic_unknown.add(module)
    return graph, dynamic_unknown


def reachable(roots: list[str], graph: dict[str, set[str]], unknown: set[str]) -> tuple[set[str], bool]:
    seen: set[str] = set()
    stack = list(roots)
    unresolved = False
    while stack:
        module = stack.pop()
        if module in seen:
            continue
        seen.add(module)
        unresolved = unresolved or module in unknown
        stack.extend(graph.get(module, ()))
    return seen, unresolved


def classify(git_range: str, registry: JobRegistry | None = None) -> list[Classification]:
    registry = registry or load_job_registry()
    residents = [job for job in registry.jobs if job.kind is JobKind.RESIDENT]
    graph, unknown = import_graph()
    reach: dict[str, set[str]] = {}
    conservative: set[str] = set()
    for job in residents:
        if job.imports is None:
            conservative.add(job.label)
            continue
        reached, unresolved = reachable(job.imports, graph, unknown)
        reach[job.label] = reached
        if unresolved:
            conservative.update(item.label for item in residents)
    all_labels = tuple(sorted(item.label for item in residents))
    output: list[Classification] = []
    for item in changes(git_range):
        path = item.path
        restarts: set[str] = set(conservative)
        rule = ""
        if path.startswith("ops/com.cobalt.") and path.endswith(".plist"):
            label = Path(path).stem
            if label in {job.label for job in residents}:
                restarts.add(label)
            rule = "plist in diff"
        readers = registry.readers_of(path)
        if readers:
            restarts.update(job.label for job in readers)
            rule = (rule + "; " if rule else "") + "resident reads"
        elif (declared := registry.no_resident_read(path)) is not None:
            rule = (rule + "; " if rule else "") + (
                f"no resident reads (one-shot: {','.join(declared.readers)})"
            )
        module = _module_for(REPO_ROOT / path)
        if path.startswith("src/"):
            if module:
                matched = [label for label, modules in reach.items() if module in modules]
                restarts.update(matched)
                rule = (rule + "; " if rule else "") + "static import reach"
            else:
                rule = (rule + "; " if rule else "") + "non-Python src asset"
        if not rule and path == "configs/cobalt/jobs.yaml":
            rule = "registry; register, no restart"
        if not rule and (path.startswith("docs/") or path in ROOT_DOCS):
            # L42 amendment O9: documentation with no runtime reader derives
            # no restart, not even the conservative set.
            output.append(Classification(path, item.change, "DOCS", ()))
            continue
        if not rule and path in OPS_TOOLS:
            output.append(
                Classification(path, item.change, "operator script; no Cobalt reader", ())
            )
            continue
        if not rule and path in REPO_META:
            # Repo metadata with no runtime reader derives no restart — the
            # same shape as the 09-15 DOCS rule, for git's own bookkeeping.
            output.append(Classification(path, item.change, "META", ()))
            continue
        if not rule and (path.startswith(".claude/") or path in HARNESS_FILES):
            # Claude Code harness settings: read by the agent CLI, never by a
            # Cobalt process (committed 2026-09-15).
            output.append(Classification(path, item.change, "HARNESS; no Cobalt reader", ()))
            continue
        if not rule and path.startswith("tests/"):
            rule = "test/documentation; no resident"
        if not rule and path == "ops/README.md":
            rule = "operations documentation; no resident"
        if not rule and path == "configs/cobalt/watchlists.yaml":
            rule = "one-shot archiver reads fresh; no resident"
        if not rule and path.startswith("configs/"):
            output.append(Classification(path, item.change, "UNCLASSIFIED CONFIG", all_labels, True))
            continue
        if not rule:
            output.append(Classification(path, item.change, "UNCLASSIFIED", all_labels, True))
            continue
        output.append(Classification(path, item.change, rule, tuple(sorted(restarts))))
    return output


def command(args) -> None:
    rows = classify(args.git_range)
    print("path\tchange\trule\trestart")
    for row in rows:
        restart = ",".join(row.restarts) or "-"
        print(f"{row.path}\t{row.change}\t{row.rule}\t{restart}")
        if row.escalate:
            print(f"ESCALATE: unclassified path {row.path}")
    labels = sorted({label for row in rows for label in row.restarts})
    print("RESTARTS: " + (" ".join(labels) if labels else "none"))
    if any(row.escalate for row in rows):
        raise RestartError("one or more changed paths were unclassified")


__all__ = ["Change", "Classification", "RestartError", "changes", "classify", "import_graph"]
