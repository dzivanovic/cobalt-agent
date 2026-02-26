"""
Orchestration State Machine for Cobalt Agent
Tracks the Architect's plan and the Drone's progress through sub-tasks.
Self-healing retry loop to overcome local LLM JSON hallucinations.
"""

from typing import List
from pydantic import BaseModel, Field
from loguru import logger
from cobalt_agent.llm import LLM

class SubTask(BaseModel):
    step_number: int = Field(description="The sequential order of this step (e.g., 1, 2, 3).")
    assigned_drone: str = Field(description="The department to handle this step: 'ENGINEERING' or 'OPS'.")
    action: str = Field(description="A clear description of what needs to be done.")
    tool_to_use: str = Field(description="The exact name of the tool to use.")
    status: str = Field(default="PENDING", description="PENDING, SUCCESS, or FAILED")
    observation: str = Field(default="", description="The output or error from the drone's execution.")

class OrchestrationState(BaseModel):
    scratchpad: str = Field(description="Your detailed chain of thought. Explain exactly how you will break this down before writing the master plan.")
    original_request: str = Field(description="The user's exact original request.")
    master_plan: List[SubTask] = Field(min_length=1, description="The step-by-step plan to achieve the goal. THIS CANNOT BE EMPTY. You MUST generate at least one task.")
    current_step: int = Field(default=1)
    status: str = Field(default="PLANNING", description="PLANNING, EXECUTING, FAILED, COMPLETED")

class OrchestratorEngine:
    """
    The Manager's Clipboard (Chief of Staff). 
    Coordinates the "Split-Brain" architecture between the Architect (Planner) and specialized Drones (Executors).
    """
    def __init__(self):
        self.llm = LLM()

    def plan_and_execute(self, user_input: str) -> str:
        logger.info("Orchestrator: Generating Master Plan...")
        
        # 1. THE ARCHITECT PHASE
        architect_prompt = f"""
        You are the Principal Systems Architect (Chief of Staff).
        Analyze the following request and break it down into a step-by-step execution plan.
        
        AVAILABLE DRONES (Departments):
        - ENGINEERING: Use for writing Python code, modifying system files, or analyzing software architecture.
        - OPS: Use for searching the knowledge base, writing Markdown journals, summarizing text, or reading/modifying Obsidian notes.
        
        Available Tools for Drones:
        - search_knowledge (Search the internal codebase, playbooks, and Obsidian notes for context)
        - read_file (Read file contents)
        - list_directory (Explore folder structures)
        - write_file (Create or modify files)
        
        RULES:
        1. Keep steps atomic (e.g., Step 1: search_knowledge, Step 2: read_file, Step 3: write_file).
        2. Do NOT write code in the plan, just the actions the drone needs to take.
        3. Assign the correct Drone to each step based on the task domain.
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
                if state and state.master_plan:
                    break
                logger.warning(f"Architect returned empty plan on attempt {attempt+1}")
            except Exception as e:
                logger.warning(f"Architect parsing failed on attempt {attempt+1}: {e}")
                
        # Final Failsafe
        if not state or not state.master_plan:
            return "❌ **Architect Error:** The LLM failed to generate a valid plan after 3 attempts. Please simplify the request."
            
        # Format the visual output for Mattermost
        output_log = "### 📋 Chief of Staff's Master Plan\n"
        output_log += f"**Thoughts:** *{state.scratchpad}*\n\n"
        for step in state.master_plan:
            output_log += f"{step.step_number}. **[{step.assigned_drone.upper()}]** {step.action} (Tool: `{step.tool_to_use}`)\n"
            
        output_log += "\n### 🚀 Execution Log\n"
        
        # 2. THE DRONE EXECUTION PHASE
        for step in state.master_plan:
            output_log += f"\n**Executing Step {step.step_number} ({step.assigned_drone}):** {step.action}\n"
            logger.info(f"Orchestrator: Executing Step {step.step_number} via {step.assigned_drone}")
            
            # Build context from previous steps (The Manager's Clipboard)
            previous_context = ""
            for prev_step in state.master_plan:
                if prev_step.step_number < step.step_number and prev_step.observation:
                    previous_context += f"Step {prev_step.step_number} Result:\n{prev_step.observation}\n\n"
            
            # Formulate the localized context for the Drone
            execution_context = f"""
            YOUR OVERALL MISSION:
            {state.original_request}
            
            PREVIOUS CONTEXT (Results of prior steps):
            {previous_context if previous_context else "None (This is the first step)."}
            
            SPECIFIC STEP TO EXECUTE NOW:
            {step.action}
            
            You must use the '{step.tool_to_use}' tool. Generate the ACTION string now.
            """
            
            # Dynamic Drone Routing
            drone_type = step.assigned_drone.upper()
            if drone_type == "OPS":
                from cobalt_agent.brain.ops import OpsDepartment
                drone = OpsDepartment()
            else:
                # Default to Engineering for unknown or explicit ENGINEERING
                from cobalt_agent.brain.engineering import EngineeringDepartment
                drone = EngineeringDepartment()
                
            # Run the task through the unified ReAct loop
            result = drone.run(execution_context)
            
            step.observation = result
            output_log += f"> {result}\n"
            
            # Zero Trust Break
            if "Action paused" in result or "Proposal [" in result:
                output_log += "\n⚠️ **Execution paused. Awaiting Human-in-the-Loop Approval.**"
                state.status = "PAUSED_FOR_APPROVAL"
                break
                
            if "Error:" in result:
                output_log += "\n❌ **Step failed. Halting execution.**"
                state.status = "FAILED"
                break
                
        if state.status == "PLANNING": 
            state.status = "COMPLETED"
            output_log += "\n✅ **Mission Accomplished.**"
            
        return output_log