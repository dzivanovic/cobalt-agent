---
title: "LLM Interface Documentation"
status: Active
module: Brain
type: Class
dependencies:
  - "[[main]]"
  - "[[prompt]]"
location: "src/cobalt_agent/llm.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# LLM (Language Model) Interface

## Overview
The LLM interface provides unified access to large language models through a single API. It supports multiple providers including Gemini and handles model configuration, prompting, and response parsing.

## Class: `LLM`

### Constructor
```python
def __init__(self, config: LLMConfig)
```
Initializes the LLM with provider configuration.

**Parameters:**
- `config`: `LLMConfig` instance containing model name and API key

### Key Attributes
- `config`: LLM configuration
- `model_name`: The model identifier (e.g., "gemini/gemini-1.5-pro")
- `api_key`: Provider API key

### Main Methods

#### `generate(prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str`
Generates text from the LLM based on the provided prompt.

**Parameters:**
- `prompt`: The input prompt text
- `temperature`: Controls randomness (0.0 to 1.0)
- `max_tokens`: Maximum tokens in the response

**Returns:**
- `str`: Generated response from the model

#### `_call_gemini(prompt: str, temperature: float, max_tokens: int) -> str`
Internal method to call the Gemini API.

**Parameters:**
- `prompt`: The input prompt
- `temperature`: Temperature setting
- `max_tokens`: Maximum tokens

**Returns:**
- Generated response from Gemini

### Internal Methods

#### `_get_provider() -> str`
Determines the LLM provider from the model name.

**Returns:**
- Provider name (e.g., "gemini")

#### `_parse_model_name(full_name: str) -> Tuple[str, str]`
Splits full model name into provider and model parts.

**Returns:**
- Tuple of (provider, model_name)

## Configuration

### Model Name Format
The model name follows the format `provider/model-name`:
- `gemini/gemini-1.5-pro`
- `gemini/gemini-2.0-flash`

### Environment Variables
- `LLM_API_KEY`: API key for the LLM provider

## Error Handling
- Missing API keys raise configuration errors
- Network failures are caught and logged
- Invalid responses are handled gracefully

## LiteLLM Routing Configuration

### Local Development (LM Studio)

For local development with LM Studio, the LLM routes requests through a local OpenAI-compatible proxy.

**Configuration Requirements:**

1. **API Base URL**: Local nodes must specify `api_base` pointing to `http://localhost:1234/v1`
   ```yaml
   models:
     local-model:
       provider: openai
       model_name: lm-studio-local
       node_ref: local_server
   ```

2. **Dummy API Key**: A local dummy API key (`lm-studio`) is required for OpenAI proxy bypass
   - LM Studio does not require authentication but LiteLLM expects an API key parameter
   - Use `lm-studio` as the placeholder value

3. **Network Topology**: The `node_ref` in model config resolves to a local node definition:
   ```yaml
   network:
     nodes:
       local_server:
         ip: 127.0.0.1
         port: 1234
         protocol: http
   ```

**Request Flow:**
```
LiteLLM → http://localhost:1234/v1/chat/completions
```

### SRE Jinja Template Safety Net

To prevent `400 BadRequest` errors when prompts contain only system messages (no user input), the `_call_provider` method dynamically appends a fallback user message:

```python
# SRE Jinja Template Safety Net
has_user = any(msg.get("role") == "user" for msg in messages)
if not has_user:
    messages.append({"role": "user", "content": "Analyze system prompt and execute."})
```

**Purpose:** Ensures all requests contain at least one user message, preventing OpenAI-compatible API errors.

**Use Cases:**
- System-only prompts from skills (e.g., `generate_response_skill`)
- Automated tool execution loops
- Structured data extraction with system instructions only

## Future Enhancements
- Support for additional LLM providers
- Streaming responses
- Token usage tracking
- Rate limit handling