---
status: To Do
priority: P1 (High)
module: Recon Scout
phase: 2 (Vision Gateway)
complexity: M
tags: [cobalt, task, recon-scout, finviz, charts]
created: 2026-03-17
---

# 47 Finviz Chart Downloader

## Objective
Build the Finviz chart downloader using Playwright AOM to automatically retrieve technical charts and screener results for watchlist stocks.

## Requirements
* [ ] Implement `FinvizExtractor` class extending the base AOM Extractor.
* [ ] Configure vault credential resolution for `finviz.com::recon` (if authentication required).
* [ ] Implement headless browsing flow using Playwright.
* [ ] Extract chart images for watchlist tickers:
  * Daily candlestick charts with indicators
  * Intraday charts (1min, 5min) for active stocks
  * Technical indicator overlays (RSI, MACD, Bollinger Bands)
* [ ] Extract screener results and heatmaps.
* [ ] Store extracted data in pgvector with domain-specific namespace.
* [ ] Implement cache validation to bypass LLM inference on repeated runs.

## Technical Specifications

### Vault Credential Resolution
```python
# Credential namespace format (optional for public pages)
CREDENTIAL_NAMESPACE = "finviz.com::recon"

# Vault lookup
credentials = vault.resolve(CREDENTIAL_NAMESPACE) if requires_auth else None
```

### AOM Extraction Pattern
```python
async def download_charts(self, tickers: list[str]) -> dict:
    """Download charts for watchlist using AOM."""
    
    results = {}
    for ticker in tickers:
        url = f"https://finviz.com/chart.ashx?t={ticker}"
        
        await self.page.goto(url)
        
        # Use AOM for semantic extraction
        accessibility_tree = await self.page.accessibility.snapshot()
        
        # Capture chart image via AOM canvas extraction
        chart_image = await self.capture_chart(".chart-canvas")
        
        # Extract technical indicators from AOM labels
        indicators = await self.extract_text_blocks(".indicator-labels")
        
        results[ticker] = {
            "chart": chart_image,  # Base64 encoded image
            "indicators": indicators,
            "timestamp": datetime.now().isoformat()
        }
    
    return results
```

### pgvector Fast Path Cache
* **Cache Key:** `finviz:charts:{ticker}:{date}`
* **TTL:** 4 hours (charts update during market hours)
* **Invalidation:** Automatic on new data detection

## Acceptance Criteria
- [ ] Extractor successfully browses Finviz without authentication (public pages).
- [ ] Chart images are downloaded and stored in structured format.
- [ ] Cache hit returns cached data without LLM inference.
- [ ] Cache miss performs full extraction and updates pgvector.

## Dependencies
* Task 39: Tool Playwright Browser (must be complete)
* PRD-012: The Recon Scout and Vision Gateway

## Related Files
* `src/cobalt_agent/tools/extractor.py` - Base extractor class
* `src/cobalt_agent/security/vault.py` - Credential resolution (optional)
* `src/cobalt_agent/memory/postgres.py` - pgvector storage