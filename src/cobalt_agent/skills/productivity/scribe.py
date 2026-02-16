"""
The Scribe Skill (Obsidian Integration)
Allows Cobalt to read, write, and search your "Second Brain".
Refactored to use Environment Variables for portability.
STRICT RULE: All automated writes go to '0 - Inbox'.
"""

import os
from pathlib import Path
from datetime import datetime
from typing import List, Optional
from loguru import logger

class Scribe:
    """
    Interface for interacting with an Obsidian Vault.
    """
    
    def __init__(self, vault_path: Optional[str] = None):
        """
        Initialize the Scribe.
        :param vault_path: Path to Obsidian vault. Defaults to env var OBSIDIAN_VAULT_PATH.
        """
        # 1. Try argument first, then environment variable
        path_str = vault_path or os.getenv("OBSIDIAN_VAULT_PATH")
        
        if not path_str:
             # Fallback for safety, but log a warning
            logger.warning("⚠️ OBSIDIAN_VAULT_PATH not set in .env. Defaulting to home/Documents/Think")
            path_str = str(Path.home() / "Documents" / "Think")

        self.vault_path = Path(path_str)

        if not self.vault_path.exists():
            logger.warning(f"⚠️ Obsidian Vault not found at {self.vault_path}. Scribe functions will fail.")

    def _resolve_path(self, filename: str) -> Path:
        """Helper to ensure file has .md extension and is inside the vault."""
        if not filename.endswith(".md"):
            filename += ".md"
        return self.vault_path / filename

    def write_note(self, filename: str, content: str, folder: str = "0 - Inbox") -> str:
        """
        Create or Overwrite a note.
        Defaults strictly to '0 - Inbox' unless overridden.
        """
        try:
            # Construct path (Vault / Folder / Filename)
            target_dir = self.vault_path / folder
            target_dir.mkdir(parents=True, exist_ok=True)
            
            clean_name = filename if filename.endswith(".md") else f"{filename}.md"
            file_path = target_dir / clean_name
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            return f"✅ Note saved: {folder}/{clean_name}"
        except Exception as e:
            logger.error(f"Failed to write note: {e}")
            return f"❌ Error writing note: {e}"

    def read_note(self, filename: str) -> str:
        """Read the content of a specific note."""
        try:
            # Try searching recursively if file not found in root
            found = list(self.vault_path.rglob(f"{filename if filename.endswith('.md') else filename + '.md'}"))
            
            if found:
                # Prioritize exact match if multiple found, otherwise take first
                file_path = found[0]
            else:
                 # Last ditch effort: check direct path
                file_path = self.vault_path / filename
                if not file_path.exists():
                    return f"❌ Note not found: {filename}"

            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"❌ Error reading note: {e}"

    def append_to_daily_note(self, content: str) -> str:
        """
        Appends text to today's Daily Log in '0 - Inbox'.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        
        # STRICT REQUIREMENT: Inbox only
        daily_folder = "0 - Inbox"
        
        try:
            timestamp = datetime.now().strftime('%H:%M')
            header = f"\n\n### {timestamp} - Cobalt Log\n"
            full_entry = header + content
            
            target_dir = self.vault_path / daily_folder
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # File format: Daily_Log_2026-02-10.md
            file_path = target_dir / f"Daily_Log_{today}.md"

            # Check if file exists to add title if new
            is_new = not file_path.exists()
            mode = "a" if not is_new else "w"

            with open(file_path, mode, encoding="utf-8") as f:
                if is_new:
                    f.write(f"# Daily Log: {today}\n")
                f.write(full_entry)
            
            return f"✅ Logged to {daily_folder}/Daily_Log_{today}.md"
        except Exception as e:
            return f"❌ Failed to log to daily note: {e}"

    def search_vault(self, query: str, limit: int = 5) -> List[str]:
        """
        Semantic search (lite). Walks the vault and finds notes containing the keyword.
        """
        matches = []
        try:
            # Walk through all .md files
            for file_path in self.vault_path.rglob("*.md"):
                # Ignore system folders
                if any(part.startswith(".") for part in file_path.parts):
                    continue
                
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        if query.lower() in content.lower():
                            matches.append(file_path.name)
                            if len(matches) >= limit:
                                break
                except:
                    continue
            
            return matches if matches else ["No matching notes found."]
        except Exception as e:
            return [f"Error searching vault: {e}"]