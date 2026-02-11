"""
Cobalt Constitution Generator (Master Version)
Contains:
1. Dashboard (The Root)
2. System Manifest (5 Depts, Coach Role, Hardware Stack)
3. Security Architecture (Zero Trust, Vault, JIT)
4. ADRs (Distributed Protocol, Python-First)
5. Project Management (Roadmap, Backlog)
"""
import os
import sys
import importlib.util
from datetime import datetime

# --- 1. ROBUST SCRIBE LOADER ---
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

# --- 2. FRONTMATTER DEFINITIONS ---

arch_frontmatter = f"""---
status: Done
priority: P0 (Critical)
module: Ops
phase: 1 (Foundation)
complexity: M
tags: [cobalt, architecture, documentation]
created: {current_date}
---
"""

pm_frontmatter = f"""---
status: In Progress
priority: P1 (High)
module: Ops
phase: 3 (Capabilities)
complexity: S
tags: [cobalt, planning, roadmap]
created: {current_date}
---
"""

dashboard_frontmatter = f"""---
status: In Progress
priority: P0 (Critical)
module: Core
phase: 1 (Foundation)
complexity: L
tags: [cobalt, root, dashboard]
created: {current_date}
---
"""

# --- 3. THE CONSTITUTION CONTENT ---

files_to_create = {
    
    # ---------------------------------------------------------
    # THE DASHBOARD (Updated with all ADRs)
    # ---------------------------------------------------------
    "0 - Projects/Cobalt/00 Cobalt Master Plan.md": f"""{dashboard_frontmatter}
# Cobalt Command Center

## 1. Strategy & Ops (Level 1)
* [[System Manifest]] - The Stack, Hierarchy, and Roles.
* [[Security Architecture]] - Zero Trust, JIT Access, and Kill-Switches.
* [[ADR-001 Cobalt-Ion Distributed Protocol]] - Architecture Decisions.
* [[ADR-002 Hybrid AI Compute]] - Local vs. Cloud Model Strategy.
* [[ADR-003 Python-First Architecture]] - Ion HUD Technology Stack.

## 2. Project Management (Level 2)
* [[Roadmap]] - The Strategic Phases (Q1/Q2 Goals).
* [[Backlog]] - Future ideas and holding pen.

## 3. Execution (Level 3)
![[Cobalt Project Board]]
""",

    # ---------------------------------------------------------
    # LEVEL 1: MASTER PLAN
    # ---------------------------------------------------------

    "0 - Projects/Cobalt/00 - Master Plan/System Manifest.md": f"""{arch_frontmatter}
# Cobalt System Manifest

## 1. The Vision
**Cobalt** is a distributed, semi-autonomous trading system acting as a "Chief of Staff."
**Dejan** is the CEO and final decision-maker.

## 2. The Hierarchy

### Level 1: The CEO (Dejan)
* **Role:** The Decision Maker.
* **Responsibilities:**
    * Setting Strategic Goals.
    * Final Approval on "High Risk" Actions.
    * Risk Control Override.

### Level 2: Cobalt (The Chief of Staff & Performance Coach)
* **Role:** The Brain & The Mirror.
* **Responsibilities:**
    * **Orchestration:** Directing the 5 Departments below.
    * **Coaching:** Reviewing Scribe's journals to provide psychological feedback.
    * **Gatekeeping:** Protecting the CEO from noise and emotional trading.
    * **Memory:** Maintaining the context of all projects and trades.

### Level 3: The Departments (The Workforce)
* **Strategos (Tactical)**
    * Market Analysis & Technical Indicators.
    * Quant Logic & Strategy Generation.
    * Pattern Recognition Engine.
* **Ion (Interface)**
    * Windows HUD Overlay (PyQt6).
    * TradeStation Execution Bridge.
    * Real-time Data Visualization.
* **Scribe (Ops)**
    * Documentation & Knowledge Management.
    * Automated Journaling & Logging.
    * Project Management (Kanban Updates).
* **Sentinel (Risk)**
    * Position Sizing Logic.
    * "Kill Switch" Enforcement.
    * Compliance & Privacy Guardrails.
* **Scout (Research)**
    * Data Gathering (FinanceTool).
    * Sentiment Analysis (News/Social).
    * Web Browsing & Due Diligence.

## 3. The Hardware Stack

* **The Brain (Mac Studio M2 Ultra)**
    * **Specs:** 96GB RAM, 2TB SSD.
    * **Role:** Central Compute Node.
    * **Workload:** Hosts DeepSeek-R1 (Local LLM), Postgres DB, and Core Logic.

* **The Engine (Windows Workstation)**
    * **Role:** Dedicated Execution Environment.
    * **Workload:** Runs TradeStation Platform and Ion Agent (HUD).
    * **Constraint:** Zero-latency link to Mac via Tailscale.

* **The Console (Lenovo X1 Carbon)**
    * **Role:** Primary Development Interface.
    * **Workload:** VSCode (Remote SSH), Task Management, Ops Control.
    * **Security:** Biometric Access required for code changes.

* **The Red Phone (Mobile iOS/Android)**
    * **Role:** Command & Control (C2).
    * **Workload:** Mattermost Alerts ("Trade Signal"), MFA "Kill Switch" Approvals.
    * **Access:** Emergency System Shutdown.

## 4. The Software Stack
* **Core Intelligence (Cobalt):**
    * **Language:** Python 3.11+
    * **Models:** DeepSeek-R1 (Thinking), OpenAI o3-mini (Speed), Gemini 1.5 Pro (Architect).
    * **Memory:** PostgreSQL (Vector + Relational), Obsidian (Markdown).

* **Departmental Stacks:**
    * **Strategos:** `pandas`, `numpy`, `ta-lib` (Technical Analysis).
    * **Ion:** `PyQt6` (GUI), `pyzmq` (Networking), `EasyLanguage` (TradeStation).
    * **Scribe:** `obsidian-api`, `jinja2` (Templating).
    * **Sentinel:** `pydantic` (Data Validation), `cryptography` (Security).
    * **Scout:** `playwright` (Browsing), `beautifulsoup4` (Scraping).
""",

    "0 - Projects/Cobalt/00 - Master Plan/Security Architecture.md": f"""{arch_frontmatter}
# Cobalt Security Architecture (Zero Trust)

## 1. Core Philosophy: "Assume Breach"
We operate under the assumption that the network is compromised. Trust is never granted implicitly based on location (LAN) or device ownership.
* **Verify Explicitly:** Always authenticate and authorize based on all available data points.
* **Use Least Privilege:** Limit user access with Just-In-Time and Just-Enough-Access (JIT/JEA).
* **Assume Breach:** Minimize blast radius and segment access.

## 2. Identity & Access Management (IAM)
* **The Identity Provider:** Tailscale is the root of trust for *Device Identity*.
* **MFA Protocol:** Critical actions (Trade > $X, System Config Changes) require out-of-band verification via Mattermost (Mobile).
* **Service-to-Service Auth:**
    * Components (e.g., Mac -> Windows) must authenticate via **mTLS** or **Signed JWTs**.
    * `Ion` will reject commands from `Cobalt` that are not cryptographically signed by `Sentinel`.

## 3. Secrets Management (The Vault)
* **No Hardcoded Keys:** API Keys (TradeStation, OpenAI) are NEVER stored in plain text code or environment variables.
* **The Cobalt Vault:**
    * Secrets are stored in an encrypted local keystore (AES-256).
    * **Injection:** Secrets are loaded into memory *only* at runtime process initialization.
    * **Rotation:** Keys are rotated regularly.

## 4. Just-In-Time (JIT) Execution
* **Standing Privileges:** `Ion` (The Executor) has **Read-Only** access to the broker by default.
* **The Token Flow:**
    1.  `Strategos` spots a trade.
    2.  `Sentinel` validates risk checks.
    3.  `Sentinel` issues a **One-Time Execution Token (OTET)**.
    4.  `Ion` uses the OTET to unlock the "Execute" function for *that specific trade only*.
    5.  Token expires immediately after execution or timeout (500ms).

## 5. Network Micro-Segmentation
* **The Airlock:**
    * `Scout` (Research/Web Scraper) is isolated in a "Dirty" VLAN/Container.
    * `Scout` CANNOT talk to `Ion` (Execution) or `Sentinel` (Risk).
    * `Scout` can only write to a sanitized "Drop Zone" in the Database.
* **Tailscale ACLs:**
    * **Mac Studio:** Can talk to Windows (Port 5555 Only).
    * **Windows:** Can talk to Mac Studio (Postgres Port Only).
    * **External:** All inbound traffic blocked.
""",

    # ---------------------------------------------------------
    # ADRs
    # ---------------------------------------------------------

    "0 - Projects/Cobalt/00 - Master Plan/ADR/ADR-001 Cobalt-Ion Distributed Protocol.md": f"""{arch_frontmatter}
# ADR-001: The Cobalt-Ion Distributed Architecture
## Status: ACCEPTED
## Decision
We use a **Distributed Actor Model**:
* **Cobalt (Mac):** Generates the "Strategy Math" (Scoring Profile).
* **Ion (Windows):** Runs the "Math" 10x/sec against live data to paint the HUD.
* **Protocol:** JSON payloads over Tailscale LAN.
""",

    "0 - Projects/Cobalt/00 - Master Plan/ADR/ADR-002 Hybrid AI Compute.md": f"""{arch_frontmatter}
# ADR-002: Hybrid AI Compute Strategy
## Status: ACCEPTED
## Decision
* **DeepSeek-R1 (Local 70B):** Used for "Morning Prep" and deep reasoning. Zero data leakage.
* **OpenAI o3-mini (Cloud):** Used for fast, non-sensitive pattern recognition during the day.
* **Gemini 1.5 Pro (Cloud):** Used as the System Architect and Code Generator (Massive Context).
""",

    "0 - Projects/Cobalt/00 - Master Plan/ADR/ADR-003 Python-First Architecture.md": f"""{arch_frontmatter}
# ADR-003: Python-First Architecture
## Status: ACCEPTED
## Decision
We will use **Python (PyQt6)** for the Ion HUD.
* **Reasoning:** Modern Python is fast enough for human-speed trading (HUD updates). It simplifies the codebase (one language for Brain and HUD) and allows code sharing (Pydantic models).
""",

    # ---------------------------------------------------------
    # LEVEL 2: PROJECT MANAGEMENT
    # ---------------------------------------------------------

    "0 - Projects/Cobalt/90 - Project Management/Roadmap.md": f"""{pm_frontmatter}
# Cobalt Strategic Roadmap

## Phase 1: The Core (Completed) ✅
* Basic Agent Setup (Hello World).
* Configuration System (YAML).
* Logging & Tooling.

## Phase 2: The Brain (Completed) ✅
* Memory System (Postgres).
* Scribe Tool (Obsidian Integration).
* DeepSeek Local Model Integration.

## Phase 3: The Tactical Department (Active) 🚧
* **Feature:** Data Feeds (FinanceTool).
* **Feature:** Strategy Playbook (YAML -> Python).
* **Feature:** Backtester (Validating Strategies).

## Phase 4: The Ion HUD (Next) 📅
* **Epic:** Build Python/PyQt Overlay for Windows.
* **Epic:** Establish Socket/ZMQ Link between Mac and Windows.
* **Epic:** Zero Trust Security Implementation (JIT/Vault).

## Phase 5: The Ops Department (Future) 🔮
* **Epic:** Mattermost Chat Integration.
* **Epic:** Automated Journaling.
""",

    "0 - Projects/Cobalt/90 - Project Management/Backlog.md": f"""{pm_frontmatter}
# Cobalt Product Backlog
## Unscheduled Ideas
* [ ] Integrate Discord scraping for sentiment analysis.
* [ ] Build "Ion Voice" for audio alerts.
* [ ] Research "Mean Reversion" strategy implementation.
"""
}

# --- 4. EXECUTE WRITE ---

print("📝 Scribe initializing Cobalt Constitution...")

for full_path, content in files_to_create.items():
    try:
        # Resolve Folder/Filename
        path_str = str(full_path)
        last_slash = path_str.rfind("/")
        
        if last_slash == -1:
            print(f"❌ Invalid path format: {full_path}")
            continue
            
        folder = path_str[:last_slash]
        filename = path_str[last_slash+1:]
        
        # Write
        result = scribe.write_note(filename=filename, content=content, folder=folder)
        print(f"✅ Generated: {full_path}")
        
    except Exception as e:
        print(f"❌ Failed: {full_path} | Error: {e}")

print("\n🏁 Cobalt Constitution generated.")