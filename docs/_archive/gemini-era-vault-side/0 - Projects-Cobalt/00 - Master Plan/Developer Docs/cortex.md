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
  - "[[ops]]"
  - "[[engineering]]"
  - "[[orchestrator]]"
location: "src/cobalt_agent/brain/cortex.py"
tags: [cobalt, dev_docs, routing, orchestrator]
created: 2026-02-23
updated: 2026-04-07
---

> **Note:** For market data architecture, see [[ADR-015 5-Pillar Relational Schema]] and [[PRD-013 Multidimensional Market Data Engine]].


# Cortex (The Chief of Staff)

## Overview
`src/cobalt_agent/brain/cortex.py`

The `Cortex` class is the Central Routing Engine (Chief of Staff). It routes user intent to specialized departments based on domains defined in `config.yaml`. Implements deterministic fast-path routing, Zero Trust security intercepts, and lazy department loading.

### Architecture Principles
- **Config-Driven**: All routing logic derived from `config.yaml`, `rules.yaml`, and `prompts.yaml`
- **Deterministic Fast-Path**: Pre-classification routing for common patterns before LLM analysis
- **Zero Trust Security**: High-risk keyword intercept with HITL approval via Proposal Engine

### Zero Trust Architecture
Under the Prime Directive, Cortex implements a **High-Risk Intercept** pattern that enforces Human-in-the-Loop (HITL) approval for any high-stakes actions before execution.

## Class: `Cortex`

### Constructor
```python
def __init__(self)
```
Initializes Cortex with configuration from `config.yaml`, loads departments, and initializes the LLM instance using the unified "fast_chat" switchboard profile.

### Key Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `config` | ConfigModel | Loaded configuration from `configs/config.yaml` |
| `departments` | Dict | Dictionary of active departments from config |
| `llm` | LLM | LLM instance for classification and routing decisions |
| `orchestrator_keywords` | List[str] | Keywords triggering orchestrator fast-path routing |
| `high_risk_keywords` | List[str] | Keywords triggering security intercept |

### Class: DomainDecision

Pydantic model for structured routing decisions.

```python
class DomainDecision(BaseModel):
    domain_name: str = Field(description="The exact name of the department (e.g. TACTICAL, OPS).")
    reasoning: str = Field(description="Why this department fits the request.")
    task_parameters: str = Field(
        description="The PRECISE entity or query to act on. For Tactical, this MUST be just the Ticker Symbol (e.g. 'NVDA') OR the command 'STRATEGY'."
    )
```

## Main Methods

### `route(user_input: str) -> Optional[str]`

Routes user input through a multi-stage pipeline with deterministic fast-path routing and LLM classification.

**Execution Flow:**

```
1. Greeting Fast Exit (< 4 words containing "hi") → return None
   ↓
2. Deterministic Fast-Path Routing (Triage Layer)
   ├─ Orchestrator Keywords → OrchestratorEngine.plan_and_execute()
   ├─ Web Keywords (http, browser, scrape) → return None (default chat)
   ↓
3. LLM Domain Classification (_classify_domain)
   ↓
4. Prime Directive Security Check (High-Risk Keywords)
   ├─ High-Risk Found → _generate_proposal() → HITL Approval
   └─ Low-Risk → Continue to Department Routing
   ↓
5. Lazy Load & Execute Department Handler
```

**Parameters:**
- `user_input` (str): The user's request to route

**Returns:** 
- `str`: Department response or proposal formatted for Mattermost
- `None`: For general chat (handled in main loop)

**Fast-Path Routing Keywords:**
| Category | Keywords | Destination |
|----------|----------|-------------|
| Orchestrator | Config-defined (complex tasks) | `OrchestratorEngine` |
| Web/Triage | http://, https://, browser, scrape, summarize the top | Default chat loop |

### `_classify_domain(user_input: str) -> DomainDecision`

Uses LLM to classify user input into a domain and extract task parameters. Builds prompt from `config.yaml` department definitions.

**Returns:** `DomainDecision` Pydantic model with:
- `domain_name`: The department name (e.g., "TACTICAL", "OPS")
- `reasoning`: Why this domain was selected  
- `task_parameters`: The action item or query

**Prompt Construction:**
1. Iterates through active departments from config
2. Builds options text with department names and descriptions
3. Loads routing prompt template from `config.prompts.routing.classify_domain`
4. Calls `llm.ask_structured(prompt, DomainDecision)`

**Fallback:** Returns `DomainDecision(domain_name="FOUNDATION", reasoning="Error", task_parameters="")` on exception

