# Deep Research Agent (Deep Dive)

## Overview
**File:** `src/cobalt_agent/skills/research/deep_dive.py`

The `DeepResearch` class implements a multi-step research agent following a "Plan → Search → Analyze → Report" workflow for in-depth topic investigation.

---

## Class: DeepResearch

### Description
A structured research agent that decomposes complex topics into targeted search queries, executes parallel information gathering, and synthesizes findings into professional reports.

### Constructor
```python
def __init__(self)
```

Initializes core components:
1. **LLM** - Structured prompt handling with Pydantic output validation
2. **SearchTool** - Web search for information retrieval
3. **BrowserTool** - Advanced web scraping capabilities
4. **Scribe** - Report delivery to Obsidian vault

---

## Pydantic Schemas

### ResearchPlan
```python
class ResearchPlan(BaseModel):
    queries: List[str]  # 3 distinct search queries investigating the topic from different angles
```

### ResearchReport
```python
class ResearchReport(BaseModel):
    title: str              # Clear, professional report title
    executive_summary: str  # High-level summary of findings
    key_findings: List[str] # Most important technical/financial facts discovered
    strategic_outlook: str  # Forward-looking analysis or conclusion
```

---

## Methods

### run
```python
def run(self, topic: str) -> str
```

Executes a multi-phase research plan on a complex topic.

**Parameters:**
- `topic` (str): The research subject to investigate

**Returns:** Path to the saved report in Obsidian vault (`0 - Inbox` folder)

---

## Execution Phases

### Phase 1: Planning
Generates a research strategy by prompting the LLM to create 3 distinct search queries.

**Prompt Template:**
```
Create a research plan for the topic: '{topic}'. Generate 3 distinct search queries.
```

**Fallback:** If structured output fails, defaults to:
- `{topic} technology overview`
- `{topic} market size`
- `{topic} key players`

---

### Phase 2: Search Execution (The Loop)
Iterates through each approved query:

1. Executes `SearchTool.run(query)` → Returns `List[SearchResult]`
2. Formats results into readable text:
   ```
   Title: {item.title}
   URL: {item.href}
   Summary: {item.body}
   ---
   ```
3. Aggregates findings per query

**Error Handling:** Individual search failures are logged but do not halt execution.

---

### Phase 3: Synthesis
Synthesizes all gathered findings into a structured report.

**Prompt Template:**
```
Analyze these raw notes on '{topic}' and generate a final report.

RAW NOTES:
{all_data}
```

Uses `ResearchReport` Pydantic model for type-safe structured output.

**Fallback:** If synthesis fails, generates an error report containing raw collected data.

---

### Phase 4: Delivery
Formats the structured report as Markdown and saves via Scribe.

**Output Format:**
```markdown
# {report.title}

**Date:** Today

## Executive Summary
{report.executive_summary}

## Key Findings
- {item1}
- {item2}
- ...

## Strategic Outlook
{report.strategic_outlook}
```

**Filename:** `Research_{topic_replaced_with_underscores}.md`  
**Destination:** `0 - Inbox` folder in Obsidian vault

---

## Integration Points

| Component | Purpose |
|-----------|---------|
| `LLM` | Structured plan generation and report synthesis |
| `SearchTool` | Web search execution for information gathering |
| `BrowserTool` | Available for advanced scraping (not actively used in current flow) |
| `Scribe` | Persists final report to Obsidian vault |

---

## Role-Based Architecture
The agent uses role-based initialization (`LLM(role="default")`) aligning with Cobalt's broader routing strategy for specialized agent behaviors.

---

## See Also
- `scanner_orchestrator` - Parallel scanner execution
- `semantic_tagger` - Content classification
- `scribe` - Obsidian note management