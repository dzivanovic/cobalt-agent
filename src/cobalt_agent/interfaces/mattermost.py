"""
Mattermost Communication Interface for Cobalt Agent
Provides a robust interface for sending and receiving messages via Mattermost.
"""

import asyncio
import json
import threading
import multiprocessing
import re
import shlex
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING
if TYPE_CHECKING:
    from cobalt_agent.main import CobaltAgent
    from cobalt_agent.core.proposals import ProposalEngine, Proposal
from urllib.parse import urlparse

import websockets
from loguru import logger
from mattermostdriver import Driver

from cobalt_agent.config import get_config, MattermostConfig


class MattermostInterface:
    """
    Interface for Mattermost communication.
    
    Handles connection to Mattermost server, authentication,
    and message sending functionality.
    """
    
    def __init__(self, config: Optional[MattermostConfig] = None, memory: Optional[Any] = None):
        self.proposal_engine: Optional[Any] = None
        """
        Initialize the Mattermost interface.
        
        Args:
            config: Optional MattermostConfig. If not provided, loads from global config.
            memory: Optional Memory instance (PostgresMemory or fallback). If not provided, loads from agent.
        """
        self.config = config or get_config().mattermost
        self.driver: Optional[Driver] = None
        self.brain: Optional[Any] = None
        self.memory: Optional[Any] = memory  # Memory instance passed from agent
        self.is_connected: bool = False
        self._boot_message_sent: bool = False  # Lifecycle hook: track if boot notification sent
        
        logger.info(f"MattermostInterface initialized (URL: {self.config.url})")
    
    def connect(self) -> bool:
        """
        Connect to the Mattermost server and authenticate.
        
        Returns:
            True if connection and authentication succeeded, False otherwise.
        """
        if not self.config.url:
            logger.error("MATTERMOST_URL is not configured")
            return False
        
        if not self.config.token:
            logger.error("MATTERMOST_TOKEN is not configured")
            return False
        
        try:
            parsed = urlparse(self.config.url)
            driver_options = {
                "url": parsed.hostname,
                "scheme": parsed.scheme or "http",
                "port": parsed.port or 8065,
                "basepath": "/api/v4",
                "token": self.config.token,
            }
            
            logger.debug(f"Driver options: {driver_options}")
            
            self.driver = Driver(options=driver_options)
            
            # Attempt login
            user = self.driver.login()
            
            if user and "id" in user:
                self.is_connected = True
                logger.info(f"Successfully connected to Mattermost as user: {user.get('username', 'unknown')}")
                return True
            else:
                logger.error("Failed to authenticate with Mattermost")
                self.is_connected = False
                return False
                
        except Exception as e:
            logger.error(f"Failed to connect to Mattermost: {e}")
            self.is_connected = False
            return False
    
    def disconnect(self) -> None:
        """Disconnect from the Mattermost server."""
        if self.driver:
            try:
                self.driver.logout()
            except Exception as e:
                logger.warning(f"Error during logout: {e}")
        self.is_connected = False
        logger.info("Disconnected from Mattermost")
    
    def send_message(self, channel_name: str, team_name: str, message: str) -> bool:
        """
        Send a message to a Mattermost channel.
        
        Args:
            channel_name: Name of the channel (without #)
            team_name: Name of the team
            message: The message content to send
            
        Returns:
            True if message was sent successfully, False otherwise.
        """
        if not self.is_connected or not self.driver:
            logger.error("Not connected to Mattermost")
            return False
        
        try:
            # Get team ID
            teams = self.driver.teams.get_team_by_name(team_name)
            if not teams:
                logger.error(f"Team not found: {team_name}")
                return False
            
            team_id = teams["id"]
            
            # Get channel ID using team_id as parameter
            channel = self.driver.channels.get_channel_by_name(team_id, channel_name)
            if not channel:
                logger.error(f"Channel not found: {channel_name} in team {team_name}")
                return False
            
            channel_id = channel["id"]
            
            post = self.driver.posts.create_post(
                options={
                    "channel_id": channel_id,
                    "message": message
                }
            )
            
            if post and "id" in post:
                logger.info(f"Message sent to #{channel_name} in team {team_name}")
                return True
            else:
                logger.error("Failed to create post")
                return False
                
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            return False
    
    def send_message_to_channel_id(self, channel_id: str, message: str) -> bool:
        """
        Send a message directly to a channel using its ID.
        
        Args:
            channel_id: The Mattermost channel ID
            message: The message content to send
            
        Returns:
            True if message was sent successfully, False otherwise.
        """
        if not self.is_connected or not self.driver:
            logger.error("Not connected to Mattermost")
            return False
        
        try:
            post = self.driver.posts.create_post(
                options={
                    "channel_id": channel_id,
                    "message": message
                }
            )
            
            if post and "id" in post:
                logger.info(f"Message sent to channel {channel_id}")
                return True
            else:
                logger.error("Failed to create post")
                return False
                
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            return False
    
    def get_my_user_id(self) -> Optional[str]:
        """
        Get the current user's ID.
        
        Returns:
            User ID string if connected, None otherwise.
        """
        if not self.is_connected or not self.driver:
            return None
        
        try:
            user = self.driver.users.get_user("me")
            return user["id"] if user else None
        except Exception as e:
            logger.error(f"Failed to get user: {e}")
            return None
    
    def _parse_action_response(self, response: Any) -> tuple[str, dict[str, str]]:
        """
        Parse action response from LLM or brain.route output.
        
        Handles multiple formats:
        1. key="value" pairs: browser url="https://..." query="..."
        2. Dict with tool_name/tool_args or action/args keys
        3. Fallback to raw string parsing
        
        Args:
            response: The response object (dict or string)
            
        Returns:
            Tuple of (tool_name, tool_args_dict)
        """
        # If response is a dict, extract from known keys
        if isinstance(response, dict):
            # Try both naming conventions
            tool_name_raw = response.get("tool_name") or response.get("action")
            tool_args_raw = response.get("tool_args") or response.get("args", {})
            
            # If tool_args is not a dict, try to parse it as a string
            if not isinstance(tool_args_raw, dict):
                _, tool_args_raw = self._parse_action_string_wrapper(str(tool_args_raw) if tool_args_raw else "")
            else:
                # Convert all values to strings
                tool_args_raw = {str(k): str(v) for k, v in tool_args_raw.items()}
            
            # If we have a string in tool_name, parse the whole thing
            if isinstance(tool_name_raw, str) and tool_name_raw:
                # If tool_args is empty but we have a full action string, parse it
                if not tool_args_raw and "tool_name" in response and isinstance(response.get("tool_name"), str):
                    # Full action is in tool_name field
                    return self._parse_action_string_wrapper(response["tool_name"])
                return tool_name_raw, tool_args_raw
            
            return "browser", tool_args_raw if tool_args_raw else {}
        
        # If response is a string, parse it directly
        if isinstance(response, str):
            return self._parse_action_string_wrapper(response)
        
        # Fallback
        logger.warning(f"Unexpected response type: {type(response)}, using defaults")
        return "browser", {}
    
    def _parse_action_string_wrapper(self, action_string: str) -> tuple[str, dict[str, str]]:
        """
        Parse action string like: browser url="https://..." query="..."
        
        Uses regex to extract key="value" or key='value' pairs.
        
        Args:
            action_string: The raw action string from LLM
            
        Returns:
            Tuple of (tool_name, tool_args_dict)
        """
        import re
        
        # Default values
        tool_name = "browser"
        tool_args: dict[str, str] = {}
        
        if not action_string or not action_string.strip():
            return tool_name, tool_args
        
        # Strip whitespace
        action_string = action_string.strip()
        
        # Extract tool name (first word)
        parts = action_string.split(None, 1)
        if not parts:
            return tool_name, tool_args
        
        tool_name = parts[0].strip().lower()
        
        # Fuzzy Match Hack: map "scrape" and "search" to "browser"
        if tool_name in ["scrape", "search"]:
            tool_name = "browser"
            logger.info(f"Fuzzy matched '{tool_name}' -> 'browser'")
        
        # If no arguments, return early
        if len(parts) <= 1:
            return tool_name, tool_args
        
        arg_string = parts[1].strip()
        
        # Try to extract key="value" or key='value' pairs using regex
        # Pattern: word followed by = then quoted value
        matches = re.findall(r'(\w+)=(?:"(.*?)"|\'(.*?)\')', arg_string)
        
        if matches:
            # We have key="value" pairs
            for key, double_quoted, single_quoted in matches:
                # Use whichever group has a value
                value = double_quoted if double_quoted else single_quoted
                if value is not None:
                    tool_args[key] = value
        else:
            # No key="value" pairs found, try alternative parsing
            # Handle unquoted values: key=value (no quotes)
            unquoted_matches = re.findall(r'(\w+)=(\S+)', arg_string)
            if unquoted_matches:
                for key, value in unquoted_matches:
                    tool_args[key] = value
            else:
                # Fallback: treat entire string as query or URL
                # Check if first word is a URL
                first_token = arg_string.split()[0] if arg_string.split() else ""
                if first_token.startswith("http"):
                    tool_args["url"] = arg_string
                else:
                    tool_args["query"] = arg_string
        
        return tool_name, tool_args
    
    async def _handle_mattermost_event(self, message: str) -> None:
        """
        Internal handler for Mattermost WebSocket events.
        
        Properly handles the Mattermost API quirk where event_data['data']['post']
        is passed as a stringified JSON object, NOT a parsed dictionary.
        
        Args:
            message: The event JSON string from Mattermost WebSocket
        """
        # Log raw payload for debugging
        logger.info(f"RAW WEBSOCKET PAYLOAD: {message}")
        
        try:
            event_data = json.loads(message)
            
            # Handle boot notification (lifecycle hook)
            event_type = event_data.get("event")
            if event_type in ("hello", "status_change"):
                status = event_data.get("data", {}).get("status", "")
                if status == "online" and not self._boot_message_sent:
                    # Send boot notification to town-square
                    message = "🟢 **Cobalt System Online** | Core systems initialized and ready. HITL Bouncer active."
                    self.send_message("town-square", self.config.approval_team, message)
                    self._boot_message_sent = True
                    logger.info("Sent boot notification to Mattermost")
                    # Continue to process other events after boot message
            
            # Only process 'posted' events (new messages)
            if event_type != "posted":
                return
            
            # Extract and parse the nested post data
            post_str = event_data.get("data", {}).get("post")
            if not post_str:
                return
            
            post_data = json.loads(post_str)
            
            user_id = post_data.get("user_id")
            channel_id = post_data.get("channel_id")
            text = post_data.get("message", "")
            
            # Ignore Mattermost system messages (joins, leaves, header updates)
            if post_data.get("type", "") != "":
                return
            
            # Ignore the bot's own messages to prevent infinite loops
            if user_id == self.get_my_user_id():
                return
            
            logger.info(f"Message received in channel {channel_id}: {text}")
            
            # === HITL APPROVAL INTERCEPTOR ===
            # Check for approval/rejection messages first
            text_lower = text.strip().lower()
            if text_lower.startswith("approve") or text_lower.startswith("reject"):
                from cobalt_agent.core.proposals import ProposalEngine, HITLProposalStore
                engine = ProposalEngine()
                
                # Check for approval response first
                result = engine.handle_approval_response(text, channel_id)
                if result:
                    # handle_approval_response returns a string message for approval/rejection
                    logger.info(f"Approval response: {result}")
                    self.send_message_to_channel_id(channel_id, result)
                    return  # Don't route to brain for approval responses
                
                # If not handled by handle_approval_response, look up from database directly
                approval_pattern = r"approve\s+(\w{8})"
                match = re.search(approval_pattern, text_lower)
                if match:
                    task_id = match.group(1)
                    
                    # Initialize ProposalEngine to access approve_and_get_payload
                    if self.proposal_engine is None:
                        from cobalt_agent.core.proposals import ProposalEngine
                        self.proposal_engine = ProposalEngine()
                    
                    # Step 1: Update DB and get payload (Transaction closes immediately)
                    proposal_data = self.proposal_engine.approve_and_get_payload(task_id)
                    
                    if proposal_data:
                        # Step 2: Execute the tool entirely outside the DB transaction
                        tool_name = proposal_data.get("tool_name")
                        tool_kwargs = proposal_data.get("tool_kwargs", {})
                        
                        try:
                            from cobalt_agent.tools.tool_manager import ToolManager
                            tool_result = ToolManager().execute_tool(
                                name=tool_name, 
                                args=tool_kwargs, 
                                bypass_hitl=True
                            )
                            # tool_result is now a dictionary from model_dump()
                            result_str = str(tool_result)
                            
                            # Step 1: Send temporary status message
                            status_msg = f"🔄 **Tool executed successfully. Synthesizing final response...**"
                            self.send_message_to_channel_id(channel_id, status_msg)
                            
                            # Step 2: Construct observation for LLM
                            observation = f"[Observation: The tool '{tool_name}' returned the following data: {tool_result}. Please provide the final, formatted response to the user based on this data.]"
                            
                            # Step 3: Route observation to LLM for final response generation
                            final_response = None
                            try:
                                # Get the brain instance from the interface
                                brain = getattr(self, 'brain', None)
                                if brain and hasattr(brain, 'llm'):
                                    # Use the LLM to generate a response based on the observation
                                    system_prompt = "You are Cobalt, an AI assistant. A tool has been executed on behalf of the user. Please provide a clear, well-formatted response summarizing the results and any next steps."
                                    final_response = brain.llm.generate_response(
                                        system_prompt=system_prompt,
                                        user_input=observation,
                                        memory_context=[],
                                        search_context=""
                                    )
                                else:
                                    # Fallback: use the raw result if LLM is not available
                                    final_response = f"✅ **Task Executed**: {result_str[:500]}..." if len(result_str) > 500 else f"✅ **Task Executed**: {result_str}"
                            except Exception as llm_error:
                                logger.error(f"Failed to generate LLM response: {llm_error}")
                                final_response = f"✅ **Task Executed**: {result_str[:500]}..." if len(result_str) > 500 else f"✅ **Task Executed**: {result_str}"
                            
                            # Step 4: Send final response to town-square (public channel for visibility)
                            if final_response:
                                # Failsafe: Ensure response is a string to prevent dict leak to Mattermost API
                                if isinstance(final_response, dict):
                                    final_response = str(final_response)
                                self.send_message("town-square", self.config.approval_team, final_response)
                                logger.info("Final LLM response sent to town-square")
                            else:
                                logger.warning("LLM generated no response")
                            # Step 5: Confirm execution in approvals channel
                            self.send_message_to_channel_id(channel_id, f"✅ **Response synthesized and broadcast to town-square.**")
                        except Exception as e:
                            logger.error(f"Failed to execute approved tool: {e}")
                            result_msg = f"❌ **Execution Failed**: {str(e)}"
                            self.send_message_to_channel_id(channel_id, result_msg)
                            self.send_message("town-square", self.config.approval_team, f"❌ **Execution Failed**: {str(e)}")
                    else:
                        # No pending proposal found
                        result_msg = f"⚠️ **Approval Failed**: No pending approval found for task [{task_id}]."
                        self.send_message_to_channel_id(channel_id, result_msg)
                    return
                
                # Check for rejection
                reject_pattern = r"reject\s+(\w{8})"
                reject_match = re.search(reject_pattern, text_lower)
                if reject_match:
                    task_id = reject_match.group(1)
                    store = HITLProposalStore()
                    proposal = store.get_proposal(task_id)
                    
                    if proposal and proposal.get("status") == "pending":
                        # Case 1: Proposal exists and is pending - reject it
                        store.update_status(task_id, "rejected")
                        result_msg = f"🛑 Action [{task_id}] was rejected by the administrator. Execution aborted."
                        
                        # Reply in the approvals channel
                        self.send_message_to_channel_id(channel_id, result_msg)
                        
                        # Broadcast to town-square
                        self.send_message("town-square", self.config.approval_team, f"🛑 Action [{task_id}] was rejected by the administrator. Execution aborted.")
                        return
                    else:
                        # Case 2: No pending proposal found (already processed or doesn't exist)
                        result_msg = f"🛑 Action [{task_id}] was rejected by the administrator. Execution aborted."
                        self.send_message_to_channel_id(channel_id, result_msg)
                        self.send_message("town-square", self.config.approval_team, f"🛑 Action [{task_id}] was rejected by the administrator. Execution aborted.")
                        return
                
                return
            
            # Route to the brain if attached - run LLM inference in background thread
            if hasattr(self, 'brain') and self.brain:
                logger.info("Routing message to Cortex in background thread...")
                
                # Use memory from MattermostInterface (initialized from agent)
                # This ensures we use PostgresMemory, not the legacy JSON fallback
                memory = self.memory
                if memory is None:
                    # Fallback to agent's memory if interface wasn't initialized with one
                    logger.warning("No memory instance available, falling back to PostgresMemory")
                    from cobalt_agent.memory.postgres import PostgresMemory
                    memory = PostgresMemory()
                
                # Capture current values to avoid closure issues
                brain = self.brain
                memory_ref = memory
                channel_id_ref = channel_id
                text_ref = text
                
                def think_and_reply():
                    try:
                        # Use 'route' method on Cortex for user input
                        response = brain.route(text_ref)
                        
                        # Handle HITL approval requirement (dict return from brain.route)
                        if isinstance(response, dict) and response.get("status") == "requires_approval":
                            # Initialize ProposalEngine if not already connected
                            if self.proposal_engine is None:
                                from cobalt_agent.core.proposals import ProposalEngine
                                self.proposal_engine = ProposalEngine()
                                # Connect to Mattermost for approval broadcast
                                if not self.proposal_engine.connect_mattermost():
                                    logger.warning("Failed to connect ProposalEngine to Mattermost")
                            
                            # The global proposal_engine is already connected to Mattermost!
                            if self.proposal_engine:
                                # Extract tool name and args from response
                                tool_name, tool_args = self._parse_action_response(response)
                                
                                # 1. Create the proposal in Postgres (returns the short ID string)
                                task_id = self.proposal_engine.create_proposal(tool_name, tool_args)
                                
                                # 2. Retrieve the full proposal object from the database so we can format it
                                proposal_store = self.proposal_engine._get_hitl_store()
                                proposal_data = proposal_store.get_proposal(task_id)
                                
                                if proposal_data:
                                    # 3. Create a Proposal object from the stored data
                                    from cobalt_agent.core.proposals import Proposal
                                    proposal_obj = Proposal(
                                        task_id=proposal_data["id"],
                                        action=proposal_data["tool_name"],
                                        justification="AI-initiated action requiring human approval",
                                        risk_assessment="Standard approval workflow",
                                        parameters=proposal_data["tool_kwargs"],
                                        timestamp=proposal_data["created_at"]
                                    )
                                    # 4. Format the beautiful Markdown card
                                    markdown_card = proposal_obj.format_for_mattermost()
                                    
                                    # 5. Broadcast to the approval channel
                                    if not self.proposal_engine.send_proposal(proposal_obj):
                                        logger.error("Failed to send proposal to Mattermost")
                                    
                                    result = f"Action paused. Proposal [{task_id}] sent to Admin for approval in Mattermost."
                                else:
                                    result = f"Error: Could not retrieve proposal [{task_id}] from database."
                            else:
                                result = "Action paused. Proposal could not be created (Mattermost connection unavailable)."
                            self.send_message_to_channel_id(channel_id_ref, str(result))
                            return
                        
                        if response:
                            # Specialized department response (TACTICAL, INTEL, OPS, etc.)
                            self.send_message_to_channel_id(channel_id_ref, response)
                        else:
                            # DEFAULT route - use ReAct loop for tool execution
                            logger.info("DEFAULT route detected, using ReAct loop...")
                            # Use the agent's LLM with the correct system prompt
                            from cobalt_agent.config import get_config
                            config = get_config()
                            from cobalt_agent.prompt import PromptEngine
                            prompt_engine = PromptEngine(config.persona)
                            system_prompt = prompt_engine.build_system_prompt()
                            
                            # Initialize conversation history with user input
                            conversation_history = [
                                {"role": "user", "content": text_ref}
                            ]
                            
                            # MAX_ITERATIONS to prevent infinite loops
                            MAX_ITERATIONS = 3
                            iteration = 0
                            final_answer = None
                            
                            while iteration < MAX_ITERATIONS:
                                iteration += 1
                                logger.info(f"ReAct iteration {iteration}/{MAX_ITERATIONS}")
                                
                                # Generate response from LLM using conversation history
                                response = brain.llm.generate_response(
                                    system_prompt=system_prompt,
                                    user_input=None,  # Already included in conversation history
                                    memory_context=conversation_history,
                                    search_context=""
                                )
                                
                                logger.info(f"LLM Response: {response}")
                                
                                # Check if response contains ACTION:
                                if "ACTION:" in response:
                                    # Parse the tool name and query
                                    logger.info("ACTION: detected, parsing tool command...")
                                    
                                    # Extract the ACTION line
                                    action_line = None
                                    for line in response.split('\n'):
                                        if 'ACTION:' in line:
                                            action_line = line
                                            break
                                    
                                    if action_line:
                                        # Parse "ACTION: tool_name ..." using the robust parser
                                        rest_of_line = action_line.replace('ACTION:', '').strip()
                                        
                                        tool_name, tool_args = self._parse_action_string_wrapper(rest_of_line)
                                        
                                        # Execute the tool
                                        from cobalt_agent.tools.tool_manager import ToolManager
                                        tool_result = ToolManager().execute_tool(
                                            name=tool_name,
                                            args=tool_args
                                        )
                                        
                                        # 1. Catch the Bouncer Interception
                                        if isinstance(tool_result, dict) and tool_result.get("status") == "requires_approval":
                                            # Grab the data
                                            tool_name_for_proposal = tool_result.get("tool_name")
                                            tool_args = tool_result.get("tool_args", {})
                                            
                                            # Initialize ProposalEngine if not already connected
                                            if self.proposal_engine is None:
                                                from cobalt_agent.core.proposals import ProposalEngine
                                                self.proposal_engine = ProposalEngine()
                                                # Connect to Mattermost for approval broadcast
                                                if not self.proposal_engine.connect_mattermost():
                                                    logger.warning("Failed to connect ProposalEngine to Mattermost")
                                            
                                            # Create the proposal in Postgres
                                            task_id = self.proposal_engine.create_proposal(tool_name_for_proposal, tool_args)
                                            
                                            # Retrieve the full proposal data from the database
                                            proposal_store = self.proposal_engine._get_hitl_store()
                                            proposal_data = proposal_store.get_proposal(task_id)
                                            
                                            if proposal_data:
                                                # Create a Proposal object from the stored data
                                                from cobalt_agent.core.proposals import Proposal
                                                proposal_obj = Proposal(
                                                    task_id=proposal_data["id"],
                                                    action=proposal_data["tool_name"],
                                                    justification="AI-initiated action requiring human approval",
                                                    risk_assessment="Standard approval workflow",
                                                    parameters=proposal_data["tool_kwargs"],
                                                    timestamp=proposal_data["created_at"]
                                                )
                                                # Send card to the admin channel
                                                if not self.proposal_engine.send_proposal(proposal_obj):
                                                    logger.error("Failed to send proposal to Mattermost")
                                                # Return the pause message to the user immediately, BREAKING the ReAct loop
                                                result = f"Action paused. Proposal [{task_id}] sent to Admin for approval in Mattermost."
                                            else:
                                                result = f"Error: Could not retrieve proposal [{task_id}] from database."
                                            
                                            self.send_message_to_channel_id(channel_id_ref, str(result))
                                            return
                                        
                                        # 2. If it's NOT a Bouncer pause, ensure it's a string for the LLM
                                        if not isinstance(tool_result, str):
                                            tool_result = str(tool_result)
                                        
                                        # Format the observation for LLM (tool_manager now returns strings)
                                        if tool_result.startswith("Error:"):
                                            observation = f"[Observation: Tool execution failed - {tool_result}]"
                                        else:
                                            observation = f"[Observation: {tool_result}]"
                                        
                                        # Append observation to conversation history
                                        conversation_history.append({
                                            "role": "assistant",
                                            "content": response
                                        })
                                        conversation_history.append({
                                            "role": "user",
                                            "content": observation
                                        })
                                        
                                        logger.info(f"Tool executed: {tool_name}, Observation: {observation}")
                                    else:
                                        # No valid ACTION line found, treat as final answer
                                        final_answer = response
                                        break
                                else:
                                    # No ACTION: found, this is the final conversational answer
                                    logger.info("No ACTION: detected, returning final answer")
                                    final_answer = response
                                    break
                            
                            # Send final answer to Mattermost
                            if final_answer:
                                # Failsafe: Ensure response is a string to prevent dict leak to Mattermost API
                                if isinstance(final_answer, dict):
                                    final_answer = str(final_answer)
                                # Update memory with assistant's response
                                memory_ref.add_log(final_answer, source="Assistant")
                                self.send_message_to_channel_id(channel_id_ref, final_answer)
                                logger.info("Final response sent to Mattermost")
                            else:
                                logger.warning("ReAct loop completed without final answer")
                    except Exception as e:
                        logger.error(f"think_and_reply error: {e}", exc_info=True)
                
                # Run the sync function in a background thread
                asyncio.create_task(asyncio.to_thread(think_and_reply))
            else:
                logger.warning("Brain is not attached to MattermostInterface! Cannot reply.")
                
        except Exception as e:
            logger.error(f"Error parsing Mattermost event: {e}", exc_info=True)
    
    def _handle_events(self, mm_driver: Driver) -> None:
        """
        Event handler for Mattermost WebSocket events.
        
        This method is called by the websocket when events are received.
        
        Args:
            mm_driver: The Mattermost driver instance (for accessing get_user_id, etc.)
        """
        # This is called for each event type from the websocket
        pass
    
    def _run_websocket_in_process(self, brain: "CobaltAgent", event_queue: "multiprocessing.Queue") -> None:
        """
        Run the Mattermost WebSocket in a separate process to avoid event loop conflicts.
        
        Args:
            brain: The CobaltAgent instance (not used directly, but for reference)
            event_queue: Queue for passing events to the main process
        """
        # Import here to ensure it runs in the new process context
        from mattermostdriver import Driver
        from loguru import logger
        
        # Reinitialize the driver in this process
        parsed = urlparse(self.config.url)
        driver_options = {
            "url": parsed.hostname,
            "scheme": parsed.scheme or "http",
            "port": parsed.port or 8065,
            "basepath": "/api/v4",
            "token": self.config.token,
        }
        
        driver = Driver(options=driver_options)
        driver.login()
        
        # Define the event handler for init_websocket
        def on_event(event: str, data: Dict[str, Any]) -> None:
            # Build the event dict from the event type and data
            event_dict = {"event": event, "data": data}
            # For now, just log to file since stdout might be redirected
            logger.info(f"Mattermost event: {event}")
            # Send to main process if needed
            try:
                event_queue.put(event_dict)
            except:
                pass
        
        try:
            # This runs its own event loop
            driver.init_websocket(on_event)
        except Exception as e:
            logger.error(f"WebSocket error: {e}")
        
        driver.logout()
    
    def start_listening(self, brain: "CobaltAgent") -> None:
        async def run_native_ws():
            # Format the URL properly for WebSockets
            base_url = self.config.url.rstrip('/')
            ws_url = base_url.replace('http://', 'ws://').replace('https://', 'wss://') + "/api/v4/websocket"
            
            logger.info(f"Connecting to native WebSocket engine: {ws_url}")
            
            headers = {"Authorization": f"Bearer {self.config.token}"}
            try:
                async with websockets.connect(ws_url, ping_interval=20, ping_timeout=20, additional_headers=headers) as ws:
                    logger.info("Connected and authenticated via HTTP headers. Listening for messages...")
                    
                    # Listen to the raw data stream forever
                    async for message in ws:
                        logger.info(f"RAW WEBSOCKET PAYLOAD: {message}")
                        await self._handle_mattermost_event(message)
            except Exception as e:
                logger.error(f"Native WebSocket connection dropped: {e}", exc_info=True)

        # Run the native engine in the main thread
        logger.info("Starting native WebSocket engine...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(run_native_ws())
        except KeyboardInterrupt:
            logger.info("Bot shut down manually.")