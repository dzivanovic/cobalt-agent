---
title: "Proposal Engine Documentation"
status: Active
module: Core
type: Engine
dependencies:
  - "[[mattermost]]"
  - "[[main]]"
  - "[[cortex]]"
  - "[[config]]"
location: "src/cobalt_agent/core/proposals.py"
tags: [cobalt, dev_docs, hitl, security]
created: 2026-02-23
---

# Proposal Engine (Zero Trust Architecture)

## Overview
The Proposal Engine enforces the Prime Directive by requiring human approval before executing high-stakes actions. It implements a standardized `Proposal` model for all destructive, financial, or system-altering commands, ensuring Zero Trust architecture through Human-in-the-Loop (HITL) validation.

### Zero Trust Principles
- **No Autonomous Execution**: No high-stakes action executes without explicit approval
- **Standardized Proposals**: All proposals follow a consistent format for review
- **Explicit Approval Flow**: Approval must be provided via Mattermost channel response
- **Cryptographic Token**: Task IDs provide unique, verifiable authorization tokens

## LLM Synthesis with Regex Extraction

### Overview
The Cortex module generates proposals using LLM synthesis with structured JSON extraction. When high-risk keywords are detected, the system calls an LLM to synthesize a proposal with action, justification, and risk_assessment fields.

### Regex Extraction Mechanism
```python
# Extract JSON block from LLM response
match = re.search(r'\{.*\}', raw_response, re.DOTALL)
if not match:
    raise ValueError("No JSON block found in LLM response.")
data = json.loads(match.group(0))
```

**Pattern Components:**
- `r'\{.*\}'`: Regex to match JSON object from start `{` to end `}`
- `re.DOTALL`: Allows `.` to match newlines (multi-line JSON)
- Extracts the first valid JSON block from LLM response

### LLM Prompt Format
```python
prompt = f"""
[SECURITY PROTOCOL: PRIME DIRECTIVE]
High-risk action detected: "{user_input}"

You are the Chief of Staff. You are FORBIDDEN from executing this autonomously.
Generate a JSON response explaining the risk.

OUTPUT FORMAT:
{{
  "action": "Summary of what was requested",
  "justification": "Why the user wants this",
  "risk_assessment": "Blunt warning about data loss or system instability"
}}

OUTPUT ONLY JSON. NO EXTRA TEXT.
"""
```

### JSON Output Schema

**Base Schema (LLM Synthesis):**
| Field | Type | Description |
|-------|------|-------------|
| `action` | `str` | Summary of the requested operation |
| `justification` | `str` | User's reasoning for why this action is necessary |
| `risk_assessment` | `str` | Potential impacts or negative consequences |

**Intent Alignment Schema (Required for All New Proposals):**
All new proposals MUST include an `intent_alignment` dictionary with exactly three required keys:

| Field | Type | Description |
|-------|------|-------------|
| `decision_boundaries` | `List[str]` | Explicit constraints defining acceptable solution space |
| `trade_offs` | `Dict[str, str]` | Key trade-offs with rationale (e.g., {"speed": "Prioritized over completeness"}) |
| `validation_metric` | `str` | Measurable success criterion for the proposal |

**Example with Intent Alignment:**
```json
{
  "action": "Refactor the browser automation module",
  "justification": "Current implementation has tight coupling issues",
  "risk_assessment": "May introduce regressions in existing browser flows",
  "intent_alignment": {
    "decision_boundaries": [
      "Must maintain backward compatibility with existing Playwright scripts",
      "Cannot increase average execution time by more than 10%",
      "Must preserve all existing test coverage"
    ],
    "trade_offs": {
      "development_time": "Accepted 2-day delay for thorough refactoring",
      "complexity": "Reduced module complexity at cost of additional abstraction layer"
    },
    "validation_metric": "All existing browser automation tests pass with zero failures"
  }
}
```

### Error Handling
- **No JSON block found**: Returns security intercept message
- **Invalid JSON**: Logs error and returns rejection message
- **Missing fields**: Uses defaults for missing fields

