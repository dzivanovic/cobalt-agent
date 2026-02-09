"""
Cobalt Agent - Prompt Engine
Constructs dynamic system prompts based on context, tools, and time.
"""

import datetime
from typing import List, Any
from cobalt_agent.config import PersonaConfig

class PromptEngine:
    """
    Generates the 'System Prompt' that tells the LLM how to behave.
    """
    
    def __init__(self, persona_config: PersonaConfig):
        self.persona = persona_config

    def build_system_prompt(self, tools: List[Any] = None) -> str:
        """
        Construct the full system prompt.
        
        Args:
            tools: List of tool objects available to the agent.
        """
        # 1. Identity & Role
        header = self._build_header()
        
        # 2. Operational Context (Time/Date)
        context = self._build_context()
        
        # 3. Directives (Rules)
        directives = self._build_directives()
        
        # 4. Tool Capabilities (What it can do)
        tool_section = self._build_tool_descriptions(tools)
        
        # Combine everything
        return f"{header}\n\n{context}\n\n{directives}\n\n{tool_section}"

    def _build_header(self) -> str:
        # Handle list of roles (join nicely)
        roles_str = ", ".join(self.persona.roles)
        # Handle list of tones
        tone_str = ", ".join(self.persona.tone)
        
        return (
            f"You are {self.persona.name}, a {roles_str}.\n"
            f"Your Tone: {tone_str}."
        )

    def _build_context(self) -> str:
        now = datetime.datetime.now()
        return (
            f"### CURRENT CONTEXT\n"
            f"- Current Date/Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"- Operating System: Python Environment (CLI)\n"
            f"- User: Administrator"
        )

    def _build_directives(self) -> str:
        # 1. Base Rules
        rules = [
            "You are an AUTONOMOUS AGENT. You are NOT a chat bot.",
            "You DO NOT have internal knowledge of real-time events.",
            "You MUST use tools to answer questions about the world."
        ]
        
        if self.persona.directives:
            rules.extend(self.persona.directives)
            
        # 2. The Protocol (Simulated Dialogue)
        protocol = (
            "\n### ⚡ CRITICAL OPERATING PROTOCOL ⚡\n"
            "To use a tool, you must output a single line starting with 'ACTION:'.\n"
            "Do not talk. Do not explain. JUST ACTION.\n\n"
            "### EXAMPLES OF CORRECT BEHAVIOR:\n"
            "User: What is the price of Apple?\n"
            "You: ACTION: finance AAPL\n"
            "System: [Observation: AAPL is $150]\n"
            "You: Apple is trading at $150.\n\n"
            "User: Find news about AI.\n"
            "You: ACTION: search AI news\n"
            "System: [Observation: AI is growing...]\n"
            "You: Recent news indicates AI is growing.\n\n"
            "### YOUR TURN:\n"
            "If I ask you a question that requires data, do not answer directly. START WITH ACTION:."
        )

        return "### DIRECTIVES\n" + "\n".join([f"- {r}" for r in rules]) + protocol

    def _build_tool_descriptions(self, tools) -> str:
        if not tools:
            return ""
            
        descriptions = []
        for tool in tools:
            # We look for a 'name' and 'description' attribute on the tool class
            name = getattr(tool, 'name', str(tool))
            desc = getattr(tool, 'description', 'No description provided.')
            descriptions.append(f"- {name}: {desc}")
        
        return "### AVAILABLE TOOLS\n" + "\n".join(descriptions)