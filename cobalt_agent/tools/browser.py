"""
Cobalt Agent - Web Browser Tool
Allows the agent to visit URLs and extract readable text.
"""

import requests
from bs4 import BeautifulSoup
from loguru import logger
from pydantic import BaseModel, Field

class BrowserTool(BaseModel):
    """
    Tool for reading the content of web pages.
    """
    name: str = "browser"
    description: str = "Visits a specific URL and returns the main text content. Use this to read news articles or documentation found via search."

    def run(self, url: str) -> str:
        """
        Fetch and parse a URL.
        
        Args:
            url: The direct link to visit (e.g., "https://example.com")
        """
        try:
            logger.info(f"Browsing URL: {url}")
            
            # 1. Fetch the page with a User-Agent (to avoid looking like a bot)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # 2. Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 3. Clean up junk (scripts, styles, nav bars)
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()
                
            # 4. Extract text
            text = soup.get_text()
            
            # 5. Clean whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            clean_text = '\n'.join(chunk for chunk in chunks if chunk)
            
            # 6. Limit length (to avoid overflowing context window)
            return clean_text[:8000] + "..." if len(clean_text) > 8000 else clean_text

        except Exception as e:
            logger.error(f"Browser Error: {e}")
            return f"Error reading page: {str(e)}"