"""F20 C2e — the commit path for executed agent files (FINAL §2 generated row, F-07; C2).

A `tmp_path` git repository; the executed-row lookup is faked. An untracked
or modified file under a `hitl_dirs` directory is committed only when its
bytes hash to an `executed` row's sha256; anything else there fails the
job loud and commits nothing. `files:` keeps both of its raises. No push.
"""

from __future__ import annotations

import subprocess

import pytest

from hitl_support import AGENT_YAML, sha

LISTED = "docs/report.md"
GENERATED_YAML = f"""files:
  - path: "{LISTED}"
    written_by: "a constructed job"
hitl_dirs: [configs/cobalt/agents]
message: "chore(generated): nightly rewrite {{date}}"
"""


def _git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True).stdout


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    (root / "configs" / "cobalt" / "agents").mkdir(parents=True)
    (root / "docs").mkdir()
    (root / "configs" / "cobalt" / "generated.yaml").write_text(GENERATED_YAML)
    (root / "configs" / "cobalt" / "agents" / "voice.yaml").write_text("agent:\n  id: voice\n")
    (root / LISTED).write_text("v1\n")
    subprocess.run(["git", "init", "-q", "-b", "main", str(root)], check=True)
    _git(root, "config", "user.email", "constructed@example.invalid")
    _git(root, "config", "user.name", "constructed")
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "-m", "seed")
    return root


def _commit(repo, executed):
    from cobalt.generated.committer import commit_generated
    from cobalt.generated.config import load_generated_config

    cfg = load_generated_config(repo_root=repo)
    return commit_generated(repo, day="2026-09-03", config=cfg, executed_sha=lambda s: s in executed)


def test_an_executed_agent_file_is_committed(repo):
    data = AGENT_YAML.encode()
    (repo / "configs" / "cobalt" / "agents" / "scout.yaml").write_bytes(data)
    (repo / LISTED).write_text("v2\n")
    out = _commit(repo, {sha(data)})
    assert out.committed
    assert out.paths == sorted([LISTED, "configs/cobalt/agents/scout.yaml"])
    assert _git(repo, "status", "--porcelain") == ""


def test_an_unbacked_file_fails_loud_and_commits_nothing(repo):
    from cobalt.generated.committer import GeneratedCommitRefused

    head = _git(repo, "rev-parse", "HEAD")
    (repo / "configs" / "cobalt" / "agents" / "scout.yaml").write_bytes(AGENT_YAML.encode())
    (repo / LISTED).write_text("v2\n")
    with pytest.raises(GeneratedCommitRefused, match="scout.yaml"):
        _commit(repo, executed=set())
    assert _git(repo, "rev-parse", "HEAD") == head
    assert _git(repo, "diff", "--cached", "--name-only") == "", "nothing staged"


def test_a_modified_voice_yaml_fails_loud(repo):
    from cobalt.generated.committer import GeneratedCommitRefused

    voice = repo / "configs" / "cobalt" / "agents" / "voice.yaml"
    voice.write_text("agent:\n  id: voice\n  charter: changed\n")
    head = _git(repo, "rev-parse", "HEAD")
    with pytest.raises(GeneratedCommitRefused, match="voice.yaml"):
        _commit(repo, executed=set())
    assert _git(repo, "rev-parse", "HEAD") == head


def test_listed_files_still_raise_when_missing_or_untracked(repo):
    from cobalt.generated.config import GeneratedConfigError, load_generated_config

    cfg = load_generated_config(repo_root=repo)
    assert cfg.hitl_dirs == ["configs/cobalt/agents"]
    (repo / LISTED).unlink()
    with pytest.raises(GeneratedConfigError, match="do not exist"):
        load_generated_config(repo_root=repo)
    _git(repo, "rm", "-q", "--cached", LISTED)
    (repo / LISTED).write_text("v1\n")
    with pytest.raises(GeneratedConfigError, match="NOT TRACKED"):
        load_generated_config(repo_root=repo)


# check (CHECK-HUB ## 4) — finding run as written


def test_check_o7_executed_bytes_under_another_name_fail_loud(repo):
    from cobalt.generated.committer import GeneratedCommitRefused

    data = AGENT_YAML.encode()
    head = _git(repo, "rev-parse", "HEAD")
    (repo / "configs" / "cobalt" / "agents" / "scout.yaml").write_bytes(data)
    (repo / "configs" / "cobalt" / "agents" / "rogue.yaml").write_bytes(data)
    with pytest.raises(GeneratedCommitRefused, match="rogue.yaml"):
        _commit(repo, {sha(data)})
    assert _git(repo, "rev-parse", "HEAD") == head
