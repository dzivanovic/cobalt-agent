"""
The Morning Briefing Skill
Orchestrates Tools to create a daily digest.
Refactored to use Pydantic Models and LLM Synthesis.
"""
from datetime import datetime
from typing import List
from loguru import logger
from pydantic import BaseModel, Field

from cobalt_agent.config import load_config
from cobalt_agent.llm import LLM
from cobalt_agent.skills.productivity.scribe import Scribe
from cobalt_agent.tools.finance import FinanceTool
from cobalt_agent.tools.search import SearchTool

# --- PYDANTIC SCHEMA ---
class BriefingReport(BaseModel):
    """Structured format for the daily briefing."""
    executive_summary: str = Field(description="A concise 3-sentence summary of the overall market and news mood.")
    market_analysis: str = Field(description="A technical analysis of the provided stock data (Bullish/Bearish/Neutral).")
    top_headlines: List[str] = Field(description="A list of the 3-5 most critical news headlines found.")
    strategic_thought: str = Field(description="A single, provocative thought or question for the user based on today's events.")

# --- SKILL ---
class MorningBriefing:
    def __init__(self):
        # 1. Load Config & LLM
        config = load_config()
        # Handle model name attribute safely
        model_name = getattr(config.llm, "model_name", getattr(config.llm, "model", "gpt-4o"))
        
        self.llm = LLM(model_name=model_name)
        
        # 2. Initialize Tools
        self.scribe = Scribe()
        self.finance = FinanceTool()
        self.search = SearchTool()

    def _gather_data(self) -> str:
        """
        Runs tools to collect raw context for the LLM.
        """
        raw_data = []
        
        # A. Markets
        tickers = ["NVDA", "SPY", "BTC-USD"]
        raw_data.append("--- MARKET DATA ---")
        for t in tickers:
            try:
                data = self.finance.run(t)
                raw_data.append(f"{t}: {str(data)}")
            except Exception as e:
                logger.warning(f"Failed to fetch {t}: {e}")

        # B. News
        query = "top technology and finance news today"
        raw_data.append(f"\n--- NEWS SEARCH: '{query}' ---")
        try:
            results = self.search.run(query)
            if isinstance(results, list):
                raw_data.extend([str(item) for item in results])
            else:
                raw_data.append(str(results))
        except Exception as e:
            logger.warning(f"Failed to search news: {e}")

        return "\n".join(raw_data)

    def run(self):
        """Generates the daily report."""
        logger.debug("🌤️ Starting Morning Briefing generation...")
        
        # 1. Gather Data
        context_data = self._gather_data()
        
        # 2. Synthesize with LLM (The "Smart" Step)
        prompt = f"""
        You are a Chief of Staff. Review the raw market data and news below.
        Synthesize a structured Morning Briefing for me.
        
        RAW DATA:
        {context_data}
        """
        
        try:
            # Use the new ask_structured method from llm.py
            report: BriefingReport = self.llm.ask_structured(prompt, BriefingReport)
            
            # 3. Format as Markdown
            today = datetime.now().strftime("%Y-%m-%d")
            md_content = f"# 🌤️ Morning Briefing: {today}\n"
            md_content += f"*Generated at: {datetime.now().strftime('%H:%M')}*\n\n"
            
            md_content += f"### 🧐 Executive Summary\n{report.executive_summary}\n\n"
            
            md_content += f"### 📈 Market Pulse\n{report.market_analysis}\n\n"
            
            md_content += "### 📰 Top Headlines\n"
            for news in report.top_headlines:
                md_content += f"- {news}\n"
                
            md_content += f"\n### 💡 Strategic Thought\n> {report.strategic_thought}\n"

        except Exception as e:
            logger.error(f"Briefing synthesis failed: {e}")
            # Fallback if LLM fails
            md_content = f"# Briefing Failed\nCould not generate structured report.\n\nRaw Data:\n{context_data}"
            filename = f"Briefing_Failed_{datetime.now().strftime('%Y-%m-%d')}"

        # 4. Save to Obsidian
        filename = f"Briefing_{datetime.now().strftime('%Y-%m-%d')}"
        path = self.scribe.write_note(filename, md_content, folder="0 - Inbox")
        
        logger.info(f"✅ Briefing saved to: {path}")
        return path