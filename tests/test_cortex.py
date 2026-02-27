"""
Cortex Router Tests
Tests keyword routing (Fast-path vs Orchestrator) and domain classification.
"""
from unittest.mock import patch, MagicMock
import pytest

from cobalt_agent.brain.cortex import Cortex, DomainDecision


class TestCortexRouting:
    """Test suite for Cortex router."""
    
    @pytest.fixture
    def mock_config(self):
        """Create a mock config with departments and cortex_routing rules."""
        mock = MagicMock()
        mock.departments = {
            "TACTICAL": {"active": True, "description": "Trading operations"},
            "INTEL": {"active": True, "description": "Research and news"},
            "OPS": {"active": True, "description": "Operations and Scribe"},
            "ENGINEERING": {"active": True, "description": "Code work"},
            "DEFAULT": {"active": True, "description": "General chat"}
        }
        # Add cortex_routing rules for fast-path keywords
        mock.rules = MagicMock()
        # Make cortex_routing return a simple object with keyword lists
        cortex_routing = MagicMock()
        cortex_routing.orchestrator_keywords = [
            "engineering", "directory", "file", "codebase", "src/", "list the", 
            "research", "summarize", "ops", "read", "write", "search", "prd"
        ]
        cortex_routing.high_risk_keywords = [
            "delete", "move", "remove", "format", "execute", "kill", "reorganize"
        ]
        mock.rules.cortex_routing = cortex_routing
        return mock
    
    @pytest.fixture
    def mock_llm_instance(self, mock_config):
        """Create a mock LLM instance."""
        mock_llm = MagicMock()
        mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="ENGINEERING",
            reasoning="Code work",
            task_parameters="test"
        )
        return mock_llm
    
    @pytest.fixture
    def cortex_instance(self, mock_config, mock_llm_instance):
        """Create a Cortex instance with mocked config and LLM."""
        with patch("cobalt_agent.brain.cortex.load_config", return_value=mock_config):
            with patch("cobalt_agent.brain.cortex.LLM", return_value=mock_llm_instance):
                cortex = Cortex()
                # Store the mock LLM for later use
                cortex._mock_llm = mock_llm_instance
                return cortex
    
    def test_orchestrator_fast_path_engineering_keyword(self, cortex_instance):
        """Test that 'write' keyword triggers Orchestrator fast-path (code work indicator)."""
        # This test verifies the fast-path routing works
        # The input should trigger fast-path, so we check OrchestratorEngine is called
        with patch("cobalt_agent.core.orchestrator.OrchestratorEngine") as mock_orch:
            mock_orch_instance = MagicMock()
            mock_orch_instance.plan_and_execute.return_value = "Orchestrator executed"
            mock_orch.return_value = mock_orch_instance
            
            result = cortex_instance.route("Please write the new module")
            
            # The fast-path should trigger OrchestratorEngine
            mock_orch.assert_called_once()
            mock_orch_instance.plan_and_execute.assert_called_once_with(
                "Please write the new module"
            )
            assert result == "Orchestrator executed"
    
    def test_orchestrator_fast_path_file_keyword(self, cortex_instance):
        """Test that 'file' keyword triggers Orchestrator fast-path."""
        with patch("cobalt_agent.core.orchestrator.OrchestratorEngine") as mock_orch:
            mock_orch_instance = MagicMock()
            mock_orch_instance.plan_and_execute.return_value = "File operation done"
            mock_orch.return_value = mock_orch_instance
            
            result = cortex_instance.route("Write a file in src/")
            
            mock_orch.assert_called_once()
            assert result == "File operation done"
    
    def test_orchestrator_fast_path_directory_keyword(self, cortex_instance):
        """Test that 'directory' keyword triggers Orchestrator fast-path."""
        with patch("cobalt_agent.core.orchestrator.OrchestratorEngine") as mock_orch:
            mock_orch_instance = MagicMock()
            mock_orch_instance.plan_and_execute.return_value = "Directory listing"
            mock_orch.return_value = mock_orch_instance
            
            result = cortex_instance.route("List the contents of the src directory")
            
            mock_orch.assert_called_once()
            assert result == "Directory listing"
    
    def test_orchestrator_fast_path_list_the_keyword(self, cortex_instance):
        """Test that 'list the' keyword triggers Orchestrator fast-path."""
        with patch("cobalt_agent.core.orchestrator.OrchestratorEngine") as mock_orch:
            mock_orch_instance = MagicMock()
            mock_orch_instance.plan_and_execute.return_value = "Listing completed"
            mock_orch.return_value = mock_orch_instance
            
            result = cortex_instance.route("List the files in the directory")
            
            mock_orch.assert_called_once()
            assert result == "Listing completed"
    
    def test_orchestrator_fast_path_codebase_keyword(self, cortex_instance):
        """Test that 'codebase' keyword triggers Orchestrator fast-path."""
        with patch("cobalt_agent.core.orchestrator.OrchestratorEngine") as mock_orch:
            mock_orch_instance = MagicMock()
            mock_orch_instance.plan_and_execute.return_value = "Code analysis"
            mock_orch.return_value = mock_orch_instance
            
            result = cortex_instance.route("Analyze the codebase structure")
            
            mock_orch.assert_called_once()
            assert result == "Code analysis"
    
    def test_web_search_fast_path_http_url(self, cortex_instance):
        """Test that HTTP URL triggers web search fast-path (returns None)."""
        result = cortex_instance.route("Visit https://example.com")
        # Should return None (handled in main chat loop)
        assert result is None
    
    def test_web_search_fast_path_browser_keyword(self, cortex_instance):
        """Test that 'browser' keyword triggers web search fast-path (returns None)."""
        result = cortex_instance.route("Use browser to scrape the page")
        assert result is None
    
    def test_tactical_routing(self, cortex_instance):
        """Test TACTICAL domain routing for trading queries."""
        # Set up the mock LLM to return TACTICAL decision
        cortex_instance._mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="TACTICAL",
            reasoning="Stock price query",
            task_parameters="NVDA"
        )
        
        with patch("cobalt_agent.brain.tactical.Strategos") as mock_strategos:
            mock_dept = MagicMock()
            mock_dept.run.return_value = "NVDA is trading at $123"
            mock_strategos.return_value = mock_dept
            
            result = cortex_instance.route("What is the current price of NVDA?")
            
            # Verify Strategos was instantiated and run was called
            mock_strategos.assert_called_once()
            mock_dept.run.assert_called_once_with("NVDA")
            assert "NVDA" in result
    
    def test_engineering_routing(self, cortex_instance):
        """Test ENGINEERING domain routing for code work."""
        # Set up the mock LLM to return ENGINEERING decision
        cortex_instance._mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="ENGINEERING",
            reasoning="Code work request",
            task_parameters="Review this function"
        )
        
        with patch("cobalt_agent.brain.engineering.EngineeringDepartment") as mock_eng:
            mock_dept = MagicMock()
            mock_dept.run.return_value = "Code reviewed successfully"
            mock_eng.return_value = mock_dept
            
            # Use a query that does NOT trigger fast-path (avoid: write, fix, update, etc.)
            result = cortex_instance.route("Review this Python function for bugs")
            
            mock_eng.assert_called_once()
            mock_dept.run.assert_called_once()
            assert result == "Code reviewed successfully"
    
    def test_ops_routing(self, cortex_instance):
        """Test OPS domain routing for operations tasks."""
        # Set up the mock LLM to return OPS decision
        cortex_instance._mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="OPS",
            reasoning="Scribe task",
            task_parameters="Log this entry"
        )

        with patch("cobalt_agent.skills.productivity.scribe.Scribe") as mock_scribe:
            mock_scribe_instance = MagicMock()
            mock_scribe_instance.append_to_daily_note.return_value = "Entry logged"
            mock_scribe.return_value = mock_scribe_instance
            
            # Use a query that does NOT trigger fast-path (avoid: save, note, etc.)
            result = cortex_instance.route("Log this entry to my journal")

            mock_scribe_instance.append_to_daily_note.assert_called_once()
            assert result == "Entry logged"

    def test_ops_routing_with_save(self, cortex_instance):
        """Test OPS domain routing with save note action."""
        # Set up the mock LLM to return OPS decision
        cortex_instance._mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="OPS",
            reasoning="Scribe task",
            task_parameters="Note content"
        )

        with patch("cobalt_agent.skills.productivity.scribe.Scribe") as mock_scribe:
            mock_scribe_instance = MagicMock()
            mock_scribe_instance.write_note.return_value = "Note saved"
            mock_scribe.return_value = mock_scribe_instance

            # Use a query that does NOT trigger fast-path (avoid: write, file, directory, etc.)
            # and contains "save" to trigger write_note
            result = cortex_instance.route("Save the project notes for later review")

            # The write_note should be called when "save" is in the prompt
            mock_scribe_instance.write_note.assert_called_once()
            assert result == "Note saved"

    def test_ops_routing_with_search(self, cortex_instance):
        """Test OPS domain routing with search action."""
        # Set up the mock LLM to return OPS decision
        cortex_instance._mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="OPS",
            reasoning="Search task",
            task_parameters="medical billing"
        )

        with patch("cobalt_agent.skills.productivity.scribe.Scribe") as mock_scribe:
            mock_scribe_instance = MagicMock()
            mock_scribe_instance.search_vault.return_value = ["Note 1", "Note 2"]
            mock_scribe.return_value = mock_scribe_instance

            # Use a query that contains "find" to trigger search (but NOT trigger fast-path)
            # "find" is in orchestrator_keywords but "find the" should work
            result = cortex_instance.route("Find the vault records for medical billing")

            mock_scribe_instance.search_vault.assert_called_once_with("medical billing")
            assert "Found these notes" in result
    
    def test_default_routing_for_general_queries(self, cortex_instance):
        """Test DEFAULT routing for general conversation."""
        # Set up the mock LLM to return DEFAULT decision
        cortex_instance._mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="DEFAULT",
            reasoning="General chat",
            task_parameters="chat"
        )
        
        result = cortex_instance.route("Hi, how are you today?")
        
        # Should return None (handled in main chat loop)
        assert result is None
    
    def test_intel_routing(self, cortex_instance):
        """Test INTEL domain routing for research queries."""
        # Set up the mock LLM to return INTEL decision
        cortex_instance._mock_llm.ask_structured.return_value = DomainDecision(
            domain_name="INTEL",
            reasoning="Research query",
            task_parameters="Latest AI developments"
        )
        
        with patch("cobalt_agent.skills.research.deep_dive.DeepResearch") as mock_research:
            mock_research_instance = MagicMock()
            mock_research_instance.run.return_value = "Research summary"
            mock_research.return_value = mock_research_instance
            
            result = cortex_instance.route("What are the latest AI developments?")
            
            mock_research.assert_called_once()
            mock_research_instance.run.assert_called_once_with("Latest AI developments")
            assert result == "Research summary"
    
    def test_high_risk_detection(self, cortex_instance):
        """Test that high-risk actions trigger proposal generation."""
        with patch.object(cortex_instance, '_generate_proposal') as mock_proposal:
            mock_proposal.return_value = "Proposal generated"

            # Use a query that does NOT trigger fast-path (avoid: write, execute, reorganize, etc.)
            # and DOES contain high-risk keywords for proposal trigger
            # "move" is a high-risk keyword, but NOT in orchestrator_keywords
            result = cortex_instance.route("Move the database to a new server")

            mock_proposal.assert_called_once()
            assert "Proposal" in result or "BLOCKED" in result
    
    def test_classification_error_handling(self, cortex_instance):
        """Test fallback when classification fails."""
        # Make the LLM raise an exception
        cortex_instance._mock_llm.ask_structured.side_effect = Exception("Classification failed")
        
        # Use a query that does NOT trigger fast-path
        # Avoid: engineering, file, directory, codebase, list the, research, read, write, search, prd
        # Avoid: http://, https://, browser, scrape, search, summarize the top
        result = cortex_instance.route("Analyze the market structure")
        
        # Should fallback to FOUNDATION domain when classification fails, which returns None
        assert result is None
