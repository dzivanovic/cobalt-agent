"""
The Morning Briefing Skill
Orchestrates Tools to create a daily digest.
"""
from datetime import datetime
from loguru import logger
from cobalt_agent.skills.productivity.scribe import Scribe
from cobalt_agent.tools.finance import FinanceTool
# We need to make sure Search is importable. 
# If tools/search.py exists, this works:
from cobalt_agent.tools.search import SearchTool 

class MorningBriefing:
    def __init__(self):
        self.scribe = Scribe()
        self.finance = FinanceTool()
        self.search = SearchTool()

    def run(self):
        """Generates the daily report."""
        logger.debug("🌤️ Starting Morning Briefing generation...")
        
        today = datetime.now().strftime("%Y-%m-%d")
        report = [f"# 🌤️ Morning Briefing: {today}\n"]
        report.append(f"*Generated at: {datetime.now().strftime('%H:%M')}*\n")
        
        # --- SECTION 1: MARKETS ---
        try:
            tickers = ["NVDA", "SPY", "BTC-USD"] 
            report.append("## 📈 Market Snapshot")
            
            for t in tickers:
                # The finance tool returns a string. We'll strip it to keep it clean.
                data = self.finance.run(t)
                report.append(f"### {t}")
                report.append(str(data) + "\n") # Ensure string
                
        except Exception as e:
            logger.error(f"Failed to fetch markets: {e}")
            report.append(f"> ⚠️ Market data unavailable: {e}")

        # --- SECTION 2: NEWS ---
        try:
            report.append("## 📰 Top Headlines")
            query = "top technology and finance news today"
            logger.debug(f"Briefing searching for: {query}")
            
            results = self.search.run(query)
            
            # <--- FIX START: Handle List vs String --->
            if isinstance(results, list):
                # If it's a list, join it into a bulleted string
                formatted_news = ""
                for item in results:
                    formatted_news += f"- {str(item)}\n"
                report.append(formatted_news)
            else:
                # If it's already a string, just add it
                report.append(str(results))
            # <--- FIX END --->
            
        except Exception as e:
            logger.error(f"Failed to fetch news: {e}")
            report.append("> ⚠️ News unavailable.")

        # --- SECTION 3: SAVE TO OBSIDIAN ---
        # Now this will work because everything in 'report' is guaranteed to be a string
        final_content = "\n".join(report)
        filename = f"Briefing_{today}"
        
        path = self.scribe.write_note(filename, final_content, folder="0 - Inbox")
        
        logger.info(f"✅ Briefing saved to: {path}")
        return path