"""
Tests for AOM (Accessibility Object Model) Extractor.

This module tests:
1. URL domain whitelist validation
2. DOM snapshot extraction from example.com
3. Compressed element format generation
4. SecurityViolation raised for non-whitelisted domains
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from src.cobalt_agent.tools.aom import AOMExtractor, SecurityViolation, extract_aom, is_url_allowed


class TestDomainWhitelist:
    """Test domain whitelist validation."""
    
    def test_allowed_domain_passes(self):
        """Test that whitelisted domains are accepted."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com", "test.com"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            # example.com should always be allowed as default
            assert is_url_allowed("https://example.com")
            assert is_url_allowed("http://example.com")
            assert is_url_allowed("https://example.com/page")
    
    def test_malicious_domain_raises_security_violation(self):
        """Test that non-whitelisted domains raise SecurityViolation."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com", "test.com"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            with pytest.raises(SecurityViolation) as exc_info:
                extractor._validate_url("https://malicious-domain.com")
            
            assert "malicious-domain.com" in str(exc_info.value)
            assert "not in the allowed domains list" in str(exc_info.value)
    
    def test_trailing_path_does_not_affect_whitelist(self):
        """Test that paths don't affect domain whitelist."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com", "test.com"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            # Should pass - example.com is whitelisted
            result = extractor._validate_url("https://example.com/some/path")
            assert "example.com" in result
    
    def test_port_is_stripped_correctly(self):
        """Test that ports are stripped from domain before validation."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com", "test.com"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            # Should pass - port is stripped, domain is checked
            result = extractor._validate_url("https://example.com:8080/page")
            assert result == "https://example.com:8080/page"
    
    def test_config_domains_are_loaded(self):
        """Test that config-defined domains are loaded."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com", "test.com", "mydomain.org"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            # Should include example.com as minimum
            assert len(extractor.allowed_domains) >= 1
            assert "example.com" in extractor.allowed_domains


