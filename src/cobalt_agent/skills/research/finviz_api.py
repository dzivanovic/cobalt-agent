"""
Finviz API Client - The Macro Engine

Ultra-fast asynchronous HTTP client for Finviz Elite authenticated CSV exports.
Bypasses browser automation entirely, directly querying elite.finviz.com API endpoints.

Features:
- Async HTTP client (httpx) for non-blocking CSV data retrieval
- Vault-based API token resolution using domain namespace format (finviz.com::api_token)
- Screener presets mapped to query strings for direct CSV export
- Quote and news export endpoints with dynamic query building

Security:
- NEVER hardcodes API tokens - resolves dynamically from VaultManager
- Uses urllib.parse for domain extraction and credential namespace resolution
- Zero Trust architecture with JIT secret retrieval

Architecture:
    1. Vault Resolution: Extract domain from URL, query VaultManager for API token
    2. HTTP Request: Construct authenticated CSV endpoint URL with httpx.AsyncClient
    3. CSV Parsing: Parse raw CSV string using csv.DictReader(io.StringIO)
    4. Return: List of dictionaries with dynamic column names as keys
"""

import csv
import io
import os
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse, parse_qs
from loguru import logger

import httpx

from ...config import get_config
from ...security.vault import VaultManager


class FinvizApiClient:
    """
    Finviz Elite API Client - HTTP-based CSV Export Consumer.

    Uses async HTTP requests with Vault-based API token to fetch
    stock data from Finviz Elite screener and export endpoints.

    Architecture:
        1. Vault Resolution: Extract domain from URL, query VaultManager for API token
        2. HTTP Request: Construct authenticated CSV endpoint URL with httpx.AsyncClient
        3. CSV Parsing: Parse raw CSV string using csv.DictReader(io.StringIO)
        4. Return: List of dictionaries with dynamic column names as keys

    Security:
        - API token resolved dynamically from Vault using domain namespace format
        - No hardcoded secrets anywhere in the codebase
        - Zero Trust architecture with JIT secret retrieval

    Performance:
        - Async HTTP client for non-blocking I/O
        - Direct CSV parsing (no HTML scraping overhead)
        - 10-50x faster than Playwright-based extraction
    """

    # Finviz Elite domain for credential resolution
    FINVIZ_DOMAIN = "finviz.com"

    # Master columns: ALL 151 columns (0-150) for complete data extraction
    MASTER_COLUMNS = ",".join(map(str, range(151)))

    # Default screener preset name to look for
    DEFAULT_PRESET_NAME = "Morning Up Gapper"

    # Preset query string mapping (Omit &ar=10 auto-refresh as it is UI-only)
    PRESET_QUERIES: dict[str, str] = {
        "Morning Up Gapper": (
            "v=150&f=sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,"
            "ta_averagetruerange_o0.5,ta_gap_u3&ft=4&o=-volume"
            "&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66"
        ),
        "Morning Down Gapper": (
            "v=150&f=sh_avgvol_o2000,sh_curvol_o100,sh_price_o1,"
            "ta_averagetruerange_o0.5,ta_gap_d3&ft=4&o=-volume"
            "&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66"
        ),
        "Morning Low Float Runners": (
            "v=150&f=sh_float_u10,sh_price_u10,ta_gap_u10&ft=4&o=-volume"
            "&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66"
        ),
        "Day Scan Custom": (
            "v=150&f=sh_curvol_o10000,sh_price_o1,sh_relvol_o3&o=-volume"
            "&c=0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66"
        ),
    }

    def __init__(self, vault_path: str = "data/.cobalt_vault"):
        """
        Initialize the FinvizApiClient.

        Args:
            vault_path: Path to the vault file for credential storage
        """
        self.vault_manager = VaultManager(vault_path)
        self._config = get_config()
        self._api_token: Optional[str] = None

        # Try to initialize vault with master key for immediate token resolution
        self._initialize_vault()

    def compile_filters(self, filters_dict: Dict[str, str]) -> str:
        """
        Convert a filter dictionary into Finviz's comma-separated format.

        Example: {"sh_price": "o1", "ta_gap": "u3"} -> "sh_price_o1,ta_gap_u3"

        Args:
            filters_dict: Dictionary of filter names to filter values

        Returns:
            Comma-separated filter string for Finviz API
        """
        filter_pairs = [f"{key}_{value}" for key, value in filters_dict.items()]
        return ",".join(filter_pairs)

    async def execute_dynamic_screener(
        self, filters_dict: Dict[str, str]
    ) -> List[Dict[str, Any]]:
        """
        Execute a dynamic screener with arbitrary filters.

        Converts filter dictionary to Finviz format and fetches results
        using ALL 151 columns for complete data extraction.

        Args:
            filters_dict: Dictionary of filter names to values
                Example: {"sh_avgvol": "o2000", "sh_curvol": "o100"}

        Returns:
            List of dictionaries containing screener results with all 151 columns

        Raises:
            httpx.TimeoutException: If network timeout occurs
            httpx.HTTPError: If HTTP request fails
        """
        # Compile filters into Finviz format
        filter_string = self.compile_filters(filters_dict)

        # Build query string with master columns (v=152 for custom exports)
        query_string = f"v=152&c={self.MASTER_COLUMNS}&f={filter_string}"

        logger.info(f"🔍 Executing dynamic screener with filters: {filter_string}")

        # Fetch CSV data using base endpoint
        return await self._fetch_csv("export.ashx", query_string)

    def _initialize_vault(self) -> None:
        """
        Initialize vault with master key for API token resolution.

        Attempts to unlock vault using COBALT_MASTER_KEY environment variable
        or config debug_mode master_key for JIT secret retrieval.
        """
        # Check if vault is unlocked, attempt to unlock with master key if available
        if not self.vault_manager._is_unlocked:
            master_key = (
                self._config.system.debug_mode
                and hasattr(self._config, "vault")
                and getattr(self._config.vault, "master_key", None)
            )
            if not master_key:
                import os

                master_key = os.getenv("COBALT_MASTER_KEY")

            if master_key:
                logger.info(f"🔑 Unlocking vault with COBALT_MASTER_KEY")
                if not self.vault_manager.unlock(master_key):
                    logger.error("Failed to unlock vault - API token unavailable")
            else:
                logger.warning(
                    "Vault is locked and no master key available - token resolution deferred"
                )

    async def _resolve_vault_credentials(self, domain: str) -> str:
        """
        Resolve API token from Vault using domain namespace format.

        Uses urllib.parse to extract the domain and query VaultManager for
        credentials in the format: {domain}::{api_token_type}

        Args:
            domain: The target domain (e.g., 'finviz.com')

        Returns:
            API token string or raises ValueError if credentials not found
        """
        # Parse and validate the domain using urllib.parse
        parsed_url = urlparse(f"https://{domain}")
        resolved_domain = parsed_url.netloc or domain

        logger.info(f"🔐 Resolving Vault API token for domain: {resolved_domain}")

        # Query VaultManager for API token using namespace format
        api_token_key = f"{resolved_domain}::api_token"

        # Check if vault is unlocked, attempt to unlock with master key if available
        if not self.vault_manager._is_unlocked:
            master_key = (
                self._config.system.debug_mode
                and hasattr(self._config, "vault")
                and getattr(self._config.vault, "master_key", None)
            )
            if not master_key:
                import os

                master_key = os.getenv("COBALT_MASTER_KEY")

            if master_key:
                logger.info(f"🔑 Unlocking vault with COBALT_MASTER_KEY")
                if not self.vault_manager.unlock(master_key):
                    logger.error("Failed to unlock vault - API token unavailable")
                    raise ValueError(
                        f"Finviz API token not found in vault. Please ensure '{api_token_key}' is set."
                    )
            else:
                logger.error("Vault is locked and no master key available")
                raise ValueError(
                    f"Finviz API token not found in vault. Please ensure '{api_token_key}' is set."
                )

        # Retrieve API token from vault
        api_token = self.vault_manager.get_secret(api_token_key)

        if not api_token:
            logger.error(f"❌ Missing API token in vault: {api_token_key}")
            raise ValueError(
                f"Finviz API token not found in vault. Please ensure '{api_token_key}' is set."
            )

        logger.info(f"✅ API token resolved successfully for {resolved_domain}")
        return api_token

    async def _fetch_csv(
        self, endpoint: str, query_string: str
    ) -> List[Dict[str, Any]]:
        """
        Base CSV fetcher for Finviz Elite API endpoints.

        Constructs the authenticated URL, performs async HTTP GET request,
        and parses raw CSV response into list of dictionaries.

        Args:
            endpoint: API endpoint path (e.g., 'export.ashx')
            query_string: URL-encoded query parameters

        Returns:
            List of dictionaries with CSV column names as keys and cell values as values

        Raises:
            httpx.TimeoutException: If network timeout occurs
            httpx.HTTPError: If HTTP request fails
        """
        # Resolve API token from Vault
        api_token = self._api_token or await self._resolve_vault_credentials(
            self.FINVIZ_DOMAIN
        )

        if not api_token:
            logger.error("❌ API token unavailable - cannot fetch data")
            raise ValueError(
                "Finviz API token not found in vault. Please ensure 'finviz.com::api_token' is set."
            )

        # Construct the full URL with authentication token
        base_url = "https://elite.finviz.com"
        url = f"{base_url}/{endpoint}?{query_string}&auth={api_token}"

        logger.info(f"🌐 Fetching CSV from: {endpoint}?{query_string[:50]}...")

        # Use httpx.AsyncClient for non-blocking HTTP request
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.get(url)

                # Raise HTTPError for 4xx/5xx responses
                response.raise_for_status()

                # Parse raw CSV string using csv.DictReader(io.StringIO)
                csv_reader = csv.DictReader(io.StringIO(response.text))
                rows = list(csv_reader)

                logger.info(f"✅ Fetched {len(rows)} rows from {endpoint}")
                return rows

            except httpx.TimeoutException as e:
                logger.error(f"Network timeout fetching {endpoint}: {e}")
                raise
            except httpx.HTTPError as e:
                logger.error(f"HTTP error fetching {endpoint}: {e}")
                raise

    async def get_screener(self, preset_name: str) -> List[Dict[str, Any]]:
        """
        Fetch screener results for a preset.

        Maps preset name to query string and calls _fetch_csv with
        the export.ashx endpoint.

        Args:
            preset_name: Name of the screener preset (e.g., "Morning Up Gapper")

        Returns:
            List of dictionaries containing screener results

        Raises:
            ValueError: If preset name is not in PRESET_QUERIES mapping
            httpx.TimeoutException: If network timeout occurs
        """
        if preset_name not in self.PRESET_QUERIES:
            logger.error(
                f"Preset '{preset_name}' not found in PRESET_QUERIES mapping"
            )
            raise ValueError(
                f"Preset '{preset_name}' not found. Available presets: {list(self.PRESET_QUERIES.keys())}"
            )

        query_string = self.PRESET_QUERIES[preset_name]

        return await self._fetch_csv("export.ashx", query_string)

    async def get_quote(self, ticker: str) -> List[Dict[str, Any]]:
        """
        Fetch quote data for a specific ticker.

        Targets: quote_export.ashx?t={ticker}&ty=c&p=d&b=1

        Args:
            ticker: Stock ticker symbol (e.g., "AAPL")

        Returns:
            List of dictionaries containing quote data

        Raises:
            httpx.TimeoutException: If network timeout occurs
        """
        ticker = ticker.upper().strip()
        query_string = f"t={ticker}&ty=c&p=d&b=1"

        return await self._fetch_csv("quote_export.ashx", query_string)

    async def get_news(
        self, ticker: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch news data for a ticker or general market news.

        Targets:
            - With ticker: news_export.ashx?t={ticker}
            - Without ticker: news_export.ashx (general market news)

        Args:
            ticker: Stock ticker symbol (optional). If None, returns general news.

        Returns:
            List of dictionaries containing news data

        Raises:
            httpx.TimeoutException: If network timeout occurs
        """
        if ticker:
            ticker = ticker.upper().strip()
            query_string = f"t={ticker}"
        else:
            query_string = ""

        return await self._fetch_csv("news_export.ashx", query_string)


async def fetch_finviz_screener(
    preset_name: Optional[str] = None,
    vault_path: str = "data/.cobalt_vault",
) -> List[Dict[str, Any]]:
    """
    Convenience function to fetch Finviz screener data.

    Args:
        preset_name: Name of the screener preset to use (default: "Morning Up Gapper")
        vault_path: Path to the encrypted vault file for credential storage

    Returns:
        List of dictionaries containing all screener data (dynamic typing)
    """
    client = FinvizApiClient(vault_path=vault_path)
    try:
        return await client.get_screener(preset_name or "Morning Up Gapper")
    finally:
        pass


async def fetch_finviz_quote(
    ticker: str,
    vault_path: str = "data/.cobalt_vault",
) -> List[Dict[str, Any]]:
    """
    Convenience function to fetch Finviz quote data.

    Args:
        ticker: Stock ticker symbol (e.g., "AAPL")
        vault_path: Path to the encrypted vault file for credential storage

    Returns:
        List of dictionaries containing quote data
    """
    client = FinvizApiClient(vault_path=vault_path)
    try:
        return await client.get_quote(ticker)
    finally:
        pass


async def fetch_finviz_news(
    ticker: Optional[str] = None,
    vault_path: str = "data/.cobalt_vault",
) -> List[Dict[str, Any]]:
    """
    Convenience function to fetch Finviz news data.

    Args:
        ticker: Stock ticker symbol (optional). If None, returns general news.
        vault_path: Path to the encrypted vault file for credential storage

    Returns:
        List of dictionaries containing news data
    """
    client = FinvizApiClient(vault_path=vault_path)
    try:
        return await client.get_news(ticker)
    finally:
        pass