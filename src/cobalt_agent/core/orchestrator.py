"""
Orchestration State Machine for Cobalt Agent
Tracks the Architect's plan and the Drone's progress through sub-tasks.
Self-healing retry loop to overcome local LLM JSON hallucinations.
"""

from typing import List

from pydantic import BaseModel, Field
from loguru import logger

from cobalt_agent.llm import LLM
from cobalt_agent.brain.engineering import EngineeringDepartment


class SubTask(BaseModel):
    """A single step in the orchestration plan."""
    
    step_number: int = Field(description="The sequential order of this step (e.g., 1, 2, 3).")
    action: str = Field(description="A clear description of what needs to be done.")
    tool_to_use: str = Field(description="The exact name of the tool to use (e.g., 'read_file', 'list_directory', 'write_file').")
    status: str = Field(default="PENDING", description="PENDING, SUCCESS, or FAILED")
    observation: str = Field(default="", description="The output or error from the drone's execution.")


class OrchestrationState(BaseModel):
    """The current state of the orchestration process."""
    
    scratchpad: str = Field(description="Your detailed chain of thought. Explain exactly how you will break this down before writing the master plan.")
    original_request: str = Field(description="The user's exact original request.")
    master_plan: List[SubTask] = Field(min_length=1, description="The step-by-step plan to achieve the goal. THIS CANNOT BE EMPTY. You MUST generate at least one task.")
    current_step: int = Field(default=1)
    status: str = Field(default="PLANNING", description="PLANNING, EXECUTING, FAILED, COMPLETED")


class OrchestratorEngine:
    """
    The Manager's Clipboard. 
    Coordinates the "Split-Brain" architecture between the Architect (Planner) and the Drone (Executor).
    """
    def __init__(self):
        self.llm = LLM()

    def plan_and_execute(self, user_input: str) -> str:
        logger.info("Orchestrator: Generating Master Plan...")
        
        # 1. THE ARCHITECT PHASE
        architect_prompt = f"""
        You are the Principal Systems Architect.
        Analyze the following engineering request and break it down into a step-by-step execution plan.
        
        USER REQUEST: "{user_input}"
        
        Available Tools for the Drone:
        - read_file (Read file contents)
        - list_directory (Explore folder structures)
        - write_file (Create or modify files)
        - search_knowledge (Search the internal codebase, playbooks, and Obsidian notes for context)
        
        RULES:
        1. Keep steps atomic (e.g., Step 1: list_directory, Step 2: read_file, Step 3: write_file).
        2. Do NOT write code in the plan, just the actions the drone needs to take.
        3. If the user gives an exact filepath to write, skip directory listing and go straight to write_file.
        4. YOU MUST POPULATE THE 'master_plan' ARRAY. Do not return an empty list.
        """
        
        state = None
        max_retries = 3
        
        # Self-Healing Retry Loop
        for attempt in range(max_retries):
            try:
                state = self.llm.ask_structured(
                    system_prompt=architect_prompt, 
                    response_model=OrchestrationState,
                    user_input=user_input
                )
                # If Pydantic validation passes and we have a plan, break the loop
                if state and state.master_plan:
                    break
                logger.warning(f"Architect returned empty plan on attempt {attempt+1}")
            except Exception as e:
                logger.warning(f"Architect parsing failed on attempt {attempt+1}: {e}")
                
        # Final Failsafe
        if not state or not state.master_plan:
            return "❌ **Architect Error:** The LLM failed to generate a valid plan after 3 attempts. Please simplify the request."
            
        # Format the visual output for Mattermost
        output_log = "### 📋 Architect's Master Plan\n"
        output_log += f"**Architect's Thoughts:** *{state.scratchpad}*\n\n"
        for step in state.master_plan:
            output_log += f"{step.step_number}. **{step.action}** (Tool: `{step.tool_to_use}`)\n"
            
        output_log += "\n### 🚀 Execution Log\n"
        
        # 2. THE DRONE EXECUTION PHASE
        for step in state.master_plan:
            output_log += f"\n**Executing Step {step.step_number}:** {step.action}\n"
            logger.info(f"Orchestrator: Executing Step {step.step_number}")
            
            # Build context from previous steps (The Manager's Clipboard)
            previous_context = ""
            for prev_step in state.master_plan:
                if prev_step.step_number < step.step_number and prev_step.observation:
                    previous_context += f"Step {prev_step.step_number} Result:\n{prev_step.observation}\n\n"
            
            # The highly-restricted dynamic persona
            drone_prompt = f"""
            You are THE FORGE DRONE, a specialized execution agent.
            Your ONLY purpose is to execute the specific task given to you.
            
            CRITICAL RULES:
            1. To modify or create a file, you MUST use the `write_file` tool. 
            2. YOU MUST USE THE EXACT SYNTAX BELOW TO CALL A TOOL.
               - CORRECT: ACTION: write_file {{"filepath": "src/test.py", "content": "print('hello')"}}
            3. DO NOT roleplay. Just output the ACTION string.
            4. NEVER guess file paths. You MUST use the EXACT FULL PATH provided in the instructions (e.g., if told to write to '0 - Inbox/file.md', do not just write 'file.md').
            
            AVAILABLE TOOLS:
            - `search_knowledge`: ACTION: search_knowledge {{"query": "Semantic search concept"}}
            - `read_file`: ACTION: read_file {{"filepath": "src/main.py"}}
            - `list_directory`: ACTION: list_directory {{"directory_path": "src/"}}
            - `write_file`: ACTION: write_file {{"filepath": "src/test.py", "content": "print('hello')"}}
            
            YOUR OVERALL MISSION:
            {state.original_request}
            
            PREVIOUS CONTEXT (Results of prior steps):
            {previous_context if previous_context else "None (This is the first step)."}
            
            SPECIFIC STEP TO EXECUTE NOW:
            {step.action}
            
            You must use the '{step.tool_to_use}' tool. Generate the ACTION string now.
            """
            
            # Spin up the drone with the isolated memory/prompt
            drone = EngineeringDepartment(system_prompt=drone_prompt)
            result = drone.run(step.action)
            
            step.observation = result
            output_log += f"> {result}\n"
            
            # Zero Trust Break: Stop loop if we hit a proposal wall
            if "Action paused" in result or "Proposal [" in result:
                output_log += "\n⚠️ **Execution paused. Awaiting Human-in-the-Loop Approval.**"
                state.status = "PAUSED_FOR_APPROVAL"
                break
                
            # Stop if the tool errors out to prevent hallucination spirals
            if "Error:" in result:
                output_log += "\n❌ **Step failed. Halting execution.**"
                state.status = "FAILED"
                break
                
        if state.status == "PLANNING": 
            state.status = "COMPLETED"
            output_log += "\n✅ **Mission Accomplished.**"
            
        return output_log