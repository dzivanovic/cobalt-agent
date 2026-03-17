"""
Cobalt Scheduler Service
Background job scheduler for automated tasks like Morning Briefing.
"""
import json
import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger
from cobalt_agent.config import get_config
from cobalt_agent.llm import LLM
from cobalt_agent.brain.base import BaseDepartment


class CobaltScheduler:
    """
    Background scheduler for automated tasks.
    Handles Morning Briefing generation and delivery.
    """
    
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.config = get_config()
        self._setup_jobs()

    def _setup_jobs(self):
        """Register all automated background tasks."""
        # Schedule Morning Briefing for 8:00 AM EST every weekday (Mon-Fri)
        self.scheduler.add_job(
            self.generate_morning_briefing,
            'cron',
            day_of_week='mon-fri',
            hour=8,
            minute=0,
            id='morning_briefing',
            replace_existing=True
        )
        logger.info("⏱️ Scheduler: Morning Briefing job registered (Mon-Fri 08:00).")

    def start(self):
        """Start the background scheduler."""
        self.scheduler.start()
        logger.info("⏱️ Cobalt Heartbeat (Scheduler) Online.")
        
        # --- TEST OVERRIDE: FIRE IMMEDIATELY ON BOOT ---
        #logger.info("🧪 Executing Immediate Test Override...")
        #self.generate_morning_briefing()
        # -----------------------------------------------

    def shutdown(self):
        """Shutdown the scheduler gracefully."""
        self.scheduler.shutdown()

    def generate_morning_briefing(self):
        """
        Runs the Gemini 3.1 Pro query and saves the output to the Obsidian Vault.
        Uses BaseDepartment's ReAct execution loop for tool access.
        Enables Google Search Grounding via googleSearch tool.
        """
        logger.info("☀️ Running Automated Morning Briefing...")
        
        today_str = datetime.now().strftime("%B %d, %Y")
        
        # Load prompt from config (safe access with .get() for None handling)
        scheduler_config = self.config.prompts.scheduler or {}
        prompt_template = scheduler_config.get("morning_briefing")
        if not prompt_template:
            raise ValueError("Morning briefing prompt not configured in prompts.yaml")
        prompt = prompt_template.format(today_str=today_str)

        # Define googleSearch tool for grounding - enables live data retrieval
        google_search_tool = [{"googleSearch": {}}]

        try:
            # Create a temporary agent using BaseDepartment with researcher role
            # This ensures the ReAct loop and ToolManager are used for tool execution
            briefing_agent = BriefingAgent(name="MorningBriefing", role="researcher")
            
            logger.info("Calling Gemini 2.5 Pro via ReAct loop for market data with googleSearch grounding...")
            report_result = briefing_agent.run(prompt, tools=google_search_tool)
            
            # Handle case where result is a dict (proposal requiring approval)
            if isinstance(report_result, dict):
                logger.error("Morning Briefing requires human approval. Proposal not written to file.")
                raise RuntimeError(f"Morning Briefing proposal requires approval: {report_result}")
            
            report_content = str(report_result)
            
            # Format the output filepath
            vault_path = self.config.system.obsidian_vault_path
            filename = f"Morning_Briefing_{datetime.now().strftime('%Y-%m-%d')}.md"
            filepath = os.path.join(vault_path, "0 - Inbox", filename)
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # Write the file directly
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_content)
                
            logger.info(f"✅ Morning Briefing successfully written to {filepath}")
            
            # Broadcast to Mattermost to notify the user
            from cobalt_agent.interfaces.mattermost import MattermostInterface
            mm = MattermostInterface()
            mm.connect()
            mm.send_message("town-square", self.config.mattermost.approval_team, f"☀️ **Morning Briefing Ready!** I have generated the pre-market analysis for {today_str} and saved it to your Inbox.")
            
        except Exception as e:
            logger.error(f"Failed to generate Morning Briefing: {e}")


class BriefingAgent(BaseDepartment):
    """
    Temporary agent for generating morning briefings.
    Inherits from BaseDepartment to leverage the ReAct execution loop and ToolManager.
    Uses the researcher role (Gemini 2.5 Pro) for market analysis.
    """
    
    def __init__(self, name: str, role: str = "researcher"):
        # BaseDepartment requires system_prompt, but we'll set it dynamically in run()
        super().__init__(name=name, system_prompt=None)
        # Override the LLM with the researcher role for this agent
        self.llm = LLM(role=role)
    
    def run(self, user_message: str, chat_history=None, tools=None) -> str | dict:
        """
        Execute the briefing task using the ReAct loop.
        
        Args:
            user_message: The morning briefing prompt with today's date
            chat_history: Optional list of previous messages for context
            tools: Optional list of tool definitions (e.g., googleSearch) to enable grounding
            
        Returns:
            The final briefing report after tool execution or max loops
        """
        logger.info(f"[{self.name}] Executing morning briefing task...")
        
        # System prompt for the financial analyst persona
        system_prompt = "You are a senior financial analyst and day trader. You have access to real-time data via tools. Output strictly in the requested markdown format."
        
        messages = [{"role": "system", "content": system_prompt}]
        if chat_history:
            messages.extend(chat_history)
            
        messages.append({"role": "user", "content": user_message})
        
        # Pass tools to LLM for grounding if provided
        llm_tools = tools if tools else None
        
        max_loops = 4
        for _ in range(max_loops):
            # Get response from LLM using the unified interface with googleSearch grounding
            memory_context = messages[:-1] if len(messages) > 1 else []
            response = self.llm.generate_response(
                system_prompt=system_prompt,
                user_input=messages[-1]["content"],
                memory_context=memory_context,
                search_context="",
                tools=llm_tools
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
                        except json.JSONDecodeError as e:
                            # Return explicit error for invalid JSON so LLM can self-correct
                            logger.warning(f"Failed to parse tool args as JSON: {e}")
                            error_msg = "Observation: Invalid JSON format. Please use strict double quotes."
                            messages.append({"role": "assistant", "content": response})
                            messages.append({"role": "system", "content": error_msg})
                            continue
                    
                    # Execute the tool via ToolManager
                    raw_result = self.tool_manager.execute_tool(tool_name, args_dict)
                    
                    # Return the raw dict to caller for centralized proposal handling
                    if isinstance(raw_result, dict) and raw_result.get("status") == "requires_approval":
                        return raw_result
                    
                    # Convert result to string
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
                    logger.exception(f"Error executing tool: {e}")
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "system", "content": f"Error executing tool: {e}"})
            else:
                # No ACTION found, meaning the agent is finished
                return response
                
        return "Error: ReAct loop maxed out. Please simplify the request."