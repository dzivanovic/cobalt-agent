"""Pure proposal derivation, artifacts, and note-target parity."""

import argparse
import hashlib
import json
import re
import subprocess
from contextlib import contextmanager
from copy import deepcopy
from datetime import UTC, datetime
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from cobalt.archiver.collector import scrub
from cobalt.archiver.config import load_config as load_archiver_config
from cobalt.radar import propose as propose_module
from cobalt.radar.models import PoolBlock
from cobalt.radar.notes import parse_note
from cobalt.radar.propose import (
    ProposalRefused,
    apply,
    artifact_sha256,
    build_artifact,
    derive_screens,
)
from cobalt.radar.sources import LegacyWatchlistsConfig
from cobalt.session import clock as session_clock_module
from cobalt.session.models import Session
from cobalt.vaultwrite import AT_END, VaultWriter
from cobalt.vaultwrite.markers import NAME_RE


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


FIXED_WATCHLISTS_BLOB = "bedf9bbfdadf98d85c3b3d32cdcb9fb678fb2b99"


def _fixed_watchlists_fixture(tmp_path):
    path = tmp_path / "legacy-watchlists.yaml"
    proc = subprocess.run(
        ["git", "cat-file", "blob", FIXED_WATCHLISTS_BLOB],
        capture_output=True,
        check=True,
    )
    path.write_bytes(proc.stdout)
    return path


def test_rendered_committed_lists_parse_to_same_archive_targets(tmp_path, monkeypatch):
    source = _fixed_watchlists_fixture(tmp_path)
    original = LegacyWatchlistsConfig.model_validate(yaml.safe_load(source.read_bytes()))
    radar_config = propose_module.load_config()
    artifacts = []
    real_write = propose_module.write_artifact

    def capture(artifact):
        artifacts.append(deepcopy(artifact))
        return real_write(artifact, directory=tmp_path / "artifacts")

    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: tmp_path)
    monkeypatch.setattr(propose_module, "write_artifact", capture)
    propose_module.lists_propose(argparse.Namespace(watchlists_yaml=str(source)))
    note = tmp_path / radar_config.notes.lists
    note.parent.mkdir(parents=True, exist_ok=True)
    note.write_text(artifacts[0]["units"][0]["body"], encoding="utf-8")
    config = load_archiver_config(note)
    assert set(config.archive_targets()) == set(original.archive_targets())
    assert set(config.backfill_targets("PROOF")) == set(original.backfill_targets("PROOF"))
    assert artifacts[0]["inputs"]["watchlists_git_blob"] == FIXED_WATCHLISTS_BLOB
    rendered = artifacts[0]["units"][0]["body"]
    assert "Derivation rules (exact, reproducible from the raw lists):" in rendered
    assert "FLAGGED JUDGMENT CALLS" in rendered
    assert len(original.archive_targets()) == 975


FIXTURE = Path("tests/fixtures/radar/radar-screens.example.md")
REAL_SHAPE_FIXTURE = Path("tests/fixtures/radar/radar-screens.real-shape.md")
REAL_COLUMNS = [0, 1, 4, 5, 129, 6, 7, 25, 26, 28, 30, 84, 93, 49, 83, 61, 63, 64, 67, 65, 66]
REAL_POOL = {
    "kind": "pool",
    "cap": 50,
    "priority": ["screens", "lists"],
    "rank_metric": {"premarket": "volume", "rth": "rvol", "aftermarket": "volume"},
    "overrides": {
        "morning_low_float": {"rank_metric": "volume"},
        "day_scan": {"first_from": "10:00"},
    },
    "stickiness_scans": 3,
}


def test_real_shape_fixture_exercises_all_seven_extraction_defects():
    text = REAL_SHAPE_FIXTURE.read_text(encoding="utf-8")
    screens, evidence = derive_screens(text)
    assert [item.screen for item in screens] == [
        "up_gappers", "down_gappers", "day_scan", "morning_low_float",
    ]
    assert [item.f for item in screens] == [
        "sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_u3",
        "sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_d3",
        "sh_curvol_o10000,sh_price_o1,sh_relvol_o3",
        "sh_float_u10,sh_price_u10,ta_gap_u10",
    ]
    assert [item.sort for item in screens] == [
        "-volume", "-relativevolume", "-volume", "-volume",
    ]
    assert all(item.columns == REAL_COLUMNS for item in screens)
    assert screens[2].active_from == "10:00"
    assert evidence[2]["active"] is not None
    assert evidence[0]["filters"].endswith("`ta_gap_u3` gap up > 3%")
    assert "**Sort:**" in evidence[0]["sort"]
    assert "**columns (`c=`):**" in evidence[0]["sort"]
    assert "o=" not in evidence[0]["export"]


