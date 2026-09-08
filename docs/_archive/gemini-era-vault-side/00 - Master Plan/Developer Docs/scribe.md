# Scribe Skill (Obsidian Integration)

## Overview
`cobalt_agent/skills/productivity/scribe.py`

The `Scribe` class is the Obsidian Vault Interface. It allows the agent to read, write, and search documents in the "Second Brain" vault.

## Class: Scribe

### Description
Interface for interacting with an Obsidian Vault. Allows reading, writing, and searching documents.

### Constructor
```python
def __init__(self, vault_path: Optional[str] = None)
```

**Parameters:**
- `vault_path` (Optional[str]): Path to Obsidian vault. Defaults to `OBSIDIAN_VAULT_PATH` env var.

**Fallback:** If environment variable not set, defaults to `~/Documents/Think`

### File Paths
All file paths are relative to the vault root. Examples:
- `0 - Inbox/note.md`
- `Projects/Task-001.md`
- `Archive/2026/January.md`

### Methods

#### write_note
```python
def write_note(self, filename: str, content: str, folder: str = "0 - Inbox") -> str
```

Create or overwrite a note in the vault.

**Parameters:**
- `filename` (str): Note filename (auto-adds `.md` if missing)
- `content` (str): Markdown content to write
- `folder` (str): Target folder within vault (default: "0 - Inbox")

**Returns:** Success message with path

**STRICT RULE:** All automated writes go to `0 - Inbox` unless explicitly overridden.

#### read_note
```python
def read_note(self, filename: str) -> str
```

Read the content of a specific note.

**Parameters:**
- `filename` (str): Note filename to read

**Returns:** File contents or error message

**Search Behavior:** Recursively searches vault if file not found in root.

#### append_to_daily_note
```python
def append_to_daily_note(self, content: str) -> str
````

Append text to today's Daily Log.

**Parameters:**
- `content` (str): Text to append

**Returns:** Path to the daily log file

**Behavior:**
- Creates file if it doesn't exist
- Adds timestamp header before content
- Uses folder: `0 - Inbox`

#### search_vault
```python
def search_vault(self, query: str, limit: int = 5) -> List[str]
```

Search for notes containing a keyword.

**Parameters:**
- `query` (str): Search term
- `limit` (int): Maximum results (default: 5)

**Returns:** List of matching filenames

**Behavior:**
- Case-insensitive substring search
- Ignores hidden files/folders (starting with `.`)
- Returns first `limit` matches

## File Path Resolution

### _resolve_path
```python
def _resolve_path(self, filename: str) -> Path
```

Helper method to ensure files have `.md` extension and are inside the vault.

## Error Handling
- Returns error strings (prefixed with `❌`) for failures
- Logs warnings to `loguru` logger
- Gracefully handles missing vault directory

## Integration Points
- Used by `MorningBriefing` for report delivery
- Used by `DeepResearch` for final report storage
- Used by `OpsDepartment` for file modifications

## See Also
- `MorningBriefing` - Briefing generation skill
- `DeepResearch` - Research report generation
- `OpsDepartment` - Documentation-focused drone