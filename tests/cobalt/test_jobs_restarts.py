"""E6 restart derivation tests."""

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
