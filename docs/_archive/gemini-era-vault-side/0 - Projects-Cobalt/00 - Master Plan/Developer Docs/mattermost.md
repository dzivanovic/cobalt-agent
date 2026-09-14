---
title: "Mattermost Interface Documentation"
status: Active
module: Interface
type: Class
dependencies:
  - "[[main]]"
  - "[[cortex]]"
  - "[[llm]]"
location: "src/cobalt_agent/interfaces/mattermost.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Mattermost Interface

## Overview
The Mattermost Interface provides real-time communication capabilities for the Cobalt Agent. It enables the agent to listen for messages in Mattermost channels and respond using the Brain's routing and LLM capabilities.

### Native WebSocket Architecture
The interface now uses a **highly stable, native WebSocket connection** (`ws://.../api/v4/websocket`) with an **async event loop** for the HITL Proposal Bouncer. This replaces legacy polling assumptions and ensures deterministic, low-latency message delivery without blocking the primary inference loop.

**Connection Details:**
- **Endpoint:** `ws://{host}/api/v4/websocket` (native WebSocket, not HTTP polling)
- **Protocol:** `ws://` or `wss://` (depending on scheme config)
- **Port:** `8065` (default Mattermost WebSocket port)
- **Authentication:** Token-based handshake via `config.token`

### Zero Trust Integration
The interface integrates with the Proposal Engine to handle **Approval Responses** for high-stakes actions. When users respond with "Approve [task_id]" in the approval channel, the interface detects the response, validates the task_id, and triggers execution of the approved action.

## Class: `MattermostInterface`

### Constructor
```python
def __init__(self, config: Optional[MattermostConfig] = None)
```
Initializes the interface with configuration. If no config is provided, loads from global config.

**Parameters:**
- `config`: Optional `MattermostConfig` instance

### Key Attributes
- `config`: Mattermost configuration (URL, token)
- `driver`: Mattermost driver instance
- `brain`: Reference to the CobaltAgent/Cortex for message processing
- `is_connected`: Boolean indicating connection status

### Main Methods

#### `connect() -> bool`
Establishes connection to the Mattermost server and authenticates.

**Returns:**
- `True` if connection and authentication succeeded
- `False` otherwise

**Configuration Sources:**
1. Environment variables: `MATTERMOST_URL`, `MATTERMOST_TOKEN`
2. YAML config: `configs/config.yaml`

#### `disconnect() -> None`
Logs out from Mattermost and disconnects from the server.

#### `send_message(channel_name: str, team_name: str, message: str) -> bool`
Sends a message to a specific channel.

