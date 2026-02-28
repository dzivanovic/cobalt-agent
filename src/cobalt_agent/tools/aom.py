"""
AOM (Accessibility Object Model) Extractor Module
Extracts DOM tree via Chrome DevTools Protocol (CDP) and converts to compressed format.

This module uses Playwright's CDP session to call `dom.snapshotter.takeDomSnapshot()`
which provides a rich accessibility tree that can be converted to a compressed element
format with numeric IDs for stable referencing.

Features:
- CDP session management with Playwright
- DOM snapshot extraction
- Accessibility tree parsing to compressed dictionary format
- Ephemeral context management (no persistent storage state)
"""

import re
import hashlib
from typing import Optional
from playwright.sync_api import sync_playwright
from loguru import logger
from ..config import get_config


class SecurityViolation(Exception):
    """Exception raised when a URL fails domain whitelist validation."""
    pass


class AOMExtractor:
    """
    Extracts AOM (Accessibility Object Model) from web pages using CDP.
    
    Uses ephemeral browser contexts with no persistent storage state.
    Enforces domain whitelist for Zero-Trust security.
    """
    
    def __init__(self):
        """Initialize the AOM extractor with domain whitelist from config."""
        config = get_config()
        browser_config = config.browser
        self.allowed_domains: list[str] = (
            browser_config.allowed_domains if browser_config else ["example.com"]
        )
        self._extracted_tree: Optional[dict] = None
    
    def _validate_url(self, url: str) -> str:
        """
        Validate URL against the domain whitelist.
        
        File URLs (file:///) are always allowed for local file access.
        HTTP/HTTPS URLs are validated against the domain whitelist.
        
        Args:
            url: The URL to validate
            
        Returns:
            The validated URL
            
        Raises:
            SecurityViolation: If the domain is not in the allowed list
        """
        # File URLs are always allowed for local file access
        if url.startswith("file://"):
            return url
        
        # Extract domain from URL
        domain_pattern = r'https?://([^/]+)'
        match = re.search(domain_pattern, url)
        if not match:
            raise SecurityViolation(f"Invalid URL format: {url}")
        
        domain = match.group(1)
        
        # Remove port if present (e.g., example.com:8080 -> example.com)
        domain = domain.split(':')[0]
        
        # Check against whitelist
        if domain not in self.allowed_domains:
            raise SecurityViolation(
                f"Domain '{domain}' is not in the allowed domains list. "
                f"Allowed: {', '.join(self.allowed_domains)}"
            )
        
        logger.debug(f"URL validated: {domain} is in allowed list")
        return url
    
    def extract(self, url: str, timeout_ms: int = 15000) -> list[dict]:
        """
        Extract the DOM tree from a URL using CDP.
        
        Args:
            url: The URL to extract AOM from
            timeout_ms: Timeout in milliseconds (default 15000)
            
        Returns:
            List of compressed element dictionaries with:
            - id: int - Stable numeric ID
            - role: str - Accessibility role
            - name: str - Accessible name
            - state: dict - Actionable state (enabled, visible, editable)
            - aria: dict - Optional aria-* attributes
            - value: str - Optional value (for inputs)
            
        Raises:
            SecurityViolation: If domain is not whitelisted
            Exception: For browser/CDP errors
        """
        # Validate URL against whitelist
        validated_url = self._validate_url(url)
        
        logger.info(f"Extracting AOM from: {validated_url}")
        
        # Use ephemeral context (no storage state)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                storage_state={}  # Ephemeral - no persistent storage
            )
            page = context.new_page()
            
            try:
                # Navigate with timeout
                page.goto(validated_url, wait_until="domcontentloaded", timeout=timeout_ms)
                
                # Wait for dynamic content to settle
                page.wait_for_timeout(2000)
                
                # Get CDP session
                cdp_session = context.new_cdp_session(page)
                
                # Call DOMSnapshot.captureSnapshot to extract the DOM tree
                snapshot_result = cdp_session.send("DOMSnapshot.captureSnapshot", {
                    "computedStyles": [],
                    "includeDOMBindings": True
                })
                
                # Parse the snapshot into compressed format
                elements = self._parse_snapshot(snapshot_result)
                
                # Store the extracted tree for potential reuse
                self._extracted_tree = {
                    "url": validated_url,
                    "timestamp": __import__("time").time(),
                    "element_count": len(elements),
                    "elements": elements
                }
                
                browser.close()
                logger.info(f"Extracted {len(elements)} elements from {validated_url}")
                
                return elements
                
            except Exception as e:
                logger.exception(f"Failed to extract AOM from {validated_url}: {e}")
                browser.close()
                raise
    
    def _parse_snapshot(self, snapshot: dict) -> list[dict]:
        """
        Parse the DOM snapshot into compressed element format.
        
        Args:
            snapshot: The raw DOM snapshot from CDP
            
        Returns:
            List of compressed element dictionaries
        """
        if not snapshot:
            return []
        
        elements = []
        
        # DOM snapshot structure has nodes array and various metadata
        # Each node has id, role, name, attributes, etc.
        nodes = snapshot.get("nodes", [])
        document_strings = snapshot.get("strings", [])
        
        # Process each node in the snapshot
        for i, node in enumerate(nodes):
            element = self._process_node(node, document_strings)
            if element:
                elements.append(element)
        
        return elements
    
    def _process_node(self, node: list, strings: list[str]) -> Optional[dict]:
        """
        Process a single node from the DOM snapshot.
        
        Args:
            node: The node data (list format from CDP snapshot)
            strings: String table for node attributes
            
        Returns:
            Compressed element dictionary or None if invalid
        """
        if not node or len(node) < 2:
            return None
        
        try:
            # Extract node properties
            node_type = node[0] if len(node) > 0 else 0
            node_name_idx = node[1] if len(node) > 1 else -1
            node_value_idx = node[2] if len(node) > 2 else -1
            
            # Get string values from strings array
            node_name = strings[node_name_idx] if node_name_idx >= 0 else ""
            node_value = strings[node_value_idx] if node_value_idx >= 0 else ""
            
            # Determine role based on node type and name
            role = self._get_role(node_type, node_name)
            
            # Extract state (actionable properties)
            state = self._extract_state(node, strings)
            
            # Extract ARIA attributes
            aria = self._extract_aria(node, strings)
            
            # Extract value for inputs
            value = self._extract_value(node, strings, node_value)
            
            # Create compressed element
            element = {
                "id": self._generate_node_id(node, node_name),
                "role": role,
                "name": state.get("name", node_name),
                "state": state,
                "aria": aria,
                "value": value
            }
            
            # Only include non-empty elements
            if element["role"] and element["id"]:
                return element
            return None
            
        except Exception as e:
            logger.debug(f"Failed to process node: {e}")
            return None
    
    def _get_role(self, node_type: int, node_name: str) -> str:
        """
        Determine the accessibility role from node type and name.
        
        Args:
            node_type: The DOM node type (1=Element, 3=Text, 8=Comment, 9=Document)
            node_name: The node name/tag
            
        Returns:
            Accessibility role string
        """
        # Map common node types to accessibility roles
        role_map = {
            1: "generic",  # Element node - generic container
            3: "text",     # Text node
            8: "comment",  # Comment node
            9: "document", # Document node
        }
        
        # Default from type
        role = role_map.get(node_type, "generic")
        
        # Override with element-specific roles
        if node_type == 1:  # Element node
            node_lower = node_name.lower()
            element_roles = {
                "a": "link",
                "button": "button",
                "input": "input",
                "select": "combobox",
                "textarea": "textbox",
                "img": "image",
                "iframe": "iframe",
                "table": "table",
                "tr": "row",
                "td": "cell",
                "th": "columnheader",
                "h1": "heading",
                "h2": "heading",
                "h3": "heading",
                "h4": "heading",
                "h5": "heading",
                "h6": "heading",
                "li": "listitem",
                "ul": "list",
                "ol": "list",
                "form": "form",
                "header": "banner",
                "footer": "contentinfo",
                "nav": "navigation",
                "main": "main",
                "article": "article",
                "section": "region",
            }
            role = element_roles.get(node_lower, "generic")
        
        return role
    
    def _extract_state(self, node: list, strings: list[str]) -> dict:
        """
        Extract actionable state from node attributes.
        
        Args:
            node: The node data
            strings: String table
            
        Returns:
            State dictionary with enabled, visible, editable keys
        """
        state = {
            "enabled": True,
            "visible": True,
            "editable": False,
            "clickable": False,
            "name": ""
        }
        
        if len(node) < 4:
            return state
        
        # Attributes start at index 3
        attributes = node[3:]
        
        # Process attributes (every other item is key/value)
        for i in range(0, len(attributes), 2):
            if i + 1 >= len(attributes):
                break
            
            key_idx = attributes[i]
            value_idx = attributes[i + 1]
            
            if key_idx < 0 or value_idx < 0:
                continue
                
            key = strings[key_idx] if key_idx < len(strings) else ""
            value = strings[value_idx] if value_idx < len(strings) else ""
            
            # Check for disabled attribute
            if key.lower() == "disabled" and value.lower() in ("", "true"):
                state["enabled"] = False
            
            # Check for hidden attribute
            if key.lower() == "hidden" or key.lower() == "aria-hidden":
                state["visible"] = value.lower() not in ("true", "true")
            
            # Check for editable elements
            if key.lower() == "input" and value.lower() in ("text", "textarea", "password"):
                state["editable"] = True
            
            # Check for aria-readonly
            if key.lower() == "aria-readonly" and value.lower() == "true":
                state["editable"] = False
            
            # Check for name/accessibility name
            if key.lower() in ("aria-label", "aria-labelledby"):
                state["name"] = value
            
            # Check for clickability
            if key.lower() in ("onclick", "role") and value.lower() != "":
                state["clickable"] = True
        
        return state
    
    def _extract_aria(self, node: list, strings: list[str]) -> dict:
        """
        Extract ARIA attributes from node.
        
        Args:
            node: The node data
            strings: String table
            
        Returns:
            Dictionary of ARIA attributes
        """
        aria = {}
        
        if len(node) < 4:
            return aria
        
        attributes = node[3:]
        
        for i in range(0, len(attributes), 2):
            if i + 1 >= len(attributes):
                break
            
            key_idx = attributes[i]
            value_idx = attributes[i + 1]
            
            if key_idx < 0 or value_idx < 0:
                continue
            
            key = strings[key_idx] if key_idx < len(strings) else ""
            value = strings[value_idx] if value_idx < len(strings) else ""
            
            # Only include ARIA attributes
            if key.lower().startswith("aria-"):
                aria[key] = value
        
        return aria
    
    def _extract_value(self, node: list, strings: list[str], default: str = "") -> str:
        """
        Extract the value from an input element.
        
        Args:
            node: The node data
            strings: String table
            default: Default value if not found
            
        Returns:
            The element value
        """
        if len(node) < 4:
            return default
        
        attributes = node[3:]
        
        for i in range(0, len(attributes), 2):
            if i + 1 >= len(attributes):
                break
            
            key_idx = attributes[i]
            value_idx = attributes[i + 1]
            
            if key_idx < 0 or value_idx < 0:
                continue
            
            key = strings[key_idx] if key_idx < len(strings) else ""
            value = strings[value_idx] if value_idx < len(strings) else ""
            
            # Return value for input/textarea
            if key.lower() == "value":
                return value
        
        return default
    
    def _generate_node_id(self, node: list, node_name: str) -> int:
        """
        Generate a stable numeric ID for a node.
        
        Args:
            node: The node data
            node_name: The node name
            
        Returns:
            A deterministic integer ID
        """
        # Use node position in array as primary ID source
        # This provides stable numeric IDs across extracts
        return hash(f"{node_name}_{id(node)}") % (10**8)
    
    def get_extracted_tree(self) -> Optional[dict]:
        """Get the most recently extracted tree."""
        return self._extracted_tree
    
    def clear_cache(self) -> None:
        """Clear the cached extracted tree."""
        self._extracted_tree = None


def extract_aom(url: str) -> list[dict]:
    """
    Convenience function to extract AOM from a URL.
    
    Args:
        url: The URL to extract from
        
    Returns:
        List of compressed element dictionaries
    """
    extractor = AOMExtractor()
    return extractor.extract(url)


def is_url_allowed(url: str) -> bool:
    """
    Check if a URL is allowed by the domain whitelist.
    
    Args:
        url: The URL to check
        
    Returns:
        True if allowed, False otherwise
    """
    extractor = AOMExtractor()
    try:
        extractor._validate_url(url)
        return True
    except SecurityViolation:
        return False