---
title: "LLM (The Brain) - Core Agent Interface"
status: Active
module: Brain
type: Class
dependencies:
  - "[[main]]"
  - "[[prompt]]"
  - "[[config]]"
location: "src/cobalt_agent/llm.py"
tags: [cobalt, dev_docs, llm, brain]
created: 2026-02-23
last_updated: 2026-04-08
---

# LLM (Language Model) - The Brain

## Overview
The `LLM` class serves as Cobalt Agent's central intelligence layer ("The Brain"). It provides a unified interface for communicating with AI providers via LiteLLM, supporting multiple model types including cloud APIs and local deployments.

**Key Capabilities:**
- Unified API for all LLM providers via LiteLLM
- Dynamic model switching based on role configuration
- Zero-trust API key management via Vault integration
- Three distinct interfaces: Chat, Direct Query, and Structured Data extraction

## Class Definition

```python
class LLM(BaseModel)
```

### Dependencies
| Dependency | Purpose |
|------------|---------|
| `pydantic` | Model validation and serialization |
| `litellm.completion` | Unified LLM provider interface |
| `loguru` | Structured logging |
| `cobalt_agent.config` | Model registry and network topology resolution |

---

## Configuration & Initialization

### Constructor
```python
def __init__(self, **data: Any) -> None
```

**Parameters:**
- `role`: Role identifier for model selection (default: "default")
- `api_key`: Optional API key as `SecretStr` (resolves from environment if omitted)

**Initialization Flow:**
1. Calls parent `BaseModel` initialization
2. Invokes `_resolve_model_config()` to determine active model

### Property: `model_name`
```python
@property
def model_name(self) -> str
```
Returns the resolved full model identifier in format `{provider}/{name}` (e.g., `openai/gpt-4`).

### Method: `switch_role(new_role: str) -> None`
Hot-swaps the active model by switching roles.

**Example:**
```python
llm.switch_role("engineer")  # Switches to engineer-optimized model
```

---

## Model Resolution (`_resolve_model_config`)

This internal method resolves the complete model configuration from `config.yaml`:

1. **Retrieve Active Profile:** Loads current profile from config
2. **Resolve Model Alias:** Maps role to model alias via `active_profile.get(role)`
3. **Validate Alias:** Raises `ValueError` if alias not found in model registry
4. **Extract Configuration:**
   - `provider`: LLM provider (e.g., "openai", "gemini")
   - `name`: Model identifier
   - `node_ref`: Optional local node reference for API base URL
   - `env_key_ref`: Environment variable key reference for API authentication

5. **Construct Model Name:** Formats as `{provider}/{name}`
6. **Resolve API Base (if local):** For models with `node_ref`, constructs endpoint from network topology:
   ```python
   self._api_base = f"{protocol}://{ip}:{port}/v1"
   ```

**Configuration Example:**
```yaml
# config.yaml
active_profile: default
profiles:
  default:
    engineer: deepseek_coder
    default: gpt4

models:
  deepseek_coder:
    provider: openai
    model_name: deepseek-chat
    node_ref: local_llama
    env_key_ref: DEEPSEEK_API_KEY

network:
  nodes:
    local_llama:
      ip: localhost
      port: 1234
      protocol: http
```

---

## API Provider Interface (`_call_provider`)

### Method Signature
```python
def _call_provider(
    messages: List[Dict[str, str]], 
    tools: Optional[List[Dict]] = None, 
    temperature: float = 0.7, 
    max_tokens: int = 4000, 
    response_format: Optional[Dict] = None
) -> str
```

### Request Flow

**1. API Key Resolution (Zero-Trust Vault Extraction)**
```python
# Priority order:
# 1. Extract from config keys using env_key_ref
# 2. Fallback to os.getenv(target_key_name)
```

**2. Message Assembly**
- Validates presence of user message; appends fallback if missing:
  ```python
  has_user = any(msg.get("role") == "user" for msg in messages)
  if not has_user:
      messages.append({"role": "user", "content": "Analyze system prompt and execute."})
  ```

**3. Request Execution via LiteLLM**
```python
kwargs = {
    "model": self._model_name,
    "messages": messages,
    "temperature": temperature,
    "max_tokens": max_tokens
}
if self._api_base: kwargs["api_base"] = self._api_base
if api_key: kwargs["api_key"] = api_key
if tools: kwargs["tools"] = tools
if response_format: kwargs["response_format"] = response_format

response = completion(**kwargs)
```

**4. Response Handling**
- Returns `response.choices[0].message.content.strip()`
- Raises `ValueError` on empty responses

### Error Handling
```python
except Exception as e:
    logger.error(f"LLM Call Failed: {str(e)}")
    raise e
```

---

## Interface 1: The Chat Interface (`generate_response`)