def test_all_four_real_screen_marker_ids_are_valid_and_stable():
    text = REAL_SHAPE_FIXTURE.read_text(encoding="utf-8")
    _first_screens, first_evidence = derive_screens(text)
    _second_screens, second_evidence = derive_screens(text)

    first = [item["section_id"] for item in first_evidence]
    second = [item["section_id"] for item in second_evidence]
    first_units = [item["unit_id"] for item in first_evidence]
    second_units = [item["unit_id"] for item in second_evidence]
    assert first == ["radar-screen-1", "radar-screen-2", "radar-screen-3", "radar-screen-4"]
    assert second == first
    assert first_units == [f"{section_id}-definition" for section_id in first]
    assert second_units == first_units
    assert all(NAME_RE.fullmatch(marker_id) for marker_id in first + first_units)


def test_real_screen_marker_ids_do_not_follow_editable_display_names():
    text = REAL_SHAPE_FIXTURE.read_text(encoding="utf-8")
    _screens, original = derive_screens(text)
    edited = text.replace("Up Gappers", "Mixed Case Opening Movers", 1).replace(
        "Day Scan (after 10:00)", "Intraday Candidates (after 10:00)", 1
    )
    _edited_screens, changed = derive_screens(edited)

    assert [(item["section_id"], item["unit_id"]) for item in changed] == [
        (item["section_id"], item["unit_id"]) for item in original
    ]


@pytest.mark.parametrize(
    ("mutation", "expected"),
    [
        (lambda value: value.replace("&o=-volume&ar=10", "&o=-relativevolume&ar=10", 1), "sort mismatch"),
        (lambda value: value.replace("ta_gap_u3&c=<same columns>", "ta_gap_d3&c=<same columns>"), "f mismatch"),
        (
            lambda value: re.sub(r"&c=0%2C1%2C4%2C5%2C129[^`]+", "", re.sub(
                r" · \*\*columns \(`c=`\):\*\* [^\n]+", "", value, count=1
            ), count=1),
            "columns",
        ),
        (lambda value: value.replace("&c=0,1,4,5,129", "&c=0,2,4,5,129", 1), "columns mismatch"),
        (
            lambda value: value.replace("0%2C1%2C4", "0%2C1%2C1", 1).replace(
                "0,1,4", "0,1,1", 1
            ),
            "columns must be unique",
        ),
        (
            lambda value: value.replace("0%2C1%2C4", "151%2C1%2C4", 1).replace(
                "0,1,4", "151,1,4", 1
            ),
            "less than or equal to 150",
        ),
        (lambda value: value.replace("- **Intent:** premarket / open gap-up scan", "- **Sort:** `-volume`\n- **Intent:** premarket / open gap-up scan"), "duplicate prose field Sort"),
        (lambda value: value.replace("## Screen 2 — Down Gappers", "## Screen 2 — Up Gappers"), "duplicate screen key"),
        (
            lambda value: value.replace("## Screen 4 —", "## Morning Screen —"),
            "not a stable screen ordinal",
        ),
        (lambda value: value.replace("used after 10:00 ET", "used after 10:01 ET"), "conflicting start times"),
    ],
)
def test_real_shape_refusal_matrix(mutation, expected):
    with pytest.raises(ProposalRefused) as caught:
        derive_screens(mutation(REAL_SHAPE_FIXTURE.read_text(encoding="utf-8")))
    assert expected in scrub(str(caught.value))


def test_real_shape_supported_markup_variants_derive_equal_models():
    text = REAL_SHAPE_FIXTURE.read_text(encoding="utf-8")
    expected, _ = derive_screens(text)
    conventional = re.sub(r"\*\*([^*\n]+?):\*\*", r"**\1**:", text)
    actual, _ = derive_screens(conventional)
    assert actual == expected


