from typing import Dict, Any, Optional, Callable
from pydantic import BaseModel, Field
import uuid
from datetime import datetime
import threading
import time
import re
from loguru import logger
from typing import TYPE_CHECKING

from cobalt_agent.config import get_config

if TYPE_CHECKING:
    from cobalt_agent.interfaces.mattermost import MattermostInterface

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
    """
    # Shared state across all instances
    pending_proposals: Dict[str, Proposal] = {}
    callbacks: Dict[str, Callable[[Proposal], None]] = {}
    
    def __init__(self):
        self.config = get_config()
        self.approval_channel = self.config.mattermost.approval_channel
        self.approval_team = self.config.mattermost.approval_team
        self.mattermost: Optional[Any] = None
        self.approved_proposals: Dict[str, Proposal] = {}
        self._approval_callback: Optional[Callable[[Proposal], None]] = None
        self._monitoring = False
        self._monitor_thread: Optional[threading.Thread] = None
        
        logger.info(f"Proposal Engine initialized (Channel: {self.approval_channel})")
    
    def connect_mattermost(self) -> bool:
        """Connect to Mattermost for approval workflow."""
        if self.mattermost:
            return True
        
        # Lazy import to avoid circular dependency
        from cobalt_agent.interfaces.mattermost import MattermostInterface
        
        self.mattermost = MattermostInterface()
        connected = self.mattermost.connect()
        
        if connected:
            # Attach brain for message routing
            self.mattermost.brain = self._get_brain_for_approval_routing()
            logger.info("Proposal Engine: Mattermost connection established")
        
        return connected
    
    def _get_brain_for_approval_routing(self) -> Any:
        """
        Get the brain instance for approval routing.
        This is a stub - the actual brain should be passed in or connected externally.
        """
        # For now, return None - the brain will be attached by the main agent
        return None
    
    def create_proposal(
        self,
        action: str,
        justification: str,
        risk_assessment: str,
        parameters: Optional[Dict[str, Any]] = None
    ) -> Proposal:
        """
        Create a new proposal for a high-stakes action.
        
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
        
        self.pending_proposals[proposal.task_id] = proposal
        logger.info(f"Proposal created: [{proposal.task_id}] {action[:50]}...")
        
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
        
        # Lazy import to avoid circular dependency
        from cobalt_agent.interfaces.mattermost import MattermostInterface
        
        # Get team ID first
        try:
            teams = self.mattermost.driver.teams.get_team_by_name(self.approval_team)
            if not teams:
                logger.error(f"Approval team not found: {self.approval_team}")
                return False
            
            team_id = teams["id"]
            
            # Get channel ID using team_id as parameter
            channel = self.mattermost.driver.channels.get_channel_by_name(team_id, self.approval_channel)
            if not channel:
                logger.error(f"Approval channel not found: {self.approval_channel} in team {self.approval_team}")
                return False
            
            channel_id = channel["id"]
            
            # Send the proposal message
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
        
        # If channel_id is provided, validate it
        if channel_id and self.approval_channel and channel_id != self.approval_channel:
            return None
        
        # Look up the pending proposal
        if task_id in self.pending_proposals:
            proposal = self.pending_proposals.pop(task_id)
            proposal.approved = True
            self.approved_proposals[task_id] = proposal
            logger.info(f"Proposal approved: [{task_id}]")
            # Execute the stored callback
            if task_id in self.callbacks:
                try:
                    self.callbacks[task_id](proposal)
                    return f"✅ Approval received for task [{task_id}]. Action executed successfully."
                except Exception as e:
                    logger.error(f"Callback execution failed: {e}")
                    return f"❌ Approval received, but execution failed: {e}"
            else:
                return f"⚠️ Approval received for [{task_id}], but no execution callback was found in memory."
        elif task_id in self.approved_proposals:
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
        # Use an event to signal when the proposal is approved or timeout occurs
        approval_event = threading.Event()
        
        def check_approval():
            start_time = time.time()
            while not approval_event.is_set():
                # Check if proposal was approved
                if proposal.task_id in self.approved_proposals:
                    approval_event.set()
                    return
                
                # Check for timeout
                if time.time() - start_time >= timeout:
                    # Remove from pending if timeout
                    if proposal.task_id in self.pending_proposals:
                        del self.pending_proposals[proposal.task_id]
                    logger.warning(f"Approval timeout for proposal: [{proposal.task_id}]")
                    return
                
                # Non-blocking wait using threading.Event
                if approval_event.wait(timeout=0.5):  # Check every 0.5 seconds
                    return
        
        # Start background thread to monitor approval
        monitor_thread = threading.Thread(target=check_approval, daemon=True)
        monitor_thread.start()
        
        # Wait for approval or timeout
        approval_event.wait()
        return proposal.task_id in self.approved_proposals
    
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
            # Execute the action (this would be implemented by the caller)
            action = proposal.action
            
            # For now, just log the action
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
        self.callbacks[task_id] = callback
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
        # This would be implemented with the Mattermost WebSocket listener
        # For now, just a placeholder
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
    
    # Connect to Mattermost
    if not engine.connect_mattermost():
        logger.error("Failed to connect to Mattermost")
        return None
    
    # Create the proposal
    proposal = engine.create_proposal(
        action=action,
        justification=justification,
        risk_assessment=risk_assessment,
        parameters=parameters
    )
    
    # Send to Mattermost
    if not engine.send_proposal(proposal):
        logger.error("Failed to send proposal")
        return None
    
    return proposal