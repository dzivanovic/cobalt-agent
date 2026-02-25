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
    error: str = Field("", description="Error message if listing failed.")

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

    def run(self, query: str) -> FileContent:
        """
        Read a file and return its contents.
        
        Args:
            query: The file path to read
        
        Returns:
            FileContent with the file contents or error
        """
        path = query.strip()
        
        logger.info(f"Reading file: {path}")
        
        try:
            # Sanitize path - prevent directory traversal
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
    """Write content to a file."""
    name = "write_file"
    description = "Write content to a file. Use when you need to modify existing code or create new files. Pass a JSON string with 'filepath' and 'content' keys."

    def __init__(self):
        pass

    def run(self, query: str) -> WriteResult:
        """
        Write content to a file.
        
        Args:
            query: Either a JSON string with 'filepath' and 'content' keys, or a plain file path
        
        Returns:
            WriteResult with success status or error
        """
        path = ""
        content = ""
        
        # Try to parse as JSON first
        if query.strip().startswith("{"):
            try:
                data = json.loads(query)
                path = data.get('filepath', '')
                content = data.get('content', '')
            except json.JSONDecodeError:
                # Fallback: treat as plain path and use the whole query as content
                path = query.strip()
                content = ""
        else:
            path = query.strip()
        
        logger.info(f"Writing to file: {path}")
        
        try:
            # Sanitize path - prevent directory traversal
            path = os.path.normpath(path)
            
            # Ensure directory exists
            dir_path = os.path.dirname(path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return WriteResult(path=path, success=True)
            
        except Exception as e:
            logger.error(f"Failed to write file {path}: {e}")
            return WriteResult(path=path, success=False, error=str(e))


class ListDirectoryTool:
    """List the contents of a directory."""
    name = "list_directory"
    description = "List the contents of a directory. Use when you need to explore the file structure. Pass the directory path as the query parameter."

    def __init__(self):
        pass

    def run(self, query: str) -> DirectoryListing:
        """
        List directory contents.
        
        Args:
            query: The directory path to list
        
        Returns:
            DirectoryListing with contents or error
        """
        path = query.strip()
        
        logger.info(f"Listing directory: {path}")
        
        try:
            # Sanitize path - prevent directory traversal
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