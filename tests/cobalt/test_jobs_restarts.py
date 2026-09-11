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

