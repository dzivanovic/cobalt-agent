---
title: "Live Run Orchestrator"
status: Active
module: Utility
type: Integration Test
dependencies: [scanner_orchestrator, semantic_tagger, finviz_api]
location: "dev_utils/live_run_orchestrator.py"
tags: [orchestration, pipeline, stress-test, finviz]
created: 2026-04-07
---

# Live Run Orchestrator - Finviz Data Pipeline Stress Test

**Location:** `dev_utils/live_run_orchestrator.py`

## Overview

A comprehensive stress test script that executes the full Finviz data pipeline to verify system stability under concurrent load. This script tests both the ingestion and semantic tagging workflows in a single run.

## Purpose

This script serves as:
- **Pipeline Validation**: Tests end-to-end data flow from API fetch to semantic tagging
- **Stress Testing**: Verifies local LLM stability under concurrent database operations
- **Integration Verification**: Validates all components work together correctly

## Prerequisites

### Dependencies

```bash
uv sync  # Ensures psycopg2, httpx, and other dependencies are installed
```

### Configuration Requirements

| Component | Source | Required Values |
|-----------|--------|-----------------|
| PostgreSQL | `config.postgres` | host, user, db, port, password |
| Vault | `data/.cobalt_vault` | Finviz API token stored |
| LLM | Local (LM Studio) | Running on configured endpoint |

### Environment Variables (Optional)

| Variable | Purpose |
|----------|---------|
| `COBALT_MASTER_KEY` | Vault decryption key for API token resolution |

## Usage

### Basic Execution

```bash
# Run full pipeline stress test
uv run dev_utils/live_run_orchestrator.py
```

## Execution Flow

The script performs **6 sequential steps**:

### Step 1: Establish PostgreSQL Connection

```python
def get_db_connection():
    config = get_config()
    db_config = config.postgres
    
    return psycopg2.connect(
        host=db_config.host,
        port=db_config.port,
        database=db_config.db,
        user=db_config.user,
        password=db_config.password,
    )
```

**Validation**: Checks that `host`, `user`, and `db` are configured before connecting.

### Step 2: Initialize Local LLM

```python
llm = LLM(role="coder")
```

The `role="coder"` configuration optimizes the model for code/data transformation tasks.

### Step 3: Initialize Finviz API Client with Vault Integration

```python
vault_manager = VaultManager(vault_path="data/.cobalt_vault")

# Auto-unlock if master key available
if not vault_manager._is_unlocked:
    master_key = config.system.debug_mode and getattr(config.vault, "master_key", None)
    if not master_key:
        master_key = os.getenv("COBALT_MASTER_KEY")
    
    if master_key:
        vault_manager.unlock(master_key)

finviz_client = FinvizApiClient(vault_path="data/.cobalt_vault")
```

**Vault Resolution Flow**:
1. Check if vault is already unlocked
2. Try `config.system.debug_mode + config.vault.master_key`
3. Fallback to `COBALT_MASTER_KEY` environment variable
4. Unlock vault for API token resolution

### Step 4: Run Scanner Ingestion Cycle

```python
scanner_orchestrator = ScannerOrchestrator(
    db_connection=conn,
    client=finviz_client,
)

await scanner_orchestrator.run_ingestion_cycle()
```

**What This Does**:
- Fetches fresh market data from Finviz API
- Processes and stores raw screener results
- Updates database with new market records

### Step 5: Initialize Semantic Tagger

```python
semantic_tagger = SemanticTagger(db_connection=conn, llm=llm)
```

The `SemanticTagger` uses the initialized LLM to perform semantic analysis on database records.

### Step 6: Run Tagging Cycle (Batch Processing)

```python
await semantic_tagger.run_tagging_cycle(batch_size=100)
```

**Batch Configuration**:
- Processes up to 100 records per batch
- Applies semantic tags using LLM-powered analysis
- Handles backlog of untagged market data

### Step 7: Commit and Cleanup

```python
conn.commit()
conn.close()
```

## Output Reference

### Expected Console Output

