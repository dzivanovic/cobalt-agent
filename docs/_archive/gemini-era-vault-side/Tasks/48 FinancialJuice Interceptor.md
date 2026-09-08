---
status: To Do
priority: P0 (Critical)
module: Recon Scout
phase: 2 (Vision Gateway)
complexity: L
tags: [cobalt, task, recon-scout, financialjuice, news]
created: 2026-03-17
---

# 48 FinancialJuice Interceptor

## Objective
Build the FinancialJuice news interceptor using Playwright AOM to automatically capture real-time market news and economic calendar events.

## Requirements
* [ ] Implement `FinancialJuiceExtractor` class extending the base AOM Extractor.
* [ ] Configure vault credential resolution for `financialjuice.com::recon`.
* [ ] Implement headless login flow using Playwright.
* [ ] Extract real-time news feed:
  * News headlines with timestamps
  * Associated tickers/symbols
  * Sentiment indicators (Bullish/Bearish/Neutral)
* [ ] Extract economic calendar events:
  * Event names (CPI, FOMC, Jobs Report)
  * Scheduled times
  * Expected vs. actual values
* [ ] Store extracted data in pgvector with domain-specific namespace.
* [ ] Implement cache validation to bypass LLM inference on repeated runs.

## Technical Specifications

### Vault Credential Resolution
```python
# Credential namespace format
CREDENTIAL_NAMESPACE = "financialjuice.com::recon"

# Vault lookup
credentials = vault.resolve(CREDENTIAL_NAMESPACE)
```

### AOM Extraction Pattern
```python
async def intercept_news(self) -> dict:
    """Intercept real-time news using AOM."""
    
    await self.page.goto("https://financialjuice.com/free-forex-news")
    
    # Use AOM for semantic extraction
    accessibility_tree = await self.page.accessibility.snapshot()
    
    # Extract news feed from AOM
    news_items = await self.extract_news_feed(".news-item")
    
    # Extract economic calendar from AOM
    events = await self.extract_calendar(".economic-calendar")
    
    return {
        "news": news_items,  # List of news items with sentiment
        "calendar": events,  # Economic calendar events
        "timestamp": datetime.now().isoformat()
    }

async def extract_news_feed(self, selector: str) -> list[dict]:
    """Extract news items using AOM."""
    
    # Get accessibility tree for semantic extraction
    snapshot = await self.page.accessibility.snapshot()
    
    news_items = []
    for node in snapshot["children"]:
        if selector in str(node.get("role", "")):
            news_items.append({
                "headline": node.get("name", ""),
                "timestamp": node.get("value", {}).get("datetime"),
                "tickers": self.extract_tickers(node),
                "sentiment": self.classify_sentiment(node)
            })
    
    return news_items
```

### pgvector Fast Path Cache
* **Cache Key:** `financialjuice:news:{date}`
* **TTL:** 15 minutes (news updates frequently during market hours)
* **Invalidation:** Automatic on new article detection

## Acceptance Criteria
- [ ] Extractor successfully logs in using vault credentials.
- [ ] Real-time news feed is captured and stored in structured format.
- [ ] Economic calendar events are extracted with proper timestamps.
- [ ] Cache hit returns cached data without LLM inference.
- [ ] Cache miss performs full extraction and updates pgvector.

## Dependencies
* Task 39: Tool Playwright Browser (must be complete)
* PRD-012: The Recon Scout and Vision Gateway

## Related Files
* `src/cobalt_agent/tools/extractor.py` - Base extractor class
* `src/cobalt_agent/security/vault.py` - Credential resolution
* `src/cobalt_agent/memory/postgres.py` - pgvector storage