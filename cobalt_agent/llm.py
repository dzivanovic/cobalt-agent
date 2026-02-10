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
    model_name: str = Field(..., description="The model to use (e.g., 'gpt-4o', 'claude-3-opus')")
    api_key: Optional[SecretStr] = Field(default=None, description="API Key (optional if in env vars)")

    def model_post_init(self, __context: Any) -> None:
        """
        Post-initialization hook to validate API key.
        """
        # Check if key is provided directly or exists in env
        # We support COBALT_LLM_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY, etc via LiteLLM
        if not self.api_key and not os.getenv("COBALT_LLM_KEY") and not os.getenv("OPENAI_API_KEY"):
            logger.warning("No API Key found. Agent functionality will be limited.")
        else:
            logger.info(f"LLM Initialized: {self.model_name}")

    def _call_provider(self, messages: List[Dict[str, str]]) -> str:
        """
        Internal helper to send messages to the provider via LiteLLM.
        """
        try:
            # Get key string safely if it exists on the instance
            key_str = self.api_key.get_secret_value() if self.api_key else None
            
            response = completion(
                model=self.model_name,
                messages=messages,
                api_key=key_str,
                temperature=0.7 
            )
            
            if not response.choices or not response.choices[0].message:
                 raise ValueError("Empty response from provider")
                 
            return response.choices[0].message.content.strip()

        except Exception as e:
            logger.error(f"LLM Call Failed: {str(e)}")
            raise e

    # --- 1. THE CHAT INTERFACE (For Main Loop) ---
    def think(self, 
              user_input: str, 
              system_prompt: str, 
              memory_context: List[Dict] = None,
              search_context: str = "") -> str:
        """
        Main conversational loop method. Handles history and context injection.
        """
        messages = []

        # A. System Prompt
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
            return self._call_provider(messages)
        except Exception:
            return "Error: My brain is not working. Check logs."

    # --- 2. THE SKILL INTERFACE (For Tools & Research) ---
    def ask(self, prompt: str, system_message: Optional[str] = None) -> str:
        """
        Direct one-off query. Used by skills like Research or Briefing.
        """
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        
        messages.append({"role": "user", "content": prompt})
        
        try:
            return self._call_provider(messages)
        except Exception as e:
            return f"Error: {e}"

    # --- 3. THE STRUCTURED INTERFACE (For Strict Data) ---
    def ask_structured(self, prompt: str, response_model: Type[T]) -> T:
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
            {"role": "user", "content": prompt}
        ]

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