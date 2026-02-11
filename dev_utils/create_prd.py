"""
Cobalt Requirements Generator
Creates the PRD-001 based on the 'Strategic Pause' conversation.
"""
import os
import sys
import importlib.util
from datetime import datetime

# --- LOAD SCRIBE ---
current_dir = os.getcwd()
scribe_path = os.path.join(current_dir, "cobalt_agent", "skills", "productivity", "scribe.py")

try:
    if not os.path.exists(scribe_path):
        raise FileNotFoundError(f"File not found at {scribe_path}")
    
    spec = importlib.util.spec_from_file_location("scribe_module", scribe_path)
    scribe_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scribe_module)
    Scribe = scribe_module.Scribe
    print("✅ Scribe Class Loaded Successfully.")
except Exception as e:
    print(f"❌ Failed to load Scribe: {e}")
    sys.exit(1)

scribe = Scribe()
current_date = datetime.now().strftime("%Y-%m-%d")

# --- PRD CONTENT ---

prd_content = f"""---
status: Approved
priority: P0
module: Core
tags: [cobalt, requirements, prd, ion]
created: {current_date}
---

# PRD-001: Cobalt-Ion Tactical HUD

## 1. Executive Summary
**The Vision:** Build a "Co-Pilot" system for manual day trading.
**The Problem:** Professional trading requires processing dozens of variables (RVOL, Levels, Tape, News) in real-time. Humans are slow and emotional.
**The Solution:** A "Heads-Up Display" (HUD) that acts as a real-time **Confidence Gauge**. It calculates the mathematical "Expected Value" (EV) of a trade 10x/second, allowing the trader to execute with conviction.

## 2. Core Philosophy
1.  **Not an Auto-Trader:** The system NEVER executes trades autonomously. It observes, calculates, and suggests. The user pulls the trigger.
2.  **Distributed Brain:** * **Mac Studio (Cobalt):** The Strategist. Slow, deep thinking. Analysis of Context & Catalysts.
    * **Windows PC (Ion):** The Calculator. Fast, reactive math. Visualizing the HUD.
3.  **Python-First:** Both components run on Python (PyQt6 for Windows HUD) to ensure speed of development and shared logic.

## 3. User Stories

### Story A: The "Morning Briefing" (Context)
**As a** Trader,
**I want** Cobalt to scan the market for "In Play" stocks and identify the specific *Strategies* (from my Playbook) that apply to them (e.g., "NVDA is an Earnings Gap"),
**So that** I start the day with a curated list of opportunities, not just raw tickers.

### Story B: The "Formula Injection" (Handoff)
**As a** System Architect,
**I want** Cobalt to send a "Math Package" (JSON) to Ion containing the specific *Weights and Variables* for the day (e.g., "For NVDA, Gap Fill is +10 points, Resistance at $145 is -20 points"),
**So that** Ion can run the math locally without latency, acting as a "dumb calculator" for Cobalt's "smart rules."

### Story C: The "Tactical Engagement" (The HUD)
**As a** Trader executing a trade,
**I want** a visual Gauge (0-100) that updates in real-time based on Price, Volume, and Time,
**So that** I can intuitively see if the trade is degrading (Score dropping) or improving (Score rising) without doing mental math.
* *Example:* "I am long NVDA. Volume dries up -> Score drops 10 points -> Gauge turns Yellow -> I trim my position."

## 4. Functional Requirements

### 4.1 The Scoring Engine (Dynamic EV)
The Score (0-100) is calculated as:
$$ Score = Base + Fuel - Friction - Decay $$
* **Base:** Static score from the Daily Setup (e.g., "A+ Setup" = 60).
* **Fuel (Momentum):** Live modifiers (e.g., `RVOL > 2.0` adds +10).
* **Friction (Risk):** Proximity to Resistance (e.g., `Dist < $0.10` subtracts -20).
* **Decay (Time):** Penalty for stalling (e.g., `-1 point` per minute of chop).

### 4.2 The "Math Package" Protocol
Cobalt must send a JSON payload to Ion containing:
* `Ticker`: Symbol (e.g., "NVDA").
* `Strategies`: List of active setups (e.g., ["GapAndGo", "BellaFade"]).
* `Zones`: Key Price Levels (Entry, Stop, Target).
* `Coefficients`: The weights for the Scoring Engine.

### 4.3 The Multi-Strategy Capability
The system must support **Conflicting Strategies** simultaneously.
* *Scenario:* NVDA gaps up.
* *HUD State:* Ion displays *two* potential scores:
    1.  **Long Score:** For the "Gap & Go" breakout.
    2.  **Short Score:** For the "Extension Fade" reversal.

## 5. Technical Constraints
* **Language:** Python 3.11+.
* **GUI Framework:** PyQt6 (Windows) for transparent overlays.
* **Communication:** ZeroMQ (ZMQ) over Tailscale LAN.
* **Data Source:** TradeStation API (connected locally on Windows).
* **Latency Target:** < 50ms from Tick to HUD Update.

## 6. Future Extensibility
* **Discord Integration:** Manual scraping of trader sentiment to adjust "Base Scores."
* **Journaling:** Automated logging of *why* a score was high/low at the moment of execution.
"""

# --- EXECUTE ---
print("📝 Generating PRD-001 based on Strategic Conversation...")

try:
    folder = "0 - Projects/Cobalt/90 - Project Management/Requirements"
    filename = "PRD-001 Cobalt-Ion Tactical HUD.md"
    
    scribe.write_note(filename=filename, content=prd_content, folder=folder)
    print(f"✅ Successfully Created: {folder}/{filename}")

except Exception as e:
    print(f"❌ Failed to create PRD: {e}")