"""
Filesystem Tools
Standard file operations for the Cobalt Agent.
Provides safe read, write, and directory listing capabilities.
"""
import json
import os
from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field, ValidationError
from loguru import logger
from pathlib import Path

from cobalt_agent.core.proposals import create_and_send_proposal, ProposalEngine
from cobalt_agent.config import get_config


class FileContent(BaseModel):
    """Structured content from a file read operation."""
    path: str = Field(description="The file path that was read.")
    content: str = Field(description="The file contents.")
    error: str = Field(default="", description="Error message if read failed.")

    def __str__(self):
        if self.error:
            return f"[Error reading {self.path}]: {self.error}"
        return f"File: {self.path}\nContent:\n{self.content[:4000]}..." if len(self.content) > 4000 else f"File: {self.path}\nContent:\n{self.content}"


class WriteResult(BaseModel):
    """Result of a file write operation."""
    path: str = Field(description="The file path that was written.")
    success: bool = Field(description="Whether the write succeeded.")
    error: str = Field(default="", description="Error message if write failed.")

    def __str__(self):
        if self.success:
            return f"Successfully wrote to {self.path}"
        return f"[Error writing {self.path}]: {self.error}"


class DirectoryListing(BaseModel):
    """Result of a directory listing operation."""
    path: str = Field(description="The directory path that was listed.")
    contents: List[Dict[str, Any]] = Field(description="List of files and directories.")
    error: str = Field(default="", description="Error message if listing failed.")

    def __str__(self):
        if self.error:
            return f"[Error listing {self.path}]: {self.error}"
        output = f"Directory: {self.path}\nContents:\n"
        for item in self.contents:
            item_type = item.get('type', 'unknown')
            item_name = item.get('name', 'unknown')
            output += f"  - [{item_type}] {item_name}\n"
        return output


class ReadFileInput(BaseModel):
    """Pydantic model for read_file tool input validation."""
    filepath: Optional[str] = Field(default=None, description="The file path to read")
    path: Optional[str] = Field(default=None, description="Alias for filepath")
    query: Optional[str] = Field(default=None, description="Alias for filepath")


class WriteFileInput(BaseModel):
    """Pydantic model for write_file tool input validation."""
    filepath: Optional[str] = Field(default=None, description="The file path to write")
    path: Optional[str] = Field(default=None, description="Alias for filepath")
    content: Optional[str] = Field(default=None, description="The content to write")


class ListDirectoryInput(BaseModel):
    """Pydantic model for list_directory tool input validation."""
    directory_path: Optional[str] = Field(default=None, description="The directory path to list")
    path: Optional[str] = Field(default=None, description="Alias for directory_path")
    query: Optional[str] = Field(default=None, description="Alias for directory_path")


class ReadFileTool:
    """Read the contents of a file."""
    name = "read_file"
    description = "Read the contents of a file. Use when you need to examine existing code or data. Pass the file path as the query parameter."

    def __init__(self):
        pass

    def run(self, query=None, **kwargs) -> FileContent:
        """
        Read a file and return its contents.
        Accepts either a filepath string directly or a JSON object with filepath key.
        """
        # Universal extraction
        data = query if query is not None else kwargs
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                # Return explicit error for invalid JSON so LLM can self-correct
                error_msg = "Observation: Invalid JSON format. Please use strict double quotes."
                return FileContent(path="unknown", content="", error=error_msg)
        
        path = ""
        if isinstance(data, dict):
            # Check common key names
            path = data.get("filepath", data.get("path", data.get("query", "")))
        elif isinstance(data, str):
            path = data.strip()
            
        if not path:
            return FileContent(path="unknown", content="", error=f"Missing filepath. Parsed data: {data}")
            
        logger.info(f"Reading file: {path}")
        
        try:
            path = os.path.normpath(path)
            if not os.path.exists(path):
                return FileContent(path=path, content="", error=f"File not found: {path}")
            if not os.path.isfile(path):
                return FileContent(path=path, content="", error=f"Not a file: {path}")
                
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            return FileContent(path=path, content=content)
            
        except Exception:
            logger.exception(f"Failed to read file {path}")
            return FileContent(path=path, content="", error="Failed to read file")


