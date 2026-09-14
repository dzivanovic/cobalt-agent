# Morning Briefing Skill

## Overview
`cobalt_agent/skills/productivity/briefing.py`

The `MorningBriefing` class is the Daily Market Intelligence Generator. It orchestrates tools to collect market data, news, and generate a structured daily digest.

## Class: MorningBriefing

### Description
Daily Market Intelligence Generator. Orchestrates tools to collect market data, news, and generate a structured daily digest.

### Constructor
```python
def __init__(self)
```

Initializes components:
1. Loads configuration
2. Creates LLM instance
3. Initializes tools (Scribe, FinanceTool, SearchTool)

### Available Tools
- `Scribe`: Writes report to Obsidian vault
- `FinanceTool`: Fetches market data for stock tickers
- `SearchTool`: Retrieves top technology and finance news

### Methods

#### run
```python
def run() -> str
```

Generates the daily morning briefing report.

**Returns:** Path to the saved Markdown file in Obsidian vault

### Execution Flow

#### Step 1: Data Gathering (`_gather_data`)
Collects raw data from multiple sources:

**Markets Data:**
- Fetches data for configured tickers: NVDA, SPY, BTC-USD
- Handles errors gracefully with warning logs

**News Search:**
- Queries for "top technology and finance news today"
- Returns up to 5 news items

#### Step 2: LLM Synthesis
Sends gathered data to LLM with a structured prompt asking for:
- Executive summary (3 sentences)
- Market analysis (Bullish/Bearish/Neutral)
- Top 3-5 headlines
- Strategic thought/question

Uses `llm.ask_structured()` with Pydantic model for type-safe output.

#### Step 3: Markdown Formatting
Creates a structured Markdown report with:
- Title with today's date
- Generation timestamp
- Executive Summary section
- Market Pulse section
- Top Headlines list
- Strategic Thought quote

#### Step 4: Vault Delivery
- Saves to `0 - Inbox` folder
- Filename format: `Briefing_YYYY-MM-DD.md`

### Pydantic Model: BriefingReport

```python
class BriefingReport(BaseModel):
    executive_summary: str      # 3-sentence market summary
    market_analysis: str        # Technical analysis
    top_headlines: List[str]    # 3-5 critical headlines
    strategic_thought: str      # Provocative question/insight
```

### Error Handling
- Falls back to raw data if LLM synthesis fails
- Logs warnings for tool failures
- Returns error message path on failure

## Key Components
- `LLM`: For structured report synthesis
- `FinanceTool`: Market data collection
- `SearchTool`: News aggregation
- `Scribe`: Obsidian delivery

## See Also
- `Scribe` - Obsidian integration skill
- `DeepResearch` - Research report generation