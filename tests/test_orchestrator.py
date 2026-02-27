"""
Orchestrator Engine Tests
Tests the OrchestratorEngine with mocked LLM returns for plan generation and Drone execution.
"""
from unittest.mock import patch, MagicMock, PropertyMock
import pytest
from pydantic import BaseModel, Field
from typing import List

from cobalt_agent.core.orchestrator import OrchestratorEngine, SubTask, OrchestrationState


# Note: These are test-specific models, not prefixed with 'Test' to avoid pytest collection warnings
class MockSubTask(BaseModel):
    """Test SubTask model with different assigned drones."""
    step_number: int
    assigned_drone: str
    action: str
    tool_to_use: str
    status: str = "PENDING"
    observation: str = ""


class MockOrchestrationState(BaseModel):
    """Test state with mock data."""
    scratchpad: str
    original_request: str
    master_plan: List[MockSubTask]
    current_step: int = 1
    status: str = "PLANNING"


class TestOrchestratorEngineClass:
    """Test suite for OrchestratorEngine."""
    
    @pytest.fixture
    def mock_orchestrator(self):
        """Create an OrchestratorEngine instance."""
        return OrchestratorEngine()
    
    @pytest.fixture
    def mock_plan_state(self):
        """Create a mock OrchestrationState with valid plan."""
        return OrchestrationState(
            scratchpad="I will analyze the request and break it down into steps.",
            original_request="Create a test file",
            master_plan=[
                SubTask(
                    step_number=1,
                    assigned_drone="ENGINEERING",
                    action="Create test file",
                    tool_to_use="write_file",
                    status="PENDING"
                )
            ],
            current_step=1,
            status="PLANNING"
        )
    
    @patch("cobalt_agent.core.orchestrator.LLM")
    def test_plan_and_execute_creates_plan(self, mock_llm_class, mock_plan_state):
        """Test that plan_and_execute generates a valid plan."""
        # Configure the mock LLM to return our mock state
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask_structured.return_value = mock_plan_state
        mock_llm_class.return_value = mock_llm_instance
        
        orchestrator = OrchestratorEngine()
        
        result = orchestrator.plan_and_execute("Create a test file")
        
        # Verify LLM was called with structured interface
        mock_llm_instance.ask_structured.assert_called_once()
        call_kwargs = mock_llm_instance.ask_structured.call_args[1]
        assert call_kwargs["response_model"] == OrchestrationState
        assert "ARCHITECT" in call_kwargs["system_prompt"].upper()
    
    @patch("cobalt_agent.core.orchestrator.LLM")
    @patch("cobalt_agent.brain.engineering.EngineeringDepartment")
    def test_plan_and_execute_creates_engineering_drone(self, mock_eng_class, mock_llm_class, mock_plan_state):
        """Test that ENGINEERING drone is instantiated for ENGINEERING tasks."""
        # Configure the mock LLM to return our mock state
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask_structured.return_value = mock_plan_state
        mock_llm_class.return_value = mock_llm_instance
        
        # Configure the Engineering drone mock
        mock_drone_instance = MagicMock()
        mock_drone_instance.run.return_value = "File created successfully"
        mock_eng_class.return_value = mock_drone_instance
        
        orchestrator = OrchestratorEngine()
        result = orchestrator.plan_and_execute("Write Python code")
        
        # Verify Engineering drone was instantiated
        mock_eng_class.assert_called_once()
    
    @patch("cobalt_agent.core.orchestrator.LLM")
    @patch("cobalt_agent.brain.ops.OpsDepartment")
    def test_plan_and_execute_creates_ops_drone(self, mock_ops_class, mock_llm_class):
        """Test that OPS drone is instantiated for OPS tasks."""
        # Create a plan with OPS assigned
        ops_state = OrchestrationState(
            scratchpad="I will search and summarize.",
            original_request="Find information",
            master_plan=[
                SubTask(
                    step_number=1,
                    assigned_drone="OPS",
                    action="Search knowledge base",
                    tool_to_use="search_knowledge",
                    status="PENDING"
                )
            ],
            current_step=1,
            status="PLANNING"
        )
        
        # Configure the mock LLM
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask_structured.return_value = ops_state
        mock_llm_class.return_value = mock_llm_instance
        
        # Configure the OPS drone mock
        mock_drone_instance = MagicMock()
        mock_drone_instance.run.return_value = "Information found"
        mock_ops_class.return_value = mock_drone_instance
        
        orchestrator = OrchestratorEngine()
        result = orchestrator.plan_and_execute("Find information")
        
        # Verify Ops drone was instantiated
        mock_ops_class.assert_called_once()
    
    @patch("cobalt_agent.core.orchestrator.LLM")
    def test_plan_and_execute_handles_empty_plan(self, mock_llm_class):
        """Test that empty plans are handled with a failsafe error."""
        # Configure the mock LLM to raise exception (simulating empty plan handling)
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask_structured.side_effect = Exception("Parsing failed - empty plan")
        mock_llm_class.return_value = mock_llm_instance
        
        orchestrator = OrchestratorEngine()
        result = orchestrator.plan_and_execute("Test request")
        
        # Verify error message for empty plan
        assert "Architect Error" in result
        assert "failed to generate a valid plan" in result.lower()
    
    @patch("cobalt_agent.core.orchestrator.LLM")
    def test_plan_and_execute_executes_all_steps(self, mock_llm_class, mock_plan_state):
        """Test that all steps in the plan are executed."""
        # Create a plan with multiple steps
        multi_step_state = OrchestrationState(
            scratchpad="Execute multiple steps.",
            original_request="Complete multi-step task",
            master_plan=[
                SubTask(
                    step_number=1,
                    assigned_drone="ENGINEERING",
                    action="Step 1",
                    tool_to_use="read_file",
                    status="PENDING",
                    observation=""
                ),
                SubTask(
                    step_number=2,
                    assigned_drone="OPS",
                    action="Step 2",
                    tool_to_use="write_file",
                    status="PENDING",
                    observation=""
                ),
                SubTask(
                    step_number=3,
                    assigned_drone="ENGINEERING",
                    action="Step 3",
                    tool_to_use="list_directory",
                    status="PENDING",
                    observation=""
                )
            ],
            current_step=1,
            status="PLANNING"
        )
        
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask_structured.return_value = multi_step_state
        mock_llm_class.return_value = mock_llm_instance
        
        orchestrator = OrchestratorEngine()
        result = orchestrator.plan_and_execute("Multi-step task")
        
        # Verify execution output contains all steps
        assert "Step 1" in result
        assert "Step 2" in result
        assert "Step 3" in result
    
    @patch("cobalt_agent.core.orchestrator.LLM")
    @patch("cobalt_agent.brain.engineering.EngineeringDepartment")
    def test_plan_and_execute_stops_on_error(self, mock_eng_class, mock_llm_class):
        """Test that execution stops when a step fails."""
        error_state = OrchestrationState(
            scratchpad="Stop on error.",
            original_request="Error task",
            master_plan=[
                SubTask(
                    step_number=1,
                    assigned_drone="ENGINEERING",
                    action="Working step",
                    tool_to_use="read_file",
                    status="PENDING",
                    observation=""
                ),
                SubTask(
                    step_number=2,
                    assigned_drone="ENGINEERING",
                    action="Should not execute",
                    tool_to_use="write_file",
                    status="PENDING",
                    observation=""
                )
            ],
            current_step=1,
            status="PLANNING"
        )
        
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask_structured.return_value = error_state
        mock_llm_class.return_value = mock_llm_instance
        
        # Make first step return error
        mock_drone_instance = MagicMock()
        mock_drone_instance.run.return_value = "Error: Something went wrong"
        mock_eng_class.return_value = mock_drone_instance
        
        orchestrator = OrchestratorEngine()
        result = orchestrator.plan_and_execute("Error task")
        
        # Verify error handling - check for error indicator in output
        assert "Error:" in result
        # Verify execution stopped (check for failure message in output)
        assert "Halting execution" in result
    
    @patch("cobalt_agent.core.orchestrator.LLM")
    @patch("cobalt_agent.brain.engineering.EngineeringDepartment")
    def test_plan_and_execute_handles_zero_trust_pause(self, mock_eng_class, mock_llm_class):
        """Test that Zero-Trust pause is handled correctly."""
        pause_state = OrchestrationState(
            scratchpad="Pause for approval.",
            original_request="Pause task",
            master_plan=[
                SubTask(
                    step_number=1,
                    assigned_drone="ENGINEERING",
                    action="Pause step",
                    tool_to_use="write_file",
                    status="PENDING",
                    observation=""
                )
            ],
            current_step=1,
            status="PLANNING"
        )
        
        mock_llm_instance = MagicMock()
        mock_llm_instance.ask_structured.return_value = pause_state
        mock_llm_class.return_value = mock_llm_instance
        
        mock_drone_instance = MagicMock()
        mock_drone_instance.run.return_value = "Action paused. Proposal sent"
        mock_eng_class.return_value = mock_drone_instance
        
        orchestrator = OrchestratorEngine()
        result = orchestrator.plan_and_execute("Pause task")
        
        # Verify Zero-Trust pause message
        assert "Action paused" in result
        assert "HUMAN-IN-THE-LOOP APPROVAL" in result.upper()