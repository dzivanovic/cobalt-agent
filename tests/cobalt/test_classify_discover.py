"""R3 — discover, KEYLESS. Over a fake transport; no socket.

The per-model endpoints record is the REAL public capture of 2026-09-23
(`tests/fixtures/classify/openrouter-model-entry.real-shape.json`, L45) —
the authority for his id (desk R46). The general list here is CONSTRUCTED
(small `{"data": [...]}` bodies): it is read only to record other matching
ids, and committing the real 457-entry list would add nothing the tests use.
Expected values are read FROM the fixture, never restated as constants.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from cobalt.classify import collector as col
from cobalt.classify.collector import ClassifyError, OpenRouterClassifier
from cobalt.classify.config import load_trial_config

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "classify" / "openrouter-model-entry.real-shape.json"
RAW = FIXTURE.read_bytes()
RECORD = json.loads(RAW)["data"]


def _list_body(*entries: dict, filler: int = 3) -> bytes:
    rows = [{"id": f"vendor/model-{i}", "name": f"Vendor Model {i}"} for i in range(filler)]
    return json.dumps({"data": [*rows, *entries]}).encode()


class Router:
    """Answers by URL; records every request (method, url, headers)."""

    def __init__(self, routes: dict[str, tuple[int, bytes]]):
        self.routes = routes
        self.calls: list[dict] = []

    def __call__(self, method, url, headers, body, timeout):
        self.calls.append({"method": method, "url": url, "headers": dict(headers), "body": body})
        return self.routes[url]


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    from cobalt.classify import config as cfg_mod

    monkeypatch.setattr(cfg_mod, "REPO_ROOT", tmp_path)
    return load_trial_config().model_copy(update={"spend_ledger": str(tmp_path / "scratch" / "classify-spend.jsonl"), "carried_spend": []})


def _routes(cfg, record=(200, RAW), listing=None):
    clf = OpenRouterClassifier(cfg)
    return {
        clf.endpoints_url(): record,
        cfg.models_url: (200, listing if listing is not None else _list_body()),
    }


def _clf(cfg, router):
    return OpenRouterClassifier(cfg, transport=router)


def test_the_endpoints_url_is_his_id_on_the_list_host(cfg):
    url = OpenRouterClassifier(cfg).endpoints_url()
    assert url == f"{cfg.models_url}/{cfg.model_id}/endpoints"
    assert url.startswith("https://openrouter.ai/")


def test_the_real_record_yields_his_entry(cfg):
    r = Router(_routes(cfg))
    d = _clf(cfg, r).discover_detail()
    (ep,) = RECORD["endpoints"]
    assert d.entry.id == RECORD["id"] == cfg.model_id
    assert d.entry.name == RECORD["name"]
    assert d.entry.created == RECORD["created"]
    assert d.entry.description == RECORD["description"]
    assert d.entry.architecture == RECORD["architecture"]
    # one endpoint → its per-endpoint fields ARE the model's
    assert d.entry.pricing == ep["pricing"]
    assert d.entry.context_length == ep["context_length"]
    assert d.entry.supported_parameters == ep["supported_parameters"]
    assert d.others == [] and d.raw_matches == []
    assert d.raw_record == RAW                          # byte for byte (L45)
    assert d.total == len(json.loads(_list_body())["data"])


def test_the_per_model_record_is_read_first_and_both_gets_are_keyless(cfg):
    r = Router(_routes(cfg))
    _clf(cfg, r).discover_detail()
    assert [c["url"] for c in r.calls] == [OpenRouterClassifier(cfg).endpoints_url(), cfg.models_url]
    for c in r.calls:
        assert c["method"] == "GET" and c["body"] is None
        assert "authorization" not in {k.lower() for k in c["headers"]}


def test_discover_never_reads_the_key(cfg, monkeypatch):
    def boom(name):
        raise AssertionError("discover read the vault")

    monkeypatch.setattr("cobalt.redact.secrets.read_secret", boom)
    _clf(cfg, Router(_routes(cfg))).discover_detail()


def test_another_matching_id_is_recorded_never_substituted(cfg):
    other = {"id": "typesafe/jev-9.99-constructed", "name": "TypeSafe: Jev constructed", "created": 1}
    r = Router(_routes(cfg, listing=_list_body(other)))
    d = _clf(cfg, r).discover_detail()
    assert d.entry.id == cfg.model_id
    assert [m.id for m in d.others] == [other["id"]]
    assert d.raw_matches == [other]
    assert _clf(cfg, Router(_routes(cfg, listing=_list_body(other)))).discover()[0].id == cfg.model_id


def test_his_id_in_the_general_list_is_not_counted_as_another(cfg):
    his = {"id": cfg.model_id, "name": RECORD["name"]}
    d = _clf(cfg, Router(_routes(cfg, listing=_list_body(his)))).discover_detail()
    assert d.others == []


def test_his_id_absent_raises_naming_it_and_the_matching_ids(cfg):
    other = {"id": "typesafe/jev-9.99-constructed", "name": "TypeSafe: Jev constructed"}
    r = Router(_routes(cfg, record=(404, b'{"error":{"code":404}}'), listing=_list_body(other)))
    with pytest.raises(ClassifyError) as e:
        _clf(cfg, r).discover_detail()
    msg = str(e.value)
    assert f"does not list {cfg.model_id}" in msg and other["id"] in msg


def test_no_match_anywhere_raises_with_the_count(cfg):
    listing = _list_body(filler=5)
    r = Router(_routes(cfg, record=(404, b"{}"), listing=listing))
    with pytest.raises(ClassifyError) as e:
        _clf(cfg, r).discover_detail()
    assert "lists no model matching" in str(e.value)
    assert f"{len(json.loads(listing)['data'])} models listed" in str(e.value)


def test_a_record_naming_another_id_is_refused(cfg):
    wrong = copy.deepcopy(json.loads(RAW))
    wrong["data"]["id"] = "typesafe/jev-9.99-constructed"
    r = Router(_routes(cfg, record=(200, json.dumps(wrong).encode())))
    with pytest.raises(ClassifyError, match="names id"):
        _clf(cfg, r).discover_detail()


def test_several_endpoints_are_not_merged_into_one_price(cfg):
    two = copy.deepcopy(json.loads(RAW))
    ep = two["data"]["endpoints"][0]
    two["data"]["endpoints"].append({**ep, "name": "constructed second endpoint"})
    d = _clf(cfg, Router(_routes(cfg, record=(200, json.dumps(two).encode())))).discover_detail()
    assert d.entry.pricing is None                      # L1: no cost picked for him


@pytest.mark.parametrize("status", [500, 429, 403])
def test_any_other_status_on_the_record_is_loud(cfg, status):
    r = Router(_routes(cfg, record=(status, b"nope")))
    with pytest.raises(ClassifyError, match=f"HTTP {status}"):
        _clf(cfg, r).discover_detail()


def test_an_unparseable_record_is_loud(cfg):
    r = Router(_routes(cfg, record=(200, b'{"data": []}')))
    with pytest.raises(ClassifyError, match="did not parse"):
        _clf(cfg, r).discover_detail()


def test_the_cli_writes_the_artifact_and_the_raw_record(cfg, tmp_path, monkeypatch, capsys):
    from cobalt.classify import cli as ccli

    router = Router(_routes(cfg))
    monkeypatch.setattr(ccli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(col, "urllib_transport", router)
    monkeypatch.setattr(ccli, "load_trial_config", lambda: cfg)

    class A:
        out = "scratch/openrouter-models-20260923.json"

    ccli.cmd_discover(A())
    out = tmp_path / A.out
    raw_out = tmp_path / "scratch" / "openrouter-models-20260923.endpoints.json"
    assert raw_out.read_bytes() == RAW
    art = json.loads(out.read_text())
    assert art["ruled_id"] == cfg.model_id and art["ruled_id_listed"] is True
    assert art["endpoints_record"] == json.loads(RAW)
    assert art["other_matching"] == []
    assert art["models_listed"] == len(json.loads(_list_body())["data"])
    line = capsys.readouterr().out
    assert line.startswith(f"DISCOVER ruled={cfg.model_id} ruled_listed=yes")
    assert "others=none" in line
    assert all("authorization" not in {k.lower() for k in c["headers"]} for c in router.calls)


def test_the_cli_refuses_an_out_outside_scratch(cfg, tmp_path, monkeypatch):
    from cobalt.classify import cli as ccli

    monkeypatch.setattr(ccli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(col, "urllib_transport", Router({}))
    monkeypatch.setattr(ccli, "load_trial_config", lambda: cfg)

    class A:
        out = "docs/models.json"

    with pytest.raises(ClassifyError, match="outside"):
        ccli.cmd_discover(A())
