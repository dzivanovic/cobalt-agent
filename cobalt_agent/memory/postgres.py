"""
Postgres Memory Adapter
Replaces memory.json with a persistent Database.
"""
import os
import json
import psycopg
from datetime import datetime
from typing import List, Dict, Any
from loguru import logger
from .base import MemoryProvider

# Note: We assume load_dotenv() was already called in config.py or main.py

class PostgresMemory(MemoryProvider):
    def __init__(self):
        # 1. Load credentials from Environment (populated by .env)
        # We default to 'cobalt'/'cobalt_brain' just in case, but password must be provided.
        self.user = os.getenv("POSTGRES_USER", "cobalt")
        self.password = os.getenv("POSTGRES_PASSWORD", "")
        self.db_name = os.getenv("POSTGRES_DB", "cobalt_brain")
        
        # 2. Construct the Connection String
        # Since Python runs on the host (not in Docker), we connect to 'localhost'
        self.db_url = f"postgresql://{self.user}:{self.password}@localhost:5432/{self.db_name}"
        
        self._init_db()

    def _get_connection(self):
        """Helper to get a fresh connection."""
        return psycopg.connect(self.db_url, autocommit=True)

    def _init_db(self):
        """Create the table if it doesn't exist."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    # Enable Vector Extension
                    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                    
                    # Create Logs Table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS memory_logs (
                            id SERIAL PRIMARY KEY,
                            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            source TEXT,
                            message TEXT,
                            data JSONB
                        );
                    """)
            logger.info("Connected to Postgres Memory (Hippocampus Online)")
        except Exception as e:
            logger.error(f"Failed to initialize Postgres: {e}")

    def add_log(self, message: str, source: str = "System", data: Dict = None):
        """Insert a new log entry."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO memory_logs (timestamp, source, message, data) VALUES (%s, %s, %s, %s)",
                        (datetime.now(), source, message, json.dumps(data or {}))
                    )
        except Exception as e:
            logger.error(f"Failed to add log to Postgres: {e}")

    def get_context(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get the most recent logs (Short Term RAM)."""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT source, message, data, timestamp 
                        FROM memory_logs 
                        ORDER BY timestamp DESC 
                        LIMIT %s
                    """, (limit,))
                    
                    rows = cur.fetchall()
                    
                    results = []
                    for row in rows:
                        results.append({
                            "source": row[0],
                            "message": row[1],
                            "data": row[2],
                            "timestamp": row[3].isoformat()
                        })
                    return results[::-1] 
        except Exception as e:
            logger.error(f"Failed to get context: {e}")
            return []

    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Keyword Search (SQL ILIKE).
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT source, message, data, timestamp 
                        FROM memory_logs 
                        WHERE message ILIKE %s 
                        ORDER BY timestamp DESC 
                        LIMIT %s
                    """, (f"%{query}%", limit))
                    
                    rows = cur.fetchall()
                    return [{
                        "source": r[0], 
                        "message": r[1], 
                        "data": r[2], 
                        "timestamp": r[3].isoformat()
                    } for r in rows]
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

    def save_memory(self) -> None:
        """
        No-op: Postgres saves data immediately upon write.
        This method exists only to satisfy the interface contract.
        """
        pass