"""
Script to populate the Obsidian Project Board with Phase 4 & 5 tasks.
Uses the Scribe tool to ensure correct formatting.
"""
import sys
import os

# Add project root to path so we can import the cobalt_agent package
# This assumes dev_utils/ is one level deep in the project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cobalt_agent.skills.productivity.scribe import Scribe

def create_task(id_num, title, priority, module, complexity, description):
    scribe = Scribe()
    # Format: "23 Strategos Agent Setup"
    filename = f"{id_num} {title}"
    
    # Frontmatter for your Kanban Board (Obsidian Canvas/Dataview compatible)
    content = f"""---
status: To Do
priority: {priority}
module: {module}
complexity: {complexity}
tags:
  - cobalt/task
created: 2026-02-10
---

# {title}

## Objective
{description}

## Acceptance Criteria
- [ ] Code implemented
- [ ] Verified with test script
"""
    # Save to 0 - Inbox (You can drag them to your board later)
    result = scribe.write_note(filename, content, folder="0 - Inbox")
    print(result)

if __name__ == "__main__":
    print("🚀 Generating Phase 4 & 5 Tasks...")
    
    # --- PHASE 4: TACTICAL (STRATEGOS) ---
    create_task("23", "Strategos Agent Setup", "P0", "Tactical", "M", 
                "Create the 'Strategos' class. This manages the Playbook and Risk, replacing the basic FinanceTool wrapper.")
    
    create_task("24", "Playbook Registry", "P1", "Tactical", "S", 
                "Create 'strategies.yaml' to define rules for Second Day Play and Fashionably Late Scalp.")
    
    create_task("25", "Strategy Interface", "P1", "Tactical", "M", 
                "Define the abstract Python class for a Strategy (check_entry, check_stop, calculate_probability).")
    
    create_task("26", "Second Day Play Impl", "P1", "Tactical", "L", 
                "Implement the specific logic from the SMB PDF: Day 1 Trend, Day 2 Open, RVOL checks.")
    
    create_task("27", "Backtest Engine", "P2", "Tactical", "XL", 
                "Create the engine that runs a Strategy against 90 days of historical minute-data.")

    # --- PHASE 5: OPS (STEWARD) ---
    create_task("28", "Ops Medical Stub", "P2", "Ops", "S", 
                "Create the Steward Agent shell to handle future medical billing tasks.")
    
    create_task("29", "Privacy Guardrails", "P0", "Ops", "M", 
                "Implement PII stripping to ensure no patient data ever hits the LLM.")

    print("\n✅ Done! Check your Obsidian '0 - Inbox' folder.")