"""
The Unified ReAct Execution Engine.
All specialized Drones inherit this execution loop.
"""
import json
import re
from abc import ABC
from typing import Optional, List, Dict
from loguru import logger
from cobalt_agent.llm import LLM
from cobalt_agent.tools.tool_manager import ToolManager


class BaseDepartment(ABC):
    """
    The Unified ReAct Execution Engine.
    All specialized Drones inherit this execution loop.
    """
    def __init__(self, name: str, system_prompt: Optional[str] = None):
        self.name = name
        self.llm = LLM()
        self.tool_manager = ToolManager()
        self.system_prompt = system_prompt

    def run(self, user_message: str, chat_history: Optional[List[Dict]] = None) -> str:
        """
        Process a request using the ReAct loop.
        
        Args:
            user_message: The user's request
            chat_history: Optional list of previous messages for context
            
        Returns:
            The final response after tool execution or max loops
        """
        logger.info(f"[{self.name}] Executing task...")
        
        messages: List[Dict] = [{"role": "system", "content": self.system_prompt}]
        if chat_history:
            messages.extend(chat_history)
            
        messages.append({"role": "user", "content": user_message})
        
        max_loops = 4
        for _ in range(max_loops):
            # Get response from LLM using the unified interface
            memory_context = messages[:-1] if len(messages) > 1 else []
            response = self.llm.generate_response(
                system_prompt=self.system_prompt,
                user_input=messages[-1]["content"],
                memory_context=memory_context,
                search_context=""
            )
            
            if "ACTION:" in response:
                try:
                    # Extract tool name and arguments from ACTION line
                    action_lines = [line for line in response.split('\n') if line.startswith('ACTION:')]
                    if not action_lines:
                        messages.append({"role": "assistant", "content": response})
                        messages.append({"role": "system", "content": "Error: Malformed ACTION format. Ensure you use ACTION: tool_name {\"key\": \"value\"}"})
                        continue
                    
                    action_line = action_lines[0]
                    command = action_line.replace('ACTION:', '').strip()
                    
                    # Parse tool name and arguments
                    parts = command.split(' ', 1)
                    tool_name = parts[0]
                    args_dict = {}
                    if len(parts) > 1:
                        try:
                            # Clean up the string if the LLM wrapped it in quotes or markdown
                            clean_args = parts[1].strip()
                            if clean_args.startswith("'") and clean_args.endswith("'"):
                                clean_args = clean_args[1:-1]
                            args_dict = json.loads(clean_args)
                            if not isinstance(args_dict, dict):
                                args_dict = {'query': clean_args}
                        except Exception as e:
                            logger.warning(f"Failed to parse tool args as JSON: {e}")
                            args_dict = {'query': parts[1] if len(parts) > 1 else ''}
                    
                    # Execute the tool
                    raw_result = self.tool_manager.execute_tool(tool_name, args_dict)
                    result_str = str(raw_result)
                    
                    # Format the result
                    if result_str.startswith("Error:"):
                        result_text = result_str
                    else:
                        result_text = result_str
                        
                    # 🛑 FAST EXIT: If we hit a Zero-Trust Proposal wall, stop looping
                    if "Action paused" in result_str or "Proposal [" in result_str:
                        return result_text
                    
                    # Append observation to history and loop
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "system", "content": f"[Observation: {result_text}]"})
                    
                except json.JSONDecodeError as e:
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "system", "content": f"Error parsing JSON arguments: {e}"})
                except Exception as e:
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "system", "content": f"Error executing tool: {e}"})
            else:
                # No ACTION found, meaning the drone is finished
                return response
                
        return "Error: ReAct loop maxed out. Please simplify the request."
