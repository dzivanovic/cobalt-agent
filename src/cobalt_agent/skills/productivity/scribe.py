"""
The Scribe Skill (Obsidian Integration)
Allows Cobalt to read, write, and search your "Second Brain".
Refactored to use Environment Variables for portability.
STRICT RULE: All automated writes go to '0 - Inbox'.

SECURITY: All write operations MUST route through ToolManager to trigger
HITL approval via the Proposal Engine. Direct filesystem access is forbidden.
"""

import os
from pathlib import Path
from datetime import datetime
from typing import List, Optional
from loguru import logger

from cobalt_agent.tools.tool_manager import ToolManager

class Scribe:
    """
    Interface for interacting with an Obsidian Vault.
    
    SECURITY NOTE: All write operations must route through ToolManager.execute_tool()
    to ensure HITL approval is triggered via the Proposal Engine. Direct filesystem
    access using open() is strictly forbidden for write operations.
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

    def _resolve_path(self, filename: str, folder: Optional[str] = None) -> str:
        """
        Helper to build a path relative to the vault.
        
        Args:
            filename: The filename (will have .md appended if missing)
            folder: Optional folder name. If provided, folder is NOT prepended twice.
                   If None, defaults to "0 - Inbox".
        
        Returns:
            A relative path string like "0 - Inbox/myfile.md" that ToolManager will
            resolve to vault_root/0 - Inbox/myfile.md
        """
        if not filename.endswith(".md"):
            filename += ".md"
        
        # Use folder if provided, otherwise default to "0 - Inbox"
        target_folder = folder if folder else "0 - Inbox"
        
        # Return relative path - ToolManager will handle joining with vault root
        return f"{target_folder}/{filename}"

    def write_note(self, filename: str, content: str, folder: str = "0 - Inbox"):
        """
        Create or Overwrite a note.
        Defaults strictly to '0 - Inbox' unless overridden.
        
        SECURITY: Routes through ToolManager to trigger HITL approval via Proposal Engine.
        Direct filesystem access is forbidden.
        
        Args:
            filename: The note filename (may include path like "0 - Inbox/filename.md")
            content: The content to write
            folder: The folder relative to vault root (e.g., "0 - Inbox")
            
        Returns:
            A message indicating the action is paused for approval with the proposal ID,
            OR a dict with status=="requires_approval" to be handled by the caller.
        """
        try:
            # Build relative path (folder/filename.md)
            # ToolManager will resolve this relative to the vault root
            
            # FIX: If filename already starts with folder prefix, don't prepend it again
            # Check if the filename already contains the folder path (like "0 - Inbox/filename.md")
            prefix = f"{folder}/"
            if filename.startswith(prefix):
                # Filename already includes the folder prefix, extract just the filename part
                # to avoid double prefix (e.g., "0 - Inbox/0 - Inbox/file.md")
                relative_path = filename if filename.endswith(".md") else f"{filename}.md"
            else:
                # Prepend folder prefix to filename
                relative_path = f"{folder}/{filename}.md" if not filename.endswith(".md") else f"{folder}/{filename}"
            
            # Use ToolManager to execute write_file - this triggers HITL approval
            tool_manager = ToolManager()
            args = {"filepath": relative_path, "content": content}
            
            result = tool_manager.execute_tool("write_file", args)
            
            # Return the raw dict to caller for centralized proposal handling
            if isinstance(result, dict) and result.get("status") == "requires_approval":
                return result
            
            return result
            
        except Exception as e:
            logger.exception(f"Failed to execute write_note for {relative_path}: {e}")
            return f"❌ Error executing write_note: {e}"

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

    def append_to_daily_note(self, content: str):
        """
        Appends text to today's Daily Log in '0 - Inbox'.
        
        SECURITY: Routes through ToolManager to trigger HITL approval via Proposal Engine.
        Direct filesystem access is forbidden.
        
        Args:
            content: The content to append to the daily log
            
        Returns:
            A message indicating the action is paused for approval with the proposal ID,
            OR a dict with status=="requires_approval" to be handled by the caller.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        
        # STRICT REQUIREMENT: Inbox only
        daily_folder = "0 - Inbox"
        
        try:
            timestamp = datetime.now().strftime('%H:%M')
            header = f"\n\n### {timestamp} - Cobalt Log\n"
            full_entry = header + content
            
            # File format: Daily_Log_2026-02-10.md
            relative_path = f"{daily_folder}/Daily_Log_{today}.md"
            
            # Use ToolManager to execute append_to_file - this triggers HITL approval
            tool_manager = ToolManager()
            args = {"filepath": relative_path, "content": full_entry}
            
            result = tool_manager.execute_tool("append_to_file", args)
            
            # Return the raw dict to caller for centralized proposal handling
            if isinstance(result, dict) and result.get("status") == "requires_approval":
                return result
            
            return result
            
        except Exception as e:
            logger.exception(f"Failed to execute append_to_daily_note for {relative_path}: {e}")
            return f"❌ Error executing append_to_daily_note: {e}"

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