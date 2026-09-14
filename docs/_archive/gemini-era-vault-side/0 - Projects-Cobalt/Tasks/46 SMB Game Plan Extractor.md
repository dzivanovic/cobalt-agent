---
status: To Do
priority: P0 (Critical)
module: Recon Scout
phase: 2 (Vision Gateway)
complexity: L
tags: [cobalt, task, recon-scout, extractor]
created: 2026-03-17
---

# 46 SMB Game Plan Extractor

## Objective
Build the SMB Trading game plan extractor using Playwright AOM to automatically retrieve daily watchlist and setup criteria.

## Requirements
* [ ] Implement `SMBExtractor` class extending the base AOM Extractor.
* [ ] Configure vault credential resolution for `rt.smbtraining.com::cobalt`.
* [ ] Implement headless login flow using Playwright.
* [ ] Extract daily game plan data:
  * Watchlist tickers with RVOL thresholds
  * Setup criteria (Gap & Go, Bella Fade, etc.)
  * Key price levels (support/resistance)
  * Market bias indicators
* [ ] Store extracted data in pgvector with domain-specific namespace.
* [ ] Implement cache validation to bypass LLM inference on repeated runs.

## Technical Specifications

### Vault Credential Resolution
```python
# Credential namespace format
CREDENTIAL_NAMESPACE = "rt.smbtraining.com::cobalt"

# Vault lookup
credentials = vault.resolve(CREDENTIAL_NAMESPACE)
```

### AOM Extraction Pattern
```python
async def extract_game_plan(self) -> dict:
    """Extract SMB daily game plan using AOM."""
    await self.page.goto("https://rt.smbtraining.com/daily-game-plan")
    
    # Use AOM for semantic extraction
    accessibility_tree = await self.page.accessibility.snapshot()
    
    # Extract watchlist table
    watchlist = await self.extract_table(".game-plan-table")
    
    # Extract setup criteria
    setups = await self.extract_text_blocks(".setup-criteria")
    
    return {
        "watchlist": watchlist,
        "setups": setups,
        "timestamp": datetime.now().isoformat()
    }
```

### pgvector Fast Path Cache
* **Cache Key:** `smb:gameplan:{date}`
* **TTL:** 24 hours (reset at market open)
* **Invalidation:** Automatic on new trading day

## Acceptance Criteria
- [ ] Extractor successfully logs in using vault credentials.
- [ ] Game plan data is extracted and stored in structured format.
- [ ] Cache hit returns cached data without LLM inference.
- [ ] Cache miss performs full extraction and updates pgvector.

## Dependencies
* Task 39: Tool Playwright Browser (must be complete)
* PRD-012: The Recon Scout and Vision Gateway

## Related Files
* `src/cobalt_agent/tools/extractor.py` - Base extractor class
* `src/cobalt_agent/security/vault.py` - Credential resolution
* `src/cobalt_agent/memory/postgres.py` - pgvector storage