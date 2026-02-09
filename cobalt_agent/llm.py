"""
Cobalt Agent - LLM (The Brain)
Handles communication with AI providers (OpenAI, Gemini, Anthropic) via LiteLLM.
"""

import os
from typing import List, Dict, Any, Optional

# <--- ADDED: Pydantic imports for validation
from pydantic import BaseModel, Field, SecretStr
from loguru import logger
from litellm import completion

# <--- ADDED: Helper model for message structure
class Message(BaseModel):
    role: str
    content: str


class LLM(BaseModel):
    """
    The Brain of the agent. 
    Processes prompts and returns intelligent responses.
    """
    
    # <--- CHANGED: Using Pydantic fields instead of __init__
    model_name: str = Field(..., description="The model to use (e.g., 'gpt-4o')")
    api_key: Optional[SecretStr] = Field(default=None, description="API Key (optional if in env vars)")

    def model_post_init(self, __context: Any) -> None:
        """
        Post-initialization hook to validate API key.
        """
        # Check if key is provided directly or exists in env
        if not self.api_key and not os.getenv("COBALT_LLM_KEY") and not os.getenv("OPENAI_API_KEY"):
            logger.warning("No API Key found for LLM. Agent will fail if asked to think.")
        else:
            logger.info(f"LLM Initialized: {self.model_name}")

    def think(self, 
              user_input: str, 
              system_prompt: str, 
              memory_context: List[Dict] = None,
              search_context: str = "") -> str:
        """
        Send a prompt to the AI and get a response.

        Args:
            user_input: What the user just said.
            system_prompt: Who the agent is (Persona).
            memory_context: List of previous chat messages.
            search_context: Results from search tools (optional).

        Returns:
            str: The AI's text response.
        """
        messages = []

        # 1. System Prompt (The Persona)
        messages.append({"role": "system", "content": system_prompt})

        # 2. Memory Context (Short-term history)
        if memory_context:
            for log in memory_context:
                # Filter: Only send User or Assistant messages to the brain
                if log.get("source") in ["User", "Assistant"]:
                    role = "user" if log["source"] == "User" else "assistant"
                    content = log.get("message", "")
                    messages.append({"role": role, "content": content})

        # 3. Search Context (Inject data if we have it)
        if search_context:
            messages.append({
                "role": "system", 
                "content": f"Relevant Information from Search Tools:\n{search_context}"
            })

        # 4. Current User Input
        messages.append({"role": "user", "content": user_input})

        try:
            logger.info(f"Sending request to {self.model_name}...")
            
            # Get key string safely if it exists
            key_str = self.api_key.get_secret_value() if self.api_key else None
            
            # Call the AI
            response = completion(
                model=self.model_name,
                messages=messages,
                api_key=key_str,
                temperature=0.7 
            )
            
            # Extract text
            reply = response.choices[0].message.content
            return reply

        except Exception as e:
            logger.error(f"LLM Brain Freeze: {str(e)}")
            return f"Error: My brain is not working. ({str(e)})"