def test_real_shape_gloss_and_url_encoding_edits_do_not_change_models():
    text = REAL_SHAPE_FIXTURE.read_text(encoding="utf-8")
    expected, _ = derive_screens(text)
    edited = text.replace("gap DOWN > 3%", "gap lower by more than 3%; annotation only")
    edited = edited.replace(
        "sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_d3&ft=4",
        "sh_avgvol_o2000%2Csh_curvol_o100%2Csh_price_o1%2Cta_averagetruerange_o0.5%2Cta_gap_d3&ft=4",
    )
    actual, evidence = derive_screens(edited)
    assert actual == expected
    assert "annotation only" in evidence[1]["filters"]


@pytest.mark.parametrize(
    ("old", "new", "expected"),
    [
        ("ta_gap_u3&ft=4", "ta_gap_d3&ft=4", "f mismatch between Export and Pasted"),
        ("ta_gap_u3&c=<same columns>", "ta_gap_u3&o=-relativevolume&c=<same columns>", "sort mismatch"),
        (
            "&c=<same columns>`",
            "&f=" + "sh_price_o1&c=<same columns>`",
            "ambiguous f",
        ),
        (
            "- **Intent:** premarket / open gap-up scan",
            "- **Active:** `99:99` to `20:00`\n- **Intent:** premarket / open gap-up scan",
            "must be quoted HH:MM",
        ),
    ],
)
def test_additional_real_shape_refusals(old, new, expected):
    with pytest.raises(ProposalRefused, match=expected):
        derive_screens(REAL_SHAPE_FIXTURE.read_text().replace(old, new, 1))


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


@pytest.mark.parametrize(
    "body", ["<html>login</html>", "Symbol\nAAA\n", "Ticker,Volume\nAAA,1,extra\n"]
)
def test_ft_compare_refuses_non_csv_or_malformed_csv(tmp_path, monkeypatch, body):
    _target, pool_path, artifacts = _proposal_env(tmp_path, monkeypatch)

    async def invalid_get(_path, _params, _token, *, on_metrics):
        on_metrics(SimpleNamespace(redirect_statuses=()))
        return SimpleNamespace(text=body)

    monkeypatch.setattr(propose_module, "finviz_get", invalid_get)
    with pytest.raises(ProposalRefused, match="Ticker header|malformed CSV"):
        propose_module.screens_propose(
            argparse.Namespace(pool_block=str(pool_path), ft_compare=True)
        )
    assert artifacts == []


def _real_validation_env(tmp_path, monkeypatch):
    cfg = propose_module.load_config()
    vault = tmp_path / "vault"
    screens = vault / cfg.notes.screens
    screens.parent.mkdir(parents=True)
    screens.write_bytes(REAL_SHAPE_FIXTURE.read_bytes())
    pool = tmp_path / "pool.yaml"
    pool.write_text(yaml.safe_dump(REAL_POOL, sort_keys=False))
    watchlists = _fixed_watchlists_fixture(tmp_path)
    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: vault)
    return screens, pool, watchlists


def test_screens_validate_is_offline_side_effect_free_and_hashes_current_bytes(
    tmp_path, monkeypatch, capsys
):
    screens, pool, watchlists = _real_validation_env(tmp_path, monkeypatch)
    before = screens.read_bytes()

    async def forbidden_http(*_args, **_kwargs):
        raise AssertionError("validator made an HTTP call")

    monkeypatch.setattr(propose_module, "finviz_get", forbidden_http)
    monkeypatch.setattr(
        propose_module,
        "write_artifact",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("validator wrote an artifact")
        ),
    )
    propose_module.screens_validate(
        argparse.Namespace(pool_block=str(pool), watchlists_yaml=str(watchlists))
    )
    output = capsys.readouterr().out
    assert hashlib.sha256(before).hexdigest() in output
    assert "up_gappers: " in output and "day_scan: 10:00-" in output
    # 2026-09-12 amendment: 90s -> 100s; budget now covers total transport
    # demand (pool 30.00 + 4 screens 2.40 + 7 list chunks 4.20 = 36.60), not
    # the pool alone.
    assert "transport budget: 36.60/40 rpm" in output
    assert "pool=30.00" in output
    assert "archive targets: 975" in output
    assert screens.read_bytes() == before


