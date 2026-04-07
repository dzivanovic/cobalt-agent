"""
Cobalt Agent - LLM (The Brain)
Handles communication with AI providers via LiteLLM.
Unified interface supporting Chat, Direct Queries, and Structured Data extraction.
"""

import os
import json
from typing import List, Dict, Any, Optional, Type, TypeVar
from pydantic import BaseModel, Field, SecretStr, ValidationError
from loguru import logger
from litellm import completion

# Generic type for Pydantic models
T = TypeVar("T", bound=BaseModel)

class LLM(BaseModel):
    """
    The Brain of the agent. 
    Processes prompts and returns intelligent responses.
    """
    
    # Configuration
    role: str = Field("default", description="The role to use for model selection")
    api_key: Optional[SecretStr] = Field(default=None, description="API Key (optional if in env vars)")
    
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self._resolve_model_config()
        
    # Model name property
    @property
    def model_name(self) -> str:
        """Public property to access the resolved model name."""
        return self._model_name
    
    def switch_role(self, new_role: str) -> None:
        """
        Switch to a new role and re-resolve the model configuration.
        This allows hot-swapping between different models (e.g., Qwen 80B -> DeepSeek 70B).
        """
        self.role = new_role
        self._resolve_model_config()
        logger.info(f"Role switched to '{new_role}', model updated to: {self._model_name}")
    
    def _resolve_model_config(self) -> None:
        from cobalt_agent.config import get_config
        config = get_config()
        
        active_profile = config.active_profile
        model_alias = active_profile.get(self.role, active_profile.get("default"))

        if model_alias not in config.models:
            raise ValueError(f"Model alias '{model_alias}' not found in registry.")
            
        model_config = config.models[model_alias]
        
        if isinstance(model_config, dict):
            provider = model_config.get("provider")
            name = model_config.get("model_name")
            self._node_ref = model_config.get("node_ref")
            self._env_key_ref = model_config.get("env_key_ref")
        else:
            provider = model_config.provider
            name = model_config.model_name
            self._node_ref = getattr(model_config, "node_ref", None)
            self._env_key_ref = getattr(model_config, "env_key_ref", None)

        self._model_name = f"{provider}/{name}"
        self._model_config = model_config

        self._api_base = None
        if self._node_ref:
            nodes = config.network.nodes
            target_node = nodes.get(self._node_ref) if isinstance(nodes, dict) else getattr(nodes, self._node_ref, None)
            
            if target_node:
                ip = target_node.get("ip") if isinstance(target_node, dict) else target_node.ip
                port = target_node.get("port") if isinstance(target_node, dict) else target_node.port
                protocol = target_node.get("protocol", "http") if isinstance(target_node, dict) else getattr(target_node, "protocol", "http")
                self._api_base = f"{protocol}://{ip}:{port}/v1"

    def _call_provider(self, messages: List[Dict[str, str]], tools: Optional[List[Dict]] = None, temperature: float = 0.7, max_tokens: int = 4000, response_format: Optional[Dict] = None) -> str:
        try:
            from cobalt_agent.config import get_config
            import os
            
            config = get_config()
            
            api_key = None
            if self._env_key_ref:
                # ZERO-TRUST VAULT EXTRACTION
                try:
                    keys_dict = {}
                    
                    # Try 1: If config is a dict (or dict-like)
                    if hasattr(config, "get"):
                        keys_dict = config.get("keys", {})
                    # Try 2: If config is a Pydantic object
                    elif hasattr(config, "model_dump"):
                        keys_dict = config.model_dump().get("keys", {})
                    # Try 3: Direct attribute fallback
                    elif hasattr(config, "keys"):
                        keys_obj = config.keys
                        keys_dict = keys_obj.model_dump() if hasattr(keys_obj, "model_dump") else dict(keys_obj)
                        
                    # Now extract from the dictionary exactly as we see it in the logs
                    target_key_name = keys_dict.get(self._env_key_ref, f"{self._env_key_ref.upper()}_API_KEY")
                    
                    # Grab the actual AIzaSy... hash!
                    api_key = keys_dict.get(target_key_name)
                    
                    # Fallback to standard OS env if it wasn't in the dict
                    if not api_key:
                        api_key = os.getenv(target_key_name)
                        
                except Exception as e:
                    from loguru import logger
                    logger.error(f"Vault extraction fault: {e}")
                
                if not api_key:
                    from loguru import logger
                    logger.warning(f"CRITICAL: Failed to extract actual hash for '{self._env_key_ref}' from Vault RAM.")
            
            # Local model requires a dummy key for LiteLLM to pass validation
            if not api_key and self._api_base:
                api_key = "dummy-local-key"

            has_user = any(msg.get("role") == "user" for msg in messages)
            if not has_user:
                messages.append({"role": "user", "content": "Analyze system prompt and execute."})

            kwargs = {
                "model": self._model_name,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            if self._api_base:
                kwargs["api_base"] = self._api_base
            if api_key:
                kwargs["api_key"] = api_key
            if tools:
                kwargs["tools"] = tools
            if response_format:
                kwargs["response_format"] = response_format
                
            from loguru import logger
            logger.debug(f"Executing: {self._model_name} | Base: {self._api_base}")
            
            from litellm import completion
            response = completion(**kwargs)
            
            if not response.choices or not response.choices[0].message:
                 raise ValueError("Empty response from provider")
                 
            return response.choices[0].message.content.strip()

        except Exception as e:
            from loguru import logger
            logger.error(f"LLM Call Failed: {str(e)}")
            raise e

    # --- 1. THE CHAT INTERFACE (For Main Loop) ---
    def generate_response(self,
                        system_prompt: Optional[str] = None,
                        user_input: Optional[str] = None,
                        memory_context: Optional[List[Dict]] = None,
                        search_context: str = "",
                        tools: Optional[List[Dict]] = None) -> str:
        """
        Main conversational loop method. Handles history and context injection.
        
        Args:
            system_prompt: System-level instructions for the LLM
            user_input: User's current input message
            memory_context: Optional list of previous messages for conversation history
            search_context: Legacy context injection (for backward compatibility)
            tools: Optional list of tool definitions for grounding (e.g., googleSearch)
        """
        messages = []

        # A. System Prompt
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        # B. Memory Context
        if memory_context:
            for item in memory_context:
                # Case 1: Memory Log (Standard)
                if "source" in item:
                    role = "user" if item["source"] == "User" else "assistant"
                    messages.append({"role": role, "content": item["message"]})
                
                # Case 2: Tool Loop Message (Raw)
                elif "role" in item:
                    messages.append({"role": item["role"], "content": item["content"]})

        # C. Search Context (Legacy/Injection)
        if search_context:
            messages.append({
                "role": "user", 
                "content": f"Context Information:\n{search_context}"
            })

        # D. Current Input
        if user_input:
            messages.append({"role": "user", "content": user_input})

        try:
            response = self._call_provider(messages, tools=tools)
            logger.info(f"Cobalt, LLM model version: {self.model_name}")
            logger.info(f"Persona Roles: Chief of Staff, Software Architect, Senior Developer, Business Analyst")
            return response
        except Exception as e:
            logger.error(f"LLM Call Failed: {str(e)}")
            raise e

    # --- 2. THE SKILL INTERFACE (For Tools & Research) ---
    def generate_response_skill(self, prompt: str) -> str:
        return self.generate_response(
            system_prompt=prompt,
            user_input=None,
            memory_context=None,
            search_context=""
        )

    def ask(self, 
            system_message: str,
            user_input: Optional[str] = None,
            tools: Optional[List[Dict]] = None,
            temperature: float = 0.7,
            max_tokens: int = 4000,
            response_format: Optional[Dict] = None) -> str:
        """
        Direct one-off query. Used by skills like Research or Briefing.
        
        Args:
            system_message: System-level instructions for the LLM
            user_input: Optional user input message
            tools: Optional list of tool definitions for grounding (e.g., googleSearch)
            response_format: Optional response format specification (e.g., {"type": "json_object"})
        """
        messages = [
            {"role": "system", "content": system_message}
        ]

        if user_input:
            messages.append({"role": "user", "content": user_input})

        try:
            return self._call_provider(messages, tools=tools, temperature=temperature, max_tokens=max_tokens, response_format=response_format)
        except Exception as e:
            logger.error(f"Ask Failed: {e}")
            raise e

    # --- 3. THE STRUCTURED INTERFACE (For Strict Data) ---
    def ask_structured(self, 
                    system_prompt: str, 
                    response_model: Type[T],
                    memory_context: Optional[List[Dict]] = None,
                    search_context: str = "", 
                    user_input: Optional[str] = None,
                    tools: Optional[List[Dict]] = None) -> T:
        """
        Forces the LLM to output JSON conforming to a Pydantic model.
        Returns the instantiated Pydantic object.
        
        Combines the caller's system_prompt (persona instructions) with
        JSON schema validation instructions.
        
        Args:
            system_prompt: System-level instructions for the LLM
            response_model: Pydantic model class to validate output against
            memory_context: Optional list of previous messages for conversation history
            search_context: Legacy context injection (for backward compatibility)
            user_input: Optional user input message
            tools: Optional list of tool definitions for grounding (e.g., googleSearch)
        """
        # Get the schema from the model
        schema = response_model.model_json_schema()
        
        # Combine system_prompt (persona instructions) with JSON schema instructions
        json_instruction = (
            f"You are a precise data output engine.\n"
            f"You MUST return ONLY valid JSON that matches this schema:\n"
            f"{json.dumps(schema, indent=2)}\n"
            f"Do not include markdown formatting (like ```json). Return raw JSON only."
        )
        
        # Concatenate system_prompt with JSON schema instructions
        combined_system_message = f"{system_prompt}\n\n{json_instruction}"

        messages = [
            {"role": "system", "content": combined_system_message},
        ]

        if memory_context:
            for item in memory_context:
                # Case 1: Memory Log (Standard)
                if "source" in item:
                    role = "user" if item["source"] == "User" else "assistant"
                    messages.append({"role": role, "content": item["message"]})
                
                # Case 2: Tool Loop Message (Raw)
                elif "role" in item:
                    messages.append({"role": item["role"], "content": item["content"]})

        if search_context:
            messages.append({
                "role": "user", 
                "content": f"Context Information:\n{search_context}"
            })

        if user_input:
            messages.append({"role": "user", "content": user_input})

        try:
            raw_response = self._call_provider(messages, tools=tools)
            
            # Clean up potential markdown leakage
            cleaned_json = raw_response.replace("```json", "").replace("```", "").strip()
            
            # Parse and Validate
            return response_model.model_validate_json(cleaned_json)
        
        except ValidationError as e:
            logger.error(f"Structured Data Control Failed: {e}")
            logger.debug(f"Raw Output: {raw_response}")
            raise ValueError(f"LLM failed to generate valid JSON: {e}")
        except Exception as e:
            logger.error(f"Structured Request Failed: {e}")
            raise e