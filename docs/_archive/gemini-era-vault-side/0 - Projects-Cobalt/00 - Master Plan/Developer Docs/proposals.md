# Proposal Engine

The Proposal Engine implements a **Human-in-the-Loop (HITL)** workflow for Cobalt Agent, ensuring that high-stakes AI actions require explicit human approval before execution. This system enforces the Prime Directive by preventing autonomous agents from performing potentially harmful operations without oversight.

## Overview

The Proposal Engine provides:
- **Persistent storage** of proposals in PostgreSQL (survives system restarts)
- **Structured approval workflow** with clear state transitions
- **Intent alignment** through explicit decision boundaries and validation metrics
- **Mattermost integration** for human review and approval

## Architecture Components

### HITLProposalStore

The `HITLProposalStore` class manages persistent storage of proposals in the PostgreSQL `hitl_proposals` table:

```python
class HITLProposalStore:
    """Persistent storage for HITL proposals using Postgres."""
    
    def create_proposal(self, task_id: str, tool_name: str, tool_kwargs: Dict[str, Any]) -> None
    def get_proposal(self, proposal_id: str) -> Optional[Dict[str, Any]]
    def get_pending_proposals(self) -> List[Dict[str, Any]]
    def update_status(self, proposal_id: str, status: str) -> bool
    def delete_proposal(self, proposal_id: str) -> bool
```

**Key Methods:**
- `create_proposal()`: Inserts a new proposal with status='pending' into the database
- `get_proposal()`: Retrieves a proposal by its UUID
- `get_pending_proposals()`: Returns all proposals awaiting human approval
- `update_status()`: Changes proposal status (pending → approved/rejected)
- `delete_proposal()`: Removes a proposal from storage

### Proposal Model

The `Proposal` class represents a structured request for action:

```python
class Proposal(BaseModel):
    task_id: str                    # 8-character UUID
    action: str                     # Command/operation to execute
    justification: str              # Reasoning for the action
    risk_assessment: str            # Potential negative impacts
    intent_alignment: IntentAlignment  # Decision boundaries, trade-offs, validation
    parameters: Dict[str, Any]      # Technical metadata
    timestamp: datetime             # Creation time
    approved: bool                  # Approval status
    approval_channel: Optional[str] # Mattermost channel ID
    approval_message_id: Optional[str]  # Message ID in Mattermost
```

### IntentAlignment Model

The `IntentAlignment` class captures structured intent metadata:

```python
class IntentAlignment(BaseModel):
    decision_boundaries: str  # Exact files/systems/resources authorized
    trade_offs: str           # Explicit trade-off decisions
    validation_metric: str    # Success condition or verification command
```

## Human-in-the-Loop (HITL) Architecture

The HITL architecture implements a **zero-trust approval workflow**:

### Workflow Steps

1. **Proposal Creation**
   - Agent identifies a high-stakes action requiring approval
   - `ProposalEngine.create_proposal(tool_name, tool_kwargs)` generates a unique task_id
   - Proposal is persisted to PostgreSQL with status='pending'

2. **Notification**
   - Proposal is formatted for Mattermost display using `format_for_mattermost()`
   - Message includes explicit intent alignment block with decision boundaries

3. **Human Review**
   - Human operator reviews the proposal in Mattermost
   - Operator replies with `Approve <task_id>` or `Reject <task_id>`

4. **Approval Processing**
   - System parses the response using regex patterns
   - `handle_approval_response()` validates and processes the approval/rejection
   - Database status is updated accordingly

5. **Execution or Cancellation**
   - If approved: `approve_and_get_payload()` returns tool execution parameters
   - If rejected: Action is aborted with appropriate logging

### Key Design Patterns

**Airlock Pattern**: The `approve_and_get_payload()` method implements an "airlock" where:
1. Database transaction updates status to 'approved' and commits immediately
2. Returns tool_name and tool_kwargs without executing the tool
3. Interface layer executes the tool after DB transaction completes (prevents deadlocks)

**Callback Pattern**: `set_approval_callback()` allows registering callbacks for async approval handling:
```python
def set_approval_callback(self, task_id: str, callback: Callable[[str, Dict[str, Any]], None]) -> None
```

## State Machine

The Proposal Engine implements a four-state machine for proposal lifecycle management:

### States

| State | Description | Transitions From |
|-------|-------------|------------------|
| `PENDING` | Initial state; awaiting human approval | Created via `create_proposal()` |
| `APPROVED` | Human approved; ready for execution | From PENDING via "Approve <task_id>" |
| `REJECTED` | Human rejected; action aborted | From PENDING via "Reject <task_id>" |
| `EXECUTED` | Action successfully completed | From APPROVED after tool execution |

### State Transitions

```
┌─────────────┐
│  PENDING    │
└──────┬──────┘
       │
       ├── Approve ──→ APPROVED ──→ Execute ──→ EXECUTED
       │
       └── Reject ──→ REJECTED (terminal)
```

### State Management

**PENDING → APPROVED**: Triggered by `handle_approval_response()` when matching "Approve <task_id>" pattern:
```python
hitl_store.update_status(task_id, 'approved')
```

**PENDING → REJECTED**: Triggered when matching "Reject <task_id>" pattern:
```python
hitl_store.update_status(task_id, 'rejected')
```

**APPROVED → EXECUTED**: Implicit transition after successful tool execution via `execute_approved()`.

### Implementation Details

The state machine is implemented through database status field:
- Storage: PostgreSQL `hitl_proposals` table with `status` column
- Valid values: 'pending', 'approved', 'rejected' (EXECUTED is a runtime state)
- Status updates use `update_status()` with immediate commit

```python
def update_status(self, proposal_id: str, status: str) -> bool:
    cur.execute("""
        UPDATE hitl_proposals
        SET status = %s, updated_at = CURRENT_TIMESTAMP
        WHERE id = %s
    """, (status, proposal_id))
    conn.commit()
```

## Usage Example

```python
from cobalt_agent.core.proposals import ProposalEngine

# Initialize engine
engine = ProposalEngine()

# Create and store proposal
task_id = engine.create_proposal(
    tool_name="browser",
    tool_kwargs={"query": "https://example.com"}
)

# Wait for approval (blocking)
is_approved = engine.wait_for_approval(task_id, timeout=3600)

if is_approved:
    # Get payload and execute
    payload = engine.approve_and_get_payload(task_id)
    # Execute tool with payload...
```

## Integration Points

- **Mattermost Interface**: Receives approval/rejection responses via `handle_approval_response()`
- **Tool Manager**: Executes approved actions with `bypass_hitl=True` flag
- **PostgreSQL Memory**: Provides persistent storage via `HITLProposalStore`

## Security Considerations

1. **Zero Trust**: No action executes without explicit approval
2. **Audit Trail**: All proposals persist in database for compliance
3. **Channel Validation**: Approval responses validated against configured channel
4. **Idempotency**: Multiple approval attempts handled gracefully (already processed detection)