def test_screens_validate_detects_installed_prose_drift(tmp_path, monkeypatch):
    screens_path, pool_path, watchlists = _real_validation_env(tmp_path, monkeypatch)
    text = screens_path.read_text()
    blocks, evidence = derive_screens(text)
    bodies = [
        propose_module._render_screen(block, evidence[index])
        for index, block in enumerate(blocks)
    ]
    bodies.append("```yaml\n" + yaml.safe_dump(REAL_POOL, sort_keys=False).strip() + "\n```")
    screens_path.write_text(text + "\n\n" + "\n\n".join(bodies) + "\n")
    screens_path.write_text(
        screens_path.read_text().replace(
            "f: sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_u3",
            "f: sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_d3",
            1,
        )
    )
    with pytest.raises(ProposalRefused, match="installed/prose f drift"):
        propose_module.screens_validate(
            argparse.Namespace(pool_block=str(pool_path), watchlists_yaml=str(watchlists))
        )


def test_screens_validate_refuses_bad_pool_before_http_or_artifact(
    tmp_path, monkeypatch
):
    _screens, pool, watchlists = _real_validation_env(tmp_path, monkeypatch)
    pool.write_text(yaml.safe_dump(dict(REAL_POOL, cap=61), sort_keys=False))
    calls = []
    monkeypatch.setattr(propose_module, "finviz_get", lambda *_a, **_k: calls.append("http"))
    monkeypatch.setattr(propose_module, "write_artifact", lambda *_a, **_k: calls.append("write"))
    with pytest.raises(ProposalRefused, match="pool budget exceeded"):
        propose_module.screens_validate(
            argparse.Namespace(pool_block=str(pool), watchlists_yaml=str(watchlists))
        )
    assert calls == []


def test_real_shape_proposal_preserves_every_original_byte(tmp_path, monkeypatch):
    screens, pool, _watchlists = _real_validation_env(tmp_path, monkeypatch)
    artifacts = []
    monkeypatch.setattr(
        propose_module,
        "write_artifact",
        lambda artifact: (artifacts.append(deepcopy(artifact)) or (tmp_path / "artifact", "a" * 64)),
    )
    before = screens.read_bytes()
    propose_module.screens_propose(
        argparse.Namespace(pool_block=str(pool), ft_compare=False)
    )
    assert screens.read_bytes() == before
    assert artifacts[0]["inputs"]["target_text"].encode() == before


def test_real_shape_proposal_refuses_unknown_override_before_http_or_artifact(
    tmp_path, monkeypatch
):
    _screens, pool, _watchlists = _real_validation_env(tmp_path, monkeypatch)
    invalid = deepcopy(REAL_POOL)
    invalid["overrides"]["unknown_screen"] = {"rank_metric": "volume"}
    pool.write_text(yaml.safe_dump(invalid, sort_keys=False))
    calls = []
    monkeypatch.setattr(propose_module, "resolve_token", lambda: calls.append("http"))
    monkeypatch.setattr(propose_module, "write_artifact", lambda *_a, **_k: calls.append("write"))
    with pytest.raises(ProposalRefused, match="unknown screen"):
        propose_module.screens_propose(
            argparse.Namespace(pool_block=str(pool), ft_compare=True)
        )
    assert calls == []


def test_ft_compare_accepts_valid_header_only_csv(tmp_path, monkeypatch):
    _target, pool_path, artifacts = _proposal_env(tmp_path, monkeypatch, ft_sets=([], []))
    propose_module.screens_propose(
        argparse.Namespace(pool_block=str(pool_path), ft_compare=True)
    )
    assert artifacts[0]["inputs"]["ft_comparisons"] == [
        {"without": 0, "with_4": 0, "symmetric_difference": []}
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
    source = _fixed_watchlists_fixture(tmp_path)
    artifacts = []
    real_write = propose_module.write_artifact

    def capture(artifact):
        artifacts.append(deepcopy(artifact))
        return real_write(artifact, directory=tmp_path / "artifacts")

    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: tmp_path)
    monkeypatch.setattr(propose_module, "write_artifact", capture)
    propose_module.lists_propose(argparse.Namespace(watchlists_yaml=str(source)))
    assert len(artifacts) == 1
    assert artifacts[0]["target_note"] == str(tmp_path / cfg.notes.lists)
    assert artifacts[0]["inputs"]["watchlists_yaml"].encode() == source.read_bytes()
    assert re.fullmatch(r"[0-9a-f]{40}", artifacts[0]["inputs"]["watchlists_git_blob"])
    assert artifacts[0]["inputs"]["watchlists_git_blob"] == FIXED_WATCHLISTS_BLOB
    assert len(artifacts[0]["units"]) == 1
    unit = artifacts[0]["units"][0]
    assert unit["section"] is None
    assert unit["unit_id"] is None
    assert unit["placement"] == "create_if_absent"


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


