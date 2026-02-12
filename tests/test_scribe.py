"""
Scribe Skill Tests
Verifies that notes are written to the correct location using environment variables.
"""
import os
import pytest
from cobalt_agent.skills.productivity.scribe import Scribe

def test_scribe_initialization(tmp_path):
    """Test if Scribe accepts a direct path."""
    scribe = Scribe(vault_path=str(tmp_path))
    assert scribe.vault_path == tmp_path

def test_scribe_env_var_fallback(monkeypatch, tmp_path):
    """
    Test if Scribe falls back to the Environment Variable if no path is given.
    """
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(tmp_path))
    scribe = Scribe()
    assert scribe.vault_path == tmp_path

def test_write_note(tmp_path):
    """Test actually writing a file to a fake vault."""
    scribe = Scribe(vault_path=str(tmp_path))
    
    filename = "test_note"
    content = "# Hello World"
    folder = "0 - Inbox"
    
    result = scribe.write_note(filename, content, folder)
    
    expected_file = tmp_path / folder / "test_note.md"
    assert expected_file.exists()
    assert expected_file.read_text(encoding="utf-8") == content
    assert "✅ Note saved" in result