```
======================================================================
COBALT FINVIZ DATA PIPELINE - STRESS TEST
======================================================================
2026-04-07 09:00:00 | INFO | [STEP 1] Connecting to PostgreSQL...
2026-04-07 09:00:01 | INFO | ✓ Database connection established
2026-04-07 09:00:01 | INFO | [STEP 2] Initializing local LLM (role='coder')...
2026-04-07 09:00:02 | INFO | ✓ LLM initialized with model: llama-3.1
2026-04-07 09:00:02 | INFO | [STEP 3] Initializing Finviz API Client...
2026-04-07 09:00:02 | INFO | 🔑 Unlocking vault for Finviz API token resolution
2026-04-07 09:00:02 | INFO | ✓ Finviz API Client initialized
2026-04-07 09:00:02 | INFO | [STEP 4] Initializing ScannerOrchestrator...
2026-04-07 09:00:02 | INFO | 🔄 Running ingestion cycle to fetch fresh market data...
[Ingestion logs...]
2026-04-07 09:00:15 | INFO | ✓ Ingestion cycle completed
2026-04-07 09:00:15 | INFO | [STEP 5] Initializing SemanticTagger...
2026-04-07 09:00:15 | INFO | ✓ SemanticTagger initialized
2026-04-07 09:00:15 | INFO | [STEP 6] Running tagging cycle (batch_size=100)...
[Tagging logs...]
2026-04-07 09:01:30 | INFO | ✓ Tagging cycle completed
2026-04-07 09:01:30 | INFO | [STEP 7] Committing changes and closing connection...
2026-04-07 09:01:30 | INFO | ✓ Changes committed successfully

======================================================================
PIPELINE STRESS TEST COMPLETED SUCCESSFULLY
======================================================================
2026-04-07 09:01:30 | INFO | ✓ All pipeline stages executed without errors
2026-04-07 09:01:30 | INFO | [CLEANUP] Database connection closed
```

## Error Handling

### Configuration Errors

```python
except ValueError as e:
    logger.error(f"✗ CONFIGURATION ERROR: {e}")
    if conn:
        conn.rollback()
    raise
```

**Triggers When**:
- Missing `host`, `user`, or `db` in postgres config
- Vault path incorrect or inaccessible

### Pipeline Errors

```python
except Exception as e:
    logger.error(f"✗ PIPELINE ERROR: {type(e).__name__}: {e}")
    if conn:
        conn.rollback()
    raise
```

**Triggers When**:
- API request failures
- Database query errors
- LLM communication failures

### Cleanup Guarantee

```python
finally:
    if conn:
        conn.close()
        logger.info("[CLEANUP] Database connection closed")
```

The `finally` block ensures database connections are always closed, even on errors.

## Component Dependencies

| Component | Module | Purpose |
|-----------|--------|---------|
| `ScannerOrchestrator` | `cobalt_agent.skills.research.scanner_orchestrator` | Manages data ingestion from Finviz |
| `SemanticTagger` | `cobalt_agent.skills.research.semantic_tagger` | Applies semantic tags to records |
| `FinvizApiClient` | `cobalt_agent.skills.research.finviz_api` | HTTP client for Finviz API |
| `LLM` | `cobalt_agent.llm` | Local LLM interface for tagging |
| `VaultManager` | `cobalt_agent.security.vault` | Secret management |

## Related Files

- **Source**: `dev_utils/live_run_orchestrator.py`
- **Scanner Orchestrator**: `src/cobalt_agent/skills/research/scanner_orchestrator.py`
- **Semantic Tagger**: `src/cobalt_agent/skills/research/semantic_tagger.py`
- **Finviz API**: `src/cobalt_agent/skills/research/finviz_api.py`
- **Config**: `src/cobalt_agent/config.py`

## See Also

- [Live Finviz API Runner](dev_utils/live_run_finviz.md) - Screener endpoint testing
- [Finviz Quote API Test Runner](dev_utils/live_run_finviz_quote.md) - Single quote endpoint
- [Dynamic Scanner YAML Test Runner](dev_utils/live_run_dynamic_scanners.md) - YAML-based scanner testing