class TestAOMExtraction:
    """Test AOM extraction functionality."""
    
    def test_extract_returns_list(self):
        """Test that extract returns a list of elements."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            # Mock the browser and page
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            # Create a mock snapshot result
            mock_snapshot = {
                "nodes": [
                    [1, 0, 1, 2, 3, 4],  # Element node
                ],
                "strings": ["html", "body", "onclick", "clickHandler"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            elements = extractor.extract("https://example.com")
            
            assert isinstance(elements, list)
            assert len(elements) > 0
    
    def test_element_has_required_fields(self):
        """Test that each element has required fields."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            # Mock the browser and page
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            # Create a mock snapshot result with proper node structure
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1, 2, 3, 4, 5],  # Element node with attributes
                ],
                "strings": ["html", "body", "role", "button", "aria-label", "Test Button"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            elements = extractor.extract("https://example.com")
            
            for element in elements:
                assert "id" in element
                assert "role" in element
                assert "name" in element
                assert "state" in element
                assert "aria" in element
                assert "value" in element
    
    def test_element_has_numeric_id(self):
        """Test that element IDs are numeric."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1, 2, 3],
                ],
                "strings": ["div", "id", "test"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            elements = extractor.extract("https://example.com")
            
            for element in elements:
                assert isinstance(element["id"], int), f"Expected int, got {type(element['id'])}"
                assert element["id"] >= 0, "ID should be non-negative"
    
    def test_element_has_role(self):
        """Test that elements have accessibility roles."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1],  # Element with no attributes
                ],
                "strings": ["button"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            elements = extractor.extract("https://example.com")
            
            for element in elements:
                assert element["role"] is not None
                assert element["role"] != ""
                assert isinstance(element["role"], str)
    
    def test_state_has_actionable_properties(self):
        """Test that state has enabled, visible, editable."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1, 2, 3, 4, 5],  # Element with attributes
                ],
                "strings": ["button", "role", "button", "aria-label", "Click Me"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            elements = extractor.extract("https://example.com")
            
            for element in elements:
                state = element["state"]
                assert "enabled" in state
                assert "visible" in state
                assert "editable" in state
                assert isinstance(state["enabled"], bool)
                assert isinstance(state["visible"], bool)
    
    def test_aria_is_dict(self):
        """Test that aria attributes are returned as dict."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1, 2, 3, 4, 5],  # Element with ARIA
                ],
                "strings": ["button", "aria-label", "Click Me", "aria-hidden", "false"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            elements = extractor.extract("https://example.com")
            
            for element in elements:
                aria = element["aria"]
                assert isinstance(aria, dict)
    
    def test_value_is_string(self):
        """Test that value is a string."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1, 2, 3, 4, 5],  # Element with value
                ],
                "strings": ["input", "value", "test value"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            elements = extractor.extract("https://example.com")
            
            for element in elements:
                value = element["value"]
                assert isinstance(value, str)


class TestLocalFileExtraction:
    """Test extraction from local HTML files."""
    
    def test_extract_from_local_file(self, tmp_path: Path):
        """Test extracting from a local HTML file."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            # Mock the browser and page
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1],
                ],
                "strings": ["div"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            file_url = "file:///test/test.html"
            elements = extractor.extract(file_url)
            
            assert isinstance(elements, list)
            assert len(elements) > 0
    
    def test_local_file_contains_expected_roles(self, tmp_path: Path):
        """Test that local file extraction has expected roles."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1],  # div
                    [1, 1, -1, 2, 3],  # h1
                ],
                "strings": ["div", "h1", "role", "heading"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            file_url = "file:///test/test.html"
            elements = extractor.extract(file_url)
            
            roles = [e["role"] for e in elements]
            
            # Should contain heading role
            assert "heading" in roles


class TestExtractAOMFunction:
    """Test the convenience extract_aom function."""
    
    def test_extract_aom_function(self):
        """Test extract_aom convenience function."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1],
                ],
                "strings": ["div"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            elements = extract_aom("https://example.com")
            
            assert isinstance(elements, list)
            assert len(elements) > 0
    
    def test_extract_aom_validates_url(self):
        """Test that extract_aom validates URL."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            with pytest.raises(SecurityViolation):
                extract_aom("https://malicious-domain.com")


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_empty_url_raises_error(self):
        """Test that empty URL raises SecurityViolation."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            with pytest.raises(SecurityViolation):
                extractor._validate_url("")
    
    def test_invalid_url_format(self):
        """Test that invalid URL format raises error."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            with pytest.raises(SecurityViolation):
                extractor._validate_url("not-a-url")
    
    def test_subdomain_validation(self):
        """Test subdomain validation."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config:
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            extractor = AOMExtractor()
            
            # Subdomain of whitelisted domain should fail
            # (unless explicitly added to whitelist)
            with pytest.raises(SecurityViolation):
                extractor._validate_url("https://sub.example.com")
    
    def test_get_extracted_tree(self):
        """Test getting extracted tree from cache."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1],
                ],
                "strings": ["div"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            
            elements = extractor.extract("https://example.com")
            
            tree = extractor.get_extracted_tree()
            
            assert tree is not None
            assert "url" in tree
            assert "timestamp" in tree
            assert "element_count" in tree
            assert "elements" in tree
            assert tree["element_count"] == len(elements)
    
    def test_clear_cache(self):
        """Test clearing the cache."""
        with patch('src.cobalt_agent.tools.aom.get_config') as mock_get_config, \
             patch('src.cobalt_agent.tools.aom.sync_playwright') as mock_playwright:
            
            mock_config = Mock()
            mock_config.browser = Mock()
            mock_config.browser.allowed_domains = ["example.com"]
            mock_get_config.return_value = mock_config
            
            mock_browser = Mock()
            mock_context = Mock()
            mock_page = Mock()
            mock_cdp_session = Mock()
            
            mock_snapshot = {
                "nodes": [
                    [1, 0, -1],
                ],
                "strings": ["div"]
            }
            
            mock_cdp_session.send.return_value = mock_snapshot
            mock_context.new_cdp_session.return_value = mock_cdp_session
            mock_browser.new_context.return_value = mock_context
            mock_context.new_page.return_value = mock_page
            mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
            
            extractor = AOMExtractor()
            
            extractor.extract("https://example.com")
            
            extractor.clear_cache()
            
            assert extractor.get_extracted_tree() is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])