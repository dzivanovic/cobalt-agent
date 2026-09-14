# create_missing_tasks.py

## Overview

The `create_missing_tasks.py` script is a utility for generating missing Phase 4 (Ion HUD) and Phase 5 (Ops) tasks on the Project Board. It leverages the Scribe integration to create properly formatted task files in Obsidian.

## Purpose

This script serves the following functions:
- Creates 4 missing tasks related to Ion Core Architecture and Ops integration
- Uses the Scribe class for consistent note formatting
- Places tasks in the `0 - Projects/Cobalt/Tasks` directory

## Location

```
dev_utils/create_missing_tasks.py
```

## Dependencies

- `src/cobalt_agent/skills/productivity/scribe.py` - Scribe class for note creation
- Dynamic module loading via `importlib.util`

## How It Works

The script follows this process:

1. **Scribe Loader**: Dynamically loads the Scribe class from its file path
2. **Task Definition**: Defines 4 tasks with YAML frontmatter and markdown content
3. **Execution**: Uses Scribe.write_note() to create each task file

### Tasks Created

| Filename | Title | Phase | Priority |
|----------|-------|-------|----------|
| 30 Ion Core Architecture.md | Establish foundational Python app for Windows HUD | 4 (Ion HUD) | P1 (High) |
| 31 Cobalt-Ion Bridge.md | Create low-latency communication link between Cobalt and Ion | 4 (Ion HUD) | P0 (Critical) |
| 32 HUD Widgets & Overlay.md | Build visual components for screen overlay | 4 (Ion HUD) | P1 (High) |
| 33 Mattermost C2 Integration.md | Connect to Mattermost for remote command and control | 5 (Ops) | P1 (High) |
| 34 Automated Trade Journaling.md | Remove manual data entry for trade logs | 5 (Ops) | P2 (Normal) |

## Usage

### Running the Script

From the project root:

```bash
uv run dev_utils/create_missing_tasks.py
```

### Expected Output

On successful execution:
```
🔍 Loading Scribe from: [path]/scribe.py
✅ Scribe Class Loaded Successfully.
📝 Creating 5 missing tasks in '0 - Projects/Cobalt/Tasks'...
✅ Created: 30 Ion Core Architecture.md
✅ Created: 31 Cobalt-Ion Bridge.md
✅ Created: 32 HUD Widgets & Overlay.md
✅ Created: 33 Mattermost C2 Integration.md
✅ Created: 34 Automated Trade Journaling.md

🏁 Board Updated. Run 'update_board.py' (or refresh Obsidian) to see changes.
```

### Error Handling

If Scribe fails to load:
```
❌ Failed to load Scribe: [error details]
```

The script exits with status code 1 if the Scribe module cannot be loaded.

## Task Structure

Each task includes:
- **YAML Frontmatter**: status, priority, module, phase, complexity, tags, created date
- **Objective Section**: Clear description of what needs to be accomplished
- **Requirements Section**: Checklist of deliverables ([ ] for incomplete)
- **Technical Notes**: Implementation specifics and design considerations

## Related Documentation

- [Scribe](scribe.md) - Note creation utility
- [Update Board](update_board.md) - Complementary board management script
- [Sprint_05_The_Ion_Bridge](../../../90 - Project Management/Sprints/Sprint_05_The_Ion_Bridge.md) - Ion Bridge sprint details
- [PRD-007 Sovereign Split-Brain Orchestration](../../../90 - Project Management/Requirements/PRD-007%20Sovereign%20Split-Brain%20Orchestration.md) - Multi-platform architecture requirements

## Maintenance Notes

This script should be run:
- When new Phase 4 or Phase 5 tasks are identified
- During sprint planning for Ion HUD development
- When onboarding new team members to the project structure

The task definitions are hardcoded and should be updated if requirements change.