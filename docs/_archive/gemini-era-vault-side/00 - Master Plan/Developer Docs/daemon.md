---
title: "Watcher Daemon Documentation"
status: Active
module: Tool
type: Class
dependencies:
  - "[[extractor]]"
  - "[[postgres]]"
  - "[[browser]]"
  - "[[mattermost]]"
location: "src/cobalt_agent/tools/daemon.py"
tags: [cobalt, dev_docs, apscheduler, watcher, daemon]
created: 2026-02-28
updated: 2026-02-28
---

# Watcher Daemon Module

**Location:** `src/cobalt_agent/tools/daemon.py`

## Overview

The Watcher Daemon is a scheduled web monitoring system that uses APScheduler to run recurring background jobs. Each watcher job fetches a URL, extracts graph entities via the Universal Extractor, computes deltas against existing graph state, and sends Mattermost alerts only when new entities are detected.

### Key Features
- **APScheduler Integration** - Background job scheduling with configurable intervals
- **ReAct Tool Actions** - `schedule_watcher`, `list_watchers`, `stop_watcher` for LLM control
- **Delta Engine** - Silent operation: alerts only trigger when new edges are detected
- **Mattermost Integration** - High-priority alerts for new entity discoveries

---

## Pydantic Input Schemas

### `ScheduleWatcherInput`

| Field | Type | Constraints | Description |
|--|--|--|--|
| `url` | str | Required | The URL to monitor |
| `interval_minutes` | int | `ge=1` | Interval between checks (minimum 1 minute) |
| `intent` | str | Required | The purpose/description of this watcher |

**Example:**
```json
{
  "url": "https://finance.yahoo.com/quote/TSLA",
  "interval_minutes": 5,
  "intent": "Monitor TSLA price movements and new strategy triggers"
}
```

---

### `ListWatchersInput`

Empty input schema - no parameters needed.

---

### `StopWatcherInput`

| Field | Type | Description |
|--|--|--|
| `job_id` | str | The ID of the job to stop |

---

## Class: `DaemonTool`

DaemonTool for managing scheduled web watchers.

### Constructor

```python
DaemonTool()
```

Initializes:
- `BackgroundScheduler` from APScheduler
- `PostgresMemory` for delta computation
- `BrowserTool` for URL fetching
- `UniversalExtractor` for entity extraction
- `_registered_jobs: Dict[str, Dict]` - Internal job metadata storage

---

### Methods

#### `start() -> None`

Start the background scheduler.

**Usage:**
```python
daemon = DaemonTool()
daemon.start()  # Scheduler begins running scheduled jobs
```

---

#### `stop() -> None`

Stop the background scheduler gracefully.

**Usage:**
```python
daemon.stop()  # Scheduler stops, pending jobs completed
```

---

#### `schedule_watcher(url: str, interval_minutes: int, intent: str) -> str`

Schedule a new watcher job to run at the specified interval.

**Parameters:**
- `url`: The URL to monitor
- `interval_minutes`: How often to check the URL (in minutes)
- `intent`: The purpose/description of this watcher

**Returns:** Job ID for the newly scheduled job (format: `watcher_<hex8>`)

**Workflow:**
1. Generate unique job ID using `uuid.uuid4().hex[:8]`
2. Store metadata in `_registered_jobs` dict
3. Schedule with APScheduler: `scheduler.add_job(..., 'interval', minutes=..., id=job_id)`

**Example:**
```python
job_id = daemon.schedule_watcher(
    url="https://finance.yahoo.com/quote/TSLA",
    interval_minutes=5,
    intent="Monitor TSLA price movements"
)
# Returns: "watcher_a1b2c3d4"
```

---

#### `list_watchers() -> List[Dict]`

List all active background jobs.

**Returns:** List of dictionaries containing job information:

| Key | Description |
|--|--|
| `job_id` | Unique job identifier |
| `next_run_time` | When the job will next execute |
| `trigger` | APScheduler trigger type (e.g., `IntervalTrigger`) |
| `is_running` | Whether the job is active |
| `url` | Monitored URL (if registered) |
| `interval_minutes` | Check interval (if registered) |
| `intent` | Watcher intent (if registered) |

**Example:**
```python
watchers = daemon.list_watchers()
for w in watchers:
    print(f"{w['job_id']}: {w['url']} @ {w['interval_minutes']}min")
```

---

#### `stop_watcher(job_id: str) -> bool`

Cancel an active watcher job.

