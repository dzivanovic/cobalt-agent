"""
Cobalt Agent - Tool Manager
Registry and execution engine for all agent capabilities.
"""

from typing import Dict, Any, List, Optional
from loguru import logger
from pydantic import BaseModel

# Import your tools
from cobalt_agent.tools.search import SearchTool
# Import Browser
from cobalt_agent.tools.browser import BrowserTool
# Import Finance
from cobalt_agent.tools.finance import FinanceTool
# Import Filesystem tools
from cobalt_agent.tools.filesystem import ReadFileTool, WriteFileTool, ListDirectoryTool

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

        # 2. Browser Tool
        browser = BrowserTool()
        self.register_tool("browser", browser)
        
        # 3. Finance Tool
        finance = FinanceTool()
        self.register_tool("finance", finance)
        
        # 4. Filesystem Tools
        self.register_tool("read_file", ReadFileTool())
        self.register_tool("write_file", WriteFileTool())
        self.register_tool("list_directory", ListDirectoryTool())
        
    def register_tool(self, name: str, tool_instance: Any):
        """Add a new tool to the registry."""
        self.tools[name] = tool_instance
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
        
        try:
            if isinstance(args, dict):
                # Safely pass the full dictionary as kwargs
                return tool.run(**args)
            else:
                return tool.run(args)
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
