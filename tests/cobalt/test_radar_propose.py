"""Pure proposal derivation, artifacts, and note-target parity."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
from types import SimpleNamespace

import pytest
import yaml

from cobalt.archiver.collector import scrub
from cobalt.archiver.config import CONFIG_PATH, WatchlistsConfig
from cobalt.radar.models import PoolBlock
from cobalt.radar.notes import parse_note
from cobalt.radar import propose as propose_module
from cobalt.radar.propose import ProposalRefused, apply, artifact_sha256, build_artifact, derive_screens, render_lists
from cobalt.radar.sources import archive_targets
from cobalt.session import clock as session_clock_module


def test_prose_derives_only_the_fixture_screen_and_detects_f_mismatch():
    text = Path("tests/fixtures/radar/radar-screens.example.md").read_text()
    screens, evidence = derive_screens(text)
    assert [x.screen for x in screens] == ["example_session_scan"]
    assert evidence[0]["filters"].startswith("- Filters")
    with pytest.raises(ProposalRefused) as caught:
        derive_screens(text.replace("`sh_avgvol_o500`", "`sh_avgvol_o200`"))
    assert "f mismatch" in scrub(str(caught.value))


def test_artifact_sha_is_canonical_and_apply_refuses_changed_target_before_writer(tmp_path):
    target = tmp_path / "note.md"
    target.write_text("original")
    artifact = build_artifact("lists", target, hashlib.sha256(b"original").hexdigest(), {"input": "synthetic"},
        [{"section": None, "unit_id": None, "placement": "create_if_absent", "body": "synthetic"}])
    assert artifact_sha256(artifact) == artifact_sha256(json.loads(json.dumps(artifact)))
    proposal = tmp_path / "proposal.json"
    proposal.write_text(json.dumps(artifact))
    target.write_text("changed")
    with pytest.raises(ProposalRefused, match="target note sha256 changed"):
        apply(argparse.Namespace(proposal=str(proposal), sha256=artifact_sha256(artifact), hitl="synthetic"))


def test_rendered_committed_lists_parse_to_same_archive_targets(tmp_path):
    config = WatchlistsConfig.model_validate(yaml.safe_load(CONFIG_PATH.read_text()))
    path = tmp_path / "Radar Lists.md"
    path.write_text(render_lists(config))
    parsed = parse_note(path, "lists")
    assert parsed.ok, parsed.errors
    assert set(archive_targets(parsed)) == set(config.archive_targets())


FIXTURE = Path("tests/fixtures/radar/radar-screens.example.md")


def _fixture_pool_bytes():
    parsed = parse_note(FIXTURE, "screens")
    pool = next(item.block for item in parsed.blocks if isinstance(item.block, PoolBlock))
    return yaml.safe_dump(pool.model_copy().model_dump(mode="json"), sort_keys=False).encode()


def _proposal_env(tmp_path, monkeypatch, *, ft_sets=None):
    cfg = propose_module.load_config()
    target = tmp_path / cfg.notes.screens
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(FIXTURE.read_bytes())
    pool_path = tmp_path / "pool.yaml"
    pool_path.write_bytes(_fixture_pool_bytes())
    artifacts = []
    real_write = propose_module.write_artifact

    def capture(artifact):
        artifacts.append(deepcopy(artifact))
        return real_write(artifact, directory=tmp_path / "artifacts")

    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: tmp_path)
    monkeypatch.setattr(propose_module, "write_artifact", capture)
    monkeypatch.setattr(propose_module, "resolve_token", _fake_token)

    if ft_sets is not None:
        async def fake_get(_path, params, _token, *, on_metrics):
            on_metrics(SimpleNamespace(redirect_statuses=()))
            values = ft_sets[1] if params.get("ft") == 4 else ft_sets[0]
            return SimpleNamespace(text="Ticker\n" + "\n".join(values) + "\n")

        monkeypatch.setattr(propose_module, "finviz_get", fake_get)
    return target, pool_path, artifacts


async def _fake_token():
    return "synthetic-token"


def test_invalid_pool_block_refuses_before_artifact(tmp_path, monkeypatch):
    _target, pool_path, artifacts = _proposal_env(tmp_path, monkeypatch)
    pool_path.write_text("kind: pool\ncap: invalid\n")
    with pytest.raises(ProposalRefused) as caught:
        propose_module.screens_propose(
            argparse.Namespace(pool_block=str(pool_path), ft_compare=False)
        )
    assert "invalid pool-block file" in scrub(str(caught.value))
    assert artifacts == []


def test_each_derived_field_has_adjacent_verbatim_source_comment():
    text = FIXTURE.read_text()
    screens, evidence = derive_screens(text)
    body = propose_module._render_screen(screens[0], evidence[0])
    source_for = {
        "screen": evidence[0]["heading"],
        "f": evidence[0]["export"],
        "sort": evidence[0]["sort"],
        "columns": evidence[0]["columns"],
        "active_from": evidence[0]["active"],
        "active_to": evidence[0]["active"],
    }
    for field, source in source_for.items():
        expected = rf"# from: {re.escape(json.dumps(source))}\n{field}:"
        assert re.search(expected, body), scrub(
            f"{field} lacks its adjacent verbatim # from comment"
        )


def test_missing_prose_window_uses_session_span_and_proposed_marker():
    text = re.sub(r"^- Active:.*\n", "", FIXTURE.read_text(), flags=re.MULTILINE)
    screens, evidence = derive_screens(text)
    from cobalt.taxonomy.loader import load_tunables

    tunables = load_tunables().by_key
    assert screens[0].active_from == tunables["session.premarket_open"].value
    assert screens[0].active_to == tunables["session.aftermarket_close"].value
    assert "# PROPOSED" in propose_module._render_screen(screens[0], evidence[0])


@pytest.mark.parametrize("different", [False, True])
def test_ft_compare_adds_ft_only_when_ticker_sets_differ(tmp_path, monkeypatch, different):
    without = ["T00"]
    with_ft = ["T00", "T01"] if different else list(without)
    _target, pool_path, artifacts = _proposal_env(
        tmp_path, monkeypatch, ft_sets=(without, with_ft)
    )
    propose_module.screens_propose(
        argparse.Namespace(pool_block=str(pool_path), ft_compare=True)
    )
    assert len(artifacts) == 1
    body = artifacts[0]["units"][0]["body"]
    assert ("ft: 4" in body) is different
    assert artifacts[0]["inputs"]["ft_comparisons"] == [
        {
            "without": len(without),
            "with_4": len(with_ft),
            "symmetric_difference": ([] if not different else ["T01"]),
        }
    ]


def test_artifact_is_verbatim_insertion_only_and_stable(tmp_path, monkeypatch, capsys):
    target, pool_path, artifacts = _proposal_env(tmp_path, monkeypatch)
    original = target.read_bytes()
    args = argparse.Namespace(pool_block=str(pool_path), ft_compare=False)
    propose_module.screens_propose(args)
    first_output = scrub(capsys.readouterr().out)
    propose_module.screens_propose(args)
    second_output = scrub(capsys.readouterr().out)

    assert len(artifacts) == 2
    assert artifacts[0]["inputs"]["target_text"].encode() == original
    assert artifacts[0]["inputs"]["pool_block"].encode() == pool_path.read_bytes()
    assert target.read_bytes() == original
    assert artifacts[0] == artifacts[1]
    assert artifact_sha256(artifacts[0]) == artifact_sha256(artifacts[1])
    for output in (first_output, second_output):
        diff = output[output.index("--- "):]
        assert "+++ " in diff
        assert not any(
            line.startswith("-") and not line.startswith("---")
            for line in diff.splitlines()
        )


def test_lists_artifact_records_watchlists_blob_and_verbatim_bytes(tmp_path, monkeypatch):
    cfg = propose_module.load_config()
    artifacts = []
    real_write = propose_module.write_artifact

    def capture(artifact):
        artifacts.append(deepcopy(artifact))
        return real_write(artifact, directory=tmp_path / "artifacts")

    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: tmp_path)
    monkeypatch.setattr(propose_module, "write_artifact", capture)
    propose_module.lists_propose(argparse.Namespace())
    assert len(artifacts) == 1
    assert artifacts[0]["target_note"] == str(tmp_path / cfg.notes.lists)
    assert artifacts[0]["inputs"]["watchlists_yaml"].encode() == CONFIG_PATH.read_bytes()
    assert re.fullmatch(r"[0-9a-f]{40}", artifacts[0]["inputs"]["watchlists_git_blob"])


class RecordingWriter:
    calls = None

    def __init__(self, *args, **kwargs):
        self.calls.append(("writer", args, kwargs))

    def create_if_absent(self, *args, **kwargs):
        self.calls.append(("create_if_absent", args, kwargs))
        return SimpleNamespace(write_id=1, path=args[0], action="created")

    def upsert_unit(self, *args, **kwargs):
        self.calls.append(("upsert_unit", args, kwargs))
        return SimpleNamespace(write_id=1, path=args[0], action="updated")


class RecordingWriteStore:
    calls = None

    def __init__(self, *args, **kwargs):
        self.calls.append(("store", args, kwargs))

    def ensure_schema(self):
        self.calls.append(("ensure_schema", (), {}))


def _apply_artifact(tmp_path, monkeypatch, *, kind="screens", body="plain\n"):
    cfg = propose_module.load_config()
    target = tmp_path / (cfg.notes.screens if kind == "screens" else cfg.notes.lists)
    target.parent.mkdir(parents=True, exist_ok=True)
    if body is not None:
        target.write_text(body)
        target_sha = hashlib.sha256(body.encode()).hexdigest()
    else:
        target_sha = "absent"
    unit = (
        {"section": "Synthetic", "unit_id": "radar-screen-synthetic", "placement": "at_end", "body": "synthetic"}
        if kind == "screens"
        else {"section": None, "unit_id": None, "placement": "create_if_absent", "body": "synthetic"}
    )
    artifact = build_artifact(kind, target, target_sha, {"verbatim": "synthetic"}, [unit])
    proposal = tmp_path / f"{kind}.json"
    proposal.write_text(json.dumps(artifact))
    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: tmp_path)
    return target, artifact, proposal


@pytest.mark.parametrize(
    ("case", "expected"),
    [
        ("artifact_sha", "artifact sha256"),
        ("target_sha", "target note sha256"),
        ("lists_now_exists", "expected absent"),
        ("blocks_present", "fenced YAML blocks"),
        ("market_reset", "market_reset"),
        ("no_token", "token"),
        ("environment", "COBALT_ENV"),
    ],
)
def test_apply_refusal_matrix_precedes_writer_and_network(
    tmp_path, monkeypatch, case, expected
):
    kind = "lists" if case == "lists_now_exists" else "screens"
    body = None if case == "lists_now_exists" else ("```yaml\n{}\n```\n" if case == "blocks_present" else "plain\n")
    target, artifact, proposal = _apply_artifact(tmp_path, monkeypatch, kind=kind, body=body)
    digest = artifact_sha256(artifact)
    if case == "artifact_sha":
        digest = "0" * 64
    elif case == "target_sha":
        target.write_text("changed\n")
    elif case == "lists_now_exists":
        target.write_text("now present\n")
    elif case == "market_reset":
        monkeypatch.setattr(
            session_clock_module,
            "now_utc",
            lambda: __import__("datetime").datetime(2026, 9, 4, 0, 30, tzinfo=__import__("datetime").timezone.utc),
        )
    elif case == "environment":
        monkeypatch.setenv("COBALT_ENV", "production")

    calls = []
    RecordingWriter.calls = calls
    RecordingWriteStore.calls = calls
    monkeypatch.setattr(propose_module, "VaultWriter", RecordingWriter)
    monkeypatch.setattr(propose_module, "VaultWriteStore", RecordingWriteStore)
    network = []
    derivations = []

    async def forbidden_http(*args, **kwargs):
        network.append((args, kwargs))
        raise AssertionError(scrub("apply made an HTTP call"))

    def forbidden_derive(*args, **kwargs):
        derivations.append((args, kwargs))
        raise AssertionError(scrub("apply re-derived screens"))

    monkeypatch.setattr(propose_module, "finviz_get", forbidden_http)
    monkeypatch.setattr(propose_module, "derive_screens", forbidden_derive)
    args = argparse.Namespace(
        proposal=str(proposal),
        sha256=digest,
        hitl="" if case == "no_token" else "synthetic-token",
        proposal_kind=kind,
    )
    with pytest.raises(ProposalRefused) as caught:
        apply(args)
    assert expected in scrub(str(caught.value))
    assert calls == []
    assert network == []
    assert derivations == []


def test_apply_uses_artifact_units_without_http_or_rederivation(tmp_path, monkeypatch):
    _target, artifact, proposal = _apply_artifact(tmp_path, monkeypatch)
    calls = []
    RecordingWriter.calls = calls
    RecordingWriteStore.calls = calls
    monkeypatch.setattr(propose_module, "VaultWriter", RecordingWriter)
    monkeypatch.setattr(propose_module, "VaultWriteStore", RecordingWriteStore)

    async def forbidden_http(*_args, **_kwargs):
        raise AssertionError(scrub("apply made an HTTP call"))

    def forbidden_derive(*_args, **_kwargs):
        raise AssertionError(scrub("apply re-derived screens"))

    monkeypatch.setattr(propose_module, "finviz_get", forbidden_http)
    monkeypatch.setattr(propose_module, "derive_screens", forbidden_derive)
    apply(
        argparse.Namespace(
            proposal=str(proposal),
            sha256=artifact_sha256(artifact),
            hitl="synthetic-token",
            proposal_kind="screens",
        )
    )
    upserts = [call for call in calls if call[0] == "upsert_unit"]
    assert len(upserts) == 1
    assert upserts[0][1][1:4] == (
        artifact["units"][0]["section"],
        artifact["units"][0]["unit_id"],
        artifact["units"][0]["body"],
    )