**Parameters:**
- `job_id`: The ID of the job to stop

**Returns:** True if job was found and stopped, False otherwise

**Workflow:**
1. Remove job from APScheduler: `scheduler.remove_job(job_id)`
2. Delete from `_registered_jobs` dict
3. Return success status

---

## Background Job Execution

### `_run_watcher_job(url: str, intent: str, postgres_memory) -> None`

Background job function executed by APScheduler on the configured interval.

**Parameters:**
- `url`: The URL to monitor
- `intent`: The watcher intent/description
- `postgres_memory`: Optional PostgresMemory for delta computation

**Workflow:**
```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                        Watcher Job Execution Flow                              │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 1. Log job start: Check {url} (intent: {intent})                              │
│ 2. Fetch content: BrowserTool().run(query=url)                                │
│ 3. Extract entities: UniversalExtractor().extract(content)                    │
│ 4. Compute delta: compute_delta(extracted_nodes, extracted_edges)             │
│ 5. Evaluate delta:                                                            │
│    - new_edges = [] AND new_nodes = [] → SILENT (return)                     │
│    - new_edges ≠ [] OR new_nodes ≠ [] → _send_watcher_alert()                │
└──────────────────────────────────────────────────────────────────────────────────┘
```

**Error Handling:**
- Logs error and returns on BrowserTool failure
- Uses `logger.exception()` for full traceback capture

---

### `_send_watcher_alert(url: str, intent: str, delta_payload: Dict) -> None`

Send a high-priority Mattermost alert for watcher detection.

**Parameters:**
- `url`: The URL where new entities were detected
- `intent`: The watcher intent
- `delta_payload`: The delta result containing new nodes and edges

**Alert Message Format:**
```
🚨 **Watcher Alert** [https://example.com]

New entities detected based on intent 'Monitor price movements'.

### New Edges Detected:
- **TSLA** ──[TRIGGERED_STRATEGY]──> **Morning Gapper**
- **95.0** ──[HAS_CONFIDENCE]──> **Morning Gapper**

### New Nodes Detected:
- `Ticker`: **TSLA**
- `Strategy`: **Morning Gapper**

---
*This is an automated alert from the Watcher Daemon.*
```

**Delivery:**
1. Connect to Mattermost via `MattermostInterface()`
2. Send to `town-square` channel, `approval_team` user
3. Disconnect after send

**Silent Operation Logic:**
- If delta has no new edges AND no new nodes → no alert is sent
- This prevents notification fatigue when monitoring stable URLs

---

## APScheduler Integration

### Configuration

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(
    _run_watcher_job,
    'interval',
    minutes=5,
    id="watcher_a1b2c3d4",
    replace_existing=True,
    args=[url, intent, postgres_memory]
)
```

### Job Trigger Types

| Type | Description |
|--|--|
| `interval` | Run at fixed time intervals (used by watchers) |
| `cron` | Run at specific times (not currently used) |
| `date` | Run once at a specific time (not currently used) |

---

## ReAct Tool Integration

### LLM Actions

The DaemonTool exposes three Pydantic-validated actions for LLM control:

#### 1. `schedule_watcher`

```python
{
  "tool": "daemon",
  "action": "schedule_watcher",
  "url": "https://finance.yahoo.com/quote/TSLA",
  "interval_minutes": 5,
  "intent": "Monitor TSLA price movements and new strategy triggers"
}
```

#### 2. `list_watchers`

```python
{
  "tool": "daemon",
  "action": "list_watchers"
}
```

#### 3. `stop_watcher`

```python
{
  "tool": "daemon",
  "action": "stop_watcher",
  "job_id": "watcher_a1b2c3d4"
}
```

### Integration with ToolManager

```python
from cobalt_agent.tools.tool_manager import ToolManager

tool_manager = ToolManager()
tool_manager.register_tool("daemon", DaemonTool())

# LLM can now call daemon actions via tool invocations
tool_manager.run("daemon", "schedule_watcher", url="...", interval_minutes=5, intent="...")
```

---

## Delta Engine Integration

### Silent Operation Flow

```python
delta_payload = compute_delta(extracted_nodes, extracted_edges, postgres_memory)

# Check for new entities
if not delta_payload.get("new_edges") and not delta_payload.get("new_nodes"):
    # Silent operation - no new information
    logger.info(f"No new entities detected at {url}")
    return

