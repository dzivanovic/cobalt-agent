# Finviz Extractor

**File:** `src/cobalt_agent/skills/research/finviz_extractor.py`  
**Component:** Finviz Recon Scout - Elite Screener Extraction Skill

---

## Overview

The `FinvizExtractor` class is an autonomous reconnaissance agent that logs into Finviz Elite using Zero-Trust Vault credentials, navigates to custom screener presets, and extracts tabular data across all paginated pages.

### Key Features
- **Vault-based credential resolution** using domain namespace format (`finviz.com::username`)
- **AOM/BrowserTool integration** for Playwright-based browser automation
- **Fast Path cache integration** via pgvector for repeated task caching
- **Robust pagination handling** with dynamic element detection
- **Clean data extraction** with whitespace normalization

---

## Architecture

### Class Structure

```
FinvizExtractor
├── Initialization (vault_path)
├── Credential Resolution (_resolve_vault_credentials)
├── Browser Navigation (_navigate_to_login, _authenticate)
├── Data Extraction (_extract_table_data)
├── Pagination Control (_has_next_page, _go_to_next_page)
├── Multi-page Extraction (_extract_all_pages)
└── Fast Path Caching (_generate_fast_path_cache_entry, extract)
```

---

## Finviz API Connection Utilization

The extractor does not use a REST API; instead, it leverages **Playwright browser automation** to interact with the Finviz Elite web interface:

1. **Credential Resolution**: Extracts domain from URL, queries VaultManager for credentials in `{domain}::{username_type}` format
2. **Direct Navigation**: Uses `_navigate_to_login()` to go directly to `https://finviz.com/login-email?remember=true` (bypasses SSO choice screen)
3. **Authentication**: Fills email/password fields and submits via button click with Enter key fallback
4. **Screener Access**: Navigates directly to preset URLs stored in `PRESET_URLS` dictionary

### PRESET_URLS Mapping
```python
PRESET_URLS: dict[str, str] = {
    "Morning Up Gapper": "https://elite.finviz.com/screener.ashx?v=150&f=sh_avgvol_o2000,..."
}
```

---

## Data Extraction Workflow

### 1. Table Detection (`_extract_table_data`)
The method uses a priority-based selector strategy:

| Priority | Selector | Description |
|----------|----------|-------------|
| 1 | `table.styled-table-new` | New Finviz styling class |
| 2 | `table[bgcolor="#d3d3d3"]` | Gray background table (Elite) |
| 3 | `table:has(th:has-text('Ticker'))` | First table with "Ticker" header |
| 4 | `table` | Any visible table (final fallback) |

### 2. Semantic Column Mapping
- Extracts **ALL** `<th>`/`<td>` text from header row into `raw_headers` (no filtering)
- For data rows: **strict 1-to-1 alignment** - skips if `len(cells) != len(raw_headers)`
- Iterates through headers and cells simultaneously:
  - If header is blank → ignores that cell (spacer column)
  - If header has text → maps `row_dict[header] = cell_text`

### 3. Data Normalization
- Whitespace cleanup: `cleanValue = cellText.replace('\n', ' ').replace('\r', '').strip()`
- Returns `List[Dict[str, Any]]` for dynamic column handling

---

## Pagination Handling

### `_has_next_page()` - Next Button Detection
Priority selector chain:
1. `a.tab-link:has-text("next")` - Tab-style pagination (Elite)
2. `b:has-text("next")` - Bold "next" text
3. `a:has-text("Next")` - Standard Next link
4. `a[href*="r="]:has-text(">")` - Right arrow pagination

### `_go_to_next_page()` - Programmatic Navigation
1. Locates "Next" button and extracts its `href` attribute (does NOT click)
2. Checks if preset URL contains `&c=...` parameter (column configuration)
3. If next URI lacks `&c=`, programmatically appends it to preserve column state
4. Navigates to constructed URL with `wait_until="networkidle"`

---

## Data Fields Extracted

The extractor dynamically captures all visible columns from the screener table. For the "Morning Up Gapper" preset, typical fields include:

| Category | Fields |
|----------|--------|
| **Identity** | Ticker, Company |
| **Volume** | Volume, Avg Vol |
| **Price** | Price, Change, Gap |
| **Technical** | ATR, Signal |
| **Fundamental** | P/E, EPS, Market Cap |
| **Performance** | Performance metrics (Week/Month/Year) |

The exact columns depend on the screener preset configuration stored in `PRESET_URLS`.

---

## Output Format for Downstream Processing

### Return Type
```python
List[Dict[str, Any]]
```

### Example Output Structure
```python
[
    {
        "Ticker": "AAPL",
        "Company": "Apple Inc.",
        "Volume": "125000000",
        "Avg Vol": "85000000",
        "Price": "175.25",
        "Change": "+2.5%",
        # ... additional columns based on preset
    },
    # ... more stock records
]
```

### Downstream Integration
- **Dynamic typing**: No fixed schema - adapts to any preset configuration
- **Semantic mapping**: Column names from HTML headers become dictionary keys
- **Clean values**: Whitespace normalized, newlines replaced with spaces

---

## Fast Path Caching Integration

The `_generate_fast_path_cache_entry()` method creates pgvector cache entries for repeated tasks:

1. Generates `task_hash` from extraction intent
2. Creates `context_signature` from page URL, title, and visible text
3. Captures element tree snapshot via CDP (`DOMSnapshot.captureSnapshot`)
4. Stores Playwright script for replay optimization

### Cache Entry Structure
```python
{
    "task_hash": str,
    "task_intent": str,
    "context_signature": str,
    "element_tree_snapshot": dict,
    "playwright_script": json_str,
    "extraction_metadata": {
        "screener_name": str,
        "page_count": int,
        "total_results": int
    }
}
```

---

## Public API

### `extract(preset_name, domain, fast_path_enabled)`
Main entry point orchestrating the complete workflow:

1. Resolve Vault credentials using domain namespace format
2. Launch Playwright browser and navigate to Finviz login
3. Authenticate with resolved credentials
4. Navigate directly to preset URL (already sorted by Volume DESC)
5. Extract data from all paginated pages with dynamic typing
6. Generate Fast Path cache entry for repeated tasks

**Returns:** `List[Dict[str, Any]]` - All extracted stock data

### `extract_finviz_screener(preset_name, vault_path, domain)`
Convenience function for direct usage:

```python
from src.cobalt_agent.skills.research.finviz_extractor import extract_finviz_screener

results = extract_finviz_screener(
    preset_name="Morning Up Gapper",
    vault_path="data/.cobalt_vault",
    domain="finviz.com"
)
```

---

## Security Considerations

- **NEVER** hardcodes credentials - resolves dynamically from VaultManager
- Uses `urllib.parse` for domain extraction and credential namespace resolution
- Zero Trust architecture with JIT (Just-In-Time) secret retrieval
- Master key fallback via `COBALT_MASTER_KEY` environment variable

---

## Dependencies

| Dependency | Purpose |
|------------|---------|
| `playwright` | Browser automation |
| `loguru` | Structured logging |
| `urllib.parse` | URL/domain parsing |
| `json` | Data serialization |
| `time` | Timing operations |

---

## Related Components

- **Vault Manager**: `src/cobalt_agent/security/vault.py`
- **Postgres Memory**: `src/cobalt_agent/memory/postgres.py`
- **Config System**: `src/cobalt_agent/config.py`