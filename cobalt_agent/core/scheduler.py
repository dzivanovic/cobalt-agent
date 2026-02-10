"""
Scheduler Module
Gives Cobalt a sense of time and allows for autonomous tasks.
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from loguru import logger
from datetime import datetime

class AgentScheduler:
    """
    Manages timed tasks for the agent.
    """
    
    def __init__(self, cortex):
        self.scheduler = BackgroundScheduler()
        self.cortex = cortex # We need access to the Brain to do things!
        self.running = False

    def start(self):
        """Start the internal clock."""
        if not self.running:
            self.scheduler.start()
            self.running = True
            logger.info("Scheduler started (Time Awareness Online)")
            
            # Example: Add a simple heartbeat job (runs every 30 mins)
            # self.add_job(self._heartbeat, "interval", minutes=30)

    def stop(self):
        """Stop the clock."""
        if self.running:
            self.scheduler.shutdown()
            self.running = False
            logger.info("Scheduler stopped")

    def add_job(self, func, trigger_type, **kwargs):
        """
        Add a new task.
        trigger_type: 'cron', 'interval', or 'date'
        kwargs: e.g. hour=9, minute=30 (for cron) or minutes=15 (for interval)
        """
        try:
            self.scheduler.add_job(func, trigger_type, **kwargs)
            logger.info(f"Scheduled task added: {func.__name__} ({trigger_type})")
        except Exception as e:
            logger.error(f"Failed to schedule task: {e}")

    def _heartbeat(self):
        """A simple task to prove it's working."""
        logger.info(f"♥ System Heartbeat: {datetime.now()}")