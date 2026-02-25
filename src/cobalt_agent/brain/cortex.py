"""
The Cortex (Manager Agent) - Config-Driven Architecture
Routes user intent based on domains defined in config.yaml.
Includes robust error handling, full Scribe logic, and Medical Admin placeholders.
"""
import re
import json
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field
from loguru import logger

from cobalt_agent.llm import LLM
from cobalt_agent.config import load_config
from cobalt_agent.core.proposals import Proposal

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

        # === DETERMINISTIC FAST-PATH ROUTING (TRIAGE) ===
        message_lower = user_input.lower()
        
        # 1. Engineering / Code Triage
        eng_keywords = ["engineering", "directory", "file", "codebase", "src/", "list the"]
        if any(keyword in message_lower for keyword in eng_keywords):
            logger.info("⚡ Fast-Path Routing Triggered: ENGINEERING")
            from cobalt_agent.brain.engineering import EngineeringDepartment
            forge = EngineeringDepartment()
            return forge.run(user_input)
            
        # 2. Web / Research Triage
        web_keywords = ["http://", "https://", "browser", "scrape", "search", "summarize the top"]
        if any(keyword in message_lower for keyword in web_keywords):
            logger.info("⚡ Fast-Path Routing Triggered: DEFAULT")
            return None  # Handle in main chat loop (same as FOUNDATION)
        
        # 2. Classify
        decision = self._classify_domain(user_input)
        
        # --- PRIME DIRECTIVE GATE ---
        high_risk_keywords = ['delete', 'move', 'remove', 'format', 'execute', 'kill', 'reorganize']
        is_high_risk = any(word in user_input.lower() for word in high_risk_keywords)
        
        if is_high_risk:
            logger.warning(f"🛡️ Security Intercept: High-risk action detected in input: {user_input}")
            return self._generate_proposal(user_input)
        # ----------------------
        
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
            from cobalt_agent.brain.engineering import EngineeringDepartment
            forge = EngineeringDepartment()
            return forge.run(params)
            
        elif domain == "DEFAULT":
            return None # Handle in main chat loop (same as FOUNDATION)
            
        elif domain == "FOUNDATION":
            return None # Handle in main chat loop
            
        else:
            return f"⚠️ Unknown Domain: {domain}"

    def _generate_proposal(self, user_input: str) -> str:
        prompt = f"""
        [SECURITY PROTOCOL: PRIME DIRECTIVE]
        High-risk action detected: "{user_input}"
        
        You are the Chief of Staff. You are FORBIDDEN from executing this autonomously.
        Generate a JSON response explaining the risk.
        
        OUTPUT FORMAT:
        {{
          "action": "Summary of what was requested",
          "justification": "Why the user wants this",
          "risk_assessment": "Blunt warning about data loss or system instability"
        }}
        
        OUTPUT ONLY JSON. NO EXTRA TEXT.
        """
        
        raw_response = ""
        try:
            # Bypass ask_structured to avoid schema confusion; use base ask/generate
            raw_response = self.llm.ask(prompt)
            
            # Bulletproof JSON extraction
            match = re.search(r'\{.*\}', raw_response, re.DOTALL)
            if not match:
                raise ValueError("No JSON block found in LLM response.")
                
            data = json.loads(match.group(0))
            
            # Manually instantiate the Proposal (task_id and timestamp will auto-generate)
            proposal = Proposal(
                action=data.get("action", "Unknown Action"),
                justification=data.get("justification", "User requested high-stakes operation."),
                risk_assessment=data.get("risk_assessment", "High risk of system modification.")
            )
            return proposal.format_for_mattermost()
            
        except Exception as e:
            logger.error(f"Proposal Generation Failed: {e} | Raw Output: {raw_response}")
            return (
                f"### 🛡️ SECURITY INTERCEPT\n"
                f"**Action Blocked:** Administrative system change.\n\n"
                f"**Reason:** The Proposal Engine could not validate the risk assessment. "
                f"Execution is denied by default per the Prime Directive."
            )

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
        
        # STRICT MUTUALLY EXCLUSIVE ROUTING PROMPT
        prompt = f"""
        You are the Chief of Staff (Cortex). Route this user request to the correct Department.
        
        USER REQUEST: "{user_input}"
        
        ACTIVE DEPARTMENTS:
        {options_text}
        - DEFAULT: General chat, web research, web browsing, article summarization. Use for queries that don't fit other domains.
        
        === STRICT ROUTING RULES (MUST FOLLOW) ===
        1. WEB RESEARCH / DEFAULT ROUTING:
           - If the user asks to browse a website, scrape a URL, summarize an article, or perform general web research, you MUST return 'DEFAULT'.
           - Examples: "What's the weather in Paris?", "Summarize this article", "Look up recent news", "Research X", "Browse Y"
        
        2. TACTICAL (TRADING ONLY - STRICTLY RESTRICTED):
           - ONLY return 'TACTICAL' if the user explicitly mentions trading, stocks, tickers, playbooks, or expected value (EV).
           - Valid examples: "What is AAPL trading at?", "TSLA stock price", "Show me playbooks", "Calculate EV for X"
           - Extract ONLY the ticker symbol (e.g. "NVDA", "AAPL") or "STRATEGY" as task_parameters
        
        3. INTEL (Research/News):
           - Use for: news, deep dives, current events (non-trading focused)
           - Extract the search topic as task_parameters
        
        4. OPS (Operations/Scribe):
           - Use for: logging, journaling, saving notes, medical billing
           - Extract relevant content as task_parameters
        
        5. ENGINEERING (CODE WORK - STRICTLY RESTRICTED):
           - ONLY return 'ENGINEERING' if the user explicitly asks to write, edit, or review code.
           - Examples: "Write a function", "Fix this bug", "Review my code", "Create a new tool"
        
        6. DEFAULT:
           - Use for: general conversation, greetings, system questions, or anything not matching the above
           - Return task_parameters: "chat"
        
        === EXAMPLES ===
        Input: "What is the current price of AAPL?"
        → Domain: TACTICAL, Parameters: "AAPL"
        
        Input: "What is the price of TSLA?"
        → Domain: TACTICAL, Parameters: "TSLA"
        
        Input: "Show me the strategies/playbooks"
        → Domain: TACTICAL, Parameters: "STRATEGY"
        
        Input: "What is the expected value of X given Y?"
        → Domain: TACTICAL, Parameters: "STRATEGY"
        
        Input: "Browse https://example.com and summarize it"
        → Domain: DEFAULT, Parameters: "chat"
        
        Input: "Summarize this article about AI"
        → Domain: DEFAULT, Parameters: "chat"
        
        Input: "Write a Python function to do X"
        → Domain: ENGINEERING, Parameters: "Python function: X"
        
        Input: "Fix the routing bug in cortex.py"
        → Domain: ENGINEERING, Parameters: "Fix routing bug in cortex.py"
        
        Input: "What's the weather like?"
        → Domain: DEFAULT, Parameters: "chat"
        
        Input: "Hi, how are you?"
        → Domain: DEFAULT, Parameters: "chat"
        
        === FINAL INSTRUCTION ===
        FOLLOW THESE RULES STRICTLY AND MUTUALLY EXCLUSIVELY:
        1. Web research/browser/URL/summary queries → DEFAULT
        2. Trading/stocks/tickers/playbooks/EV → TACTICAL
        3. Writing/editing/reviewing code → ENGINEERING
        4. Everything else → DEFAULT
        
        Return the decision structured correctly. DO NOT DEVIATE FROM THESE RULES.
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