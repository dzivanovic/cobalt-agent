"""
Cobalt Scheduler Service
Background job scheduler for automated tasks like Morning Briefing.
"""
import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger
from cobalt_agent.llm import LLM
from cobalt_agent.config import get_config


class CobaltScheduler:
    """
    Background scheduler for automated tasks.
    HandlesMorning Briefing generation and delivery.
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
        """
        logger.info("☀️ Running Automated Morning Briefing...")
        
        today_str = datetime.now().strftime("%B %d, %Y")
        
        # Load prompt from config
        prompt_template = self.config.prompts.scheduler.morning_briefing
        prompt = prompt_template.format(today_str=today_str)

        try:
            # Explicitly force the researcher profile (Gemini 3.1 Pro)
            research_llm = LLM(role="researcher")
            
            logger.info("Calling Gemini 3.1 Pro for market data...")
            report_content = research_llm.ask(
                system_message="You are a senior financial analyst and day trader. You have access to real-time data. Output strictly in the requested markdown format.",
                user_input=prompt
            )
            
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