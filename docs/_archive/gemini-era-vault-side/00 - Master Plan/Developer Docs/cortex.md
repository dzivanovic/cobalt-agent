---
title: "Cortex Documentation"
status: Active
module: Brain
type: Orchestrator
dependencies:
  - "[[main]]"
  - "[[tactical]]"
  - "[[llm]]"
  - "[[prompt]]"
location: "src/cobalt_agent/main.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Cortex (The Chief of Staff)

## Overview
Cortex is the central routing and coordination agent for the Cobalt system. It acts as the "Chief of Staff" that routes user requests to the appropriate specialized department (Tactical, Intel, Ops, Engineering) based on the user's intent.

### Zero Trust Architecture
Under the Prime Directive (ADR-006), Cortex implements a **High-Risk Intercept** pattern that enforces Human-in-the-Loop (HITL) approval for any high-stakes actions before execution. This ensures Zero Trust: no destructive, financial, or system-altering commands execute without explicit human approval.

## Class: `Cortex`

### Constructor
```python
def __init__(self)
```
Initializes Cortex with configuration from `config.yaml`, loads departments, and initializes the LLM instance.

### Key Attributes
- `config`: Loaded configuration from `configs/config.yaml`
- `departments`: Dictionary of active departments from config
- `llm`: LLM instance for classification and routing decisions

### Main Methods

#### `route(user_input: str) -> Optional[str]`
Routes user input to the appropriate department handler.

**Logic:**
1. Fast exit for simple greetings (< 4 words, "hi")
2. Direct bypass for questions (? or keywords: price, what)
3. Classify domain using LLM
4. Route to department handler (Tactical, Intel, Ops, Engineering, Foundation)

**Returns:**
- String response from department handler, or `None` for general chat (Foundation)

#### `_classify_domain(user_input: str) -> DomainDecision`
Uses LLM to classify user input into a domain and extract task parameters.

**Returns:** `DomainDecision` Pydantic model with:
- `domain_name`: The department name (e.g., "TACTICAL", "OPS")
- `reasoning`: Why this domain was selected
- `task_parameters`: The action item or query

### Department Handlers

#### `_run_tactical(params: str) -> str`
Routes to `Strategos` for trading and market data tasks.

**Handles:**
- Stock price queries (extracts ticker symbol)
- Strategy queries (when "STRATEGY" or "PLAYBOOK" is mentioned)

#### `_run_intel(params: str) -> str`
Routes to Research/Briefing skills.

**Handles:**
- "briefing" → `MorningBriefing().run()`
- Other → `DeepResearch().run(params)`

#### `_run_ops(params: str, original_input: str) -> str`
Routes to Scribe (Operations/Scribe) for logging, saving, and searching.

**Handles:**
- "log"/"journal" → Append to daily note
- "save"/"note" → Create new note
- "search"/"find" → Search vault
- "medical"/"billing" → Placeholder for future Steward logic

### `_generate_proposal(user_input: str) -> str`
Generates a Proposal using LLM synthesis for high-risk actions.

**Purpose:**
The Prime Directive FORBIDS autonomous execution of high-risk actions. This method:
1. Detects high-risk keywords in user input
2. Calls LLM to synthesize a structured JSON proposal
3. Extracts JSON using regex and instantiates Proposal
4. Returns formatted proposal for Mattermost display

**LLM Prompt:**
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

**Regex Extraction Mechanism:**
```python
# Extract JSON block from LLM response
match = re.search(r'\{.*\}', raw_response, re.DOTALL)
if not match:
    raise ValueError("No JSON block found in LLM response.")
data = json.loads(match.group(0))
```

**Parameters:**
- `user_input`: The original user request containing high-risk keywords

**Returns:**
- Formatted Markdown string with proposal details
- Returns error message if Proposal Engine fails

**Error Handling:**
```python
except Exception as e:
    logger.error(f"Proposal Generation Failed: {e} | Raw Output: {raw_response}")
    return (
        f"### 🛡️ SECURITY INTERCEPT\n"
        f"**Action Blocked:** Administrative system change.\n\n"
        f"**Reason:** The Proposal Engine could not validate the risk assessment. "
        f"Execution is denied by default per the Prime Directive."
    )
```

