"""
Mattermost Communication Interface for Cobalt Agent
Provides a robust interface for sending and receiving messages via Mattermost.
"""

import asyncio
import json
import threading
import multiprocessing
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
    
    def __init__(self, config: Optional[MattermostConfig] = None):
        self.proposal_engine: Optional[Any] = None
        """
        Initialize the Mattermost interface.
        
        Args:
            config: Optional MattermostConfig. If not provided, loads from global config.
        """
        self.config = config or get_config().mattermost
        self.driver: Optional[Driver] = None
        self.brain: Optional[Any] = None
        self.is_connected: bool = False
        
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
            
            # Only process 'posted' events (new messages)
            if event_data.get("event") != "posted":
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
            text_lower = text.strip().lower()
            if text_lower.startswith("approve") or text_lower.startswith("reject"):
                from cobalt_agent.core.proposals import ProposalEngine
                engine = ProposalEngine()
                
                # Handle the response and send the result back to the channel
                result_msg = engine.handle_approval_response(text)
                if result_msg:
                    # Reply in the approvals channel
                    self.send_message_to_channel_id(channel_id, result_msg)
                    
                    # CLOSE THE LOOP: Broadcast to town-square so the user knows the outcome
                    if "✅ Approval received" in result_msg:
                        self.send_message("town-square", self.config.approval_team, "✅ **Task Completed:** The pending action was approved and successfully executed.")
                    elif "❌ Rejection received" in result_msg:
                        self.send_message("town-square", self.config.approval_team, "❌ **Task Cancelled:** The pending action was rejected by an Admin.")
                return
            
            # Check for approval response first
            if self.proposal_engine:
                approved_proposal = self.proposal_engine.handle_approval_response(text, channel_id)
                if approved_proposal:
                    logger.info(f"Proposal approved: [{approved_proposal.task_id}]")
                    # Execute the approved action
                    self.proposal_engine.execute_approved(approved_proposal)
                    return  # Don't route to brain for approval responses
            
            # Route to the brain if attached - run LLM inference in background thread
            if hasattr(self, 'brain') and self.brain:
                logger.info("Routing message to Cortex in background thread...")
                
                # Import tool_manager for the tool loop
                from cobalt_agent.tools.tool_manager import ToolManager
                from cobalt_agent.memory import MemorySystem
                from cobalt_agent.config import get_config
                
                # Try to get memory from brain if available (for longer-term context)
                try:
                    memory = self.brain.memory if hasattr(self.brain, 'memory') else MemorySystem()
                except:
                    memory = MemorySystem()
                
                def think_and_reply():
                    try:
                        # Use 'route' method on Cortex for user input
                        response = self.brain.route(text)
                        if response:
                            # Specialized department response (TACTICAL, INTEL, OPS, etc.)
                            self.send_message_to_channel_id(channel_id, response)
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
                                {"role": "user", "content": text}
                            ]
                            
                            # MAX_ITERATIONS to prevent infinite loops
                            MAX_ITERATIONS = 3
                            iteration = 0
                            final_answer = None
                            
                            while iteration < MAX_ITERATIONS:
                                iteration += 1
                                logger.info(f"ReAct iteration {iteration}/{MAX_ITERATIONS}")
                                
                                # Generate response from LLM using conversation history
                                response = self.brain.llm.generate_response(
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
                                        # Parse "ACTION: tool_name query_string"
                                        action_parts = action_line.replace('ACTION:', '').strip().split(' ', 1)
                                        tool_name = action_parts[0].strip().lower()
                                        query = action_parts[1].strip() if len(action_parts) > 1 else ""
                                        
                                        # Fuzzy Match Hack: map "scrape" and "search" to "browser"
                                        if tool_name in ["scrape", "search"]:
                                            tool_name = "browser"
                                            logger.info(f"Fuzzy matched '{tool_name}' -> 'browser'")
                                        
                                        # Execute the tool
                                        tool_manager = ToolManager()
                                        tool_result = tool_manager.execute_tool(
                                            tool_name=tool_name,
                                            args={"query": query}
                                        )
                                        
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
                                # Update memory with assistant's response
                                memory.add_log(final_answer, source="Assistant")
                                self.send_message_to_channel_id(channel_id, final_answer)
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