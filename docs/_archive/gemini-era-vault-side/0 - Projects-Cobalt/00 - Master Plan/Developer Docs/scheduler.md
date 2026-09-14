# Scheduler Service

## Overview
`cobalt_agent/services/scheduler.py`

The `SchedulerService` class is the Cron-Based Automation Engine. It manages scheduled tasks like daily Morning Briefings and automated vault maintenance.

## Class: SchedulerService

### Description
Cron-Based Automation Engine. Manages scheduled tasks like daily Morning Briefings and automated vault maintenance.

### Constructor
```python
def __init__(self)
```

Initializes the scheduler and loads configured cron jobs from the configuration file.

### Methods

#### start
```python
def start()
```

Start the scheduler in a background thread. Loads cron jobs from `configs/config.yaml`.

#### stop
```python
def stop()
```

Gracefully stop the scheduler and cancel all pending jobs.

#### add_cron_job
```python
def add_cron_job(self, job_name: str, schedule: str, func: callable, *args, **kwargs)
```

Add a new cron job to the scheduler.

**Parameters:**
- `job_name` (str): Unique identifier for the job
- `schedule` (str): Cron expression (e.g., "0 9 * * *" for 9 AM daily)
- `func` (callable): Function to execute when scheduled
- `*args`: Positional arguments for the function
- `**kwargs`: Keyword arguments for the function

#### add_interval_job
```python
def add_interval_job(self, job_name: str, seconds: int, func: callable, *args, **kwargs)
```

Add a job that runs at interval intervals.

**Parameters:**
- `job_name` (str): Unique identifier for the job
- `seconds` (int): Interval in seconds
- `func` (callable): Function to execute
- `*args`: Positional arguments for the function
- `**kwargs`: Keyword arguments for the function

### Built-in Jobs

#### Morning Briefing Generation
- **Schedule:** Daily at 9:00 AM
- **Function:** `MorningBriefing().run()`
- **Output:** Markdown report saved to Obsidian vault in `0 - Inbox` folder
- **Content:** Market data, news headlines, strategic thoughts

#### Vault Management
- **Schedule:** Daily at midnight
- **Function:** AES-256 encrypted backup of Vault contents
- **Purpose:** Ensure local vault integrity and backup

#### Daily Log Cleanup
- **Schedule:** Weekly on Sunday at 11:59 PM
- **Function:** Archive and compress old daily logs
- **Purpose:** Maintain vault performance

### Configuration
Jobs are defined in `configs/config.yaml` under the `scheduler` section:
```yaml
scheduler:
  jobs:
    - name: "Morning Briefing"
      type: "cron"
      schedule: "0 9 * * *"
      task: "briefing"
    - name: "Vault Backup"
      type: "interval"
      seconds: 86400
      task: "vault_backup"
```

### Thread Management
- Scheduler runs in a background daemon thread
- Graceful shutdown ensures all jobs complete before stopping
- Thread-safe job queue for concurrent job handling

## Key Components
- `APScheduler`: Scheduler engine
- `MorningBriefing`: Briefing generation skill
- `Scribe`: Obsidian integration
- `Config`: Configuration management

## See Also
- `MorningBriefing` - Daily briefing generation skill
- `Scribe` - Obsidian integration skill