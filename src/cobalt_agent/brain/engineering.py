"""
The Forge (Engineering Department)
Cobalt's Principal Systems Architect and Senior Software Engineer.
Responsible for reading, analyzing, and writing code.
"""
from loguru import logger
from cobalt_agent.llm import LLM
from cobalt_agent.tools.tool_manager import ToolManager


class EngineeringDepartment:
    """
    The Forge - Cobalt's codebase manipulation department.
    Handles code reading, analysis, and writing tasks.
    """
    
    def __init__(self):
        """Initialize the Engineering Department."""
        logger.info("🛠️ The Forge (Engineering) Online")
        self.llm = LLM()
        self.tool_manager = ToolManager()
        
        self.system_prompt = """
        You are THE FORGE, Cobalt's Principal Systems Architect and Senior Software Engineer.
        Your job is to read, analyze, and write code.
        
        CRITICAL RULES:
        1. NEVER guess the contents of a file or directory.
        2. To modify a file, use the `write_file` tool. 
        3. The `write_file` tool requires a valid JSON string with `filepath` and `content`.
        4. When you use `write_file`, it will NOT execute immediately. It sends a Proposal to the user. You must inform the user that a proposal has been generated.
        5. Think step-by-step. First list the directory using `list_directory`, then read the target file using `read_file`, then propose the change.
        
        AVAILABLE TOOLS:
        - `read_file`: Reads the contents of a file. (Example: ACTION: read_file src/main.py)
        - `list_directory`: Lists the files in a folder. (Example: ACTION: list_directory src/cobalt_agent/)
        - `write_file`: Proposes a file modification. (Example: ACTION: write_file {"filepath": "...", "content": "..."})
        """

    def run(self, user_message: str, chat_history: list = None) -> str:
        """
        Process an engineering request using ReAct loop.
        
        Args:
            user_message: The user's request for engineering work
            chat_history: Optional list of previous messages for context
            
        Returns:
            The final response after tool execution or max loops
        """
        logger.info("The Forge is analyzing an engineering request...")
        
        # Build the LLM prompt with tools
        messages = [{"role": "system", "content": self.system_prompt}]
        if chat_history:
            messages.extend(chat_history)
            
        messages.append({"role": "user", "content": user_message})
        
        # Execute the ReAct loop for engineering tools
        max_loops = 4
        for _ in range(max_loops):
            # Get response from LLM
            response = self.llm.generate_response(
                system_prompt=self.system_prompt,
                user_input=messages[-1]["content"],
                memory_context=messages[:-1] if len(messages) > 1 else None,
                search_context=""
            )
            
            logger.debug(f"Forge LLM Response: {response}")
            
            if "ACTION:" in response:
                # Extract tool name and query from ACTION line
                action_lines = [line for line in response.split('\n') if line.startswith('ACTION:')]
                if not action_lines:
                    return response
                    
                action_line = action_lines[0]
                command = action_line.replace('ACTION:', '').strip()
                
                # Parse tool name and arguments
                parts = command.split(' ', 1)
                tool_name = parts[0]
                args_dict = {}
                if len(parts) > 1:
                    try:
                        import json
                        # Clean up the string if the LLM wrapped it in quotes or markdown
                        clean_args = parts[1].strip()
                        if clean_args.startswith("'") and clean_args.endswith("'"):
                            clean_args = clean_args[1:-1]
                        
                        args_dict = json.loads(clean_args)
                        if not isinstance(args_dict, dict):
                            args_dict = {'query': clean_args}
                    except Exception as e:
                        logger.warning(f"Failed to parse tool args as JSON: {e}")
                        args_dict = {'query': parts[1]}
                
                logger.debug(f"Forge executing tool: {tool_name}, args: {args_dict}")
                
                # Execute the tool
                result = self.tool_manager.execute_tool(tool_name, args_dict)
                
                # Format the result
                if result.success:
                    result_text = result.output
                else:
                    result_text = f"Error: {result.error}"
                
                # Append observation to history and loop
                messages.append({"role": "assistant", "content": response})
                messages.append({"role": "system", "content": f"[Observation: {result_text}]"})
            else:
                return response
                
        return "Error: ReAct loop maxed out. Please simplify the request."