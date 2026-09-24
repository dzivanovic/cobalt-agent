"""C2 — `configs/cobalt/voice.yaml` and `configs/cobalt/agents/voice.yaml`.

FINAL §5 path refusals (each a test), W7 tunables (a missing key crashes,
L1/L10), G2/K5's `scratch_max_age_s ≤ stt_timeout_s` refusal, and the
agent registry entry (L16): a ROUTE NAME, the V1 tool allowlist, the
single confirm / cancel words ([F-08]).
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest
import yaml

from cobalt.voice import config as vc
from cobalt.voice import registry as vr

GOOD_VOICE = yaml.safe_load(vc.CONFIG_PATH.read_text())
GOOD_AGENT = yaml.safe_load(vr.CONFIG_PATH.read_text())


@pytest.fixture
def dirs(tmp_path, monkeypatch):
    """Scratch / model dirs under tmp_path — outside repo, vault and backup."""
    monkeypatch.delenv(vc.SCRATCH_ENV, raising=False)
    monkeypatch.delenv(vc.MODEL_ENV, raising=False)
    s, m = tmp_path / "scratch", tmp_path / "models"
    return s, m


def _voice(tmp_path: Path, s: Path, m: Path, **over) -> Path:
    d = copy.deepcopy(GOOD_VOICE)
    d["voice"]["scratch_dir"] = str(s)
    d["voice"]["model_dir"] = str(m)
    d["voice"].update(over)
    p = tmp_path / "voice.yaml"
    p.write_text(yaml.safe_dump(d))
    return p


# --- the committed files ----------------------------------------------


def test_committed_voice_config_loads_with_the_dev_defaults(monkeypatch):
    monkeypatch.delenv(vc.SCRATCH_ENV, raising=False)
    monkeypatch.delenv(vc.MODEL_ENV, raising=False)
    cfg = vc.load_voice_config()
    assert cfg.scratch_dir == Path("/Users/cobalt/.cobalt-dev/voice-scratch")
    assert cfg.model_dir == Path("/Users/cobalt/.cobalt-dev/voice-models")
    assert cfg.stt_engine == "faster-whisper"
    assert cfg.plan_route == "local.plan"
    assert cfg.allowed_peers == ["127.0.0.1", "::1"]
    assert cfg.scratch_max_age_s > cfg.stt_timeout_s


def test_committed_files_sit_outside_the_old_loader_glob():
    # configs/*.yaml (top level) is the old tree's live glob (CLAUDE.md).
    assert vc.CONFIG_PATH.parent.name == "cobalt"
    assert vr.CONFIG_PATH.parent.name == "agents" and vr.CONFIG_PATH.parent.parent.name == "cobalt"


def test_every_tunable_names_its_source_in_the_committed_file():
    """C5 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 5): each key's
    OWN comment block — the comment lines directly above it, back to the
    previous key or the section line — holds `# source:`."""
    lines = vc.CONFIG_PATH.read_text().splitlines()
    checked = []
    for key in GOOD_VOICE["voice"]:
        (at,) = [i for i, l in enumerate(lines) if l.startswith(f"  {key}:")]
        block = []
        i = at - 1
        while i >= 0 and lines[i].lstrip().startswith("#") and lines[i].startswith("  "):
            block.append(lines[i])
            i -= 1
        assert any("# source:" in l for l in block), key
        checked.append(key)
    assert checked == list(GOOD_VOICE["voice"]) and len(checked) == 14


# --- W7: a missing key crashes ---------------------------------------------


@pytest.mark.parametrize("key", list(GOOD_VOICE["voice"]))
def test_every_missing_key_crashes(tmp_path, dirs, key):
    s, m = dirs
    p = _voice(tmp_path, s, m)
    d = yaml.safe_load(p.read_text())
    del d["voice"][key]
    p.write_text(yaml.safe_dump(d))
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(p)
    assert key in str(e.value)


def test_an_unknown_key_crashes(tmp_path, dirs):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError):
        vc.load_voice_config(_voice(tmp_path, s, m, cloud_stt="on"))


def test_stt_engine_has_no_cloud_value(tmp_path, dirs):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError):
        vc.load_voice_config(_voice(tmp_path, s, m, stt_engine="cloud"))


# --- FINAL §5: the path refusals -----------------------------------------


def test_a_good_tmp_layout_loads(tmp_path, dirs):
    s, m = dirs
    cfg = vc.load_voice_config(_voice(tmp_path, s, m))
    assert cfg.scratch_dir == s.resolve() and cfg.model_dir == m.resolve()


@pytest.mark.parametrize("field", ["scratch_dir", "model_dir"])
def test_a_relative_path_is_refused(tmp_path, dirs, field):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, **{field: "relative/dir"}))
    assert "relative" in str(e.value)


@pytest.mark.parametrize("field", ["scratch_dir", "model_dir"])
def test_a_path_under_the_repo_root_is_refused(tmp_path, dirs, field):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, **{field: str(vc.REPO_ROOT / "scratch" / "x")}))
    assert "repo" in str(e.value)


@pytest.mark.parametrize("field", ["scratch_dir", "model_dir"])
def test_a_path_under_docs_is_refused(tmp_path, dirs, field):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, **{field: str(vc.REPO_ROOT / "docs" / "voice")}))
    # C8 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 8): the docs
    # refusal's exact message, its fixed tail read from config.py's source.
    import inspect

    (src_line,) = [l for l in inspect.getsource(vc._check_path).splitlines() if "sits under docs/" in l]
    tail = src_line.split("{p} ", 1)[1].split('"', 1)[0]
    assert str(e.value) == f"{field} {(vc.REPO_ROOT / 'docs' / 'voice').resolve()} {tail}"


@pytest.mark.parametrize("field", ["scratch_dir", "model_dir"])
def test_a_path_under_the_resolved_vault_is_refused(tmp_path, dirs, field, monkeypatch):
    s, m = dirs
    vault = tmp_path / "devvault"
    vault.mkdir()
    monkeypatch.setenv("COBALT_VAULT_PATH", str(vault))
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, **{field: str(vault / "voice")}))
    assert "vault" in str(e.value)


@pytest.mark.parametrize("field", ["scratch_dir", "model_dir"])
def test_a_path_under_the_production_vault_is_refused_even_in_dev(tmp_path, dirs, field):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, **{field: "/Users/cobalt/Vault/Think/voice"}))
    assert "vault" in str(e.value)


@pytest.mark.parametrize("field", ["scratch_dir", "model_dir"])
def test_a_path_under_a_backup_source_is_refused(tmp_path, dirs, field):
    s, m = dirs
    src = tmp_path / "backed-up"
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, **{field: str(src / "voice")}), backup_sources=[src])
    assert "backup" in str(e.value)


def _backup_sources() -> list[Path]:
    from cobalt.backup.config import load_backup_config

    return [Path(p) for p in load_backup_config().sources]


def _start_aset_exports() -> dict[str, str]:
    import re

    text = (vc.REPO_ROOT / "ops" / "start_aset.sh").read_text()
    return dict(re.findall(r'^export (COBALT_VOICE_[A-Z_]+)="([^"]+)"', text, re.M))


def test_the_production_overrides_are_exported_by_the_aset_launcher():
    ex = _start_aset_exports()
    assert ex == {vc.SCRATCH_ENV: "/Users/cobalt/.cobalt/voice-scratch",
                  vc.MODEL_ENV: "/Users/cobalt/.cobalt/voice-models"}


@pytest.mark.parametrize("which", ["committed", "production"])
def test_every_real_path_is_clear_of_every_backup_source(which, monkeypatch):
    """FINAL §5 against the REAL backup.yaml: the committed dev values and
    the production overrides in ops/start_aset.sh load with every backup
    source passed (the resident itself does not read backup.yaml — see
    load_voice_config's docstring)."""
    monkeypatch.delenv(vc.SCRATCH_ENV, raising=False)
    monkeypatch.delenv(vc.MODEL_ENV, raising=False)
    if which == "production":
        for k, v in _start_aset_exports().items():
            monkeypatch.setenv(k, v)
    cfg = vc.load_voice_config(backup_sources=_backup_sources())
    srcs = [str(p) for p in _backup_sources()]
    assert "/Users/cobalt/Vault/Think" in srcs
    for p in (cfg.scratch_dir, cfg.model_dir):
        assert not any(str(p).startswith(s) for s in srcs)


def test_the_resident_loader_reads_no_backup_config():
    import inspect

    src = inspect.getsource(vc)
    assert "load_backup_config" not in src and "backup.config" not in src


# --- G2 / K5 --------------------------------------------------------------


@pytest.mark.parametrize("age", [5, 10])
def test_scratch_age_not_above_stt_timeout_is_refused(tmp_path, dirs, age):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, stt_timeout_s=10, scratch_max_age_s=age))
    assert "scratch_max_age_s" in str(e.value)


