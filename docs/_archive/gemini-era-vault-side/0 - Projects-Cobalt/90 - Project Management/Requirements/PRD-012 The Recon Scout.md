---
title: "PRD-012: The Recon Scout and Vision Gateway"
status: Draft
priority: P0
module: [Requirements]
phase: 2
complexity: L
tags: [cobalt, prd, requirements, recon-scout]
created: 2026-03-17
---

# PRD-012: The Recon Scout and Vision Gateway

## 1. Executive Summary
**The Vision:** Build an autonomous reconnaissance system that gathers market intelligence from multiple financial data sources using browser automation and intelligent extraction.
**The Problem:** Traders must manually visit multiple websites (SMB Trading, Finviz, FinancialJuice) to gather market data, news, and chart information. This process is time-consuming and error-prone.
**The Solution:** A "Recon Scout" agent that automates data collection from financial websites using Playwright's AOM (Accessibility Object Model) extractor, with intelligent caching via pgvector Fast Path to minimize LLM inference costs.

## 2. Core Philosophy: The Recon Scout Architecture

### 2.1 Playwright AOM Extractor
The system uses Playwright's Accessibility Object Model (AOM) extractor to reliably parse financial websites:

* **DOM-Agnostic Extraction:** AOM provides a semantic representation of web elements, making extraction resilient to CSS class changes and layout updates.
* **Structured Data Capture:** Extracts tables, charts, news feeds, and price data with semantic context.
* **Headless Execution:** All browsing occurs in headless mode via Playwright for efficiency.

### 2.2 Dynamic Vault Credential Resolution
The system uses domain-namespaced credential resolution from the secure vault:

* **Namespace Format:** `domain::username` (e.g., `rt.smbtraining.com::cobalt`, `finviz.com::recon`)
* **Automatic Resolution:** The Vault service resolves credentials dynamically based on the target domain.
* **Zero Trust:** Credentials are never hardcoded; they are fetched at runtime with proper access control.

### 2.3 pgvector Fast Path Cache
Repeated reconnaissance queries are cached to bypass LLM inference:

* **Cache Key:** Hash of the query parameters (domain, date range, data type).
* **Cache Hit:** Returns cached results without LLM inference when data hasn't changed.
* **Cache Miss:** Performs full extraction and stores results in pgvector for future lookups.

## 3. User Stories

### Story A: SMB Game Plan Extraction
**As a** Trader,
**I want** the Recon Scout to automatically extract my daily game plan from SMB Trading's member portal,
**So that** I can review the day's setups without manually logging in.

* **Target Domain:** `rt.smbtraining.com`
* **Credential Namespace:** `rt.smbtraining.com::cobalt`
* **Data Extracted:** Daily watchlist, setup criteria, key levels, market bias

### Story B: Finviz Chart Download
**As a** Trader,
**I want** the Recon Scout to download technical charts from Finviz for my watchlist stocks,
**So that** I have historical context and pattern recognition data.

* **Target Domain:** `finviz.com`
* **Credential Namespace:** `finviz.com::recon` (if authentication required)
* **Data Extracted:** Chart images, technical indicators, heatmaps, screener results

### Story C: FinancialJuice News Interception
**As a** Trader,
**I want** the Recon Scout to intercept real-time news from FinancialJuice,
**So that** I can react to breaking market events immediately.

* **Target Domain:** `financialjuice.com`
* **Credential Namespace:** `financialjuice.com::recon`
* **Data Extracted:** News headlines, timestamps, tickers, sentiment indicators

## 4. Functional Requirements

### 4.1 The AOM Extractor Interface
```python
class AOMExtractor:
    async def extract(self, url: str, domain: str) -> dict:
        """Extract structured data using AOM."""
    
    async def login(self, domain: str) -> None:
        """Authenticate using vault credentials."""
    
    async def scrape_table(self, table_selector: str) -> list[dict]:
        """Extract tabular data via AOM."""
    
    async def capture_chart(self, chart_selector: str) -> bytes:
        """Capture chart image via AOM."""
```

### 4.2 Vault Credential Resolution
The vault service must resolve credentials dynamically:

* **Input:** Domain namespace (e.g., `rt.smbtraining.com`)
* **Output:** Credential object with username, password, and any 2FA tokens.
* **Security:** Credentials are encrypted at rest and in transit.

### 4.3 pgvector Fast Path Cache
The cache layer must implement:

* **Cache Key Generation:** SHA-256 hash of `(domain, query_params, timestamp)`.
* **Cache Validation:** Check if cached data is still fresh (configurable TTL).
* **Cache Invalidation:** Automatic invalidation when source data changes.

### 4.4 Recon Scout Orchestrator
The orchestrator coordinates multiple reconnaissance tasks:

* **Task Queue:** FIFO queue for scheduled recon jobs.
* **Rate Limiting:** Respect website rate limits and terms of service.
* **Error Handling:** Retry logic with exponential backoff.

## 5. Technical Constraints

* **Browser Automation:** Playwright with Chromium headless.
* **AOM Access:** Use Playwright's accessibility tree for element extraction.
* **Vault Integration:** Zero Trust vault service with domain-namespaced credentials.
* **Database:** PostgreSQL with pgvector extension for caching.
* **LLM Integration:** Bypass inference on cache hits; use Qwen 3.5 122B for novel queries.
* **Execution Mode:** Headless, non-interactive browser sessions.

## 6. Data Sources Configuration

### 6.1 SMB Trading (rt.smbtraining.com)
| Field | Value |
|-------|-------|
| Credential Namespace | `rt.smbtraining.com::cobalt` |
| Data Type | Daily game plan, watchlist |
| Update Frequency | Once per trading day |

### 6.2 Finviz (finviz.com)
| Field | Value |
|-------|-------|
| Credential Namespace | `finviz.com::recon` (optional) |
| Data Type | Charts, heatmaps, screener results |
| Update Frequency | On-demand or scheduled |

### 6.3 FinancialJuice (financialjuice.com)
| Field | Value |
|-------|-------|
| Credential Namespace | `financialjuice.com::recon` |
| Data Type | Real-time news, economic calendar |
| Update Frequency | Continuous during market hours |

## 7. Future Extensibility

* **Additional Sources:** Add support for more financial websites (TradingView, Benzinga, etc.).
* **Sentiment Analysis:** Use LLM to analyze news sentiment and update scores.
* **Alert System:** Push notifications for breaking news or significant market events.<task_progress>
- [x] Read and audit PRD-001 (identify Rust/Split-Brain references)
- [x] Update PRD-001 to Unified MoE Architecture (Python/PyQt6)
- [x] Generate PRD-012 (Recon Scout and Vision Gateway)
- [ ] Task Board Alignment - Delete obsolete tasks
- [ ] Task Board Alignment - Create new formatted Markdown tasks
</task_progress>
</write_to_file>