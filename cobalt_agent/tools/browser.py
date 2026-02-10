"""
Browser Tool
Visits a URL and extracts clean text content.
Now returns structured Pydantic models.
"""
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field
from loguru import logger

# --- PYDANTIC MODEL ---
class WebPageContent(BaseModel):
    """Structured content from a visited webpage."""
    url: str = Field(description="The source URL.")
    title: str = Field(description="The page title.")
    content: str = Field(description="The cleaned text content of the article/page.")
    error: str = Field("", description="Error message if fetch failed.")

    def __str__(self):
        """Summary for LLM consumption."""
        if self.error:
            return f"[Error reading {self.url}]: {self.error}"
        return f"### {self.title}\n{self.content[:4000]}..." # Truncate to save tokens

# --- TOOL ---
class BrowserTool:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def run(self, url: str) -> WebPageContent:
        """
        Fetches and cleans text from a URL.
        """
        try:
            logger.debug(f"Browsing: {url}")
            
            # 1. Fetch
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # 2. Parse
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract Title
            title = soup.title.string if soup.title else "No Title"
            
            # Extract Text (Remove scripts/styles)
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()
                
            text = soup.get_text(separator="\n")
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            clean_text = '\n'.join(chunk for chunk in chunks if chunk)

            return WebPageContent(
                url=url,
                title=title.strip(),
                content=clean_text
            )

        except Exception as e:
            logger.error(f"Browser failed for {url}: {e}")
            return WebPageContent(
                url=url, 
                title="Error", 
                content="", 
                error=str(e)
            )