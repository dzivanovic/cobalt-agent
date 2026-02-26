"""
Filesystem Tools
Standard file operations for the Cobalt Agent.
Provides safe read, write, and directory listing capabilities.
"""
import json
import os
from typing import Dict, List, Any
from pydantic import BaseModel, Field
from loguru import logger

from cobalt_agent.core.proposals import create_and_send_proposal, ProposalEngine


class FileContent(BaseModel):
    """Structured content from a file read operation."""
    path: str = Field(description="The file path that was read.")
    content: str = Field(description="The file contents.")
    error: str = Field("", description="Error message if read failed.")

    def __str__(self):
        if self.error:
            return f"[Error reading {self.path}]: {self.error}"
        return f"File: {self.path}\nContent:\n{self.content[:4000]}..." if len(self.content) > 4000 else f"File: {self.path}\nContent:\n{self.content}"


class WriteResult(BaseModel):
    """Result of a file write operation."""
    path: str = Field(description="The file path that was written.")
    success: bool = Field(description="Whether the write succeeded.")
    error: str = Field("", description="Error message if write failed.")

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


class ReadFileTool:
    """Read the contents of a file."""
    name = "read_file"
    description = "Read the contents of a file. Use when you need to examine existing code or data. Pass the file path as the query parameter."

    def __init__(self):
        pass

    def run(self, query=None, **kwargs) -> FileContent:
        """
        Read a file and return its contents.
        """
        import json
        import ast
        
        # Universal extraction
        data = query if query is not None else kwargs
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                try:
                    data = ast.literal_eval(data)
                except Exception:
                    # Fallback: treat the string itself as the path
                    pass

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
            
        except Exception as e:
            logger.error(f"Failed to read file {path}: {e}")
            return FileContent(path=path, content="", error=str(e))


class WriteFileTool:
    """Modifies or creates a file."""
    name = "write_file"
    
    def run(self, query=None, **kwargs) -> str:
        import json
        import ast
        from loguru import logger
        from cobalt_agent.core.proposals import create_and_send_proposal, ProposalEngine
        
        filepath = None
        content = None
        
        # Universal extraction
        data = query if query is not None else kwargs
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e1:
                try:
                    data = ast.literal_eval(data)
                except Exception as e2:
                    logger.error(f"WriteFileTool parsing failed. JSON error: {e1} | AST error: {e2} | Data: {data}")
                    return f"Error: Failed to parse arguments. Received: {data}"
        
        if isinstance(data, dict):
            # Handle nested query dictionaries
            if "filepath" not in data and "query" in data:
                if isinstance(data["query"], dict):
                    data = data["query"]
                elif isinstance(data["query"], str):
                    try:
                        data = ast.literal_eval(data["query"])
                    except Exception:
                        pass

            filepath = data.get("filepath")
            content = data.get("content")

        if not filepath or content is None:
            logger.error(f"WriteFileTool missing fields. Parsed data: {data}")
            return f"Error: Missing filepath or content. Parsed data: {data}"

        from pathlib import Path
        from cobalt_agent.config import get_config

        # Resolve the path properly
        target_path = Path(filepath)

        # If it's just a raw markdown filename with no directories, force it to 0 - Inbox
        if len(target_path.parts) == 1 and target_path.suffix == '.md':
            target_path = Path(f"0 - Inbox/{target_path.name}")

        # If it's an Obsidian note (like '0 - Inbox/Note.md') and doesn't start with docs/
        # we should route it to the configured vault path
        if str(target_path).startswith("0 - ") and not str(target_path).startswith("docs/"):
            config = get_config()
            vault_path = Path(config.system.obsidian_vault_path)
            target_path = vault_path / target_path

        def execute_write(proposal_obj):
            try:
                # Ensure the parent directory exists before writing
                target_path.parent.mkdir(parents=True, exist_ok=True)

                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                logger.info(f"Proposal Engine executed write to: {target_path} ({len(content)} bytes)")
            except Exception as e:
                logger.error(f"Failed to physically write file {target_path}: {e}")
            
        try:
            proposal = create_and_send_proposal(
                action=f"Write {len(content)} bytes to {filepath}",
                justification="Agent requested file modification via WriteFileTool.",
                risk_assessment="HIGH"
            )
        except Exception as e:
            logger.error(f"Proposal Engine crash: {e}")
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
        """
        import json
        import ast
        
        # Universal extraction
        data = query if query is not None else kwargs
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                try:
                    data = ast.literal_eval(data)
                except Exception:
                    # Fallback: treat the string itself as the path
                    pass

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
            
        except Exception as e:
            logger.error(f"Failed to list directory {path}: {e}")
            return DirectoryListing(path=path, contents=[], error=str(e))
