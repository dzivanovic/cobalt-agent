"""Seam S1 §2.3 — the route registry `configs/cobalt/modelaccess.yaml`.

`extra="forbid"`, a missing key crashes (L1), `lane: local` ⇒ loopback host,
no `fallback` key (FINAL [F-23]: fallback is the routing lane's, frozen).
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from cobalt.modelaccess import load_routes
from cobalt.modelaccess.config import CONFIG_PATH, ModelAccessConfigError

GOOD = {
    "routes": {
        "local.plan": {
            "lane": "local",
            "kind": "openai_compatible",
            "api_base": "http://127.0.0.1:1234/v1",
            "model": "mainframe",
            "no_think": True,
            "think_policy": "forbid_nonempty",
            "timeout_s": 30,
            "max_output_tokens": 256,
            "response_format": "json_schema",
            "key_name": None,
        }
    }
}


def _write(tmp_path: Path, data) -> Path:
    p = tmp_path / "modelaccess.yaml"
    p.write_text(yaml.safe_dump(data))
    return p


def _route(**over):
    import copy

    d = copy.deepcopy(GOOD)
    d["routes"]["local.plan"].update(over)
    return d


def test_committed_registry_loads_with_exactly_the_local_plan_route():
    cfg = load_routes(CONFIG_PATH)
    assert list(cfg.routes) == ["local.plan"]
    r = cfg.routes["local.plan"]
    assert (r.lane, r.kind, r.model, r.no_think, r.think_policy) == (
        "local", "openai_compatible", "mainframe", True, "forbid_nonempty")
    assert r.api_base == "http://127.0.0.1:1234/v1"
    assert r.key_name is None


def test_committed_registry_lives_outside_the_old_loader_glob():
    # CLAUDE.md config boundary: configs/*.yaml (top level) is the old tree's.
    assert CONFIG_PATH.parent.name == "cobalt" and CONFIG_PATH.parent.parent.name == "configs"


def test_a_good_file_loads(tmp_path):
    assert load_routes(_write(tmp_path, GOOD)).routes["local.plan"].timeout_s == 30


@pytest.mark.parametrize("key", list(GOOD["routes"]["local.plan"]))
def test_every_missing_key_crashes(tmp_path, key):
    d = _route()
    del d["routes"]["local.plan"][key]
    with pytest.raises(ModelAccessConfigError) as e:
        load_routes(_write(tmp_path, d))
    assert key in str(e.value)


@pytest.mark.parametrize("host", ["10.0.0.5", "192.168.1.20", "example.com", "0.0.0.0", "100.64.0.1"])
def test_a_local_lane_with_a_non_loopback_host_refuses_to_load(tmp_path, host):
    with pytest.raises(ModelAccessConfigError) as e:
        load_routes(_write(tmp_path, _route(api_base=f"http://{host}:1234/v1")))
    assert "loopback" in str(e.value)


@pytest.mark.parametrize("host", ["127.0.0.1", "localhost", "[::1]"])
def test_loopback_hosts_load(tmp_path, host):
    load_routes(_write(tmp_path, _route(api_base=f"http://{host}:1234/v1")))


def test_a_fallback_key_refuses_to_load(tmp_path):
    with pytest.raises(ModelAccessConfigError) as e:
        load_routes(_write(tmp_path, _route(fallback="cloud.plan")))
    assert "fallback" in str(e.value)


def test_a_top_level_fallback_refuses_too(tmp_path):
    d = _route()
    d["fallback"] = {"local.plan": "cloud.plan"}
    with pytest.raises(ModelAccessConfigError):
        load_routes(_write(tmp_path, d))


@pytest.mark.parametrize("field,value", [("lane", "metered"), ("kind", "openrouter_systemone"),
                                         ("think_policy", "strip"), ("response_format", "tool_call")])
def test_v1_accepts_only_its_one_lane_kind_and_policy(tmp_path, field, value):
    with pytest.raises(ModelAccessConfigError):
        load_routes(_write(tmp_path, _route(**{field: value})))


@pytest.mark.parametrize("field,value", [("timeout_s", 0), ("timeout_s", -1), ("max_output_tokens", 0)])
def test_budgets_must_be_positive(tmp_path, field, value):
    with pytest.raises(ModelAccessConfigError):
        load_routes(_write(tmp_path, _route(**{field: value})))


def test_a_key_value_is_never_a_config_field(tmp_path):
    # key_name is a VaultManager NAME; anything shaped like a secret value is refused.
    with pytest.raises(ModelAccessConfigError):
        load_routes(_write(tmp_path, _route(key_name="sk-" + "A" * 30)))


def test_a_missing_file_crashes(tmp_path):
    with pytest.raises(ModelAccessConfigError):
        load_routes(tmp_path / "absent.yaml")


def test_a_yaml_syntax_error_names_its_line(tmp_path):
    p = tmp_path / "modelaccess.yaml"
    p.write_text("routes:\n  local.plan:\n    lane: [local\n")
    with pytest.raises(ModelAccessConfigError) as e:
        load_routes(p)
    assert "line" in str(e.value)
