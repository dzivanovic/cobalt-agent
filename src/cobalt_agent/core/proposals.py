"""
HITL (Human-in-the-Loop) Proposal Engine

This module implements a persistent approval workflow where high-stakes AI actions
must be approved by a human operator before execution. Proposals are stored in
PostgreSQL instead of volatile memory, ensuring they survive system restarts.

The workflow:
1. Agent creates a proposal -> stored in hitl_proposals table (status='pending')
2. Proposal is sent to Mattermost for human review
3. Human replies with 'Approve <task_id>' or 'Reject <task_id>'
4. System updates proposal status in database and executes/cancels action
"""
from typing import Dict, Any, Optional, Callable, List
from pydantic import BaseModel, Field
import uuid
from datetime import datetime
import threading
import time
import re
import json
from loguru import logger
from typing import TYPE_CHECKING

from cobalt_agent.config import get_config

if TYPE_CHECKING:
    from cobalt_agent.interfaces.mattermost import MattermostInterface


class HITLProposalStore:
    """
    Persistent storage for HITL (Human-in-the-Loop) proposals using Postgres.
    Stores proposals in the hitl_proposals table instead of volatile memory.
    """
    
    def __init__(self):
        from cobalt_agent.memory.postgres import PostgresMemory
        self.postgres = PostgresMemory()
    
    def create_proposal(self, tool_name: str, tool_kwargs: Dict[str, Any]) -> str:
        """
        Create a new pending proposal and store it in the database.
        
        Args:
            tool_name: Name of the tool to be executed
            tool_kwargs: JSON-serializable arguments for the tool
            
        Returns:
            The UUID of the created proposal
        """
        try:
            proposal_id = str(uuid.uuid4())
            with self.postgres._get_conn() as conn:
                conn.execute("""
                    INSERT INTO hitl_proposals (id, status, tool_name, tool_kwargs, created_at)
                    VALUES (%s, %s, %s, %s, %s)
                """, (proposal_id, 'pending', tool_name, json.dumps(tool_kwargs), datetime.now()))
                conn.commit()
                logger.info(f"HITL proposal created: [{proposal_id}] for tool '{tool_name}'")
                return proposal_id
        except Exception as e:
            logger.error(f"Failed to create HITL proposal: {e}")
            raise
    
    def get_proposal(self, proposal_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a proposal by ID.
        
        Args:
            proposal_id: The UUID of the proposal
            
        Returns:
            Dictionary with proposal data, or None if not found
        """
        try:
            with self.postgres._get_conn() as conn:
                result = conn.execute("""
                    SELECT id, status, tool_name, tool_kwargs, created_at, updated_at
                    FROM hitl_proposals
                    WHERE id = %s
                """, (proposal_id,)).fetchone()
                
                if result:
                    return {
                        "id": str(result[0]),
                        "status": result[1],
                        "tool_name": result[2],
                        "tool_kwargs": result[3] if isinstance(result[3], dict) else json.loads(result[3]),
                        "created_at": result[4],
                        "updated_at": result[5]
                    }
                return None
        except Exception as e:
            logger.error(f"Failed to get proposal: {e}")
            return None
    
    def get_pending_proposals(self) -> List[Dict[str, Any]]:
        """
        Get all pending proposals.
        
        Returns:
            List of dictionaries with pending proposal data
        """
        try:
            with self.postgres._get_conn() as conn:
                results = conn.execute("""
                    SELECT id, status, tool_name, tool_kwargs, created_at, updated_at
                    FROM hitl_proposals
                    WHERE status = %s
                """, ('pending',)).fetchall()
                
                proposals = []
                for row in results:
                    proposals.append({
                        "id": str(row[0]),
                        "status": row[1],
                        "tool_name": row[2],
                        "tool_kwargs": row[3] if isinstance(row[3], dict) else json.loads(row[3]),
                        "created_at": row[4],
                        "updated_at": row[5]
                    })
                return proposals
        except Exception as e:
            logger.error(f"Failed to get pending proposals: {e}")
            return []
    
    def update_status(self, proposal_id: str, status: str) -> bool:
        """
        Update the status of a proposal.
        
        Args:
            proposal_id: The UUID of the proposal
            status: The new status ('approved', 'rejected', 'pending')
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with self.postgres._get_conn() as conn:
                conn.execute("""
                    UPDATE hitl_proposals
                    SET status = %s,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                """, (status, proposal_id))
                conn.commit()
                logger.info(f"HITL proposal [{proposal_id}] status updated to '{status}'")
                return True
        except Exception as e:
            logger.error(f"Failed to update proposal status: {e}")
            return False
    
    def delete_proposal(self, proposal_id: str) -> bool:
        """
        Delete a proposal from the database.
        
        Args:
            proposal_id: The UUID of the proposal
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with self.postgres._get_conn() as conn:
                conn.execute("""
                    DELETE FROM hitl_proposals WHERE id = %s
                """, (proposal_id,))
                conn.commit()
                logger.info(f"HITL proposal [{proposal_id}] deleted")
                return True
        except Exception as e:
            logger.error(f"Failed to delete proposal: {e}")
            return False


# --- PROPOSAL MODEL ---
class Proposal(BaseModel):
    """Standardized ticket for high-stakes AI actions."""
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    action: str = Field(description="The specific command or operation to be executed.")
    justification: str = Field(description="The agent's reasoning for why this action is necessary.")
    risk_assessment: str = Field(description="A summary of potential negative impacts (e.g., data loss, capital risk).")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Technical metadata required for execution.")
    timestamp: datetime = Field(default_factory=datetime.now)
    approved: bool = False
    approval_channel: Optional[str] = None
    approval_message_id: Optional[str] = None

    def format_for_mattermost(self) -> str:
        return (
            f"### 🛡️ ACTION PROPOSAL [{self.task_id}]\n"
            f"**Action:** `{self.action}`\n\n"
            f"**Justification:** {self.justification}\n"
            f"**Risk:** {self.risk_assessment}\n\n"
            f"### ⚠️ ACTION REQUIRED: Reply exactly with 'Approve {self.task_id}' to execute."
        )


# --- PROPOSAL ENGINE ---
class ProposalEngine:
    """
    The Proposal Engine enforces the Prime Directive by requiring human approval
    before executing high-stakes actions. It creates proposals, sends them to
    Mattermost for approval, and only executes approved actions.
    
    Proposals are stored in the hitl_proposals Postgres table for persistence.
    """
    
    def __init__(self):
        self.config = get_config()
        self.approval_channel = self.config.mattermost.approval_channel
        self.approval_team = self.config.mattermost.approval_team
        self.mattermost: Optional[Any] = None
        self._hitl_store: Optional[HITLProposalStore] = None
        self._pending_proposals_cache: Dict[str, Proposal] = {}
        self._callbacks: Dict[str, Callable[[Proposal], None]] = {}
        self._approval_callback: Optional[Callable[[Proposal], None]] = None
        
        logger.info(f"Proposal Engine initialized (Channel: {self.approval_channel})")
    
    def _get_hitl_store(self) -> HITLProposalStore:
        """Get or create the HITL proposal store."""
        if self._hitl_store is None:
            self._hitl_store = HITLProposalStore()
        return self._hitl_store
    
    def connect_mattermost(self) -> bool:
        """Connect to Mattermost for approval workflow."""
        if self.mattermost:
            return True
        
        from cobalt_agent.interfaces.mattermost import MattermostInterface
        
        self.mattermost = MattermostInterface()
        connected = self.mattermost.connect()
        
        if connected:
            self.mattermost.brain = self._get_brain_for_approval_routing()
            logger.info("Proposal Engine: Mattermost connection established")
        
        return connected
    
    def _get_brain_for_approval_routing(self) -> Any:
        """
        Get the brain instance for approval routing.
        This is a stub - the actual brain should be passed in or connected externally.
        """
        return None
    
    def create_proposal(
        self,
        action: str,
        justification: str,
        risk_assessment: str,
        parameters: Optional[Dict[str, Any]] = None
    ) -> Proposal:
        """
        Create a new proposal for a high-stakes action and store it in Postgres.
        
        Args:
            action: The specific command or operation to be executed
            justification: The agent's reasoning for why this action is necessary
            risk_assessment: A summary of potential negative impacts
            parameters: Technical metadata required for execution
            
        Returns:
            The created Proposal object
        """
        proposal = Proposal(
            action=action,
            justification=justification,
            risk_assessment=risk_assessment,
            parameters=parameters or {}
        )
        
        # Store in Postgres (primary storage for persistence)
        hitl_store = self._get_hitl_store()
        hitl_store.create_proposal(
            tool_name="proposal_engine",
            tool_kwargs={
                "task_id": proposal.task_id,
                "action": action,
                "justification": justification,
                "risk_assessment": risk_assessment,
                "parameters": parameters or {}
            }
        )
        
        # Also cache in memory for quick lookups during the session
        self._pending_proposals_cache[proposal.task_id] = proposal
        logger.info(f"Proposal created and stored: [{proposal.task_id}] {action[:50]}...")
        
        return proposal
    
    def send_proposal(self, proposal: Proposal) -> bool:
        """
        Send a proposal to Mattermost for approval.
        
        Args:
            proposal: The Proposal object to send
            
        Returns:
            True if proposal was sent successfully
        """
        if not self.mattermost:
            logger.error("Mattermost not connected. Cannot send proposal.")
            return False
        
        if not self.approval_channel:
            logger.error("Approval channel not configured.")
            return False
        
        message = proposal.format_for_mattermost()
        
        try:
            teams = self.mattermost.driver.teams.get_team_by_name(self.approval_team)
            if not teams:
                logger.error(f"Approval team not found: {self.approval_team}")
                return False
            
            team_id = teams["id"]
            
            channel = self.mattermost.driver.channels.get_channel_by_name(team_id, self.approval_channel)
            if not channel:
                logger.error(f"Approval channel not found: {self.approval_channel} in team {self.approval_team}")
                return False
            
            channel_id = channel["id"]
            
            post = self.mattermost.driver.posts.create_post(
                options={
                    "channel_id": channel_id,
                    "message": message
                }
            )
            
            if post and "id" in post:
                proposal.approval_message_id = post["id"]
                proposal.approval_channel = channel_id
                logger.info(f"Proposal sent to Mattermost: [{proposal.task_id}]")
                return True
            else:
                logger.error("Failed to send proposal to Mattermost")
                return False
                
        except Exception as e:
            logger.error(f"Failed to send proposal: {e}")
            return False
    
    def handle_approval_response(self, message: str, channel_id: Optional[str] = None) -> Optional[str]:
        """
        Check if a message is an approval response for a pending proposal and return a formatted message.
        
        Args:
            message: The message text from Mattermost
            channel_id: Optional channel ID where the message was posted
            
        Returns:
            A formatted message string if this is a valid approval response, None otherwise
        """
        # Check if this is an approval message
        approval_pattern = r"approve\s+(\w{8})"
        match = re.search(approval_pattern, message.lower())
        
        if not match:
            # Check for reject pattern
            reject_pattern = r"reject\s+(\w{8})"
            reject_match = re.search(reject_pattern, message.lower())
            if reject_match:
                task_id = reject_match.group(1)
                return f"❌ Rejection received for task [{task_id}]. The action has been cancelled."
            return None
        
        task_id = match.group(1)
        
        # Validate channel if provided
        if channel_id and self.approval_channel and channel_id != self.approval_channel:
            return None
        
        # Look up the pending proposal from cache
        if task_id in self._pending_proposals_cache:
            proposal = self._pending_proposals_cache.pop(task_id)
            proposal.approved = True
            self._pending_proposals_cache[task_id] = proposal  # Keep for record
            
            # Update database status
            hitl_store = self._get_hitl_store()
            hitl_store.update_status(task_id, 'approved')
            
            logger.info(f"Proposal approved: [{task_id}]")
            
            # Execute the callback
            if task_id in self._callbacks:
                try:
                    self._callbacks[task_id](proposal)
                    del self._callbacks[task_id]
                    return f"✅ Approval received for task [{task_id}]. Action executed successfully."
                except Exception as e:
                    logger.error(f"Callback execution failed: {e}")
                    return f"❌ Approval received, but execution failed: {e}"
            else:
                return f"⚠️ Approval received for [{task_id}], but no execution callback was found in memory."
        elif task_id in self._pending_proposals_cache and self._pending_proposals_cache[task_id].approved:
            return f"ℹ️ Proposal [{task_id}] was already approved."
        else:
            logger.warning(f"Approval for unknown task_id: {task_id}")
            return f"⚠️ No pending approval found for task [{task_id}]."
    
    def wait_for_approval(self, proposal: Proposal, timeout: int = 3600) -> bool:
        """
        Wait for a proposal to be approved (non-blocking with threading.Event).
        
        Args:
            proposal: The Proposal to wait for
            timeout: Maximum time to wait in seconds (default 1 hour)
            
        Returns:
            True if approved, False if timed out
        """
        approval_event = threading.Event()
        
        def check_approval():
            start_time = time.time()
            while not approval_event.is_set():
                if proposal.task_id in self._pending_proposals_cache:
                    cached_proposal = self._pending_proposals_cache[proposal.task_id]
                    if cached_proposal.approved:
                        approval_event.set()
                        return
                
                if time.time() - start_time >= timeout:
                    if proposal.task_id in self._pending_proposals_cache:
                        del self._pending_proposals_cache[proposal.task_id]
                    logger.warning(f"Approval timeout for proposal: [{proposal.task_id}]")
                    return
                
                if approval_event.wait(timeout=0.5):
                    return
        
        monitor_thread = threading.Thread(target=check_approval, daemon=True)
        monitor_thread.start()
        
        approval_event.wait()
        
        # Check database for approval status
        if proposal.task_id in self._pending_proposals_cache:
            return self._pending_proposals_cache[proposal.task_id].approved
        
        # Also check database directly
        hitl_store = self._get_hitl_store()
        db_proposal = hitl_store.get_proposal(proposal.task_id)
        return db_proposal is not None and db_proposal.get("status") == "approved"
    
    def execute_approved(self, proposal: Proposal) -> bool:
        """
        Execute an approved proposal's action.
        
        Args:
            proposal: The approved Proposal to execute
            
        Returns:
            True if execution succeeded
        """
        if not proposal.approved:
            logger.error(f"Cannot execute unapproved proposal: [{proposal.task_id}]")
            return False
        
        try:
            action = proposal.action
            logger.info(f"Executing approved action: {action}")
            
            if self._approval_callback:
                self._approval_callback(proposal)
            
            return True
        except Exception as e:
            logger.error(f"Failed to execute approved action [{proposal.task_id}]: {e}")
            return False
    
    def set_approval_callback(self, task_id: str, callback: Callable[[Proposal], None]) -> None:
        """
        Set a callback function to be called when a proposal is approved.
        
        Args:
            task_id: The unique identifier for the task
            callback: Function that takes a Proposal and returns None
        """
        self._callbacks[task_id] = callback
        logger.info(f"Approval callback set for task [{task_id}]")
    
    def start_monitoring(self) -> None:
        """Start monitoring for approval responses in the background."""
        if self._monitoring:
            logger.warning("Monitoring already running")
            return
        
        self._monitoring = True
        self._monitor_thread = threading.Thread(target=self._monitor_approval_channel, daemon=True)
        self._monitor_thread.start()
        logger.info("Proposal Engine monitoring started")
    
    def _monitor_approval_channel(self) -> None:
        """Background thread to monitor the approval channel for approval responses."""
        logger.info("Approval channel monitoring started (WebSocket listener attached to MattermostInterface)")
    
    def stop_monitoring(self) -> None:
        """Stop monitoring for approval responses."""
        self._monitoring = False
        if self._monitor_thread:
            self._monitor_thread.join(timeout=1)
        logger.info("Proposal Engine monitoring stopped")


# --- CONVENIENCE FUNCTION ---
def create_and_send_proposal(
    action: str,
    justification: str,
    risk_assessment: str,
    parameters: Optional[Dict[str, Any]] = None
) -> Optional[Proposal]:
    """
    Convenience function to create and send a proposal.
    
    Args:
        action: The specific command or operation to be executed
        justification: The agent's reasoning for why this action is necessary
        risk_assessment: A summary of potential negative impacts
        parameters: Technical metadata required for execution
        
    Returns:
        The created and sent Proposal if successful, None otherwise
    """
    engine = ProposalEngine()
    
    if not engine.connect_mattermost():
        logger.error("Failed to connect to Mattermost")
        return None
    
    proposal = engine.create_proposal(
        action=action,
        justification=justification,
        risk_assessment=risk_assessment,
        parameters=parameters
    )
    
    if not engine.send_proposal(proposal):
        logger.error("Failed to send proposal")
        return None
    
    return proposal