## Department Handlers

### `_run_tactical(params: str) -> str`

Routes to `Strategos` for trading and market data tasks.

**Parameter Cleaning Logic:**
- If params contains "STRATEGY" or "PLAYBOOK": Pass raw keyword
- Otherwise: Extract first word as ticker symbol (strips punctuation)

```python
if "STRATEGY" in params.upper() or "PLAYBOOK" in params.upper():
    task = "STRATEGY"
else:
    task = params.split()[0].strip(".,!?")
```

### `_run_intel(params: str) -> str`

Routes to Research/Briefing skills.

**Routing Logic:**
| Param Pattern | Destination |
|---------------|-------------|
| Contains "briefing" | `MorningBriefing().run()` |
| Other | `DeepResearch().run(params)` |

### `_run_ops(params: str, original_input: str) -> str`

Routes to Scribe for operations tasks. Uses `original_input` for context in logging/saving.

| Keyword Pattern | Action |
|-----------------|--------|
| "log" or "journal" | Append to daily note via `scribe.append_to_daily_note()` |
| "save" or "note" | Create new note with timestamped filename in `0 - Inbox/` folder |
| "search" or "find" | Search vault via `scribe.search_vault()` |
| "medical" or "billing" | Placeholder: "Medical Admin module is not yet implemented" |

### `_generate_proposal(user_input: str) -> str`

Generates a Proposal using LLM synthesis for high-risk actions.

**Purpose:**
The Prime Directive FORBIDS autonomous execution of high-risk actions. This method:
1. Detects high-risk keywords in user input
2. Calls LLM to synthesize a structured JSON proposal
3. Extracts JSON using regex and instantiates Proposal
4. Returns formatted proposal for Mattermost display

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

## Domain Routing Table

| Domain | Purpose | Parameters | Implementation |
|--------|---------|------------|----------------|
| `TACTICAL` | Trading & Market Data | Ticker symbol or "STRATEGY" | `_run_tactical()` → `Strategos` |
| `INTEL` | Research & Briefings | Search topic | `_run_intel()` → `MorningBriefing` or `DeepResearch` |
| `OPS` | Operations & Logging | Task parameters | `_run_ops()` → `Scribe` |
| `ENGINEERING` | Code Generation | Task description | `_run_engineering()` → `EngineeringDepartment` |
| `FOUNDATION` | General Chat | N/A | Returns `None` (handled in main loop) |
| `DEFAULT` | Fallback Chat | N/A | Returns `None` (handled in main loop) |
| `GROWTH` | Strategic Growth | N/A | Returns placeholder message |

## Example Flows

### Market Data Query
```
User: "What is the price of AAPL?"
→ Fast-path check: No match
→ LLM classifies: domain="TACTICAL", task_parameters="AAPL"
→ Prime Directive check: Low-risk → Bypass
→ _run_tactical("AAPL")
→ Strategos().run("AAPL")
→ Returns market data
```

### Research Query
```
User: "What's new in AI?"
→ Fast-path check: No match  
→ LLM classifies: domain="INTEL", task_parameters="AI"
→ Prime Directive check: Low-risk → Bypass
→ _run_intel("AI")
→ DeepResearch().run("AI")
→ Returns search results
```

### High-Risk Intercept Example
```
User: "Delete all old notes and format the system"
→ Fast-path check: No match
→ LLM classifies: domain="OPS", task_parameters="all old notes"
→ Prime Directive check: "delete" keyword found → HIGH-RISK
→ _generate_proposal("Delete all old notes and format the system")
→ LLM generates structured JSON proposal
→ Returns formatted proposal for Mattermost approval
```

### Orchestrator Fast-Path Example
```
User: "Create a comprehensive market analysis report"
→ Fast-path check: "comprehensive" matches orchestrator keywords
→ Direct call: OrchestratorEngine().plan_and_execute(user_input)
→ Returns orchestrated response (bypasses LLM classification)
```

## Configuration Sources

| Source | Purpose | Location |
|--------|---------|----------|
| `config.yaml.departments` | Department definitions and active status | configs/config.yaml |
| `rules.yaml.cortex_routing.orchestrator_keywords` | Complex task keywords for orchestrator routing | configs/rules.yaml |
| `rules.yaml.cortex_routing.high_risk_keywords` | Keywords triggering HITL approval | configs/rules.yaml |
| `prompts.routing.classify_domain` | LLM prompt template for domain classification | configs/prompts.yaml |