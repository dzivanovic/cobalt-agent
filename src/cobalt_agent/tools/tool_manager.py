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

    def execute_tool(self, tool_name: str, args: Dict[str, Any]) -> ToolResult:
        """
        Execute a registered tool by name.
        
        Args:
            tool_name: The name of the tool (e.g., 'search')
            args: Dictionary of arguments for the tool (e.g., {'query': '...'})
        """
        if tool_name not in self.tools:
            return ToolResult(success=False, output=None, error=f"Tool '{tool_name}' not found.")
            
        tool = self.tools[tool_name]
        
        try:
            logger.info(f"Executing tool: {tool_name} with args: {args}")
            
            # This logic assumes all tools have a .run() method
            # We might need to adapt this if tools have different signatures
            if hasattr(tool, 'run'):
                # Extract the main argument (most tools just take a query string for now)
                # This is a simplification; later we will make this robust.
                query = args.get('query') or args.get('q') or list(args.values())[0]
                
                result = tool.run(query)
                return ToolResult(success=True, output=result)
            else:
                return ToolResult(success=False, output=None, error=f"Tool '{tool_name}' has no run() method.")

        except Exception as e:
            logger.error(f"Tool Execution Failed: {e}")
            return ToolResult(success=False, output=None, error=str(e))