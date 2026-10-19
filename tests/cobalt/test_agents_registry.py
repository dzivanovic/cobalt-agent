"""F20 C1 — the generic agent registry (FINAL §2 `agents/registry.py`; T9; L16).

An agent exists only as a validated `configs/cobalt/agents/<id>.yaml`. A
tool the code catalog does not name is refused at load, and the chassis
admits the subscription login only (R1112). `voice.yaml` keeps its own
loader; the generic loader lists it by id and never re-validates it.
"""

from __future__ import annotations

import pytest

from hitl_support import AGENT_YAML


def test_cos_yaml_loads():
    from cobalt.agents.registry import AGENTS_DIR, TOOL_CATALOG, load_entry

    entry = load_entry(AGENTS_DIR / "cos.yaml")
    assert entry.id == "cos"
    assert entry.chassis.kind == "sdk" and entry.chassis.auth == "subscription"
    assert entry.chassis.model == "claude-sonnet-5-5"
    assert set(entry.tools) == set(TOOL_CATALOG)


def test_an_unknown_tool_is_refused_at_load():
    from cobalt.agents.registry import AgentRegistryError, parse_entry

    assert parse_entry(AGENT_YAML, where="constructed").tools == ["radar.pool"]
    with pytest.raises(AgentRegistryError, match="shell.run"):
        parse_entry(AGENT_YAML.replace("[radar.pool]", "[radar.pool, shell.run]"), where="constructed")


def test_an_api_key_chassis_is_refused():
    from cobalt.agents.registry import AgentRegistryError, parse_entry

    with pytest.raises(AgentRegistryError, match="auth"):
        parse_entry(AGENT_YAML.replace("auth: subscription", "auth: api_key"), where="constructed")


def test_voice_yaml_still_loads_through_its_own_loader():
    from cobalt.voice.registry import load_agent

    spec = load_agent()
    assert spec.id == "voice" and spec.route


def test_list_names_voice_and_cos():
    from cobalt.agents.registry import list_agents

    listed = {a.id: a for a in list_agents()}
    assert sorted(listed) == ["cos", "voice"]
    assert listed["voice"].validated is False, "voice.yaml is listed, never re-validated"
    assert listed["cos"].validated is True
