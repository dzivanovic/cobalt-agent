"""
Browser Tool with Playwright
Visits a URL and extracts clean text content. Supports dynamic actions via JSON DSL.

Features:
- Headless Chromium browsing
- Form filling, clicks, and navigation
- JSON-based action sequence support
- Clean text extraction
- AOM ID-based element referencing
- Vault credential injection
- Fast Path cache lookup and write-back for Phase 3
"""
import json
import time
from typing import Optional, Literal, Union, Dict, Any, List
from pydantic import BaseModel, Field, ValidationError, Discriminator, Tag
from loguru import logger
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError, ElementHandle

from .maps import Maps, get_maps
from ..security.vault import VaultManager
from ..config import get_config
from ..memory.postgres import PostgresMemory, compute_task_hash, compute_context_signature

# Define BrowserCommand class for backward compatibility
class BrowserCommand(BaseModel):
    """Pydantic model for browser tool command validation."""
    url: str = Field(default="", description="The URL to navigate to")
    actions: list = Field(default_factory=list, description="List of actions to perform")


class ClickAction(BaseModel):
    """Action to click on an element by its AOM ID."""
    action: Literal["click"] = "click"
    id: int


class TypeAction(BaseModel):
    """Action to type text into an element by its AOM ID."""
    action: Literal["type"] = "type"
    id: int
    text: str


class MapsAction(BaseModel):
    """Action to navigate to a URL and refresh the element map."""
    action: Literal["maps"] = "maps"
    url: str


class ExtractAction(BaseModel):
    """Action to extract AOM data from the current page."""
    action: Literal["extract"] = "extract"


class InjectCredentialsAction(BaseModel):
    """Action to inject credentials from Vault for authentication."""
    action: Literal["inject_credentials"] = "inject_credentials"
    vault_path: str


BrowserAction = Union[
    ClickAction,
    TypeAction,
    MapsAction,
    ExtractAction,
    InjectCredentialsAction
]


class WebPageContent(BaseModel):
    """Structured content from a visited webpage."""
    url: str = Field(description="The final URL after navigation.")
    title: str = Field(description="The page title.")
    content: str = Field(description="The cleaned text content of the page.")
    error: str = Field(default="", description="Error message if fetch failed.")

    def __str__(self):
        if self.error:
            return f"[Error reading {self.url}]: {self.error}"
        return f"### {self.title}\n{self.content[:4000]}.."


