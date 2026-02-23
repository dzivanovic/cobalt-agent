"""
The Cortex (Manager Agent) - Config-Driven Architecture
Routes user intent based on domains defined in config.yaml.
Includes robust error handling, full Scribe logic, and Medical Admin placeholders.
"""
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field
from loguru import logger

from cobalt_agent.llm import LLM
from cobalt_agent.config import load_config

# --- ROUTING MODEL ---
class DomainDecision(BaseModel):
    domain_name: str = Field(description="The exact name of the department (e.g. TACTICAL, OPS).")
    reasoning: str = Field(description="Why this department fits the request.")
    task_parameters: str = Field(
        description="The PRECISE entity or query to act on. For Tactical, this MUST be just the Ticker Symbol (e.g. 'NVDA') OR the command 'STRATEGY'."
    )

class Cortex:
    def __init__(self):
        self.config = load_config()
        
        # --- ROBUST LLM CONFIG ---
        # Try 'model_name' first, then 'model', then default to 'gpt-4o'
        model_name = getattr(self.config.llm, "model_name", None)
        if not model_name:
            model_name = getattr(self.config.llm, "model", "gpt-4o")
            
        self.llm = LLM(model_name=model_name)
        
        # --- ROBUST DEPARTMENTS LOAD ---
        deps = getattr(self.config, "departments", None)
        if deps is None:
            deps = {}
        self.departments = deps
        
        logger.info(f"🧠 Cortex Online | Loaded {len(self.departments)} Departments from Config")

    def route(self, user_input: str) -> Optional[str]:
        """Dynamically routes based on config."""
        # Fast exit
        if len(user_input.split()) < 4 and "hi" in user_input.lower():
            return None

        # 1. Hardcoded bypass for questions - routes to FOUNDATION (standard chat with tool access)
        text_lower = user_input.lower()
        if "?" in text_lower or "price" in text_lower or "what" in text_lower:
            logger.info("Direct route bypass triggered: Question detected.")
            return None
        
        # 2. Classify
        decision = self._classify_domain(user_input)
        
        # 2. Lazy Load & Execute
        domain = decision.domain_name.upper()
        params = decision.task_parameters.strip()

        logger.info(f"👉 Cortex Routing: {domain} | Task: {params}")
        
        if domain == "TACTICAL":
            return self._run_tactical(params)
        
        elif domain == "INTEL":
            return self._run_intel(params)
            
        elif domain == "GROWTH":
            return "👷 The Architect (Growth) is defined but not yet hired."
            
        elif domain == "OPS":
            return self._run_ops(params, user_input) # Pass original input for Scribe context
            
        elif domain == "ENGINEERING":
            return "🛠️ Forge (Engineering) is defined but not yet hired."
            
        elif domain == "FOUNDATION":
            return None # Handle in main chat loop
            
        else:
            return f"⚠️ Unknown Domain: {domain}"

    def _classify_domain(self, user_input: str) -> DomainDecision:
        """Builds prompt from config.yaml definitions."""
        options_text = ""
        
        # Guard against empty departments
        if not self.departments:
            options_text = "- TACTICAL\n- INTEL\n- OPS"
        else:
            for name, data in self.departments.items():
                is_active = False
                desc = "No description"
                if isinstance(data, dict):
                    is_active = data.get('active', False)
                    desc = data.get('description', desc)
                elif hasattr(data, 'active'):
                    is_active = getattr(data, 'active', False)
                    desc = getattr(data, 'description', desc)

                if is_active:
                    options_text += f"- {name}: {desc}\n"
        
        # UPDATED PROMPT: Explicitly maps "Strategy" to TACTICAL
        prompt = f"""
        You are the Chief of Staff (Cortex). Route this user request to the correct Department.
        
        USER REQUEST: "{user_input}"
        
        ACTIVE DEPARTMENTS:
        {options_text}
        - FOUNDATION: General chat, greetings, system questions.
        
        === ROUTING LOGIC ===
        1. TACTICAL (Trading/Market Data):
           - Use for: stock prices, market data, ticker queries (e.g., "AAPL", "TSLA", "NVDA")
           - Use for: "What is the price of X?", "Give me AAPL data", "Stock price"
           - Extract ONLY the ticker symbol (e.g. "NVDA", "AAPL") as task_parameters
           - Use "STRATEGY" ONLY if user explicitly asks about strategies, strategies menu, or playbooks
        
        2. INTEL (Research/News):
           - Use for: news, general research, deep dives, current events
           - Extract the search topic as task_parameters
        
        3. OPS (Operations/Scribe):
           - Use for: logging, journaling, saving notes, medical billing
           - Extract relevant content as task_parameters
        
        4. FOUNDATION:
           - Use for: greetings, small talk, system questions
           - Return task_parameters: "chat"
        
        === EXAMPLES ===
        Input: "What is the current price of AAPL?"
        → Domain: TACTICAL, Parameters: "AAPL"
        
        Input: "What is the price of TSLA?"
        → Domain: TACTICAL, Parameters: "TSLA"
        
        Input: "Show me the strategies"
        → Domain: TACTICAL, Parameters: "STRATEGY"
        
        Input: "What's new in AI?"
        → Domain: INTEL, Parameters: "AI"
        
        Input: "Hi, how are you?"
        → Domain: FOUNDATION, Parameters: "chat"
        
        === INSTRUCTION ===
        For ANY question asking about a stock price, ticker, or market data, route to TACTICAL with the ticker symbol as the parameter.
        Do NOT use STRATEGY unless user explicitly mentions strategies or playbooks.
        
        Return the decision structured correctly.
        """
        try:
            return self.llm.ask_structured(prompt, DomainDecision)
        except Exception:
            return DomainDecision(domain_name="FOUNDATION", reasoning="Error", task_parameters="")

    # --- DEPARTMENT HANDLERS ---
    
    def _run_tactical(self, params: str) -> str:
        """Handles Trading & Market Data."""
        from cobalt_agent.brain.tactical import Strategos
        try:
            # Clean up params
            # If the LLM sends "STRATEGY" or "PLAYBOOK", we pass it raw.
            # If it sends a ticker "NVDA", we clean it.
            if "STRATEGY" in params.upper() or "PLAYBOOK" in params.upper():
                task = "STRATEGY"
            else:
                task = params.split()[0].strip(".,!?")
                
            department_head = Strategos()
            return department_head.run(task)
        except Exception as e:
            return f"Tactical Error: {e}"

    def _run_intel(self, params: str) -> str:
        """Handles Research & Briefings."""
        if "briefing" in params.lower():
            from cobalt_agent.skills.productivity.briefing import MorningBriefing
            return MorningBriefing().run()
        else:
            from cobalt_agent.skills.research.deep_dive import DeepResearch
            return DeepResearch().run(params)

    def _run_ops(self, params: str, original_input: str) -> str:
        """
        Handles Operations (Scribe, Medical, Scheduling).
        """
        from cobalt_agent.skills.productivity.scribe import Scribe
        scribe = Scribe()
        
        prompt_lower = original_input.lower()
        
        # 1. LOGGING
        if "log" in prompt_lower or "journal" in prompt_lower:
            content = original_input.replace("log", "").replace("journal", "").strip()
            if not content: return "Please provide text to log."
            return scribe.append_to_daily_note(content)
            
        # 2. SAVING (New Note)
        elif "save" in prompt_lower or "note" in prompt_lower:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            filename = f"AutoNote_{timestamp}" 
            content = params if len(params) > 5 else original_input
            return scribe.write_note(filename, content, folder="0 - Inbox")
            
        # 3. SEARCHING
        elif "search" in prompt_lower or "find" in prompt_lower:
            # Use the LLM extracted param for the query
            results = scribe.search_vault(params)
            if not results: return "No notes found."
            return f"🔍 Found these notes:\n- " + "\n- ".join(results)
            
        # 4. MEDICAL (Placeholder for future Steward logic)
        elif "medical" in prompt_lower or "billing" in prompt_lower:
             return "🏥 Medical Admin module is not yet implemented. (See Ops Department Plan)"
             
        return "Ops processed the request."