## High-Risk Intercept (Zero Trust Enforcement)

### Overview
The High-Risk Intercept is a middleware layer that enforces the Prime Directive by intercepting high-risk actions and routing them through the Proposal Engine before execution. This ensures all destructive, financial, or system-altering commands require explicit human approval.

The Cortex module implements this by detecting high-risk keywords in user input and generating a Proposal using LLM synthesis with structured JSON extraction.

### Intercept Logic Flow
```
1. route(user_input) receives request
   ↓
2. Classify domain using LLM (_classify_domain)
   ↓
3. Check for high-risk keywords in original input
   ↓
4. ┌───────────── High-Risk Keyword Found ─────────┐
   ↓                                                ↓
5. Call _generate_proposal(user_input)            Bypass (Low-Risk)
   ↓                                                ↓
6. LLM generates JSON with:                      Route to department
   - action: Summary of requested operation
   - justification: Why user wants this
   - risk_assessment: Potential impacts
   ↓
7. Regex extraction: r'\{.*\}' (raw_response, re.DOTALL)
   ↓
8. Instantiate Proposal (task_id auto-generates)
   ↓
9. Return proposal.format_for_mattermost()
   ↓
10. User sees proposal in Mattermost approval channel
   ↓
11. User responds with "Approve [task_id]"
   ↓
12. MattermostInterface detects via regex: r"approve\s+(\w{8})"
   ↓
13. ProposalEngine moves to approved list
   ↓
14. Execute approved action via callback
```

### High-Risk Detection Criteria
Tasks are classified as high-risk if user input contains any of these keywords:
- `delete`, `move`, `remove`, `format`, `execute`, `kill`, `reorganize`

**Case-insensitive detection** in `_generate_proposal()`:
```python
high_risk_keywords = ['delete', 'move', 'remove', 'format', 'execute', 'kill', 'reorganize']
is_high_risk = any(word in user_input.lower() for word in high_risk_keywords)
```

### Integration with ProposalEngine
```python
from cobalt_agent.core.proposals import ProposalEngine

# In route() method:
if is_high_risk(decision.domain_name, decision.task_parameters):
    engine = ProposalEngine()
    engine.connect_mattermost()
    
    proposal = engine.create_proposal(
        action=get_command(decision),
        justification=decision.reasoning,
        risk_assessment="Potential financial loss or data modification"
    )
    
    engine.send_proposal(proposal)
    engine.wait_for_approval(proposal)
    engine.execute_approved(proposal)
else:
    # Route directly to department
    return self._route_to_department(decision)
```

### Approval Response Handling
When a user responds with "Approve [task_id]":
1. MattermostInterface detects the message via WebSocket
2. `handle_approval_response()` validates the pattern and task_id
3. ProposalEngine moves proposal from pending to approved
4. Approved callback executes the action

### Security Guarantees
- **No autonomous execution**: All high-risk actions require explicit approval
- **Audit trail**: All proposals are logged with timestamps
- **Channel validation**: Approval must occur in designated channel only
- **Token validation**: 8-character task_id ensures approval matches correct proposal

## Domain Routing Logic

| Domain | Purpose | Parameters |
|--------|---------|------------|
| `TACTICAL` | Trading & Market Data | Ticker symbol or "STRATEGY" |
| `INTEL` | Research & News | Search topic |
| `OPS` | Operations & Logging | Task parameters |
| `ENGINEERING` | Engineering | TODO - Not implemented |
| `FOUNDATION` | General Chat | "chat" |

## Configuration
Departments are loaded from `config.yaml` under the `departments` section. Only departments marked as `active: true` are considered for routing.

## Example Flow
```
User: "What is the price of AAPL?"
→ LLM classifies: domain="TACTICAL", params="AAPL"
→ _run_tactical("AAPL")
→ Strategos().run("AAPL")
→ Returns market data
```

```
User: "What's new in AI?"
→ LLM classifies: domain="INTEL", params="AI"
→ _run_intel("AI")
→ DeepResearch().run("AI")
→ Returns search results