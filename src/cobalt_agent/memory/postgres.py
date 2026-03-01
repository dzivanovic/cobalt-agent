"""
Postgres Memory Adapter (The Hippocampus)
Hybrid: Combines Persistent Logging with Vector Embeddings for Semantic Search.

Context Signature Hashing:
- Computes deterministic SHA-256 hashes for page contexts
- Used for Fast Path cache lookups in Phase 3
- Hash is computed from URL, title, and visible text preview

Configuration Sources (highest to lowest priority):
1. Environment variables (POSTGRES_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD)
2. YAML config in configs/*.yaml
"""

import os
import json
import hashlib
import uuid
import time
from datetime import datetime, timedelta
from html.parser import HTMLParser
from typing import List, Dict, Any, Optional, Tuple
from loguru import logger

try:
    import psycopg
except ImportError:
    psycopg = None
    logger.warning("psycopg not installed, PostgresMemory will fail at runtime")

from litellm import embedding
from ..config import get_config
from ..security.vault import VaultManager
from .base import MemoryProvider


def compute_context_signature(url: str, title: str, visible_text: str) -> str:
    """
    Compute a deterministic SHA-256 hash for a page context.
    
    This function takes the page URL, title, and a preview of visible text,
    then computes a SHA-256 hash that serves as a unique signature for the
    context. This signature is used for Fast Path cache lookups in Phase 3.
    
    Args:
        url: The page URL
        title: The page title
        visible_text: A preview/summary of the visible text content
        
    Returns:
        A hex string SHA-256 hash of the context signature
        
    Example:
        >>> signature = compute_context_signature(
        ...     "https://example.com/page",
        ...     "Example Page",
        ...     "This is the visible content"
        ... )
        >>> print(signature)  # e.g., "a3f2b8c9..."
    """
    # Normalize inputs to ensure consistent hashing
    normalized_url = url.strip().lower()
    normalized_title = title.strip() if title else ""
    normalized_text = visible_text.strip() if visible_text else ""
    
    # Concatenate with a unique delimiter to prevent collisions
    context_string = f"{normalized_url}\x00{normalized_title}\x00{normalized_text}"
    
    # Compute SHA-256 hash
    hash_obj = hashlib.sha256(context_string.encode('utf-8'))
    return hash_obj.hexdigest()


def compute_task_hash(task_intent: str) -> str:
    """
    Compute a deterministic UUID hash for a task intent.
    
    This function takes the task intent (user request + context) and computes
    a deterministic UUID hash that serves as the lookup key for Fast Path
    cache lookups in Phase 3.
    
    Args:
        task_intent: The task intent description
        
    Returns:
        A hex string UUID hash of the task intent
    """
    # Create a deterministic hash from the task intent
    hash_obj = hashlib.sha256(task_intent.encode('utf-8'))
    # Convert to UUID format (version 5 namespace-like)
    hash_bytes = hash_obj.digest()[:16]
    return str(uuid.UUID(bytes=hash_bytes))


def extract_visible_text(page_content: str, max_length: int = 500) -> str:
    """
    Extract visible text content from HTML for context signature.
    
    Args:
        page_content: Raw HTML content from the page
        max_length: Maximum length of returned text
        
    Returns:
        Extracted visible text, truncated to max_length
    """
    class TextExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text_parts = []
            self.in_script_style = False
            
        def handle_starttag(self, tag, attrs):
            if tag.lower() in ('script', 'style'):
                self.in_script_style = True
                
        def handle_endtag(self, tag):
            if tag.lower() in ('script', 'style'):
                self.in_script_style = False
                
        def handle_data(self, data):
            if not self.in_script_style:
                self.text_parts.append(data.strip())
                
        def get_text(self) -> str:
            return ' '.join(filter(None, self.text_parts))
    
    try:
        parser = TextExtractor()
        parser.feed(page_content)
        text = parser.get_text()
        return text[:max_length]
    except Exception:
        # Fallback: simple text extraction
        import re
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', page_content)
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        return text[:max_length]


