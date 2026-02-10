"""
The Cortex (The Dispatcher)
Decides which Persona or Skill should handle the user's request.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from loguru import logger

# Import Skills
from cobalt_agent.skills.productivity.scribe import Scribe
from cobalt_agent.tools.finance import FinanceTool  # <--- NEW IMPORT

class Cortex:
    """
    The Central Nervous System of the Agent.
    Routes prompts to the correct specialist.
    """
    
    def __init__(self):
        # Initialize Capabilities (The "Hands")
        self.scribe = Scribe()
        self.finance = FinanceTool() # <--- INITIALIZE TRADER
        
        # Define keywords that trigger specific personas
        self.intent_triggers = {
            "scribe": ["save", "log", "record", "note", "obsidian", "remind", "journal"],
            "trader": ["price", "buy", "sell", "chart", "trend", "volume", "rsi", "stock"] # Added 'stock'
        }

    def route(self, prompt: str) -> str:
        """
        Analyzes the prompt and executes the correct skill.
        Returns the result string.
        """
        intent = self._detect_intent(prompt)
        
        if intent == "scribe":
            return self._handle_scribe(prompt)
        elif intent == "trader":
            return self._handle_trader(prompt) # <--- CALL THE NEW HANDLER
        else:
            return None # Return None implies "Pass to General LLM"

    def _detect_intent(self, prompt: str) -> str:
        """Simple keyword matching to guess intent."""
        prompt_lower = prompt.lower()
        
        for intent, keywords in self.intent_triggers.items():
            if any(k in prompt_lower for k in keywords):
                return intent
        return "general"

    def _handle_scribe(self, prompt: str) -> str:
        """Logic for the Scribe Persona."""
        prompt_lower = prompt.lower()
        
        # 1. LOGGING (Append to daily note)
        if "log" in prompt_lower or "journal" in prompt_lower:
            # Clean the prompt (remove "log this")
            content = prompt.replace("log", "").replace("journal", "").strip()
            if not content: return "Please provide text to log."
            return self.scribe.append_to_daily_note(content)
            
        # 2. SAVING (Create new note)
        elif "save" in prompt_lower or "note" in prompt_lower:
            # Heuristic: First 5 words are title? 
            # For now, let's just save to "Inbox"
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            filename = f"AutoNote_{timestamp}" 
            return self.scribe.write_note(filename, prompt, folder="0 - Inbox")
            
        # 3. SEARCHING
        elif "search" in prompt_lower or "find" in prompt_lower:
            query = prompt.replace("search", "").replace("find", "").strip()
            results = self.scribe.search_vault(query)
            return f"🔍 Found these notes:\n- " + "\n- ".join(results)
            
        return "I'm not sure what you want the Scribe to do (Log/Save/Search)."

    def _handle_trader(self, prompt: str) -> str:
        """Logic for the Trader Persona (Rule-Based Ticker Extraction)."""
        # 1. Clean the prompt to find the Ticker
        # Heuristic: Look for uppercase words that are 1-5 chars long
        words = prompt.split()
        candidates = []
        
        ignore_words = ["PRICE", "STOCK", "CHECK", "WHAT", "IS", "THE", "OF", "FOR", "CHART", "VOLUME", "TREND", "RSI"]
        
        for w in words:
            # Strip punctuation like "NVDA?" or "NVDA."
            clean_w = w.upper().strip("?.!,")
            if clean_w in ignore_words:
                continue
            # Tickers are usually 1-5 chars (e.g. F, AAPL, GOOGL)
            if 1 <= len(clean_w) <= 5 and clean_w.isalpha():
                candidates.append(clean_w)
        
        if not candidates:
            return "📉 I couldn't identify a stock ticker. Try 'price of NVDA'."
            
        ticker = candidates[0] # Pick the first valid candidate
        
        # 2. Call the Finance Tool
        try:
            # The FinanceTool.run method takes the ticker
            result = self.finance.run(ticker)
            return f"📈 [Trader]: {result}"
        except Exception as e:
            logger.error(f"Trader Error: {e}")
            return f"❌ Trading Engine Error: {e}"