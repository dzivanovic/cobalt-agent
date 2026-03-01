"""
Cobalt Watcher Daemon - Scheduled Web Monitoring System

This module provides the DaemonTool for scheduling recurring web watchers,
and the background job execution logic that monitors URLs and detects changes.

Features:
- APScheduler integration for background job scheduling
- Watcher jobs that fetch URLs and compute deltas
- Mattermost interrupt system for alerts on new entities
- Dual-Path Agentic/Human web logic via BrowserTool
"""
import uuid
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from loguru import logger
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job as APSchedulerJob

from ..tools.browser import BrowserTool
from ..tools.extractor import UniversalExtractor, compute_delta, DeltaResult
from ..memory.postgres import PostgresMemory
from ..interfaces.mattermost import MattermostInterface
from ..config import get_config


class ScheduleWatcherInput(BaseModel):
    """Pydantic input schema for scheduling a watcher job."""
    url: str = Field(..., description="The URL to monitor")
    interval_minutes: int = Field(..., ge=1, description="Interval in minutes between checks")
    intent: str = Field(..., description="The intent or purpose of this watcher")


class ListWatchersInput(BaseModel):
    """Pydantic input schema for listing watcher jobs (empty - no input needed)."""
    pass


class StopWatcherInput(BaseModel):
    """Pydantic input schema for stopping a watcher job."""
    job_id: str = Field(..., description="The ID of the job to stop")


class DaemonTool:
    """
    DaemonTool for managing scheduled web watchers.
    
    Provides a Pydantic-based interface for the LLM to schedule,
    list, and stop recurring background jobs using APScheduler.
    """
    
    def __init__(self):
        """Initialize the DaemonTool with scheduler and dependencies."""
        self.scheduler = BackgroundScheduler()
        self.config = get_config()
        self._postgres_memory: Optional[PostgresMemory] = None
        
        # Try to initialize PostgresMemory if available
        try:
            self._postgres_memory = PostgresMemory()
            logger.info("✅ DaemonTool: PostgresMemory initialized")
        except Exception as e:
            logger.warning(f"⚠️ DaemonTool: PostgresMemory initialization skipped: {e}")
            self._postgres_memory = None
        
        self.browser_tool = BrowserTool()
        self.extractor = UniversalExtractor()
        self._registered_jobs: Dict[str, Dict] = {}
        
    def start(self) -> None:
        """Start the background scheduler."""
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("⏱️ DaemonTool: Scheduler started")
    
    def stop(self) -> None:
        """Stop the background scheduler."""
        if self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("⏹️ DaemonTool: Scheduler stopped")
    
    def schedule_watcher(self, url: str, interval_minutes: int, intent: str) -> str:
        """
        Schedule a new watcher job to run at the specified interval.
        
        Args:
            url: The URL to monitor
            interval_minutes: How often to check the URL (in minutes)
            intent: The purpose/description of this watcher
            
        Returns:
            The job ID for the newly scheduled job
        """
        # Generate a unique job ID
        job_id = f"watcher_{uuid.uuid4().hex[:8]}"
        
        # Store job metadata
        self._registered_jobs[job_id] = {
            "url": url,
            "interval_minutes": interval_minutes,
            "intent": intent
        }
        
        # Schedule the job with APScheduler
        self.scheduler.add_job(
            _run_watcher_job,
            'interval',
            minutes=interval_minutes,
            id=job_id,
            replace_existing=True,
            args=[url, intent, self._postgres_memory]
        )
        
        logger.info(f"⏰ DaemonTool: Scheduled watcher job '{job_id}' for {url} every {interval_minutes} minutes")
        return job_id
    
    def list_watchers(self) -> List[Dict]:
        """
        List all active background jobs.
        
        Returns:
            List of dictionaries containing job information
        """
        jobs = self.scheduler.get_jobs()
        
        job_info = []
        for job in jobs:
            info = {
                "job_id": job.id,
                "next_run_time": str(job.next_run_time),
                "trigger": str(job.trigger),
                "is_running": job.next_run_time is not None
            }
            
            # Add registered job metadata if available
            if job.id in self._registered_jobs:
                info.update(self._registered_jobs[job.id])
            
            job_info.append(info)
        
        logger.info(f"📋 DaemonTool: Listed {len(job_info)} watcher jobs")
        return job_info
    
    def stop_watcher(self, job_id: str) -> bool:
        """
        Cancel an active watcher job.
        
        Args:
            job_id: The ID of the job to stop
            
        Returns:
            True if the job was found and stopped, False otherwise
        """
        try:
            self.scheduler.remove_job(job_id)
            if job_id in self._registered_jobs:
                del self._registered_jobs[job_id]
            
            logger.info(f"⏹️ DaemonTool: Stopped watcher job '{job_id}'")
            return True
        except Exception as e:
            logger.error(f"Failed to stop watcher job '{job_id}': {e}")
            return False


