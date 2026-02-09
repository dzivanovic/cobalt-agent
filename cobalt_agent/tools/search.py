"""Web search tool using DuckDuckGo."""

from ddgs import DDGS
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class SearchTool:
    """Tool for performing web searches using DuckDuckGo."""
    
    def __init__(self):
        """Initialize the search tool."""
        pass
    
    def run(self, query: str, max_results: int = 3) -> List[Dict[str, Any]]:
        """
        Perform a web search and return results.
        
        Args:
            query: The search query string
            max_results: Maximum number of results to return (default: 3)
            
        Returns:
            List of dictionaries containing search results with keys:
            - title: Result title
            - href: URL link
            - body: Result description/snippet
        """
        try:
            logger.info(f"Performing search for: {query}")
            results = []
            
            # Create DDGS instance and perform search
            with DDGS() as ddgs:
                search_results = ddgs.text(query, max_results=max_results)
                
                # Format the results
                for result in search_results:
                    results.append({
                        'title': result.get('title', ''),
                        'href': result.get('href', ''),
                        'body': result.get('body', '')
                    })
            
            logger.info(f"Found {len(results)} results")
            return results
            
        except Exception as e:
            logger.error(f"Search failed: {str(e)}", exc_info=True)
            return []
