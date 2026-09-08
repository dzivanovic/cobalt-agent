---
title: "Story-001: Initial Brainstorm"
status: Active
module: [Requirements]
tags: [cobalt, user_story]
created: 2026-02-23
---

# Story-001: Initial Brainstorm

## The Cobalt-Ion Distributed Architecture

### System Overview

**Cobalt (Mac Studio - The Strategist):**
- Runs the heavy AI (DeepSeek 70B)
- Monitors the "Catalyst" and "Setup" phases (Minutes/Hours)
- Sets the Rules and generates Scoring Profiles

**Ion (Windows PC - The Engine):**
- A lightweight Python application
- Monitors the "Trade" and "Execution" phases (Milliseconds)
- Runs the math based on formulas provided by Cobalt

### The Data Flow (The "Formula Injection")
1. **Cobalt** scans the market (continuously) and identifies a Ticker as "In Play."
2. **Cobalt** selects *all applicable strategies* from the Playbook (e.g., NVDA fits both "Gap & Go" and "Fade").
3. **Cobalt** generates a **Scoring Profile (JSON)** and pushes it to Ion.
   - This profile contains *Variables* (Weights), not *Decisions*.
   - Example: `{"strategy": "BellaFade", "trigger": "Price < VWAP", "rvol_weight": 10}`.
4. **Ion** subscribes to live data (TradeStation).
5. **Ion** calculates the Score (0-100) and EV live.
6. **Ion** paints the HUD.

### The Core Concept: "Configurator vs. Calculator"

To achieve the speed you need (color changing instantly as volume dries up), we cannot ask the LLM to calculate the score every second. The LLM is too slow and "fuzzy."

Instead, we split the brain:

- **Cobalt (The Coach / Mac):** _Sets the Rules._
  - Before the market opens (or when you spot a setup), Cobalt analyzes the context (News, Daily Chart, Sector).
  - Output: Generates a **"Scoring Profile"** (a JSON file).
    - Example: "For NVDA today: If RVOL > 3, +10 points. If Price hits 145.50 (Resistance), -15 points. If SPY drops, -20 points."

- **Ion (The Engine / Windows):** _Runs the Math._
  - Reads the live data feed and applies the _Scoring Profile_ 10 times a second.
  - Output: Draws the Gauge. It doesn't "think"; it just calculates.

### The Visual Metaphor: "The Confidence Gauge"

Imagine a UI widget floating next to your TradeStation charts.

- **The Needle (0-100):** Represents your **Dynamic Score**.
  - **0-40 (Red):** "No Go" or "Abort." (Iceberg ahead).
  - **41-70 (Yellow):** "Cautious Hold." (Trim position, tighten stops).
  - **71-100 (Green):** "Conviction." (Add size, hold for target).

- **The Delta (Rate of Change):**
  - If the needle suddenly drops from 90 to 60 in 2 seconds, that's your alert to get out _before_ the price collapses. This is faster than waiting for a candle to close red.

### The Logic: How We Calculate "Dynamic EV"

Dynamic EV = (Prob(win) × Dist(target)) - (Prob(loss) × Dist(stop))

**The Inputs (The Variables Ion Monitors):**
1. **The Setup Score (Static Baseline):**
   - Defined by Cobalt in the morning. (e.g., "A+ Setup = Base Probability 60%").
2. **The "Fuel" (Real-Time Momentum):**
   - **RVOL:** Is volume expanding on the move? (Boosts Probability).
   - **Tape Speed:** Are prints accelerating?
3. **The "Friction" (Resistance/Support):**
   - As Price → Resistance, the **Reward** shrinks, but the **Risk of Reversal** grows.
   - Effect: EV drops rapidly as you hit target. The HUD goes yellow ("Take Profit").
4. **The "Decay" (Time):**
   - If you enter and price goes sideways for 10 minutes, probability of success usually drops.
   - Effect: The score slowly bleeds down, turning the gauge yellow/red solely because "It's taking too long."

### Technical Architecture: The "Sidecar" Pattern

**The Stack:**
- **Frontend (Ion):** **Python** (PyQt6 or similar for overlay).
  - Why? Cross-platform development. Deep integration with Windows via native APIs. Can draw "Always on Top" transparent overlays.
- **Data Source:** **TradeStation API / NinjaTrader API.**
  - Ion connects directly to the feed. No round-trip to the Mac for data.
- **The Brain Link:**
  - Cobalt (Mac) runs a **Web Dashboard** (or API endpoint).
  - You chat with Cobalt: _"Watch NVDA for a Gap and Go."_
  - Cobalt sends the **Parameters** to Ion over the LAN.
  - Ion lights up: _"NVDA Watchlist Active. Waiting for Breakout at $145."_

### Strategy: How to Build This

**Phase 1: The "Dashboard" (Mac-based Prototype)**
- Use Python on the Mac.
- Use a fast plotting library (like `Streamlit` or `Dash`) to visualize the "Gauge."
- Input: Simulate the data feed (or hook into a lightweight API like Alpaca/Polygon).
- Goal: Perfect the **Scoring Formula**.

**Phase 2: The "Overlay" (Windows Port)**
- Once the math works, port the _Calculator_ to Python on Windows (Ion).
- Build the visual overlay using PyQt6.

### Trade Phases (State Management)

The HUD needs to behave differently depending on where you are in the trade.

