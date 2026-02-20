"""
Postgres Memory Adapter (The Hippocampus)
Hybrid: Combines Persistent Logging with Vector Embeddings for Semantic Search.

Configuration Sources (highest to lowest priority):
1. Environment variables (POSTGRES_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD)
2. YAML config in configs/*.yaml
"""
import os
import json
import psycopg
from datetime import datetime
from typing import List, Dict, Any, Optional
from loguru import logger
from litellm import embedding
from ..config import get_config
from .base import MemoryProvider

class PostgresMemory(MemoryProvider):
    def _get_conn(self):
        """Get a database connection."""
        return psycopg.connect(self.conn_str)
    
    def __init__(self):
        # 1. Load Credentials from config object
        config = get_config()
        postgres_config = config.postgres
        
        self.host = postgres_config.host
        self.port = postgres_config.port
        self.db = postgres_config.db
        self.user = postgres_config.user
        self.password = postgres_config.password or os.getenv("POSTGRES_PASSWORD", "cobalt_password")
        
        # Connection String (using config-based host for proper host-based execution)
        self.conn_str = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        self.table_name = "memory_logs"
        
        # 2. Initialize DB (Auto-create vector table)
        self._init_db()
    
    def _init_db(self):
        """Initialize database connection and create tables."""
        try:
            with self._get_conn() as conn:
                # Enable Vector Extension
                conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                
                # Create Table with VECTOR Column (1536 dims for OpenAI)
                # We use 'content' instead of 'message' to standardize with RAG tools
                conn.execute(f"""
                    CREATE TABLE IF NOT EXISTS {self.table_name} (
                        id SERIAL PRIMARY KEY,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        source TEXT,
                        content TEXT,
                        embedding vector(1536), 
                        metadata JSONB DEFAULT '{{}}'::jsonb
                    );
                """)
                logger.info("🧠 Connected to Postgres Memory (Vector Ready)")
        except Exception as e:
            logger.error(f"Failed to init DB: {e}")

    def _generate_embedding(self, text: str) -> List[float]:
        """Turns text into a list of numbers using LiteLLM."""
        try:
            text = text.replace("\n", " ")
            response = embedding(
                model="text-embedding-3-small",
                input=[text]
            )
            
            # ROBUST PARSING FIX: Handle both Object and Dict responses
            data_item = response.data[0]
            if isinstance(data_item, dict):
                return data_item['embedding']
            else:
                return data_item.embedding
                
        except Exception as e:
            logger.error(f"Embedding failed: {e}")
            return []

    def add_log(self, message: str, source: str = "System", data: Dict = None):
        """
        Saves a memory AND its vector representation.
        """
        # Generate Vector
        vector = self._generate_embedding(message)
        
        if not data:
            data = {}
            
        try:
            with self._get_conn() as conn:
                if vector:
                    conn.execute(
                        f"INSERT INTO {self.table_name} (source, content, embedding, metadata) VALUES (%s, %s, %s, %s)",
                        (source, message, str(vector), json.dumps(data))
                    )
                else:
                    # Fallback (save without vector if embedding fails)
                    conn.execute(
                        f"INSERT INTO {self.table_name} (source, content, metadata) VALUES (%s, %s, %s)",
                        (source, message, json.dumps(data))
                    )
        except Exception as e:
            logger.error(f"Failed to save memory: {e}")

    def get_context(self, limit: int = 10) -> str:
        """
        Get the most recent logs (Short Term RAM).
        Fetched from DB so it persists across restarts.
        """
        try:
            with self._get_conn() as conn:
                # We fetch the raw rows
                rows = conn.execute(f"""
                    SELECT timestamp, source, content 
                    FROM {self.table_name} 
                    ORDER BY timestamp DESC 
                    LIMIT %s
                """, (limit,)).fetchall()
                
                # Format into a chat-log string for the LLM
                context = ""
                # Reverse so it reads chronologically (Old -> New)
                for row in rows[::-1]:
                    ts = row[0].strftime("%H:%M") if hasattr(row[0], 'strftime') else str(row[0])
                    context += f"[{ts}] {row[1]}: {row[2]}\n"
                
                return context
        except Exception as e:
            logger.error(f"Failed to get context: {e}")
            return ""

    def search(self, query: str, limit: int = 5) -> List[Dict]:
        """
        Semantic Search: Finds memories mathematically similar to the query.
        """
        vector = self._generate_embedding(query)
        if not vector:
            return []

        try:
            with self._get_conn() as conn:
                # The <=> operator is "Cosine Distance" (Lower is better)
                results = conn.execute(f"""
                    SELECT timestamp, source, content, metadata, 
                           1 - (embedding <=> %s) as similarity
                    FROM {self.table_name}
                    WHERE embedding IS NOT NULL
                    ORDER BY embedding <=> %s
                    LIMIT %s;
                """, (str(vector), str(vector), limit)).fetchall()
                
                memories = []
                for row in results:
                    # Filter low relevance (Similarity < 0.3 is usually noise)
                    if row[4] < 0.3: 
                        continue
                        
                    memories.append({
                        "timestamp": row[0],
                        "source": row[1],
                        "content": row[2],
                        "metadata": row[3],
                        "score": row[4]
                    })
                
                return memories
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []
            
    def save_memory(self) -> None:
        """Postgres saves immediately, so this is a no-op."""
        pass