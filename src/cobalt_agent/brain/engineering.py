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
    
    def __init__(self, system_prompt: str = None):
        """Initialize the Engineering Department."""
        logger.info("🛠️ The Forge (Engineering) Online")
        self.llm = LLM()
        self.tool_manager = ToolManager()
        
        if system_prompt:
            self.system_prompt = system_prompt
        else:
            self.system_prompt = """
        You are THE FORGE, Cobalt's Principal Systems Architect and Senior Software Engineer.
        Your job is to read, analyze, and write code.
        
        CRITICAL RULES:
        1. NEVER guess the contents of a file or directory.
        2. To modify or create a file, you MUST use the `write_file` tool. 
        3. YOU MUST USE THE EXACT SYNTAX BELOW TO CALL A TOOL. If you do not use the `ACTION:` prefix, the tool will fail.
           - CORRECT: ACTION: write_file {"filepath": "src/test.py", "content": "print('hello')"}
           - INCORRECT: {"filepath": "src/test.py", "content": "print('hello')"}
           - INCORRECT: ```json\n{"filepath": "src/test.py", "content": "print('hello')"}\n```
        4. DO NOT roleplay. DO NOT say "I will create the file now." Just output the ACTION string.
        5. WORKFLOW EFFICIENCY: If the user provides an exact filepath (e.g., "create a file at src/test.py"), DO NOT use `list_directory`. Execute `write_file` immediately to save context space.
        6. WAIT PROTOCOL: If you use the `write_file` tool and the System Observation says "Action paused. Proposal sent", YOU MUST STOP. Output a final conversational message saying "I have submitted the proposal for your approval." DO NOT try to write the file again.
        
        AVAILABLE TOOLS:
        - `read_file`: Reads a file. 
          Syntax: ACTION: read_file {"filepath": "src/main.py"}
        
        - `list_directory`: Lists a folder. 
          Syntax: ACTION: list_directory {"directory_path": "src/"}
        
        - `write_file`: Modifies or creates a file. YOU MUST USE THIS TO PROPOSE CHANGES. 
          Syntax: ACTION: write_file {"filepath": "src/test.py", "content": "print('hello')"}
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
                raw_result = self.tool_manager.execute_tool(tool_name, args_dict)
                
                # Forcibly cast the result to a string (it might be a Pydantic model)
                result_str = str(raw_result)
                
                # Format the result
                if result_str.startswith("Error:"):
                    result_text = result_str
                else:
                    result_text = result_str
                    
                # 🛑 FAST EXIT: If we hit a Zero-Trust Proposal wall, do not force the LLM to loop again.
                if "Action paused" in result_str or "Proposal [" in result_str:
                    return result_text
                
                # Append observation to history and loop
                messages.append({"role": "assistant", "content": response})
                messages.append({"role": "system", "content": f"[Observation: {result_text}]"})
            else:
                return response
                
        return "Error: ReAct loop maxed out. Please simplify the request."