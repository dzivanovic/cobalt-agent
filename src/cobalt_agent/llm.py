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
        from cobalt_agent.config import load_config
        # Load the configuration object
        config = load_config()
        
        # Debugging: Print the config object to verify its attributes
        logger.debug(f"Config Object: {config.__dict__}")
        # 1. Resolve the Model Alias (Intent -> Alias)
        active_profile = config.active_profile
        
        model_alias = active_profile.get(self.role, active_profile.get("default"))

        # 2. Retrieve Model Config (Alias -> Config)
        if model_alias not in config.models:
            raise ValueError(f"Model alias '{model_alias}' not found in registry.")
            
        model_config = config.models[model_alias]
        
        # 3. Construct Model String
        if isinstance(model_config, dict):
            provider = model_config.get("provider")
            name = model_config.get("model_name")
            node_ref = model_config.get("node_ref")
            env_key_ref = model_config.get("env_key_ref")
        else:
            provider = model_config.provider
            name = model_config.model_name
            node_ref = getattr(model_config, "node_ref", None)
            env_key_ref = getattr(model_config, "env_key_ref", None)

        self._model_name = f"{provider}/{name}"

        # 4. Resolve Network or Keys
        if node_ref:
            nodes = config.network.nodes
            target_node = nodes.get(node_ref) if isinstance(nodes, dict) else getattr(nodes, node_ref, None)
            
            if not target_node:
                raise ValueError(f"Node reference '{node_ref}' not found in network topology.")
            
            if isinstance(target_node, dict):
                ip = target_node.get("ip")
                port = target_node.get("port")
                protocol = target_node.get("protocol", "http")
            else:
                ip = target_node.ip
                port = target_node.port
                protocol = getattr(target_node, "protocol", "http")

            self._api_base = f"{protocol}://{ip}:{port}"
            
        elif env_key_ref:
            keys = config.keys
            env_var_name = keys.get(env_key_ref) if isinstance(keys, dict) else getattr(keys, env_key_ref, None)
            
            if env_var_name:
                self.api_key = SecretStr(os.getenv(env_var_name, ""))
        
    def _call_provider(self, messages: List[Dict[str, str]]) -> str:
        """
        Internal helper to send messages to the provider via LiteLLM.
        """
        try:
            # Get key string safely if it exists on the instance
            key_str = self.api_key.get_secret_value() if self.api_key else None
            
            api_base = self._api_base
            
            # Make the call
            response = completion(
                model=self._model_name,
                messages=messages,
                api_key=key_str,
                base_url=api_base,  
                temperature=0.7 
            )
            
            if not response.choices or not response.choices[0].message:
                 raise ValueError("Empty response from provider")
                 
            return response.choices[0].message.content.strip()

        except Exception as e:
            logger.error(f"LLM Call Failed: {str(e)}")
            raise e

    # --- 1. THE CHAT INTERFACE (For Main Loop) ---
    def generate_response(self,
                          system_prompt: str,
                          user_input: Optional[str] = None,
                          memory_context: List[Dict] = None,
                          search_context: str = "") -> str:
        """
        Main conversational loop method. Handles history and context injection.
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
            response = self._call_provider(messages)
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
            user_input: Optional[str] = None) -> str:
        """
        Direct one-off query. Used by skills like Research or Briefing.
        """
        messages = [
            {"role": "system", "content": system_message},
        ]

        if user_input:
            messages.append({"role": "user", "content": user_input})

        try:
            return self._call_provider(messages)
        except Exception as e:
            logger.error(f"Ask Failed: {str(e)}")
            raise e

    # --- 3. THE STRUCTURED INTERFACE (For Strict Data) ---
    def ask_structured(self, 
                       system_prompt: str, 
                       response_model: Type[T],
                       memory_context: List[Dict] = None,
                       search_context: str = "", 
                       user_input: Optional[str] = None) -> T:
        """
        Forces the LLM to output JSON conforming to a Pydantic model.
        Returns the instantiated Pydantic object.
        """
        # Get the schema from the model
        schema = response_model.model_json_schema()
        
        system_instruction = (
            f"You are a precise data output engine.\n"
            f"You MUST return ONLY valid JSON that matches this schema:\n"
            f"{json.dumps(schema, indent=2)}\n"
            f"Do not include markdown formatting (like ```json). Return raw JSON only."
        )

        messages = [
            {"role": "system", "content": system_instruction},
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
            raw_response = self._call_provider(messages)
            
            # Clean up potential markdown leakage
            cleaned_json = raw_response.replace("```json", "").replace("```", "").strip()
            
            # Parse and Validate
            return response_model.model_validate_json(cleaned_json)
            
        except ValidationError as e:
            logger.error(f"Structured Data Validation Failed: {e}")
            logger.debug(f"Raw Output: {raw_response}")
            raise ValueError(f"LLM failed to generate valid JSON: {e}")
        except Exception as e:
            logger.error(f"Structured Request Failed: {e}")
            raise e