1. **Phase 1: The Stalk (Watchlist)**
   - **Gauge:** Shows **"Setup Quality"**.
   - **Goal:** Alert you when price hits the Trigger _with_ High Score.
   - Logic: Focus heavily on "Gap Maintenance" and "Pre-market Volume."

2. **Phase 2: The Engagement (In Trade)**
   - **Gauge:** Shows **"Holding Confidence"**.
   - **Goal:** Tell you when to fold.
   - Logic:
     - **Time Decay:** Starts ticking. If price doesn't move, score drops.
     - **Extension:** As price moves away from VWAP, risk increases (Score might dip to Yellow to signal "Trim").
     - **Resistance:** As price hits Target, EV drops (Risk of reversal).

### Multi-Strategy Reality

The critical requirement: NVDA having _multiple_ active strategies simultaneously.

**The Architectural Fix:** Cobalt cannot send "One Instruction." It must send a **Strategy Package**. Ion will display **Multiple Gauges** (or a Split Gauge) for NVDA:

1. **Long Gauge (Gap & Go):** Currently at **30/100** (Waiting for breakout).
2. **Short Gauge (Fade):** Currently at **10/100** (Not extended enough).

As the day evolves, if NVDA rips to $145.50 and volume dies:

- **Long Gauge:** Drops to 0 (Trade invalidated).
- **Short Gauge:** Spikes to **95/100** (Green Light).

This is why the Mac must run all day. It watches the "Macro" shift. If the SPY suddenly tanks, Cobalt updates the package: _"Market is now Bearish. Disable all Long strategies. Boost Short EV by 20%."_ Ion receives this update instantly and the HUD changes color before you even blink.

### The Playbook Architecture

Professional traders only execute trades that are in their Playbook.

**Hierarchical State Machine:**
- **Level 1 (Catalyst/Context):** "NVDA is In Play (Earnings)." (Determined by Cobalt/Mac).
- **Level 2 (Setup/Regime):** "It is currently a 'Morning Drive' or 'Reversal' regime." (Determined by Cobalt/Mac).
- **Level 3 (Trade Strategy):** "Active Strategies: `GapAndGo` (Long) AND `BellaFade` (Short)." (Cobalt sends BOTH to Ion).
- **Level 4 (Execution):** "Price broke $145.50 on High Volume -> Trigger `GapAndGo`." (Ion/Windows executes).

### The "Formula Injection" Architecture

Cobalt (The Strategist) and Ion (The Engine) interaction:

1. **Cobalt (Morning/Prep):** Analyzes the context (Daily chart, News, Sector). Determines _what matters today_.
   - Example: "For NVDA, because the market is bearish, 'Gap Strength' is less important, but 'Relative Volume' is critical. Also, there is an iceberg (resistance) at $145.50."
   
2. **The Artifact:** Cobalt generates a **Strategy Config Object (JSON)** that contains _weights and penalties_, not just hard rules.

3. **Ion (Live):** Receives this object. It plugs live data into the formula 10 times a second.

**The Strategy Config Object (JSON):**
```json
{
  "ticker": "NVDA",
  "strategy": "Gap_And_Go",
  "direction": "LONG",
  "levels": {
    "entry": 142.50,
    "stop": 141.00,
    "target": 145.50,
    "resistance_zones": [145.50, 148.00]
  },
  "scoring_weights": {
    "base_score": 65,
    "rvol_multiplier": 5.0,
    "spy_correlation": 10.0,
    "time_decay": -0.5
  },
  "abort_conditions": [
    "price < 140.00",
    "rvol < 0.2 after 10:00"
  ]
}
```

**Why this is powerful:**
- **Ion doesn't need to know _why_ SPY correlation matters.** It just knows: _"If SPY is Green, add 10 points."_
- **Cobalt can change the strategy dynamically.** On a crazy Fed Day, Cobalt might send a config with `base_score: 40` (start cautious) and `time_decay: -2.0` (get out fast if it stalls).

### Next Steps

1. **Don't write the code yourself.** Delete the skeleton I gave you.
2. **Define the Interface:** We only need to define _how_ Cobalt talks to the Strategy Engine (e.g., `analyze(data) -> signal`).
3. **The "Forge" (Future):** When we get to Phase 7, you will paste the SMB PDF, and **Cobalt** will generate `second_day_play.py` and run the backtest.

### Revised Strategic Roadmap

Since we are avoiding "Rapid Coding," let's lock in the **Architecture** before we write another line.

**Does this look like the correct ecosystem to you?**

1. **Mac Studio (The Brain)**
   - **DeepSeek 70B (Local):** The reasoning engine.
   - **Postgres (Docker):** The memory.
   - **Cobalt Core:** The manager.
   - Status: **Built.**

2. **Windows Rig (The Body)**
   - **TradeStation/DAS:** The platform.
   - **Ion Agent (Python Service):**
     - Listens on port 5555.
     - Reads "Account Value" and "Positions" every 1s.
     - Can trigger "Flatten" or "Buy" instantly.
   - Status: **Not Started (Phase 6).**

3. **The "Nerve" (LAN)**
   - A dedicated, encrypted channel between Mac and PC.
   - Keeps the "Brain" safe from Windows viruses/crashes.

### Decision Point

Do you want to continue fleshing out the **Brain (Playbook Logic)** on the Mac now, knowing it will eventually send commands to Ion?

OR

Do you want to switch gears and design the **Ion Protocol** (how the two machines talk) so we know what data we need to send?