# --- the env overrides (the vault pattern) ---------------------------------


def test_env_overrides_win_and_are_checked_too(tmp_path, dirs, monkeypatch):
    s, m = dirs
    p = _voice(tmp_path, s, m)
    monkeypatch.setenv(vc.SCRATCH_ENV, str(tmp_path / "o-scratch"))
    monkeypatch.setenv(vc.MODEL_ENV, str(tmp_path / "o-models"))
    cfg = vc.load_voice_config(p)
    assert cfg.scratch_dir == (tmp_path / "o-scratch").resolve()
    assert cfg.model_dir == (tmp_path / "o-models").resolve()
    monkeypatch.setenv(vc.SCRATCH_ENV, "relative")
    with pytest.raises(vc.VoiceConfigError):
        vc.load_voice_config(p)


@pytest.mark.parametrize("which", ["scratch", "model"])
@pytest.mark.parametrize("value", ["", "   "])
def test_a_set_but_empty_env_override_crashes(tmp_path, dirs, monkeypatch, which, value):
    """C3 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 3; L1 "a config
    error crashes; it never silently falls back"): an override that is SET
    but empty is an error naming the variable — never the committed default."""
    s, m = dirs
    var = vc.SCRATCH_ENV if which == "scratch" else vc.MODEL_ENV
    monkeypatch.setenv(var, value)
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m))
    assert var in str(e.value)