# New entities detected - trigger Mattermost alert
_send_watcher_alert(url, intent, delta_payload)
```

### Alert Trigger Conditions

| Condition | Action |
|--|--|
| `new_edges = []` AND `new_nodes = []` | No alert (silent) |
| `new_edges ≠ []` OR `new_nodes ≠ []` | Send Mattermost alert |

---

## Usage Examples

### Basic Watcher Setup

```python
from cobalt_agent.tools.daemon import DaemonTool

# Initialize daemon
daemon = DaemonTool()
daemon.start()

# Schedule a watcher
job_id = daemon.schedule_watcher(
    url="https://finance.yahoo.com/quote/TSLA",
    interval_minutes=5,
    intent="Monitor TSLA price movements"
)

print(f"Watcher scheduled with ID: {job_id}")

# List active watchers
watchers = daemon.list_watchers()
for w in watchers:
    print(f"Job: {w['job_id']}, Next: {w['next_run_time']}")
```

### Stopping a Watcher

```python
# Stop a specific watcher
daemon.stop_watcher(job_id="watcher_a1b2c3d4")

# Stop all watchers
watchers = daemon.list_watchers()
for w in watchers:
    daemon.stop_watcher(w['job_id'])
```

### Manual Job Execution

```python
from cobalt_agent.tools.daemon import _run_watcher_job
from cobalt_agent.memory.postgres import PostgresMemory

# Run a watcher job manually (for testing)
postgres = PostgresMemory()
_run_watcher_job(
    url="https://finance.yahoo.com/quote/TSLA",
    intent="Test watcher",
    postgres_memory=postgres
)
```

---

## Error Handling

### BrowserTool Failures

```python
if browser_result.error:
    logger.error(f"Watcher Job: Failed to fetch {url}: {browser_result.error}")
    return  # Graceful exit, no alert
```

### PostgresMemory Unavailable

```python
try:
    postgres_memory = PostgresMemory()
except Exception as e:
    logger.warning(f"PostgresMemory initialization skipped: {e}")
    postgres_memory = None
```

### Mattermost Alert Failures

```python
try:
    mm = MattermostInterface()
    mm.send_message(...)
except Exception as e:
    logger.exception(f"Failed to send watcher alert: {e}")
```

---

## Performance

### Timing Metrics

| Operation | Typical Duration |
|--|--|
| Browser fetch (Fast Path) | 5-50ms |
| Browser fetch (Fallback) | 1-5s |
| LLM extraction | 1-3s |
| Delta computation | 500ms-2s |
| Mattermost alert | 500ms-2s |

### Job Interval Recommendations

| Use Case | Recommended Interval |
|--|--|
| Price monitoring | 1-5 minutes |
| News monitoring | 15-30 minutes |
| Social media monitoring | 30-60 minutes |
| Low-priority monitoring | 2-4 hours |

---

## Testing

### Unit Tests

- `tests/test_daemon.py` - Tests watcher scheduling and execution

### Test Scenarios

1. **Schedule Watcher**: Verify job ID generation and storage
2. **List Watchers**: Verify job listing and metadata
3. **Stop Watcher**: Verify job removal and cleanup
4. **Background Execution**: Verify `_run_watcher_job` executes correctly
5. **Delta Silence**: Verify no alert when delta is empty

---

## Configuration

No additional configuration required. Uses global configuration:

```yaml
llm:
  model_name: "gpt-4o-mini"

mattermost:
  webhook_url: "${MATTERMOST_WEBHOOK_URL}"
  approval_team: "engineering"
```

---

## Related Modules

- **APScheduler** (`apscheduler.schedulers.background`) - Background job scheduling
- **UniversalExtractor** (`src/cobalt_agent/tools/extractor.py`) - Entity extraction
- **PostgresMemory** (`src/cobalt_agent/memory/postgres.py`) - Delta computation
- **BrowserTool** (`src/cobalt_agent/tools/browser.py`) - URL content fetching
- **MattermostInterface** (`src/cobalt_agent/interfaces/mattermost.py`) - Alert delivery

---

## Migration Notes

### Previous Implementation

- Manual cron job management
- No LLM control over watchers
- No delta engine (alert on every run)

### New Implementation

- APScheduler for robust scheduling
- LLM ReAct tools for dynamic watcher management
- Delta engine for silent operation (only alert on changes)

---

## Future Enhancements

1. **Dynamic Rescheduling**: Adjust interval based on entity change frequency
2. **Alert Deduplication**: Group alerts by entity type
3. **Job Priority**: Support priority-based scheduling
4. **Persistence**: Store watcher config in database for recovery