class BrowserTool:
    name = "browser"
    description = (
        "A full headless browser. You can pass a simple URL to scrape it, OR pass a JSON string to perform actions. "
        "JSON schema: {'url': '...', 'actions': [{'type': 'fill', 'selector': '...', 'text': '...'}, {'type': 'click', 'selector': '...'}]}"
    )

    def __init__(self):
        """Initialize the BrowserTool with Maps instance and Fast Path cache."""
        self._maps = get_maps()
        self._vault_manager: Optional[VaultManager] = None
        self._current_page = None
        self._postgres_memory: Optional[PostgresMemory] = None
        self._fast_path_cache = None
        self._fast_path_metrics = {
            "cache_hits": 0,
            "cache_misses": 0,
            "total_time_ms": 0
        }
        
        # Initialize Fast Path cache if postgres is available
        try:
            self._postgres_memory = PostgresMemory()
            self._fast_path_cache = self._postgres_memory.fast_path_cache
            logger.info("✅ Fast Path cache initialized")
        except Exception as e:
            logger.warning(f"⚠️ Fast Path cache initialization skipped: {e}")
            self._fast_path_cache = None

    def _parse_browser_action(self, raw_action: Dict[str, Any]) -> BrowserAction:
        """
        Parse a raw dictionary into a BrowserAction Pydantic model.
        
        Args:
            raw_action: Dictionary containing action data
            
        Returns:
            Parsed BrowserAction (one of the action types)
            
        Raises:
            ValidationError: If the action doesn't match any valid schema
        """
        # Determine action type from the 'action' field
        action_type = raw_action.get("action")
        
        if action_type == "click":
            return ClickAction(**raw_action)
        elif action_type == "type":
            return TypeAction(**raw_action)
        elif action_type == "maps":
            return MapsAction(**raw_action)
        elif action_type == "extract":
            return ExtractAction(**raw_action)
        elif action_type == "inject_credentials":
            return InjectCredentialsAction(**raw_action)
        else:
            from pydantic import ValidationError
            raise ValueError(f"Unknown action type: {action_type}")

    def _get_element_selector(self, element_id: int) -> Optional[str]:
        """
        Get the CSS selector for an element by its AOM ID.
        
        Args:
            element_id: The numeric AOM ID
            
        Returns:
            CSS selector string, or None if not found
        """
        element_ref = self._maps.get_element(element_id)
        if element_ref:
            return element_ref.get("selector")
        return None

    def _execute_click(self, element_id: int) -> str:
        """
        Execute a click action on an element by its AOM ID.
        
        Args:
            element_id: The numeric AOM ID
            
        Returns:
            Observation string describing the result
        """
        selector = self._get_element_selector(element_id)
        if not selector:
            return f"Error: Element ID {element_id} not found in current map"
        
        if not self._current_page:
            return f"Error: No page loaded"
        
        try:
            self._current_page.wait_for_selector(selector, timeout=5000)
            self._current_page.click(selector)
            return f"Successfully clicked element with ID {element_id} (selector: {selector})"
        except Exception as e:
            return f"Error clicking element ID {element_id}: {str(e)}"

    def _execute_type(self, element_id: int, text: str) -> str:
        """
        Execute a type action on an element by its AOM ID.
        
        Args:
            element_id: The numeric AOM ID
            text: Text to type
            
        Returns:
            Observation string describing the result
        """
        selector = self._get_element_selector(element_id)
        if not selector:
            return f"Error: Element ID {element_id} not found in current map"
        
        if not self._current_page:
            return f"Error: No page loaded"
        
        try:
            self._current_page.wait_for_selector(selector, timeout=5000)
            self._current_page.fill(selector, text)
            return f"Successfully typed '{text}' into element ID {element_id} (selector: {selector})"
        except Exception as e:
            return f"Error typing into element ID {element_id}: {str(e)}"

    def _execute_maps(self, url: str) -> str:
        """
        Execute a navigation action and refresh the element map.
        
        Args:
            url: URL to navigate to
            
        Returns:
            Observation string describing the result
        """
        if not self._current_page:
            return "Error: No page loaded"
        
        try:
            # Navigate to the new URL
            self._current_page.goto(url, wait_until="domcontentloaded", timeout=15000)
            self._current_page.wait_for_timeout(2000)
            
            # Refresh the maps with the new page
            self._maps.refresh_tree(self._current_page, url)
            
            title = self._current_page.title()
            return f"Navigated to {url}. Title: {title}. Maps tree refreshed."
        except Exception as e:
            return f"Error navigating to {url}: {str(e)}"

    def _execute_extract(self) -> str:
        """
        Execute an extract action to get AOM data from current page.
        
        Returns:
            Observation string with extracted element count
        """
        if not self._current_page:
            return "Error: No page loaded. Please navigate to a URL first."
        
        try:
            # Get the current page URL
            url = self._current_page.url
            
            # Use the AOMExtractor to get elements
            from .aom import AOMExtractor
            extractor = AOMExtractor()
            elements = extractor.extract(url)
            
            # Update maps with the new elements
            for element in elements:
                element_id = element.get("id")
                if element_id is None:
                    continue  # Skip elements without valid IDs
                role = element.get("role", "")
                name = element.get("name", "")
                
                # Create a simple selector based on role
                selector = self._generate_selector(element)
                
                if selector:
                    self._maps.add_element(element_id, selector)
            
            return f"Extracted {len(elements)} elements from current page."
        except Exception as e:
            return f"Error extracting AOM data: {str(e)}"

    def _execute_inject_credentials(self, vault_path: str) -> str:
        """
        Execute a credential injection action using VaultManager.
        
        Args:
            vault_path: Path/identifier for the credentials in the vault
            
        Returns:
            Observation string describing the result
        """
        # Get the vault manager from config
        try:
            config = get_config()
            vault_mgr = config.vault_manager
            
            if not vault_mgr:
                return "Error: VaultManager not initialized. Vault may be locked."
            
            if not vault_mgr._is_unlocked:
                return "Error: Vault is locked. Please unlock vault first."
            
            # Retrieve credentials from vault
            credentials = vault_mgr.get_secret(vault_path)
            
            if not credentials:
                return f"Error: No credentials found at path '{vault_path}'"
            
            # Parse credentials
            try:
                cred_dict = json.loads(credentials)
            except json.JSONDecodeError:
                # If not JSON, treat as a single secret value
                cred_dict = {"value": credentials}
            
            # Inject credentials into the page
            result = self._inject_credentials_to_page(cred_dict)
            
            # Note: credentials are NEVER returned in the observation
            return result
            
        except Exception as e:
            logger.exception(f"Failed to inject credentials: {e}")
            return f"Error injecting credentials: {str(e)}"

    def _inject_credentials_to_page(self, credentials: Dict[str, str]) -> str:
        """
        Inject credentials into the current page using Playwright.
        
        Args:
            credentials: Dictionary of credential key-value pairs
            
        Returns:
            Observation string describing injection results
        """
        if not self._current_page:
            return "Error: No page loaded. Cannot inject credentials."
        
        injected_count = 0
        
        # Try common credential field selectors
        for key, value in credentials.items():
            if not value:
                continue
                
            # Try various field selectors
            selectors_to_try = [
                f'input[name="{key}"]',
                f'input[id="{key}"]',
                f'input[placeholder*="{key}"]',
            ]
            
            for selector in selectors_to_try:
                try:
                    self._current_page.wait_for_selector(selector, timeout=2000)
                    self._current_page.fill(selector, value)
                    injected_count += 1
                    logger.debug(f"Injected credential '{key}' via selector: {selector}")
                    break  # Move to next credential once we find a matching field
                except Exception:
                    continue
        
        if injected_count > 0:
            return f"Successfully injected {injected_count} credential(s) into page fields."
        else:
            return "Note: No matching form fields found for injected credentials (credentials not returned)."

    def _generate_fast_path_task_hash(self, url: str, actions: List[Dict]) -> str:
        """
        Generate a deterministic task hash for Fast Path caching.
        
        Args:
            url: The URL being accessed
            actions: List of action dictionaries
            
        Returns:
            UUID string hash for the task
        """
        # Create a deterministic representation of the task
        task_data = {
            "url": url,
            "actions": actions
        }
        task_json = json.dumps(task_data, sort_keys=True)
        return compute_task_hash(task_json)
    
    def _generate_context_signature(self, url: str) -> str:
        """
        Generate a context signature for the URL.
        
        Args:
            url: The URL to generate context signature for
            
        Returns:
            SHA-256 hex string signature
        """
        # We'll need to get page content for context signature
        # For now, use the URL as context
        return compute_context_signature(url, "", "")
    
    def _execute_fast_path_lookup(
        self, 
        url: str, 
        actions: List[Dict], 
        task_hash: str,
        context_signature: str
    ) -> Optional[Dict]:
        """
        Look up a cached browser task in the Fast Path cache.
        
        Args:
            url: The URL being accessed
            actions: List of action dictionaries
            task_hash: Pre-computed task hash
            context_signature: Pre-computed context signature
            
        Returns:
            Cached task data if found, None otherwise
        """
        if not self._fast_path_cache:
            return None
            
        try:
            # Look up by context signature and task hash
            result = self._fast_path_cache.lookup(
                task_intent=f"{url}: {json.dumps(actions)}",
                context_signature=context_signature,
                similarity_threshold=0.85
            )
            
            if result:
                logger.info(f"✅ Fast Path cache HIT for task {task_hash[:8]}...")
                self._fast_path_metrics["cache_hits"] += 1
                return result
                
            logger.debug(f"Fast Path cache MISS for task {task_hash[:8]}...")
            self._fast_path_metrics["cache_misses"] += 1
            return None
            
        except Exception as e:
            logger.error(f"Failed to lookup Fast Path cache: {e}")
            return None
    
    def _execute_fast_path_write_back(
        self,
        url: str,
        actions: List[Dict],
        task_hash: str,
        context_signature: str,
        element_tree_snapshot: Dict[str, Any],
        playwright_script: str,
        execution_time_ms: int
    ) -> bool:
        """
        Write a successful task back to the Fast Path cache.
        
        Args:
            url: The URL that was accessed
            actions: List of action dictionaries
            task_hash: The task hash
            context_signature: The context signature
            element_tree_snapshot: The AOM element tree snapshot
            playwright_script: The Playwright script to execute
            execution_time_ms: The execution time in milliseconds
            
        Returns:
            True if successful, False otherwise
        """
        if not self._fast_path_cache:
            return False
            
        try:
            self._fast_path_cache.write_back(
                task_hash=task_hash,
                task_intent=f"{url}: {json.dumps(actions)}",
                context_signature=context_signature,
                element_tree_snapshot=element_tree_snapshot,
                playwright_script=playwright_script,
                success_rate=1.0
            )
            logger.info(f"✅ Fast Path cache written for task {task_hash[:8]}...")
            return True
        except Exception as e:
            logger.error(f"Failed to write to Fast Path cache: {e}")
            return False
    
    def _generate_selector(self, element: Dict[str, Any]) -> Optional[str]:
        """
        Generate a CSS selector for an element based on its properties.
        
        Args:
            element: Element dictionary from AOM extraction
            
        Returns:
            CSS selector string, or None if not possible
        """
        role = element.get("role", "")
        name = element.get("name", "")
        aria = element.get("aria", {})
        
        # Try aria-label first (most specific)
        if "aria-label" in aria:
            return f'[aria-label="{aria["aria-label"]}"]'
        
        # Try name attribute
        if name:
            # Escape special characters in selector
            safe_name = name.replace('"', '\\"')
            return f'[aria-label="{safe_name}"], [placeholder="{safe_name}"]'
        
        # Try role-based selector
        role_selectors = {
            "button": "button",
            "link": "a",
            "input": "input",
            "textbox": "input[type='text'], textarea",
            "heading": "h1, h2, h3, h4, h5, h6",
        }
        
        if role in role_selectors:
            return role_selectors[role]
        
        return None

    def run(self, **kwargs) -> WebPageContent:
        """
        Executes a browsing session. Handles both simple URLs and JSON action sequences.
        
        Args:
            **kwargs: Either a 'query' string (URL) or 'url' and 'actions' parameters
        
        Returns:
            WebPageContent with the extracted data
        """
        # Try to parse input through Pydantic model for strict validation
        try:
            # Try to validate against BrowserCommand first
            if kwargs:
                try:
                    validated = BrowserCommand(**kwargs)
                    url = validated.url
                    actions = validated.actions
                except ValidationError:
                    # Fallback: check if there's a 'query' key with string value
                    query = kwargs.get("query", "")
                    if isinstance(query, str) and query.strip().startswith("{") and query.strip().endswith("}"):
                        command = json.loads(query)
                        url = command.get("url", "")
                        actions = command.get("actions", [])
                    else:
                        # Last resort: use query as URL directly
                        url = query if query else ""
                        actions = []
            else:
                url = ""
                actions = []
        except ValidationError as e:
            # Return error for invalid Pydantic validation
            return WebPageContent(url="unknown", title="Validation Error", content="", error=str(e))
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse browser query as JSON: {e}")
            return WebPageContent(url="unknown", title="Parse Error", content="", error=f"Invalid JSON: {e}")
        
        # If url is empty at this point, try to get it from query parameter directly
        if not url:
            query = kwargs.get("query", "")
            if isinstance(query, str):
                url = query.strip()
            else:
                url = ""
        
        actions = []
        if isinstance(query, str) and query.strip().startswith("{") and query.strip().endswith("}"):
            try:
                command = json.loads(query)
                url = command.get("url", url)
                actions = command.get("actions", actions)
            except json.JSONDecodeError:
                logger.warning("Failed to parse browser query as JSON, treating as raw URL.")
        
        # Ensure URL has protocol
        if not url.startswith("http"):
            url = "https://" + url

        logger.info(f"🌐 Playwright navigating to: {url}")

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                page = context.new_page()
                self._current_page = page
                
                # 1. Navigate
                page.goto(url, wait_until="domcontentloaded", timeout=15000)
                
                # 2. Refresh maps with the new page
                self._maps.refresh_tree(page, url)

                # 3. Process each action
                action_results = []
                
                for raw_action in actions:
                    try:
                        # Parse the raw action into a Pydantic model
                        action = self._parse_browser_action(raw_action)
                        logger.debug(f"Parsed action: {action}")
                        
                        # Execute based on action type
                        if isinstance(action, ClickAction):
                            result = self._execute_click(action.id)
                            action_results.append(result)
                            logger.debug(f"Click result: {result}")
                            
                        elif isinstance(action, TypeAction):
                            result = self._execute_type(action.id, action.text)
                            action_results.append(result)
                            logger.debug(f"Type result: {result}")
                            
                        elif isinstance(action, MapsAction):
                            result = self._execute_maps(action.url)
                            action_results.append(result)
                            logger.debug(f"Maps result: {result}")
                            
                        elif isinstance(action, ExtractAction):
                            result = self._execute_extract()
                            action_results.append(result)
                            logger.debug(f"Extract result: {result}")
                            
                        elif isinstance(action, InjectCredentialsAction):
                            result = self._execute_inject_credentials(action.vault_path)
                            action_results.append(result)
                            logger.debug(f"Inject credentials result: {result}")
                            
                    except ValidationError as e:
                        error_msg = f"Action validation error: {str(e)}"
                        action_results.append(error_msg)
                        logger.warning(error_msg)
                    except Exception as e:
                        error_msg = f"Error executing action: {str(e)}"
                        action_results.append(error_msg)
                        logger.exception(error_msg)

                # 4. Wait for any dynamic content to settle
                page.wait_for_timeout(2000)

                # 5. Extract Data
                title = page.title()
                
                # Strip out scripts and styles before getting text
                page.evaluate("""
                    document.querySelectorAll('script, style, nav, footer, header, iframe').forEach(el => el.remove());
                """)
                content = page.locator("body").inner_text()
                
                # Clean up whitespace
                clean_text = "\n".join([line.strip() for line in content.splitlines() if line.strip()])
                final_url = page.url

                browser.close()

                # Combine action results into observation
                observation = ""
                if action_results:
                    observation = "\n".join(action_results)
                
                return WebPageContent(
                    url=final_url,
                    title=title,
                    content=clean_text
                )

        except PlaywrightTimeoutError:
            return WebPageContent(url=url, title="Timeout", content="", error="Page load or action timed out.")
        except Exception as e:
            logger.exception(f"Playwright error: {e}")
            return WebPageContent(url=url, title="Error", content="", error=str(e))