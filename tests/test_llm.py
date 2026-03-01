"""
LLM Tests
Tests for the LLM (Language Model) class with proper mocking of external API calls.
"""
from unittest.mock import patch, MagicMock
import pytest

from cobalt_agent.llm import LLM


class TestLLM:
    """Test suite for LLM class."""
    
    @pytest.fixture
    def mock_config(self):
        """Mock configuration to return test data."""
        config = MagicMock()
        config.active_profile = {
            "default": "test-model"
        }
        config.models = {
            "test-model": {
                "provider": "openai",
                "model_name": "gpt-4",
                "env_key_ref": "OPENAI_API_KEY"
            }
        }
        config.network = MagicMock(nodes={})
        config.model_dump.return_value = {
            "keys": {
                "OPENAI_API_KEY": "TEST_API_KEY"
            }
        }
        return config
    
    def test_llm_initialization_with_default_role(self, mock_config):
        """Test LLM initialization with default role."""
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="default")
            
            assert llm.role == "default"
            assert llm.model_name == "openai/gpt-4"
    
    def test_llm_initialization_with_custom_role(self, mock_config):
        """Test LLM initialization with a custom role."""
        mock_config.active_profile = {
            "custom_role": "custom-model"
        }
        mock_config.models = {
            "custom-model": {
                "provider": "anthropic",
                "model_name": "claude-3",
                "env_key_ref": "ANTHROPIC_API_KEY"
            }
        }
        
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="custom_role")
            
            assert llm.role == "custom_role"
            assert llm.model_name == "anthropic/claude-3"
    
    def test_switch_role_updates_model(self, mock_config):
        """Test that switch_role properly updates the model."""
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="default")
            initial_model = llm.model_name
            
            mock_config.active_profile = {
                "default": "test-model",
                "strategist": "strategist-model"
            }
            mock_config.models = {
                "test-model": {
                    "provider": "openai",
                    "model_name": "gpt-4"
                },
                "strategist-model": {
                    "provider": "anthropic",
                    "model_name": "claude-3"
                }
            }
            
            llm.switch_role("strategist")
            
            assert llm.role == "strategist"
            assert llm.model_name == "anthropic/claude-3"
    
    def test_generate_response_calls_completion(self, mock_config):
        """Test that generate_response properly calls the LLM provider."""
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="default")
            
            with patch("cobalt_agent.llm.completion") as mock_completion:
                mock_response = MagicMock()
                mock_response.choices = [MagicMock()]
                mock_response.choices[0].message = MagicMock()
                mock_response.choices[0].message.content = "Test response"
                mock_completion.return_value = mock_response
                
                result = llm.generate_response(
                    system_prompt="You are a helpful assistant",
                    user_input="Hello"
                )
                
                assert result == "Test response"
                mock_completion.assert_called_once()
    
    def test_ask_method_calls_completion(self, mock_config):
        """Test that ask method calls completion with proper messages."""
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="default")
            
            with patch("cobalt_agent.llm.completion") as mock_completion:
                mock_response = MagicMock()
                mock_response.choices = [MagicMock()]
                mock_response.choices[0].message = MagicMock()
                mock_response.choices[0].message.content = "Direct answer"
                mock_completion.return_value = mock_response
                
                result = llm.ask("System prompt", "User input")
                
                assert result == "Direct answer"
                
                # Verify the messages were passed correctly
                call_kwargs = mock_completion.call_args[1]
                messages = call_kwargs["messages"]
                assert messages[0]["role"] == "system"
                assert messages[0]["content"] == "System prompt"
                assert messages[1]["role"] == "user"
                assert messages[1]["content"] == "User input"
    
    def test_ask_structured_returns_pydantic_model(self, mock_config):
        """Test that ask_structured returns a validated Pydantic model."""
        from pydantic import BaseModel, Field
        
        class TestModel(BaseModel):
            name: str
            value: int
        
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="default")
            
            with patch("cobalt_agent.llm.completion") as mock_completion:
                mock_response = MagicMock()
                mock_response.choices = [MagicMock()]
                mock_response.choices[0].message = MagicMock()
                # Return raw JSON as the LLM would
                mock_response.choices[0].message.content = '{"name": "test", "value": 42}'
                mock_completion.return_value = mock_response
                
                result = llm.ask_structured("Test prompt", TestModel)
                
                assert isinstance(result, TestModel)
                assert result.name == "test"
                assert result.value == 42
    
    def test_llm_api_base_resolved_for_local_model(self):
        """Test that API base is correctly resolved for local models."""
        config = MagicMock()
        config.active_profile = {
            "local-model": "local-model"
        }
        config.models = {
            "local-model": {
                "provider": "ollama",
                "model_name": "llama2",
                "node_ref": "local-node"
            }
        }
        config.network.nodes = {
            "local-node": {
                "ip": "192.168.1.100",
                "port": 11434,
                "protocol": "http"
            }
        }
        config.model_dump.return_value = {
            "keys": {}
        }
        
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = config
            
            llm = LLM(role="local-model")
            
            assert llm._api_base == "http://192.168.1.100:11434"
    
    def test_llm_no_api_base_for_cloud_model(self, mock_config):
        """Test that API base is None for cloud models."""
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="default")
            
            assert llm._api_base is None
    
    def test_ask_structured_contains_both_system_prompt_and_json_schema(self, mock_config):
        """Test that ask_structured combines system_prompt with JSON schema instructions."""
        from pydantic import BaseModel, Field
        import json
        
        class TestModel(BaseModel):
            name: str
            value: int
        
        with patch("cobalt_agent.config.load_config") as mock_load:
            mock_load.return_value = mock_config
            
            llm = LLM(role="default")
            
            # Personas instructions that should be preserved
            persona_instructions = "You are a senior software architect. Follow best practices."
            
            with patch("cobalt_agent.llm.completion") as mock_completion:
                mock_response = MagicMock()
                mock_response.choices = [MagicMock()]
                mock_response.choices[0].message = MagicMock()
                mock_response.choices[0].message.content = '{"name": "test", "value": 42}'
                mock_completion.return_value = mock_response
                
                llm.ask_structured(persona_instructions, TestModel)
                
                # Verify the messages were passed correctly
                call_kwargs = mock_completion.call_args[1]
                messages = call_kwargs["messages"]
                
                # Check that we have a system message
                assert messages[0]["role"] == "system"
                
                # Get the combined system message
                combined_message = messages[0]["content"]
                
                # Verify persona instructions are present
                assert persona_instructions in combined_message
                
                # Verify JSON schema instructions are present
                assert "You are a precise data output engine" in combined_message
                
                # Verify the schema is included
                schema_str = json.dumps(TestModel.model_json_schema(), indent=2)
                assert schema_str in combined_message
