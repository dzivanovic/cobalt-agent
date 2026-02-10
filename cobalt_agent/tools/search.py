"""
Search Tool
Now returns strict Pydantic models instead of raw dictionaries.
Updated to use the new 'ddgs' package.
"""
from typing import List
from pydantic import BaseModel, Field
from loguru import logger
from ddgs import DDGS # <--- CHANGED THIS IMPORT

# --- PYDANTIC MODELS ---
class SearchResult(BaseModel):
    """A single search result item."""
    title: str = Field(description="The title of the search result.")
    href: str = Field(description="The URL link to the result.")
    body: str = Field(description="The snippet or summary text.")

# --- TOOL ---
class SearchTool:
    def __init__(self):
        pass

    def run(self, query: str, max_results: int = 5) -> List[SearchResult]:
        """
        Executes a search and returns a list of typed SearchResult objects.
        """
        try:
            logger.debug(f"Searching for: {query}")
            
            # 1. Execute Search
            # We use the context manager approach for safety
            with DDGS() as ddgs:
                # .text() returns a generator/iterator, so we cast to list
                results = list(ddgs.text(query, max_results=max_results))
            
            # 2. Convert to Pydantic Models
            structured_results = []
            for item in results:
                try:
                    # We map the raw dict keys to our model
                    structured_results.append(SearchResult(
                        title=item.get('title', 'No Title'),
                        href=item.get('href', '#'),
                        body=item.get('body', 'No description available.')
                    ))
                except Exception as e:
                    logger.warning(f"Skipping malformed search result: {e}")
            
            if not structured_results:
                 logger.warning(f"No results found for '{query}'")
                 return []
                 
            return structured_results

        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []