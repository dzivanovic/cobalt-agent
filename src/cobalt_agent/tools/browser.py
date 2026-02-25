"""
Browser Tool with Playwright
Visits a URL and extracts clean text content. Supports dynamic actions via JSON DSL.

Features:
- Headless Chromium browsing
- Form filling, clicks, and navigation
- JSON-based action sequence support
- Clean text extraction
"""
import json
from pydantic import BaseModel, Field
from loguru import logger
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


class WebPageContent(BaseModel):
    """Structured content from a visited webpage."""
    url: str = Field(description="The final URL after navigation.")
    title: str = Field(description="The page title.")
    content: str = Field(description="The cleaned text content of the page.")
    error: str = Field("", description="Error message if fetch failed.")

    def __str__(self):
        if self.error:
            return f"[Error reading {self.url}]: {self.error}"
        return f"### {self.title}\n{self.content[:4000]}..."


class BrowserTool:
    name = "browser"
    description = (
        "A full headless browser. You can pass a simple URL to scrape it, OR pass a JSON string to perform actions. "
        "JSON schema: {'url': '...', 'actions': [{'type': 'fill', 'selector': '...', 'text': '...'}, {'type': 'click', 'selector': '...'}]}"
    )

    def __init__(self):
        pass

    def run(self, query: str) -> WebPageContent:
        """
        Executes a browsing session. Handles both simple URLs and JSON action sequences.
        
        Args:
            query: Either a plain URL string, or a JSON object with:
                - url: The page URL
                - actions: Array of actions (fill, click)
        
        Returns:
            WebPageContent with the extracted data
        """
        url = query.strip()
        actions = []

        # Check if the LLM passed a JSON command object instead of a raw URL
        if query.strip().startswith("{") and query.strip().endswith("}"):
            try:
                command = json.loads(query)
                url = command.get("url", "")
                actions = command.get("actions", [])
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
                
                # 1. Navigate
                page.goto(url, wait_until="domcontentloaded", timeout=15000)

                # 2. Execute Actions (if any)
                for action in actions:
                    act_type = action.get("type")
                    selector = action.get("selector")
                    
                    if act_type == "fill" and selector:
                        text = action.get("text", "")
                        page.fill(selector, text)
                        logger.debug(f"Filled {selector} with '{text}'")
                    elif act_type == "click" and selector:
                        page.click(selector)
                        page.wait_for_load_state("networkidle", timeout=10000)
                        logger.debug(f"Clicked {selector}")

                # 3. Wait for any dynamic content to settle
                page.wait_for_timeout(2000)

                # 4. Extract Data
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

                return WebPageContent(
                    url=final_url,
                    title=title,
                    content=clean_text
                )

        except PlaywrightTimeoutError:
            return WebPageContent(url=url, title="Timeout", content="", error="Page load or action timed out.")
        except Exception as e:
            logger.error(f"Playwright error: {e}")
            return WebPageContent(url=url, title="Error", content="", error=str(e))