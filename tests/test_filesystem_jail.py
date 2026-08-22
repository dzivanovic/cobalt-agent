"""
Filesystem path-jail tests (assessment finding 06-H1).

Proves BaseFileTool._validate_path rejects paths that resolve outside the
configured Obsidian vault root: '../' escapes and absolute paths outside
the root — and still accepts vault-relative paths.
"""
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from cobalt_agent.tools.filesystem import BaseFileTool, SecurityError, WriteFileTool


@pytest.fixture
def vault_root(tmp_path):
    root = tmp_path / "vault"
    root.mkdir()
    return root


@pytest.fixture
def jailed_tool(vault_root):
    cfg = MagicMock()
    cfg.system.obsidian_vault_path = str(vault_root)
    with patch("cobalt_agent.tools.filesystem.get_config", return_value=cfg):
        yield BaseFileTool()


def test_relative_path_inside_vault_is_accepted(jailed_tool, vault_root):
    resolved = jailed_tool._validate_path("0 - Inbox/note.md")
    assert resolved == (vault_root / "0 - Inbox" / "note.md").resolve()
    assert resolved.is_relative_to(vault_root.resolve())


@pytest.mark.parametrize(
    "escape",
    [
        "../outside.md",
        "../../etc/hosts",
        "0 - Inbox/../../outside.md",
    ],
)
def test_dotdot_escape_is_rejected(jailed_tool, escape):
    with pytest.raises(SecurityError):
        jailed_tool._validate_path(escape)


def test_absolute_path_outside_vault_is_rejected(jailed_tool, tmp_path):
    outside = tmp_path / "outside.md"  # sibling of the vault root, not inside it
    with pytest.raises(SecurityError):
        jailed_tool._validate_path(str(outside))
    with pytest.raises(SecurityError):
        jailed_tool._validate_path("/etc/hosts")


def test_absolute_path_inside_vault_is_accepted(jailed_tool, vault_root):
    inside = vault_root / "sub" / "note.md"
    assert jailed_tool._validate_path(str(inside)) == inside.resolve()


def test_write_tool_refuses_to_write_outside_vault(vault_root, tmp_path):
    cfg = MagicMock()
    cfg.system.obsidian_vault_path = str(vault_root)
    target = tmp_path / "escaped.md"
    with patch("cobalt_agent.tools.filesystem.get_config", return_value=cfg):
        tool = WriteFileTool()
        result = tool.run(filepath=str(target), content="should not land here")
    assert "Access denied" in result
    assert not target.exists()
    # and the vault root itself stays untouched
    assert list(vault_root.iterdir()) == []