### Example Flow
```
1. User input: "Delete the old log files"
   ↓
2. Cortex.route() detects high-risk keyword "delete"
   ↓
3. Calls _generate_proposal() with user input
   ↓
4. LLM generates JSON response:
   {
     "action": "Delete old log files",
     "justification": "User wants to clean up logs",
     "risk_assessment": "Could affect audit trail if logs are needed later"
   }
   ↓
5. Regex extracts JSON block using r'\{.*\}'
   ↓
6. Instantiate Proposal with extracted fields
   ↓
7. Return formatted proposal for Mattermost display
```

## Class: `Proposal`

### Constructor
```python
def __init__(
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    action: str = Field(description="The specific command or operation to be executed.")
    justification: str = Field(description="The agent's reasoning for why this action is necessary.")
    risk_assessment: str = Field(description="A summary of potential negative impacts.")
    parameters: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.now)
    approved: bool = False
    approval_channel: Optional[str] = None
    approval_message_id: Optional[str] = None
)
```

### Key Attributes

| Field | Type | Description |
|-------|------|-------------|
| `task_id` | `str` | Unique 8-character identifier for approval matching |
| `action` | `str` | The raw command to be executed |
| `justification` | `str` | Agent's reasoning for the action |
| `risk_assessment` | `str` | Summary of potential negative impacts |
| `intent_alignment` | `Dict[str, Any]` | **Required**: Alignment context with decision_boundaries, trade_offs, validation_metric |
| `parameters` | `Dict[str, Any]` | Technical metadata for execution |
| `timestamp` | `datetime` | When proposal was created |
| `approved` | `bool` | Whether this proposal has been approved |
| `approval_channel` | `Optional[str]` | Mattermost channel for approval |
| `approval_message_id` | `Optional[str]` | Mattermost post ID for tracking |

### Methods

#### `format_for_mattermost() -> str`
Formats the proposal for display in Mattermost approval channel.

**Output Format:**
```markdown
### 🛡️ ACTION PROPOSAL [task_id]
**Action:** `command`
**Justification:** agent reasoning
**Risk:** potential impacts

---
⚠️ *This action is paused per the Prime Directive. Reply with 'Approve [task_id]' to proceed.*
```

## Class: `ProposalEngine`

### Constructor
```python
def __init__(self)
```
Initializes the Proposal Engine with configuration from `config.yaml`.

**Key Initialization Steps:**
1. Loads approval channel and team from config
2. Initializes empty proposal dictionaries
3. Logs connection details

### Key Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `config` | `CobaltSettings` | Global configuration |
| `approval_channel` | `str` | Mattermost channel for approval messages |
| `approval_team` | `str` | Team containing approval channel |
| `mattermost` | `Optional[MattermostInterface]` | Mattermost connection instance |
| `approved_proposals` | `Dict[str, Proposal]` | Successfully approved proposals |
| `pending_proposals` | `Dict[str, Proposal]` | Waiting for approval |
| `callbacks` | `Dict[str, Callable[[Proposal], None]]` | **Memory-locked execution callbacks** - frozen Python callbacks mapped to task IDs |
| `_approval_callback` | `Optional[Callable]` | Callback for approved proposals |
| `_monitoring` | `bool` | Whether background monitoring is active |

### Main Methods

#### `connect_mattermost() -> bool`
Establishes connection to Mattermost for approval workflow.

**Returns:**
- `True` if connection and authentication succeeded
- `False` otherwise

**Behavior:**
- Creates `MattermostInterface` instance
- Attempts to connect and authenticate
- Attaches brain for message routing
- Logs connection status

