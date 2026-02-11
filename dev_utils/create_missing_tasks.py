"""
Cobalt Task Generator
Creates the missing Phase 4 (Ion) and Phase 5 (Ops) tasks on the Project Board.
"""
import os
import sys
import importlib.util
from datetime import datetime

# --- 1. ROBUST SCRIBE LOADER (The "Smoking Gun" Fix) ---
# This works because 'uv run' executes from the Project Root.
current_dir = os.getcwd()
scribe_path = os.path.join(current_dir, "cobalt_agent", "skills", "productivity", "scribe.py")

print(f"🔍 Loading Scribe from: {scribe_path}")

try:
    if not os.path.exists(scribe_path):
        raise FileNotFoundError(f"File not found at {scribe_path}")

    # Load module directly by file path (bypassing package issues)
    spec = importlib.util.spec_from_file_location("scribe_module", scribe_path)
    scribe_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scribe_module)
    
    Scribe = scribe_module.Scribe
    print("✅ Scribe Class Loaded Successfully.")
except Exception as e:
    print(f"❌ Failed to load Scribe: {e}")
    sys.exit(1)

# Initialize
scribe = Scribe()
current_date = datetime.now().strftime("%Y-%m-%d")

# --- 2. DEFINE TASKS ---

tasks = {
    "30 Ion Core Architecture.md": f"""---
status: To Do
priority: P1 (High)
module: Interface
phase: 4 (Ion HUD)
complexity: L
tags: [cobalt, task, ion]
created: {current_date}
---

# 30 Ion Core Architecture

## Objective
Establish the foundational Python application for the **Windows HUD**.

## Requirements
* [ ] Create `ion_agent/` directory structure on Windows.
* [ ] Initialize a **PyQt6** application loop.
* [ ] Implement a **Transparent Overlay Window** (Click-through capable).
* [ ] Create a system tray icon for background management.
* [ ] Ensure it can run alongside TradeStation without stealing focus.

## Technical Notes
* Use `PyQt6.QtCore.Qt.WindowType.FramelessWindowHint`.
* Must handle high-DPI scaling (4K monitors).
""",

    "31 Cobalt-Ion Bridge.md": f"""---
status: To Do
priority: P0 (Critical)
module: Core
phase: 4 (Ion HUD)
complexity: M
tags: [cobalt, task, network]
created: {current_date}
---

# 31 Cobalt-Ion Bridge

## Objective
Create the low-latency communication link between **Cobalt (Mac)** and **Ion (Windows)**.

## Requirements
* [ ] Implement **ZeroMQ (ZMQ)** PUB/SUB pattern.
* [ ] **Publisher:** Cobalt (Mac) broadcasting strategy signals.
* [ ] **Subscriber:** Ion (Windows) listening for HUD updates.
* [ ] Define the JSON payload schema (Ticker, Action, Confidence, Price).
* [ ] Secure the connection over **Tailscale IP**.

## Technical Notes
* Latency target: < 50ms.
* Use `zmq.asyncio` for non-blocking I/O.
""",

    "32 HUD Widgets & Overlay.md": f"""---
status: To Do
priority: P1 (High)
module: Interface
phase: 4 (Ion HUD)
complexity: M
tags: [cobalt, task, ui]
created: {current_date}
---

# 32 HUD Widgets & Overlay

## Objective
Build the specific visual components that appear on the screen.

## Requirements
* [ ] **Confidence Gauge:** A visual bar/dial showing Model Confidence (0-100%).
* [ ] **Signal Box:** A "BUY/SELL" indicator that flashes on trigger.
* [ ] **Trade Log:** A small scrolling list of recent fills.
* [ ] **P&L Ticker:** Real-time session P&L display.

## Design
* "Dark Mode" aesthetic (Cyberpunk/High-Contrast).
* Green = Long, Red = Short.
""",

    "33 Mattermost C2 Integration.md": f"""---
status: To Do
priority: P1 (High)
module: Ops
phase: 5 (Ops)
complexity: M
tags: [cobalt, task, chat]
created: {current_date}
---

# 33 Mattermost C2 Integration

## Objective
Connect Cobalt to the "Red Phone" (Mattermost) for remote command and control.

## Requirements
* [ ] Create a Mattermost Bot Account ("Cobalt").
* [ ] Implement **Incoming Webhooks** for alerts (Trade Signals).
* [ ] Implement **Outgoing Webhooks** (or Slash Commands) for user commands.
* [ ] **Kill Switch:** Create a command `/cobalt stop` that halts all trading instantly.
* [ ] **Approval Flow:** Interactive buttons for "Approve Trade?" messages.
""",

    "34 Automated Trade Journaling.md": f"""---
status: To Do
priority: P2 (Normal)
module: Skills
phase: 5 (Ops)
complexity: S
tags: [cobalt, task, journaling]
created: {current_date}
---

# 34 Automated Trade Journaling

## Objective
Remove manual data entry by having Cobalt write its own trade logs.

## Requirements
* [ ] Capture execution details (Entry, Exit, Size, P&L).
* [ ] Capture "Why?" (The Strategy Logic snapshot at moment of trade).
* [ ] Format as a Markdown table.
* [ ] Append to the **Daily Note** in Obsidian via Scribe.

## Format
| Time | Ticker | Side | P&L | Strategy | Confidence |
|------|--------|------|-----|----------|------------|
"""
}

# --- 3. EXECUTE WRITE ---
print(f"📝 Creating {len(tasks)} missing tasks in '0 - Projects/Cobalt/Tasks'...")

target_folder = "0 - Projects/Cobalt/Tasks"

for filename, content in tasks.items():
    try:
        # Scribe.write_note(filename, content, folder)
        result = scribe.write_note(filename=filename, content=content, folder=target_folder)
        print(f"✅ Created: {filename}")
    except Exception as e:
        print(f"❌ Failed: {filename} | Error: {e}")

print("\n🏁 Board Updated. Run 'update_board.py' (or refresh Obsidian) to see changes.")