"""E6 restart derivation tests."""

import ast
import shutil
from pathlib import Path

import pytest

from cobalt.jobs import restarts
from cobalt.jobs.restarts import Change, classify, reachable


def test_reachable_static_graph_and_unknown_dynamic_import():
    graph = {"root": {"child"}, "child": set()}
    assert reachable(["root"], graph, set()) == ({"root", "child"}, False)
    assert reachable(["root"], graph, {"child"}) == ({"root", "child"}, True)


def test_plist_read_and_docs_rules(monkeypatch):
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("ops/com.cobalt.radar.plist", "A"),
        Change("configs/cobalt/radar.yaml", "A"),
        Change("docs/example.md", "M"),
    ])
    rows = classify("HEAD...HEAD")
    by_path = {row.path: row for row in rows}
    assert by_path["ops/com.cobalt.radar.plist"].restarts == ("com.cobalt.radar",)
    assert "com.cobalt.radar" in by_path["configs/cobalt/radar.yaml"].restarts
    assert by_path["docs/example.md"].restarts == ()


def test_documentation_paths_derive_no_restart_and_are_labelled_docs(monkeypatch):
    # L42 amendment O9: a documentation path with no runtime reader derives
    # no restart; a root markdown file is never UNCLASSIFIED.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("QWEN.md", "M"),
        Change("docs/40 - DevDocs/reports/ops-2026-09-15.md", "A"),
        Change("src/cobalt/cli.py", "M"),
    ])
    by_path = {row.path: row for row in classify("HEAD...HEAD")}
    for path in ("QWEN.md", "docs/40 - DevDocs/reports/ops-2026-09-15.md"):
        assert by_path[path].rule == "DOCS"
        assert by_path[path].restarts == ()
        assert by_path[path].escalate is False
    assert "com.cobalt.radar" in by_path["src/cobalt/cli.py"].restarts
    assert not any(row.escalate for row in by_path.values())


def test_claude_harness_settings_derive_no_restart(monkeypatch):
    # `.claude/settings.json` is read by the Claude Code harness, never by a
    # Cobalt process (committed 2026-09-15).
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change(".claude/settings.json", "A"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is False
    assert row.restarts == ()


def test_grok_sandbox_profile_is_harness_and_derives_no_restart(monkeypatch):
    # 2026-09-17: `ops/grok-sandbox.toml` is the Grok CLI's sandbox profile,
    # read by the Grok harness (`~/.grok/sandbox.toml`), never by a Cobalt
    # process. It derived UNCLASSIFIED (all residents) on 09-16.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("ops/grok-sandbox.toml", "A"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is False
    assert row.restarts == ()
    assert row.rule.startswith("HARNESS")


def test_repo_meta_files_derive_no_restart_and_are_labelled_meta(monkeypatch):
    # Carried three times (S2-P2 ESCALATE 14): `.gitignore` is git's own
    # bookkeeping. No Cobalt process opens it, so it can derive no restart —
    # but it escalated as UNCLASSIFIED (all residents) on every range that
    # touched it.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change(".gitignore", "M"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.rule == "META"
    assert row.restarts == ()
    assert row.escalate is False


def test_every_repo_meta_path_is_meta(monkeypatch):
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change(path, "M") for path in sorted(restarts.REPO_META)
    ])
    rows = classify("HEAD...HEAD")
    assert len(rows) == len(restarts.REPO_META)
    assert {row.rule for row in rows} == {"META"}
    assert not any(row.escalate for row in rows)


def test_an_operator_script_with_no_cobalt_reader_derives_no_restart(monkeypatch):
    # `ops/cto-desk.sh` is run by a human or an agent at a shell. No Cobalt
    # process imports or reads it and no plist names it, so it can derive no
    # restart — it escalated as UNCLASSIFIED (every resident) on the range
    # that added it.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("ops/cto-desk.sh", "A"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.restarts == ()
    assert row.escalate is False
    assert "no Cobalt reader" in row.rule


def test_a_resident_wrapper_script_is_not_an_operator_script(monkeypatch):
    # The reason OPS_TOOLS is an explicit list and not `ops/*.sh`:
    # `start_aset.sh` IS read — it is what com.cobalt.aset's plist executes.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("ops/start_aset.sh", "M"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is True
    assert row.restarts  # the conservative set, until someone rules on it