#### `create_proposal(
    action: str,
    justification: str,
    risk_assessment: str,
    parameters: Optional[Dict] = None
) -> Proposal`
Creates a new proposal for a high-stakes action.

**Parameters:**
- `action`: The specific command to execute
- `justification`: Agent's reasoning for necessity
- `risk_assessment`: Summary of potential negative impacts
- `parameters`: Technical metadata for execution

**Returns:**
- Created `Proposal` object
- Added to `pending_proposals` dictionary

**Behavior:**
- Generates unique 8-character task_id
- Creates and stores proposal in pending queue
- Logs proposal creation

#### `send_proposal(proposal: Proposal) -> bool`
Sends a proposal to Mattermost for human review.

**Parameters:**
- `proposal`: The `Proposal` object to send

**Returns:**
- `True` if proposal was sent successfully
- `False` otherwise

**Behavior:**
1. Validates Mattermost connection
2. Retrieves team ID by name
3. Retrieves channel ID using team_id
4. Creates Mattermost post with formatted proposal
5. Stores approval_message_id in proposal
6. Logs success/failure

**Error Cases:**
- No Mattermost connection
- Approval channel not configured
- Team or channel not found

#### `handle_approval_response(message: str, channel_id: str) -> Optional[Proposal]`
Checks if a message is an approval response for a pending proposal.

**Parameters:**
- `message`: The message text from Mattermost
- `channel_id`: The channel ID where the message was posted

**Returns:**
- `Proposal` if this is a valid approval response
- `None` if not an approval or task_id not found

**Approval Pattern:**
- Regex: `approve\s+(\w{8})` (case-insensitive)
- Must match 8-character task_id
- Must be in approval channel

**Behavior:**
1. Extracts task_id from message using regex
2. Validates channel is approval channel
3. Looks up pending proposal by task_id
4. Moves proposal from pending to approved
5. Sets `approved = True`

#### `wait_for_approval(proposal: Proposal, timeout: int = 3600) -> bool`
Waits for a proposal to be approved (polling mode).

**Parameters:**
- `proposal`: The `Proposal` to wait for
- `timeout`: Maximum wait time in seconds (default: 1 hour)

**Returns:**
- `True` if approved within timeout
- `False` if timeout reached

**Behavior:**
- Polls every 5 seconds
- Checks `approved_proposals` dictionary
- Removes from pending on timeout

#### `execute_approved(proposal: Proposal) -> bool`
Executes an approved proposal's action.

**Parameters:**
- `proposal`: The approved `Proposal` to execute

**Returns:**
- `True` if execution succeeded
- `False` otherwise

**Behavior:**
1. Validates proposal is approved
2. Logs execution start
3. Calls approval callback if set
4. Handles execution errors

#### `set_approval_callback(callback: Callable[[Proposal], None]) -> None`
Sets a callback function for approved proposals.

**Parameters:**
- `callback`: Function that takes a `Proposal` and returns `None`

**Usage:**
```python
def on_approval(proposal: Proposal):
    engine.execute_approved(proposal)

engine.set_approval_callback(on_approval)
```

#### `start_monitoring() -> None`
Starts background monitoring for approval responses.

**Behavior:**
- Creates daemon thread for monitoring
- Calls `_monitor_approval_channel()`

#### `_monitor_approval_channel() -> None`
Background thread to monitor approval channel for responses.

**Implementation Note:**
- WebSocket listener is attached to `MattermostInterface`
- This method serves as monitoring entry point

#### `stop_monitoring() -> None`
Stops background monitoring for approval responses.

**Behavior:**
- Sets monitoring flag to False
- Waits for thread to join
- Logs monitoring stop

## Memory-Locked Callbacks (Zero Trust Execution)

### Overview
The `ProposalEngine` class stores **frozen Python execution callbacks** in a shared class dictionary. This implements a "coat-check" system where the LLM proposes an action, receives approval, and then the callback is executed.

### Callback Storage
```python
class ProposalEngine:
    # Shared state across all instances
    pending_proposals: Dict[str, Proposal] = {}
    callbacks: Dict[str, Callable[[Proposal], None]] = {}
```

**Security Characteristics:**
- **No disk persistence**: Callbacks exist only in memory
- **8-character task_id**: Cryptographic token for approval matching
- **Class-level storage**: Shared across all `ProposalEngine` instances
- **Automatic cleanup**: Callbacks removed after execution or timeout

### Callback Lifecycle
```
1. LLM proposes file write via WriteFileTool
   ↓