class WriteFileTool:
    """Modifies or creates a file."""
    name = "write_file"
    
    def run(self, query=None, **kwargs) -> str:
        filepath = None
        content = None
        
        # Universal extraction
        data = query if query is not None else kwargs
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError as e:
                # Return explicit error for invalid JSON so LLM can self-correct
                error_msg = f"Observation: Invalid JSON format. Please use strict double quotes. Error: {e}"
                return error_msg
        
        if isinstance(data, dict):
            # Handle nested query dictionaries
            if "filepath" not in data and "query" in data:
                if isinstance(data["query"], dict):
                    data = data["query"]
                elif isinstance(data["query"], str):
                    try:
                        data = json.loads(data["query"])
                    except json.JSONDecodeError:
                        return "Observation: Invalid JSON format. Please use strict double quotes."

            filepath = data.get("filepath")
            content = data.get("content")

        if not filepath or content is None:
            logger.error(f"WriteFileTool missing fields. Parsed data: {data}")
            return f"Error: Missing filepath or content. Parsed data: {data}"

        # Resolve the path properly
        target_path = Path(filepath)
        
        # Get the base vault path from config
        config = get_config()
        base_path = Path(config.system.obsidian_vault_path)
        
        # CRITICAL: No hardcoded path forcing - accept the path as-is from the LLM
        # The caller must provide the full relative path within the vault
        
        # Path traversal protection: ensure resolved path is within vault
        resolved_target = target_path.resolve()
        resolved_base = base_path.resolve()
        
        if not resolved_target.is_relative_to(resolved_base):
            logger.error(f"Path traversal attempt blocked: {target_path} is outside vault {base_path}")
            raise PermissionError(f"Access denied: Path '{target_path}' is outside the Obsidian vault.")
        
        # Ensure the parent directory exists before writing
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        def execute_write(proposal_obj):
            try:
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                logger.info(f"Proposal Engine executed write to: {target_path} ({len(content)} bytes)")
            except Exception as e:
                logger.exception(f"Failed to physically write file {target_path}: {e}")
        
        try:
            proposal = create_and_send_proposal(
                action=f"Write {len(content)} bytes to {filepath}",
                justification="Agent requested file modification via WriteFileTool.",
                risk_assessment="HIGH"
            )
        except Exception as e:
            logger.exception(f"Proposal Engine crash: {e}")
            return f"Error: Proposal Engine crashed: {e}"
        
        if proposal:
            engine = ProposalEngine()
            engine.set_approval_callback(proposal.task_id, execute_write)
            engine.pending_proposals[proposal.task_id] = proposal
            return f"Action paused. Proposal [{proposal.task_id}] sent to Admin for approval in Mattermost."
        else:
            return "Error: Failed to generate Proposal Ticket. Mattermost connection failed."


class ListDirectoryTool:
    """List the contents of a directory."""
    name = "list_directory"
    description = "List the contents of a directory. Use when you need to explore the file structure. Pass the directory path as the query parameter."

    def __init__(self):
        pass

    def run(self, query=None, **kwargs) -> DirectoryListing:
        """
        List directory contents.
        Accepts either a directory_path string directly or a JSON object with directory_path key.
        """
        # Universal extraction
        data = query if query is not None else kwargs
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                # Return explicit error for invalid JSON so LLM can self-correct
                error_msg = "Observation: Invalid JSON format. Please use strict double quotes."
                return DirectoryListing(path="unknown", contents=[], error=error_msg)
        
        path = ""
        if isinstance(data, dict):
            path = data.get("directory_path", data.get("path", data.get("query", "")))
        elif isinstance(data, str):
            path = data.strip()
            
        if not path:
            return DirectoryListing(path="unknown", contents=[], error=f"Missing directory_path. Parsed data: {data}")
            
        logger.info(f"Listing directory: {path}")
        
        try:
            path = os.path.normpath(path)
            if not os.path.exists(path):
                return DirectoryListing(path=path, contents=[], error=f"Directory not found: {path}")
            if not os.path.isdir(path):
                return DirectoryListing(path=path, contents=[], error=f"Not a directory: {path}")
                
            contents = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                item_type = "dir" if os.path.isdir(item_path) else "file"
                contents.append({
                    'name': item,
                    'type': item_type
                })
            return DirectoryListing(path=path, contents=contents)
            
        except Exception:
            logger.exception(f"Failed to list directory {path}")
            return DirectoryListing(path=path, contents=[], error="Failed to list directory")