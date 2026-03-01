"""
Daemon Tool Tests
Tests for the Watcher Daemon system including scheduler integration
and Mattermost interrupt handling.
"""
import pytest
from unittest.mock import patch, MagicMock, call, mock_open, PropertyMock
from datetime import datetime, timedelta
import json


class TestRunWatcherJob:
    """Test suite for _run_watcher_job background function."""
    
    @patch('cobalt_agent.tools.daemon.BrowserTool')
    @patch('cobalt_agent.tools.daemon.UniversalExtractor')
    @patch('cobalt_agent.tools.daemon.compute_delta')
    @patch('cobalt_agent.tools.daemon._send_watcher_alert')
    @patch('cobalt_agent.tools.daemon.get_config')
    def test_watcher_job_with_new_entities(
        self, mock_get_config, mock_send_alert, mock_compute_delta, mock_extractor_class, mock_browser
    ):
        """Test that watcher job triggers alert when new entities are detected."""
        # Mock config
        mock_config = MagicMock()
        mock_config.mattermost.approval_team = "approval-team"
        mock_get_config.return_value = mock_config
        
        # Mock browser result
        mock_browser_result = MagicMock()
        mock_browser_result.error = ""
        mock_browser_result.title = "Test Page"
        mock_browser_result.content = "TSLA is going up. New strategy detected."
        mock_browser.return_value.run.return_value = mock_browser_result
        
        # Mock extraction result
        mock_extraction_result = MagicMock()
        mock_extraction_result.nodes = []
        mock_extraction_result.edges = []
        mock_extractor_instance = MagicMock()
        mock_extractor_instance.extract.return_value = mock_extraction_result
        mock_extractor_class.return_value = mock_extractor_instance
        
        # Mock delta payload with new entities
        mock_delta_payload = {
            "new_nodes": [{"entity_type": "Ticker", "name": "TSLA", "properties": {}}],
            "new_edges": [{"source_name": "TSLA", "target_name": "Strategy", "relationship": "TRIGGERED", "properties": {}}],
            "existing_count": 0
        }
        mock_compute_delta.return_value = mock_delta_payload
        
        # Import function
        from cobalt_agent.tools.daemon import _run_watcher_job
        
        # Run the watcher job
        _run_watcher_job("https://example.com", "Monitor stocks", None)
        
        # Verify browser was called
        mock_browser.return_value.run.assert_called_once_with(query="https://example.com")
        
        # Verify extraction was called with content
        mock_extractor_instance.extract.assert_called_once_with(mock_browser_result.content)
        
        # Verify delta was computed - note: compute_delta is called twice in _run_watcher_job
        assert mock_compute_delta.call_count == 2
        
        # Verify alert was sent with correct args
        mock_send_alert.assert_called_once()
        call_args = mock_send_alert.call_args
        assert call_args[0][0] == "https://example.com"
        assert call_args[0][1] == "Monitor stocks"
        assert call_args[0][2] == mock_delta_payload
    
    @patch('cobalt_agent.tools.daemon.BrowserTool')
    @patch('cobalt_agent.tools.daemon.UniversalExtractor')
    @patch('cobalt_agent.tools.daemon.compute_delta')
    @patch('cobalt_agent.tools.daemon._send_watcher_alert')
    @patch('cobalt_agent.tools.daemon.get_config')
    def test_watcher_job_silent_on_no_new_entities(
        self, mock_get_config, mock_send_alert, mock_compute_delta, mock_extractor_class, mock_browser
    ):
        """Test that watcher job does NOT trigger alert when no new entities detected."""
        # Mock config
        mock_config = MagicMock()
        mock_config.mattermost.approval_team = "approval-team"
        mock_get_config.return_value = mock_config
        
        # Mock browser result
        mock_browser_result = MagicMock()
        mock_browser_result.error = ""
        mock_browser_result.title = "Test Page"
        mock_browser_result.content = "No new information here."
        mock_browser.return_value.run.return_value = mock_browser_result
        
        # Mock extraction result
        mock_extraction_result = MagicMock()
        mock_extraction_result.nodes = []
        mock_extraction_result.edges = []
        mock_extractor_instance = MagicMock()
        mock_extractor_instance.extract.return_value = mock_extraction_result
        mock_extractor_class.return_value = mock_extractor_instance
        
        # Mock delta payload with no new entities
        mock_delta_payload = {
            "new_nodes": [],
            "new_edges": [],
            "existing_count": 5
        }
        mock_compute_delta.return_value = mock_delta_payload
        
        # Import function
        from cobalt_agent.tools.daemon import _run_watcher_job
        
        # Run the watcher job
        _run_watcher_job("https://example.com", "Monitor stocks", None)
        
        # Verify browser was called
        mock_browser.return_value.run.assert_called_once()
        
        # Verify alert was NOT sent (silence when no new entities)
        mock_send_alert.assert_not_called()