2. ProposalEngine.create_proposal() generates task_id
   ↓
3. WriteFileTool creates execute_write() closure
   ↓
4. ProposalEngine.set_approval_callback(task_id, execute_write)
   ↓
5. Proposal sent to Mattermost approval channel
   ↓
6. User responds with "Approve [task_id]"
   ↓
7. MattermostInterface intercepts approval response
   ↓
8. ProposalEngine.handle_approval_response() executes callback
   ↓
9. File modification executes in RAM callback
   ↓
10. Callback removed from callbacks dictionary
```

### `set_approval_callback(task_id: str, callback: Callable[[Proposal], None]) -> None`
Sets a callback function to be called when a proposal is approved.

**Parameters:**
- `task_id`: The unique 8-character identifier for the task
- `callback`: Function that takes a `Proposal` and returns `None`

**Usage:**
```python
def execute_write(proposal_obj):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

engine = ProposalEngine()
engine.set_approval_callback(proposal.task_id, execute_write)
```

**Execution Flow:**
1. Callback stored in `ProposalEngine.callbacks[task_id]`
2. Mattermost approval received via WebSocket interceptor
3. `handle_approval_response()` extracts task_id from message
4. Callback retrieved and executed with proposal object
5. Callback removed from dictionary after execution

### Error Handling

**Callback Execution Failures:**
- **Exception during execution**: Error logged, user notified via Mattermost
- **Callback not found**: Warning logged, user notified of missing callback
- **Duplicate approval**: Ignored (already approved or already executed)

## Convenience Functions

### `create_and_send_proposal(...) -> Optional[Proposal]`
Convenience function to create and send a proposal in one call.

**Parameters:**
- `action`: The specific command to execute
- `justification`: Agent's reasoning
- `risk_assessment`: Potential negative impacts
- `parameters`: Technical metadata

**Returns:**
- `Proposal` if successful
- `None` if connection or send fails

**Behavior:**
1. Creates new `ProposalEngine` instance
2. Connects to Mattermost
3. Creates the proposal
4. Sends to Mattermost

## Zero Trust Workflow

### Standard Approval Flow
```
1. Agent identifies high-stakes action
   ↓
2. Creates Proposal with task_id, action, justification, risk
   ↓
3. Sends to Mattermost approval channel
   ↓
4. User sees proposal and responds with "Approve [task_id]"
   ↓
5. MattermostInterface detects approval response
   ↓
6. ProposalEngine validates and moves to approved list
   ↓
7. Callback executes the approved action
   ↓
8. Action completes
```

### High-Risk Intercept (Cortex Integration)
The Cortex module intercepts classified tasks and routes them through the Proposal Engine before any department execution:

```
Cortex.route() → Classifies Task
                ↓
        Is it high-risk?
                ↓
        ┌───── Yes ──────┐
        ↓              ↓
    No              ProposalEngine.create_proposal()
        ↓              ↓
    Route to      ProposalEngine.send_proposal()
    Department    ↓
        ↓              ↓
    Execute    Wait for Approval
                            ↓
                    ProposalEngine.execute_approved()
                            ↓
                        Execute Action
```

## Configuration

### Mattermost Settings
```yaml
mattermost:
  url: "https://mattermost.example.com"
  token: "${MATTERMOST_TOKEN}"
  approval_channel: "approvals"  # Channel for proposals
  approval_team: "cobalt-team"   # Team containing approval channel
```

### Human Intervention Triggers
The following actions require proposal approval:
- File system modifications
- Financial transactions
- System command execution
- Configuration changes
- Any destructive operation

## Security Considerations

1. **Task ID Format**: 8-character UUID prefix balances uniqueness with manual entry feasibility
2. **Channel Validation**: Approval must occur in designated channel only
3. **Regex Matching**: Case-insensitive pattern matching for user convenience
4. **No Auto-Approval**: All high-stakes actions require explicit human approval
5. **Logging**: All proposal lifecycle events are logged for audit trail