class FastPathCache:
    """
    Fast Path Cache Manager for Browser Tasks.
    
    Provides CRUD operations for the browser_fast_path table with pgvector
    integration for cosine similarity lookups.
    """
    
    def __init__(self, postgres_memory: 'PostgresMemory'):
        """
        Initialize the Fast Path Cache manager.
        
        Args:
            postgres_memory: The PostgresMemory instance to use for database operations
        """
        self.postgres = postgres_memory
        self._ensure_table_exists()
    
    def _ensure_table_exists(self) -> None:
        """Ensure the browser_fast_path table exists with proper schema."""
        try:
            with self.postgres._get_conn() as conn:
                # Enable Vector Extension
                conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                
                # Create browser_fast_path table
                # task_hash is UUID for lookup
                # task_intent is the text description for similarity search
                # context_signature is the SHA-256 hash for exact matching
                # element_tree_snapshot is the AOM snapshot
                # playwright_script is the deterministic script to execute
                # execution_time_ms tracks performance
                # success_rate tracks reliability
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS browser_fast_path (
                        id SERIAL PRIMARY KEY,
                        task_hash UUID NOT NULL UNIQUE,
                        task_intent TEXT NOT NULL,
                        context_signature TEXT NOT NULL,
                        element_tree_snapshot JSONB NOT NULL,
                        playwright_script TEXT NOT NULL,
                        execution_time_ms INTEGER DEFAULT 0,
                        success_rate FLOAT DEFAULT 1.0,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                
                # Create pgvector index on task_hash for cosine similarity
                # The task_hash is stored as a UUID, which needs to be converted
                # to a vector for similarity search. We'll use a separate embedding
                # column for vector operations.
                conn.execute("""
                    ALTER TABLE browser_fast_path 
                    ADD COLUMN IF NOT EXISTS task_hash_embedding vector(1536);
                """)
                
                # Create index on the embedding column for similarity search
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_browser_fast_path_embedding 
                    ON browser_fast_path 
                    USING ivfflat (task_hash_embedding vector_cosine_ops)
                    WITH (lists = 100);
                """)
                
                # Create index on context_signature for exact matching
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_browser_fast_path_context 
                    ON browser_fast_path (context_signature);
                """)
                
                # Create index on created_at for cleanup
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_browser_fast_path_created 
                    ON browser_fast_path (created_at);
                """)
                
                conn.commit()
                logger.info("✅ browser_fast_path table initialized with pgvector index")
                
        except Exception as e:
            logger.error(f"Failed to create browser_fast_path table: {e}")
            raise
    
    def _generate_task_hash_embedding(self, task_hash: str) -> List[float]:
        """
        Generate an embedding for the task hash.
        
        Args:
            task_hash: The UUID string hash of the task
            
        Returns:
            A 1536-dimensional embedding vector
        """
        try:
            # We'll use the task hash as a seed to generate a deterministic embedding
            # by creating a consistent text representation
            embedding_text = f"browser task: {task_hash}"
            embedding_text = embedding_text.replace("\n", " ")
            
            response = embedding(
                model="text-embedding-3-small",
                input=[embedding_text]
            )
            
            # Handle both Object and Dict responses
            data_item = response.data[0]
            if isinstance(data_item, dict):
                return data_item['embedding']
            else:
                return data_item.embedding
                
        except Exception as e:
            logger.error(f"Failed to generate embedding for task hash: {e}")
            # Return a zero vector as fallback
            return [0.0] * 1536
    
    def lookup(
        self, 
        task_intent: str, 
        context_signature: str,
        similarity_threshold: float = 0.85,
        limit: int = 1
    ) -> Optional[Dict[str, Any]]:
        """
        Look up a cached browser task by intent and context.
        
        Args:
            task_intent: The task intent description
            context_signature: The SHA-256 context signature hash
            similarity_threshold: Minimum cosine similarity for a match (0.0-1.0)
            limit: Maximum number of results to return
            
        Returns:
            A dictionary with cached task data, or None if no match found
        """
        try:
            with self.postgres._get_conn() as conn:
                # First, try exact context signature match
                result = conn.execute("""
                    SELECT task_hash, task_intent, context_signature, 
                           element_tree_snapshot, playwright_script, 
                           execution_time_ms, success_rate, created_at
                    FROM browser_fast_path
                    WHERE context_signature = %s
                    ORDER BY success_rate DESC, created_at DESC
                    LIMIT %s
                """, (context_signature, limit)).fetchall()
                
                if result:
                    # Check if we have an embedding for this task_hash
                    cached_row = result[0]
                    task_hash = cached_row[0]
                    
                    # Get the embedding for similarity search
                    embedding_result = conn.execute("""
                        SELECT task_hash_embedding
                        FROM browser_fast_path
                        WHERE task_hash = %s
                    """, (task_hash,)).fetchone()
                    
                    if embedding_result and embedding_result[0]:
                        # Use vector similarity search
                        cached_embedding = embedding_result[0]
                        if isinstance(cached_embedding, str):
                            cached_embedding = [float(x) for x in cached_embedding.strip('[]').split(',')]
                        
                        # Generate query embedding
                        query_embedding = self._generate_task_hash_embedding(str(task_hash))
                        
                        # Calculate cosine similarity
                        similarity = self._cosine_similarity(cached_embedding, query_embedding)
                        
                        if similarity >= similarity_threshold:
                            return {
                                "task_hash": str(cached_row[0]),
                                "task_intent": cached_row[1],
                                "context_signature": cached_row[2],
                                "element_tree_snapshot": cached_row[3],
                                "playwright_script": cached_row[4],
                                "execution_time_ms": cached_row[5],
                                "success_rate": float(cached_row[6]),
                                "created_at": cached_row[7],
                                "similarity": similarity
                            }
                    
                    # If no embedding, return the cached result
                    return {
                        "task_hash": str(cached_row[0]),
                        "task_intent": cached_row[1],
                        "context_signature": cached_row[2],
                        "element_tree_snapshot": cached_row[3],
                        "playwright_script": cached_row[4],
                        "execution_time_ms": cached_row[5],
                        "success_rate": float(cached_row[6]),
                        "created_at": cached_row[7],
                        "similarity": 1.0  # Exact match
                    }
                
                return None
                
        except Exception as e:
            logger.error(f"Failed to lookup cached task: {e}")
            return None
    
    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """
        Calculate cosine similarity between two vectors.
        
        Args:
            vec1: First vector
            vec2: Second vector
            
        Returns:
            Cosine similarity (1.0 = identical, 0.0 = orthogonal, -1.0 = opposite)
        """
        if len(vec1) != len(vec2):
            return 0.0
            
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = sum(a * a for a in vec1) ** 0.5
        norm2 = sum(b * b for b in vec2) ** 0.5
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
            
        return dot_product / (norm1 * norm2)
    
    def record_hit(self, task_hash: str, execution_time_ms: int) -> None:
        """
        Record a cache hit for metrics.
        
        Args:
            task_hash: The UUID hash of the task
            execution_time_ms: The execution time in milliseconds
        """
        try:
            with self.postgres._get_conn() as conn:
                conn.execute("""
                    UPDATE browser_fast_path
                    SET execution_time_ms = %s,
                        created_at = CURRENT_TIMESTAMP  -- Refresh timestamp
                    WHERE task_hash = %s
                """, (execution_time_ms, task_hash))
                conn.commit()
                logger.debug(f"✅ Cache hit recorded for task {task_hash}")
        except Exception as e:
            logger.error(f"Failed to record cache hit: {e}")
    
    def write_back(
        self,
        task_hash: str,
        task_intent: str,
        context_signature: str,
        element_tree_snapshot: Dict[str, Any],
        playwright_script: str,
        success_rate: float = 1.0
    ) -> bool:
        """
        Write a new cached task to the database.
        
        Args:
            task_hash: UUID hash of the task intent
            task_intent: Task intent description
            context_signature: SHA-256 context signature
            element_tree_snapshot: AOM element tree snapshot
            playwright_script: Deterministic Playwright script
            success_rate: Initial success rate (0.0-1.0)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Generate embedding for the task hash
            task_hash_str = str(task_hash)
            task_embedding = self._generate_task_hash_embedding(task_hash_str)
            
            with self.postgres._get_conn() as conn:
                conn.execute("""
                    INSERT INTO browser_fast_path 
                    (task_hash, task_intent, context_signature, element_tree_snapshot, 
                     playwright_script, execution_time_ms, success_rate, created_at, task_hash_embedding)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (task_hash) DO UPDATE SET
                        task_intent = EXCLUDED.task_intent,
                        context_signature = EXCLUDED.context_signature,
                        element_tree_snapshot = EXCLUDED.element_tree_snapshot,
                        playwright_script = EXCLUDED.playwright_script,
                        success_rate = EXCLUDED.success_rate,
                        created_at = CURRENT_TIMESTAMP
                """, (
                    task_hash_str,
                    task_intent,
                    context_signature,
                    json.dumps(element_tree_snapshot),
                    playwright_script,
                    0,  # initial execution_time_ms
                    success_rate,
                    datetime.now(),
                    str(task_embedding)
                ))
                conn.commit()
                logger.info(f"✅ Fast Path cache written for task {task_hash}")
                return True
                
        except Exception as e:
            logger.error(f"Failed to write back to Fast Path cache: {e}")
            return False
    
    def invalidate_old_cache(self, days: int = 30) -> int:
        """
        Invalidate cache entries older than specified days.
        
        Args:
            days: Number of days before cache entry expires
            
        Returns:
            Number of entries invalidated
        """
        try:
            cutoff_date = datetime.now() - timedelta(days=days)
            
            with self.postgres._get_conn() as conn:
                result = conn.execute("""
                    DELETE FROM browser_fast_path
                    WHERE created_at < %s
                    RETURNING task_hash
                """, (cutoff_date,)).fetchall()
                
                invalidated_count = len(result)
                conn.commit()
                logger.info(f"✅ Invalidated {invalidated_count} Fast Path cache entries older than {days} days")
                return invalidated_count
                
        except Exception as e:
            logger.error(f"Failed to invalidate old cache entries: {e}")
            return 0
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get cache performance metrics.
        
        Returns:
            Dictionary with cache statistics
        """
        try:
            with self.postgres._get_conn() as conn:
                # Total cached tasks
                total = conn.execute("""
                    SELECT COUNT(*) FROM browser_fast_path
                """).fetchone()[0]
                
                # Average execution time
                avg_time = conn.execute("""
                    SELECT AVG(execution_time_ms) FROM browser_fast_path
                    WHERE execution_time_ms > 0
                """).fetchone()[0] or 0
                
                # Success rate breakdown
                success_rate = conn.execute("""
                    SELECT AVG(success_rate) FROM browser_fast_path
                """).fetchone()[0] or 0
                
                # Cache entries by age (30 day buckets)
                age_distribution = conn.execute("""
                    SELECT 
                        CASE 
                            WHEN created_at > CURRENT_TIMESTAMP - INTERVAL '7 days' THEN '0-7 days'
                            WHEN created_at > CURRENT_TIMESTAMP - INTERVAL '14 days' THEN '7-14 days'
                            WHEN created_at > CURRENT_TIMESTAMP - INTERVAL '30 days' THEN '14-30 days'
                            ELSE '30+ days'
                        END as age_bucket,
                        COUNT(*) as count
                    FROM browser_fast_path
                    GROUP BY age_bucket
                    ORDER BY age_bucket
                """).fetchall()
                
                return {
                    "total_cached_tasks": total,
                    "average_execution_time_ms": avg_time,
                    "average_success_rate": success_rate,
                    "age_distribution": {row[0]: row[1] for row in age_distribution}
                }
                
        except Exception as e:
            logger.error(f"Failed to get cache metrics: {e}")
            return {}


class PostgresMemory(MemoryProvider):
    def _get_conn(self):
        """Get a database connection."""
        return psycopg.connect(self.conn_str)
    
    def _scrub_secrets(self, text: str) -> str:
        """
        Scrub all secret values from the text.
        
        Retrieves active secrets from the VaultManager and replaces any
        plaintext instances with [REDACTED_SECRET].
        
        Args:
            text: The input text that may contain secret values
            
        Returns:
            The text with all secret values replaced by [REDACTED_SECRET]
        """
        # Get vault manager instance
        vault_mgr = VaultManager()
        
        # Try to unlock vault with master key if available
        master_key = os.getenv("COBALT_MASTER_KEY")
        if master_key:
            vault_mgr.unlock(master_key)
        
        # Get all secrets from vault
        secrets_to_scrub = []
        if vault_mgr._is_unlocked:
            for secret_name in vault_mgr.list_secrets():
                secret_value = vault_mgr.get_secret(secret_name)
                if secret_value:
                    secrets_to_scrub.append(secret_value)
        
        # Also check config for any API keys that might be loaded
        try:
            config = get_config()
            # Check keys section for any secret values
            if hasattr(config, 'keys') and config.keys:
                for key_name, key_value in config.keys.items():
                    if key_value and isinstance(key_value, str):
                        secrets_to_scrub.append(key_value)
        except Exception:
            # If we can't access config, continue without it
            pass
        
        # Replace all secret values with redacted marker
        result = text
        for secret in secrets_to_scrub:
            if secret:
                result = result.replace(secret, "[REDACTED_SECRET]")
        
        return result
    
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
        
        # Initialize Fast Path Cache manager
        self.fast_path_cache = FastPathCache(self)
    
    def _init_graph_tables(self) -> None:
        """Initialize graph database tables (graph_nodes and graph_edges)."""
        try:
            with self._get_conn() as conn:
                # Create graph_nodes table
                # Unique constraint on (entity_type, name) prevents duplicate entities
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS graph_nodes (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        entity_type VARCHAR(255) NOT NULL,
                        name VARCHAR(255) NOT NULL,
                        properties JSONB DEFAULT '{}'::jsonb,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(entity_type, name)
                    );
                """)
                
                # Create graph_edges table
                # Foreign keys with ON DELETE CASCADE ensures orphan edges are removed
                # Unique constraint on (source_id, target_id, relationship) prevents duplicate edges
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS graph_edges (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        source_id UUID NOT NULL REFERENCES graph_nodes(id) ON DELETE CASCADE,
                        target_id UUID NOT NULL REFERENCES graph_nodes(id) ON DELETE CASCADE,
                        relationship VARCHAR(255) NOT NULL,
                        properties JSONB DEFAULT '{}'::jsonb,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(source_id, target_id, relationship)
                    );
                """)
                
                # Create indexes for performance
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_graph_nodes_entity_type_name 
                    ON graph_nodes (entity_type, name);
                """)
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_graph_edges_source 
                    ON graph_edges (source_id);
                """)
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_graph_edges_target 
                    ON graph_edges (target_id);
                """)
                
                conn.commit()
                logger.info("🧠 Graph database tables initialized (graph_nodes, graph_edges)")
        except Exception as e:
            logger.error(f"Failed to init graph tables: {e}")
            raise
    
    def _init_hitl_tables(self) -> None:
        """Initialize HITL (Human-in-the-Loop) database tables for pending approvals."""
        try:
            with self._get_conn() as conn:
                # Create hitl_proposals table
                # Stores pending approvals in persistent Postgres DB instead of RAM
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS hitl_proposals (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        status VARCHAR(50) NOT NULL DEFAULT 'pending',  -- 'pending', 'approved', 'rejected'
                        tool_name VARCHAR(255) NOT NULL,
                        tool_kwargs JSONB NOT NULL DEFAULT '{}'::jsonb,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                
                # Create indexes for performance
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_hitl_proposals_status 
                    ON hitl_proposals (status);
                """)
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_hitl_proposals_created_at 
                    ON hitl_proposals (created_at);
                """)
                conn.execute("""
                    CREATE INDEX IF NOT EXISTS idx_hitl_proposals_status_created 
                    ON hitl_proposals (status, created_at);
                """)
                
                conn.commit()
                logger.info("🧠 HITL proposals table initialized (hitl_proposals)")
        except Exception as e:
            logger.error(f"Failed to init HITL tables: {e}")
            raise
    
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
        
        # Initialize graph tables
        self._init_graph_tables()
        
        # Initialize HITL tables
        self._init_hitl_tables()

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
        Scrubs secrets from the message before storing or generating embeddings.
        """
        # Scrub secrets from the message BEFORE processing
        scrubbed_message = self._scrub_secrets(message)
        
        # Generate Vector from scrubbed content
        vector = self._generate_embedding(scrubbed_message)
        
        if not data:
            data = {}
            
        try:
            with self._get_conn() as conn:
                if vector:
                    conn.execute(
                        f"INSERT INTO {self.table_name} (source, content, embedding, metadata) VALUES (%s, %s, %s, %s)",
                        (source, scrubbed_message, str(vector), json.dumps(data))
                    )
                else:
                    # Fallback (save without vector if embedding fails)
                    conn.execute(
                        f"INSERT INTO {self.table_name} (source, content, metadata) VALUES (%s, %s, %s)",
                        (source, scrubbed_message, json.dumps(data))
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

    def close(self) -> None:
        """Close the database connection (no-op for connection-per-operation pattern)."""
        # Since we create new connections for each operation via _get_conn(),
        # there's no persistent connection to close. This method exists for
        # API consistency with context manager patterns.
        pass

    def __enter__(self):
        """Context manager entry - returns self."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - calls close."""
        self.close()
        return False

    # ===== GRAPH DATABASE CRUD OPERATIONS =====

    def upsert_node(self, entity_type: str, name: str, properties: Dict[str, Any] = None) -> str:
        """
        Insert or update a graph node.
        
        Args:
            entity_type: The type of entity (e.g., 'Ticker', 'Material', 'Strategy')
            name: The unique name of the entity (e.g., 'TSLA', 'Cellulose')
            properties: Optional JSONB properties dictionary
            
        Returns:
            The UUID of the node (as a string)
        """
        try:
            timestamp = datetime.now()
            
            with self._get_conn() as conn:
                # First try to get the existing node by entity_type + name
                existing = conn.execute("""
                    SELECT id FROM graph_nodes
                    WHERE entity_type = %s AND name = %s
                """, (entity_type, name)).fetchone()
                
                if existing:
                    # Node exists, update it
                    existing_id = str(existing[0])
                    conn.execute("""
                        UPDATE graph_nodes
                        SET properties = %s,
                            updated_at = %s
                        WHERE id = %s
                    """, (json.dumps(properties) if properties else '{}', timestamp, existing_id))
                    conn.commit()
                    return existing_id
                else:
                    # Node doesn't exist, insert it
                    node_id = str(uuid.uuid4())
                    conn.execute("""
                        INSERT INTO graph_nodes (id, entity_type, name, properties, created_at, updated_at)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        node_id,
                        entity_type,
                        name,
                        json.dumps(properties) if properties else '{}',
                        timestamp,
                        timestamp
                    ))
                    conn.commit()
                    return node_id
        except Exception as e:
            logger.error(f"Failed to upsert node: {e}")
            raise

    def upsert_edge(self, source_id: str, target_id: str, relationship: str, properties: Dict[str, Any] = None) -> str:
        """
        Insert or update a graph edge.
        
        Args:
            source_id: UUID of the source node
            target_id: UUID of the target node
            relationship: The type of relationship (e.g., 'TRIGGERED_STRATEGY', 'IS_USED_IN')
            properties: Optional JSONB properties dictionary
            
        Returns:
            The UUID of the edge (as a string)
        """
        try:
            timestamp = datetime.now()
            
            with self._get_conn() as conn:
                # First try to get the existing edge
                existing = conn.execute("""
                    SELECT id FROM graph_edges
                    WHERE source_id = %s AND target_id = %s AND relationship = %s
                """, (source_id, target_id, relationship)).fetchone()
                
                if existing:
                    # Edge exists, update it
                    existing_id = str(existing[0])
                    conn.execute("""
                        UPDATE graph_edges
                        SET properties = %s,
                            created_at = %s
                        WHERE id = %s
                    """, (json.dumps(properties) if properties else '{}', timestamp, existing_id))
                    conn.commit()
                    return existing_id
                else:
                    # Edge doesn't exist, insert it
                    edge_id = str(uuid.uuid4())
                    conn.execute("""
                        INSERT INTO graph_edges (id, source_id, target_id, relationship, properties, created_at)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        edge_id,
                        source_id,
                        target_id,
                        relationship,
                        json.dumps(properties) if properties else '{}',
                        timestamp
                    ))
                    conn.commit()
                    return edge_id
        except Exception as e:
            logger.error(f"Failed to upsert edge: {e}")
            raise

    def get_node(self, entity_type: str, name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a node by entity type and name.
        
        Args:
            entity_type: The type of entity
            name: The unique name of the entity
            
        Returns:
            Dictionary with node data, or None if not found
        """
        try:
            with self._get_conn() as conn:
                result = conn.execute("""
                    SELECT id, entity_type, name, properties, created_at, updated_at
                    FROM graph_nodes
                    WHERE entity_type = %s AND name = %s
                """, (entity_type, name)).fetchone()
                
                if result:
                    return {
                        "id": str(result[0]),
                        "entity_type": result[1],
                        "name": result[2],
                        "properties": result[3] if isinstance(result[3], dict) else json.loads(result[3]),
                        "created_at": result[4],
                        "updated_at": result[5]
                    }
                return None
        except Exception as e:
            logger.error(f"Failed to get node: {e}")
            return None

    def get_edges(self, node_id: str, direction: str = 'both') -> List[Dict[str, Any]]:
        """
        Retrieve edges connected to a node.
        
        Args:
            node_id: UUID of the node
            direction: 'out' for outgoing (source), 'in' for incoming (target), 'both' for both
            
        Returns:
            List of dictionaries with edge data
        """
        try:
            with self._get_conn() as conn:
                if direction == 'out':
                    # Edges where node is source
                    results = conn.execute("""
                        SELECT id, source_id, target_id, relationship, properties, created_at
                        FROM graph_edges
                        WHERE source_id = %s
                    """, (node_id,)).fetchall()
                elif direction == 'in':
                    # Edges where node is target
                    results = conn.execute("""
                        SELECT id, source_id, target_id, relationship, properties, created_at
                        FROM graph_edges
                        WHERE target_id = %s
                    """, (node_id,)).fetchall()
                else:  # 'both'
                    # Edges where node is either source or target
                    results = conn.execute("""
                        SELECT id, source_id, target_id, relationship, properties, created_at
                        FROM graph_edges
                        WHERE source_id = %s OR target_id = %s
                    """, (node_id, node_id)).fetchall()
                
                edges = []
                for row in results:
                    edges.append({
                        "id": str(row[0]),
                        "source_id": str(row[1]),
                        "target_id": str(row[2]),
                        "relationship": row[3],
                        "properties": row[4] if isinstance(row[4], dict) else json.loads(row[4]),
                        "created_at": row[5]
                    })
                return edges
        except Exception as e:
            logger.error(f"Failed to get edges: {e}")
            return []