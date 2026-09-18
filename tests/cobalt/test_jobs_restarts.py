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