### Method Signature
```python
def generate_response(
    system_prompt: Optional[str] = None,
    user_input: Optional[str] = None,
    memory_context: Optional[List[Dict]] = None,
    search_context: str = "",
    tools: Optional[List[Dict]] = None
) -> str
```

### Message Assembly Order
1. **System Prompt:** Added as `{"role": "system", "content": system_prompt}`
2. **Memory Context:** Iterates through history items:
   - If `source` present: Maps "User" → user role, else → assistant role
   - If `role` present: Uses raw role/content directly
3. **Search Context (Legacy):** Appends as user message with context wrapper
4. **Current Input:** Final user message

### Use Cases
- Main agent conversation loop
- Context-rich interactions with memory injection
- Tool-augmented requests

---

## Interface 2: The Skill Interface (`generate_response_skill`, `ask`)

### Skill Method (Simplified)
```python
def generate_response_skill(self, prompt: str) -> str
```
Convenience wrapper for single-prompt queries with no history.

### Direct Ask Method
```python
def ask(
    system_message: str,
    user_input: Optional[str] = None,
    tools: Optional[List[Dict]] = None,
    temperature: float = 0.7,
    max_tokens: int = 4000,
    response_format: Optional[Dict] = None
) -> str
```

**Use Cases:**
- Research skills (one-off queries)
- Briefing generation
- Tool execution with structured parameters

---

## Interface 3: The Structured Interface (`ask_structured`)

### Method Signature
```python
def ask_structured(
    system_prompt: str, 
    response_model: Type[T],
    memory_context: Optional[List[Dict]] = None,
    search_context: str = "", 
    user_input: Optional[str] = None,
    tools: Optional[List[Dict]] = None
) -> T
```

### Purpose
Forces LLM output to conform to a Pydantic model schema via JSON validation.

### Implementation Flow
1. **Schema Extraction:** `schema = response_model.model_json_schema()`
2. **Instruction Assembly:** Combines system prompt with JSON schema directive:
   ```python
   json_instruction = (
       f"You are a precise data output engine.\n"
       f"You MUST return ONLY valid JSON that matches this schema:\n"
       f"{json.dumps(schema, indent=2)}\n"
       f"Do not include markdown formatting (like ```json). Return raw JSON only."
   )
   ```
3. **Message Construction:** Builds message list with system + memory + search + user contexts
4. **Request Execution:** Calls `_call_provider` with assembled messages
5. **Response Cleaning:** Strips markdown code blocks:
   ```python
   cleaned_json = raw_response.replace("```json", "").replace("```", "").strip()
   ```
6. **Validation:** `response_model.model_validate_json(cleaned_json)`

### Error Handling
```python
except ValidationError as e:
    logger.error(f"Structured Data Control Failed: {e}")
    logger.debug(f"Raw Output: {raw_response}")
    raise ValueError(f"LLM failed to generate valid JSON: {e}")
```

### Use Cases
- Strict data extraction (e.g., financial entities, structured records)
- Schema-enforced API responses
- Automated parsing workflows

---

## Configuration Reference

### Model Name Format
```
{provider}/{model-name}
```
Examples:
- `openai/gpt-4`
- `gemini/gemini-1.5-pro`
- `anthropic/claude-3-opus`

### Environment Variables
| Variable | Purpose |
|----------|---------|
| `{ENV_KEY_REF}_API_KEY` | API key for provider (e.g., `GEMINI_API_KEY`, `OPENAI_API_KEY`) |

### Local Model Configuration
For local deployments (e.g., LM Studio, Ollama):

```yaml
models:
  local_model:
    provider: openai  # LiteLLM treats local endpoints as OpenAI-compatible
    model_name: local-model
    node_ref: local_server
    env_key_ref: LOCAL_API_KEY

network:
  nodes:
    local_server:
      ip: localhost
      port: 1234
      protocol: http
```

**Note:** Local models require a dummy API key for LiteLLM validation bypass.

---

## Error Handling Strategy

| Failure Mode | Response |
|--------------|----------|
| Missing API key | Logs CRITICAL warning; request may fail at provider level |
| Empty provider response | Raises `ValueError("Empty response from provider")` |
| JSON validation failure | Logs raw output; raises descriptive `ValueError` |
| Network timeout | Propagates exception with error logging |

---

## Integration Points

### Dependencies
- **LiteLLM:** Unified provider abstraction layer
- **Pydantic:** Schema validation and model definition
- **Config System:** Model registry resolution

### Related Components
- `cobalt_agent.config`: Model and network configuration
- `cobalt_agent.prompt`: System prompt templates
- `cobalt_agent.memory`: Context injection for conversations

---

## Future Enhancements
- Streaming response support
- Token usage metrics and cost tracking
- Rate limiting and retry logic
- Multi-model fallback chains