def test_plan_route_must_equal_the_agent_registry_route(tmp_path, dirs):
    """C9 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 9; L1, L3): a
    `plan_route` that is not the agent registry's `route` crashes, naming both."""
    s, m = dirs
    registry_route = vr.load_agent().route
    with pytest.raises(vc.VoiceConfigError) as e:
        vc.load_voice_config(_voice(tmp_path, s, m, plan_route="local.other"))
    assert "local.other" in str(e.value) and registry_route in str(e.value)


@pytest.mark.parametrize("field", ["allowed_peers"])
def test_allowed_peers_must_be_ip_literals(tmp_path, dirs, field):
    s, m = dirs
    with pytest.raises(vc.VoiceConfigError):
        vc.load_voice_config(_voice(tmp_path, s, m, allowed_peers=["localhost"]))
    with pytest.raises(vc.VoiceConfigError):
        vc.load_voice_config(_voice(tmp_path, s, m, allowed_peers=[]))


# --- the agent registry (L16) ---------------------------------------------


def _agent(tmp_path, **over) -> Path:
    d = copy.deepcopy(GOOD_AGENT)
    d["agent"].update(over)
    p = tmp_path / "voice-agent.yaml"
    p.write_text(yaml.safe_dump(d))
    return p


def test_committed_agent_is_the_v1_allowlist():
    a = vr.load_agent()
    assert a.id == "voice"
    assert a.route == "local.plan"
    assert sorted(a.tools) == ["cards.numbers", "cards.open", "cards.set_stop", "radar.pool"]
    assert {n: t.kind for n, t in a.tools.items()} == {
        "cards.open": "read", "radar.pool": "read", "cards.numbers": "read", "cards.set_stop": "act"}
    assert all(t.trading_logic is False for t in a.tools.values())
    assert a.confirm_words == ["yes"] and a.cancel_words == ["no"]
    assert a.charter.strip()


@pytest.mark.parametrize("route", [
    "http://127.0.0.1:1234/v1", "openai/gpt-x", "mainframe", "anthropic.model", "local.nope"])
def test_the_route_must_be_a_registered_route_name(tmp_path, route):
    with pytest.raises(vr.AgentConfigError):
        vr.load_agent(_agent(tmp_path, route=route))


@pytest.mark.parametrize("words", [["yes", "yeah"], ["yep"], [], ["Yes"]])
def test_confirm_words_are_exactly_yes(tmp_path, words):
    with pytest.raises(vr.AgentConfigError):
        vr.load_agent(_agent(tmp_path, confirm_words=words))


@pytest.mark.parametrize("words", [["no", "nope"], ["cancel"], []])
def test_cancel_words_are_exactly_no(tmp_path, words):
    with pytest.raises(vr.AgentConfigError):
        vr.load_agent(_agent(tmp_path, cancel_words=words))


def test_a_tool_the_code_does_not_have_is_refused(tmp_path):
    d = copy.deepcopy(GOOD_AGENT["agent"]["tools"])
    d["orders.place"] = {"kind": "act", "trading_logic": False, "args": {}}
    with pytest.raises(vr.AgentConfigError):
        vr.load_agent(_agent(tmp_path, tools=d))


def test_an_arg_type_the_code_does_not_parse_is_refused(tmp_path):
    d = copy.deepcopy(GOOD_AGENT["agent"]["tools"])
    d["cards.set_stop"]["args"]["stop"]["type"] = "free_text"
    with pytest.raises(vr.AgentConfigError):
        vr.load_agent(_agent(tmp_path, tools=d))


def test_a_missing_agent_key_crashes(tmp_path):
    d = copy.deepcopy(GOOD_AGENT)
    del d["agent"]["charter"]
    p = tmp_path / "a.yaml"
    p.write_text(yaml.safe_dump(d))
    with pytest.raises(vr.AgentConfigError):
        vr.load_agent(p)
