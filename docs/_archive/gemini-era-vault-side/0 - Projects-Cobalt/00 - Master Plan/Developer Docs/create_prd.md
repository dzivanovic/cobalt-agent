# create_prd.py

## Overview

The `create_prd.py` script is a utility for generating Product Requirement Documents (PRDs) for Project Cobalt. It creates PRD-001 (Cobalt-Ion Tactical HUD) based on strategic conversations and architectural decisions.

## Purpose

This script serves the following functions:
- Generates comprehensive PRD documents with proper YAML frontmatter
- Creates detailed requirements for the Cobalt-Ion Tactical HUD system
- Uses the Scribe integration for consistent note formatting
- Places PRDs in the `0 - Projects/Cobalt/90 - Project Management/Requirements` directory

## Location

```
dev_utils/create_prd.py
```

## Dependencies

- `src/cobalt_agent/skills/productivity/scribe.py` - Scribe class for note creation
- Dynamic module loading via `importlib.util`

## How It Works

The script follows this process:

1. **Scribe Loader**: Dynamically loads the Scribe class from its file path
2. **PRD Content Generation**: Creates comprehensive PRD content with:
   - YAML frontmatter (status, priority, module, tags, created date)
   - Executive summary with vision and problem statement
   - Core philosophy principles
   - User stories covering key scenarios
   - Functional requirements with technical specifications
   - Technical constraints and future extensibility
3. **Execution**: Uses Scribe.write_note() to create the PRD file

### PRD-001 Content Structure

The generated PRD includes:

| Section | Description |
|---------|-------------|
| Executive Summary | Vision, problem statement, and solution overview |
| Core Philosophy | Three guiding principles: Not an Auto-Trader, Distributed Brain, Python-First |
| User Stories | Three key scenarios: Morning Briefing, Formula Injection, Tactical Engagement |
| Functional Requirements | Scoring Engine (Dynamic EV) and Math Package Protocol specifications |
| Technical Constraints | Language, GUI framework, communication protocol, data source, latency targets |
| Future Extensibility | Discord integration and automated journaling plans |

## Usage

### Running the Script

From the project root:

```bash
uv run dev_utils/create_prd.py
```

### Expected Output

On successful execution:
```
📝 Generating PRD-001 based on Strategic Conversation...
✅ Successfully Created: 0 - Projects/Cobalt/90 - Project Management/Requirements/PRD-001 Cobalt-Ion Tactical HUD.md
```

### Error Handling

If Scribe fails to load:
```
❌ Failed to load Scribe: [error details]
```

The script exits with status code 1 if the Scribe module cannot be loaded.

## Key Concepts Documented

### The "Co-Pilot" System
- **Vision**: Build a real-time confidence gauge for manual day trading
- **Problem**: Professional trading requires processing dozens of variables (RVOL, Levels, Tape, News) in real-time
- **Solution**: A HUD that calculates mathematical "Expected Value" (EV) of a trade 10x/second

### Distributed Architecture
- **Mac Studio (Cobalt)**: The Strategist - Slow, deep thinking; Analysis of Context & Catalysts
- **Windows PC (Ion)**: The Calculator - Fast, reactive math; Visualizing the HUD

### Scoring Formula
```
Score = Base + Fuel - Friction - Decay
```

Where:
- **Base**: Static score from Daily Setup (e.g., "A+ Setup" = 60)
- **Fuel**: Momentum modifiers (e.g., RVOL > 2.0 adds +10)
- **Friction**: Risk proximity (e.g., Distance < $0.10 subtracts -20)
- **Decay**: Time penalty (e.g., -1 point per minute of chop)

## Related Documentation

- [Scribe](scribe.md) - Note creation utility
- [PRD-001 Cobalt-Ion Tactical HUD](../../../90 - Project Management/Requirements/PRD-001%20Cobalt-Ion%20Tactical%20HUD.md) - The generated PRD document
- [Sprint_05_The_Ion_Bridge](../../../90 - Project Management/Sprints/Sprint_05_The_Ion_Bridge.md) - Ion Bridge sprint details
- [PRD-007 Sovereign Split-Brain Orchestration](../../../90 - Project Management/Requirements/PRD-007%20Sovereign%20Split-Brain%20Orchestration.md) - Multi-platform architecture requirements

## Maintenance Notes

This script should be run:
- When new major features or components are identified
- During initial project setup to establish requirements baseline
- When onboarding new team members to understand system architecture

The PRD content is hardcoded and should be updated if requirements evolve.