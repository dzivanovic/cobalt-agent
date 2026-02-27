"""
Scheduler Tests
Tests that the APScheduler registers cron jobs correctly.
"""
import pytest
from unittest.mock import patch, MagicMock, call
from datetime import datetime, time


class TestCobaltScheduler:
    """Test suite for CobaltScheduler."""
    
    @patch("cobalt_agent.services.scheduler.BackgroundScheduler")
    @patch("cobalt_agent.services.scheduler.get_config")
    def test_scheduler_registers_morning_briefing_job(self, mock_get_config, mock_scheduler_class):
        """Test that Morning Briefing job is registered with correct cron schedule."""
        # Mock the config
        mock_config = MagicMock()
        mock_config.system.obsidian_vault_path = "/test/vault"
        mock_get_config.return_value = mock_config
        
        # Mock the scheduler
        mock_scheduler = MagicMock()
        mock_scheduler_class.return_value = mock_scheduler
        
        # Import and instantiate scheduler
        from cobalt_agent.services.scheduler import CobaltScheduler
        
        scheduler = CobaltScheduler()
        
        # Verify scheduler was created
        mock_scheduler_class.assert_called_once()
        
        # Verify the job was added with correct parameters
        mock_scheduler.add_job.assert_called_once()
        
        # Get the call arguments - call_args is (args, kwargs) tuple
        call_args = mock_scheduler.add_job.call_args
        args = call_args[0]
        kwargs = call_args[1] if len(call_args) > 1 else {}
        
        # First positional arg should be the function
        assert args[0] == scheduler.generate_morning_briefing
        # Second positional arg is the trigger type
        assert args[1] == "cron"
        assert kwargs.get("day_of_week") == "mon-fri"
        assert kwargs.get("hour") == 8
        assert kwargs.get("minute") == 0
        assert kwargs.get("id") == "morning_briefing"
        assert kwargs.get("replace_existing") is True
    
    @patch("cobalt_agent.services.scheduler.BackgroundScheduler")
    @patch("cobalt_agent.services.scheduler.get_config")
    def test_scheduler_start_method(self, mock_get_config, mock_scheduler_class):
        """Test that start() method starts the scheduler."""
        # Mock the config
        mock_config = MagicMock()
        mock_config.system.obsidian_vault_path = "/test/vault"
        mock_get_config.return_value = mock_config
        
        # Mock the scheduler
        mock_scheduler = MagicMock()
        mock_scheduler_class.return_value = mock_scheduler
        
        from cobalt_agent.services.scheduler import CobaltScheduler
        
        scheduler = CobaltScheduler()
        scheduler.start()
        
        # Verify scheduler.start() was called
        mock_scheduler.start.assert_called_once()
    
    @patch("cobalt_agent.services.scheduler.BackgroundScheduler")
    @patch("cobalt_agent.services.scheduler.get_config")
    def test_scheduler_shutdown_method(self, mock_get_config, mock_scheduler_class):
        """Test that shutdown() method shuts down the scheduler."""
        # Mock the config
        mock_config = MagicMock()
        mock_config.system.obsidian_vault_path = "/test/vault"
        mock_get_config.return_value = mock_config
        
        # Mock the scheduler
        mock_scheduler = MagicMock()
        mock_scheduler_class.return_value = mock_scheduler
        
        from cobalt_agent.services.scheduler import CobaltScheduler
        
        scheduler = CobaltScheduler()
        scheduler.shutdown()
        
        # Verify scheduler.shutdown() was called
        mock_scheduler.shutdown.assert_called_once()
    
    @patch("cobalt_agent.services.scheduler.BackgroundScheduler")
    @patch("cobalt_agent.services.scheduler.get_config")
    @patch("cobalt_agent.services.scheduler.LLM")
    @patch("cobalt_agent.services.scheduler.os")
    @patch("cobalt_agent.services.scheduler.open", create=True)
    def test_generate_morning_briefing(self, mock_open, mock_os, mock_llm_class, mock_get_config, mock_scheduler_class):
        """Test that generate_morning_briefing generates and saves the briefing."""
        # Mock the config
        mock_config = MagicMock()
        mock_config.system.obsidian_vault_path = "/test/vault"
        mock_get_config.return_value = mock_config
        
        # Mock the scheduler
        mock_scheduler = MagicMock()
        mock_scheduler_class.return_value = mock_scheduler
        
        # Mock the LLM
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask.return_value = "Market Analysis\n\nSummary: Buy stocks"
        mock_llm_class.return_value = mock_llm_instance
        
        from cobalt_agent.services.scheduler import CobaltScheduler
        
        scheduler = CobaltScheduler()
        scheduler.generate_morning_briefing()
        
        # Verify LLM was called
        mock_llm_instance.ask.assert_called_once()
        
        # Verify os.makedirs was called to create directory
        mock_os.makedirs.assert_called_once()
        
        # Verify file was opened for writing
        mock_open.assert_called_once()
        
        # Verify write was called
        write_call = mock_open.return_value.__enter__.return_value.write
        write_call.assert_called_once()
    
    @patch("cobalt_agent.services.scheduler.BackgroundScheduler")
    @patch("cobalt_agent.services.scheduler.get_config")
    def test_scheduler_has_correct_job_count(self, mock_get_config, mock_scheduler_class):
        """Test that scheduler has exactly one job registered."""
        # Mock the config
        mock_config = MagicMock()
        mock_config.system.obsidian_vault_path = "/test/vault"
        mock_get_config.return_value = mock_config
        
        # Mock the scheduler
        mock_scheduler = MagicMock()
        mock_scheduler_class.return_value = mock_scheduler
        
        from cobalt_agent.services.scheduler import CobaltScheduler
        
        scheduler = CobaltScheduler()
        
        # Only one job should be registered (morning_briefing)
        mock_scheduler.add_job.assert_called_once()
    
    @patch("cobalt_agent.services.scheduler.BackgroundScheduler")
    @patch("cobalt_agent.services.scheduler.get_config")
    def test_scheduler_replaces_existing_job(self, mock_get_config, mock_scheduler_class):
        """Test that jobs are set to replace_existing=True."""
        # Mock the config
        mock_config = MagicMock()
        mock_config.system.obsidian_vault_path = "/test/vault"
        mock_get_config.return_value = mock_config
        
        # Mock the scheduler
        mock_scheduler = MagicMock()
        mock_scheduler_class.return_value = mock_scheduler
        
        from cobalt_agent.services.scheduler import CobaltScheduler
        
        scheduler = CobaltScheduler()
        
        # Get the call arguments
        call_kwargs = mock_scheduler.add_job.call_args[1]
        
        # Verify replace_existing is True
        assert call_kwargs["replace_existing"] is True