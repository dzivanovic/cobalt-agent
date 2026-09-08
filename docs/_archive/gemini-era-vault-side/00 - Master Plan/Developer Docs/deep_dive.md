# Deep Research Agent (Deep Dive)

## Overview
`cobalt_agent/skills/research/deep_dive.py`

The `DeepResearch` class implements a multi-step research agent that follows a "Plan -> Search -> Analyze -> Report" loop.

## Class: DeepResearch

### Description
A multi-step research agent that follows a "Plan -> Search -> Analyze -> Report" loop using Pydantic models for type-safe LLM interactions.

### Constructor
```python
def __init__(self)
```

Initializes components:
1. Loads configuration
2. Extracts LLM model name
3. Initializes LLM instance
4. Initializes tools (SearchTool, BrowserTool)
5. Initializes Scribe skill for output delivery

### Available Tools
- `SearchTool`: Web search for information gathering
- `BrowserTool`: Advanced browser automation for web scraping
- `Scribe`: Writes final report to Obsidian vault

### Pydantic Models

#### ResearchPlan
```python
class ResearchPlan(BaseModel):
    queries: List[str]  # 3 distinct search queries for the topic
```

#### ResearchReport
```python
class ResearchReport(BaseModel):
    title: str                    # Professional report title
    executive_summary: str        # High-level findings summary
    key_findings: List[str]       # List of most important facts
    strategic_outlook: str        # Forward-looking analysis
```

### Methods

#### run
```python
def run(self, topic: str) -> str
```

Executes a multi-step research plan on a complex topic.

**Parameters:**
- `topic` (str): The research topic

**Returns:** Path to the saved report in Obsidian vault

### Execution Phases

#### Phase 1: Planning
Generates a research strategy with:
- 3 distinct search queries
- Uses LLM with `ResearchPlan` Pydantic model
- Falls back to default queries on error

#### Phase 2: Search Execution
For each query:
1. Runs `SearchTool` to gather results
2. Formats results into readable strings
3. Appends to findings list

**Result Format:**
```
Title: {item.title}
URL: {item.href}
Summary: {item.body}
---
```

#### Phase 3: Synthesis
Sends all findings to LLM with structured prompt asking for:
- Professional title
- Executive summary
- Key findings list
- Strategic outlook

Uses `ResearchReport` Pydantic model for type-safe output.

#### Phase 4: Delivery
Formats report as Markdown:
```markdown
# {report.title}
**Date:** Today

## Executive Summary
{report.executive_summary}

## Key Findings
- {item1}
- {item2}

## Strategic Outlook
{report.strategic_outlook}
```

Saves to `0 - Inbox` folder with filename: `Research_{topic}.md`

### Error Handling
- Falls back to default queries if planning fails
- Continues execution even if individual searches fail
- Generates error report with raw data if synthesis fails

## Key Components
- `LLM`: For structured plan and report generation
- `SearchTool`: Information gathering
- `BrowserTool`: Web scraping (if needed)
- `Scribe`: Report delivery to Obsidian

## See Also
- `MorningBriefing` - Daily briefing generation
- `Scribe` - Obsidian integration
- `DeepResearch` - Research report generation