def _run_watcher_job(url: str, intent: str, postgres_memory: Optional[PostgresMemory] = None) -> None:
    """
    Background job function that runs a watcher check.
    
    This function is executed by APScheduler on the configured interval.
    It fetches the URL content, computes the delta against existing graph data,
    and triggers a Mattermost alert if new entities are detected.
    
    Args:
        url: The URL to monitor
        intent: The purpose/description of this watcher
        postgres_memory: Optional PostgresMemory instance for delta computation
    """
    logger.info(f"🕵️ Watcher Job: Checking {url} (intent: {intent})")
    
    try:
        # Step 1: Fetch content from URL using BrowserTool
        # Use a simple URL query (no actions for basic scraping)
        browser_result = BrowserTool().run(query=url)
        
        if browser_result.error:
            logger.error(f"Watcher Job: Failed to fetch {url}: {browser_result.error}")
            return
        
        logger.info(f"Watcher Job: Fetched content from {url} (title: {browser_result.title})")
        
        # Step 2: Extract graph entities and compute delta
        delta = compute_delta([], [], postgres_memory)  # Initialize delta computation
        
        # Extract entities from the content
        extraction_result = UniversalExtractor().extract(browser_result.content)
        
        # Compute delta with the extracted entities
        delta_payload = compute_delta(
            extraction_result.nodes,
            extraction_result.edges,
            postgres_memory
        )
        
        # Step 3: Evaluate delta and trigger alert if needed
        if not delta_payload.get("new_edges") and not delta_payload.get("new_nodes"):
            # Silent operation - no new entities
            logger.info(f"Watcher Job: No new entities detected at {url}")
            return
        
        # New entities detected - trigger Mattermost interrupt
        _send_watcher_alert(url, intent, delta_payload)
        
    except Exception as e:
        logger.exception(f"Watcher Job: Error running watcher for {url}: {e}")


def _send_watcher_alert(url: str, intent: str, delta_payload: Dict) -> None:
    """
    Send a high-priority Mattermost alert for watcher detection.
    
    Args:
        url: The URL where new entities were detected
        intent: The watcher intent
        delta_payload: The delta result containing new nodes and edges
    """
    try:
        mm = MattermostInterface()
        if not mm.connect():
            logger.error("Failed to connect to Mattermost for watcher alert")
            return
        
        # Build the alert message
        alert_title = f"🚨 **Watcher Alert** [{url}]"
        alert_message = f"{alert_title}\n\nNew entities detected based on intent '{intent}'."
        
        # Add markdown summary of new edges
        new_edges = delta_payload.get("new_edges", [])
        new_nodes = delta_payload.get("new_nodes", [])
        
        if new_edges:
            alert_message += "\n\n### New Edges Detected:\n"
            for edge in new_edges:
                source = edge.get("source_name", "unknown")
                target = edge.get("target_name", "unknown")
                relationship = edge.get("relationship", "unknown")
                alert_message += f"- **{source}** ──[{relationship}]──> **{target}**\n"
        
        if new_nodes:
            alert_message += "\n### New Nodes Detected:\n"
            for node in new_nodes:
                entity_type = node.get("entity_type", "unknown")
                name = node.get("name", "unknown")
                alert_message += f"- `{entity_type}`: **{name}**\n"
        
        alert_message += "\n---\n*This is an automated alert from the Watcher Daemon.*"
        
        # Send to mattermost
        mm.send_message("town-square", mm.config.approval_team, alert_message)
        mm.disconnect()
        
        logger.info(f"🚨 Watcher Alert: Sent Mattermost notification for {url}")
        
    except Exception as e:
        logger.exception(f"Failed to send watcher alert: {e}")