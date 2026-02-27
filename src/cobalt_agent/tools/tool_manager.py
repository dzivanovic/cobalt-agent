"""
Cobalt Agent - Tool Manager
Registry and execution engine for all agent capabilities.
"""

from typing import Dict, Any, List, Optional, Type
from loguru import logger
from pydantic import BaseModel, ValidationError
import json

# Import your tools
from cobalt_agent.tools.search import SearchTool
# Import Browser
from cobalt_agent.tools.browser import BrowserTool, BrowserCommand
# Import Finance
from cobalt_agent.tools.finance import FinanceTool
# Import Filesystem tools
from cobalt_agent.tools.filesystem import ReadFileTool, WriteFileTool, ListDirectoryTool
from cobalt_agent.tools.filesystem import ReadFileInput, WriteFileInput, ListDirectoryInput
# Import Knowledge Base
from cobalt_agent.tools.knowledge import KnowledgeSearchTool

class ToolResult(BaseModel):
    """Standardized output for any tool execution."""
    success: bool
    output: Any
    error: Optional[str] = None

class ToolManager:
    """
    Manages the registration and execution of tools.
    Allows the LLM to 'see' and 'use' functions.
    """
    
    def __init__(self):
        self.tools: Dict[str, Any] = {}
        self._register_core_tools()
        
    def _register_core_tools(self):
        """Register the default built-in tools."""
        # 1. Search Tool
        search = SearchTool()
        self.register_tool("search", search)

        # 2. Browser Tool (with Pydantic schema)
        browser = BrowserTool()
        self.register_tool("browser", browser, schema=BrowserCommand)
        
        # 3. Finance Tool
        finance = FinanceTool()
        self.register_tool("finance", finance)
        
        # 4. Filesystem Tools (with Pydantic schemas)
        self.register_tool("read_file", ReadFileTool(), schema=ReadFileInput)
        self.register_tool("write_file", WriteFileTool(), schema=WriteFileInput)
        self.register_tool("list_directory", ListDirectoryTool(), schema=ListDirectoryInput)
        
        # 5. Knowledge Base
        self.register_tool("search_knowledge", KnowledgeSearchTool())
        
    def register_tool(self, name: str, tool_instance: Any, schema: Optional[Type[BaseModel]] = None):
        """Add a new tool to the registry."""
        self.tools[name] = tool_instance
        self.tools[name + '_schema'] = schema  # Store schema separately
        logger.info(f"Tool registered: {name}")

    def get_tool_descriptions(self) -> List[Any]:
        """Return the list of tool objects for the Prompt Engine."""
        return list(self.tools.values())

    def execute_tool(self, name: str, args: Any) -> str:
        from loguru import logger
        logger.info(f"Executing tool: {name} with args: {args}")
        
        if name not in self.tools:
            return f"Error: Tool '{name}' not found."
            
        tool = self.tools[name]
        schema_key = name + '_schema'
        
        try:
            # Validate against Pydantic schema if available
            if schema_key in self.tools and self.tools[schema_key]:
                schema = self.tools[schema_key]
                try:
                    # If args is a dict, validate it against the schema
                    if isinstance(args, dict):
                        validated_args = schema(**args)
                        return tool.run(**validated_args.model_dump())
                    elif isinstance(args, str):
                        # Try to parse string as JSON first
                        try:
                            parsed_args = json.loads(args)
                            validated_args = schema(**parsed_args)
                            return tool.run(**validated_args.model_dump())
                        except json.JSONDecodeError:
                            # Return error for invalid JSON
                            return f"Observation: Invalid JSON format. Please use strict double quotes."
                except ValidationError as e:
                    # Return exact error message for LLM to self-correct
                    error_str = str(e)
                    logger.warning(f"Pydantic validation error for tool {name}: {error_str}")
                    return f"Error: {error_str}"
            
            # Fallback for tools without Pydantic schema
            if isinstance(args, dict):
                return tool.run(**args)
            else:
                return tool.run(args)
        except json.JSONDecodeError as e:
            return f"Observation: Invalid JSON format. Please use strict double quotes."
        except TypeError as e:
            # Fallback for legacy tools that strictly only accept a single positional 'query' string
            logger.warning(f"Tool {name} rejected kwargs, falling back to positional: {e}")
            if isinstance(args, dict):
                if "query" in args:
                    return tool.run(args["query"])
                elif len(args) == 1:
                    return tool.run(list(args.values())[0])
                else:
                    return tool.run(str(args))
            return tool.run(str(args))
        except Exception as e:
            logger.error(f"Error executing tool {name}: {str(e)}")
            return f"Error executing tool {name}: {str(e)}"
