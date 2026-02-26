from pydantic import BaseModel, Field
from typing import List, Any
from loguru import logger
from cobalt_agent.memory.postgres import PostgresMemory

class SearchResult(BaseModel):
    source: str
    content: str
    score: float

class KnowledgeSearchTool:
    name = "search_knowledge"
    description = "Search the agent's internal vector database (codebase, playbooks, and Obsidian vault) for semantic context. Pass a conceptual query string."

    def __init__(self):
        self.memory = PostgresMemory()

    def run(self, query=None, **kwargs) -> str:
        """Searches the vector DB and returns formatted results."""
        import json
        import ast
        
        # Universal extraction
        data = query if query is not None else kwargs
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                try:
                    data = ast.literal_eval(data)
                except Exception:
                    pass

        search_query = ""
        if isinstance(data, dict):
            search_query = data.get("query", data.get("search", ""))
        elif isinstance(data, str):
            search_query = data.strip()
            
        if not search_query:
            return "Error: Missing search query."
            
        logger.info(f"📚 Searching Vector Knowledge Base for: '{search_query}'")
        
        try:
            results = self.memory.search(search_query, limit=5)
            if not results:
                return f"No relevant information found in the knowledge base for '{search_query}'."
                
            output = f"### Knowledge Base Results for '{search_query}':\n\n"
            for idx, res in enumerate(results, 1):
                # Retrieve the filepath/metadata if it was stored
                meta = res.get('metadata', {})
                filepath = meta.get('filepath', res.get('source', 'Unknown'))
                content = res.get('content', '').strip()
                score = res.get('score', 0.0)
                
                output += f"**Result {idx}** (Source: `{filepath}`, Relevance: {score:.2f})\n"
                output += f"```text\n{content}\n```\n\n"
                
            return output
            
        except Exception as e:
            logger.error(f"Knowledge search failed: {e}")
            return f"Error executing knowledge search: {e}"