def test_an_unknown_dotfile_still_escalates(monkeypatch):
    # The rule is an EXPLICIT LIST, never a glob on dotfiles: a new dotfile
    # nobody has classified is exactly the case ESCALATE exists for (L42).
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change(".mystery-rc", "A"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.rule == "UNCLASSIFIED"
    assert row.escalate is True
    assert row.restarts  # the conservative set: every resident


def test_a_declared_one_shot_only_config_derives_no_restart(monkeypatch):
    # Ruled 2026-09-15: notify.yaml has no resident reader; declared in
    # jobs.yaml `no_resident_reads`, so it no longer escalates.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("configs/cobalt/notify.yaml", "M"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is False
    assert row.restarts == ()
    assert "no resident" in row.rule



def test_generated_rules_yaml_derives_no_restart(monkeypatch):
    # 2026-09-16: configs/cobalt/rules.yaml is regenerated and re-read by the
    # prefill one-shots only (daily.py / drc.py -> regenerate_rules_config);
    # the nightly generated commit escalated it as UNCLASSIFIED CONFIG.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("configs/cobalt/rules.yaml", "M"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is False
    assert row.restarts == ()
    assert "no resident" in row.rule


_LOADER = "cobalt.backup.config.load_backup_config"

#: Every function that reaches the loader, as the call-graph walk derives it
#: on the real tree (round-3 fix, 2026-09-22).
EXPECTED_BACKUP_YAML_READERS = frozenset({
    "cobalt.backup.config.load_backup_config",
    "cobalt.backup.restic.snapshot",
    "cobalt.backup.restic.latest_snapshot_age",
    "cobalt.backup.restic.restore",
    "cobalt.backup.cli._run",
    "cobalt.backup.cli._status",
    "cobalt.backup.cli._restore",
    "cobalt.heartbeat.probes.backup_freshness",
    "cobalt.heartbeat.runner.take_beat",
    "cobalt.heartbeat.runner.run_beat",
    "cobalt.heartbeat.cli.cmd_beat",
    "cobalt.heartbeat.cli.cmd_show",
})


def _backup_yaml_readers(root: Path) -> tuple[set[str], set[str], set[str], set[str]]:
    """Every function that reaches load_backup_config() through calls.

    Sol's Q2 (ops-6a-check-r2-2026-09-22.md row 15): a file-name check
    misses a new call in a listed file, an aliased import of the loader and
    a resident calling an existing wrapper. So this walks FUNCTION -> FUNCTION
    call edges, because module reach cannot answer it: com.cobalt.radar
    imports cobalt.cli, which imports every command module (restarts.md,
    smoke paragraph). It reuses the classifier's own walker (L3):
    restarts._module_for names modules, restarts._resolve_from resolves
    relative imports, and restarts.reachable is the traversal, run on the
    reversed call graph. Only the call/reference-edge extraction is new.

    Returns (readers, entrypoints, referrers, unresolved): entrypoints are
    readers no other reader calls; referrers hold a non-call reference to a
    reader (set_defaults(func=...)); unresolved holds every scope where the
    name load_backup_config did not resolve to the loader (L1: red, never
    silence). Code outside any function is the scope "<module>.<module>".
    """
    assert Path(restarts.REPO_ROOT) == root, "patch restarts.REPO_ROOT to the tree walked"
    name = _LOADER.rsplit(".", 1)[1]
    modules = {m: p for p in (root / "src").rglob("*.py") if (m := restarts._module_for(p))}
    trees = {m: ast.parse(p.read_text(encoding="utf-8"), filename=str(p)) for m, p in modules.items()}
    funcs: set[str] = set()
    classes: set[str] = set()
    toplevel: dict[str, set[str]] = {m: set() for m in modules}
    bindings: dict[str, dict[str, str]] = {m: {} for m in modules}

    def _package_name(m: str) -> str:
        # _resolve_from climbs from the module's parent; a package's
        # __init__ IS the package, so it resolves from "<pkg>.__init__".
        return f"{m}.__init__" if modules[m].name == "__init__.py" else m

    def _collect(m: str, node: ast.AST, prefix: str) -> None:
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                qual = f"{prefix}.{child.name}"
                (classes if isinstance(child, ast.ClassDef) else funcs).add(qual)
                if prefix == m:
                    toplevel[m].add(child.name)
                _collect(m, child, qual)
            else:
                _collect(m, child, prefix)

    for m, tree in trees.items():
        _collect(m, tree, m)
        # Imports at ANY depth: probes.backup_freshness imports the loader
        # inside the function. `from pkg import x` binds "pkg.x" whether x is
        # a module (restarts.import_graph's child-module rule) or a symbol.
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.asname:
                        bindings[m][alias.asname] = alias.name
                    else:
                        head = alias.name.split(".")[0]
                        bindings[m][head] = head
            elif isinstance(node, ast.ImportFrom):
                target = restarts._resolve_from(_package_name(m), node)
                if target:
                    for alias in node.names:
                        if alias.name != "*":
                            bindings[m][alias.asname or alias.name] = f"{target}.{alias.name}"

    def _canonical(dotted: str) -> str:
        # Follow package re-exports (cobalt.backup -> .config) to the
        # defining module, to a fixed point.
        seen: set[str] = set()
        while dotted not in funcs and dotted not in modules and dotted not in seen:
            seen.add(dotted)
            parts = dotted.split(".")
            owner = next(
                (i for i in range(len(parts) - 1, 0, -1) if ".".join(parts[:i]) in modules), None
            )
            if owner is None:
                return dotted
            bound = bindings[".".join(parts[:owner])].get(parts[owner])
            if bound is None:
                return dotted
            dotted = ".".join([bound, *parts[owner + 1 :]])
        return dotted

    def _resolve(m: str, scope: str, node: ast.AST) -> str | None:
        attrs: list[str] = []
        while isinstance(node, ast.Attribute):
            attrs.append(node.attr)
            node = node.value
        if not isinstance(node, ast.Name):
            return None
        base = None
        enclosing = scope
        while enclosing.startswith(m + "."):  # nested defs, innermost first
            if enclosing not in classes and f"{enclosing}.{node.id}" in funcs:
                base = f"{enclosing}.{node.id}"
                break
            enclosing = enclosing.rsplit(".", 1)[0]
        if base is None and node.id in toplevel[m]:
            base = f"{m}.{node.id}"
        if base is None and node.id in bindings[m]:
            base = bindings[m][node.id]
        if base is None:
            return None
        return _canonical(".".join([base, *reversed(attrs)]))

    callers: dict[str, set[str]] = {}  # callee -> caller scopes (reversed)
    references: dict[str, set[str]] = {}  # scope -> functions referred to
    unresolved: set[str] = set()

    def _visit(m: str, node: ast.AST, prefix: str, scope: str) -> None:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # Decorators, defaults and bases run in the enclosing scope.
            outer = [*node.decorator_list]
            if isinstance(node, ast.ClassDef):
                outer += [*node.bases, *node.keywords]
            else:
                outer += [*node.args.defaults, *(d for d in node.args.kw_defaults if d)]
            for part in outer:
                _visit(m, part, prefix, scope)
            qual = f"{prefix}.{node.name}"
            inner = scope if isinstance(node, ast.ClassDef) else qual
            for stmt in node.body:
                _visit(m, stmt, qual, inner)
            return
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            target = (
                restarts._resolve_from(_package_name(m), node)
                if isinstance(node, ast.ImportFrom) else None
            )
            for alias in node.names:
                if alias.name.split(".")[-1] == name:
                    full = f"{target}.{alias.name}" if isinstance(node, ast.ImportFrom) else alias.name
                    if _canonical(full) != _LOADER:
                        unresolved.add(scope)
            return
        if isinstance(node, ast.Call):
            callee = _resolve(m, scope, node.func)
            if callee is not None:
                callers.setdefault(callee, set()).add(scope)
        if isinstance(node, (ast.Name, ast.Attribute)):
            spelled = node.id if isinstance(node, ast.Name) else node.attr
            target = _resolve(m, scope, node)
            if spelled == name and target != _LOADER:
                unresolved.add(scope)
            if target in funcs and id(node) not in skip and isinstance(node.ctx, ast.Load):
                references.setdefault(scope, set()).add(target)
        if isinstance(node, ast.Call):
            skip.add(id(node.func))
        if isinstance(node, ast.Attribute):
            skip.add(id(node.value))
        for child in ast.iter_child_nodes(node):
            _visit(m, child, prefix, scope)

    skip: set[int] = set()  # a Call's func, or an inner link of a dotted chain
    for m, tree in trees.items():
        for stmt in tree.body:
            _visit(m, stmt, m, f"{m}.<module>")

    readers = restarts.reachable([_LOADER], callers, set())[0]
    entrypoints = {r for r in readers if not (callers.get(r, set()) - {r}) & readers}
    referrers = {s for s, targets in references.items() if targets & readers} - readers
    return readers, entrypoints, referrers, unresolved


def test_backup_yaml_is_read_by_one_shots_only_and_derives_no_restart(monkeypatch):
    # 2026-09-22: the 6a commit of `ops/2026-09-21` (the vault key-store file
    # joins restic's include set) changed configs/cobalt/backup.yaml, and
    # `cobalt jobs restarts main..HEAD` escalated it UNCLASSIFIED CONFIG
    # (every resident, exit 1) — round-1 check ops-6a-check-2026-09-22.md
    # ESCALATE 1. Two one-shots read it, through the one loader
    # load_backup_config(): com.cobalt.backup (backup/restic.py:164 via
    # `cobalt backup run`) and com.cobalt.heartbeat (heartbeat/probes.py:431,
    # backup_freshness, from take_beat). Checked here: every function that
    # reaches the loader through any chain of calls — through aliases and
    # module attributes — is pinned, with its CLI entrypoints (round-3 fix,
    # Sol's Q2). NOT checked: a resident PLIST invoking an operator command;
    # a second call inside a function that is already a reader (no new reader).
    from pathlib import Path

    from cobalt.jobs.config import JobKind, load_job_registry

    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("configs/cobalt/backup.yaml", "M"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is False
    assert row.restarts == ()
    # The string follows the declared `readers:` order in jobs.yaml.
    assert row.rule == "no resident reads (one-shot: com.cobalt.backup,com.cobalt.heartbeat)"

    readers, entrypoints, referrers, unresolved = _backup_yaml_readers(Path(restarts.REPO_ROOT))
    assert unresolved == set(), sorted(unresolved)
    assert readers == EXPECTED_BACKUP_YAML_READERS, sorted(readers)
    # Each entrypoint is a CLI handler (set_defaults(func=...)):
    #   _run      -> `cobalt backup run`     -> com.cobalt.backup (ops/run_backup.sh:39)
    #   cmd_beat  -> `cobalt heartbeat beat` -> com.cobalt.heartbeat
    #                (ops/com.cobalt.heartbeat.plist:30-43)
    #   _status, _restore, cmd_show -> operator commands, no job.
    assert entrypoints == {
        "cobalt.backup.cli._run",
        "cobalt.backup.cli._status",
        "cobalt.backup.cli._restore",
        "cobalt.heartbeat.cli.cmd_beat",
        "cobalt.heartbeat.cli.cmd_show",
    }, sorted(entrypoints)
    assert referrers == {
        "cobalt.backup.cli.add_parser",
        "cobalt.heartbeat.cli.add_parser",
    }, sorted(referrers)
    # No import-time read: nothing reads the file at module scope, so no
    # resident's static import reach (the classifier's own walk) can read it
    # by importing. Vacuous today; a real guard the day someone does.
    import_time = {r.removesuffix(".<module>") for r in readers if r.endswith(".<module>")}
    assert not import_time
    graph, unknown = restarts.import_graph()
    for job in load_job_registry().jobs:
        if job.kind is JobKind.RESIDENT and job.imports:
            assert not restarts.reachable(job.imports, graph, unknown)[0] & import_time, job.label

    declared = load_job_registry().no_resident_read("configs/cobalt/backup.yaml")
    assert declared is not None
    assert set(declared.readers) == {"com.cobalt.backup", "com.cobalt.heartbeat"}
    assert all(
        load_job_registry().by_label[label].kind is JobKind.ONE_SHOT
        for label in declared.readers
    )


# Sol's three cases (round-2 check row 15), each planted in a fresh copy of
# the REAL src/ tree (L45): the walk must find the planted reader, so the
# pinned reader set cannot survive any of them.
_DUMP_DATABASE_RETURN = '    return dump_database_to(name, into / f"{name}.sql")\n'
_PLANTED_CALL = "    load_backup_config()  # planted: a new call inside a listed file\n"


@pytest.mark.parametrize(
    "case", ["new_call_in_listed_file", "aliased_loader_import", "resident_uses_wrapper"]
)
def test_backup_yaml_reader_proof_goes_red_through_any_wrapper(monkeypatch, tmp_path, case):
    src = tmp_path / "src"
    shutil.copytree(
        Path(restarts.REPO_ROOT) / "src", src, ignore=shutil.ignore_patterns("__pycache__")
    )
    monkeypatch.setattr(restarts, "REPO_ROOT", tmp_path)
    if case == "new_call_in_listed_file":
        # dump_database (backup/restic.py) is not a reader today.
        restic = src / "cobalt" / "backup" / "restic.py"
        text = restic.read_text(encoding="utf-8")
        assert text.count(_DUMP_DATABASE_RETURN) == 1
        restic.write_text(
            text.replace(_DUMP_DATABASE_RETURN, _PLANTED_CALL + _DUMP_DATABASE_RETURN),
            encoding="utf-8",
        )
        planted = {"cobalt.backup.restic.dump_database"}
    elif case == "aliased_loader_import":
        (src / "cobalt" / "radar" / "_planted_reader.py").write_text(
            "from cobalt.backup.config import load_backup_config as _cfg\n"
            "\n"
            "\n"
            "def planted():\n"
            "    return _cfg()\n",
            encoding="utf-8",
        )
        planted = {"cobalt.radar._planted_reader.planted"}
    else:
        # A resident module calling each existing wrapper with no cfg: once
        # all three from one function, then each from its own, so every
        # wrapper chain must resolve on its own — latest_snapshot_age alone
        # would otherwise make `planted` a reader (run B, round-3 report).
        (src / "cobalt" / "radar" / "_planted_beat.py").write_text(
            "from cobalt.backup.restic import latest_snapshot_age\n"
            "from cobalt.heartbeat import probes as hb\n"
            "from cobalt.heartbeat.runner import take_beat\n"
            "\n"
            "\n"
            "def planted():\n"
            "    take_beat()\n"
            "    hb.backup_freshness()\n"
            "    latest_snapshot_age()\n"
            "\n"
            "\n"
            "def planted_take_beat():\n"
            "    take_beat()\n"
            "\n"
            "\n"
            "def planted_backup_freshness():\n"
            "    hb.backup_freshness()\n"
            "\n"
            "\n"
            "def planted_latest_snapshot_age():\n"
            "    latest_snapshot_age()\n",
            encoding="utf-8",
        )
        planted = {
            "cobalt.radar._planted_beat.planted",
            "cobalt.radar._planted_beat.planted_take_beat",
            "cobalt.radar._planted_beat.planted_backup_freshness",
            "cobalt.radar._planted_beat.planted_latest_snapshot_age",
        }

    readers, _entrypoints, _referrers, unresolved = _backup_yaml_readers(tmp_path)
    assert unresolved == set()
    assert planted <= readers, sorted(readers)
    assert readers != EXPECTED_BACKUP_YAML_READERS


def test_a_new_one_shot_plist_derives_an_explicit_bootstrap_and_no_restart(monkeypatch):
    # S2-P4 R1-22/R2-6: a brand-new one-shot plist used to vanish from the
    # derivation. Its action is now explicit: bootstrap once, restart nothing.
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("ops/com.cobalt.replay.plist", "A"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is False
    assert row.restarts == ()
    assert "bootstrap once: com.cobalt.replay" in row.rule


def test_a_smoke_suite_file_derives_no_restart_and_no_job_runs_the_smoke(monkeypatch):
    # S2-P4 §5 (Astra R2-6): `configs/cobalt/smoke/<suite>.yaml` is read only
    # by `cobalt smoke`, an operator command. No plist runs it, and the only
    # code that opens a suite file is `smoke/cli.py`'s `run` — both halves of
    # that claim are checked here, so the rule stops being true the moment
    # either changes. (Import reach is not the question: `com.cobalt.radar`
    # enters through `cobalt.cli`, which mounts every command module, so a
    # change to smoke's CODE still derives that restart by the src/ rule.)
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("configs/cobalt/smoke/s2.yaml", "A"),
    ])
    (row,) = classify("HEAD...HEAD")
    assert row.escalate is False
    assert row.restarts == ()
    assert "operator command" in row.rule

    from pathlib import Path

    repo = Path(restarts.REPO_ROOT)
    assert not [p.name for p in (repo / "ops").glob("com.cobalt.*.plist") if "smoke" in p.read_text()]
    openers = sorted(
        str(p.relative_to(repo))
        for p in (repo / "src").rglob("*.py")
        if any(token in p.read_text() for token in ("load_suite(", "suite_path(", "SUITES_DIR"))
    )
    assert openers == ["src/cobalt/smoke/cli.py", "src/cobalt/smoke/config.py"]