**Parameters:**
- `channel_name`: Name of the channel (without #)
- `team_name`: Name of the team
- `message`: Message content to send

**Returns:**
- `True` if message sent successfully
- `False` otherwise

#### `send_message_to_channel_id(channel_id: str, message: str) -> bool`
Directly sends a message to a channel using its ID.

**Parameters:**
- `channel_id`: Mattermost channel ID
- `message`: Message content

#### `get_my_user_id() -> Optional[str]`
Returns the current user's Mattermost ID.

### WebSocket Integration

#### `start_listening(brain: "CobaltAgent") -> None`
Starts the WebSocket listener in the main thread to receive incoming messages.

**Features:**
- Connects to Mattermost WebSocket API
- Processes incoming messages
- Routes to Brain for inference
- Sends responses back to channel

**Message Flow:**
1. WebSocket receives "posted" event
2. Extract post data (user_id, channel_id, message)
3. Ignore bot's own messages
4. Route to `brain.route()` or generate conversational response
5. Send response to channel

### Internal Methods

#### `_handle_mattermost_event(message: str) -> None`
Processes incoming WebSocket events.

**Handles:**
- Event parsing and validation
- Post data extraction from JSON
- Message routing to Brain
- Conversational response generation

#### `_handle_events(mm_driver: Driver) -> None`
Event handler callback for Mattermost events.

#### `_run_websocket_in_process(brain: "CobaltAgent", event_queue: "multiprocessing.Queue") -> None`
Runs the WebSocket listener in a separate process to avoid event loop conflicts.

### Approval Response Handling

#### Overview
The MattermostInterface detects and processes **Approval Responses** for high-stakes actions. When users respond with "Approve [task_id]" in the approval channel, the interface validates the response using regex and triggers the Proposal Engine to execute the approved action.

**Key Integration Points:**
- `MattermostInterface` receives WebSocket events
- `proposal_engine.handle_approval_response()` validates approval pattern and task_id
- `proposal_engine.execute_approved()` executes the approved action

#### Approval Pattern Regex
```python
approval_pattern = r"approve\s+(\w{8})"
```

**Pattern Components:**
- `approve`: Literal text (case-insensitive)
- `\s+`: One or more whitespace characters
- `(\w{8})`: Capture group for exactly 8 word characters (task_id)

**Example Matches:**
| Input | Extracted Task ID | Match? |
|-------|-------------------|--------|
| `approve abc12345` | `abc12345` | ✅ Yes |
| `Approve ABC12345` | `ABC12345` | ✅ Yes |
| `approved xyz98765` | `xyz98765` | ✅ Yes |
| `APPROVE 12345678` | `12345678` | ✅ Yes |
| `approve abc123` | `N/A` | ❌ No (wrong length) |
| `Deny abc12345` | `N/A` | ❌ No (wrong keyword) |

#### Approval Response Processing Flow
```
1. WebSocket receives "posted" event with message
   ↓
2. _handle_mattermost_event() extracts message text and channel_id
   ↓
3. ┌──────── proposal_engine attached? ─────────┐
   │                                            ↓
   │                                     No engine → skip
   ↓
   ┌───────────── Yes ─────────┐
   ↓                         ↓
4. Call proposal_engine.handle_approval_response(text, channel_id)
   ↓
5. Regex pattern matching checks for approval pattern
   ↓
6. ┌───────────── Match ─────────┐
   ↓                             ↓
7. Extract task_id (8-char ID)  No match → route to brain
   ↓
8. Validate channel matches approval_channel config
   ↓
9. ┌───────────── Valid ─────────┐
   ↓                             ↓
10. Look up task_id in pending_proposals  Invalid channel → route to brain
   ↓
11. ┌───────────── Found ─────────┐
   ↓                             ↓
12. Remove from pending, add to approved  Unknown task_id → route to brain
   ↓
13. Set proposal.approved = True
   ↓
14. Log approval event
   ↓
15. ┌──────── approval_callback set? ─────────┐
   │                                         ↓
   │                                  No callback → done
   ↓
   ┌───────────── Yes ─────────┐
   ↓                         ↓
16. Execute approved action   Execute callback with proposal
   ↓
17. Return to message loop
```

#### Integration with ProposalEngine

**Connection Setup:**
```python
from cobalt_agent.core.proposals import ProposalEngine

# In main.py or initialization:
engine = ProposalEngine()
engine.connect_mattermost()
engine.start_monitoring()

# Attach engine to MattermostInterface:
mm_interface.proposal_engine = engine
mm_interface.brain = cobalt_agent.cortex
```

**Message Processing Priority:**
1. **Approval responses** (highest priority) - processed first
2. **Brain routing** - for non-approval messages

**Flow when approval detected:**
```python
# In _handle_mattermost_event():
if self.proposal_engine:
    approved_proposal = self.proposal_engine.handle_approval_response(text, channel_id)
    if approved_proposal:
        # Execute the approved action
        self.proposal_engine.execute_approved(approved_proposal)
        return  # Don't route to brain for approval responses

# Only reach here if not an approval response
if self.brain:
    response = self.brain.route(text)
    self.send_message_to_channel_id(channel_id, response)
```

#### The `handle_approval_response()` Method

**Location:** `ProposalEngine` (not `MattermostInterface`)

**Signature:**
```python
def handle_approval_response(self, message: str, channel_id: str) -> Optional[Proposal]
```

**Behavior:**
1. Regex extracts task_id from message
2. Validates channel matches approval_channel config
3. Looks up task_id in pending_proposals
4. If found: removes from pending, adds to approved, sets approved=True
5. Returns the approved Proposal (or None if not an approval)

**Returns:**
- `Proposal` object if this is a valid approval response
- `None` if message doesn't match approval pattern or task_id not found

#### Error Handling

**Common failure cases:**
- **No approval engine attached**: Message routes to brain normally
- **Channel mismatch**: Approval ignored, message routes to brain
- **Unknown task_id**: Warning logged, message routes to brain
- **Regex no match**: Message routes to brain normally

---

## HITL Interceptor (Zero Trust)

### Overview
The MattermostInterface implements a **WebSocket-level interceptor** that processes approval/reject messages before any LLM inference. This ensures Zero Trust by bypassing the ReAct loop for approval responses.

**Location:** `_handle_mattermost_event()` method

### Interceptor Priority

```
1. WebSocket receives "posted" event with message
   ↓
2. HITL Interceptor checks if message starts with "approve" or "reject"
   ↓
   ┌───────────── Match ─────────┐
   ↓                             ↓
3. Call engine.handle_approval_response()   No match → skip interceptor
   ↓                             ↓
4. Send result back to channel   Route to brain for LLM inference
   ↓
5. Return (don't process further)
```

### Supported Approval Patterns

| Pattern | Case-Sensitive | Extracts | Example |
|---------|---------------|--------|--------|
| `approve\s+(\w{8})` | Case-insensitive | 8-char task-id | `Approve abc12345` |
| `reject\s+(\w{8})` | Case-insensitive | 8-char task_id | `Reject xyz98765` |

### Response Messages

**Approval Success:**
```
✅ Approval received for task [abc12345]. Action executed successfully.
```

**Approval Timeout:**
```
⚠️ Approval received for [abc12345], but no execution callback was found in memory.
```

**Unknown Task ID:**
```
⚠️ No pending approval found for task [abc12345].
```

**Already Approved:**
```
ℹ️ Proposal [abc12345] was already approved.
```

**Rejection:**
```
❌ Rejection received for task [abc12345]. The action has been cancelled.
```

---

## System Message Filtering

### Overview
The MattermostInterface filters out **Mattermost system messages** (joins, leaves, header updates) to prevent the LLM from responding to non-user events.

### System Message Detection

```python
# Ignore Mattermost system messages (joins, leaves, header updates)
if post_data.get("type", "") != "":
    return
```

### System Message Types Filtered

| Message Type | Description | Filtered? |
|--------------|-------------|----------|
| Empty (`""`) | Regular user message | ❌ No |
| `"system_join"` | User joins channel | ✅ Yes |
| `"system_leave"` | User leaves channel | ✅ Yes |
| `"system_header"` | Channel header updated | ✅ Yes |
| `"system_join_leave"` | Group membership change | ✅ Yes |
| `"system_purpose"` | Channel purpose updated | ✅ Yes |

### Implementation Note
Only messages with an empty `type` field (regular user messages) pass through to the LLM inference pipeline. All system-generated events are silently dropped.

## Integration with Brain

The Mattermost interface requires a Brain (Cortex) attachment to process messages:

```python
mm_interface.brain = cobalt_agent.cortex
```

When a message is received:
1. `cortex.route(text)` attempts to match to a department
2. If matched, department response is sent
3. If not matched, LLM generates conversational response

## Configuration Example
```yaml
mattermost:
  url: "https://mattermost.example.com"
  token: "${MATTERMOST_TOKEN}"
  scheme: "https"
  port: 443