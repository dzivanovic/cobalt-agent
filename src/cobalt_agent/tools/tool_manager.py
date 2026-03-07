"""
Cobalt Agent - Tool Manager
Registry and execution engine for all agent capabilities.
"""

import json
import uuid
from typing import Any, Dict, List, Optional, Type
from loguru import logger
from pydantic import BaseModel, ValidationError

# Import CobaltJSONEncoder for RFC-compliant JSON serialization
from cobalt_agent.utils.serializers import CobaltJSONEncoder

# Import your tools
from cobalt_agent.tools.search import SearchTool
# Import Browser
from cobalt_agent.tools.browser import BrowserTool, BrowserCommand
# Import Finance
from cobalt_agent.tools.finance import FinanceTool
# Import Filesystem tools
from cobalt_agent.tools.filesystem import ReadFileTool, WriteFileTool, ListDirectoryTool, AppendToFileTool
from cobalt_agent.tools.filesystem import ReadFileInput, WriteFileInput, ListDirectoryInput
# Import Knowledge Base
from cobalt_agent.tools.knowledge import KnowledgeSearchTool
from cobalt_agent.tools.daemon import DaemonTool
from cobalt_agent.tools.aom import AOMExtractor
from cobalt_agent.tools.maps import Maps
from cobalt_agent.tools.extractor import UniversalExtractor

# Dangerous tools that require HITL approval (write_file, browser actions, daemon, aom, maps, extractor, append_to_file)
DANGEROUS_TOOLS = {
    "write_file",
    "append_to_file",
    "browser",
    "daemon",
    "aom",
    "maps",
    "extractor"
}


class ToolResult(BaseModel):
    """Standardized output for any tool execution."""
    success: bool
    output: Any
    error: Optional[str] = None