class MemoryWriteStore:
    """DB-free audit seam for exercising the real VaultWriter merge path."""

    def __init__(self):
        self.rows = []

    def purge_expired(self):
        return 0

    def last_after(self, note, section, unit):
        for row in reversed(self.rows):
            if (row["note"], row["section"], row["unit"]) == (note, section, unit):
                return row["unit_after"]
        return None

    def recent_afters(self, note, section, unit, limit=10):
        matches = [
            (index, row["unit_after"])
            for index, row in reversed(list(enumerate(self.rows, start=1)))
            if (row["note"], row["section"], row["unit"]) == (note, section, unit)
        ]
        return matches[:limit]

    @contextmanager
    def pending_write(self, **row):
        self.rows.append(row)
        try:
            yield len(self.rows)
        except BaseException:
            self.rows.pop()
            raise


class OpenSessionClock:
    def session(self, _now):
        return Session.RTH


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


def test_real_screen_reapply_targets_existing_sections_without_duplicates(
    tmp_path, monkeypatch
):
    target, pool, _watchlists = _real_validation_env(tmp_path, monkeypatch)
    artifacts = []
    monkeypatch.setattr(
        propose_module,
        "write_artifact",
        lambda artifact: (
            artifacts.append(deepcopy(artifact)) or (tmp_path / "artifact", "a" * 64)
        ),
    )
    propose_module.screens_propose(
        argparse.Namespace(pool_block=str(pool), ft_compare=False)
    )

    monkeypatch.setattr(VaultWriter, "_annotate_sync", lambda _self, _result: None)
    writer = VaultWriter(
        "test.radar.reapply",
        store=MemoryWriteStore(),
        clock=OpenSessionClock(),
        now=lambda: datetime(2026, 9, 10, 14, 0, tzinfo=UTC),
    )
    units = artifacts[0]["units"]
    first = [
        writer.upsert_unit(
            target, unit["section"], unit["unit_id"], unit["body"], placement=AT_END
        )
        for unit in units
    ]
    second = [
        writer.upsert_unit(
            target, unit["section"], unit["unit_id"], unit["body"], placement=AT_END
        )
        for unit in units
    ]

    assert all(result.action == "updated" for result in first)
    assert all(result.action == "unchanged" for result in second)
    content = target.read_text(encoding="utf-8")
    for section_id in (
        "radar-screen-1",
        "radar-screen-2",
        "radar-screen-3",
        "radar-screen-4",
    ):
        assert content.count(f"<!-- cobalt:section {section_id} -->") == 1
        assert content.count(f"<!-- /cobalt:section {section_id} -->") == 1


def test_lists_apply_uses_create_if_absent_and_no_section_marker_id(
    tmp_path, monkeypatch
):
    source = _fixed_watchlists_fixture(tmp_path)
    artifacts = []
    real_write = propose_module.write_artifact

    def capture(artifact):
        artifacts.append(deepcopy(artifact))
        return real_write(artifact, directory=tmp_path / "artifacts")

    monkeypatch.setattr("cobalt.vault.resolve_vault_path", lambda: tmp_path)
    monkeypatch.setattr(propose_module, "write_artifact", capture)
    propose_module.lists_propose(argparse.Namespace(watchlists_yaml=str(source)))
    proposal = next((tmp_path / "artifacts").glob("lists-*.json"))

    calls = []
    RecordingWriter.calls = calls
    RecordingWriteStore.calls = calls
    monkeypatch.setattr(propose_module, "VaultWriter", RecordingWriter)
    monkeypatch.setattr(propose_module, "VaultWriteStore", RecordingWriteStore)
    apply(
        argparse.Namespace(
            proposal=str(proposal),
            sha256=artifact_sha256(artifacts[0]),
            hitl="synthetic-token",
            proposal_kind="lists",
        )
    )

    assert len([call for call in calls if call[0] == "create_if_absent"]) == 1
    assert [call for call in calls if call[0] == "upsert_unit"] == []
