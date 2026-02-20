"""
Mattermost Communication Interface for Cobalt Agent
Provides a robust interface for sending and receiving messages via Mattermost.
"""

from typing import Optional, Dict, Any
from urllib.parse import urlparse

from mattermostdriver import Driver
from loguru import logger

from cobalt_agent.config import get_config, MattermostConfig


class MattermostInterface:
    """
    Interface for Mattermost communication.
    
    Handles connection to Mattermost server, authentication,
    and message sending functionality.
    """
    
    def __init__(self, config: Optional[MattermostConfig] = None):
        """
        Initialize the Mattermost interface.
        
        Args:
            config: Optional MattermostConfig. If not provided, loads from global config.
        """
        self.config = config or get_config().mattermost
        self.driver: Optional[Driver] = None
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