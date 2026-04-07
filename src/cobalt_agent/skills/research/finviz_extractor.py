"""
Finviz Recon Scout - Elite Screener Extraction Skill

Autonomous reconnaissance agent that logs into Finviz Elite using Zero-Trust Vault
credentials, navigates to custom screener presets, and extracts tabular data across
all paginated pages.

Features:
- Vault-based credential resolution using domain namespace format (finviz.com::username)
- AOM/BrowserTool integration for Playwright-based browser automation
- Fast Path cache integration via pgvector for repeated task caching
- Robust pagination handling with dynamic element detection
- Clean data extraction with whitespace normalization

Security:
- NEVER hardcodes credentials - resolves dynamically from VaultManager
- Uses urllib.parse for domain extraction and credential namespace resolution
- Zero Trust architecture with JIT secret retrieval

Architecture Upgrades:
- Bypass Pydantic for dynamic column handling (custom presets)
- Strict 1-to-1 semantic mapping with spacer column awareness
- Programmatic URL pagination preserving custom columns (&c=...)
"""

import json
import os
import time
from typing import Optional, List, Dict, Any
from urllib.parse import urlparse, parse_qs
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from loguru import logger

from ...config import get_config
from ...security.vault import VaultManager
from ...memory.postgres import PostgresMemory, compute_task_hash, compute_context_signature