class TestSendWatcherAlert:
    """Test suite for _send_watcher_alert function."""
    
    @patch('cobalt_agent.tools.daemon.MattermostInterface')
    @patch('cobalt_agent.tools.daemon.get_config')
    def test_alert_sends_markdown_summary(self, mock_get_config, mock_mm_class):
        """Test that alert message includes markdown summary of new edges."""
        # Create a mock MattermostConfig with approval_team set
        mock_mattermost_config = MagicMock()
        mock_mattermost_config.approval_team = "approval-team"
        
        # Create a mock main config with mattermost set
        mock_main_config = MagicMock()
        mock_main_config.mattermost = mock_mattermost_config
        mock_get_config.return_value = mock_main_config
        
        # Mock MattermostInterface - we need to set the config attribute on the instance
        mock_mm = MagicMock()
        mock_mm.connect.return_value = True
        mock_mm.send_message.return_value = True
        mock_mm.disconnect.return_value = None
        # The config attribute will be set by MattermostInterface.__init__ via get_config()
        # We need to mock the config attribute to return our mock_mattermost_config
        mock_mm.config = mock_mattermost_config
        mock_mm_class.return_value = mock_mm
        
        # Import function
        from cobalt_agent.tools.daemon import _send_watcher_alert
        
        # Test delta payload
        delta_payload = {
            "new_nodes": [
                {"entity_type": "Ticker", "name": "TSLA", "properties": {}}
            ],
            "new_edges": [
                {
                    "source_name": "TSLA",
                    "target_name": "Morning Gapper",
                    "relationship": "TRIGGERED_STRATEGY",
                    "properties": {"confidence": 0.95}
                }
            ]
        }
        
        # Send alert
        _send_watcher_alert("https://example.com", "Monitor stocks", delta_payload)
        
        # Verify Mattermost was connected
        mock_mm.connect.assert_called_once()
        
        # Verify message was sent with correct channel
        # send_message takes positional args: channel_name, team_name, message
        mock_mm.send_message.assert_called_once()
        call_args = mock_mm.send_message.call_args[0]
        assert call_args[0] == "town-square"  # channel_name
        assert call_args[1] == "approval-team"  # team_name
        
        # Verify message contains expected content
        message = call_args[2]
        assert "🚨 **Watcher Alert**" in message
        assert "https://example.com" in message
        assert "Monitor stocks" in message
        assert "TSLA" in message
        assert "Morning Gapper" in message
        assert "TRIGGERED_STRATEGY" in message
        
        # Verify disconnect was called
        mock_mm.disconnect.assert_called_once()
    
    @patch('cobalt_agent.tools.daemon.MattermostInterface')
    @patch('cobalt_agent.tools.daemon.get_config')
    def test_alert_not_sent_when_mm_connection_fails(self, mock_get_config, mock_mm_class):
        """Test that no alert is sent when Mattermost connection fails."""
        # Mock config
        mock_config = MagicMock()
        mock_config.mattermost.approval_team = "approval-team"
        mock_get_config.return_value = mock_config
        
        # Mock MattermostInterface that fails to connect
        mock_mm = MagicMock()
        mock_mm.connect.return_value = False
        mock_mm.disconnect.return_value = None
        type(mock_mm).config = PropertyMock(return_value=mock_config)
        mock_mm_class.return_value = mock_mm
        
        # Import function
        from cobalt_agent.tools.daemon import _send_watcher_alert
        
        # Test delta payload
        delta_payload = {
            "new_nodes": [],
            "new_edges": []
        }
        
        # Send alert
        _send_watcher_alert("https://example.com", "Monitor stocks", delta_payload)
        
        # Verify connect was called but send_message was NOT called
        mock_mm.connect.assert_called_once()
        mock_mm.send_message.assert_not_called()