class ToolManager:
    """
    Manages the registration and execution of tools.
    Allows the LLM to 'see' and 'use' functions.
    
    DECORATED: No longer imports ProposalEngine. Dangerous tools now return a status dict
    signaling the Bouncer (BaseDepartment) to handle HITL approval.
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
        self.register_tool("append_to_file", AppendToFileTool(), schema=WriteFileInput)
        self.register_tool("list_directory", ListDirectoryTool(), schema=ListDirectoryInput)
        
        # 5. Knowledge Base
        self.register_tool("search_knowledge", KnowledgeSearchTool())
        
        # 6. Daemon Tool (dangerous - requires HITL approval)
        daemon = DaemonTool()
        self.register_tool("daemon", daemon)
        
        # 7. AOM Tool (dangerous - requires HITL approval) - AOMExtractor
        aom = AOMExtractor()
        self.register_tool("aom", aom)
        
        # 8. Maps Tool (dangerous - requires HITL approval) - Maps
        maps = Maps()
        self.register_tool("maps", maps)
        
        # 9. Extractor Tool (dangerous - requires HITL approval) - UniversalExtractor
        extractor = UniversalExtractor()
        self.register_tool("extractor", extractor)
        
    def register_tool(self, name: str, tool_instance: Any, schema: Optional[Type[BaseModel]] = None):
        """Add a new tool to the registry."""
        self.tools[name] = tool_instance
        self.tools[name + '_schema'] = schema  # Store schema separately
        logger.info(f"Tool registered: {name}")

    def get_tool_descriptions(self) -> List[Any]:
        """Return the list of tool objects for the Prompt Engine."""
        return list(self.tools.values())

    def execute_tool(self, name: str, args: Any, bypass_hitl: bool = False) -> Any:
        """
        Execute a tool by name with the provided arguments.
        
        Dangerous tools (write_file, append_to_file, browser, daemon, aom, maps, extractor)
        are intercepted here and return a status dict signaling the Bouncer to create
        a HITL proposal.
        
        Args:
            name: The name of the tool to execute
            args: Arguments for the tool (dict or string)
            bypass_hitl: If True, skip HITL approval and execute directly (VIP pass)
            
        Returns:
            For dangerous tools with bypass_hitl=False: {"status": "requires_approval", "tool_name": ..., "tool_args": ...}
            For dangerous tools with bypass_hitl=True: Result string from tool execution
            For safe tools: Result string from tool execution
        """
        from loguru import logger
        logger.info(f"Executing tool: {name} with args: {args}")
        
        if name not in self.tools:
            return f"Error: Tool '{name}' not found."
        
        # VIP Bypass: Skip HITL approval if bypass_hitl is True
        if bypass_hitl:
            # Import tool directly - no Proposal Engine needed
            tool = self.tools[name]
            schema_key = name + '_schema'
            
            try:
                # Validate against Pydantic schema if available
                if schema_key in self.tools and self.tools[schema_key]:
                    schema = self.tools[schema_key]
                    try:
                        if isinstance(args, dict):
                            validated_args = schema(**args)
                            result = tool.run(**validated_args.model_dump())
                        elif isinstance(args, str):
                            try:
                                parsed_args = json.loads(args)
                                validated_args = schema(**parsed_args)
                                result = tool.run(**validated_args.model_dump())
                            except json.JSONDecodeError:
                                return f"Observation: Invalid JSON format. Please use strict double quotes."
                    except ValidationError as e:
                        error_str = str(e)
                        logger.warning(f"Pydantic validation error for tool {name}: {error_str}")
                        return f"Error: {error_str}"
                else:
                    if isinstance(args, dict):
                        result = tool.run(**args)
                    else:
                        result = tool.run(args)
                
                # Serialize Pydantic models to dictionaries before returning
                if isinstance(result, BaseModel):
                    result = result.model_dump()
                
                return json.dumps(result, cls=CobaltJSONEncoder)
                
            except json.JSONDecodeError:
                return f"Observation: Invalid JSON format. Please use strict double quotes."
            except TypeError as e:
                logger.warning(f"Tool {name} rejected kwargs, falling back to positional: {e}")
                if isinstance(args, dict):
                    if "query" in args:
                        result = tool.run(args["query"])
                    elif len(args) == 1:
                        result = tool.run(list(args.values())[0])
                    else:
                        result = tool.run(str(args))
                else:
                    result = tool.run(str(args))
                
                # Serialize Pydantic models to dictionaries before returning
                if isinstance(result, BaseModel):
                    result = result.model_dump()
                
                return json.dumps(result, cls=CobaltJSONEncoder)
            except Exception as e:
                logger.error(f"Error executing tool {name}: {str(e)}")
                return f"Error executing tool {name}: {str(e)}"
        
        # Check if this is a dangerous tool that requires HITL approval
        if name in DANGEROUS_TOOLS:
            # Return a status dict instead of calling ProposalEngine directly
            # This prevents circular imports and decouples ToolManager from ProposalEngine
            tool_kwargs = args if isinstance(args, dict) else {"query": args}
            return {
                "status": "requires_approval",
                "tool_name": name,
                "tool_args": tool_kwargs
            }
        
        # Safe tools (search, read_file, finance, search_knowledge, list_directory) execute directly
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
                        result = tool.run(**validated_args.model_dump())
                    elif isinstance(args, str):
                        # Try to parse string as JSON first
                        try:
                            parsed_args = json.loads(args)
                            validated_args = schema(**parsed_args)
                            result = tool.run(**validated_args.model_dump())
                        except json.JSONDecodeError:
                            # Return error for invalid JSON
                            return f"Observation: Invalid JSON format. Please use strict double quotes."
                except ValidationError as e:
                    # Return exact error message for LLM to self-correct
                    error_str = str(e)
                    logger.warning(f"Pydantic validation error for tool {name}: {error_str}")
                    return f"Error: {error_str}"
            else:
                if isinstance(args, dict):
                    result = tool.run(**args)
                else:
                    result = tool.run(args)
            
            # Serialize Pydantic models to dictionaries before returning
            if isinstance(result, BaseModel):
                result = result.model_dump()
            
            return json.dumps(result, cls=CobaltJSONEncoder)
            
        except json.JSONDecodeError as e:
            return f"Observation: Invalid JSON format. Please use strict double quotes."
        except TypeError as e:
            # Fallback for legacy tools that strictly only accept a single positional 'query' string
            logger.warning(f"Tool {name} rejected kwargs, falling back to positional: {e}")
            if isinstance(args, dict):
                if "query" in args:
                    result = tool.run(args["query"])
                elif len(args) == 1:
                    result = tool.run(list(args.values())[0])
                else:
                    result = tool.run(str(args))
            else:
                result = tool.run(str(args))
            
            # Serialize Pydantic models to dictionaries before returning
            if isinstance(result, BaseModel):
                result = result.model_dump()
            
            return json.dumps(result, cls=CobaltJSONEncoder)
        except Exception as e:
            logger.error(f"Error executing tool {name}: {str(e)}")
            return f"Error executing tool {name}: {str(e)}"