class FinvizExtractor:
    """
    Finviz Elite Screener Extraction Agent.
    
    Uses Playwright browser automation with Vault-based credentials to extract
    stock data from Finviz Elite screener presets.
    
    Architecture:
        1. Vault Resolution: Extract domain from URL, query VaultManager for credentials
        2. AOM Navigation: Use Playwright to navigate and authenticate
        3. Screener Selection: Navigate to screener, select preset via dropdown
        4. Data Extraction: Parse table headers and rows with pagination loop
        5. Fast Path Integration: Cache results in pgvector for repeated tasks
    
    Security:
        - Credentials resolved dynamically from Vault using domain namespace format
        - No hardcoded secrets anywhere in the codebase
        - Zero Trust architecture with JIT secret retrieval
    
    Data Handling:
        - Dynamic typing: Returns List[Dict[str, Any]] for custom column presets
        - Semantic mapping: Strict 1-to-1 alignment with spacer column awareness
        - Pagination state: Programmatic URL construction preserves &c=... parameters
    """

    # Finviz Elite domain for credential resolution
    FINVIZ_DOMAIN = "finviz.com"
    
    # Default screener preset name to look for
    DEFAULT_PRESET_NAME = "Morning Up Gapper"

    def __init__(self, vault_path: str = "data/.cobalt_vault"):
        """
        Initialize the FinvizExtractor.
        
        Args:
            vault_path: Path to the encrypted vault file for credential storage
        """
        self.vault_manager = VaultManager(vault_path)
        self._config = get_config()
        self._postgres_memory: Optional[PostgresMemory] = None
        self._current_page = None
        self._browser_context = None
        self._preset_url: Optional[str] = None  # Store preset URL for pagination
        
        # Try to initialize PostgresMemory for Fast Path cache
        try:
            self._postgres_memory = PostgresMemory()
            logger.info("✅ PostgresMemory initialized for Fast Path cache")
        except Exception as e:
            logger.warning(f"⚠️ PostgresMemory initialization skipped: {e}")

    def _resolve_vault_credentials(self, domain: str) -> tuple[Optional[str], Optional[str]]:
        """
        Resolve credentials from Vault using domain namespace format.
        
        Uses urllib.parse to extract the domain and query VaultManager for
        credentials in the format: {domain}::{username_type}
        
        Args:
            domain: The target domain (e.g., 'finviz.com')
            
        Returns:
            Tuple of (username, password) or (None, None) if credentials not found
        """
        # Parse and validate the domain using urllib.parse
        parsed_url = urlparse(f"https://{domain}")
        resolved_domain = parsed_url.netloc or domain
        
        logger.info(f"🔐 Resolving Vault credentials for domain: {resolved_domain}")
        
        # Query VaultManager for credentials using namespace format
        username_key = f"{resolved_domain}::username"
        password_key = f"{resolved_domain}::password"
        
        # Check if vault is unlocked, attempt to unlock with master key if available
        if not self.vault_manager._is_unlocked:
            master_key = self._config.system.debug_mode and hasattr(self._config, 'vault') and getattr(self._config.vault, 'master_key', None)
            if not master_key:
                import os
                master_key = os.getenv("COBALT_MASTER_KEY")
            
            if master_key:
                logger.info(f"🔑 Unlocking vault with COBALT_MASTER_KEY")
                if not self.vault_manager.unlock(master_key):
                    logger.error("Failed to unlock vault - credentials unavailable")
                    return None, None
            else:
                logger.error("Vault is locked and no master key available")
                return None, None
        
        # Retrieve credentials from vault
        username = self.vault_manager.get_secret(username_key)
        password = self.vault_manager.get_secret(password_key)
        
        if username and password:
            logger.info(f"✅ Credentials resolved successfully for {resolved_domain}")
        else:
            missing = []
            if not username:
                missing.append(username_key)
            if not password:
                missing.append(password_key)
            logger.error(f"❌ Missing credentials in vault: {', '.join(missing)}")
        
        return username, password

    def _navigate_to_login(self) -> bool:
        """
        Navigate directly to Finviz login-email endpoint (bypasses SSO choice screen).
        
        Returns:
            True if navigation successful, False otherwise
        """
        self._current_page.goto(
            "https://finviz.com/login-email?remember=true", 
            wait_until="networkidle",
            timeout=30000
        )
        logger.info("✅ Navigated directly to Finviz login-email endpoint")
        return True

    def _authenticate(self, username: str, password: str) -> bool:
        """
        Authenticate using resolved Vault credentials.
        
        Direct form submission to login-email endpoint (bypasses SSO choice screen).
        Clean, linear sequence: fill email -> fill password -> submit.
        
        Args:
            username: Resolved Vault username
            password: Resolved Vault password
            
        Returns:
            True if authentication successful, False otherwise
        """
        # Fill email field with direct AOM locator
        self._current_page.locator('input[name="email"]').fill(username)
        
        # Fill password field with direct AOM locator
        self._current_page.locator('input[name="password"]').fill(password)
        
        # Submit form via button click (with Enter key fallback)
        try:
            self._current_page.locator('button[type="submit"]').click()
        except Exception:
            self._current_page.locator('input[name="password"]').press("Enter")
        
        # Wait for network to idle after form submission
        self._current_page.wait_for_load_state("networkidle")
        
        # Verify authentication succeeded by checking for Screener tab indicator
        try:
            self._current_page.wait_for_selector('a:has-text("Screener")', timeout=5000)
            logger.info("✅ Authentication successful - Screener tab confirmed")
            return True
        except PlaywrightTimeoutError:
            logger.error("❌ Authentication failed - Screener tab not found")
            return False

    # Preset URL mapping dictionary - Direct URL routing for Finviz Elite screener presets
    PRESET_URLS: dict[str, str] = {
        "Morning Up Gapper": "https://elite.finviz.com/screener.ashx?v=150&f=sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,ta_averagetruerange_o0.5,ta_gap_u3&ft=4&o=-volume&ar=10&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66"
    }

    def _extract_table_data(self) -> List[Dict[str, Any]]:
        """
        Extract data from the screener table with dynamic header parsing.
        
        Semantic Column Mapping Strategy:
            1. Extract ALL <th>/<td> text from header row into raw_headers (no filtering)
            2. For data rows: strict 1-to-1 alignment - skip if len(cells) != len(raw_headers)
            3. Iterate through raw_headers and cells simultaneously:
               - If header is blank, ignore that cell (spacer column)
               - If header has text, map cell to header: row_dict[header] = cell_text
        
        Table locator priority:
            1. table.styled-table-new (new Finviz styling)
            2. table[bgcolor="#d3d3d3"] (gray background table)
            3. First table containing "Ticker" in header (most robust fallback)
        
        Returns:
            List of dictionaries with dynamic column names as keys and cell text as values
        """
        extracted_data: List[Dict[str, Any]] = []
        
        try:
            # Take screenshot before attempting extraction for debugging
            os.makedirs("logs", exist_ok=True)
            self._current_page.screenshot(path="logs/debug_table.png")
            
            # Robust table locator with fallback heuristics
            table_selector: Optional[str] = None
            
            # Priority 1: New Finviz styling class
            try:
                if self._current_page.locator('table.styled-table-new').count() > 0:
                    table_selector = 'table.styled-table-new'
            except Exception:
                pass
            
            # Priority 2: Gray background table (common in Elite)
            if not table_selector:
                try:
                    if self._current_page.locator('table[bgcolor="#d3d3d3"]').count() > 0:
                        table_selector = 'table[bgcolor="#d3d3d3"]'
                except Exception:
                    pass
            
            # Priority 3: First table containing "Ticker" in header (most robust)
            if not table_selector:
                try:
                    ticker_table = self._current_page.locator("table").filter(has_text="Ticker")
                    if ticker_table.count() > 0:
                        table_selector = "table:has(th:has-text('Ticker'))"
                except Exception:
                    pass
            
            # Final fallback: any visible table
            if not table_selector:
                try:
                    first_table = self._current_page.locator("table").first
                    if first_table.count() > 0:
                        table_selector = "table"
                except Exception:
                    pass
            
            if not table_selector:
                raise TimeoutError("No table found on page after trying all selectors")
            
            # Wait for the selected table to be available
            self._current_page.wait_for_selector(table_selector, timeout=10000)
            
            # Resilient wait: Allow Finviz's internal JavaScript to populate tbody elements
            self._current_page.wait_for_timeout(2000)
            
            # Step 1: Extract ALL headers from thead (including empty spacer columns)
            raw_headers: List[str] = []
            
            # Try to find header in thead (th elements)
            thead_row = self._current_page.locator(f"{table_selector} thead tr").first
            if thead_row.count() > 0:
                header_cells = thead_row.locator("th")
                header_count = header_cells.count()
                for i in range(header_count):
                    th_cell = header_cells.nth(i)
                    header_text = th_cell.inner_text().strip()
                    raw_headers.append(header_text)  # Keep ALL headers including empty strings
            
            # If no headers found in thead, try first row of tbody with th elements
            if not raw_headers:
                tbody_first_row = self._current_page.locator(f"{table_selector} tbody tr").first
                if tbody_first_row.count() > 0:
                    header_th_cells = tbody_first_row.locator("th")
                    header_count = header_th_cells.count()
                    if header_count > 0:
                        for i in range(header_count):
                            th_cell = header_th_cells.nth(i)
                            header_text = th_cell.inner_text().strip()
                            raw_headers.append(header_text)  # Keep ALL headers including empty strings
            
            # If still no headers, use the first row's td elements as dynamic column names
            if not raw_headers:
                all_rows = self._current_page.locator(f"{table_selector} tr")
                first_row = all_rows.nth(0)
                td_cells = first_row.locator("td")
                header_count = td_cells.count()
                
                if header_count > 0:
                    for i in range(header_count):
                        td_cell = td_cells.nth(i)
                        header_text = td_cell.inner_text().strip()
                        raw_headers.append(header_text)  # Keep ALL headers including empty strings
            
            if not raw_headers:
                logger.warning("⚠️ No headers found in table - returning empty results")
                return []
            
            # Step 2: Extract all data rows with strict semantic mapping
            all_rows = self._current_page.locator(f"{table_selector} tr")
            row_count = all_rows.count()
            
            for i in range(row_count):
                row = all_rows.nth(i)
                
                # Get td cells from this row for data extraction
                try:
                    td_cells = row.locator("td")
                    cell_count = td_cells.count()
                    
                    # Strict length matching: skip if cells don't match raw_headers (spacer awareness)
                    if cell_count != len(raw_headers):
                        continue
                    
                    # Skip empty rows (rows with no text content)
                    row_text = row.inner_text().strip()
                    if not row_text:
                        continue
                    
                    # Semantic mapping: iterate through raw_headers and cells simultaneously
                    row_dict: Dict[str, str] = {}
                    for j in range(cell_count):
                        td_cell = td_cells.nth(j)
                        cell_text = td_cell.inner_text().strip()
                        
                        # Clean up whitespace from cell text
                        clean_value = cell_text.replace('\n', ' ').replace('\r', '').strip()
                        
                        # If header is blank, ignore that cell (spacer column)
                        # If header has text, map to dictionary
                        if j < len(raw_headers):
                            header_name = raw_headers[j].strip()
                            if header_name:  # Non-empty header only
                                row_dict[header_name] = clean_value
                    
                    if row_dict:
                        extracted_data.append(row_dict)
                
                except Exception as row_error:
                    continue
            
            logger.info(f"✅ Extracted {len(extracted_data)} rows with {len([h for h in raw_headers if h])} columns")
            
        except Exception as e:
            logger.error(f"Failed to extract table data: {e}")
        
        return extracted_data

    def _has_next_page(self) -> bool:
        """
        Check if there's a next page available.
        
        Finviz Elite uses various pagination patterns depending on the view mode.
        Priority selectors:
            1. a.tab-link:has-text("next") - Tab-style pagination (Elite)
            2. b:has-text("next") - Bold "next" text (common in Elite)
            3. a:has-text("Next") - Standard Next link
            4. a[href*="r="]:has-text(">") - Right arrow pagination
        
        Returns:
            True if next page button exists and is clickable, False otherwise
        """
        try:
            # Priority 1: Tab-style pagination (Elite version)
            if self._current_page.locator('a.tab-link:has-text("next")').count() > 0:
                return True
            
            # Priority 2: Bold "next" text (common in Elite)
            if self._current_page.locator('b:has-text("next")').count() > 0:
                return True
            
            # Priority 3: Standard Next link (case-insensitive)
            if self._current_page.locator('a:has-text("Next")').count() > 0:
                return True
            
            # Priority 4: Right arrow pagination
            if self._current_page.locator('a[href*="r="]:has-text(">")').count() > 0:
                return True
            
            return False
            
        except Exception:
            return False

    def _go_to_next_page(self) -> bool:
        """
        Navigate to the next page of results with programmatic URL construction.
        
        Pagination State Preservation Strategy:
            1. Locate the "Next" button/arrow element
            2. Extract its href attribute (DO NOT click the element)
            3. Check if preset_url contains &c=... parameter
            4. If next_uri lacks &c=..., programmatically append it
            5. Navigate to constructed URL with wait_until="networkidle"
        
        Returns:
            True if navigation successful, False otherwise
        """
        try:
            # Locate the "Next" button and extract its href (don't click yet)
            next_btn = None
            
            # Priority 1: Tab-style pagination (Elite version)
            try:
                next_btn = self._current_page.locator('a.tab-link:has-text("next")').first
                if next_btn.count() > 0:
                    pass
            except Exception:
                pass
            
            # Priority 2: Bold "next" text (common in Elite)
            if not next_btn:
                try:
                    next_btn = self._current_page.locator('b:has-text("next")').first
                    if next_btn.count() > 0:
                        pass
                except Exception:
                    pass
            
            # Priority 3: Standard Next link (case-insensitive)
            if not next_btn:
                try:
                    next_btn = self._current_page.locator('a:has-text("Next")').first
                    if next_btn.count() > 0:
                        pass
                except Exception:
                    pass
            
            # Priority 4: Right arrow pagination
            if not next_btn:
                try:
                    next_btn = self._current_page.locator('a[href*="r="]:has-text(">")').first
                    if next_btn.count() > 0:
                        pass
                except Exception:
                    pass
            
            if not next_btn or next_btn.count() == 0:
                logger.error("❌ No next button found")
                return False
            
            # Extract href attribute from the Next button (DO NOT click)
            next_uri = next_btn.get_attribute("href")
            
            if not next_uri:
                logger.error("❌ Next button has no href attribute")
                return False
            
            # Check if preset_url contains &c=... parameter and preserve it
            constructed_url = next_uri
            
            if self._preset_url and '&c=' in self._preset_url:
                # Extract the &c=... parameter from preset URL
                parsed_preset = urlparse(self._preset_url)
                preset_params = parse_qs(parsed_preset.query)
                
                if 'c' in preset_params:
                    # Check if next_uri already has &c= parameter
                    parsed_next = urlparse(next_uri)
                    next_params = parse_qs(parsed_next.query)
                    
                    if 'c' not in next_params:
                        # Append &c=... to the constructed URL
                        c_value = preset_params['c'][0]
                        separator = '&' if '?' in next_uri else '?'
                        constructed_url = f"{next_uri}{separator}c={c_value}"
            
            # Navigate to constructed URL with networkidle wait
            self._current_page.goto(constructed_url, wait_until="networkidle", timeout=60000)
            
            # Wait for new table data to load using robust selector
            self._current_page.wait_for_selector('table:has(th:has-text("Ticker"))', timeout=15000)
            self._current_page.wait_for_timeout(1000)  # Brief wait for data rendering
            
            logger.info("✅ Navigated to next page with preserved pagination state")
            return True
            
        except Exception as e:
            logger.error(f"Failed to navigate to next page: {e}")
            return False

    def _extract_all_pages(self, screener_name: str = None) -> tuple[List[Dict[str, Any]], int]:
        """
        Extract data from all paginated pages.
        
        Args:
            screener_name: Name of the screener preset (for tracking)
            
        Returns:
            Tuple of (complete list of stock data from all pages, page count)
        """
        screener_name = screener_name or self.DEFAULT_PRESET_NAME
        all_data: List[Dict[str, Any]] = []
        page_count = 0
        
        logger.info(f"📊 Starting extraction for screener: {screener_name}")
        
        while True:
            page_count += 1
            logger.info(f"📄 Processing page {page_count}...")
            
            # Extract data from current page
            page_data = self._extract_table_data()
            all_data.extend(page_data)
            
            # Check if there's a next page
            if not self._has_next_page():
                logger.info(f"✅ No more pages. Total rows extracted: {len(all_data)}")
                break
            
            # Navigate to next page with preserved pagination state
            if not self._go_to_next_page():
                logger.warning("⚠️ Could not navigate to next page - stopping extraction")
                break
        
        return all_data, page_count

    def _generate_fast_path_cache_entry(
        self, 
        screener_name: str, 
        page_count: int, 
        total_results: int
    ) -> Optional[Dict[str, Any]]:
        """
        Generate a Fast Path cache entry for the extraction task.
        
        Args:
            screener_name: Name of the screener preset used
            page_count: Number of pages scraped
            total_results: Total number of stocks extracted
            
        Returns:
            Cache entry dictionary or None if PostgresMemory unavailable
        """
        if not self._postgres_memory:
            return None
        
        try:
            # Get current page context for signature generation
            url = self._current_page.url if self._current_page else ""
            title = self._current_page.title() if self._current_page else ""
            
            # Generate context signature from page state
            visible_text = self._current_page.locator("body").inner_text()[:1000] if self._current_page else ""
            context_signature = compute_context_signature(url, title, visible_text)
            
            # Generate task hash for the extraction intent
            task_intent = f"Finviz screener: {screener_name}"
            task_hash = compute_task_hash(task_intent)
            
            # Create element tree snapshot from current page
            try:
                cdp_session = self._browser_context.new_cdp_session(self._current_page)
                snapshot_result = cdp_session.send("DOMSnapshot.captureSnapshot", {
                    "computedStyles": [],
                    "includeDOMBindings": True
                })
                
                # Convert snapshot to serializable format
                element_tree_snapshot = {
                    "nodes": snapshot_result.get("nodes", {}),
                    "strings": snapshot_result.get("strings", []),
                    "timestamp": time.time()
                }
            except Exception as snapshot_error:
                logger.warning(f"Failed to capture element tree snapshot: {snapshot_error}")
                element_tree_snapshot = {"error": str(snapshot_error)}
            
            cache_entry = {
                "task_hash": task_hash,
                "task_intent": task_intent,
                "context_signature": context_signature,
                "element_tree_snapshot": element_tree_snapshot,
                "playwright_script": json.dumps({
                    "url": self.PRESET_URLS.get(screener_name, ""),
                    "actions": [
                        {"type": "navigate", "url": self.PRESET_URLS.get(screener_name, "")},
                        {"type": "extract_all_pages"}
                    ]
                }),
                "execution_time_ms": 0,  # Will be updated by browser tool
                "success_rate": 1.0,
                "extraction_metadata": {
                    "screener_name": screener_name,
                    "page_count": page_count,
                    "total_results": total_results
                }
            }
            
            # Write to Fast Path cache
            self._postgres_memory.fast_path_cache.write_back(
                task_hash=task_hash,
                task_intent=task_intent,
                context_signature=context_signature,
                element_tree_snapshot=element_tree_snapshot,
                playwright_script=cache_entry["playwright_script"],
                success_rate=1.0
            )
            
            logger.info(f"✅ Fast Path cache written for task: {task_hash[:8]}...")
            return cache_entry
            
        except Exception as e:
            logger.error(f"Failed to write Fast Path cache entry: {e}")
            return None

    def extract(
        self, 
        preset_name: str = None,
        domain: str = FINVIZ_DOMAIN,
        fast_path_enabled: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Main extraction method - orchestrates the complete workflow.
        
        Workflow:
            1. Resolve Vault credentials using domain namespace format
            2. Launch Playwright browser and navigate to Finviz login
            3. Authenticate with resolved credentials
            4. Navigate directly to preset URL (already sorted by Volume DESC)
            5. Extract data from all paginated pages with dynamic typing
            6. Generate Fast Path cache entry for repeated tasks
        
        Args:
            preset_name: Name of the screener preset to use (default: "Morning Up Gapper")
            domain: Domain for credential resolution (default: finviz.com)
            fast_path_enabled: Whether to enable Fast Path caching
            
        Returns:
            List of dictionaries containing all extracted stock data (dynamic typing)
        """
        preset_name = preset_name or self.DEFAULT_PRESET_NAME
        
        logger.info(f"🚀 Starting Finviz Recon Scout extraction")
        logger.info(f"📋 Target preset: {preset_name}")
        logger.info(f"🌐 Domain: {domain}")
        
        # Step 1: Resolve Vault credentials using urllib.parse domain resolution
        username, password = self._resolve_vault_credentials(domain)
        
        if not username or not password:
            logger.error("Failed to resolve Vault credentials")
            return []
        
        # Step 2: Launch Playwright browser and authenticate
        try:
            with sync_playwright() as p:
                self._browser_context = p.chromium.launch(headless=True)
                context = self._browser_context.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                self._current_page = context.new_page()
                
                # Navigate to login and authenticate
                if not self._navigate_to_login():
                    logger.error("Failed to navigate to login page")
                    return []
                
                if not self._authenticate(username, password):
                    logger.error("Authentication failed")
                    return []
                
                # Step 3: Navigate directly to the preset URL (already sorted by Volume DESC)
                if preset_name not in self.PRESET_URLS:
                    logger.error(f"Preset '{preset_name}' not found in PRESET_URLS mapping")
                    return []
                
                self._preset_url = self.PRESET_URLS[preset_name]  # Store for pagination
                
                logger.info(f"🔗 Navigating directly to preset URL: {self._preset_url}")
                
                self._current_page.goto(
                    self._preset_url,
                    wait_until="networkidle",
                    timeout=60000
                )
                
                logger.info(f"✅ Navigated to preset: {preset_name} (URL routing)")
                
                # Step 4: Extract data from all pages with dynamic typing
                all_data, page_count = self._extract_all_pages(preset_name)
                
                # Step 5: Generate Fast Path cache entry (no Pydantic conversion needed)
                if fast_path_enabled and self._postgres_memory:
                    self._generate_fast_path_cache_entry(preset_name, page_count, len(all_data))
                
                logger.info(f"✅ Extraction complete: {len(all_data)} stocks across {page_count} pages")
                
                return all_data
                
        except PlaywrightTimeoutError as e:
            logger.error(f"Playwright timeout during extraction: {e}")
            return []
        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            return []
        finally:
            # Clean up browser resources
            if self._browser_context:
                try:
                    self._browser_context.close()
                except Exception:
                    pass

    def close(self):
        """Clean up browser resources."""
        try:
            if self._browser_context:
                self._browser_context.close()
                logger.info("✅ Browser context closed")
        except Exception as e:
            logger.error(f"Error closing browser: {e}")


def extract_finviz_screener(
    preset_name: str = None,
    vault_path: str = "data/.cobalt_vault",
    domain: str = "finviz.com"
) -> List[Dict[str, Any]]:
    """
    Convenience function to extract Finviz screener data.
    
    Args:
        preset_name: Name of the screener preset to use (default: "Morning Up Gapper")
        vault_path: Path to the encrypted vault file for credential storage
        domain: Domain for credential resolution (default: finviz.com)
        
    Returns:
        List of dictionaries containing all extracted stock data (dynamic typing)
    """
    extractor = FinvizExtractor(vault_path=vault_path)
    try:
        return extractor.extract(preset_name=preset_name, domain=domain)
    finally:
        extractor.close()