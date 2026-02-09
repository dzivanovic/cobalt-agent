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
        """
        messages = []

        # 1. System Prompt (The Persona)
        messages.append({"role": "system", "content": system_prompt})

        # 2. Unified Context Handling
        if memory_context:
            for item in memory_context:
                
                # Case A: It's a Memory Log (from MemorySystem)
                if "source" in item:
                    if item["source"] == "User":
                        messages.append({"role": "user", "content": item["message"]})
                    elif item["source"] == "Assistant":
                        messages.append({"role": "assistant", "content": item["message"]})
                
                # Case B: It's a Tool Loop Message (from interface.py)
                elif "role" in item:
                    messages.append({
                        "role": item["role"], 
                        "content": item["content"]
                    })

        # 3. Search Context (Inject data if we have it)
        # Note: In the new loop, this is mostly handled by observations, 
        # but we keep it for legacy compatibility.
        if search_context:
             messages.append({
                "role": "user", 
                "content": f"Context Information:\n{search_context}"
            })

        # 4. Current User Input
        # Only add if it's not empty (sometimes the loop passes empty input to prompt continuation)
        if user_input:
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
            if not response.choices or not response.choices[0].message:
                 return "Error: Empty response from brain."
                 
            reply = response.choices[0].message.content
            return reply

        except Exception as e:
            logger.error(f"LLM Brain Freeze: {str(e)}")
            return f"Error: My brain is not working. ({str(e)})"